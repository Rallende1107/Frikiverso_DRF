from django import forms
from django.utils.translation import gettext_lazy as _
from core.utils.validators import validate_file_extension, validate_url, ALLOWED_IMAGE_EXTENSIONS
from core.utils.utils import procesar_urls
from apps.common.models import (ImageSize, Language)

from .models import (
    Genre, GameEngine, Censorship, Prefix, Status, Platform, Developer, Translator, Publisher, Game, GameImage,
    GameImageExtra, DeveloperLink, TranslatorLink, PublisherLink, DeveloperImage, DeveloperImageExtra,
    TranslatorImage, TranslatorImageExtra, PublisherImage, PublisherImageExtra, TitleGame, F95GameFetchStatus,
    )

# Create your forms here.
########################################################################################################    Formulario para Genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['parent', 'name', 'name_esp', 'description', 'explicit', 'is_active']

    parent = forms.ModelChoiceField(
        queryset=Genre.objects.filter(is_active=True),
        required=False,
        label=_('Género padre'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'parent',
            }
        )
    )

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del género (inglés)'),
                'autocomplete': 'off',
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
                'placeholder': _('Nombre del género (español)'),
                'autocomplete': 'off',
                'id': 'name_esp',
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del género'),
                'id': 'description',
                'rows':3,
            }
        )
    )

    explicit = forms.BooleanField(
        required=False,
        label=_('Explícito'),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'explicit',
                'title': _('Marcar si el contenido es explícito'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el género.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '').strip().title() if self.cleaned_data.get('name_esp') else ''
        return name_esp

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = ''.join(name.upper().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        qs = Genre.objects.exclude(pk=self.instance.pk)

        for genre in qs:
            if normalized_name == ''.join(genre.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un género con el nombre "%(name)s" o es muy similar.') % {'name': name})

            if name_esp and genre.name_esp and normalized_name_esp == ''.join(genre.name_esp.upper().split()):
                raise forms.ValidationError(_('Ya existe un género con el nombre en español "%(name_esp)s" o es muy similar.') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para GameEngine
class GameEngineForm(forms.ModelForm):
    class Meta:
        model = GameEngine
        fields = ['name', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=50,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del motor de desarrollo'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar el nombre.'),
            'max_length': _('El nombre excede el largo permitido.'),
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del motor'),
                'rows':3,
                'id': 'description'
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
                'title': _('Marcar para activar o desmarcar para desactivar el motor de desarrollo.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        normalized_name = ''.join(name.upper().split()) if name else ''
        qs = GameEngine.objects.exclude(pk=self.instance.pk)

        for obj in qs:
            if normalized_name == ''.join(obj.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un motor con el nombre "%(name)s" o es muy similar.') % {'name': name})
        return cleaned_data

########################################################################################################    Formulario para Censorship
class CensorshipForm(forms.ModelForm):
    class Meta:
        model = Censorship
        fields = ['name', 'name_esp', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=30,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre de la censura (inglés)'),
                'autocomplete': 'off',
                'id': 'name'
            }
        )
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=30,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': _('Nombre de la censura (español)'),
            'autocomplete': 'off',
            'id': 'name_esp'
            }
        )
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Descripción de la censura'),
            'rows': 3,
            'id': 'description'
        })
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la censura.'),
            }
        )
    )


    def clean_name(self):
        return self.cleaned_data.get('name', '').strip().title()

    def clean_name_esp(self):
        return self.cleaned_data.get('name_esp', '').strip().title() if self.cleaned_data.get('name_esp') else ''

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')
        norm_name = ''.join(name.upper().split()) if name else ''
        norm_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        qs = Censorship.objects.exclude(pk=self.instance.pk)
        for c in qs:
            if norm_name == ''.join(c.name.upper().split()):
                raise forms.ValidationError(_('Ya existe una censura con el nombre "%(name)s" o muy similar.') % {'name': name})
            if name_esp and c.name_esp and norm_name_esp == ''.join(c.name_esp.upper().split()):
                raise forms.ValidationError(_('Ya existe una censura con el nombre en español "%(name_esp)s" o muy similar.') % {'name_esp': name_esp})
        return cleaned_data

