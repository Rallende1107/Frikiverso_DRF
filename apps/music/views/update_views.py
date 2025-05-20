# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (UpdateView)

# Local app imports - Models
from apps.music.models import (Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra,)

# Local app imports - Forms
from apps.music.forms import (GenreForm, RoleForm, AlbumTypeForm, ArtistTypeForm, ArtistForm, ArtistMemberForm, AlbumForm, SongForm, AlbumImageForm, AlbumImageExtraForm, ArtistImageForm, ArtistImageExtraForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Album
class AlbumUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = Templates.Music.Album.UPDATE
    success_url = reverse_lazy(URLS.Music.Album.LIST)
    title = _('Editar Álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.success(self.request, _('¡El álbum "%(title)s" fue editado exitosamente!') % {'title': title})
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
class AlbumImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = AlbumImage
    form_class = AlbumImageForm
    template_name = Templates.Music.AlbumImage.UPDATE
    success_url = reverse_lazy(URLS.Music.AlbumImage.LIST)
    title = _('Editar imagen de álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        album_name = form.instance.album.title
        messages.success(self.request, _('¡La imagen del álbum "%(album_name)s" fue editada exitosamente!') % {'album_name': album_name})
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
class AlbumImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = AlbumImageExtra
    form_class = AlbumImageExtraForm
    template_name = Templates.Music.AlbumImageExtra.UPDATE
    success_url = reverse_lazy(URLS.Music.AlbumImageExtra.LIST)
    title = _('Editar imagen adicional de álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        album_name = form.instance.album.title
        messages.success(self.request, _('¡La imagen adicional del álbum "%(album_name)s" fue editada exitosamente!') % {'album_name': album_name})
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
class AlbumTypeUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = AlbumType
    form_class = AlbumTypeForm
    template_name = Templates.Music.AlbumType.UPDATE
    success_url = reverse_lazy(URLS.Music.AlbumType.LIST)
    title = _('Editar Tipo de Álbum')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El tipo de álbum "%(name)s" fue editado exitosamente!') % {'name': name})
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
class ArtistUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = Templates.Music.Artist.UPDATE
    success_url = reverse_lazy(URLS.Music.Artist.LIST)
    title = _('Editar artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El artista "%(name)s" fue editado exitosamente!') % {'name': name})
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
class ArtistImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = ArtistImage
    form_class = ArtistImageForm
    template_name = Templates.Music.ArtistImage.UPDATE
    success_url = reverse_lazy(URLS.Music.ArtistImage.LIST)
    title = _('Editar imagen de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        artist_name = form.instance.artist.title
        messages.success(self.request, _('¡La imagen del artista "%(artist_name)s" fue editada exitosamente!') % {'artist_name': artist_name})
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
class ArtistImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = ArtistImageExtra
    form_class = ArtistImageExtraForm
    template_name = Templates.Music.ArtistImageExtra.UPDATE
    success_url = reverse_lazy(URLS.Music.ArtistImageExtra.LIST)
    title = _('Editar imagen adicional de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        artist_name = form.instance.artist.title
        messages.success(self.request, _('¡La imagen adicional del artista "%(artist_name)s" fue editada exitosamente!') % {'artist_name': artist_name})
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
class ArtistMemberUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = ArtistMember
    form_class = ArtistMemberForm
    template_name = Templates.Music.ArtistMember.UPDATE
    success_url = reverse_lazy(URLS.Music.ArtistMember.LIST)
    title = _('Editar miembro de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        artist = form.cleaned_data.get('artist')
        person = form.cleaned_data.get('person')
        messages.success(self.request,_('¡El miembro "%(person)s" fue editado al artista "%(artist)s" exitosamente!')% {'person': person, 'artist': artist})
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
class ArtistTypeUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = ArtistType
    form_class = ArtistTypeForm
    template_name = Templates.Music.ArtistType.UPDATE
    success_url = reverse_lazy(URLS.Music.ArtistType.LIST)
    title = _('Editar tipo de artista')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El tipo de artista "%(name)s" fue editado exitosamente!') % {'name': name})
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
class GenreUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Music.Genre.UPDATE
    success_url = reverse_lazy(URLS.Music.Genre.LIST)
    title = _('Editar Género Musical')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El género musical "%(name)s" fue editado exitosamente!') % {'name': name})
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
class RoleUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = Templates.Music.Role.UPDATE
    success_url = reverse_lazy(URLS.Music.Role.LIST)
    title = _('Editar Rol')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El rol "%(name)s" fue editado exitosamente!') % {'name': name})
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
class SongUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Song
    form_class = SongForm
    template_name = Templates.Music.Song.UPDATE
    success_url = reverse_lazy(URLS.Music.Song.LIST)
    title = _('Editar Canción')
    permission_redirect_url = URLS.Home.MUSIC

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        messages.success(self.request, _('¡La canción "%(title)s" fue editada exitosamente!') % {'title': title})
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
