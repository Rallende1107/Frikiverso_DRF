# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)

# Local app imports - Models
# from apps.renpy.models import (F95GameFetchStatus,)
from apps.renpy.models import (
    Censorship, Developer, DeveloperImage, DeveloperImageExtra, DeveloperLink,
    Game, GameEngine, GameImage, GameImageExtra, Genre, Platform, Prefix, Publisher, PublisherImage,
    PublisherImageExtra, PublisherLink, Status, TitleGame, Translator, TranslatorImage, TranslatorImageExtra, TranslatorLink
    )

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Censorship
class CensorshipListView(PermissionRequiredMessageMixin, ListView):
    model = Censorship
    template_name = Templates.Renpy.Censorship.LIST
    context_object_name = 'censorships'
    title = _('Lista de Censuras')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.CENSORSHIP
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.CENSORSHIP
        context['key_map'] = KeyMap.Renpy.CENSORSHIP
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Censorship.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class DeveloperListView(PermissionRequiredMessageMixin, ListView):
    model = Developer
    template_name = Templates.Renpy.Developer.LIST
    context_object_name = 'developers'
    title = _('Lista de Desarolladores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.DEVELOPER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.DEVELOPER
        context['key_map'] = KeyMap.Renpy.DEVELOPER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Developer.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Renpy.DeveloperLink.LIST),
                'label': _('Enlaces'),
                'icon': 'bi bi-plus-circle',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.DeveloperLink.CREATE),
                'label': _('Anadir Enlace'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Censorship
############################################################################################################################################    Censorship
class DeveloperImageListView(PermissionRequiredMessageMixin, ListView):
    model = DeveloperImage
    template_name = Templates.Renpy.DeveloperImage.LIST
    context_object_name = 'developer_images'
    title = _('Lista de Imágenes de Desarrolladores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.DEVELOPER_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.DEVELOPER_IMAGE
        context['key_map'] = KeyMap.Renpy.DEVELOPER_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.DeveloperImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class DeveloperImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = DeveloperImageExtra
    template_name = Templates.Renpy.DeveloperImageExtra.LIST
    context_object_name = 'developer_images_extra'
    title = _('Lista de Imágenes Extra de Desarrolladores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.DEVELOPER_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.DEVELOPER_IMAGE_EXTRA
        context['key_map'] = KeyMap.Renpy.DEVELOPER_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.DeveloperImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class DeveloperLinkListView(PermissionRequiredMessageMixin, ListView):
    model = DeveloperLink
    template_name = Templates.Renpy.DeveloperLink.LIST
    context_object_name = 'developer_links'
    title = _('Lista de Enlaces de Desarrolladores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.DEVELOPER_LINK
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.DEVELOPER_LINK
        context['key_map'] = KeyMap.Renpy.DEVELOPER_LINK
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.DeveloperLink.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.LIST
    context_object_name = 'games'
    title = _('Lista de Juegos')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.GAME
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.GAME
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Game.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Renpy.Game.LOAD),
                'label': _('Cargar'),
                'icon': 'bi bi-cloud-arrow-up',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameEngineListView(PermissionRequiredMessageMixin, ListView):
    model = GameEngine
    template_name = Templates.Renpy.GameEngine.LIST
    context_object_name = 'game_engines'
    title = _('Lista de Motores de Desarrollo')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.GAME_ENGINE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.GAME_ENGINE
        context['key_map'] = KeyMap.Renpy.GAME_ENGINE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.GameEngine.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameImageListView(PermissionRequiredMessageMixin, ListView):
    model = GameImage
    template_name = Templates.Renpy.GameImage.LIST
    context_object_name = 'game_images'
    title = _('Lista de Imágenes de Juegos')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.GAME_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.GAME_IMAGE
        context['key_map'] = KeyMap.Renpy.GAME_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.GameImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = GameImageExtra
    template_name = Templates.Renpy.GameImageExtra.LIST
    context_object_name = 'game_extra_images'
    title = _('Lista de Imágenes Extra de Juegos')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.GAME_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.GAME_IMAGE_EXTRA
        context['key_map'] = KeyMap.Renpy.GAME_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.GameImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context


class GenreListView(PermissionRequiredMessageMixin, ListView):
    model = Genre
    template_name = Templates.Renpy.Genre.LIST
    context_object_name = 'genres'
    title = _('Lista de Géneros')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.GENRE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.GENRE
        context['key_map'] = KeyMap.Renpy.GENRE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Genre.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PlatformListView(PermissionRequiredMessageMixin, ListView):
    model = Platform
    template_name = Templates.Renpy.Platform.LIST
    context_object_name = 'platforms'
    title = _('Lista de Plataformas')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.PLATFORM
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PLATFORM
        context['key_map'] = KeyMap.Renpy.PLATFORM
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Platform.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PrefixListView(PermissionRequiredMessageMixin, ListView):
    model = Prefix
    template_name = Templates.Renpy.Prefix.LIST
    context_object_name = 'prefixes'
    title = _('Lista de Prefijos')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.PREFIX
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PREFIX
        context['key_map'] = KeyMap.Renpy.PREFIX
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Prefix.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PublisherListView(PermissionRequiredMessageMixin, ListView):
    model = Publisher
    template_name = Templates.Renpy.Publisher.LIST
    context_object_name = 'publishers'
    title = _('Lista de Editores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.PUBLISHER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PUBLISHER
        context['key_map'] = KeyMap.Renpy.PUBLISHER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Publisher.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PublisherImageListView(PermissionRequiredMessageMixin, ListView):
    model = PublisherImage
    template_name = Templates.Renpy.PublisherImage.LIST
    context_object_name = 'publisher_images'
    title = _('Lista de Imágenes de Editores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.PUBLISHER_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PUBLISHER_IMAGE
        context['key_map'] = KeyMap.Renpy.PUBLISHER_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.PublisherImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context


class PublisherImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = PublisherImageExtra
    template_name = Templates.Renpy.PublisherImageExtra.LIST
    context_object_name = 'publisher_image_extras'
    title = _('Lista de Imágenes Extra de Editores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.PUBLISHER_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PUBLISHER_IMAGE_EXTRA
        context['key_map'] = KeyMap.Renpy.PUBLISHER_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.PublisherImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PublisherLinkListView(PermissionRequiredMessageMixin, ListView):
    model = PublisherLink
    template_name = Templates.Renpy.PublisherLink.LIST
    context_object_name = 'publisher_links'
    title = _('Lista de Enlaces de Editores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.PUBLISHER_LINK
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PUBLISHER_LINK
        context['key_map'] = KeyMap.Renpy.PUBLISHER_LINK
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.PublisherLink.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class StatusListView(PermissionRequiredMessageMixin, ListView):
    model = Status
    template_name = Templates.Renpy.Status.LIST
    context_object_name = 'statuses'
    title = _('Lista de Estados')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.STATUS
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.STATUS
        context['key_map'] = KeyMap.Renpy.STATUS
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Status.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class TranslatorListView(PermissionRequiredMessageMixin, ListView):
    model = Translator
    template_name = Templates.Renpy.Translator.LIST
    context_object_name = 'translators'
    title = _('Lista de Traductores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.TRANSLATOR
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.TRANSLATOR
        context['key_map'] = KeyMap.Renpy.TRANSLATOR
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Translator.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context


class TranslatorImageListView(PermissionRequiredMessageMixin, ListView):
    model = TranslatorImage
    template_name = Templates.Renpy.TranslatorImage.LIST
    context_object_name = 'translator_images'
    title = _('Lista de Imágenes de Traductores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.TRANSLATOR_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.TRANSLATOR_IMAGE
        context['key_map'] = KeyMap.Renpy.TRANSLATOR_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.TranslatorImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class TranslatorImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = TranslatorImageExtra
    template_name = Templates.Renpy.TranslatorImageExtra.LIST
    context_object_name = 'translator_image_extras'
    title = _('Lista de Imágenes Extra de Traductores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.TRANSLATOR_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.TRANSLATOR_IMAGE_EXTRA
        context['key_map'] = KeyMap.Renpy.TRANSLATOR_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.TranslatorImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class TranslatorLinkListView(PermissionRequiredMessageMixin, ListView):
    model = TranslatorLink
    template_name = Templates.Renpy.TranslatorLink.LIST
    context_object_name = 'translator_links'
    title = _('Lista de Enlaces de Traductores')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.TRANSLATOR_LINK
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.TRANSLATOR_LINK
        context['key_map'] = KeyMap.Renpy.TRANSLATOR_LINK
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.TranslatorLink.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context


class TitleGameListView(PermissionRequiredMessageMixin, ListView):
    model = TitleGame
    template_name = Templates.Renpy.TitleGame.LIST
    context_object_name = 'title_games'
    title = _('Lista de Títulos de Juegos')
    permission_redirect_url = URLS.Home.RENPY

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Renpy.TITLE_GAME
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.TITLE_GAME
        context['key_map'] = KeyMap.Renpy.TITLE_GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.TitleGame.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context



