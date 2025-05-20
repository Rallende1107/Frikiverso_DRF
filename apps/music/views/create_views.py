
# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (CreateView)

# Local app imports - Models
from apps.music.models import (Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra,)

# Local app imports - Forms
from apps.music.forms import (GenreForm, RoleForm, AlbumTypeForm, ArtistTypeForm, ArtistForm, ArtistMemberForm, AlbumForm, SongForm, AlbumImageForm, AlbumImageExtraForm, ArtistImageForm, ArtistImageExtraForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Album
class AlbumCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = Templates.Music.Album.CREATE
    success_url = reverse_lazy(URLS.Music.Album.LIST)
    title = _('Añadir Álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.success(self.request, _('¡El álbum "%(title)s" fue creado exitosamente!') % {'title': title})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ALBUM
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    AlbumImage
class AlbumImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = AlbumImage
    form_class = AlbumImageForm
    template_name = Templates.Music.AlbumImage.CREATE
    success_url = reverse_lazy(URLS.Music.AlbumImage.LIST)
    title = _('Añadir imagen de álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        album_name = form.instance.album.title
        messages.success(self.request, _('¡La imagen del álbum "%(album_name)s" fue creada exitosamente!') % {'album_name': album_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ALBUM_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    AlbumImageExtra
class AlbumImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = AlbumImageExtra
    form_class = AlbumImageExtraForm
    template_name = Templates.Music.AlbumImageExtra.CREATE
    success_url = reverse_lazy(URLS.Music.AlbumImageExtra.LIST)
    title = _('Añadir imagen adicional de álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        album_name = form.instance.album.title
        messages.success(self.request, _('¡La imagen adicional del álbum "%(album_name)s" fue creada exitosamente!') % {'album_name': album_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ALBUM_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    AlbumType
class AlbumTypeCreateView(PermissionRequiredMessageMixin, CreateView):
    model = AlbumType
    form_class = AlbumTypeForm
    template_name = Templates.Music.AlbumType.CREATE
    success_url = reverse_lazy(URLS.Music.AlbumType.LIST)
    title = _('Añadir Tipo de Álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El tipo de álbum "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ALBUM_TYPE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Artist
class ArtistCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = Templates.Music.Artist.CREATE
    success_url = reverse_lazy(URLS.Music.Artist.LIST)
    title = _('Añadir artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El artista "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ARTIST
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    ArtistImage
class ArtistImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = ArtistImage
    form_class = ArtistImageForm
    template_name = Templates.Music.ArtistImage.CREATE
    success_url = reverse_lazy(URLS.Music.ArtistImage.LIST)
    title = _('Añadir imagen de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        artist_name = form.instance.artist.title
        messages.success(self.request, _('¡La imagen del artista "%(artist_name)s" fue creada exitosamente!') % {'artist_name': artist_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ARTIST_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    ArtistImageExtra
class ArtistImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = ArtistImageExtra
    form_class = ArtistImageExtraForm
    template_name = Templates.Music.ArtistImageExtra.CREATE
    success_url = reverse_lazy(URLS.Music.ArtistImageExtra.LIST)
    title = _('Añadir imagen adicional de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        artist_name = form.instance.artist.title
        messages.success(self.request, _('¡La imagen adicional del artista "%(artist_name)s" fue creada exitosamente!') % {'artist_name': artist_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ARTIST_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    ArtistMember
class ArtistMemberCreateView(PermissionRequiredMessageMixin, CreateView):
    model = ArtistMember
    form_class = ArtistMemberForm
    template_name = Templates.Music.ArtistMember.CREATE
    success_url = reverse_lazy(URLS.Music.ArtistMember.LIST)
    title = _('Añadir miembro de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        artist = form.cleaned_data.get('artist')
        person = form.cleaned_data.get('person')
        messages.success(self.request,_('¡El miembro "%(person)s" fue añadido al artista "%(artist)s" exitosamente!')% {'person': person, 'artist': artist})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ARTIST_MEMBER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    ArtistType
class ArtistTypeCreateView(PermissionRequiredMessageMixin, CreateView):
    model = ArtistType
    form_class = ArtistTypeForm
    template_name = Templates.Music.ArtistType.CREATE
    success_url = reverse_lazy(URLS.Music.ArtistType.LIST)
    title = _('Añadir tipo de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El tipo de artista "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ARTIST_TYPE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Genre
class GenreCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Music.Genre.CREATE
    success_url = reverse_lazy(URLS.Music.Genre.LIST)
    title = _('Añadir Género Musical')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El género musical "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Role
class RoleCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = Templates.Music.Role.CREATE
    success_url = reverse_lazy(URLS.Music.Role.LIST)
    title = _('Añadir Rol')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El rol "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.ROLE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Song
class SongCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Song
    form_class = SongForm
    template_name = Templates.Music.Song.CREATE
    success_url = reverse_lazy(URLS.Music.Song.LIST)
    title = _('Añadir Canción')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.success(self.request, _('¡La canción "%(title)s" fue creada exitosamente!') % {'title': title})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Music.SONG
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context
