from django import forms
from apps.common.models import Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website
from django.forms.widgets import DateInput
from core.utils.validators import validate_file_extension, ALLOWED_IMAGE_EXTENSIONS
from django.utils.translation import gettext_lazy as _
# Create your forms here.
########################################################################################################    Modelo para Country
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'name_esp', 'code', 'numeric_code', 'is_active']

    name = forms.CharField(
        required=True,
        max_length=60,
        label='Nombre en Inglés',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del país (inglés)',
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': 'Debe ingresar el nombre en inglés.',
            'max_length': 'El nombre excede el largo permitido.'
        }
    )

    name_esp = forms.CharField(
        required=True,
        max_length=60,
        label='Nombre en Español',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del país (español)',
                'autocomplete': 'off',
                'id': 'name_esp'
            }
        ),
        error_messages={
            'required': 'Debe ingresar el nombre en español.',
            'max_length': 'El nombre excede el largo permitido.'
        }
    )

    code = forms.CharField(
        required=False,
        max_length=4,
        label='Código',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Código de país (opcional)',
                'autocomplete': 'off',
                'id': 'code'
            }
        )
    )

    numeric_code = forms.IntegerField(
        required=False,
        label='Código Numérico',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Código numérico del país',
                'id': 'numeric_code'
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': 'Marcar para activar o desactivar el país',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip().title()
        return name_esp

    def clean_code(self):
        code = self.cleaned_data.get('code', '').strip().upper()
        return code

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        # Validación cruzada para asegurar que no existan duplicados similares
        normalized_name = ''.join(name.upper().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        qs = Country.objects.exclude(pk=self.instance.pk)

        for country in qs:
            if normalized_name == ''.join(country.name.upper().split()):
                raise forms.ValidationError(f'El nombre en inglés "{name}" ya existe o es muy similar.')
            if normalized_name_esp == ''.join(country.name_esp.upper().split()):
                raise forms.ValidationError(f'El nombre en español "{name_esp}" ya existe o es muy similar.')

        return cleaned_data

########################################################################################################    Modelo para Format
class FormatForm(forms.ModelForm):
    class Meta:
        model = Format
        fields = [
            'name',  'description', 'for_video', 'for_music', 'for_image',
            'for_document', 'for_other', 'is_active'
        ]

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=15,
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Formato',
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el Nombre del Formato.',
            'max_length': 'El Nombre del Formato excede lo permitido.',
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label='Descripción Formato',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del Formato (opcional)',
                'id': 'description',
                'rows': 3,
                'autocomplete': 'off',
            }
        )
    )



    for_video = forms.BooleanField(
        required=False,
        label='Videos',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_video',
                'title': 'Marcar si el formato es para Videos',
            }
        )
    )

    for_music = forms.BooleanField(
        required=False,
        label='Música',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_music',
                'title': 'Marcar si el formato es para Música',
            }
        )
    )

    for_image = forms.BooleanField(
        required=False,
        label='Imágenes',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_image',
                'title': 'Marcar si el formato es para Imágenes',
            }
        )
    )

    for_document = forms.BooleanField(
        required=False,
        label='Documentos',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_document',
                'title': 'Marcar si el formato es para Documentos',
            }
        )
    )

    for_other = forms.BooleanField(
        required=False,
        label='Otros',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'for_other',
                'title': 'Marcar si el formato es para Otros tipos de archivos',
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': 'Marcar para activar o desactivar el Formato',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.upper() for part in name.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        # Normaliza el nombre eliminando espacios y convirtiendo a minúsculas
        normalized_name = ''.join(name.upper().split()) if name else ''

        # Verifica si un formato con el nombre normalizado ya existe, ignorando el caso actual
        if normalized_name:
            existing_formats = Format.objects.exclude(pk=self.instance.pk)
            for format_obj in existing_formats:
                existing_normalized_name = ''.join(format_obj.name.upper().split())
                if normalized_name == existing_normalized_name:
                    raise forms.ValidationError(f'El Formato "{name}" ya existe o es muy similar.')

        return cleaned_data

########################################################################################################    Modelo para ImageSize
class ImageSizeForm(forms.ModelForm):
    class Meta:
        model = ImageSize
        fields = ['name', 'name_esp', 'is_active']

    name = forms.CharField(
        required=True,
        max_length=20,
        label='Nombre (Inglés)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del tamaño (inglés)',
                'autocomplete': 'off',
                'id': 'name',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el nombre del tamaño en inglés.',
            'max_length': 'El nombre en inglés excede el largo permitido.'
        }
    )

    name_esp = forms.CharField(
        required=True,
        max_length=20,
        label='Nombre (Español)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del tamaño (español)',
                'autocomplete': 'off',
                'id': 'name_esp',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el nombre del tamaño en español.',
            'max_length': 'El nombre en español excede el largo permitido.'
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': 'Marcar si el tamaño está activo',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip().title()
        return name_esp

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = ''.join(name.upper().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        qs = ImageSize.objects.exclude(pk=self.instance.pk)

        for size in qs:
            if normalized_name == ''.join(size.name.upper().split()):
                raise forms.ValidationError(f'El nombre "{name}" ya existe o es muy similar.')
            if normalized_name_esp == ''.join(size.name_esp.upper().split()):
                raise forms.ValidationError(f'El nombre en español "{name_esp}" ya existe o es muy similar.')

        return cleaned_data

########################################################################################################    Modelo para Language
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'acronym', 'name_esp', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=20,
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Idioma',
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el Nombre del Idioma.',
            'max_length': 'El Nombre del Idioma excede lo permitido.',
        }
    )

    acronym = forms.CharField(
        required=False,
        strip=True,
        max_length=5,
        label='Sigla Idioma',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Sigla del Idioma (opcional)',
                'id': 'acronym',
                'type': 'text',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': 'La Sigla del Idioma excede lo permitido.',
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=20,
        label='Nombre Español',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Idioma en Español (opcional)',
                'id': 'name_esp',
                'type': 'text',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': 'El Nombre en Español del Idioma excede lo permitido.',
        }
    )



    is_active = forms.BooleanField(
        required=False,
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
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
        acronym = cleaned_data.get('acronym')

        # Normaliza los nombres e iniciales eliminando espacios y convirtiendo a minúsculas
        normalized_name = ''.join(name.lower().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.lower().split()) if name_esp else ''
        normalized_acronym = ''.join(acronym.lower().split()) if acronym else ''


        # Verifica si ya existe un idioma con el nombre, iniciales, o combinaciones similares
        existing_languages = Language.objects.exclude(pk=self.instance.pk)
        for language in existing_languages:
            existing_normalized_name = ''.join(language.name.lower().split())
            existing_normalized_name_esp = ''.join(language.name_esp.lower().split())
            existing_normalized_acronym = ''.join(language.acronym.lower().split())

            if normalized_name == existing_normalized_name:
                raise forms.ValidationError(f'El idioma "{name}" ya existe o es muy similar.')

            if normalized_name_esp and normalized_name_esp == existing_normalized_name_esp:
                raise forms.ValidationError(f'El nombre en español "{name_esp}" ya existe o es muy similar.')

            if normalized_acronym and normalized_acronym == existing_normalized_acronym:
                raise forms.ValidationError(f'La sigla "{acronym}" ya existe o es muy similar.')


        return cleaned_data

########################################################################################################    Modelo para Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'biography', 'birth_date', 'country', 'is_active']

    full_name = forms.CharField(
        required=True,
        max_length=255,
        label='Nombre Completo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo de la persona',
                'autocomplete': 'off',
                'id': 'full_name',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el nombre completo.',
            'max_length': 'El nombre excede el largo permitido.',
        }
    )

    biography = forms.CharField(
        required=False,
        label='Biografía',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Biografía de la persona (opcional)',
                'rows': 4,
                'id': 'biography'
            }
        )
    )

    birth_date = forms.DateField(
        required=False,
        label='Fecha de Nacimiento',
        widget=DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'birth_date'
            }
        )
    )

    country = forms.ModelChoiceField(
        required=False,
        label='País',
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
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': 'Marcar para activar o desactivar a la persona',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo países activos
        self.fields['country'].queryset = Country.objects.filter(is_active=True)

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name', '').strip()
        return ' '.join(part.capitalize() for part in full_name.split())

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')

        if full_name:
            normalized = ''.join(full_name.upper().split())
            qs = Person.objects.exclude(pk=self.instance.pk)
            for person in qs:
                existing = ''.join(person.full_name.upper().split())
                if normalized == existing:
                    raise forms.ValidationError(f'La persona "{full_name}" ya existe o es muy similar.')

        return cleaned_data

########################################################################################################    Modelo para PersonImage
class PersonImageForm(forms.ModelForm):
    class Meta:
        model = PersonImage
        fields = ['person', 'size_image', 'image', 'image_url', 'is_active']

    person = forms.ModelChoiceField(
        queryset=Person.objects.filter(is_active=True),
        required=True,
        label='Persona',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        )
    )

    size_image = forms.ModelChoiceField(
        queryset=ImageSize.objects.filter(is_active=True),
        required=True,
        label='Tamaño de Imagen',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'size_image'
            }
        )
    )

    image = forms.ImageField(
        required=True,
        label='Imagen',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'id': 'image'
            }
        ),
        error_messages={
            'required': 'Debe subir una imagen.',
            'invalid': 'El archivo seleccionado no es válido.',
        }
    )

    image_url = forms.URLField(
        required=False,
        label='URL Alternativa',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'URL de la imagen (opcional)',
                'id': 'image_url',
                'autocomplete': 'off'
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        initial=True,
        label='Activo',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active'
            }
        )
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            validate_file_extension(image, ALLOWED_IMAGE_EXTENSIONS)
        return image

    def clean_image_url(self):
        url = self.cleaned_data.get('image_url', '').strip()
        return url or None  # Si está vacío, se guarda como None

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


