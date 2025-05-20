# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (CreateView)

# Local app imports - Models
from apps.movie.models import (Genre, Type, Role, Rating, Movie, TitleMovie, MovieStaff, MovieCast, MovieImage, MovieImageExtra,)
from apps.common.models import (Company,)

# Local app imports - Forms
from apps.movie.forms import (GenreForm, TypeForm, RoleForm, RatingForm, MovieForm, TitleMovieForm, MovieStaffForm, MovieCastForm, MovieImageForm, MovieImageExtraForm,)
from apps.common.forms import (CompanyForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Genre
class GenreCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Movie.Genre.CREATE
    success_url = reverse_lazy(URLS.Movie.Genre.LIST)
    title = _('Añadir género cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El género cinematográfico "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Movie
class MovieCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = Templates.Movie.Movie.CREATE
    success_url = reverse_lazy(URLS.Movie.Movie.LIST)
    title = _('Añadir película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.title
        messages.success(self.request, _('¡La película "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    MovieCast
class MovieCastCreateView(PermissionRequiredMessageMixin, CreateView):
    model = MovieCast
    form_class = MovieCastForm
    template_name = Templates.Movie.MovieCast.CREATE
    success_url = reverse_lazy(URLS.Movie.MovieCast.LIST)
    title = _('Añadir reparto cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El reparto cinematográfico "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_CAST
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    MovieImage
class MovieImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = MovieImage
    form_class = MovieImageForm
    template_name = Templates.Movie.MovieImage.CREATE
    success_url = reverse_lazy(URLS.Movie.MovieImage.LIST)
    title = _('Añadir imagen de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen de la película "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    MovieImageExtra
class MovieImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = MovieImageExtra
    form_class = MovieImageExtraForm
    template_name = Templates.Movie.MovieImageExtra.CREATE
    success_url = reverse_lazy(URLS.Movie.MovieImageExtra.LIST)
    title = _('Añadir imagen adicional de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen adicional de la película "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    MovieStaff
class MovieStaffCreateView(PermissionRequiredMessageMixin, CreateView):
    model = MovieStaff
    form_class = MovieStaffForm
    template_name = Templates.Movie.MovieStaff.CREATE
    success_url = reverse_lazy(URLS.Movie.MovieStaff.LIST)
    title = _('Añadir personal cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El personal cinematográfico "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_STAFF
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Rating
class RatingCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Rating
    form_class = RatingForm
    template_name = Templates.Movie.Rating.CREATE
    success_url = reverse_lazy(URLS.Movie.Rating.LIST)
    title = _('Añadir clasificación')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de película "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.RATING
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Role
class RoleCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = Templates.Movie.Role.CREATE
    success_url = reverse_lazy(URLS.Movie.Role.LIST)
    title = _('Añadir rol cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El rol cinematográfico "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.ROLE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    TitleMovie
class TitleMovieCreateView(PermissionRequiredMessageMixin, CreateView):
    model = TitleMovie
    form_class = TitleMovieForm
    template_name = Templates.Movie.TitleMovie.CREATE
    success_url = reverse_lazy(URLS.Movie.TitleMovie.LIST)
    title = _('Añadir título de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El título de película "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.TITLE_MOVIE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Type
class TypeCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = Templates.Movie.Type.CREATE
    success_url = reverse_lazy(URLS.Movie.Type.LIST)
    title = _('Añadir tipo de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de película "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.TYPE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Distributor
class DistributorCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Movie.Distributor.CREATE
    success_url = reverse_lazy(URLS.Movie.Distributor.LIST)
    title = _('Añadir distribuidora cinematográfica')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La distribuidora cinematográfica "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.DISTRIBUTOR
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Producer
class ProducerCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Movie.Producer.CREATE
    success_url = reverse_lazy(URLS.Movie.Producer.LIST)
    title = _('Añadir productora cinematográfica')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La productora cinematográfica "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.PRODUCER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context