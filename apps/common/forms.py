from django import forms
from apps.common.models import Company, Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website
from django.forms.widgets import DateInput
from core.utils.validators import validate_file_extension, validate_url, ALLOWED_IMAGE_EXTENSIONS
from django.utils.translation import gettext_lazy as _
from core.utils.utils import normalize_text, to_title_text, to_upper_text, to_capitalized_sentence
from django.utils.text import slugify

# Create your forms here.

########################################################################################################    Formulario para Company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'country', 'founded_year', 'disolved_year', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=255,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    country = forms.ModelChoiceField(
        queryset=None,
        required=False,
        label=_('País'),
        empty_label=_('Seleccione un país'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'country',
            }
        ),
    )

    founded_year = forms.IntegerField(
        required=False,
        min_value=0,
        label=_('Año Fundación'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Año de fundación'),
                'type': 'number',
                'id': 'founded_year',
            }
        ),
        error_messages={
            'min_value': _('El año de fundacion no puede ser menor a 0.'),
            'invalid': _('Ingrese un número válido para el año de fundación.'),
        },
    )

    disolved_year = forms.IntegerField(
        required=False,
        min_value=0,
        label=_('Año Disolución'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Año de disolución'),
                'type': 'number',
                'id': 'disolved_year',
            }
        ),
        error_messages={
            'min_value': _('El año de disolución no puede ser menor a 0.'),
            'invalid': _('Ingrese un número válido para el año de disolución.'),
        },
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.filter(is_active=True)

    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        country = cleaned_data.get('country')
        founded = cleaned_data.get('founded_year')
        disolved = cleaned_data.get('disolved_year')

        if founded and disolved and disolved < founded:
            self.add_error('disolved_year', _('El año de disolución no puede ser menor al de fundación.'))

        normalized_name = normalize_text(name) if name else ''
        qs = Company.objects.exclude(pk=self.instance.pk)

        for company in qs:
            if company.country == country and normalized_name == normalize_text(company.name):
                raise forms.ValidationError(_('Ya existe una compañía con el nombre "%(name)s" en el país seleccionado o es muy similar.') % {'name': name})

        return cleaned_data