########################################################################################################    Formulario para Prefix
class PrefixForm(forms.ModelForm):
    class Meta:
        model = Prefix
        fields = ['name', 'name_esp', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=30,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del prefijo'),
                'autocomplete': 'off',
                'id': 'name'
            }
        )
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=30,
        label=_('Nombre Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del prefijo en español'),
                'autocomplete': 'off',
                'id': 'name_esp'
            }
        )
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del prefijo'),
                'rows': 3,
                'id': 'description'
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
                'title': _('Marcar para activar o desmarcar para desactivar el prefijo.'),
            }
        )
    )

    def clean_name(self):
        return self.cleaned_data.get('name', '').strip().title()

    def clean_name_esp(self):
        return self.cleaned_data.get('name_esp', '').strip().title() if self.cleaned_data.get('name_esp') else ''

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')
        norm_name = ''.join(name.upper().split()) if name else ''
        norm_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        qs = Prefix.objects.exclude(pk=self.instance.pk)
        for p in qs:
            if norm_name == ''.join(p.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un prefijo con el nombre "%(name)s" o muy similar.') % {'name': name})
            if name_esp and p.name_esp and norm_name_esp == ''.join(p.name_esp.upper().split()):
                raise forms.ValidationError(_('Ya existe un prefijo con el nombre en español "%(name_esp)s" o muy similar.') % {'name_esp': name_esp})
        return cleaned_data

########################################################################################################    Formulario para Status
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name', 'name_esp', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=30,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del estado'),
                'autocomplete': 'off',
                'id': 'name'
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
        max_length=30,
        label=_('Nombre en Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del estado (español)'),
                'autocomplete': 'off',
                'id': 'name_esp'
            }
        )
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Descripción del estado'),
                'rows': 3,
                'id': 'description'
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
                'title': _('Marcar para activar o desmarcar para desactivar el estado.'),
            }
        )
    )

    def clean_name(self):
        return self.cleaned_data.get('name', '').strip().title()

    def clean_name_esp(self):
        value = self.cleaned_data.get('name_esp', '')
        return value.strip().title() if value else None

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        qs = Status.objects.exclude(pk=self.instance.pk)
        normalized_name = ''.join(name.upper().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        for obj in qs:
            if normalized_name == ''.join(obj.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un estado con un nombre similar: %(name)s.') % {'name': name})

            if name_esp and obj.name_esp and normalized_name_esp == ''.join(obj.name_esp.upper().split()):
                raise forms.ValidationError(_('Ya existe un estado con un nombre español similar: %(name_esp)s.') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Platform
class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name', 'name_esp', 'description', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=30,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre de la plataforma'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.')
        }
    )

    name_esp = forms.CharField(
        required=False,
        strip=True,
        max_length=30,
        label=_('Nombre en Español'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre en español (opcional)'),
                'autocomplete': 'off',
                'id': 'name_esp'
            }
        ),
        error_messages={
            'max_length': _('El nombre en español excede el largo permitido.')
        }
    )

    description = forms.CharField(
        required=False,
        strip=True,
        label=_('Descripción'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Descripción de la plataforma (opcional)'),
            'rows': 3,
            'id': 'description'
        })
    )

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la plataforma.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean_name_esp(self):
        name_esp = self.cleaned_data.get('name_esp', '')
        return name_esp.strip().title() if name_esp else ''

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        name_esp = cleaned_data.get('name_esp')

        normalized_name = ''.join(name.upper().split()) if name else ''
        normalized_name_esp = ''.join(name_esp.upper().split()) if name_esp else ''

        qs = Platform.objects.exclude(pk=self.instance.pk)

        for platform in qs:
            if normalized_name == ''.join(platform.name.upper().split()):
                raise forms.ValidationError(_('Ya existe una plataforma con el nombre "%(name)s" o uno muy similar.') % {'name': name})
            if name_esp and normalized_name_esp == ''.join((platform.name_esp or '').upper().split()):
                raise forms.ValidationError(_('Ya existe una plataforma con el nombre en español "%(name_esp)s" o uno muy similar.') % {'name_esp': name_esp})

        return cleaned_data

