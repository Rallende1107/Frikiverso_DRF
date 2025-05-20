# Django imports
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (UpdateView,)

# Local app imports - Models
from apps.common.models import (Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Local app imports - Forms
from apps.common.forms import (CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm, PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    Country
class CountryUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.CREATE
    success_url = reverse_lazy(URLS.Common.Country.LIST)
    title = _('Editar País')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
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
    title = _('Editar Formato')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Formato "%(name)s" fue editado exitosamente!') % {'name': name})
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
    title = _('Editar Tamaño de Imágenes')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Tamaño de Imágen "%(name)s" fue editado exitosamente!') % {'name': name})
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
    title = _( 'Editar Idioma')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
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
    title = _('Editar Persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('full_name')
        messages.success(self.request, _('¡La Persona "%(name)s" fue editado exitosamente!') % {'name': name})
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
    title = _('Editar Imagen de persona')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        old_instance = self.get_object()
        old_image_url = old_instance.get_img_url() if old_instance and old_instance.image else None

        self.object = form.save()

        # Solo eliminar la imagen anterior si realmente se cambió
        if form.has_changed() and 'image' in form.changed_data and old_image_url:
            try:
                delete_previous_media(old_image_url)
            except Exception as e:
                messages.error(self.request, _('Error al eliminar la imagen anterior: %(error)s') % {'error': e})

        person_name = self.object.person.full_name
        messages.success(self.request, _('¡La Imagen de la persona "%(name)s" fue actualizada exitosamente!') % {'name': person_name})
        return redirect(self.get_success_url())

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

        form = self.get_form()
        have_media_file = 'image' in form.fields
        media_url = None
        if have_media_file:
            objeto = self.get_object()
            if objeto and objeto.get_img_url():
                media_url = objeto.get_img_url()

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
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
        old_instance = self.get_object()
        old_image_url = old_instance.get_img_url() if old_instance and old_instance.image else None

        self.object = form.save()

        # Solo eliminar la imagen anterior si realmente se cambió
        if form.has_changed() and 'image' in form.changed_data and old_image_url:
            try:
                delete_previous_media(old_image_url)
            except Exception as e:
                messages.error(self.request, _('Error al eliminar la imagen anterior: %(error)s') % {'error': e})

        person_name = self.object.person.full_name
        messages.success(self.request, _('¡La imagen adicional de la persona "%(name)s" fue actualizada exitosamente!') % {'name': person_name})
        return redirect(self.get_success_url())

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

        form = self.get_form()
        have_media_file = 'image' in form.fields
        media_url = None
        if have_media_file:
            objeto = self.get_object()
            if objeto and objeto.get_img_url():
                media_url = objeto.get_img_url()

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        return context

############################################################################################################################################    PersonNickname
class PersonNicknameUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonNickname
    form_class = PersonNicknameForm
    template_name = Templates.Common.PersonNickname.CREATE
    success_url = reverse_lazy(URLS.Common.PersonNickname.LIST)
    title = _('Editar PersonNicknamea')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('full_name')
        messages.success(self.request, _('¡La PersonNicknamea "%(name)s" fue editado exitosamente!') % {'name': name})
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
    title = _('Editar Calidad')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡La Calidad "%(name)s" fue editada exitosamente!') % {'name': name})
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
    title = _('Editar Sitio Web')
    permission_redirect_url = URLS.Home.COMMON

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, _('¡El Sitio Web "%(name)s" fue editado exitosamente!') % {'name': name})
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