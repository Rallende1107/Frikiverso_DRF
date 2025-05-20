# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (UpdateView)

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
class GenreUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Movie.Genre.UPDATE
    success_url = reverse_lazy(URLS.Movie.Genre.LIST)
    title = _('Editar género cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El género cinematográfico "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class MovieUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = Templates.Movie.Movie.UPDATE
    success_url = reverse_lazy(URLS.Movie.Movie.LIST)
    title = _('Editar película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.title
        messages.success(self.request, _('¡La película "%(name)s" fue actualizada exitosamente!') % {'name': name})
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
class MovieCastUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = MovieCast
    form_class = MovieCastForm
    template_name = Templates.Movie.MovieCast.UPDATE
    success_url = reverse_lazy(URLS.Movie.MovieCast.LIST)
    title = _('Editar reparto cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El reparto cinematográfico "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class MovieImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = MovieImage
    form_class = MovieImageForm
    template_name = Templates.Movie.MovieImage.UPDATE
    success_url = reverse_lazy(URLS.Movie.MovieImage.LIST)
    title = _('Editar imagen de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen de la película "%(name)s" fue actualizada exitosamente!') % {'name': name})
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
class MovieImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = MovieImageExtra
    form_class = MovieImageExtraForm
    template_name = Templates.Movie.MovieImageExtra.UPDATE
    success_url = reverse_lazy(URLS.Movie.MovieImageExtra.LIST)
    title = _('Editar imagen adicional de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen adicional de la película "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class MovieStaffUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = MovieStaff
    form_class = MovieStaffForm
    template_name = Templates.Movie.MovieStaff.UPDATE
    success_url = reverse_lazy(URLS.Movie.MovieStaff.LIST)
    title = _('Editar personal cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El personal cinematográfico "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class RatingUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Rating
    form_class = RatingForm
    template_name = Templates.Movie.Rating.UPDATE
    success_url = reverse_lazy(URLS.Movie.Rating.LIST)
    title = _('Editar clasificación')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de película "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class RoleUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = Templates.Movie.Role.UPDATE
    success_url = reverse_lazy(URLS.Movie.Role.LIST)
    title = _('Editar rol cinematográfico')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El rol cinematográfico "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class TitleMovieUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = TitleMovie
    form_class = TitleMovieForm
    template_name = Templates.Movie.TitleMovie.UPDATE
    success_url = reverse_lazy(URLS.Movie.TitleMovie.LIST)
    title = _('Editar título de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El título de película "%(name)s" fue actualizado exitosamente!') % {'name': name})
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
class TypeUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = Templates.Movie.Type.UPDATE
    success_url = reverse_lazy(URLS.Movie.Type.LIST)
    title = _('Editar tipo de película')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de película "%(name)s" fue actualizado exitosamente!') % {'name': name})
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

############################################################################################################################################    Company
############################################################################################################################################    Company
class DistributorUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Movie.Distributor.UPDATE
    success_url = reverse_lazy(URLS.Movie.Distributor.LIST)
    title = _('Editar distribuidora cinematográfica')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La distribuidora cinematográfica "%(name)s" fue actualizada exitosamente!') % {'name': name})
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

############################################################################################################################################    Company
class ProducerUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Movie.Producer.UPDATE
    success_url = reverse_lazy(URLS.Movie.Producer.LIST)
    title = _('Editar productora cinematográfica')
    permission_redirect_url = URLS.Home.MOVIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La productora cinematográfica "%(name)s" fue actualizada exitosamente!') % {'name': name})
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