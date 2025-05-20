# Django imports
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (DetailView)

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
# ############################################################################################################################################
class CensorshipDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Censorship
    template_name = Templates.Renpy.Censorship.DETAIL
    context_object_name = 'censorship'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La censura que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Censorship.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Censorship, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.CENSORSHIP
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Censorship.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class DeveloperDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Developer
    template_name = Templates.Renpy.Developer.DETAIL
    context_object_name = 'developer'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El desarrollador que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Developer.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Developer, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Developer.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class DeveloperImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = DeveloperImage
    template_name = Templates.Renpy.DeveloperImage.DETAIL
    context_object_name = 'developer_image'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen del desarrollador no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.DeveloperImage.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(DeveloperImage, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER_IMAGE
        context['title'] = f"Imagen de {self.object.developer.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.DeveloperImage.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class DeveloperImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = DeveloperImageExtra
    template_name = Templates.Renpy.DeveloperImageExtra.DETAIL
    context_object_name = 'developer_image_extra'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen adicional del desarrollador no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.DeveloperImageExtra.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(DeveloperImageExtra, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER_IMAGE_EXTRA
        context['title'] = f"Imagen adicional de {self.object.developer.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.DeveloperImageExtra.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class DeveloperLinkDetailView(PermissionRequiredMessageMixin, DetailView):
    model = DeveloperLink
    template_name = Templates.Renpy.DeveloperLink.DETAIL
    context_object_name = 'developer_link'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El enlace del desarrollador no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.DeveloperLink.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(DeveloperLink, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.DEVELOPER_LINK
        context['title'] = f"Enlace de {self.object.developer.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.DeveloperLink.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class GameDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Game
    template_name = Templates.Renpy.Game.DETAIL
    context_object_name = 'game'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El juego que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Game.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Game, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME
        context['title'] = self.object.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Game.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class GameEngineDetailView(PermissionRequiredMessageMixin, DetailView):
    model = GameEngine
    template_name = Templates.Renpy.GameEngine.DETAIL
    context_object_name = 'game_engine'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El motor de desarrollo que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.GameEngine.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GameEngine, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME_ENGINE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.GameEngine.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class GameImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = GameImage
    template_name = Templates.Renpy.GameImage.DETAIL
    context_object_name = 'game_image'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen del juego no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.GameImage.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GameImage, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME_IMAGE
        context['title'] = f"Imagen de {self.object.game.title}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.GameImage.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class GameImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = GameImageExtra
    template_name = Templates.Renpy.GameImageExtra.DETAIL
    context_object_name = 'game_image_extra'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen adicional del juego no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.GameImageExtra.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GameImageExtra, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME_IMAGE_EXTRA
        context['title'] = f"Imagen adicional de {self.object.game.title}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.GameImageExtra.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class GenreDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Genre
    template_name = Templates.Renpy.Genre.DETAIL
    context_object_name = 'genre'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El género no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Genre.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Genre, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GENRE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Genre.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class PlatformDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Platform
    template_name = Templates.Renpy.Platform.DETAIL
    context_object_name = 'platform'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La plataforma no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Platform.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Platform, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PLATFORM
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Platform.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class PrefixDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Prefix
    template_name = Templates.Renpy.Prefix.DETAIL
    context_object_name = 'prefix'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El prefijo no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Prefix.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Prefix, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PREFIX
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Prefix.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class PublisherDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Publisher
    template_name = Templates.Renpy.Publisher.DETAIL
    context_object_name = 'publisher'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El editor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Publisher.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Publisher, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Publisher.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class PublisherImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = PublisherImage
    template_name = Templates.Renpy.PublisherImage.DETAIL
    context_object_name = 'publisher_image'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen del editor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.PublisherImage.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PublisherImage, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER_IMAGE
        context['title'] = f"Imagen de {self.object.publisher.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.PublisherImage.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class PublisherImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = PublisherImageExtra
    template_name = Templates.Renpy.PublisherImageExtra.DETAIL
    context_object_name = 'publisher_image_extra'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen adicional del editor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.PublisherImageExtra.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PublisherImageExtra, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER_IMAGE_EXTRA
        context['title'] = f"Imagen adicional de {self.object.publisher.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.PublisherImageExtra.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class PublisherLinkDetailView(PermissionRequiredMessageMixin, DetailView):
    model = PublisherLink
    template_name = Templates.Renpy.PublisherLink.DETAIL
    context_object_name = 'publisher_link'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El enlace del editor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.PublisherLink.LIST))
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PublisherLink, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.PUBLISHER_LINK
        context['title'] = f"Enlace de {self.object.publisher.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.PublisherLink.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context

class StatusDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Status
    template_name = Templates.Renpy.Status.DETAIL
    context_object_name = 'status'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('El estado no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Status.LIST))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.STATUS
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Status.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class TranslatorDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Translator
    template_name = Templates.Renpy.Translator.DETAIL
    context_object_name = 'translator'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('El traductor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.Translator.LIST))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.Translator.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class TranslatorImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = TranslatorImage
    template_name = Templates.Renpy.TranslatorImage.DETAIL
    context_object_name = 'translator_image'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('La imagen del traductor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.TranslatorImage.LIST))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR_IMAGE
        context['title'] = f"Imagen de {self.object.translator.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.TranslatorImage.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class TranslatorImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = TranslatorImageExtra
    template_name = Templates.Renpy.TranslatorImageExtra.DETAIL
    context_object_name = 'translator_image_extra'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('La imagen adicional del traductor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.TranslatorImageExtra.LIST))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR_IMAGE_EXTRA
        context['title'] = f"Imagen adicional de {self.object.translator.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.TranslatorImageExtra.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class TranslatorLinkDetailView(PermissionRequiredMessageMixin, DetailView):
    model = TranslatorLink
    template_name = Templates.Renpy.TranslatorLink.DETAIL
    context_object_name = 'translator_link'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('El enlace del traductor no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.TranslatorLink.LIST))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TRANSLATOR_LINK
        context['title'] = f"Enlace de {self.object.translator.name}"
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.TranslatorLink.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context


class TitleGameDetailView(PermissionRequiredMessageMixin, DetailView):
    model = TitleGame
    template_name = Templates.Renpy.TitleGame.DETAIL
    context_object_name = 'title_game'
    permission_redirect_url = URLS.Home.RENPY

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('El título de juego no se encontró.'))
            return redirect(reverse_lazy(URLS.Renpy.TitleGame.LIST))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.TITLE_GAME
        context['title'] = self.object.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Renpy.TitleGame.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context
















# class DeveloperDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Developer
#     template_name = TPL_RENPY_DEVELOPER_DTL
#     context_object_name = 'developer'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El desarrollador que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_DEVELOPER_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(Developer, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         objeto = self.get_object()
#         img_url = objeto.get_img_url()

#         context['objeto'] = self.object
#         context['links'] = self.object.links.filter(is_active=True)
#         context['class'] = BG_RENPY_DEVELOPER
#         context['img_url'] = img_url
#         context['title'] = self.object.name
#         context['listURL'] =  reverse_lazy(URL_RENPY_DEVELOPER_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context


# class TranslatorDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Translator
#     template_name = TPL_RENPY_TRANSLATOR_DTL
#     context_object_name = 'translator'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El traductor que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_TRANSLATOR_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(Translator, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         objeto = self.get_object()
#         img_url = objeto.get_img_url()

#         context['img_url'] = img_url
#         context['links'] = self.object.links.filter(is_active=True)
#         context['class'] = BG_RENPY_TRANSLATOR
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         context['listURL'] =  reverse_lazy(URL_RENPY_TRANSLATOR_LST)
#         return context






# class PublisherDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Publisher
#     template_name = TPL_RENPY_PUBLISHER_DTL
#     context_object_name = 'publisher'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El editor que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_PUBLISHER_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(Publisher, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         objeto = self.get_object()
#         img_url = objeto.get_img_url()
#         game_count = objeto.get_num_games()
#         context['game_count'] = game_count
#         context['img_url'] = img_url
#         context['links'] = self.object.links.filter(is_active=True)
#         context['class'] = BG_RENPY_PUBLISHER
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         context['listURL'] =  reverse_lazy(URL_RENPY_PUBLISHER_LST)
#         return context


# class DeveloperLinkDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = DeveloperLink
#     template_name = TPL_RENPY_DEVELOPER_LINK_DTL
#     context_object_name = 'developer_link'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El link de desarrollador que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(DeveloperLink, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         developer = self.object.developer
#         context['developer_name'] = developer.name if developer else "N/A"
#         context['developer'] = developer
#         context['class'] = BG_RENPY_DEVELOPER_LINK
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] =  reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context


# class TranslatorLinkDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = TranslatorLink
#     template_name = TPL_RENPY_TRANSLATOR_LINK_DTL
#     context_object_name = 'translator_link'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El link del traductor que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(TranslatorLink, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         translator = self.object.translator
#         context['translator_name'] = translator.name if translator else "N/A"
#         context['translator'] = translator
#         context['class'] = BG_RENPY_TRANSLATOR_LINK
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] =  reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context


# class PublisherLinkDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = PublisherLink
#     template_name = TPL_RENPY_PUBLISHER_LINK_DTL
#     context_object_name = 'publisher_link'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El link del editor que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(PublisherLink, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         publisher = self.object.publisher
#         context['publisher_name'] = publisher.name if publisher else "N/A"
#         context['publisher'] = publisher
#         context['class'] = BG_RENPY_PUBLISHER_LINK
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] =  reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context


# class GenreRenpyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = GenreRenpy
#     template_name = TPL_RENPY_GENRE_DTL
#     context_object_name = 'genre'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El género de juego que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_GENRE_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(GenreRenpy, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['game_count'] = self.object.get_num_games()
#         context['class'] = BG_RENPY_GENRE
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] = reverse_lazy(URL_RENPY_GENRE_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context

# class GameEngineDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = GameEngine
#     template_name = TPL_RENPY_ENGINE_DTL
#     context_object_name = 'engine'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El motor de desarrollo que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_ENGINE_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(GameEngine, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['game_count'] = self.object.get_num_games()
#         context['class'] = BG_RENPY_ENGINE
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] = reverse_lazy(URL_RENPY_ENGINE_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context

# class GameStateDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = GameState
#     template_name = TPL_RENPY_STATUS_DTL
#     context_object_name = 'game_statu'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El estado de juego que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_STATUS_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(GameState, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['game_count'] = self.object.get_num_games()
#         context['class'] = BG_RENPY_STATUS
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] = reverse_lazy(URL_RENPY_STATUS_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context

# class PlatformDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Platform
#     template_name = TPL_RENPY_PLATFORM_DTL
#     context_object_name = 'platform'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'La plataforma que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_PLATFORM_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(Platform, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['game_count'] = self.object.get_num_games()
#         context['class'] = BG_RENPY_PLATFORM
#         context['objeto'] = self.object
#         context['title'] = self.object.name
#         context['listURL'] = reverse_lazy(URL_RENPY_PLATFORM_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context


# class GameDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Game
#     template_name = TPL_RENPY_GAME_DTL
#     context_object_name = 'game'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'El juego que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_GAME_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(Game, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         game = self.object  # Obtén el objeto de juego actual
#         # Obtener los nombres de los desarrolladores
#         game.developer_names = ', '.join(dev.name for dev in game.developers.all())
#         # Obtener los nombres de los estados del juego
#         game.state_names = ', '.join(status.name for status in game.states.all())
#         # Obtener los nombres de los motores
#         game.engine_names = ', '.join(engine.name for engine in game.engines.all())
#         # Obtener los nombres de los géneros
#         game.genre_names = ', '.join(genre.name for genre in game.genres.all())
#         # Obtener los nombres de las plataformas
#         game.platform_names = ', '.join(platform.name for platform in game.platforms.all())
#         # Obtener los nombres de los idiomas originales
#         game.language_names = ', '.join(lang.name for lang in game.languages.all())
#         # Obtener los nombres de los traductores
#         game.translator_names = ', '.join(translator.name for translator in game.translators.all())
#         # Obtener las imágenes activas asociadas al juego
#         game.images = game.images_as_game.filter(is_active=True)  # Filtrar solo imágenes activas
#         # Agregar el juego al contexto

#         context['game'] = game
#         context['class'] = BG_RENPY_GAME
#         context['objeto'] = self.object
#         context['title'] = self.object.title
#         context['listURL'] = reverse_lazy(URL_RENPY_GAME_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context

# class GameImageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = GameImage
#     template_name = TPL_RENPY_GAME_IMG_DTL
#     context_object_name = 'game_image'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
#         return redirect(URL_RENPY_HOME)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             messages.error(self.request, 'La imagen del juego que buscas no se encontró.')
#             return redirect(reverse_lazy(URL_RENPY_GAME_IMG_LST))

#         return super().get(request, *args, **kwargs)

#     def get_object(self):
#         return get_object_or_404(GameImage, pk=self.kwargs['pk'])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['file_size'] = self.object.file_size  # Agregar tamaño del archivo al contexto
#         context['dimensions'] = self.object.dimensions  # Agregar dimensiones de la imagen al contexto
#         juego = self.object.game.title
#         title = f'Img. de {juego}'
#         context['class'] = BG_RENPY_GAME_IMG
#         context['objeto'] = self.object
#         context['title'] = title
#         context['listURL'] = reverse_lazy(URL_RENPY_GAME_IMG_LST)
#         context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
#         return context

# class CoverGameDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = CoverGame
#     template_name = 'renpy/cover_game/cover_game_detail.html'
#     context_object_name = 'image_game'

#     def test_func(self):
#         return self.request.user.is_authenticated

#     def handle_no_permission(self):
#         messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
#         return redirect(URL_RENPY_HOME)

#     def get_object(self):
#         try:
#             return get_object_or_404(CoverGame, pk=self.kwargs['pk'])
#         except Http404:
#             messages.error(
#                 self.request, 'La imagen que buscas no se encontró.')
#             return redirect(URL_OTAKU_IMAGEN_ANIME_LST)

#     def get_game_name(self, image):
#         juegos = image.juego.all()  # Accede a los juegos relacionados
#         juego_names = [juego.title for juego in juegos]  # Crea una lista de títulos
#         return ", ".join(juego_names)  # Une los nombres con comas

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Agregar los detalles de la imagen normal al contexto
#         juego_names = self.get_game_name(self.object)

#         # Pasar la lista de nombres al contexto
#         context['juego'] = juego_names
#         context['image'] = self.object.get_img_url()
#         context['image_name'] = self.object.get_image_name()
#         context['image_extension'] = self.object.get_image_extension()
#         context['image_file_size'] = self.object.image_file_size
#         context['image_dimensions'] = self.object.image_dimensions
#         context['class'] = BG_OTAKU_COVER_ANIME
#         context['objeto'] = self.object
#         context['title'] = (f"Portada Juegos {juego_names}")
#         context['listURL'] = reverse_lazy(URL_OTAKU_IMAGEN_ANIME_LST)
#         context['homeURL'] = reverse_lazy(URL_OTAKU_HOME_ANIME)
#         return context