########################################################################################################    Modelo para PersonImageExtra
class PersonImageExtraForm(forms.ModelForm):
    class Meta:
        model = PersonImageExtra
        fields = ['person', 'image', 'is_active']

    person = forms.ModelChoiceField(
        queryset=Person.objects.filter(is_active=True),
        required=True,
        label='Persona',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        )
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
            'required': 'Debe subir una imagen.',
            'invalid': 'El archivo seleccionado no es válido.',
        }
    )

    is_active = forms.BooleanField(
        required=False,
        initial=True,
        label='Activo',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active'
            }
        )
    )

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
            raise forms.ValidationError('Debe subir una imagen.')

        return cleaned_data

########################################################################################################    Modelo para PersonNickname
class PersonNicknameForm(forms.ModelForm):
    class Meta:
        model = PersonNickname
        fields = ['person', 'nickname', 'is_active']

    person = forms.ModelChoiceField(
        queryset=Person.objects.filter(is_active=True),
        required=True,
        label='Persona',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'person'
            }
        )
    )

    nickname = forms.CharField(
        required=True,
        max_length=100,
        label='Apodo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Apodo de la Persona',
                'id': 'nickname',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar un apodo.',
            'max_length': 'El apodo excede los 100 caracteres permitidos.',
        }
    )

    is_active = forms.BooleanField(
        required=False,
        initial=True,
        label='Activo',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active'
            }
        )
    )

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname', '').strip()
        return ' '.join(part.capitalize() for part in nickname.split())

    def clean(self):
        cleaned_data = super().clean()
        nickname = cleaned_data.get('nickname')
        person = cleaned_data.get('person')

        if nickname and person:
            normalized_nickname = ''.join(nickname.upper().split())

            existing_nicks = PersonNickname.objects.filter(person=person).exclude(pk=self.instance.pk)
            for existing in existing_nicks:
                existing_normalized = ''.join(existing.nickname.upper().split())
                if normalized_nickname == existing_normalized:
                    raise forms.ValidationError(f'El apodo "{nickname}" ya está registrado para esta persona.')

        return cleaned_data

