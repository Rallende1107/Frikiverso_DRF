from django import forms
from .models import(Company, Genre, Serie, SerieCast, SerieImage, SerieImageExtra, SerieStaff, Rating, Role, TitleSerie, Type,)
from django.forms.widgets import DateInput
from core.utils.validators import validate_file_extension, validate_url, ALLOWED_IMAGE_EXTENSIONS
from django.utils.translation import gettext_lazy as _
from apps.common.models import ImageSize, Person, Language
from core.utils.utils import to_title_text, normalize_text

# Create your forms here.
########################################################################################################    Formulario para Genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['parent', 'name', 'name_esp', 'description', 'explicit', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del género'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del género.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=50,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del género en español'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name_esp'
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        },
    )

    parent = forms.ModelChoiceField(
        queryset=None,
        required=False,
        label=_('Padre'),
        empty_label=_('Seleccione un género padre'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'parent',
            }
        ),
    )

    description = forms.CharField(
        required=False,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del género'),
                'rows': 3,
                'id': 'description',
            }
        ),
    )

    explicit = forms.BooleanField(
        required=False,
        label=_('Explícito'),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'explicit',
                'title': _('Marcar si el género es explícito'),
            }
        ),
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
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Genre.objects.filter(is_active=True).exclude(pk=self.instance.pk if self.instance else None)


    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean_name_esp(self):
        return to_title_text(self.cleaned_data.get('name_esp', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')
        parent = cleaned_data.get('parent')

        normalized_name = normalize_text(name) if name else ''
        normalized_name_esp = normalize_text(name_esp) if name_esp else ''

        qs = Genre.objects.exclude(pk=self.instance.pk if self.instance else None)

        for genre in qs:
            if normalize_text(genre.name) == normalized_name:
                raise forms.ValidationError(_('Ya existe un género con el nombre "%(name)s" o es muy similar.') % {'name': name})

            if name_esp and normalize_text(genre.name_esp) == normalized_name_esp:
                raise forms.ValidationError(_('Ya existe un género con el nombre en español "%(name_esp)s" o es muy similar.') % {'name_esp': name_esp})

            if parent and parent.pk == self.instance.pk:
                self.add_error('parent', _('Un género no puede ser su propio padre.'))

        return cleaned_data

########################################################################################################    Formulario para Serie
class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = [
            'title', 'title_secundary', 'release_year', 'duration_minutes', 'synopsis',
            'serie_types', 'serie_rating', 'genres', 'producers', 'distributors', 'is_active'
        ]

    title = forms.CharField(
        required=True,
        max_length=255,
        strip=True,
        label=_('Título Original'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Título original de la serie'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'title'
            }
        ),
        error_messages={
            'required': _('Debe ingresar el título original de la serie.'),
            'max_length': _('El título excede el largo permitido.'),
        },
    )

    title_secundary = forms.CharField(
        required=False,
        max_length=255,
        strip=True,
        label=_('Título Secundario'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Título secundario de la serie'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'title_secundary'
            }
        ),
        error_messages={
            'max_length': _('El título secundario excede el largo permitido.'),
        },
    )

    synopsis = forms.CharField(
        required=False,
        label=_('Sinopsis'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Sinopsis de la serie'),
                'rows': 4,
                'id': 'synopsis'
            }
        ),
    )

    release_year = forms.IntegerField(
        required=False,
        min_value=0,
        label=_('Año Lanzamiento'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Año de lanzamiento'),
                'type': 'number',
                'id': 'release_year'
            }
        ),
        error_messages={
            'min_value': _('El año de lanzamiento no puede ser menor a 0.'),
            'invalid': _('Ingrese un número válido para el año de lanzamiento.'),
        },
    )

    duration_minutes = forms.IntegerField(
        required=False,
        min_value=0,
        initial=0,
        label=_('Duración Minutos'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Duración en minutos'),
                'type': 'number',
                'id': 'duration_minutes'
            }
        ),
        error_messages={
            'min_value': _('La duración no puede ser menor a 0.'),
            'invalid': _('Ingrese un número válido para la duración.'),
        },
    )

    serie_types = forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label=_('Seleccione un tipo de serie'),
        label=_('Tipo Serie'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'serie_types',
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un tipo de serie.'),
        },
    )

    serie_rating = forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label=_('Seleccione una clasificación'),
        label=_('Clasificación Serie'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'serie_rating',
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una clasificación.'),
        },
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Géneros'),
        # empty_label=_('Seleccione un género'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'genres',
                'size': 6,
            }
        ),
    )

    producers = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Productoras'),
        # empty_label=_('Seleccione una productora'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'producers',
                'size': 6,
            }
        ),
    )

    distributors = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Distribuidoras'),
        # empty_label=_('Seleccione una distribuidora'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'distributors',
                'size': 6,
            }
        ),
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la serie.'),
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['serie_types'].queryset = Type.objects.filter(is_active=True)
        self.fields['serie_rating'].queryset = Rating.objects.filter(is_active=True)
        self.fields['genres'].queryset = Genre.objects.filter(is_active=True)
        self.fields['producers'].queryset = Company.objects.filter(is_active=True)
        self.fields['distributors'].queryset = Company.objects.filter(is_active=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        title_secundary = cleaned_data.get('title_secundary')
        release_year = cleaned_data.get('release_year')

        normalized_title = normalize_text(title) if title else ''
        normalized_title_secundary = normalize_text(title_secundary) if title_secundary else ''

        qs = Serie.objects.exclude(pk=self.instance.pk if self.instance else None)

        for serie in qs:
            # Validar que no exista serie con misma combinación título, título secundario y año
            if (normalize_text(serie.title) == normalized_title and normalize_text(serie.title_secundary or '') == normalized_title_secundary and serie.release_year == release_year):
                raise forms.ValidationError(_('Ya existe una serie con el mismo título, título secundario y año de lanzamiento.'))

        return cleaned_data

########################################################################################################    Formulario para SerieCast
class SerieCastForm(forms.ModelForm):
    class Meta:
        model = SerieCast
        fields = ['serie', 'actor', 'role', 'character_name', 'is_active']

    serie = forms.ModelChoiceField(
        queryset=Serie.objects.filter(is_active=True),
        required=True,
        label=_('Serie'),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'serie',
        }),
        error_messages={
            'required': _('Debe seleccionar una serie.'),
        }
    )

    actor = forms.ModelChoiceField(
        queryset=Person.objects.filter(is_active=True),
        required=True,
        label=_('Actor'),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'actor',
        }),
        error_messages={
            'required': _('Debe seleccionar un actor.'),
        }
    )

    role = forms.ModelChoiceField(
        queryset=Role.objects.filter(is_active=True, role_cast=True),
        required=True,
        label=_('Rol'),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'role',
        }),
        error_messages={
            'required': _('Debe seleccionar un rol.'),
        }
    )

    character_name = forms.CharField(
        max_length=100,
        required=True,
        label=_('Personaje'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Nombre del personaje'),
            'autocomplete': 'off',
            'type': 'text',
            'id': 'character_name',
        }),
        error_messages={
            'required': _('Debe ingresar el nombre del personaje.'),
            'max_length': _('El nombre del personaje excede el largo permitido.'),
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'is_active',
        }),
        initial=True,
    )

    def clean_character_name(self):
        character_name = self.cleaned_data.get('character_name')
        if character_name:
            return character_name.strip().title()
        return character_name

    def clean(self):
        cleaned_data = super().clean()
        serie = cleaned_data.get('serie')
        actor = cleaned_data.get('actor')
        role = cleaned_data.get('role')
        character_name = cleaned_data.get('character_name')

        if not all([serie, actor, role, character_name]):
            return cleaned_data  # Validaciones por campo

        # Normalizar el nombre del personaje para comparación (sin espacios y mayúsculas)
        normalized_character = normalize_text(character_name)

        # Formatear el character_name para guardarlo correctamente (título)
        cleaned_data['character_name'] = to_title_text(character_name)

        # Buscar duplicados con comparación normalizada
        existing = SerieCast.objects.exclude(pk=self.instance.pk).filter(
            serie=serie,
            actor=actor,
            role=role,
        )

        for cast in existing:
            if normalize_text(cast.character_name) == normalized_character:
                raise forms.ValidationError( _('Ya existe un registro de este actor interpretando a este personaje en esa serie con ese rol.'))

        return cleaned_data

