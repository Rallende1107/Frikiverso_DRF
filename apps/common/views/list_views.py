# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)

# Local app imports - Models
from apps.common.models import (Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Country
class CountryListView(PermissionRequiredMessageMixin, ListView):
    model = Country
    template_name = Templates.Common.Country.LST
    context_object_name = 'country'
    title = _('Lista de Países')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for country in context[self.context_object_name]:
            # Combina el nombre y las iniciales en inglés
            if country.code:
                country.combined_name = f'{country.name} ({country.code})'
            else:
                country.combined_name = country.name

            # Combina el nombre y las iniciales en español
            if country.name_esp:
                country.combined_name_esp = f'{country.name_esp} ({country.code})'
            else:
                country.combined_name_esp = country.name_esp

        context['title'] = self.title
        context['class'] = CSSBackground.Common.COUNTRY
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.COUNTRY
        context['key_map'] = KeyMap.Common.COUNTRY
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Country.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Format
class FormatListView(PermissionRequiredMessageMixin, ListView):
    model = Format
    template_name = Templates.Common.Format.LST
    context_object_name = 'formats'
    title = _('Lista de Formatos')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.FORMAT
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.FORMAT
        context['key_map'] = KeyMap.Common.FORMAT
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Format.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    ImageSize
class ImageSizeListView(PermissionRequiredMessageMixin, ListView):
    model = ImageSize
    template_name = Templates.Common.ImageSize.LST
    context_object_name = 'imagesizes'
    title = _('Lista de Tamaños de Imágenes')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.IMAGE_SIZE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.IMAGE_SIZE
        context['key_map'] = KeyMap.Common.IMAGE_SIZE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.ImageSize.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Language
class LanguageListView(PermissionRequiredMessageMixin, ListView):
    model = Language
    template_name = Templates.Common.Language.LST
    context_object_name = 'languages'
    title = _('Lista de Idiomas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for language in context[self.context_object_name]:
            # Combina el nombre y las iniciales en inglés
            if language.acronym:
                language.combined_language = f'{language.name} ({language.acronym})'
            else:
                language.combined_language = language.name

            # Combina el nombre y las iniciales en español
            if language.name_esp:
                language.combined_language_esp = f'{language.name_esp} ({language.acronym})'
            else:
                language.combined_language_esp = language.name_esp

        context['title'] = self.title
        context['class'] = CSSBackground.Common.LANGUAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.LANGUAGE
        context['key_map'] = KeyMap.Common.LANGUAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Language.ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Person
class PersonListView(PermissionRequiredMessageMixin, ListView):
    model = Person
    template_name = Templates.Common.Person.LST
    context_object_name = 'persons'
    title = _('Lista de Personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON
        context['key_map'] = KeyMap.Common.PERSON
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Person.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    PersonImage
class PersonImageListView(PermissionRequiredMessageMixin, ListView):
    model = PersonImage
    template_name = Templates.Common.PersonImage.LST
    context_object_name = 'images'
    title = _('Lista de imágenes de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for img in context[self.context_object_name]:
            # Si la relación 'anime' es un ForeignKey, accedemos directamente a la propiedad 'anime'
            img.person_name = img.get_object_name()
            # Obtener el nombre y la extensión de la imagen
            img.image_name = img.get_object_name()

            # Obtener la URL de la imagen si está disponible
            img.image_url_local = img.get_img_url()
            img.image_url_external = img.image_url if img.image_url else None

        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON_IMAGE
        context['key_map'] = KeyMap.Common.PERSON_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.PersonImage.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    PersonImageExtra
class PersonImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = PersonImageExtra
    template_name = Templates.Common.PersonImageExtra.LST
    context_object_name = 'images'
    title = _('Lista de imagenes adicionales de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for img in context[self.context_object_name]:
            # Si la relación 'anime' es un ForeignKey, accedemos directamente a la propiedad 'anime'
            img.person_name = img.get_object_name()
            # Obtener el nombre y la extensión de la imagen
            img.image_name = img.get_object_name()

            # Obtener la URL de la imagen si está disponible
            img.image_url_local = img.get_img_url()

        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON_IMAGE_EXTRA
        context['key_map'] = KeyMap.Common.PERSON_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.PersonImageExtra.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    PersonNickname
class PersonNicknameListView(PermissionRequiredMessageMixin, ListView):
    model = PersonNickname
    template_name = Templates.Common.PersonNickname.LST
    context_object_name = 'nicknames'
    title = _('Lista de Apodos de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON_NICKNAME
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON_NICKNAME
        context['key_map'] = KeyMap.Common.PERSON_NICKNAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.PersonNickname.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Quality
class QualityListView(PermissionRequiredMessageMixin, ListView):
    model = Quality
    template_name = Templates.Common.Quality.LST
    context_object_name = 'qualitys'
    title = _('Lista de Calidades')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.QUALITY
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.QUALITY
        context['key_map'] = KeyMap.Common.QUALITY
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Quality.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Website
class WebsiteListView(PermissionRequiredMessageMixin, ListView):
    model = Website
    template_name = Templates.Common.Website.LST
    context_object_name = 'websites'
    title = _('Lista de Sitios Web\'s')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for website in context[self.context_object_name]:
            # Combina el nombre y el acrónimo
            if website.acronym:
                website.display_name = f"{website.name} ({website.acronym})"
                website.display_link = website.acronym  # Solo el acrónimo
            else:
                website.display_name = website.name
                website.display_link = website.name  # Solo el nombre


        context['title'] = self.title
        context['class'] = CSSBackground.Common.WEBSITE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.WEBSITE
        context['key_map'] = KeyMap.Common.WEBSITE
        # print('🔑 Key Map:', context['key_map'])  # Debug por consola

        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Website.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

