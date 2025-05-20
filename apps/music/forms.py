from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra
from apps.common.models import Person, ImageSize
from core.utils.validators import validate_file_extension, ALLOWED_AUDIO_EXTENSIONS, ALLOWED_IMAGE_EXTENSIONS, validate_url
from core.utils.utils import normalize_text
# Create your forms here.
########################################################################################################    Formulario para Album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'album_type', 'release_date', 'is_active']

    title = forms.CharField(
        required=True,
        strip=True,
        max_length=255,
        label=_('Título'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Título del álbum'),
                'id': 'title',
                'type': 'text',
                'autocomplete': 'off',
                'required': 'required'
            }
        ),
        error_messages={
            'required': _('Debe ingresar el título del álbum.'),
            'max_length': _('El título excede el largo permitido.'),
        }
    )

    artist = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Artista'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'artist',
                'required': 'required'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un artista.'),
        }
    )

    album_type = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Tipo'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'album_type',
                'required': 'required'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un tipo de álbum.'),
        }
    )

    release_date = forms.DateField(
        required=False,
        label=_('Fecha Lanzamiento'),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'release_date',
                'autocomplete': 'off',
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar el álbum.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['artist'].queryset = Artist.objects.filter(is_active=True)
        self.fields['album_type'].queryset = AlbumType.objects.filter(is_active=True)

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        return ' '.join(word.capitalize() for word in title.split())

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        artist = cleaned_data.get('artist')
        album_type = cleaned_data.get('album_type')

        if title and artist and album_type:
            normalized_title = normalize_text(title)
            existing_albums = Album.objects.exclude(pk=self.instance.pk if self.instance else None)
            for album in existing_albums.filter(artist=artist, album_type=album_type):
                if normalize_text(album.title) == normalized_title:
                    raise forms.ValidationError(
                        _('Ya existe un álbum con este título para el mismo artista y tipo.')
                    )
        return cleaned_data

########################################################################################################    Formulario para AlbumImage
class AlbumImageForm(forms.ModelForm):
    class Meta:
        model = AlbumImage
        fields = ['album', 'size_image', 'image', 'image_url', 'is_active']

    album = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Álbum'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'album'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una álbum.'),
        },
    )

    size_image = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Tamaño de Imagen'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'size_image'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un tamaño de imagen.'),
        },
    )

    image = forms.ImageField(
        required=True,
        label=_('Imagen'),
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'image'
            }
        ),
        error_messages={
            'required': _('Debe subir una imagen.'),
            'invalid': _('El archivo seleccionado no es válido.'),
        },
    )

    image_url = forms.CharField(
        required=False,
        max_length= 2000,
        label='URL',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL de la imagen (opcional)'),
                'id': 'image_url',
                'autocomplete': 'off',
                'type': 'url',
            }
        ),
        error_messages={
            'max_length': _('La URL excede el largo permitido.'),
        },
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen de la álbum.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['album'].disabled = True
            self.fields['size_image'].disabled = True

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_file_extension(image, ALLOWED_IMAGE_EXTENSIONS)
        return image

    def clean_image_url(self):
        url = self.cleaned_data.get('image_url', '').strip()
        return validate_url(url)

    def clean(self):
        cleaned_data = super().clean()

        # Si ya hay errores en 'image' o 'image_url', no continuar validación general
        if self.errors.get('image') or self.errors.get('image_url'):
            return cleaned_data

        image = cleaned_data.get('image')
        image_url = cleaned_data.get('image_url')

        if not image and not image_url:
            raise forms.ValidationError(_('Debe subir una imagen o proporcionar una URL.'))

        return cleaned_data

########################################################################################################    Formulario para AlbumImageExtra
class AlbumImageExtraForm(forms.ModelForm):
    class Meta:
        model = AlbumImageExtra
        fields = ['album', 'image', 'is_active']

    album = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label='Álbum',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'album'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una álbum.'),
        },
    )

    image = forms.ImageField(
        required=True,
        label='Imagen Extra',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'image'
            }
        ),
        error_messages={
            'required': _('Debe subir una imagen.'),
            'invalid': _('El archivo seleccionado no es válido.'),
        },
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional de la álbum.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['album'].disabled = True

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_file_extension(image, ALLOWED_IMAGE_EXTENSIONS)
        return image

    def clean(self):
        cleaned_data = super().clean()

        # Si ya hay errores en 'image', no continuar validación general
        if self.errors.get('image'):
            return cleaned_data

        image = cleaned_data.get('image')
        if not image:
            raise forms.ValidationError(_('Debe subir una imagen.'))

        return cleaned_data