########################################################################################################    Formulario para Developer
class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=150,
        label=_('Nombre'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Nombre del desarrollador'),
            'autocomplete': 'off',
            'id': 'name'
        }),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.')
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
                'title': _('Marcar para activar o desmarcar para desactivar al desarrollador.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        normalized_name = ''.join(name.upper().split()) if name else ''

        qs = Developer.objects.exclude(pk=self.instance.pk)
        for dev in qs:
            if normalized_name == ''.join(dev.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un desarrollador con un nombre similar: %(name)s.') % {'name': name})

        return cleaned_data

########################################################################################################    Formulario para Translator
class TranslatorForm(forms.ModelForm):
    class Meta:
        model = Translator
        fields = ['name', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=150,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del traductor'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.')
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
                'title': _('Marcar para activar o desmarcar para desactivar al traductor.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        normalized_name = ''.join(name.upper().split()) if name else ''

        qs = Translator.objects.exclude(pk=self.instance.pk)
        for translator in qs:
            if normalized_name == ''.join(translator.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un traductor con un nombre similar: %(name)s.') % {'name': name})

        return cleaned_data

########################################################################################################    Formulario para Publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'is_active']

    name = forms.CharField(
        required=True,
        strip=True,
        max_length=150,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del editor'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.')
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
                'title': _('Marcar para activar o desmarcar para desactivar al editor.'),
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip().title()
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        normalized_name = ''.join(name.upper().split()) if name else ''

        qs = Publisher.objects.exclude(pk=self.instance.pk)
        for publisher in qs:
            if normalized_name == ''.join(publisher.name.upper().split()):
                raise forms.ValidationError(_('Ya existe un editor con un nombre similar: %(name)s.') % {'name': name})

        return cleaned_data

########################################################################################################    Formulario para Game
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'title', 'version', 'release_date', 'synopsis', 'background', 'is_active',
            # FK
            'status', 'engine', 'censored',
            # Many
            'platforms', 'developers', 'publishers', 'languages',
            'translators', 'genres',
            # Opcionales
            'url_fzone', 'url_steam',
        ]

    title = forms.CharField(
        max_length=255,
        strip=True,
        required=True,
        label=_('Título'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Título del juego'),
                'autocomplete': 'off',
                'id': 'title'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un título.'),
            'max_length': _('El título excede el largo permitido.')
        }
    )

    version = forms.CharField(
        max_length=50,
        strip=True,
        required=False,
        label=_('Versión'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Versión del juego'),
                'id': 'version'
            }
        ),
        error_messages={
            'max_length': _('La versión excede el largo permitido.')
        }
    )

    release_date = forms.DateField(
        required=True,
        label=_('Fecha de Lanzamiento'),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'release_date'
            }
        )
    )

    synopsis = forms.CharField(
        required=False,
        strip=True,
        label=_('Sinopsis'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': _('Resumen o sinopsis'),
                'rows': 3
            }
        )
    )

    background = forms.CharField(
        required=False,
        strip=True,
        label=_('Reseña'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Detalles adicionales del juego'),
            'rows': 3
        })
    )

    url_fzone = forms.CharField(
        required=False,
        strip=True,
        max_length=250,
        label=_('URL F95'),
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL F95Zone (Opcional)'),
                'id': 'url_fzone',
                'type': 'url',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('La URL de F95Zone excede lo permitido.'),
        }
    )

    url_steam = forms.CharField(
        required=False,
        strip=True,
        max_length=250,
        label=_('URL Steam'),
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL Steam (Opcional)'),
                'id': 'url_steam',
                'type': 'url',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'max_length': _('La URL de Steam excede lo permitido.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar el juego.'),
            }
        )
    )

    # ForeignKey & ManyToMany fields
    status = forms.ModelChoiceField(
        queryset=None,
        required=False,
        label=_('Estado'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'status',
            }
        )
    )

    engine = forms.ModelChoiceField(
        queryset=None,
        required=False,
        label=_('Motor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'engine',
            }
        )
    )

    censored = forms.ModelChoiceField(
        queryset=None,
        required=False,
        label=_('Censura'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'censored',
            }
        )
    )

    platforms = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Plataformas'),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'checkbox-multiple-wrapper',
                'id': 'platforms',
            }
        )
    )

    developers = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Desarrolladores'),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'checkbox-multiple-wrapper',
                'id': 'developers',
            }
        )
    )

    publishers = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Editores'),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'checkbox-multiple-wrapper',
                'id': 'publishers',
            }
        )
    )

    languages = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Idiomas'),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'checkbox-multiple-wrapper',
                'id': 'languages',
            }
        )
    )

    translators = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Traductores'),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'checkbox-multiple-wrapper',
                'id': 'translators',
            }
        )
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=None,
        required=False,
        label=_('Géneros'),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'checkbox-multiple-wrapper',
                'id': 'genres',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['status'].queryset = Status.objects.filter(is_active=True)
        self.fields['engine'].queryset = GameEngine.objects.filter(is_active=True)
        self.fields['censored'].queryset = Censorship.objects.filter(is_active=True)
        self.fields['platforms'].queryset = Platform.objects.filter(is_active=True)
        self.fields['developers'].queryset = Developer.objects.filter(is_active=True)
        self.fields['publishers'].queryset = Publisher.objects.filter(is_active=True)
        self.fields['languages'].queryset = Language.objects.filter(is_active=True)
        self.fields['translators'].queryset = Translator.objects.filter(is_active=True)
        self.fields['genres'].queryset = Genre.objects.filter(is_active=True)

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        return title

    def clean_url_steam(self):
        url_steam = self.cleaned_data.get('url_steam', '').strip()
        if url_steam:
            try:
                return validate_url(url_steam)
            except ValueError:
                raise forms.ValidationError(_('La URL de Steam no es válida.'))
        return url_steam

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        url_fzone = cleaned_data.get('url_fzone')
        version = cleaned_data.get('version')

        try:
            url_fzone_limpia, fzone_id = procesar_urls(url_fzone, tipo=1)
        except ValueError as e:
            raise forms.ValidationError(str(e))

        cleaned_data['url_fzone'] = url_fzone_limpia
        cleaned_data['fzone_id'] = fzone_id

        if title and fzone_id:
            qs = Game.objects.exclude(pk=self.instance.pk).filter(
                fzone_id=fzone_id,
                title__iexact=title.strip(),
                url_fzone__iexact=url_fzone_limpia.strip()
            )
            if qs.exists():
                raise forms.ValidationError(_('Ya existe un juego con el mismo título, ID F95 y URL.'))

        # Aquí asignamos version_txt
        cleaned_data['version_txt'] = version or ''

        return cleaned_data

