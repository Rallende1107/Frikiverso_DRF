# Django imports
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (DetailView)

# Local app imports - Models
from apps.common.models import (Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    Country
class CountryDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Country
    template_name = Templates.Common.Country.DTL
    context_object_name = 'country'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El País que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.Country.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(Country, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Información adicional del contexto
        context['class'] = CSSBackground.Common.COUNTRY
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Country.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    Format
class FormatDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Format
    template_name = Templates.Common.Format.DTL
    context_object_name = 'format'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El formato que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.Format.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(Format, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Información adicional del contexto
        context['class'] = CSSBackground.Common.FORMAT
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Format.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    ImageSize
class ImageSizeDetailView(PermissionRequiredMessageMixin, DetailView):
    model = ImageSize
    template_name = Templates.Common.ImageSize.DTL
    context_object_name = 'imagesize'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El Tamaño de imagen que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.ImageSize.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(ImageSize, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Información adicional del contexto
        context['class'] = CSSBackground.Common.IMAGE_SIZE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.ImageSize.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    Language
class LanguageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Language
    template_name = Templates.Common.Language.DTL
    context_object_name = 'language'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El Idioma que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.Country.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(Language, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.LANGUAGE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Language.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    Person
class PersonDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Person
    template_name = Templates.Common.Person.DTL
    context_object_name = 'persons'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La Persona que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.Person.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Person, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON
        context['title'] = self.object.full_name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Person.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    PersonImage
class PersonImageDetailView(PermissionRequiredMessageMixin, DetailView):
    model = PersonImage
    template_name = Templates.Common.PersonImage.DTL
    context_object_name = 'image'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.PersonImage.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PersonImage, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON_IMAGE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.PersonImage.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    PersonImageExtra
class PersonImageExtraDetailView(PermissionRequiredMessageMixin, DetailView):
    model = PersonImageExtra
    template_name = Templates.Common.PersonImageExtra.DTL
    context_object_name = 'image'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La imagen adicional que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.PersonImageExtra.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PersonImageExtra, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON_IMAGE_EXTRA
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.PersonImageExtra.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context
#######################################################################################################################################    PersonNickname
class PersonNicknameDetailView(PermissionRequiredMessageMixin, DetailView):
    model = PersonNickname
    template_name = Templates.Common.PersonNickname.DTL
    context_object_name = 'nickname'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El Apodo de persona que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.PersonNickname.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PersonNickname, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Common.PERSON_NICKNAME
        context['title'] = self.object.nickname
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.PersonNickname.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    Quality
class QualityDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Quality
    template_name = Templates.Common.Quality.DTL
    context_object_name = 'quality'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('La Calidad que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.Quality.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(Quality, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Información adicional del contexto
        context['class'] = CSSBackground.Common.QUALITY
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Quality.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    Website
class WebsiteDetailView(PermissionRequiredMessageMixin, DetailView):
    model = Website
    template_name = Templates.Common.Website.DTL
    context_object_name = 'quality'
    permission_redirect_url = URLS.Home.COMMON

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, _('El Sitio Web que buscas no se encontró.'))
            return redirect(reverse_lazy(URLS.Common.Website.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(Website, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Información adicional del contexto
        context['class'] = CSSBackground.Common.WEBSITE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Website.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context