########################################################################################################    Formulario para Country
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'name_esp', 'code', 'numeric_code', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=60,
        label=_('Nombre en Inglés'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del país (inglés)'),
                'autocomplete': 'off',
                'id': 'name',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre en inglés.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    name_esp = forms.CharField(
        required=True,
        strip=True,
        max_length=60,
        label=_('Nombre en Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del país (español)'),
                'autocomplete': 'off',
                'id': 'name_esp',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre en español.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    code = forms.CharField(
        required=False,
        strip=True,
        max_length=4,
        label=_('Código'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Código de país (opcional)'),
                'autocomplete': 'off',
                'id': 'code',
                'type': 'text',
            }
        )
    )

    numeric_code = forms.IntegerField(
        required=True,
        label=_('Código Numérico'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Código numérico del país'),
                'id': 'numeric_code'
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
                'title': _('Marcar para activar o desmarcar para desactivar el país.'),
            }
        )
    )

    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean_name_esp(self):
        return to_title_text(self.cleaned_data.get('name_esp', ''))

    def clean_code(self):
        return to_upper_text(self.cleaned_data.get('code', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        # Validación cruzada para asegurar que no existan duplicados similares
        normalized_name = normalize_text(name) if name else ''
        normalized_name_esp = normalize_text(name_esp) if name_esp else ''

        qs = Country.objects.exclude(pk=self.instance.pk)

        for country in qs:
            if normalize_text(country.name) == normalized_name:
                raise forms.ValidationError(_('Ya existe un país con el nombre "%(name)s" o es muy similar.') % {'name': name})

            if normalize_text(country.name_esp) == normalized_name_esp:
                raise forms.ValidationError(_('Ya existe un país con el nombre en español "%(name_esp)s" o es muy similar.') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Format
class FormatForm(forms.ModelForm):
    class Meta:
        model = Format
        fields = ['name', 'description', 'for_video', 'for_music', 'for_image',
            'for_document', 'for_other', 'is_active'
        ]

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=15,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del Formato'),
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el Nombre del Formato.'),
            'max_length': _('El Nombre del Formato excede lo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción Formato'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del Formato (opcional)'),
                'id': 'description',
                'rows': 3,
                'autocomplete': 'off',
                'type': 'text',
            }
        )
    )

    for_video = forms.BooleanField(
        required=False,
        label=_('Videos'),
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_video',
                'title': _('Marcar si el formato es para Videos.'),
            }
        )
    )

    for_music = forms.BooleanField(
        required=False,
        label=_('Música'),
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_music',
                'title': _('Marcar si el formato es para Música.'),
            }
        )
    )

    for_image = forms.BooleanField(
        required=False,
        label=_('Imágenes'),
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_image',
                'title': _('Marcar si el formato es para Imágenes.'),
            }
        )
    )

    for_document = forms.BooleanField(
        required=False,
        label=_('Documentos'),
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_document',
                'title': _('Marcar si el formato es para Documentos.'),
            }
        )
    )

    for_other = forms.BooleanField(
        required=False,
        label=_('Otros'),
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_other',
                'title': _('Marcar si el formato es para Otros tipos de archivos.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el formato.'),
            }
        )
    )

    def clean_name(self):
        return to_upper_text(self.cleaned_data.get('name', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        normalized_name = normalize_text(name) if name else ''

        if normalized_name:
            existing_formats = Format.objects.exclude(pk=self.instance.pk)
            for format_obj in existing_formats:
                existing_normalized_name = normalize_text(format_obj.name)
                if normalized_name == existing_normalized_name:
                    raise forms.ValidationError(_('Ya existe un Formato con el nombre "%(name)s" o es muy similar.') % {'name': name})

        return cleaned_data

########################################################################################################    Formulario para ImageSize
class ImageSizeForm(forms.ModelForm):
    class Meta:
        model = ImageSize
        fields = ['name', 'name_esp', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=20,
        label=_('Nombre (Inglés)'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del tamaño (inglés)'),
                'autocomplete': 'off',
                'id': 'name',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del tamaño en inglés.'),
            'max_length': _('El nombre en inglés excede el largo permitido.'),
        }
    )

    name_esp = forms.CharField(
        required=True,
        strip=True,
        max_length=20,
        label=_('Nombre (Español)'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del tamaño (español)'),
                'autocomplete': 'off',
                'id': 'name_esp',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del tamaño en español.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el tamaño de imagen.'),
            }
        )
    )

    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean_name_esp(self):
        return to_title_text(self.cleaned_data.get('name_esp', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = normalize_text(name) if name else ''
        normalized_name_esp = normalize_text(name_esp) if name_esp else ''

        qs = ImageSize.objects.exclude(pk=self.instance.pk)

        for size in qs:
            if normalize_text(size.name) == normalized_name:
                raise forms.ValidationError(_('Ya existe un Tamaño de imagen con el nombre "%(name)s" o es muy similar.') % {'name': name})

            if normalize_text(size.name_esp) == normalized_name_esp:
                raise forms.ValidationError(_('Ya existe un Tamaño de imagen con el nombre en español "%(name_esp)s" o es muy similar.') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Language
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'acronym', 'name_esp', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=20,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del Idioma'),
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el Nombre del Idioma.'),
            'max_length': _('El Nombre del Idioma excede lo permitido.'),
        }
    )

    acronym = forms.CharField(
        required=False,
        strip=True,
        max_length=5,
        label=_('Sigla Idioma'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Sigla del Idioma (opcional)'),
                'id': 'acronym',
                'type': 'text',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('La Sigla del Idioma excede lo permitido.'),
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=20,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del Idioma en Español (opcional)'),
                'id': 'name_esp',
                'type': 'text',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('El Nombre en Español del Idioma excede lo permitido.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el idioma.'),
            }
        )
    )

    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean_name_esp(self):
        return to_title_text(self.cleaned_data.get('name_esp', ''))

    def clean_acronym(self):
        return to_upper_text(self.cleaned_data.get('acronym', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')
        acronym = cleaned_data.get('acronym')

        normalized_name = normalize_text(name) if name else ''
        normalized_name_esp = normalize_text(name_esp) if name_esp else ''
        normalized_acronym = normalize_text(acronym) if acronym else ''

        # Verifica si ya existe un idioma con el nombre, iniciales, o combinaciones similares
        existing_languages = Language.objects.exclude(pk=self.instance.pk)
        for language in existing_languages:
            if normalize_text(language.name) == normalized_name:
                raise forms.ValidationError(_('Ya existe un idioma con el nombre "%(name)s" o es muy similar.') % {'name': name})

            if normalized_name_esp and normalize_text(language.name_esp) == normalized_name_esp:
                raise forms.ValidationError(_('Ya existe un idioma con el nombre en español "%(name_esp)s" o es muy similar.') % {'name_esp': name_esp})

            if normalized_acronym and normalize_text(language.acronym) == normalized_acronym:
                raise forms.ValidationError(_('Ya existe un idioma con el acrónimo "%(acronym)s" o es muy similar.') % {'acronym': acronym})

        return cleaned_data

########################################################################################################    Formulario para Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'biography', 'birth_date', 'country', 'is_active']

    full_name = forms.CharField(
        required=True,
        strip=True,
        max_length=150,
        label=_('Nombre Completo'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre completo de la persona'),
                'autocomplete': 'off',
                'id': 'full_name',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre completo.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    biography = forms.CharField(
        required=False,
        strip=True,
        label=_('Biografía'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Biografía de la persona (opcional)'),
                'rows': 4,
                'id': 'biography',
                'type': 'text',
            }
        )
    )

    birth_date = forms.DateField(
        required=False,
        label=_('Fecha de Nacimiento'),
        widget=DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'birth_date'
            }
        )
    )

    country = forms.ModelChoiceField(
        required=False,
        label=_('País'),
        empty_label=_('Seleccione un país'),
        queryset=None,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'country',
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
                'title': _('Marcar para activar o desmarcar para desactivar a la persona.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = Country.objects.filter(is_active=True)

    def clean_full_name(self):
        return to_title_text(self.cleaned_data.get('full_name', ''))

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')

        if full_name:
            normalized = normalize_text(full_name)
            qs = Person.objects.exclude(pk=self.instance.pk)
            for person in qs:
                existing = normalize_text(person.full_name)
                if normalized == existing:
                    raise forms.ValidationError(_('Ya existe una persona con el nombre "%(full_name)s" o es muy similar.') % {'full_name': full_name})

        return cleaned_data

########################################################################################################    Formulario para PersonImage
class PersonImageForm(forms.ModelForm):
    class Meta:
        model = PersonImage
        fields = ['person', 'size_image', 'image', 'image_url', 'is_active']

    person = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Persona'),
        empty_label=_('Seleccione una persona'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una persona.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen de la persona.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['person'].disabled = True
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

########################################################################################################    Formulario para PersonImageExtra
class PersonImageExtraForm(forms.ModelForm):
    class Meta:
        model = PersonImageExtra
        fields = ['person', 'image', 'is_active']

    person = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label='Persona',
        empty_label=_('Seleccione una persona'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una persona.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional de la persona.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.filter(is_active=True)

        if self.instance.pk:
            # Deshabilitar los campos si es edición
            self.fields['person'].disabled = True

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

########################################################################################################    Formulario para PersonNickname
class PersonNicknameForm(forms.ModelForm):
    class Meta:
        model = PersonNickname
        fields = ['person', 'nickname', 'is_active']

    person = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label='Persona',
        empty_label=_('Seleccione una persona'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar una persona.'),
        },
    )

    nickname = forms.CharField(
        required=True,
        max_length=100,
        label='Apodo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Apodo de la Persona'),
                'id': 'nickname',
                'autocomplete': 'off',
                'type': 'text',
            }
        ),
        error_messages={
            'required': _('Debe ingresar un apodo.'),
            'max_length': _('El apodo excede los 100 caracteres permitidos.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el apodo de la persona.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.filter(is_active=True)

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname', '').strip()
        return ' '.join(part.capitalize() for part in nickname.split())

    def clean(self):
        cleaned_data = super().clean()
        nickname = cleaned_data.get('nickname')
        person = cleaned_data.get('person')

        if nickname and person:
            normalized_nickname = normalize_text(nickname)

            existing_nicks = PersonNickname.objects.filter(person=person).exclude(pk=self.instance.pk)
            for existing in existing_nicks:
                existing_normalized = normalize_text(existing.nickname)
                if normalized_nickname == existing_normalized:
                    raise forms.ValidationError(_('El apodo "%(nickname)s" ya está registrado para esta persona.') % {'nickname': nickname})

        return cleaned_data

########################################################################################################    Formulario para Quality
class QualityForm(forms.ModelForm):
    class Meta:
        model = Quality
        fields = ['name', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=10,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre de la Calidad'),
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el Nombre de la Calidad.'),
            'max_length': _('El Nombre de la Calidad excede lo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción Calidad'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción de la Calidad (opcional)'),
                'id': 'description',
                'rows': 3,
                'autocomplete': 'off',
                'type': 'text',
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
                'title': _('Marcar para activar o desmarcar para desactivar la calidad.'),
            }
        )
    )

    def clean_name(self):
        return to_upper_text(self.cleaned_data.get('name', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name:
            normalized_name = normalize_text(name)

            existing_qualities = Quality.objects.exclude(pk=self.instance.pk)

            for quality in existing_qualities:
                existing_normalized_name = normalize_text(quality.name)
                if normalized_name == existing_normalized_name:
                    raise forms.ValidationError(_('Ya existe una calidad con el nombre "%(name)s" o es muy similar.') % {'name': name})

        return cleaned_data

########################################################################################################    Formulario para Website
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'acronym', 'url', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre de la Página de Descarga'),
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el Nombre del sitio web.'),
            'max_length': _('El Nombre del sitio web excede lo permitido.'),
        }
    )

    acronym = forms.CharField(
        required=True,
        strip=True,
        max_length=5,
        label=_('Acrónimo'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Acrónimo del sitio web.'),
                'id': 'acronym',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el acrónimo del sitio web.'),
            'max_length': _('El acrónimo del sitio web exceden lo permitido.'),
        }
    )

    url = forms.CharField(
        required=True,
        max_length=250,
        label='URL',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL del sitio web'),
                'id': 'url',
                'type': 'url',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': _('Debe ingresar la URL del sitio web.'),
            'max_length': _('La URL del sitio web excede lo permitido.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el sitio web.'),
            }
        )
    )

    def clean_name(self):
        return to_title_text( self.cleaned_data.get('name', ''))

    def clean_acronym(self):
        return to_upper_text(self.cleaned_data.get('acronym', ''))

    def clean_url(self):
        url = self.cleaned_data.get('url', '').strip()
        return validate_url(url)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        url = cleaned_data.get('url')

        normalized_name = normalize_text(name) if name else ''
        normalized_url = url.lower().strip() if url else ''

        existing_websites = Website.objects.exclude(pk=self.instance.pk)
        for website in existing_websites:
            existing_normalized_name = normalize_text(website.name)
            existing_normalized_url = website.url.lower().strip()

            if normalized_name == existing_normalized_name:
                raise forms.ValidationError(_('Ya existe un sitio web con el nombre "%(name)s" o es muy similar.') % {'name': name})

            if normalized_url == existing_normalized_url:
                raise forms.ValidationError(_('Ya existe un sitio web con la URL "%(url)s" o es muy similar.') % {'url': url})

        return cleaned_data



from .models import ContextApp, Genre, Type, Rating, Status


class ContextAppForm(forms.ModelForm):
    class Meta:
        model = ContextApp
        fields = ['name', 'is_active']

    name = forms.ChoiceField(
        choices=ContextApp.APPS,
        label=_('Nombre'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'name',
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un nombre.'),
            'invalid_choice': _('Selección no válida.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el contexto.'),
            }
        )
    )

    def clean_name(self):
        # Normalizar el nombre para comparación
        name = self.cleaned_data.get('name')
        normalized_name = self.normalize_text(name)

        # Excluir la instancia actual si es edición
        qs = ContextApp.objects.exclude(pk=self.instance.pk if self.instance else None)
        for ctx in qs:
            if self.normalize_text(ctx.name) == normalized_name:
                raise forms.ValidationError(_('Ya existe un contexto con el nombre "%(name)s" o muy similar.') % {'name': name})
        return name

    @staticmethod
    def normalize_text(text):
        # Normaliza texto para comparación, puedes ajustar esta función según tu necesidad
        return text.strip().lower() if text else ''


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['parent', 'name', 'name_esp', 'description', 'explicit', 'contexts', 'is_active']

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
                'id': 'name',
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
                'id': 'name_esp',
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

    contexts = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        label=_('ContextAppos'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'contexts',
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
        self.fields['contexts'].queryset = ContextApp.objects.filter(is_active=True)

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

        # Validar que el género no sea su propio padre
        if parent and self.instance and parent.pk == self.instance.pk:
            self.add_error('parent', _('Un género no puede ser su propio padre.'))

        qs = Genre.objects.exclude(pk=self.instance.pk if self.instance else None)

        # Validar que no haya otro género con el mismo nombre o nombre en español o combinación
        for genre in qs:
            genre_name_norm = normalize_text(genre.name)
            genre_name_esp_norm = normalize_text(genre.name_esp) if genre.name_esp else ''

            # Validar nombre repetido
            if normalized_name and genre_name_norm == normalized_name:
                raise forms.ValidationError(
                    _('Ya existe un género con el nombre "%(name)s" o muy similar.') % {'name': name}
                )

            # Validar nombre_esp repetido
            if normalized_name_esp and genre_name_esp_norm == normalized_name_esp:
                raise forms.ValidationError(
                    _('Ya existe un género con el nombre en español "%(name_esp)s" o muy similar.') % {'name_esp': name_esp}
                )

            # Validar combinación nombre + nombre_esp repetida
            if normalized_name and normalized_name_esp:
                if genre_name_norm == normalized_name and genre_name_esp_norm == normalized_name_esp:
                    raise forms.ValidationError(
                        _('Ya existe un género con la combinación del nombre y nombre en español igual.')
                    )

        return cleaned_data


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['parent', 'name', 'name_esp', 'description', 'contexts', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del tipo'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del tipo.'),
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
                'placeholder': _('Nombre del tipo en español'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name_esp',
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
        empty_label=_('Seleccione un tipo padre'),
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
                'placeholder': _('Descripción del tipo'),
                'rows': 3,
                'id': 'description',
            }
        ),
    )

    contexts = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        label=_('ContextAppos'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'contexts',
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
                'title': _('Marcar para activar o desmarcar para desactivar el tipo.'),
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Type.objects.filter(is_active=True).exclude(pk=self.instance.pk if self.instance else None)
        self.fields['contexts'].queryset = ContextApp.objects.filter(is_active=True)

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

        # Validar que el tipo no sea su propio padre
        if parent and self.instance and parent.pk == self.instance.pk:
            self.add_error('parent', _('Un tipo no puede ser su propio padre.'))

        qs = Type.objects.exclude(pk=self.instance.pk if self.instance else None)

        for obj in qs:
            obj_name_norm = normalize_text(obj.name)
            obj_name_esp_norm = normalize_text(obj.name_esp) if obj.name_esp else ''

            # Validar nombre repetido
            if normalized_name and obj_name_norm == normalized_name:
                raise forms.ValidationError(
                    _('Ya existe un tipo con el nombre "%(name)s" o muy similar.') % {'name': name}
                )

            # Validar nombre_esp repetido
            if normalized_name_esp and obj_name_esp_norm == normalized_name_esp:
                raise forms.ValidationError(
                    _('Ya existe un tipo con el nombre en español "%(name_esp)s" o muy similar.') % {'name_esp': name_esp}
                )

            # Validar combinación nombre + nombre_esp repetida
            if normalized_name and normalized_name_esp:
                if obj_name_norm == normalized_name and obj_name_esp_norm == normalized_name_esp:
                    raise forms.ValidationError(
                        _('Ya existe un tipo con la combinación del nombre y nombre en español igual.')
                    )

        return cleaned_data


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['acronym', 'name', 'name_esp', 'contexts', 'is_active']

    acronym = forms.CharField(
        required=True,
        strip=True,
        max_length=15,
        label=_('Acrónimo'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Acrónimo'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'acronym',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el acrónimo.'),
            'max_length': _('El acrónimo excede el largo permitido.'),
        },
    )

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=60,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre de la clasificación'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=60,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre en español'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name_esp',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        },
    )

    contexts = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        label=_('ContextAppos'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'contexts',
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
                'title': _('Marcar para activar o desmarcar para desactivar la clasificación.'),
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contexts'].queryset = ContextApp.objects.filter(is_active=True)

    def clean_acronym(self):
        return self.cleaned_data.get('acronym', '').strip().upper()

    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean_name_esp(self):
        return to_title_text(self.cleaned_data.get('name_esp', ''))

    def clean(self):
        cleaned_data = super().clean()
        acronym = cleaned_data.get('acronym')
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_acronym = normalize_text(acronym) if acronym else ''
        normalized_name = normalize_text(name) if name else ''
        normalized_name_esp = normalize_text(name_esp) if name_esp else ''

        qs = Rating.objects.exclude(pk=self.instance.pk if self.instance else None)

        for obj in qs:
            obj_acronym_norm = normalize_text(obj.acronym)
            obj_name_norm = normalize_text(obj.name)
            obj_name_esp_norm = normalize_text(obj.name_esp) if obj.name_esp else ''

            if normalized_acronym and obj_acronym_norm == normalized_acronym:
                raise forms.ValidationError(
                    _('Ya existe una clasificación con el acrónimo "%(acronym)s" o muy similar.') % {'acronym': acronym}
                )

            if normalized_name and obj_name_norm == normalized_name:
                raise forms.ValidationError(
                    _('Ya existe una clasificación con el nombre "%(name)s" o muy similar.') % {'name': name}
                )

            if normalized_name_esp and obj_name_esp_norm == normalized_name_esp:
                raise forms.ValidationError(
                    _('Ya existe una clasificación con el nombre en español "%(name_esp)s" o muy similar.') % {'name_esp': name_esp}
                )

            if normalized_name and normalized_name_esp:
                if obj_name_norm == normalized_name and obj_name_esp_norm == normalized_name_esp:
                    raise forms.ValidationError(
                        _('Ya existe una clasificación con la combinación del nombre y nombre en español igual.')
                    )

        return cleaned_data


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name', 'name_esp', 'description', 'contexts', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del estado'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name',
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre del estado.'),
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
                'placeholder': _('Nombre del estado en español'),
                'autocomplete': 'off',
                'type': 'text',
                'id': 'name_esp',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        },
    )

    description = forms.CharField(
        required=False,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del estado'),
                'rows': 3,
                'id': 'description',
            }
        ),
    )

    contexts = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        label=_('ContextAppos'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-select',
                'id': 'contexts',
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
                'title': _('Marcar para activar o desmarcar para desactivar el estado.'),
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contexts'].queryset = ContextApp.objects.filter(is_active=True)

    def clean_name(self):
        return to_title_text(self.cleaned_data.get('name', ''))

    def clean_name_esp(self):
        return to_title_text(self.cleaned_data.get('name_esp', ''))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = normalize_text(name) if name else ''
        normalized_name_esp = normalize_text(name_esp) if name_esp else ''

        qs = Status.objects.exclude(pk=self.instance.pk if self.instance else None)

        for obj in qs:
            obj_name_norm = normalize_text(obj.name)
            obj_name_esp_norm = normalize_text(obj.name_esp) if obj.name_esp else ''

            if normalized_name and obj_name_norm == normalized_name:
                raise forms.ValidationError(
                    _('Ya existe un estado con el nombre "%(name)s" o muy similar.') % {'name': name}
                )

            if normalized_name_esp and obj_name_esp_norm == normalized_name_esp:
                raise forms.ValidationError(
                    _('Ya existe un estado con el nombre en español "%(name_esp)s" o muy similar.') % {'name_esp': name_esp}
                )

            if normalized_name and normalized_name_esp:
                if obj_name_norm == normalized_name and obj_name_esp_norm == normalized_name_esp:
                    raise forms.ValidationError(
                        _('Ya existe un estado con la combinación del nombre y nombre en español igual.')
                    )

        return cleaned_data