########################################################################################################    Formulario para SerieImage
class SerieImageForm(forms.ModelForm):
    class Meta:
        model = SerieImage
        fields = ['serie', 'size_image', 'image', 'image_url', 'is_active']

    serie = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Serie'),
        empty_label=_('Seleccione una serie'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'serie'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una serie.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen de la serie.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['serie'].queryset = Serie.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['serie'].disabled = True
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

########################################################################################################    Formulario para SerieImageExtra
class SerieImageExtraForm(forms.ModelForm):
    class Meta:
        model = SerieImageExtra
        fields = ['serie', 'image', 'is_active']

    serie = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label='Serie',
        empty_label=_('Seleccione una serie'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'serie'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una serie.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional de la serie.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['serie'].queryset = Serie.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['serie'].disabled = True

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

########################################################################################################    Formulario para SerieStaff
class SerieStaffForm(forms.ModelForm):
    class Meta:
        model = SerieStaff
        fields = ['serie', 'person', 'role', 'is_active']

    serie = forms.ModelChoiceField(
        queryset=Serie.objects.filter(is_active=True),
        label=_('Serie'),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'serie'}),
        required=True,
    )

    person = forms.ModelChoiceField(
        queryset=Person.objects.filter(is_active=True),
        label=_('Persona'),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'person'}),
        required=True,
    )

    role = forms.ModelChoiceField(
        queryset=Role.objects.filter(is_active=True, role_staff=True),
        label=_('Rol'),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'role'}),
        required=True,
    )

    is_active = forms.BooleanField(
        label=_('Activo'),
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        serie = cleaned_data.get('serie')
        person = cleaned_data.get('person')
        role = cleaned_data.get('role')

        if not all([serie, person, role]):
            return cleaned_data

        qs = SerieStaff.objects.exclude(pk=self.instance.pk).filter( serie=serie, person=person, role=role,)

        if qs.exists():
            raise forms.ValidationError( _('Ya existe un registro con esa combinación de serie, persona y rol.'))

        return cleaned_data

########################################################################################################    Formulario para Rating
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['acronym', 'name', 'name_esp', 'is_active']

    acronym = forms.CharField(
        max_length=15,
        label=_('Acrónimo'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'acronym'}),
        required=True,
    )
    name = forms.CharField(
        max_length=60,
        label=_('Nombre'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        required=True,
    )
    name_esp = forms.CharField(
        max_length=60,
        label=_('Nombre Español'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_esp'}),
        required=False,
    )
    is_active = forms.BooleanField(
        label=_('Activo'),
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        acronym = cleaned_data.get('acronym')
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        if not acronym or not name:
            return cleaned_data

        qs = Rating.objects.exclude(pk=self.instance.pk).filter(
            acronym__iexact=acronym,
            name__iexact=name,
        )
        if name_esp:
            qs = qs.filter(name_esp__iexact=name_esp)
        else:
            qs = qs.filter(name_esp__isnull=True)

        if qs.exists():
            raise forms.ValidationError(_('Ya existe una clasificación con esos datos.'))

        return cleaned_data

########################################################################################################    Formulario para Role
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'name_esp', 'description', 'role_staff', 'role_cast', 'is_active']

    name = forms.CharField(
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        required=True,
    )
    name_esp = forms.CharField(
        max_length=50,
        label=_('Nombre Español'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_esp'}),
        required=False,
    )
    description = forms.CharField(
        label=_('Descripción'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'description'}),
        required=False,
    )
    role_staff = forms.BooleanField(
        label=_('Rol Personal'),
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'role_staff'}),
    )
    role_cast = forms.BooleanField(
        label=_('Rol Elenco'),
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'role_cast'}),
    )
    is_active = forms.BooleanField(
        label=_('Activo'),
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')
        role_staff = cleaned_data.get('role_staff')
        role_cast = cleaned_data.get('role_cast')

        if not name:
            return cleaned_data

        qs = Role.objects.exclude(pk=self.instance.pk).filter(
            name__iexact=name,
            role_staff=role_staff,
            role_cast=role_cast
        )
        if name_esp:
            qs = qs.filter(name_esp__iexact=name_esp)
        else:
            qs = qs.filter(name_esp__isnull=True)

        if qs.exists():
            raise forms.ValidationError(_('Ya existe un rol con esos datos.'))

        return cleaned_data

########################################################################################################    Formulario para TitleSerie
class TitleSerieForm(forms.ModelForm):
    class Meta:
        model = TitleSerie
        fields = ['serie', 'title_lang', 'title', 'is_active']

    serie = forms.ModelChoiceField(
        queryset=Serie.objects.filter(is_active=True),
        label=_('Serie'),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'serie'}),
        required=True,
    )
    title_lang = forms.ModelChoiceField(
        queryset=Language.objects.filter(is_active=True),
        label=_('Idioma'),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'title_lang'}),
        required=True,
    )
    title = forms.CharField(
        max_length=255,
        label=_('Título'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
        required=True,
    )
    is_active = forms.BooleanField(
        label=_('Activo'),
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        serie = cleaned_data.get('serie')
        title_lang = cleaned_data.get('title_lang')
        title = cleaned_data.get('title')

        if serie and title_lang and title:
            title = title.strip()

            exists = TitleSerie.objects.exclude(pk=self.instance.pk).filter(
                serie=serie,
                title_lang=title_lang,
                title__iexact=title
            )

            if exists.exists():
                raise forms.ValidationError(
                    _('Ya existe este título para la serie en ese idioma.')
                )

        return cleaned_data

########################################################################################################    Formulario para Type
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['parent', 'name', 'name_esp', 'description', 'is_active']

    parent = forms.ModelChoiceField(
        queryset=Type.objects.filter(is_active=True),
        required=False,
        label=_('Padre'),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'parent'}),
    )
    name = forms.CharField(
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        required=True,
    )
    name_esp = forms.CharField(
        max_length=50,
        label=_('Nombre Español'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name_esp'}),
        required=False,
    )
    description = forms.CharField(
        label=_('Descripción'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'description'}),
        required=False,
    )
    is_active = forms.BooleanField(
        label=_('Activo'),
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        if not name:
            return cleaned_data

        qs = Type.objects.exclude(pk=self.instance.pk).filter(name__iexact=name)
        if name_esp:
            qs = qs.filter(name_esp__iexact=name_esp)
        else:
            qs = qs.filter(name_esp__isnull=True)

        if qs.exists():
            raise forms.ValidationError(_('Ya existe un tipo con ese nombre y nombre español.'))

        return cleaned_data

