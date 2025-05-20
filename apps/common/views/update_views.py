# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import (UpdateView)

# Local app imports - Models
from apps.common.models import (Company, Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Local app imports - Forms
from apps.common.forms import (CompanyForm, CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm, PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin
from core.utils.utils import get_media_context

# Create your views here.
############################################################################################################################################    Country
class CompanyUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = Templates.Common.Company.UPDATE
    success_url = reverse_lazy(URLS.Common.Company.LIST)
    title = _('Editar compañia')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La compañia "%(name)s" fue editada exitosamente!') % {'name': name})
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
class CountryUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.CREATE
    success_url = reverse_lazy(URLS.Common.Country.LIST)
    title = _('Editar país')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El país "%(name)s" fue editado exitosamente!') % {'name': name})
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
class FormatUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Format
    form_class = FormatForm
    template_name = Templates.Common.Format.CREATE
    success_url = reverse_lazy(URLS.Common.Format.LIST)
    title = _('Editar formato')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El formato "%(name)s" fue editado exitosamente!') % {'name': name})
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
class ImageSizeUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = ImageSize
    form_class = ImageSizeForm
    template_name = Templates.Common.ImageSize.CREATE
    success_url = reverse_lazy(URLS.Common.ImageSize.LIST)
    title = _('Editar tamaño de imagen')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El tamaño de imagen "%(name)s" fue editado exitosamente!') % {'name': name})
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
class LanguageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = Templates.Common.Language.CREATE
    success_url = reverse_lazy(URLS.Common.Language.LIST)
    title = _('Editar idioma')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El idioma "%(name)s" fue editado exitosamente!') % {'name': name})
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
class PersonUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = Templates.Common.Person.CREATE
    success_url = reverse_lazy(URLS.Common.Person.LIST)
    title = _('Editar persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.full_name
        messages.success(self.request, _('¡La persona "%(name)s" fue editada exitosamente!') % {'name': name})
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
class PersonImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonImage
    form_class = PersonImageForm
    template_name = Templates.Common.PersonImage.CREATE
    success_url = reverse_lazy(URLS.Common.PersonImage.LIST)
    title = _('Editar imagen de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.person.full_name
        messages.success(self.request, _('¡La imagen de "%(name)s" fue editada exitosamente!') % {'name': name})
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
        context['media_file_table'], context['media_url'] = get_media_context(self)
        return context

############################################################################################################################################    PersonImageExtra
class PersonImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonImageExtra
    form_class = PersonImageExtraForm
    template_name = Templates.Common.PersonImageExtra.CREATE
    success_url = reverse_lazy(URLS.Common.PersonImageExtra.LIST)
    title = _('Editar imagen adicional de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.person.full_name
        messages.success(self.request, _('¡La imagen adicional de "%(name)s" fue editada exitosamente!') % {'name': name})
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
        context['media_file_table'], context['media_url'] = get_media_context(self)
        return context

############################################################################################################################################    PersonNickname
class PersonNicknameUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonNickname
    form_class = PersonNicknameForm
    template_name = Templates.Common.PersonNickname.CREATE
    success_url = reverse_lazy(URLS.Common.PersonNickname.LIST)
    title = _('Editar apodo de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        person = form.instance.person
        nickname = form.instance.nickname
        full_name = person.full_name
        messages.success(self.request, _('¡El apodo "%(nickname)s" de "%(full_name)s" fue editado exitosamente!')% {'nickname': nickname, 'full_name': full_name})
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
class QualityUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Quality
    form_class = QualityForm
    template_name = Templates.Common.Quality.CREATE
    success_url = reverse_lazy(URLS.Common.Quality.LIST)
    title = _('Editar calidad')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡La calidad "%(name)s" fue editada exitosamente!') % {'name': name})
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
class WebsiteUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Website
    form_class = WebsiteForm
    template_name = Templates.Common.Website.CREATE
    success_url = reverse_lazy(URLS.Common.Website.LIST)
    title = _('Editar sitio web')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.instance.name
        messages.success(self.request, _('¡El sitio web "%(name)s" fue editado exitosamente!') % {'name': name})
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