########################################################################################################    Formulario para AlbumType
class AlbumTypeForm(forms.ModelForm):
    class Meta:
        model = AlbumType
        fields = ['name', 'name_esp', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre'),
                'id': 'name',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del tipo.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=50,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre Español'),
                'id': 'name_esp',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        max_length=2500,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción'),
                'id': 'description',
                'rows': 3,
            }
        ),
        error_messages={
            'max_length': _('La descripción excede lo permitido.'),
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar el tipo de álbum.'),
            }
        )
    )


    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.capitalize() for part in name.split())

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip()
        return ' '.join(part.capitalize() for part in name_esp.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = ''.join(name.lower().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.lower().split()) if name_esp else ''

        ModelClass = AlbumType if isinstance(self, AlbumTypeForm) else ArtistType
        existing = ModelClass.objects.exclude(pk=self.instance.pk if self.instance else None)

        for obj in existing:
            if normalized_name == ''.join(obj.name.lower().split()):
                raise forms.ValidationError(_('Ya existe un tipo con el nombre "%(name)s".') % {'name': name})
            if obj.name_esp and normalized_name_esp == ''.join(obj.name_esp.lower().split()):
                raise forms.ValidationError(_('Ya existe un tipo con el nombre en español "%(name_esp)s".') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Artist
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'biography', 'start_year', 'year_end', 'artist_type', 'genre', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=150,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del Artista'),
                'id': 'name',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del artista.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    biography = forms.CharField(
        required=False,
        strip=True,
        label=_('Biografía'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Biografía del artista'),
                'id': 'biography',
                'rows': 3,
            }
        ),
    )

    start_year = forms.IntegerField(
        required=False,
        label=_('Año inicio'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Año inicio'),
                'id': 'start_year',
            }
        ),
    )

    year_end = forms.IntegerField(
        required=False,
        label=_('Año término'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Año término'),
                'id': 'year_end',
            }
        ),
    )

    artist_type = forms.ModelChoiceField(
        queryset=None,
        label=_('Tipo Artista'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'artist_type',
            }
        )
    )

    genre = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Géneros'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'genre',
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar al artista.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['genre'].queryset = Genre.objects.filter(is_active=True)
        self.fields['artist_type'].queryset = ArtistType.objects.filter(is_active=True)

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(word.capitalize() for word in name.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '').strip()
        start_year = cleaned_data.get('start_year')
        year_end = cleaned_data.get('year_end')

        # Validación año fin no menor al inicio
        if start_year and year_end and year_end < start_year:
            self.add_error('year_end', _('El año de término no puede ser menor al de inicio.'))

        # Validación unicidad por nombre + inicial
        normalized_name = ''.join(name.lower().split())
        initial = normalized_name[0] if normalized_name else ''

        existing_artists = Artist.objects.exclude(pk=self.instance.pk if self.instance else None)
        for artist in existing_artists:
            existing_name = ''.join(artist.name.lower().split())
            if normalized_name == existing_name and initial == artist.initial.lower():
                raise forms.ValidationError(_('Ya existe un artista con el mismo nombre y la misma inicial.'))

        return cleaned_data

########################################################################################################    Formulario para ArtistImage
class ArtistImageForm(forms.ModelForm):
    class Meta:
        model = ArtistImage
        fields = ['artist', 'size_image', 'image', 'image_url', 'is_active']

    artist = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Artista'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'artist'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una artista.'),
        },
    )

    size_image = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Tamaño de Imagen'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'size_image'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un tamaño de imagen.'),
        },
    )

    image = forms.ImageField(
        required=True,
        label=_('Imagen'),
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'image'
            }
        ),
        error_messages={
            'required': _('Debe subir una imagen.'),
            'invalid': _('El archivo seleccionado no es válido.'),
        },
    )

    image_url = forms.CharField(
        required=False,
        max_length= 2000,
        label='URL',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL de la imagen (opcional)'),
                'id': 'image_url',
                'autocomplete': 'off',
                'type': 'url',
            }
        ),
        error_messages={
            'max_length': _('La URL excede el largo permitido.'),
        },
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen de la álbum.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist'].queryset = Artist.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['artist'].disabled = True
            self.fields['size_image'].disabled = True

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_file_extension(image, ALLOWED_IMAGE_EXTENSIONS)
        return image

    def clean_image_url(self):
        url = self.cleaned_data.get('image_url', '').strip()
        return validate_url(url)

    def clean(self):
        cleaned_data = super().clean()

        # Si ya hay errores en 'image' o 'image_url', no continuar validación general
        if self.errors.get('image') or self.errors.get('image_url'):
            return cleaned_data

        image = cleaned_data.get('image')
        image_url = cleaned_data.get('image_url')

        if not image and not image_url:
            raise forms.ValidationError(_('Debe subir una imagen o proporcionar una URL.'))

        return cleaned_data

