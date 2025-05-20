# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)

# Local app imports - Models
from apps.movie.models import (Genre, Type, Role, Rating, Movie, TitleMovie, MovieStaff, MovieCast, MovieImage, MovieImageExtra,)
from apps.common.models import (Company,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Genre
class GenreListView(PermissionRequiredMessageMixin, ListView):
    model = Genre
    template_name = Templates.Movie.Genre.LIST
    context_object_name = 'genres'
    title = _('Lista de géneros cinematográficos')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.GENRE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.GENRE
        context['key_map'] = KeyMap.Movie.GENRE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Genre.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Movie
class MovieListView(PermissionRequiredMessageMixin, ListView):
    model = Movie
    template_name = Templates.Movie.Movie.LIST
    context_object_name = 'movies'
    title = _('Lista de películas')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.MOVIE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.MOVIE
        context['key_map'] = KeyMap.Movie.MOVIE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Movie.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    MovieCast
class MovieCastListView(PermissionRequiredMessageMixin, ListView):
    model = MovieCast
    template_name = Templates.Movie.MovieCast.LIST
    context_object_name = 'MovieCasts'
    title = _('Lista de reparto cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.MOVIE_CAST
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.MOVIE_CAST
        context['key_map'] = KeyMap.Movie.MOVIE_CAST
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.MovieCast.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    MovieImage
class MovieImageListView(PermissionRequiredMessageMixin, ListView):
    model = MovieImage
    template_name = Templates.Movie.MovieImage.LIST
    context_object_name = 'MovieImages'
    title = _('Lista de imagen de película')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.MOVIE_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.MOVIE_IMAGE
        context['key_map'] = KeyMap.Movie.MOVIE_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.MovieImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    MovieImageExtra
class MovieImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = MovieImageExtra
    template_name = Templates.Movie.MovieImageExtra.LIST
    context_object_name = 'MovieImageExtras'
    title = _('Lista de imagen adicional de película')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.MOVIE_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.MOVIE_IMAGE_EXTRA
        context['key_map'] = KeyMap.Movie.MOVIE_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.MovieImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    MovieStaff
class MovieStaffListView(PermissionRequiredMessageMixin, ListView):
    model = MovieStaff
    template_name = Templates.Movie.MovieStaff.LIST
    context_object_name = 'MovieStaffs'
    title = _('Lista de personal cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.MOVIE_STAFF
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.MOVIE_STAFF
        context['key_map'] = KeyMap.Movie.MOVIE_STAFF
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.MovieStaff.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Rating
class RatingListView(PermissionRequiredMessageMixin, ListView):
    model = Rating
    template_name = Templates.Movie.Rating.LIST
    context_object_name = 'Ratings'
    title = _('Lista de clasificación')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.RATING
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.RATING
        context['key_map'] = KeyMap.Movie.RATING
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Rating.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Role
class RoleListView(PermissionRequiredMessageMixin, ListView):
    model = Role
    template_name = Templates.Movie.Role.LIST
    context_object_name = 'Roles'
    title = _('Lista de rol cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.ROLE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.ROLE
        context['key_map'] = KeyMap.Movie.ROLE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Role.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    TitleMovie
class TitleMovieListView(PermissionRequiredMessageMixin, ListView):
    model = TitleMovie
    template_name = Templates.Movie.TitleMovie.LIST
    context_object_name = 'TitleMovies'
    title = _('Lista de título de película')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.TITLE_MOVIE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.TITLE_MOVIE
        context['key_map'] = KeyMap.Movie.TITLE_MOVIE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.TitleMovie.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Type
class TypeListView(PermissionRequiredMessageMixin, ListView):
    model = Type
    template_name = Templates.Movie.Type.LIST
    context_object_name = 'Types'
    title = _('Lista de tipo de película')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.TYPE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.TYPE
        context['key_map'] = KeyMap.Movie.TYPE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Type.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Distributor
class DistributorListView(PermissionRequiredMessageMixin, ListView):
    model = Company
    template_name = Templates.Movie.Distributor.LIST
    context_object_name = 'Companys'
    title = _('Lista de distribuidora cinematográfica')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.DISTRIBUTOR
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.DISTRIBUTOR
        context['key_map'] = KeyMap.Movie.DISTRIBUTOR
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Distributor.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Producer
class ProducerListView(PermissionRequiredMessageMixin, ListView):
    model = Company
    template_name = Templates.Movie.Producer.LIST
    context_object_name = 'Companys'
    title = _('Lista de productora cinematográfica')
    permission_redirect_url = URLS.Home.MOVIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Movie.PRODUCER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Movie.PRODUCER
        context['key_map'] = KeyMap.Movie.PRODUCER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.MOVIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Movie.Producer.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context