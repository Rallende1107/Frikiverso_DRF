# Django imports
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (UpdateView,)

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
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    Country
class CensorshipUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Censorship
    form_class = CensorshipForm
    template_name = Templates.Renpy.Censorship.UPDATE
    success_url = reverse_lazy(URLS.Renpy.Censorship.CREATE)
    title = _('Editar Censura')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡La Censura "%(name)s" fue editada exitosamente!') % {'name': name})
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
class DeveloperUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = Templates.Renpy.Developer.UPDATE
    success_url = reverse_lazy(URLS.Renpy.Developer.LIST)
    title = _('Editar Desarrollado')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El desarrollador "%(name)s" fue editado exitosamente!') % {'name': name})
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

############################################################################################################################################    Developer
############################################################################################################################################    Developer
############################################################################################################################################    Developer
class DeveloperImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = DeveloperImage
    form_class = DeveloperImageForm
    template_name = Templates.Renpy.DeveloperImage.CREATE
    success_url = reverse_lazy(URLS.Renpy.DeveloperImage.LIST)
    title = _('Editar imagen de desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        developer_name = form.instance.developer.name
        messages.success(self.request, _('¡La Imagen del desarrollador "%(name)s" fue actualizada exitosamente!') % {'name': developer_name})
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

class DeveloperImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = DeveloperImageExtra
    form_class = DeveloperImageExtraForm
    template_name = Templates.Renpy.DeveloperImageExtra.CREATE
    success_url = reverse_lazy(URLS.Renpy.DeveloperImageExtra.LIST)
    title = _('Editar imagen adicional desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        developer_name = form.instance.developer.name
        messages.success(self.request, _('¡La Imagen adicional del desarrollador "%(name)s" fue actualizada exitosamente!') % {'name': developer_name})
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

class DeveloperLinkUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = DeveloperLink
    form_class = DeveloperLinkForm
    template_name = Templates.Renpy.DeveloperLink.CREATE
    success_url = reverse_lazy(URLS.Renpy.DeveloperLink.LIST)
    title = _('Editar enlace de desarrollador')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        developer_name = form.instance.developer.name
        messages.success(self.request, _('¡El enlace del desarrollador "%(name)s" fue actualizado exitosamente!') % {'name': developer_name})
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

class GameUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = Templates.Renpy.Game.CREATE
    success_url = reverse_lazy(URLS.Renpy.Game.LIST)
    title = _('Editar Juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('title')
        messages.success(self.request, _('¡El Juego "%(name)s" fue actualizado exitosamente!') % {'name': name})
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

class GameEngineUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = GameEngine
    form_class = GameEngineForm
    template_name = Templates.Renpy.GameEngine.CREATE
    success_url = reverse_lazy(URLS.Renpy.GameEngine.LIST)
    title = _('Editar motor de desarrollo')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El motor de desarrollo "%(name)s" fue actualizado exitosamente!') % {'name': name})
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


class GameImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = GameImage
    form_class = GameImageForm
    template_name = Templates.Renpy.GameImage.CREATE
    success_url = reverse_lazy(URLS.Renpy.GameImage.LIST)
    title = _('Editar imagen de juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        game_name = form.instance.game.title
        messages.success(self.request, _('¡La Imagen del juego "%(name)s" fue actualizada exitosamente!') % {'name': game_name})
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


class GameImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = GameImageExtra
    form_class = GameImageExtraForm
    template_name = Templates.Renpy.GameImageExtra.CREATE
    success_url = reverse_lazy(URLS.Renpy.GameImageExtra.LIST)
    title = _('Editar imagen adicional juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        game_name = form.instance.game.title
        messages.success(self.request, _('¡La Imagen adicional del juego "%(name)s" fue actualizada exitosamente!') % {'name': game_name})
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

class GenreUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Renpy.Genre.CREATE
    success_url = reverse_lazy(URLS.Renpy.Genre.LIST)
    title = _('Editar Género')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Género "%(name)s" fue actualizado exitosamente!') % {'name': name})
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

class PlatformUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Platform
    form_class = PlatformForm
    template_name = Templates.Renpy.Platform.CREATE
    success_url = reverse_lazy(URLS.Renpy.Platform.LIST)
    title = _('Editar Plataforma')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡La Plataforma "%(name)s" fue actualizada exitosamente!') % {'name': name})
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

class PrefixUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Prefix
    form_class = PrefixForm
    template_name = Templates.Renpy.Prefix.CREATE
    success_url = reverse_lazy(URLS.Renpy.Prefix.LIST)
    title = _('Editar prefijo')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El prefijo "%(name)s" fue actualizado exitosamente!') % {'name': name})
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

class PublisherUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = Templates.Renpy.Publisher.CREATE
    success_url = reverse_lazy(URLS.Renpy.Publisher.LIST)
    title = _('Editar Editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El editor "%(name)s" fue actualizado exitosamente!') % {'name': name})
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


class PublisherImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PublisherImage
    form_class = PublisherImageForm
    template_name = Templates.Renpy.PublisherImage.CREATE
    success_url = reverse_lazy(URLS.Renpy.PublisherImage.LIST)
    title = _('Editar imagen de editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        publisher_name = form.instance.publisher.name
        messages.success(self.request, _('¡La Imagen del editor "%(name)s" fue actualizada exitosamente!') % {'name': publisher_name})
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

class PublisherImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PublisherImageExtra
    form_class = PublisherImageExtraForm
    template_name = Templates.Renpy.PublisherImageExtra.CREATE
    success_url = reverse_lazy(URLS.Renpy.PublisherImageExtra.LIST)
    title = _('Editar imagen adicional editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        publisher_name = form.instance.publisher.name
        messages.success(self.request, _('¡La Imagen adicional del editor "%(name)s" fue actualizada exitosamente!') % {'name': publisher_name})
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


class PublisherLinkUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PublisherLink
    form_class = PublisherLinkForm
    template_name = Templates.Renpy.PublisherLink.CREATE
    success_url = reverse_lazy(URLS.Renpy.PublisherLink.LIST)
    title = _('Editar enlace de editor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        publisher_name = form.instance.publisher.name
        messages.success(self.request, _('¡El enlace del editor "%(name)s" fue actualizado exitosamente!') % {'name': publisher_name})
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


class StatusUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = Templates.Renpy.Status.CREATE
    success_url = reverse_lazy(URLS.Renpy.Status.LIST)
    title = _('Editar Estado')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El estado "%(name)s" fue actualizado exitosamente!') % {'name': name})
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

class TranslatorUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Translator
    form_class = TranslatorForm
    template_name = Templates.Renpy.Translator.CREATE
    success_url = reverse_lazy(URLS.Renpy.Translator.LIST)
    title = _('Editar Traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El traductor "%(name)s" fue actualizado exitosamente!') % {'name': name})
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

class TranslatorImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = TranslatorImage
    form_class = TranslatorImageForm
    template_name = Templates.Renpy.TranslatorImage.CREATE
    success_url = reverse_lazy(URLS.Renpy.TranslatorImage.LIST)
    title = _('Editar imagen de traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        translator_name = form.instance.translator.name
        messages.success(self.request, _('¡La Imagen del traductor "%(name)s" fue actualizada exitosamente!') % {'name': translator_name})
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




class TranslatorImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = TranslatorImageExtra
    form_class = TranslatorImageExtraForm
    template_name = Templates.Renpy.TranslatorImageExtra.CREATE
    success_url = reverse_lazy(URLS.Renpy.TranslatorImageExtra.LIST)
    title = _('Editar imagen adicional de traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        translator_name = form.instance.translator.name
        messages.success(self.request, _('¡La Imagen adicional del traductor "%(name)s" fue actualizada exitosamente!') % {'name': translator_name})
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

class TranslatorLinkUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = TranslatorLink
    form_class = TranslatorLinkForm
    template_name = Templates.Renpy.TranslatorLink.CREATE
    success_url = reverse_lazy(URLS.Renpy.TranslatorLink.LIST)
    title = _('Editar enlace de traductor')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        translator_name = form.instance.translator.name
        messages.success(self.request, _('¡El enlace del traductor "%(name)s" fue actualizado exitosamente!') % {'name': translator_name})
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

class TitleGameUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = TitleGame
    form_class = TitleGameForm
    template_name = Templates.Renpy.TitleGame.CREATE
    success_url = reverse_lazy(URLS.Renpy.TitleGame.LIST)
    title = _('Editar Título de Juego')
    permission_redirect_url = URLS.Home.RENPY

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.success(self.request, _('¡El título "%(title)s" fue actualizado exitosamente!') % {'title': title})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TITLE_GAME
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

