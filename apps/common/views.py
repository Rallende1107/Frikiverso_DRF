# Django imports
from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView, View)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy, reverse
# Modelos
from .models import (Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,)
# Fomularios
from .forms import (CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm, PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm,)

from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap

############################################################################################################################################    Constantes

############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.HOME
    title = 'General'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.COMMON
        context['title'] = self.title
        card_sections = {

            'Administración de Usuarios': [
                {
                    'title': 'Usuarios',
                    'img_url': ImageCards.Users.USER,
                    'go_url': None,
                    'view_url': URLS.Users.LST,
                    'add_url': URLS.Users.ADD,
                    'text': 'Gestionar usuarios del sistema.',
                    'extra_buttons': [
                        {
                            'url': URLS.Users.ADD_STAFF,
                            'label': 'Crear usuario staff',
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                        {
                            'url': URLS.Users.ADD_SUPER,
                            'label': 'Crear superusuario',
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                    ],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },
            ],

            'Gestión General': [
                {
                    'title': 'Países',
                    'img_url': ImageCards.Common.COUNTRY,
                    'go_url': None,
                    'view_url': URLS.Common.Country.LST,
                    'add_url': URLS.Common.Country.ADD,
                    'text': 'Gestionar países del sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Formatos',
                    'img_url': ImageCards.Common.FORMAT,
                    'go_url': None,
                    'view_url': URLS.Common.Format.LST,
                    'add_url': URLS.Common.Format.ADD,
                    'text': 'Gestionar formatos del sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tamaños de imagen',
                    'img_url': ImageCards.Common.IMAGE_SIZE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestionar tamaños de imagen del sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Lenguajes',
                    'img_url': ImageCards.Common.LANGUAGE,
                    'go_url': None,
                    'view_url': URLS.Common.Language.LST,
                    'add_url': URLS.Common.Language.ADD,
                    'text': 'Gestionar lenguajes del sistema.',
                    'extra_buttons': [],
                },
            ],

            'Gestión de Personas': [
                {
                    'title': 'Personas',
                    'img_url': ImageCards.Common.PERSON,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestionar personas del sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes de personas',
                    'img_url': ImageCards.Common.PERSON_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestionar imágenes de personas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes extra de personas',
                    'img_url': ImageCards.Common.PERSON_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestionar imágenes adicionales de personas.',
                    'extra_buttons': [],
                },
            ],

            'Configuración Adicional': [
                {
                    'title': 'Calidades',
                    'img_url': ImageCards.Common.QUALITY,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestionar calidades del sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Sitios web',
                    'img_url': ImageCards.Common.WEBSITE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestionar sitios web del sistema.',
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
        return context


####################################################################    CORE   #####################################################################

############################################################################################################################################    Country
class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.ADD
    success_url = reverse_lazy(URLS.Common.Country.LST)
    title = 'Añadir País'

    def test_func(self):
        # Permitir acceso si es superusuario o staff
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'País "{name}" creado exitosamente!')
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

class CountryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = Templates.Common.Country.ADD
    success_url = reverse_lazy(URLS.Common.Country.LST)
    title = 'Editar País'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'País "{name}" editado exitosamente!')
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

class CountryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Country
    template_name = Templates.Common.Country.LST
    context_object_name = 'country'
    title = 'Lista de Países'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URLS.Home.COMMON)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # for language in context['countries']:
        #     # Combina el nombre y las iniciales en inglés
        #     if language.acronym:
        #         language.combined_language = f'{language.name} ({language.acronym})'
        #     else:
        #         language.combined_language = language.name

        #     # Combina el nombre y las iniciales en español
        #     if language.name_esp:
        #         language.combined_language_esp = f'{language.name_esp} ({language.acronym})'
        #     else:
        #         language.combined_language_esp = language.name_esp

        context['title'] = self.title
        context['class'] = CSSBackground.Common.COUNTRY
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.Common.COUNTRY
        context['key_map'] = KeyMap.Common.COUNTRY
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Country.ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class CountryDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Country
    template_name = Templates.Common.Country.DTL
    context_object_name = 'country'

    # 1. Funciones de permisos
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(reverse_lazy(URLS.Common.Country.LST))

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El País que buscas no se encontró.')
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
class FormatCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Format
    form_class = FormatForm
    template_name = Templates.Common.Format.ADD
    success_url = reverse_lazy(URLS.Common.Format.LST)
    title = 'Añadir Formato'

    def test_func(self):
        # Permitir acceso si es superusuario o staff
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Formato "{name}" creado exitosamente!')
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

class FormatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Format
    form_class = FormatForm
    template_name = Templates.Common.Format.ADD
    success_url = reverse_lazy('core_app:format_list')
    title = 'Editar Formato'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Formato "{name}" editado exitosamente!')
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

class FormatListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Format
    template_name = Templates.Common.Format.LST
    context_object_name = 'formats'
    title = 'Lista de Formatos'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URLS.Home.COMMON)

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
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Common.Format.ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class FormatDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Format
    template_name = Templates.Common.Format.DTL
    context_object_name = 'format'

    # 1. Funciones de permisos
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(reverse_lazy(URLS.Common.Format.LST))

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El formato que buscas no se encontró.')
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

#

############################################################################################################################################    Lenguaje
class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = Templates.Common.Language.ADD
    success_url = reverse_lazy(URLS.Common.Language.LST)
    title = 'Añadir Idioma'

    def test_func(self):
        # Permitir acceso si es superusuario o staff
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Idioma "{name}" creado exitosamente!')
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

class LanguageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = Templates.Common.Language.ADD
    success_url = reverse_lazy(URLS.Common.Language.LST)
    title = 'Editar Idioma'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.INDEX)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Idioma "{name}" editado exitosamente!')
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

class LanguageListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Language
    template_name = Templates.Common.Language.LST
    context_object_name = 'languages'
    title = 'Lista de Idiomas'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URLS.Home.COMMON)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for language in context['languages']:
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

class LanguageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Language
    template_name = Templates.Common.Language.DTL
    context_object_name = 'language'

    # 1. Funciones de permisos
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(reverse_lazy(URLS.Common.Language.LST))

    # 2. Funciones de acceso al objeto
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El Idioma que buscas no se encontró.')
            return redirect(reverse_lazy(URLS.Common.Language.LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        """Obtiene el álbum o lanza un Http404 si no se encuentra."""
        return get_object_or_404(Language, pk=self.kwargs['pk'])

    # 3. Función de contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Información adicional del contexto
        context['class'] = CSSBackground.Common.LANGUAGE
        context['title'] = self.object.name
        context['objeto'] = self.object
        context['listURL'] = reverse_lazy(URLS.Common.Language.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

# ############################################################################################################################################    FormatosLenguaje

