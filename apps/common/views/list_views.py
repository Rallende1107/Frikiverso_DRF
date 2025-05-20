# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)

# Local app imports - Models
from apps.common.models import (Company, Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Company
class CompanyListView(PermissionRequiredMessageMixin, ListView):
    model = Company
    template_name = Templates.Common.Company.LIST
    context_object_name = 'companies'
    title = _('Lista de compañias')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for country in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Common.COMPANY
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.COMPANY
        context['key_map'] = KeyMap.Common.COMPANY
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Company.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Country
class CountryListView(PermissionRequiredMessageMixin, ListView):
    model = Country
    template_name = Templates.Common.Country.LIST
    context_object_name = 'countries'
    title = _('Lista de países')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for country in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.Country.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Format
class FormatListView(PermissionRequiredMessageMixin, ListView):
    model = Format
    template_name = Templates.Common.Format.LIST
    context_object_name = 'formats'
    title = _('Lista de formatos')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.Format.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    ImageSize
class ImageSizeListView(PermissionRequiredMessageMixin, ListView):
    model = ImageSize
    template_name = Templates.Common.ImageSize.LIST
    context_object_name = 'images_sizes'
    title = _('Lista de tamaños de imágenes')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.ImageSize.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Language
class LanguageListView(PermissionRequiredMessageMixin, ListView):
    model = Language
    template_name = Templates.Common.Language.LIST
    context_object_name = 'languages'
    title = _('Lista de idiomas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for language in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.Language.CREATE),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Person
class PersonListView(PermissionRequiredMessageMixin, ListView):
    model = Person
    template_name = Templates.Common.Person.LIST
    context_object_name = 'persons'
    title = _('Lista de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.Person.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    PersonImage
class PersonImageListView(PermissionRequiredMessageMixin, ListView):
    model = PersonImage
    template_name = Templates.Common.PersonImage.LIST
    context_object_name = 'images'
    title = _('Lista de imágenes de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for img in context[self.context_object_name]:
            img.person_name = img.get_object_name()
            img.image_name = img.get_image_name()
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
                'url': reverse_lazy(URLS.Common.PersonImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    PersonImageExtra
class PersonImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = PersonImageExtra
    template_name = Templates.Common.PersonImageExtra.LIST
    context_object_name = 'images'
    title = _('Lista de imágenes adicionales de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for img in context[self.context_object_name]:
            img.person_name = img.get_object_name()
            img.image_name = img.get_image_name()
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
                'url': reverse_lazy(URLS.Common.PersonImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    PersonNickname
class PersonNicknameListView(PermissionRequiredMessageMixin, ListView):
    model = PersonNickname
    template_name = Templates.Common.PersonNickname.LIST
    context_object_name = 'nicknames'
    title = _('Lista de apodos de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.PersonNickname.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Quality
class QualityListView(PermissionRequiredMessageMixin, ListView):
    model = Quality
    template_name = Templates.Common.Quality.LIST
    context_object_name = 'qualities'
    title = _('Lista de calidades')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for ccc in context[self.context_object_name]:
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
                'url': reverse_lazy(URLS.Common.Quality.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Website
class WebsiteListView(PermissionRequiredMessageMixin, ListView):
    model = Website
    template_name = Templates.Common.Website.LIST
    context_object_name = 'web_sites'
    title = _('Lista de sitios webs')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for website in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Common.WEBSITE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.WEBSITE
        context['key_map'] = KeyMap.Common.WEBSITE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Website.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context