########################################################################################################    Formulario para ArtistImageExtra
class ArtistImageExtraForm(forms.ModelForm):
    class Meta:
        model = ArtistImageExtra
        fields = ['artist', 'image', 'is_active']

    artist = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label='Álbum',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'artist'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una álbum.'),
        },
    )

    image = forms.ImageField(
        required=True,
        label='Imagen Extra',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'image'
            }
        ),
        error_messages={
            'required': _('Debe subir una imagen.'),
            'invalid': _('El archivo seleccionado no es válido.'),
        },
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional de la álbum.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist'].queryset = Artist.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['artist'].disabled = True

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_file_extension(image, ALLOWED_IMAGE_EXTENSIONS)
        return image

    def clean(self):
        cleaned_data = super().clean()

        # Si ya hay errores en 'image', no continuar validación general
        if self.errors.get('image'):
            return cleaned_data

        image = cleaned_data.get('image')
        if not image:
            raise forms.ValidationError(_('Debe subir una imagen.'))

        return cleaned_data

########################################################################################################    Formulario para ArtistMember
class ArtistMemberForm(forms.ModelForm):
    class Meta:
        model = ArtistMember
        fields = ['artist', 'person', 'role', 'join_date', 'leave_date', 'is_active']

    artist = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Artista'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'artist'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un artista.'),
        }
    )

    person = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Persona'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una persona.'),
        }
    )

    role = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Rol'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'role'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un rol.'),
        }
    )

    join_date = forms.DateField(
        required=False,
        label=_('Fecha Ingreso'),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
            'class': 'form-control',
            'type': 'date',
            'id': 'join_date'
        }),
    )

    leave_date = forms.DateField(
        required=False,
        label=_('Fecha Salida'),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
            'class': 'form-control',
            'type': 'date',
            'id': 'leave_date'
        }),
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la membresia del artista.'),
            }
        )
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['artist'].queryset = Artist.objects.filter(is_active=True)
        self.fields['person'].queryset = Person.objects.filter(is_active=True)
        self.fields['role'].queryset = Role.objects.filter(is_active=True)

    def clean(self):
        cleaned_data = super().clean()
        artist = cleaned_data.get('artist')
        person = cleaned_data.get('person')
        role = cleaned_data.get('role')
        join_date = cleaned_data.get('join_date')
        leave_date = cleaned_data.get('leave_date')

        # Validar fecha de salida posterior a la de ingreso
        if join_date and leave_date and leave_date < join_date:
            self.add_error('leave_date', _('La fecha de salida no puede ser anterior a la de ingreso.'))

        # Validar duplicado de combinación única
        if artist and person and role:
            exists = ArtistMember.objects.exclude(pk=self.instance.pk if self.instance else None).filter(artist=artist, person=person, role=role).exists()
            if exists:
                raise forms.ValidationError(_('Ya existe un registro para esta combinación de artista, persona y rol.'))

        return cleaned_data