########################################################################################################    Formulario para GameImage
class GameImageForm(forms.ModelForm):
    class Meta:
        model = GameImage
        fields = ['game', 'size_image', 'image', 'image_url', 'is_active']

    game = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Juego'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'game'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un juego.'),
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
        strip=True,
        max_length= 2000,
        label=_('URL'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen del juego.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].queryset = Game.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

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

########################################################################################################    Formulario para GameImageExtra
class GameImageExtraForm(forms.ModelForm):
    class Meta:
        model = GameImageExtra
        fields = ['game', 'image', 'is_active']

    game = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Juego'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'game'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un juego.'),
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

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional del juego.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].queryset = Game.objects.filter(is_active=True)

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

########################################################################################################    Formulario para DeveloperLink
class DeveloperLinkForm(forms.ModelForm):
    class Meta:
        model = DeveloperLink
        fields = ['developer', 'name', 'url', 'is_active']

    developer = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Desarrollador'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'developer'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un desarrollador.'),
        },
    )

    name = forms.CharField(
        max_length=150,
        strip=True,
        required=True,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del enlace'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    url = forms.CharField(
        required=True,
        strip=True,
        max_length= 2000,
        label=_('URL'),
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL'),
                'id': 'url',
                'autocomplete': 'off',
                'type': 'url',
            }
        ),
        error_messages={
            'required': _('Debe ingresar una URL.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la web del desarrollador.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['developer'].queryset = Developer.objects.filter(is_active=True)

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_url(self):
        url = self.cleaned_data.get('url', '').strip()
        return validate_url(url)

    def clean(self):
        cleaned_data = super().clean()
        developer = cleaned_data.get('developer')
        name = cleaned_data.get('name')
        url = cleaned_data.get('url')

        if developer and name and url:
            exists = DeveloperLink.objects.exclude(pk=self.instance.pk).filter(
                developer=developer,
                name__iexact=name.strip(),
                url__iexact=url.strip()
            )
            if exists.exists():
                raise forms.ValidationError(_('Ya existe un enlace con el mismo nombre y URL para este desarrollador.'))

        return cleaned_data

########################################################################################################    Formulario para TranslatorLink
class TranslatorLinkForm(forms.ModelForm):
    class Meta:
        model = TranslatorLink
        fields = ['translator', 'name', 'url', 'is_active']

    translator = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Traductor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'translator'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un traductor.'),
        },
    )

    name = forms.CharField(
        max_length=150,
        strip=True,
        required=True,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del enlace'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    url = forms.CharField(
        required=True,
        strip=True,
        max_length= 2000,
        label=_('URL'),
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL'),
                'id': 'url',
                'autocomplete': 'off',
                'type': 'url',
            }
        ),
        error_messages={
            'required': _('Debe ingresar una URL.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la web del traductor.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['translator'].queryset = Translator.objects.filter(is_active=True)

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_url(self):
        url = self.cleaned_data.get('url', '').strip()
        return validate_url(url)

    def clean(self):
        cleaned_data = super().clean()
        translator = cleaned_data.get('translator')
        name = cleaned_data.get('name')
        url = cleaned_data.get('url')

        if translator and name and url:
            exists = TranslatorLink.objects.exclude(pk=self.instance.pk).filter(
                translator=translator,
                name__iexact=name.strip(),
                url__iexact=url.strip()
            )
            if exists.exists():
                raise forms.ValidationError(_('Ya existe un enlace con el mismo nombre y URL para este desarrollador.'))

        return cleaned_data

########################################################################################################    Formulario para PublisherLink
class PublisherLinkForm(forms.ModelForm):
    class Meta:
        model = PublisherLink
        fields = ['publisher', 'name', 'url', 'is_active']

    publisher = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Editor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'publisher'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un editor.'),
        },
    )

    name = forms.CharField(
        max_length=150,
        strip=True,
        required=True,
        label=_('Nombre'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Nombre del enlace'),
                'autocomplete': 'off',
                'id': 'name'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un nombre.'),
            'max_length': _('El nombre excede el largo permitido.'),
        },
    )

    url = forms.CharField(
        required=True,
        strip=True,
        max_length= 2000,
        label=_('URL'),
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('URL'),
                'id': 'url',
                'autocomplete': 'off',
                'type': 'url',
            }
        ),
        error_messages={
            'required': _('Debe ingresar una URL.'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la web del editor.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['publisher'].queryset = Publisher.objects.filter(is_active=True)

    def clean_name(self):
        return self.cleaned_data['name'].strip()

    def clean_url(self):
        url = self.cleaned_data.get('url', '').strip()
        return validate_url(url)

    def clean(self):
        cleaned_data = super().clean()
        publisher = cleaned_data.get('publisher')
        name = cleaned_data.get('name')
        url = cleaned_data.get('url')

        if publisher and name and url:
            exists = PublisherLink.objects.exclude(pk=self.instance.pk).filter(
                publisher=publisher,
                name__iexact=name.strip(),
                url__iexact=url.strip()
            )
            if exists.exists():
                raise forms.ValidationError(_('Ya existe un enlace con el mismo nombre y URL para este editor.'))

        return cleaned_data

########################################################################################################    Formulario para DeveloperImage
class DeveloperImageForm(forms.ModelForm):
    class Meta:
        model = DeveloperImage
        fields = ['developer', 'size_image', 'image', 'image_url', 'is_active']

    developer = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Desarrollador'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'developer'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un desarrollador.'),
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
        strip=True,
        max_length= 2000,
        label=_('URL'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen del desarrollador.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['developer'].queryset = Developer.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

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

########################################################################################################    Formulario para DeveloperImageExtra
class DeveloperImageExtraForm(forms.ModelForm):
    class Meta:
        model = DeveloperImageExtra
        fields = ['developer', 'image', 'is_active']

    developer = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Desarrollador'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'developer'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un desarrollador.'),
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

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional del desarrollador.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['developer'].queryset = Developer.objects.filter(is_active=True)

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

########################################################################################################    Formulario para TranslatorImage
class TranslatorImageForm(forms.ModelForm):
    class Meta:
        model = TranslatorImage
        fields = ['translator', 'size_image', 'image', 'image_url', 'is_active']

    translator = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Traductor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'translator'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un traductor.'),
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
        strip=True,
        max_length= 2000,
        label=_('URL'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen del traductor.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['translator'].queryset = Translator.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

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

########################################################################################################    Formulario para TranslatorImageExtra
class TranslatorImageExtraForm(forms.ModelForm):
    class Meta:
        model = TranslatorImageExtra
        fields = ['translator', 'image', 'is_active']

    translator = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Traductor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'translator'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un traductor.'),
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

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional del traductor.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['translator'].queryset = Translator.objects.filter(is_active=True)

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

########################################################################################################    Formulario para PublisherImage
class PublisherImageForm(forms.ModelForm):
    class Meta:
        model = PublisherImage
        fields = ['publisher', 'size_image', 'image', 'image_url', 'is_active']

    publisher = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Editor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'publisher'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un editor.'),
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
        strip=True,
        max_length= 2000,
        label=_('URL'),
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
                'title': _('Marcar para activar o desmarcar para desactivar la imagen del editor.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['publisher'].queryset = Publisher.objects.filter(is_active=True)
        self.fields['size_image'].queryset = ImageSize.objects.filter(is_active=True)

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

########################################################################################################    Formulario para PublisherImageExtra
class PublisherImageExtraForm(forms.ModelForm):
    class Meta:
        model = PublisherImageExtra
        fields = ['publisher', 'image', 'is_active']

    publisher = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Editor'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'publisher'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un editor.'),
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

    is_active = forms.BooleanField(
        required=False,
        label=_('Activo'),
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'is_active',
                'title': _('Marcar para activar o desmarcar para desactivar la imagen adicional del editor.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['publisher'].queryset = Publisher.objects.filter(is_active=True)

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

########################################################################################################    Formulario para TitleGame
class TitleGameForm(forms.ModelForm):
    class Meta:
        model = TitleGame
        fields = ['game', 'language', 'title', 'is_active']

    game = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Juego'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'game'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un juego.'),
        },
    )

    language = forms.ModelChoiceField(
        queryset=None,
        required=True,
        label=_('Idioma'),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'language'
            }
        ),
        error_messages={
            'required': _('Debe seleccionar un idioma.'),
        },
    )

    title = forms.CharField(
        max_length=20000,
        strip=True,
        required=True,
        label=_('Título'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Título'),
                'autocomplete': 'off',
                'id': 'title'
            }
        ),
        error_messages={
            'required': _('Debe ingresar un título.'),
            'max_length': _('El título excede el largo permitido.')
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
                'title': _('Marcar para activar o desmarcar para desactivar el título del jeugo.'),
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].queryset = Game.objects.filter(is_active=True)
        self.fields['language'].queryset = Language.objects.filter(is_active=True)

    def clean_title(self):
        return self.cleaned_data['title'].strip()

    def clean(self):
        cleaned_data = super().clean()
        game = cleaned_data.get('game')
        language = cleaned_data.get('language')
        title = cleaned_data.get('title')

        if game and language and title:
            exists = TitleGame.objects.exclude(pk=self.instance.pk).filter(
                game=game,
                language=language,
                title__iexact=title.strip()
            )
            if exists.exists():
                raise forms.ValidationError(_('Ya existe este título para el juego e idioma seleccionados.'))
        return cleaned_data

