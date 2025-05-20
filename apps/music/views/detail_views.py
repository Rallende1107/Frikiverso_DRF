
from django.views.generic import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import Http404
from apps.music.models import ArtistImage
# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

from django.utils.translation import gettext_lazy as _
############################################################################################################################################    Album
############################################################################################################################################    AlbumImage
############################################################################################################################################    AlbumImageExtra
############################################################################################################################################    AlbumType
############################################################################################################################################    Artist
############################################################################################################################################    ArtistImage
############################################################################################################################################    ArtistImageExtra
############################################################################################################################################    ArtistMember
############################################################################################################################################    ArtistType
############################################################################################################################################    Genre
############################################################################################################################################    Role
############################################################################################################################################    Song

class ArtistImageDetailView(PermissionRequiredMixin, DetailView):
    model = ArtistImage
    template_name = Templates.Music.ArtistImage.DETAIL  # Ajusta según tu template
    context_object_name = 'artist_image'
    permission_required = 'music_app.view_artistimage'  # Ajusta permiso si tienes uno específico
    permission_redirect_url = URLS.Home.RENPY  # O donde quieras redirigir si no tiene permiso

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(request, _('La imagen del artista no se encontró.'))
            return redirect(reverse_lazy('music_app:artist_image_list'))  # Ajusta la url de la lista
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ARTIST_IMAGE  # Ajusta tu CSSBackground
        context['title'] = f'Imagen de {self.object.artist}'
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy('music_app:artist_image_list')  # Ajusta url lista
        context['homeURL'] = reverse_lazy(URLS.Home.RENPY)
        return context