########################################################################################################    Formulario para ArtistType
class ArtistTypeForm(forms.ModelForm):
    class Meta:
        model = ArtistType
        fields = ['name', 'name_esp', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre'),
                'id': 'name',
                'type': 'text',
                'autocomplete': 'off',
                'required': 'required'
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del tipo de artista.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=50,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre Español'),
                'id': 'name_esp',
                'type': 'text',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        max_length=2500,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del tipo de artista'),
                'id': 'description',
                'autocomplete': 'off',
                'rows': 3,
            }
        ),
        error_messages={
            'max_length': _('La descripción excede lo permitido.'),
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar el tipo de artista.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.capitalize() for part in name.split())

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip()
        return ' '.join(part.capitalize() for part in name_esp.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = ''.join(name.lower().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.lower().split()) if name_esp else ''

        existing_types = ArtistType.objects.exclude(pk=self.instance.pk if self.instance else None)

        for atype in existing_types:
            if normalized_name and ''.join(atype.name.lower().split()) == normalized_name:
                raise forms.ValidationError(
                    _('Ya existe un tipo de artista con el nombre "%(name)s" o uno muy similar.') % {'name': name}
                )

            if name_esp and atype.name_esp:
                if ''.join(atype.name_esp.lower().split()) == normalized_name_esp:
                    raise forms.ValidationError(
                        _('Ya existe un tipo de artista con el nombre en español "%(name_esp)s" o uno muy similar.') % {'name_esp': name_esp}
                    )

        return cleaned_data

########################################################################################################    Formulario para Genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['parent', 'name', 'name_esp', 'description', 'is_active']

    parent = forms.ModelChoiceField(
        queryset=None,
        required=False,
        label=_('Padre'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'parent'
            }
        ),
    )

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=40,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre'),
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del género.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=40,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre Español'),
                'id': 'name_esp',
                'type': 'text',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        max_length=250,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del Género'),
                'id': 'description',
                'autocomplete': 'off',
                'rows': 3,
            }
        ),
        error_messages={
            'max_length': _('La descripción del género excede lo permitido.'),
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar el género.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Genre.objects.filter(is_active=True)

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.capitalize() for part in name.split())

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip()
        return ' '.join(part.capitalize() for part in name_esp.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        # Normaliza los nombres eliminando espacios y convirtiendo a minúsculas
        normalized_name = ''.join(name.lower().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.lower().split()) if name_esp else ''

        # Verifica si un género con el nombre normalizado ya existe, ignorando el caso actual
        if normalized_name:
            existing_genres = Genre.objects.exclude(pk=self.instance.pk if self.instance else None)
            for genre in existing_genres:
                existing_normalized_name = ''.join(genre.name.lower().split())
                if normalized_name == existing_normalized_name:
                    raise forms.ValidationError(_('Ya existe un género con el nombre "%(name)s" o es muy similar.') % {'name': name})

        # Verifica si un género con el nombre en español normalizado ya existe, ignorando el caso actual
        if normalized_name_esp:
            existing_genres = Genre.objects.exclude(pk=self.instance.pk if self.instance else None)
            for genre in existing_genres:
                existing_normalized_name_esp = ''.join(genre.name_esp.lower().split())
                if normalized_name_esp == existing_normalized_name_esp:
                    raise forms.ValidationError(_('Ya existe un género con el nombre en español "%(name_esp)s" o es muy similar.') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Role
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'name_esp', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=30,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre'),
                'id': 'name',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del rol.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=30,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre Español'),
                'id': 'name_esp',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar el rol.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.capitalize() for part in name.split())

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip()
        return ' '.join(part.capitalize() for part in name_esp.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = ''.join(name.lower().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.lower().split()) if name_esp else ''

        existing_roles = Role.objects.exclude(pk=self.instance.pk if self.instance else None)

        for role in existing_roles:
            if normalized_name == ''.join(role.name.lower().split()):
                raise forms.ValidationError(_('Ya existe un rol con el nombre "%(name)s".') % {'name': name})
            if role.name_esp and normalized_name_esp == ''.join(role.name_esp.lower().split()):
                raise forms.ValidationError(_('Ya existe un rol con el nombre en español "%(name_esp)s".') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Song
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'lyrics', 'release_date', 'album_song_id', 'audio_file', 'is_active']

    title = forms.CharField(
        required=True,
        strip=True,
        max_length=255,
        label=_('Título'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Título de la canción'),
                'id': 'title',
                'type': 'text',
                'autocomplete': 'off',
                'required': 'required',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el título de la canción.'),
            'max_length': _('El título excede el largo permitido.'),
        }
    )

    album = forms.ModelChoiceField(
        queryset=Album.objects.filter(is_active=True),
        required=True,
        label=_('Álbum'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'album',
                'required': 'required',
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un álbum para la canción.'),
        }
    )

    lyrics = forms.CharField(
        required=False,
        strip=True,
        label=_('Letra'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Letra de la canción'),
                'id': 'lyrics',
                'rows': 4,
                'autocomplete': 'off',
            }
        ),
    )

    album_song_id = forms.IntegerField(
        required=False,
        min_value=0,
        label=_('ID Canción Álbum'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Orden en el álbum'),
                'id': 'album_song_id',
            }
        )
    )

    release_date = forms.DateField(
        required=False,
        label=_('Fecha Lanzamiento'),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'release_date',
                'autocomplete': 'off',
            }
        )
    )

    audio_file = forms.FileField(
        required=False,
        label=_('Archivo Audio'),
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'audio_file',
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la canción.'),
            }
        )
    )

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        return ' '.join(word.capitalize() for word in title.split())

    def clean_audio_file(self):
        audio_file = self.cleaned_data.get('audio_file')
        if audio_file:
            validate_file_extension(audio_file, ALLOWED_AUDIO_EXTENSIONS)
        return audio_file

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        album = cleaned_data.get('album')
        album_song_id = cleaned_data.get('album_song_id')

        if title and album:
            normalized_title = ''.join(title.lower().split())
            existing_songs = Song.objects.exclude(pk=self.instance.pk if self.instance else None)
            for song in existing_songs.filter(album=album, album_song_id=album_song_id):
                if ''.join(song.title.lower().split()) == normalized_title:
                    raise forms.ValidationError(
                        _('Ya existe una canción con este título y número en el álbum seleccionado.')
                    )
        return cleaned_data