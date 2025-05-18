# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

# Local app imports - Models
# from apps.renpy.models import (F95GameFetchStatus,)
from apps.renpy.models import (
    Censorship, Developer, DeveloperImage, DeveloperImageExtra, DeveloperLink,
    Game, GameEngine, GameImage, GameImageExtra, Genre, Platform, Prefix, Publisher, PublisherImage,
    PublisherImageExtra, PublisherLink, Status, TitleGame, Translator, TranslatorImage, TranslatorImageExtra, TranslatorLink
    )

# Local app imports - Forms
# from apps.renpy.forms import (F95GameFetchStatusForm,)
from apps.renpy.forms import (
    CensorshipForm, DeveloperForm, DeveloperImageForm, DeveloperImageExtraForm, DeveloperLinkForm,
    GameForm, GameEngineForm, GameImageForm, GameImageExtraForm, GenreForm, PlatformForm, PrefixForm, PublisherForm, PublisherImageForm,
    PublisherImageExtraForm, PublisherLinkForm, StatusForm, TitleGameForm, TranslatorForm, TranslatorImageForm, TranslatorImageExtraForm, TranslatorLinkForm
    )

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Censorship
class CensorshipCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Censorship
    form_class = CensorshipForm
    template_name = Templates.Renpy.Censorship.ADD
    success_url = reverse_lazy(URLS.Renpy.Censorship.LST)
    title = _('Añadir Censura')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡La Censura "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.CENSORSHIP
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Developer
class DeveloperCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = Templates.Renpy.Developer.ADD
    success_url = reverse_lazy(URLS.Renpy.Developer.LST)
    title = _('Añadir Desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El desarrollador "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################
class DeveloperImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = DeveloperImage
    form_class = DeveloperImageForm
    template_name = Templates.Renpy.DeveloperImage.ADD
    success_url = reverse_lazy(URLS.Renpy.DeveloperImage.LST)
    title = _('Añadir imagen de desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        developer_name = form.instance.developer.name
        messages.success(self.request, _('¡La Imagen del desarrollador "%(name)s" fue creada exitosamente!') % {'name': developer_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class DeveloperImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = DeveloperImageExtra
    form_class = DeveloperImageExtraForm
    template_name = Templates.Renpy.DeveloperImageExtra.ADD
    success_url = reverse_lazy(URLS.Renpy.DeveloperImageExtra.LST)
    title = _('Añadir imagen adicional desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        developer_name = form.instance.developer.name
        messages.success(self.request, _('¡La Imagen adicional del desarrollador "%(name)s" fue creada exitosamente!') % {'name': developer_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class DeveloperLinkCreateView(PermissionRequiredMessageMixin, CreateView):
    model = DeveloperLink
    form_class = DeveloperLinkForm
    template_name = Templates.Renpy.DeveloperLink.ADD
    success_url = reverse_lazy(URLS.Renpy.DeveloperLink.LST)
    title = _('Añadir enlace de desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        developer_name = form.instance.developer.name
        messages.success(self.request, _('¡El enlace del desarrollador "%(name)s" fue creado exitosamente!') % {'name': developer_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = Templates.Renpy.Game.ADD
    success_url = reverse_lazy(URLS.Renpy.Game.LST)
    title = _('Añadir Juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('title')
        messages.success(self.request, _('¡El Juego "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameEngineCreateView(PermissionRequiredMessageMixin, CreateView):
    model = GameEngine
    form_class = GameEngineForm
    template_name = Templates.Renpy.GameEngine.ADD
    success_url = reverse_lazy(URLS.Renpy.GameEngine.LST)
    title = _('Añadir motor de desarrollo')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El motor de desarrollo "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME_ENGINE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = GameImage
    form_class = GameImageForm
    template_name = Templates.Renpy.GameImage.ADD
    success_url = reverse_lazy(URLS.Renpy.GameImage.LST)
    title = _('Añadir imagen de juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        game_name = form.instance.game.title
        messages.success(self.request, _('¡La Imagen del juego "%(name)s" fue creada exitosamente!') % {'name': game_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = GameImageExtra
    form_class = GameImageExtraForm
    template_name = Templates.Renpy.GameImageExtra.ADD
    success_url = reverse_lazy(URLS.Renpy.GameImageExtra.LST)
    title = _('Añadir imagen adicional juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        game_name = form.instance.game.title
        messages.success(self.request, _('¡La Imagen adicional del juego "%(name)s" fue creada exitosamente!') % {'name': game_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GenreCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Renpy.Genre.ADD
    success_url = reverse_lazy(URLS.Renpy.Genre.LST)
    title = _('Añadir Género')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Género "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PlatformCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Platform
    form_class = PlatformForm
    template_name = Templates.Renpy.Platform.ADD
    success_url = reverse_lazy(URLS.Renpy.Platform.LST)
    title = _('Añadir Plataforma')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡La Plataforma "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PLATFORM
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PrefixCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Prefix
    form_class = PrefixForm
    template_name = Templates.Renpy.Prefix.ADD
    success_url = reverse_lazy(URLS.Renpy.Prefix.LST)
    title = _('Añadir prefijo')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El prefijo "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PREFIX
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = Templates.Renpy.Publisher.ADD
    success_url = reverse_lazy(URLS.Renpy.Publisher.LST)
    title = _('Añadir Editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El editor "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = PublisherImage
    form_class = PublisherImageForm
    template_name = Templates.Renpy.PublisherImage.ADD
    success_url = reverse_lazy(URLS.Renpy.PublisherImage.LST)
    title = _('Añadir imagen de editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        publisher_name = form.instance.publisher.name
        messages.success(self.request, _('¡La Imagen del editor "%(name)s" fue creada exitosamente!') % {'name': publisher_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = PublisherImageExtra
    form_class = PublisherImageExtraForm
    template_name = Templates.Renpy.PublisherImageExtra.ADD
    success_url = reverse_lazy(URLS.Renpy.PublisherImageExtra.LST)
    title = _('Añadir imagen adicional editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        publisher_name = form.instance.publisher.name
        messages.success(self.request, _('¡La Imagen adicional del editor "%(name)s" fue creada exitosamente!') % {'name': publisher_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherLinkCreateView(PermissionRequiredMessageMixin, CreateView):
    model = PublisherLink
    form_class = PublisherLinkForm
    template_name = Templates.Renpy.PublisherLink.ADD
    success_url = reverse_lazy(URLS.Renpy.PublisherLink.LST)
    title = _('Añadir enlace de editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        publisher_name = form.instance.publisher.name
        messages.success(self.request, _('¡El enlace del editor "%(name)s" fue creado exitosamente!') % {'name': publisher_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class StatusCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = Templates.Renpy.Status.ADD
    success_url = reverse_lazy(URLS.Renpy.Status.LST)
    title = _('Añadir Estado')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El estado "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.STATUS
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Translator
    form_class = TranslatorForm
    template_name = Templates.Renpy.Translator.ADD
    success_url = reverse_lazy(URLS.Renpy.Translator.LST)
    title = _('Añadir Traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El traductor "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = TranslatorImage
    form_class = TranslatorImageForm
    template_name = Templates.Renpy.TranslatorImage.ADD
    success_url = reverse_lazy(URLS.Renpy.TranslatorImage.LST)
    title = _('Añadir imagen de traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        translator_name = form.instance.translator.name
        messages.success(self.request, _('¡La Imagen del traductor "%(name)s" fue creada exitosamente!') % {'name': translator_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = TranslatorImageExtra
    form_class = TranslatorImageExtraForm
    template_name = Templates.Renpy.TranslatorImageExtra.ADD
    success_url = reverse_lazy(URLS.Renpy.TranslatorImageExtra.LST)
    title = _('Añadir imagen adicional traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        translator_name = form.instance.translator.name
        messages.success(self.request, _('¡La Imagen adicional del traductor "%(name)s" fue creada exitosamente!') % {'name': translator_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorLinkCreateView(PermissionRequiredMessageMixin, CreateView):
    model = TranslatorLink
    form_class = TranslatorLinkForm
    template_name = Templates.Renpy.TranslatorLink.ADD
    success_url = reverse_lazy(URLS.Renpy.TranslatorLink.LST)
    title = _('Añadir enlace de traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        translator_name = form.instance.translator.name
        messages.success(self.request, _('¡El enlace del traductor "%(name)s" fue creado exitosamente!') % {'name': translator_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TitleGameCreateView(PermissionRequiredMessageMixin, CreateView):
    model = TitleGame
    form_class = TitleGameForm
    template_name = Templates.Renpy.TitleGame.ADD
    success_url = reverse_lazy(URLS.Renpy.TitleGame.LST)
    title = _('Añadir Título de Juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.success(self.request, _('¡El título "%(title)s" fue creado exitosamente!') % {'title': title})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TITLE_GAME  # Ajusta el enum según corresponda
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

