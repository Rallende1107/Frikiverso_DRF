# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (ListView)

# Local app imports - Models
from apps.serie.models import (Genre, Type, Role, Rating, Serie, TitleSerie, SerieStaff, SerieCast, SerieImage, SerieImageExtra,)
from apps.common.models import (Company,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Genre
class GenreListView(PermissionRequiredMessageMixin, ListView):
    model = Genre
    template_name = Templates.Serie.Genre.LIST
    context_object_name = 'genres'
    title = _('Lista de géneros cinematográficos')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.GENRE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.GENRE
        context['key_map'] = KeyMap.Serie.GENRE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Genre.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Serie
class SerieListView(PermissionRequiredMessageMixin, ListView):
    model = Serie
    template_name = Templates.Serie.Serie.LIST
    context_object_name = 'series'
    title = _('Lista de series')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.SERIE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.SERIE
        context['key_map'] = KeyMap.Serie.SERIE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Serie.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    SerieCast
class SerieCastListView(PermissionRequiredMessageMixin, ListView):
    model = SerieCast
    template_name = Templates.Serie.SerieCast.LIST
    context_object_name = 'SerieCasts'
    title = _('Lista de reparto cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.SERIE_CAST
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.SERIE_CAST
        context['key_map'] = KeyMap.Serie.SERIE_CAST
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.SerieCast.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    SerieImage
class SerieImageListView(PermissionRequiredMessageMixin, ListView):
    model = SerieImage
    template_name = Templates.Serie.SerieImage.LIST
    context_object_name = 'SerieImages'
    title = _('Lista de imagen de serie')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.SERIE_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.SERIE_IMAGE
        context['key_map'] = KeyMap.Serie.SERIE_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.SerieImage.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    SerieImageExtra
class SerieImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = SerieImageExtra
    template_name = Templates.Serie.SerieImageExtra.LIST
    context_object_name = 'SerieImageExtras'
    title = _('Lista de imagen adicional de serie')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.SERIE_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.SERIE_IMAGE_EXTRA
        context['key_map'] = KeyMap.Serie.SERIE_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.SerieImageExtra.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    SerieStaff
class SerieStaffListView(PermissionRequiredMessageMixin, ListView):
    model = SerieStaff
    template_name = Templates.Serie.SerieStaff.LIST
    context_object_name = 'SerieStaffs'
    title = _('Lista de personal cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.SERIE_STAFF
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.SERIE_STAFF
        context['key_map'] = KeyMap.Serie.SERIE_STAFF
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.SerieStaff.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Rating
class RatingListView(PermissionRequiredMessageMixin, ListView):
    model = Rating
    template_name = Templates.Serie.Rating.LIST
    context_object_name = 'Ratings'
    title = _('Lista de clasificación')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.RATING
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.RATING
        context['key_map'] = KeyMap.Serie.RATING
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Rating.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Role
class RoleListView(PermissionRequiredMessageMixin, ListView):
    model = Role
    template_name = Templates.Serie.Role.LIST
    context_object_name = 'Roles'
    title = _('Lista de rol cinematográfico')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.ROLE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.ROLE
        context['key_map'] = KeyMap.Serie.ROLE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Role.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    TitleSerie
class TitleSerieListView(PermissionRequiredMessageMixin, ListView):
    model = TitleSerie
    template_name = Templates.Serie.TitleSerie.LIST
    context_object_name = 'TitleSeries'
    title = _('Lista de título de serie')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.TITLE_SERIE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.TITLE_SERIE
        context['key_map'] = KeyMap.Serie.TITLE_SERIE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.TitleSerie.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Type
class TypeListView(PermissionRequiredMessageMixin, ListView):
    model = Type
    template_name = Templates.Serie.Type.LIST
    context_object_name = 'Types'
    title = _('Lista de tipo de serie')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.TYPE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.TYPE
        context['key_map'] = KeyMap.Serie.TYPE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Type.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Distributor
class DistributorListView(PermissionRequiredMessageMixin, ListView):
    model = Company
    template_name = Templates.Serie.Distributor.LIST
    context_object_name = 'Companys'
    title = _('Lista de distribuidora cinematográfica')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.DISTRIBUTOR
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.DISTRIBUTOR
        context['key_map'] = KeyMap.Serie.DISTRIBUTOR
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Distributor.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Producer
class ProducerListView(PermissionRequiredMessageMixin, ListView):
    model = Company
    template_name = Templates.Serie.Producer.LIST
    context_object_name = 'Companys'
    title = _('Lista de productora cinematográfica')
    permission_redirect_url = URLS.Home.SERIE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for genre in context[self.context_object_name]:
        context['title'] = self.title
        context['class'] = CSSBackground.Serie.PRODUCER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Serie.PRODUCER
        context['key_map'] = KeyMap.Serie.PRODUCER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.SERIE),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Serie.Producer.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context