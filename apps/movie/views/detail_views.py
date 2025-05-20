# Django imports
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (DetailView)

# Local app imports - Models
from apps.movie.models import (Genre, Type, Role, Rating, Movie, TitleMovie, MovieStaff, MovieCast, MovieImage, MovieImageExtra,)
from apps.common.models import (Company,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Genre
class GenreDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Genre
    template_name = Templates.Movie.Genre.DETAIL
    context_object_name = 'genres'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Genre.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Genre, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.GENRE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Genre.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    Movie
class MovieDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Movie
    template_name = Templates.Movie.Movie.DETAIL
    context_object_name = 'movies'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Movie.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Movie, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Movie.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    MovieCast
class MovieCastDetailView(PermissionRequiredMessageMixin, DetailView):
    model = MovieCast
    template_name = Templates.Movie.MovieCast.DETAIL
    context_object_name = 'MovieCasts'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.MovieCast.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(MovieCast, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_CAST
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.MovieCast.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    MovieImage
class MovieImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = MovieImage
    template_name = Templates.Movie.MovieImage.DETAIL
    context_object_name = 'MovieImages'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.MovieImage.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(MovieImage, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_IMAGE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.MovieImage.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    MovieImageExtra
class MovieImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = MovieImageExtra
    template_name = Templates.Movie.MovieImageExtra.DETAIL
    context_object_name = 'MovieImageExtras'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.MovieImageExtra.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(MovieImageExtra, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_IMAGE_EXTRA
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.MovieImageExtra.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    MovieStaff
class MovieStaffDetailView(PermissionRequiredMessageMixin, DetailView):
    model = MovieStaff
    template_name = Templates.Movie.MovieStaff.DETAIL
    context_object_name = 'MovieStaffs'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.MovieStaff.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(MovieStaff, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.MOVIE_STAFF
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.MovieStaff.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    Rating
class RatingDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Rating
    template_name = Templates.Movie.Rating.DETAIL
    context_object_name = 'Ratings'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Rating.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Rating, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.RATING
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Rating.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    Role
class RoleDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Role
    template_name = Templates.Movie.Role.DETAIL
    context_object_name = 'Roles'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Role.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Role, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.ROLE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Role.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    TitleMovie
class TitleMovieDetailView(PermissionRequiredMessageMixin, DetailView):
    model = TitleMovie
    template_name = Templates.Movie.TitleMovie.DETAIL
    context_object_name = 'TitleMovies'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.TitleMovie.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(TitleMovie, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.TITLE_MOVIE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.TitleMovie.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    Type
class TypeDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Type
    template_name = Templates.Movie.Type.DETAIL
    context_object_name = 'Types'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Type.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Type, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.TYPE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Type.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    Distributor
class DistributorDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Company
    template_name = Templates.Movie.Distributor.DETAIL
    context_object_name = 'Companys'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Company.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Company, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.DISTRIBUTOR
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Distributor.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context

############################################################################################################################################    Producer
class ProducerDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Company
    template_name = Templates.Movie.Producer.DETAIL
    context_object_name = 'Companys'
    permission_redirect_url = URLS.Home.MOVIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Movie.Company.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Company, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Movie.PRODUCER
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Movie.Producer.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.MOVIE)
        return context
