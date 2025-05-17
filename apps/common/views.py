# Imports de Django
from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView, View)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _

# Imports de la app (modelos y formularios)
from .models import (
    Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra,
    PersonNickname, Quality, Website
)
from .forms import (
    CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm,
    PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm
)
# Imports de utilidades y mixins propios
from core.mixins import PermissionRequiredMessageMixin
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap
from core.utils.texts import Titles
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = _('General')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.COMMON
        context['title'] = self.title
        card_sections = {

            _('Administración de Usuarios'): [
                {
                    'title': _('Usuarios'),
                    'img_url': ImageCards.Users.USER,
                    'go_url': None,
                    'view_url': URLS.Users.LST,
                    'add_url': URLS.Users.ADD,
                    'text': _('Gestionar usuarios del sistema.'),
                    'extra_buttons': [
                        {
                            'url': URLS.Users.ADD_STAFF,
                            'label': _('Crear usuario del equipo'),
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                        {
                            'url': URLS.Users.ADD_SUPER,
                            'label': _('Crear super usuario'),
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                    ],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },
            ],

            _('Gestión General'): [
                {
                    'title': _('Países'),
                    'img_url': ImageCards.Common.COUNTRY,
                    'go_url': None,
                    'view_url': URLS.Common.Country.LST,
                    'add_url': URLS.Common.Country.ADD,
                    'text': _('Gestionar países del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Formatos'),
                    'img_url': ImageCards.Common.FORMAT,
                    'go_url': None,
                    'view_url': URLS.Common.Format.LST,
                    'add_url': URLS.Common.Format.ADD,
                    'text': _('Gestionar formatos del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Tamaños de imagen'),
                    'img_url': ImageCards.Common.IMAGE_SIZE,
                    'go_url': None,
                    'view_url': URLS.Common.ImageSize.LST,
                    'add_url': URLS.Common.ImageSize.ADD,
                    'text': _('Gestionar tamaños de imagen del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Idiomas'),
                    'img_url': ImageCards.Common.LANGUAGE,
                    'go_url': None,
                    'view_url': URLS.Common.Language.LST,
                    'add_url': URLS.Common.Language.ADD,
                    'text': _('Gestionar Idiomas del sistema.'),
                    'extra_buttons': [],
                },
            ],

            _('Gestión de Personas'): [
                {
                    'title': _('Personas'),
                    'img_url': ImageCards.Common.PERSON,
                    'go_url': None,
                    'view_url': URLS.Common.Person.LST,
                    'add_url': URLS.Common.Person.ADD,
                    'text': _('Gestionar personas del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de personas'),
                    'img_url': ImageCards.Common.PERSON_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Common.PersonImage.LST,
                    'add_url': URLS.Common.PersonImage.ADD,
                    'text': _('Gestionar imágenes de personas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes extra de personas'),
                    'img_url': ImageCards.Common.PERSON_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Common.PersonImageExtra.LST,
                    'add_url': URLS.Common.PersonImageExtra.ADD,
                    'text': _('Gestionar imágenes adicionales de personas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Apodos de personas'),
                    'img_url': ImageCards.Common.PERSON_NICKNAME,
                    'go_url': None,
                    'view_url': URLS.Common.PersonNickname.LST,
                    'add_url': URLS.Common.PersonNickname.ADD,
                    'text': _('Gestionar apodeos de las personas.'),
                    'extra_buttons': [],
                },
            ],

            _('Configuración Adicional'): [
                {
                    'title': _('Calidades'),
                    'img_url': ImageCards.Common.QUALITY,
                    'go_url': None,
                    'view_url': URLS.Common.Quality.LST,
                    'add_url': URLS.Common.Quality.ADD,
                    'text': _('Gestionar calidades del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Sitios web'),
                    'img_url': ImageCards.Common.WEBSITE,
                    'go_url': None,
                    'view_url': URLS.Common.Website.LST,
                    'add_url': URLS.Common.Website.ADD,
                    'text': _('Gestionar sitios web del sistema.'),
                    'extra_buttons': [],
                },
            ],
        }

        # Filtrar tarjetas y secciones que no deben mostrarse
        filtered_sections = {}
        for section, items in card_sections.items():
            filtered_items = [item for item in items if item.get('show', True)]
            if filtered_items:
                filtered_sections[section] = filtered_items

        context['card_sections'] = filtered_sections
        context['labels'] = {
            'go': _('Ir'),
            'view_all': _('Todos'),
            'add': _('Añadir'),
        }


        return context

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

class CountryUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.ADD
    success_url = reverse_lazy(URLS.Common.Country.LST)
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

class CountryListView(PermissionRequiredMessageMixin, ListView):
    model = Country
    template_name = Templates.Common.Country.LST
    context_object_name = 'country'
    title = _('Lista de Países')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for country in context[self.context_object_name]:
            # Combina el nombre y las iniciales en inglés
            if country.code:
                country.combined_name = f'{country.name} ({country.code})'
            else:
                country.combined_name = country.name

            # Combina el nombre y las iniciales en español
            if country.name_esp:
                country.combined_name_esp = f'{country.name_esp} ({country.code})'
            else:
                country.combined_name_esp = country.name_esp

        context['title'] = self.title
        context['class'] = CSSBackground.Common.COUNTRY
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.COUNTRY
        context['key_map'] = KeyMap.Common.COUNTRY
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Country.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

class FormatUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Format
    form_class = FormatForm
    template_name = Templates.Common.Format.ADD
    success_url = reverse_lazy(URLS.Common.Format.LST)
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

class FormatListView(PermissionRequiredMessageMixin, ListView):
    model = Format
    template_name = Templates.Common.Format.LST
    context_object_name = 'formats'
    title = _('Lista de Formatos')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.FORMAT
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.FORMAT
        context['key_map'] = KeyMap.Common.FORMAT
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Format.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

class ImageSizeUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = ImageSize
    form_class = ImageSizeForm
    template_name = Templates.Common.ImageSize.ADD
    success_url = reverse_lazy(URLS.Common.ImageSize.LST)
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

class ImageSizeListView(PermissionRequiredMessageMixin, ListView):
    model = ImageSize
    template_name = Templates.Common.ImageSize.LST
    context_object_name = 'imagesizes'
    title = _('Lista de Tamaños de Imágenes')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.IMAGE_SIZE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.IMAGE_SIZE
        context['key_map'] = KeyMap.Common.IMAGE_SIZE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.ImageSize.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

############################################################################################################################################    Lenguaje
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

class LanguageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = Templates.Common.Language.ADD
    success_url = reverse_lazy(URLS.Common.Language.LST)
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

class LanguageListView(PermissionRequiredMessageMixin, ListView):
    model = Language
    template_name = Templates.Common.Language.LST
    context_object_name = 'languages'
    title = _('Lista de Idiomas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for language in context[self.context_object_name]:
            # Combina el nombre y las iniciales en inglés
            if language.acronym:
                language.combined_language = f'{language.name} ({language.acronym})'
            else:
                language.combined_language = language.name

            # Combina el nombre y las iniciales en español
            if language.name_esp:
                language.combined_language_esp = f'{language.name_esp} ({language.acronym})'
            else:
                language.combined_language_esp = language.name_esp

        context['title'] = self.title
        context['class'] = CSSBackground.Common.LANGUAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.LANGUAGE
        context['key_map'] = KeyMap.Common.LANGUAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Language.ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

class PersonUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = Templates.Common.Person.ADD
    success_url = reverse_lazy(URLS.Common.Person.LST)
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

class PersonListView(PermissionRequiredMessageMixin, ListView):
    model = Person
    template_name = Templates.Common.Person.LST
    context_object_name = 'persons'
    title = _('Lista de Personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON
        context['key_map'] = KeyMap.Common.PERSON
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Person.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

class PersonImageUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonImage
    form_class = PersonImageForm
    template_name = Templates.Common.PersonImage.ADD
    success_url = reverse_lazy(URLS.Common.PersonImage.LST)
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

class PersonImageListView(PermissionRequiredMessageMixin, ListView):
    model = PersonImage
    template_name = Templates.Common.PersonImage.LST
    context_object_name = 'images'
    title = _('Lista de imágenes de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for img in context[self.context_object_name]:
            # Si la relación 'anime' es un ForeignKey, accedemos directamente a la propiedad 'anime'
            img.person_name = img.get_object_name()
            # Obtener el nombre y la extensión de la imagen
            img.image_name = img.get_object_name()

            # Obtener la URL de la imagen si está disponible
            img.image_url_local = img.get_img_url()
            img.image_url_external = img.image_url if img.image_url else None

        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON_IMAGE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON_IMAGE
        context['key_map'] = KeyMap.Common.PERSON_IMAGE
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.PersonImage.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

class PersonImageExtraUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonImageExtra
    form_class = PersonImageExtraForm
    template_name = Templates.Common.PersonImageExtra.ADD
    success_url = reverse_lazy(URLS.Common.PersonImageExtra.LST)
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

class PersonImageExtraListView(PermissionRequiredMessageMixin, ListView):
    model = PersonImageExtra
    template_name = Templates.Common.PersonImageExtra.LST
    context_object_name = 'images'
    title = _('Lista de imagenes adicionales de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for img in context[self.context_object_name]:
            # Si la relación 'anime' es un ForeignKey, accedemos directamente a la propiedad 'anime'
            img.person_name = img.get_object_name()
            # Obtener el nombre y la extensión de la imagen
            img.image_name = img.get_object_name()

            # Obtener la URL de la imagen si está disponible
            img.image_url_local = img.get_img_url()

        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON_IMAGE_EXTRA
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON_IMAGE_EXTRA
        context['key_map'] = KeyMap.Common.PERSON_IMAGE_EXTRA
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.PersonImageExtra.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

class PersonNicknameUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = PersonNickname
    form_class = PersonNicknameForm
    template_name = Templates.Common.PersonNickname.ADD
    success_url = reverse_lazy(URLS.Common.PersonNickname.LST)
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

class PersonNicknameListView(PermissionRequiredMessageMixin, ListView):
    model = PersonNickname
    template_name = Templates.Common.PersonNickname.LST
    context_object_name = 'nicknames'
    title = _('Lista de Apodos de personas')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.PERSON_NICKNAME
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.PERSON_NICKNAME
        context['key_map'] = KeyMap.Common.PERSON_NICKNAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.PersonNickname.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

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

############################################################################################################################################    Quality Create
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

############################################################################################################################################    Quality Update
class QualityUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Quality
    form_class = QualityForm
    template_name = Templates.Common.Quality.ADD
    success_url = reverse_lazy(URLS.Common.Quality.LST)
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

############################################################################################################################################    Quality List
class QualityListView(PermissionRequiredMessageMixin, ListView):
    model = Quality
    template_name = Templates.Common.Quality.LST
    context_object_name = 'qualitys'
    title = _('Lista de Calidades')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Common.QUALITY
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.QUALITY
        context['key_map'] = KeyMap.Common.QUALITY
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Quality.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Quality Detail
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

############################################################################################################################################    Quality Create
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

############################################################################################################################################    Website Update
class WebsiteUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = Website
    form_class = WebsiteForm
    template_name = Templates.Common.Website.ADD
    success_url = reverse_lazy(URLS.Common.Website.LST)
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

############################################################################################################################################    Website List
class WebsiteListView(PermissionRequiredMessageMixin, ListView):
    model = Website
    template_name = Templates.Common.Website.LST
    context_object_name = 'websites'
    title = _('Lista de Sitios Web\'s')
    permission_redirect_url = URLS.Home.COMMON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for website in context[self.context_object_name]:
            # Combina el nombre y el acrónimo
            if website.acronym:
                website.display_name = f"{website.name} ({website.acronym})"
                website.display_link = website.acronym  # Solo el acrónimo
            else:
                website.display_name = website.name
                website.display_link = website.name  # Solo el nombre


        context['title'] = self.title
        context['class'] = CSSBackground.Common.WEBSITE
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.WEBSITE
        context['key_map'] = KeyMap.Common.WEBSITE
        # print('🔑 Key Map:', context['key_map'])  # Debug por consola

        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Website.ADD),
                'label': _('Añadir'),
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    Website Detail
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






"""
class CountryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    # Configuración...

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Debes estar logueado para acceder a esta página.")
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return request.user.is_staff or request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permisos para realizar esta acción.")
        return redirect(URLS.Home.COMMON)

"""