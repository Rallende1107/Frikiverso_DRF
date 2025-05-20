# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (CreateView)

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
class GenreCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Serie.Genre.CREATE
    success_url = reverse_lazy(URLS.Serie.Genre.LIST)
    title = _('Añadir género cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Serie
class SerieCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Serie
    form_class = SerieForm
    template_name = Templates.Serie.Serie.CREATE
    success_url = reverse_lazy(URLS.Serie.Serie.LIST)
    title = _('Añadir serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.title
        messages.success(self.request, _('¡La serie "%(name)s" fue creada exitosamente!') % {'name': name})
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
class SerieCastCreateView(PermissionRequiredMessageMixin, CreateView):
    model = SerieCast
    form_class = SerieCastForm
    template_name = Templates.Serie.SerieCast.CREATE
    success_url = reverse_lazy(URLS.Serie.SerieCast.LIST)
    title = _('Añadir reparto cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.SERIE_CAST
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    SerieImage
class SerieImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = SerieImage
    form_class = SerieImageForm
    template_name = Templates.Serie.SerieImage.CREATE
    success_url = reverse_lazy(URLS.Serie.SerieImage.LIST)
    title = _('Añadir imagen de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen de la serie "%(name)s" fue creada exitosamente!') % {'name': name})
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
class SerieImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = SerieImageExtra
    form_class = SerieImageExtraForm
    template_name = Templates.Serie.SerieImageExtra.CREATE
    success_url = reverse_lazy(URLS.Serie.SerieImageExtra.LIST)
    title = _('Añadir imagen adicional de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La imagen adicional de la serie "%(name)s" fue creado exitosamente!') % {'name': name})
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
class SerieStaffCreateView(PermissionRequiredMessageMixin, CreateView):
    model = SerieStaff
    form_class = SerieStaffForm
    template_name = Templates.Serie.SerieStaff.CREATE
    success_url = reverse_lazy(URLS.Serie.SerieStaff.LIST)
    title = _('Añadir personal cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.SERIE_STAFF
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Rating
class RatingCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Rating
    form_class = RatingForm
    template_name = Templates.Serie.Rating.CREATE
    success_url = reverse_lazy(URLS.Serie.Rating.LIST)
    title = _('Añadir clasificación')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de serie "%(name)s" fue creado exitosamente!') % {'name': name})
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
class RoleCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = Templates.Serie.Role.CREATE
    success_url = reverse_lazy(URLS.Serie.Role.LIST)
    title = _('Añadir rol cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.ROLE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    TitleSerie
class TitleSerieCreateView(PermissionRequiredMessageMixin, CreateView):
    model = TitleSerie
    form_class = TitleSerieForm
    template_name = Templates.Serie.TitleSerie.CREATE
    success_url = reverse_lazy(URLS.Serie.TitleSerie.LIST)
    title = _('Añadir título de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El título de serie "%(name)s" fue creado exitosamente!') % {'name': name})
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
class TypeCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = Templates.Serie.Type.CREATE
    success_url = reverse_lazy(URLS.Serie.Type.LIST)
    title = _('Añadir tipo de serie')
    permission_redirect_url = URLS.Home.SERIE

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo de serie "%(name)s" fue creado exitosamente!') % {'name': name})
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

############################################################################################################################################    Distributor
class DistributorCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Serie.Distributor.CREATE
    success_url = reverse_lazy(URLS.Serie.Distributor.LIST)
    title = _('Añadir distribuidora cinematográfica')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.DISTRIBUTOR
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Producer
class ProducerCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Serie.Producer.CREATE
    success_url = reverse_lazy(URLS.Serie.Producer.LIST)
    title = _('Añadir productora cinematográfica')
    permission_redirect_url = URLS.Home.SERIE

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
        context['class'] = CSSBackground.Serie.PRODUCER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context