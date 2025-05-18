# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (CreateView)

# Local app imports - Models
from apps.common.models import (Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Local app imports - Forms
from apps.common.forms import (CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm, PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    Country
class CountryCreateView(PermissionRequiredMessageMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.ADD
    success_url = reverse_lazy(URLS.Common.Country.LST)
    title = _('Añadir País')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
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
    template_name = Templates.Common.Format.ADD
    success_url = reverse_lazy(URLS.Common.Format.LST)
    title = _('Añadir Formato')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Formato "%(name)s" fue creado exitosamente!') % {'name': name})
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
    template_name = Templates.Common.ImageSize.ADD
    success_url = reverse_lazy(URLS.Common.ImageSize.LST)
    title = _('Añadir Tamaño de Imágenes')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Tamaño de Imágen "%(name)s" fue creado exitosamente!') % {'name': name})
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
    template_name = Templates.Common.Language.ADD
    success_url = reverse_lazy(URLS.Common.Language.LST)
    title = _('Añadir Idioma')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
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
    template_name = Templates.Common.Person.ADD
    success_url = reverse_lazy(URLS.Common.Person.LST)
    title = _('Añadir Persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('full_name')
        messages.success(self.request, _('¡La Persona "%(name)s" fue creada exitosamente!') % {'name': name})
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
    template_name = Templates.Common.PersonImage.ADD
    success_url = reverse_lazy(URLS.Common.PersonImage.LST)
    title = _('Añadir imagen de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        person_name = form.instance.person.full_name
        messages.success(self.request, _('¡La Imagen de la persona "%(name)s" fue creada exitosamente!') % {'name': person_name})
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
    template_name = Templates.Common.PersonImageExtra.ADD
    success_url = reverse_lazy(URLS.Common.PersonImageExtra.LST)
    title = _('Añadir imagen adicional de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        person_name = form.instance.person.full_name
        messages.success(self.request, _('¡La Imagen adicional de la persona "%(name)s" fue creada exitosamente!') % {'name': person_name})
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
    template_name = Templates.Common.PersonNickname.ADD
    success_url = reverse_lazy(URLS.Common.PersonNickname.LST)
    title = _('Añadir PersonNicknamea')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('full_name')
        messages.success(self.request, _('¡La PersonNicknamea "%(name)s" fue creada exitosamente!') % {'name': name})
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
    template_name = Templates.Common.Quality.ADD
    success_url = reverse_lazy(URLS.Common.Quality.LST)
    title = _('Añadir Calidad')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('La Calidad "%(name)s" fue creada exitosamente!') % {'name': name})
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
    template_name = Templates.Common.Website.ADD
    success_url = reverse_lazy(URLS.Common.Website.LST)
    title = _('Añadir Sitio Web')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('El Sitio Web "%(name)s" fue creado exitosamente!') % {'name': name})
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
