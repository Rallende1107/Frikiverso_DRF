# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (CreateView)

# Local app imports - Models
from apps.common.models import (Company, Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Local app imports - Forms
from apps.common.forms import (CompanyForm, CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm, PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Company
class CompanyCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Common.Company.CREATE
    success_url = reverse_lazy(URLS.Common.Company.LIST)
    title = _('Añadir compañia')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La compañia "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.COMPANY
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Country
class CountryCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.CREATE
    success_url = reverse_lazy(URLS.Common.Country.LIST)
    title = _('Añadir país')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El país "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.COUNTRY
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Format
class FormatCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Format
    form_class = FormatForm
    template_name = Templates.Common.Format.CREATE
    success_url = reverse_lazy(URLS.Common.Format.LIST)
    title = _('Añadir formato')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El formato "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.FORMAT
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    ImageSize
class ImageSizeCreateView(PermissionRequiredMessageMixin, CreateView):
    model = ImageSize
    form_class = ImageSizeForm
    template_name = Templates.Common.ImageSize.CREATE
    success_url = reverse_lazy(URLS.Common.ImageSize.LIST)
    title = _('Añadir tamaño de imagen')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tamaño de imagen "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.IMAGE_SIZE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Language
class LanguageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Language
    form_class = LanguageForm
    template_name = Templates.Common.Language.CREATE
    success_url = reverse_lazy(URLS.Common.Language.LIST)
    title = _('Añadir idioma')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El idioma "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.LANGUAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Person
class PersonCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = Templates.Common.Person.CREATE
    success_url = reverse_lazy(URLS.Common.Person.LIST)
    title = _('Añadir persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.full_name
        messages.success(self.request, _('¡La persona "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    PersonImage
class PersonImageCreateView(PermissionRequiredMessageMixin, CreateView):
    model = PersonImage
    form_class = PersonImageForm
    template_name = Templates.Common.PersonImage.CREATE
    success_url = reverse_lazy(URLS.Common.PersonImage.LIST)
    title = _('Añadir imagen de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.person.full_name
        messages.success(self.request, _('¡La imagen de la persona "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON_IMAGE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    PersonImageExtra
class PersonImageExtraCreateView(PermissionRequiredMessageMixin, CreateView):
    model = PersonImageExtra
    form_class = PersonImageExtraForm
    template_name = Templates.Common.PersonImageExtra.CREATE
    success_url = reverse_lazy(URLS.Common.PersonImageExtra.LIST)
    title = _('Añadir imagen adicional de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.person.full_name
        messages.success(self.request, _('¡La imagen adicional de la persona "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON_IMAGE_EXTRA
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    PersonNickname
class PersonNicknameCreateView(PermissionRequiredMessageMixin, CreateView):
    model = PersonNickname
    form_class = PersonNicknameForm
    template_name = Templates.Common.PersonNickname.CREATE
    success_url = reverse_lazy(URLS.Common.PersonNickname.LIST)
    title = _('Añadir apodo de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        person = form.instance.person
        nickname = form.instance.nickname
        full_name = person.full_name
        messages.success(self.request, _('¡El apodo "%(nickname)s" de "%(full_name)s" fue creado exitosamente!')% {'nickname': nickname, 'full_name': full_name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON_NICKNAME
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context


############################################################################################################################################    Quality
class QualityCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Quality
    form_class = QualityForm
    template_name = Templates.Common.Quality.CREATE
    success_url = reverse_lazy(URLS.Common.Quality.LIST)
    title = _('Añadir calidad')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La calidad "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.QUALITY
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

############################################################################################################################################    Website
class WebsiteCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Website
    form_class = WebsiteForm
    template_name = Templates.Common.Website.CREATE
    success_url = reverse_lazy(URLS.Common.Website.LIST)
    title = _('Añadir sitio web')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El sitio web "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.WEBSITE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

from apps.common.models import ContextApp as Context, Genre, Type, Rating, Status
from apps.common.forms import ContextAppForm as ContextForm, GenreForm, TypeForm, RatingForm, StatusForm




class ContextCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Context
    form_class = ContextForm
    template_name = Templates.Common.Context.CREATE
    success_url = reverse_lazy(URLS.Common.Context.LIST)
    title = _('Añadir contexto')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El contexto "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.CONTEXT
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GenreCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = Templates.Common.Genre.CREATE
    success_url = reverse_lazy(URLS.Common.Genre.LIST)
    title = _('Añadir género')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El género "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context




class TypeCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Type
    form_class = TypeForm
    template_name = Templates.Common.Type.CREATE
    success_url = reverse_lazy(URLS.Common.Type.LIST)
    title = _('Añadir tipo')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tipo "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.TYPE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class RatingCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Rating
    form_class = RatingForm
    template_name = Templates.Common.Rating.CREATE
    success_url = reverse_lazy(URLS.Common.Rating.LIST)
    title = _('Añadir clasificación')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La clasificación "%(name)s" fue creada exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.RATING
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context


class StatusCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = Templates.Common.Status.CREATE
    success_url = reverse_lazy(URLS.Common.Status.LIST)
    title = _('Añadir estado')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El estado "%(name)s" fue creado exitosamente!') % {'name': name})
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.STATUS
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context