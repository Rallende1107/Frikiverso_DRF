# Django imports
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (DetailView)

# Local app imports - Models
from apps.serie.models import (Genre, Type, Role, Rating, Serie, TitleSerie, SerieStaff, SerieCast, SerieImage, SerieImageExtra,)
from apps.common.models import (Company,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Genre
class GenreDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Genre
    template_name = Templates.Serie.Genre.DETAIL
    context_object_name = 'genres'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Genre.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Genre, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.GENRE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Genre.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    Serie
class SerieDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Serie
    template_name = Templates.Serie.Serie.DETAIL
    context_object_name = 'series'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Serie.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Serie, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Serie.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    SerieCast
class SerieCastDetailView(PermissionRequiredMessageMixin, DetailView):
    model = SerieCast
    template_name = Templates.Serie.SerieCast.DETAIL
    context_object_name = 'SerieCasts'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.SerieCast.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(SerieCast, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE_CAST
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.SerieCast.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    SerieImage
class SerieImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = SerieImage
    template_name = Templates.Serie.SerieImage.DETAIL
    context_object_name = 'SerieImages'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.SerieImage.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(SerieImage, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE_IMAGE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.SerieImage.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    SerieImageExtra
class SerieImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = SerieImageExtra
    template_name = Templates.Serie.SerieImageExtra.DETAIL
    context_object_name = 'SerieImageExtras'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.SerieImageExtra.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(SerieImageExtra, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE_IMAGE_EXTRA
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.SerieImageExtra.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    SerieStaff
class SerieStaffDetailView(PermissionRequiredMessageMixin, DetailView):
    model = SerieStaff
    template_name = Templates.Serie.SerieStaff.DETAIL
    context_object_name = 'SerieStaffs'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.SerieStaff.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(SerieStaff, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE_STAFF
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.SerieStaff.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    Rating
class RatingDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Rating
    template_name = Templates.Serie.Rating.DETAIL
    context_object_name = 'Ratings'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Rating.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Rating, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.RATING
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Rating.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    Role
class RoleDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Role
    template_name = Templates.Serie.Role.DETAIL
    context_object_name = 'Roles'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Role.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Role, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.ROLE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Role.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    TitleSerie
class TitleSerieDetailView(PermissionRequiredMessageMixin, DetailView):
    model = TitleSerie
    template_name = Templates.Serie.TitleSerie.DETAIL
    context_object_name = 'TitleSeries'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.TitleSerie.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(TitleSerie, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.TITLE_SERIE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.TitleSerie.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    Type
class TypeDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Type
    template_name = Templates.Serie.Type.DETAIL
    context_object_name = 'Types'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Type.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Type, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.TYPE
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Type.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    Distributor
class DistributorDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Company
    template_name = Templates.Serie.Distributor.DETAIL
    context_object_name = 'Companys'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Company.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Company, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.DISTRIBUTOR
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Distributor.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context

############################################################################################################################################    Producer
class ProducerDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Company
    template_name = Templates.Serie.Producer.DETAIL
    context_object_name = 'Companys'
    permission_redirect_url = URLS.Home.SERIE

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('el género que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Serie.Company.LIST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Company, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.PRODUCER
        context['title'] = self.title
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Serie.Producer.LIST)
        context['homeURL'] = reverse_lazy(URLS.Home.SERIE)
        return context
