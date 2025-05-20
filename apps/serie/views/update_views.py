# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (UpdateView)

# Local app imports - Models
from apps.serie.models import (Genre, Type, Role, Rating, Serie, TitleSerie, SerieStaff, SerieCast, SerieImage, SerieImageExtra,)
from apps.common.models import (Company,)

# Local app imports - Forms
from apps.serie.forms import (GenreForm, TypeForm, RoleForm, RatingForm, SerieForm, TitleSerieForm, SerieStaffForm, SerieCastForm, SerieImageForm, SerieImageExtraForm,)
from apps.common.forms import (CompanyForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Genre
class GenreUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Serie.Genre.UPDATE
    success_url = reverse_lazy(URLS.Serie.Genre.LIST)
    title = _('Editar género cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Serie
class SerieUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Serie
    form_class = SerieForm
    template_name = Templates.Serie.Serie.UPDATE
    success_url = reverse_lazy(URLS.Serie.Serie.LIST)
    title = _('Editar serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.title
        messages.success(self.request, _('¡La serie "%(name)s" fue actualizada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    SerieCast
class SerieCastUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = SerieCast
    form_class = SerieCastForm
    template_name = Templates.Serie.SerieCast.UPDATE
    success_url = reverse_lazy(URLS.Serie.SerieCast.LIST)
    title = _('Editar reparto cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.SERIE_CAST
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    SerieImage
class SerieImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = SerieImage
    form_class = SerieImageForm
    template_name = Templates.Serie.SerieImage.UPDATE
    success_url = reverse_lazy(URLS.Serie.SerieImage.LIST)
    title = _('Editar imagen de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen de la serie "%(name)s" fue actualizada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    SerieImageExtra
class SerieImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = SerieImageExtra
    form_class = SerieImageExtraForm
    template_name = Templates.Serie.SerieImageExtra.UPDATE
    success_url = reverse_lazy(URLS.Serie.SerieImageExtra.LIST)
    title = _('Editar imagen adicional de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen adicional de la serie "%(name)s" fue actualizado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.SERIE_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    SerieStaff
class SerieStaffUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = SerieStaff
    form_class = SerieStaffForm
    template_name = Templates.Serie.SerieStaff.UPDATE
    success_url = reverse_lazy(URLS.Serie.SerieStaff.LIST)
    title = _('Editar personal cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.SERIE_STAFF
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Rating
class RatingUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Rating
    form_class = RatingForm
    template_name = Templates.Serie.Rating.UPDATE
    success_url = reverse_lazy(URLS.Serie.Rating.LIST)
    title = _('Editar clasificación')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de serie "%(name)s" fue actualizado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.RATING
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Role
class RoleUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = Templates.Serie.Role.UPDATE
    success_url = reverse_lazy(URLS.Serie.Role.LIST)
    title = _('Editar rol cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.ROLE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    TitleSerie
class TitleSerieUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = TitleSerie
    form_class = TitleSerieForm
    template_name = Templates.Serie.TitleSerie.UPDATE
    success_url = reverse_lazy(URLS.Serie.TitleSerie.LIST)
    title = _('Editar título de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El título de serie "%(name)s" fue actualizado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.TITLE_SERIE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Type
class TypeUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Type
    form_class = TypeForm
    template_name = Templates.Serie.Type.UPDATE
    success_url = reverse_lazy(URLS.Serie.Type.LIST)
    title = _('Editar tipo de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de serie "%(name)s" fue actualizado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Serie.TYPE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Company
############################################################################################################################################    Company
class DistributorUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Serie.Distributor.UPDATE
    success_url = reverse_lazy(URLS.Serie.Distributor.LIST)
    title = _('Editar distribuidora cinematográfica')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.DISTRIBUTOR
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Company
class ProducerUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Serie.Producer.UPDATE
    success_url = reverse_lazy(URLS.Serie.Producer.LIST)
    title = _('Editar productora cinematográfica')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.PRODUCER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context