# class F95GameFetchStatusForm(forms.ModelForm):
#     class Meta:
#         model = F95GameFetchStatus
#         fields = ['url', 'f95_id', 'status', 'processed', 'data']

#     url = forms.URLField(
#         required=False,
#         label=_('URL'),
#         widget=forms.URLInput(attrs={
#             'class': 'form-control',
#             'placeholder': _('URL del juego'),
#             'id': 'url'
#         })
#     )

#     f95_id = forms.IntegerField(
#         required=True,
#         label=_('ID F95Zone'),
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'id': 'f95_id'
#         })
#     )

#     status = forms.BooleanField(
#         required=False,
#         initial=False,
#         label=_('Estado'),
#         widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'status'})
#     )

#     processed = forms.BooleanField(
#         required=False,
#         initial=False,
#         label=_('Procesado'),
#         widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'processed'})
#     )

#     data = forms.JSONField(
#         required=False,
#         label=_('Datos'),
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'rows': 5,
#             'id': 'data'
#         })
#     )

#     def clean(self):
#         cleaned_data = super().clean()
#         f95_id = cleaned_data.get('f95_id')
#         url = cleaned_data.get('url')
#         status = cleaned_data.get('status')

#         if f95_id is not None:
#             exists = F95GameFetchStatus.objects.exclude(pk=self.instance.pk).filter(
#                 f95_id=f95_id,
#                 url=url,
#                 status=status,
#             )
#             if exists.exists():
#                 raise forms.ValidationError(_('Ya existe un estado con el mismo ID, URL y estado.'))

#         return cleaned_data
class LoadGamesForm(forms.Form):
    inicio = forms.IntegerField(label="Inicio", min_value=1)
    fin = forms.IntegerField(label="Fin", min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Obtener el último ID del modelo F95GameFetchStatus
        ultimo_id = F95GameFetchStatus.objects.order_by('-f95_id').values_list('f95_id', flat=True).first() or 1
        self.fields['inicio'].initial = ultimo_id

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get("inicio")
        fin = cleaned_data.get("fin")

        if inicio is not None and fin is not None and fin < inicio:
            raise forms.ValidationError("El campo 'Fin' debe ser mayor o igual que 'Inicio'.")
        return cleaned_data