########################################################################################################    Modelo para Quality
class QualityForm(forms.ModelForm):
    class Meta:
        model = Quality
        fields = ['name', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=10,
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la Calidad',
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el Nombre de la Calidad.',
            'max_length': 'El Nombre de la Calidad excede lo permitido.',
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label='Descripción Calidad',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descripción de la Calidad (opcional)',
                'id': 'description',
                'rows': 3,
                'autocomplete': 'off',
            }
        )
    )

    is_active = forms.BooleanField(
        required=False,
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': 'Marcar para activar o desactivar la Calidad',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.upper() for part in name.split())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        # Normaliza el nombre eliminando espacios y convirtiendo a minúsculas
        normalized_name = ''.join(name.upper().split()) if name else ''

        # Verifica si una calidad con el nombre normalizado ya existe, ignorando el caso actual
        if normalized_name:
            existing_qualities = Quality.objects.exclude(pk=self.instance.pk)
            for quality in existing_qualities:
                existing_normalized_name = ''.join(quality.name.upper().split())
                if normalized_name == existing_normalized_name:
                    raise forms.ValidationError(f'La Calidad "{name}" ya existe o es muy similar.')

        return cleaned_data

########################################################################################################    Modelo para Website
class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'acronym', 'url', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la Página de Descarga',
                'id': 'name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar el Nombre de la Página de Descarga.',
            'max_length': 'El Nombre de la Página de Descarga excede lo permitido.',
        }
    )

    acronym = forms.CharField(
        required=True,
        strip=True,
        max_length=5,
        label='Siglas',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Siglas de la Página de Descarga',
                'id': 'acronym',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar las Siglas de la Página de Descarga.',
            'max_length': 'Las Siglas de la Página de Descarga exceden lo permitido.',
        }
    )

    url = forms.URLField(
        required=True,
        max_length=250,
        label='URL',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'URL de la Página de Descarga',
                'id': 'URL',
                'type': 'url',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe ingresar la URL de la Página de Descarga.',
            'max_length': 'La URL de la Página de Descarga excede lo permitido.',
            'invalid': 'Debe ingresar una URL válida.',
        }
    )

    is_active = forms.BooleanField(
        required=False,
        label='Activo',
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        return ' '.join(part.capitalize() for part in name.split())

    def clean_acronym(self):
        acronym = self.cleaned_data.get('acronym', '').strip().upper()
        return acronym

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        URL = cleaned_data.get('URL')

        # Normaliza el nombre eliminando espacios y convirtiendo a minúsculas
        normalized_name = ''.join(name.lower().split()) if name else ''
        normalized_url = URL.lower().strip() if URL else ''

        # Verifica si ya existe una página de descarga con el nombre o URL similares
        existing_websites = Website.objects.exclude(pk=self.instance.pk)
        for website in existing_websites:
            existing_normalized_name = ''.join(website.name.lower().split())
            existing_normalized_url = website.URL.lower().strip()

            if normalized_name == existing_normalized_name:
                raise forms.ValidationError(f'La página de descarga "{name}" ya existe o es muy similar.')

            if normalized_url == existing_normalized_url:
                raise forms.ValidationError(f'La URL "{URL}" ya existe o es muy similar.')

        return cleaned_data
