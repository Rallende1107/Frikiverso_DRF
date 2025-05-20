# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)
from django.views.generic.edit import FormView
# Local app imports - Models
# from apps.renpy.models import (F95GameFetchStatus,)
from apps.renpy.models import (
    Censorship, Developer, DeveloperImage, DeveloperImageExtra, DeveloperLink,
    Game, GameEngine, GameImage, GameImageExtra, Genre, Platform, Prefix, Publisher, PublisherImage,
    PublisherImageExtra, PublisherLink, Status, TitleGame, Translator, TranslatorImage, TranslatorImageExtra, TranslatorLink
    )

# from apps.renpy.forms import (F95GameFetchStatus,)
from apps.renpy.forms import (LoadGamesForm)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################
class GameByDeveloperListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        return Game.objects.filter(developers__id=self.kwargs['developer_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        developer = Developer.objects.get(id=self.kwargs['developer_id'])
        context['developer'] = developer
        context['title'] = _('Juegos desarrollados por %(developer)s') % {'developer': developer.name}
        context['class'] = CSSBackground.Renpy.DEVELOPER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.DEVELOPER
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Developer.LIST),
                'label': _('Desarrolladores'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GameByStatusListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        return Game.objects.filter(status__id=self.kwargs['status_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = Status.objects.get(id=self.kwargs['status_id'])
        context['status'] = status
        context['title'] = _('Juegos en estado  %(status)s') % {'status': status.name}
        context['class'] = CSSBackground.Renpy.STATUS
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.STATUS
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Status.LIST),
                'label': _('Estados'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GameByPlatformListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        return Game.objects.filter(platforms__id=self.kwargs['platform_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        platform = Platform.objects.get(id=self.kwargs['platform_id'])
        context['platform'] = platform
        context['title'] = _('Juegos para %(platform)s') % {'platform': platform.name}
        context['class'] = CSSBackground.Renpy.PLATFORM
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PLATFORM
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Platform.LIST),
                'label': _('Plataformas'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GameByEngineListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated


    def get_queryset(self):
        return Game.objects.filter(engine__id=self.kwargs['engine_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        engine = GameEngine.objects.get(id=self.kwargs['engine_id'])
        context['engine'] = engine
        context['title'] = _('Juegos desarrollador en %(name)s') % {'name': engine.name}
        context['class'] = CSSBackground.Renpy.ENGINE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.ENGINE
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.GameEngine.LIST),
                'label': _('Motores de Desarrollo'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GameByGenreListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated


    def get_queryset(self):
        return Game.objects.filter(genres__id=self.kwargs['genre_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.get(id=self.kwargs['genre_id'])
        context['genre'] = genre
        context['title'] = _('Juegos con el género %(name)s') % {'name': genre.name}
        context['class'] = CSSBackground.Renpy.GENRE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.GENRE
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Genre.LIST),
                'label': _('Géneros'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GameByTranslatorListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        return Game.objects.filter(translators__id=self.kwargs['translator_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        translator = Translator.objects.get(id=self.kwargs['translator_id'])
        context['translator'] = translator
        context['title'] = _('Juegos traducidos por %(name)s') % {'name': translator.name}
        context['class'] = CSSBackground.Renpy.TRANSLATOR
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.TRANSLATOR
        context['key_map'] = KeyMap.Renpy.GAME

        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Translator.LIST),
                'label': _('Traductores'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GameByPublisherListView(PermissionRequiredMessageMixin, ListView):
    model = Game
    template_name = Templates.Renpy.Game.GAME_BY
    context_object_name = 'games'
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        return Game.objects.filter(publishers__id=self.kwargs['publisher_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publisher = Publisher.objects.get(id=self.kwargs['publisher_id'])
        context['publisher'] = publisher
        context['title'] = _('Juegos editados por %(name)s') % {'name': publisher.name}
        context['class'] = CSSBackground.Renpy.PUBLISHER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Renpy.PUBLISHER
        context['key_map'] = KeyMap.Renpy.GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.RENPY),
                'label': _('Inicio'),
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Renpy.Publisher.LIST),
                'label': _('Editores'),
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context




