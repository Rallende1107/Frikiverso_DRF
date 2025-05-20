
# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)

# Local app imports - Models
from apps.music.models import (Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Album
class AlbumListView(PermissionRequiredMessageMixin, ListView):
    model = Album
    template_name = Templates.Music.Album.LIST
    context_object_name = 'albums'
    title = _('Álbumes Musicales')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ALBUM
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ALBUM
        context['key_map'] = KeyMap.Music.ALBUM
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.Album.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    AlbumImage
class AlbumImageListView(PermissionRequiredMessageMixin, ListView):
    model = AlbumImage
    template_name = Templates.Music.AlbumImage.LIST
    context_object_name = 'images'
    title = _('Imagenes de Álbumes')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ALBUM_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ALBUM_IMAGE
        context['key_map'] = KeyMap.Music.ALBUM_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.AlbumImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    AlbumImageExtra
class AlbumImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = AlbumImageExtra
    template_name = Templates.Music.AlbumImageExtra.LIST
    context_object_name = 'images'
    title = _('Imagenes Adicionales de Álbumes')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ALBUM_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ALBUM_IMAGE_EXTRA
        context['key_map'] = KeyMap.Music.ALBUM_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.AlbumImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    AlbumType
class AlbumTypeListView(PermissionRequiredMessageMixin, ListView):
    model = AlbumType
    template_name = Templates.Music.AlbumType.LIST
    context_object_name = 'types'
    title = _('Tipos de Álbumes')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ALBUM_TYPE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ALBUM_TYPE
        context['key_map'] = KeyMap.Music.ALBUM_TYPE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.AlbumType.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Artist
class ArtistListView(PermissionRequiredMessageMixin, ListView):
    model = Artist
    template_name = Templates.Music.Artist.LIST
    context_object_name = 'artists'
    title = _('Artistas')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ARTIST
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ARTIST
        context['key_map'] = KeyMap.Music.ARTIST
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.Artist.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    ArtistImage
class ArtistImageListView(PermissionRequiredMessageMixin, ListView):
    model = ArtistImage
    template_name = Templates.Music.ArtistImage.LIST
    context_object_name = 'images'
    title = _('Imagenes de Artistas')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ARTIST_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ARTIST_IMAGE
        context['key_map'] = KeyMap.Music.ARTIST_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.ArtistImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    ArtistImageExtra
class ArtistImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = ArtistImageExtra
    template_name = Templates.Music.ArtistImageExtra.LIST
    context_object_name = 'images'
    title = _('Imagenes Adicionales de Artistas')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ARTIST_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ARTIST_IMAGE_EXTRA
        context['key_map'] = KeyMap.Music.ARTIST_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.ArtistImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    ArtistMember
class ArtistMemberListView(PermissionRequiredMessageMixin, ListView):
    model = ArtistMember
    template_name = Templates.Music.ArtistMember.LIST
    context_object_name = 'artist_members'
    title = _('Miembros de Artistas')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ARTIST_MEMBER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ARTIST_MEMBER
        context['key_map'] = KeyMap.Music.ARTIST_MEMBER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.ArtistMember.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    ArtistType
class ArtistTypeListView(PermissionRequiredMessageMixin, ListView):
    model = ArtistType
    template_name = Templates.Music.ArtistType.LIST
    context_object_name = 'types'
    title = _('Tipos de Artistas')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ARTIST_TYPE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ARTIST_TYPE
        context['key_map'] = KeyMap.Music.ARTIST_TYPE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.ArtistType.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Genre
class GenreListView(PermissionRequiredMessageMixin, ListView):
    model = Genre
    template_name = Templates.Music.Genre.LIST
    context_object_name = 'genres'
    title = _('Géneros Musicales')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for xxx in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Music.GENRE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.GENRE
        context['key_map'] = KeyMap.Music.GENRE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.Genre.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Role
class RoleListView(PermissionRequiredMessageMixin, ListView):
    model = Role
    template_name = Templates.Music.Role.LIST
    context_object_name = 'roles'
    title = _('Listado de Roles Musicales')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Music.ROLE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.ROLE
        context['key_map'] = KeyMap.Music.ROLE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.Role.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Song
class SongListView(PermissionRequiredMessageMixin, ListView):
    model = Song
    template_name = Templates.Music.Song.LIST
    context_object_name = 'songs'
    title = _('Listado de Canciones')
    permission_redirect_url = URLS.Home.MUSIC

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Music.SONG
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Music.SONG
        context['key_map'] = KeyMap.Music.SONG
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MUSIC),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Music.Song.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context