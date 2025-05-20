import time
# Django imports
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView, DetailView, TemplateView, View)
# Local app imports
from .models import (Developer, Translator, Publisher, DeveloperLink, TranslatorLink, PublisherLink,)
from .models import (GenreRenpy, GameEngine, GameState, Platform,)
from .models import (Game, GameImage, CoverGame)
from .forms import (DeveloperForm, TranslatorForm, PublisherForm, DeveloperLinkForm, TranslatorLinkForm, PublisherLinkForm,)
from .forms import (GenreRenpyForm, GameEngineForm, GameStateForm, PlatformForm,)
from .forms import (GameForm, GameImageForm, CoverGameForm)
# Utility imports
from Frikiverso.utils import delete_previous_media
from .funciones import process_f95_url, generate_unique_negative_id, iniciar_scraper
from .utils import obtener_ultimo_id
from Frikiverso.constantes import *
from Frikiverso.constantes_img import *



# # Create your views here.
############################################################################################################################################    Home.
class RenpyVerseHomeView(TemplateView):
    template_name = TPL_HOME
    title = 'Inicio Juegos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_HOME
        context['title'] = self.title
        context['cards'] = [
            {
                'title': 'Juegos',
                'img_url': IMG_RENPY_GAME,
                'view_url': URL_RENPY_GAME_LST,
                'add_url': URL_RENPY_GAME_ADD,
                'text': 'Gestión de Juegos',
                'extra_buttons': [
                    {
                        'url': URL_RENPY_GAME_LOAD,
                        'label': 'Cargar Juegos de F95',
                        'icon': 'bi bi-cloud-arrow-up',
                        'show': self.request.user.is_superuser,
                        'btn_class': 'btn-danger'
                    },
                    ],
            },
            {
                'title': 'Géneros Juegos',
                'img_url': IMG_RENPY_GENRE,
                'view_url': URL_RENPY_GENRE_LST,
                'add_url': URL_RENPY_GENRE_ADD,
                'text': 'Gestión de Géneros Juegos',
                'extra_buttons': [],
            },
            {
                'title': 'Desarrolladores',
                'img_url': IMG_RENPY_DEVELOPER,
                'view_url': URL_RENPY_DEVELOPER_LST,
                'add_url': URL_RENPY_DEVELOPER_ADD,
                'text': 'Gestión de Desarrolladores',
                'extra_buttons': [],
            },
            {
                'title': 'Motores Desarrollo',
                'img_url': IMG_RENPY_ENGINE,
                'view_url': URL_RENPY_ENGINE_LST,
                'add_url': URL_RENPY_ENGINE_ADD,
                'text': 'Gestión de Motores Desarrollo',
                'extra_buttons': [],
            },
            {
                'title': 'Plataformas',
                'img_url': IMG_RENPY_PLATFORM,
                'view_url': URL_RENPY_PLATFORM_LST,
                'add_url': URL_RENPY_PLATFORM_ADD,
                'text': 'Gestión de Plataformas',
                'extra_buttons': [],
            },
            {
                'title': 'Estados',
                'img_url': IMG_RENPY_STATUS,
                'view_url': URL_RENPY_STATUS_LST,
                'add_url': URL_RENPY_STATUS_ADD,
                'text': 'Gestión de Estados',
                'extra_buttons': [],
            },
            {
                'title': 'Traductores',
                'img_url': IMG_RENPY_TRANSLATOR,
                'view_url': URL_RENPY_TRANSLATOR_LST,
                'add_url': URL_RENPY_TRANSLATOR_ADD,
                'text': 'Gestión de Traductores',
                'extra_buttons': [],
            },
            {
                'title': 'Editores',
                'img_url': IMG_RENPY_PUBLISHER,
                'view_url': URL_RENPY_PUBLISHER_LST,
                'add_url': URL_RENPY_PUBLISHER_ADD,
                'text': 'Gestión de Editores',
                'extra_buttons': [],
            },
            {
                'title': 'Img. Juegos',
                'img_url': IMG_RENPY_GAME_IMG,
                'view_url': URL_RENPY_GAME_IMG_LST,
                'add_url': URL_RENPY_GAME_IMG_ADD,
                'text': 'Gestión de Imagenes de Juegos',
                'extra_buttons': [],
            },
            {
                'title': 'Web\'s Desarrolladores',
                'img_url': IMG_RENPY_DEVELOPER_LINK,
                'view_url': URL_RENPY_DEVELOPER_LINK_LST,
                'add_url': URL_RENPY_DEVELOPER_LINK_ADD,
                'text': 'Gestión de Web\'s Desarrolladores',
                'extra_buttons': [],
            },
            {
                'title': 'Web\'s Traductores',
                'img_url': IMG_RENPY_TRANSLATOR_LINK,
                'view_url': URL_RENPY_TRANSLATOR_LINK_LST,
                'add_url': URL_RENPY_TRANSLATOR_LINK_ADD,
                'text': 'Gestión de Web\'s Traductores',
                'extra_buttons': [],
            },
            {
                'title': 'Web\'s Editores',
                'img_url': IMG_RENPY_PUBLISHER_LINK,
                'view_url': URL_RENPY_PUBLISHER_LINK_LST,
                'add_url': URL_RENPY_PUBLISHER_LINK_ADD,
                'text': 'Gestión de Web\'s Editores',
                'extra_buttons': [],
            },
            {
                'title': 'Portada Juegos',
                'img_url': IMG_RENPY_COVER_GAME,
                'view_url': URL_RENPY_COVER_GAME_LST,
                'add_url': URL_RENPY_COVER_GAME_ADD,
                'text': 'Gestióna las portadas de los juegos',
                'extra_buttons': [],
            },
        ]
        return context

############################################################################################################################################    Developer
class DeveloperCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = TPL_RENPY_DEVELOPER_ADD
    success_url = reverse_lazy(URL_RENPY_DEVELOPER_LST)
    title = 'Añadir Desarrollador'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Desarrollador "{name}" creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_DEVELOPER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class DeveloperUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = TPL_RENPY_DEVELOPER_ADD
    success_url = reverse_lazy(URL_RENPY_DEVELOPER_LST)
    title = 'Editar Desarrollador'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        objeto = self.get_object()
        media_url = objeto.get_img_url() if objeto else None

        self.object = form.save()
        if 'img' in self.request.FILES and media_url:
            try:
                delete_previous_media(media_url)
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la imagen anterior: {e}')

        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Desarrollador "{name}" editado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        media_url = None

        form = self.get_form()
        if 'img' in form.fields:
            objeto = self.get_object()
            media_url = objeto.get_img_url() if objeto and objeto.get_img_url() else None

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        context['class'] = BG_RENPY_DEVELOPER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class DeveloperListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Developer
    template_name = TPL_RENPY_DEVELOPER_LST
    context_object_name = 'developers'
    title = 'Lista de Desarrolladores'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = BG_RENPY_DEVELOPER
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENTITIES
        context['key_map'] = KEY_RENPY_DEVELOPER
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST),
                'label': 'Enlaces',
                'icon': 'bi bi-list-ul',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_LINK_ADD),
                'label': 'Anadir Enlace',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class DeveloperDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Developer
    template_name = TPL_RENPY_DEVELOPER_DTL
    context_object_name = 'developer'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El desarrollador que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_DEVELOPER_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Developer, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()

        context['objeto'] = self.object
        context['links'] = self.object.links.filter(is_active=True)
        context['class'] = BG_RENPY_DEVELOPER
        context['img_url'] = img_url
        context['title'] = self.object.name
        context['listURL'] =  reverse_lazy(URL_RENPY_DEVELOPER_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    Translator
class TranslatorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Translator
    form_class = TranslatorForm
    template_name = TPL_RENPY_TRANSLATOR_ADD
    success_url = reverse_lazy(URL_RENPY_TRANSLATOR_LST)
    title = 'Añadir Traductor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Traductor "{name}" creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_TRANSLATOR
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Translator
    form_class = TranslatorForm
    template_name = TPL_RENPY_TRANSLATOR_ADD
    success_url = reverse_lazy(URL_RENPY_TRANSLATOR_LST)
    title = 'Editar Traductor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        objeto = self.get_object()
        media_url = objeto.get_img_url() if objeto else None

        self.object = form.save()
        if 'img' in self.request.FILES and media_url:
            try:
                delete_previous_media(media_url)
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la imagen anterior: {e}')

        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Traductor "{name}" editado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        media_url = None

        form = self.get_form()
        if 'img' in form.fields:
            objeto = self.get_object()
            media_url = objeto.get_img_url() if objeto and objeto.get_img_url() else None

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        context['class'] = BG_RENPY_TRANSLATOR
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Translator
    template_name = TPL_RENPY_TRANSLATOR_LST
    context_object_name = 'translators'
    title = 'Lista de Traductores'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = BG_RENPY_TRANSLATOR
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENTITIES
        context['key_map'] = KEY_RENPY_TRANSLATOR
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST),
                'label': 'Enlaces',
                'icon': 'bi bi-list-ul',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_LINK_ADD),
                'label': 'Anadir Enlace',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class TranslatorDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Translator
    template_name = TPL_RENPY_TRANSLATOR_DTL
    context_object_name = 'translator'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El traductor que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_TRANSLATOR_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Translator, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()

        context['img_url'] = img_url
        context['links'] = self.object.links.filter(is_active=True)
        context['class'] = BG_RENPY_TRANSLATOR
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        context['listURL'] =  reverse_lazy(URL_RENPY_TRANSLATOR_LST)
        return context

############################################################################################################################################    Publisher
class PublisherCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = TPL_RENPY_PUBLISHER_ADD
    success_url = reverse_lazy(URL_RENPY_PUBLISHER_LST)
    title = 'Añadir Editor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Editor creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_PUBLISHER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = TPL_RENPY_PUBLISHER_ADD
    success_url = reverse_lazy(URL_RENPY_PUBLISHER_LST)
    title = 'Editar Editor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        objeto = self.get_object()
        media_url = objeto.get_img_url() if objeto else None

        self.object = form.save()
        if 'img' in self.request.FILES and media_url:
            try:
                delete_previous_media(media_url)
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la imagen anterior: {e}')

        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Editor "{name}" editado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        media_url = None

        form = self.get_form()
        if 'img' in form.fields:
            objeto = self.get_object()
            media_url = objeto.get_img_url() if objeto and objeto.get_img_url() else None

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        context['class'] = BG_RENPY_PUBLISHER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Publisher
    template_name = TPL_RENPY_PUBLISHER_LST
    context_object_name = 'publishers'
    title = 'Lista de Editores'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = BG_RENPY_PUBLISHER
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENTITIES
        context['key_map'] = KEY_RENPY_PUBLISHER
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST),
                'label': 'Enlaces',
                'icon': 'bi bi-list-ul',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_LINK_ADD),
                'label': 'Anadir Enlace',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PublisherDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Publisher
    template_name = TPL_RENPY_PUBLISHER_DTL
    context_object_name = 'publisher'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El editor que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_PUBLISHER_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Publisher, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()
        game_count = objeto.get_num_games()
        context['game_count'] = game_count
        context['img_url'] = img_url
        context['links'] = self.object.links.filter(is_active=True)
        context['class'] = BG_RENPY_PUBLISHER
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        context['listURL'] =  reverse_lazy(URL_RENPY_PUBLISHER_LST)
        return context

############################################################################################################################################    Developer Links
class DeveloperLinkCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DeveloperLink
    form_class = DeveloperLinkForm
    template_name = TPL_RENPY_DEVELOPER_LINK_ADD
    success_url = reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST)
    title = 'Añadir Enlace de Desarrollador'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Enlace de desarrollador creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_DEVELOPER_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class DeveloperLinkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DeveloperLink
    form_class = DeveloperLinkForm
    template_name = TPL_RENPY_DEVELOPER_LINK_ADD
    success_url = reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST)
    title = 'Editar Enlace de Desarrollador'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Enlace de desarrollador editado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_DEVELOPER_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class DeveloperLinkListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = DeveloperLink
    template_name = TPL_RENPY_DEVELOPER_LINK_LST
    context_object_name = 'developer_links'
    title = 'Lista de Enlaces Desarrolladores'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = BG_RENPY_DEVELOPER_LINK
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENTITIES_LINK
        context['key_map'] = KEY_RENPY_DEVELOPER_LINK
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_LINK_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_LST),
                'label': 'Desarrolladores',
                'icon': 'bi bi-list-ul',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_ADD),
                'label': 'Anadir Desarrollador',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class DeveloperLinkDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = DeveloperLink
    template_name = TPL_RENPY_DEVELOPER_LINK_DTL
    context_object_name = 'developer_link'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El link de desarrollador que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(DeveloperLink, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        developer = self.object.developer
        context['developer_name'] = developer.name if developer else "N/A"
        context['developer'] = developer
        context['class'] = BG_RENPY_DEVELOPER_LINK
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] =  reverse_lazy(URL_RENPY_DEVELOPER_LINK_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    Translator Links
class TranslatorLinkCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = TranslatorLink
    form_class = TranslatorLinkForm
    template_name = TPL_RENPY_TRANSLATOR_LINK_ADD
    success_url = reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST)
    title = 'Añadir Enlace de Traductor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Enlace de traductor creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_TRANSLATOR_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorLinkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TranslatorLink
    form_class = TranslatorLinkForm
    template_name = TPL_RENPY_TRANSLATOR_LINK_ADD
    success_url = reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST)
    title = 'Editar Enlace de Traductor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Enlace de traductor editado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_TRANSLATOR_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class TranslatorLinkListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = TranslatorLink
    template_name = TPL_RENPY_TRANSLATOR_LINK_LST
    context_object_name = 'translator_links'
    title = 'Lista de Enlaces Traductores'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = BG_RENPY_TRANSLATOR_LINK
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENTITIES_LINK
        context['key_map'] = KEY_RENPY_TRANSLATOR_LINK
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_LINK_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_LST),
                'label': 'Traductores',
                'icon': 'bi bi-list-ul',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_ADD),
                'label': 'Anadir Traductor',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class TranslatorLinkDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = TranslatorLink
    template_name = TPL_RENPY_TRANSLATOR_LINK_DTL
    context_object_name = 'translator_link'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El link del traductor que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(TranslatorLink, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        translator = self.object.translator
        context['translator_name'] = translator.name if translator else "N/A"
        context['translator'] = translator
        context['class'] = BG_RENPY_TRANSLATOR_LINK
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] =  reverse_lazy(URL_RENPY_TRANSLATOR_LINK_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    PublisherLink
class PublisherLinkCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = PublisherLink
    form_class = PublisherLinkForm
    template_name = TPL_RENPY_PUBLISHER_LINK_ADD
    success_url = reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST)
    title = 'Añadir Enlace de Editor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Enlace del editor creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_PUBLISHER_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherLinkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PublisherLink
    form_class = PublisherLinkForm
    template_name = TPL_RENPY_PUBLISHER_LINK_ADD
    success_url = reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST)
    title = 'Editar Enlace de Editor'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Enlace del editor editado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_PUBLISHER_LINK
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PublisherLinkListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = PublisherLink
    template_name = TPL_RENPY_PUBLISHER_LINK_LST
    context_object_name = 'publisher_links'
    title = 'Lista de Enlaces Editores'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.title
        context['class'] = BG_RENPY_PUBLISHER_LINK
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENTITIES_LINK
        context['key_map'] = KEY_RENPY_PUBLISHER_LINK
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_LINK_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_LST),
                'label': 'Editores',
                'icon': 'bi bi-list-ul',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_ADD),
                'label': 'Anadir Editor',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PublisherLinkDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PublisherLink
    template_name = TPL_RENPY_PUBLISHER_LINK_DTL
    context_object_name = 'publisher_link'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El link del editor que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(PublisherLink, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publisher = self.object.publisher
        context['publisher_name'] = publisher.name if publisher else "N/A"
        context['publisher'] = publisher
        context['class'] = BG_RENPY_PUBLISHER_LINK
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] =  reverse_lazy(URL_RENPY_PUBLISHER_LINK_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    Generos
class GenreRenpyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = GenreRenpy
    form_class = GenreRenpyForm
    template_name = TPL_RENPY_GENRE_ADD
    success_url = reverse_lazy(URL_RENPY_GENRE_LST)
    title = 'Añadir Género'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Género "{name}" creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GenreRenpyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GenreRenpy
    form_class = GenreRenpyForm
    template_name = TPL_RENPY_GENRE_ADD
    success_url = reverse_lazy(URL_RENPY_GENRE_LST)
    title = 'Editar Género'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Género "{name}" editado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_GENRE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GenreRenpyListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = GenreRenpy
    template_name = TPL_RENPY_GENRE_LST
    context_object_name = 'genres'
    title = 'Lista de Géneros'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for genre in context['genres']:
            if genre.name_esp:
                genre.display_name = f'{genre.name} ({genre.name_esp})'
            else:
                genre.display_name = genre.name

        context['title'] = self.title
        context['class'] = BG_RENPY_GENRE
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_GENRE
        context['key_map'] = KEY_RENPY_GENRE
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_GENRE_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GenreRenpyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = GenreRenpy
    template_name = TPL_RENPY_GENRE_DTL
    context_object_name = 'genre'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El género de juego que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_GENRE_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GenreRenpy, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_count'] = self.object.get_num_games()
        context['class'] = BG_RENPY_GENRE
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] = reverse_lazy(URL_RENPY_GENRE_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    GameEngine
class GameEngineCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = GameEngine
    form_class = GameEngineForm
    template_name = TPL_RENPY_ENGINE_ADD
    success_url = reverse_lazy(URL_RENPY_ENGINE_LST)
    title = 'Añadir Motor Desarrollo'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Motor de Desarrollo "{name}" creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_ENGINE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameEngineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GameEngine
    form_class = GameEngineForm
    template_name = TPL_RENPY_ENGINE_ADD
    success_url = reverse_lazy(URL_RENPY_ENGINE_LST)
    title = 'Editar Motor Desarrollo'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        messages.success(self.request, f'Motor de Desarrollo "{name}" editado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_ENGINE
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameEngineListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = GameEngine
    template_name = TPL_RENPY_ENGINE_LST
    context_object_name = 'engines'
    title = 'Lista de Motores de Desarrollo'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for engine in context['engines']:
            if engine.name_esp:
                engine.display_name = f'{engine.name} ({engine.name_esp})'
            else:
                engine.display_name = engine.name

        context['title'] = self.title
        context['class'] = BG_RENPY_ENGINE
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENGINE
        context['key_map'] = KEY_RENPY_ENGINE
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_ENGINE_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameEngineDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = GameEngine
    template_name = TPL_RENPY_ENGINE_DTL
    context_object_name = 'engine'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El motor de desarrollo que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_ENGINE_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GameEngine, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_count'] = self.object.get_num_games()
        context['class'] = BG_RENPY_ENGINE
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] = reverse_lazy(URL_RENPY_ENGINE_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    GameState
class GameStateCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = GameState
    form_class = GameStateForm
    template_name = TPL_RENPY_STATUS_ADD
    success_url = reverse_lazy(URL_RENPY_STATUS_LST)
    title = 'Añadir Estado del Juego'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Estado del juego creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_STATUS
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameStateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GameState
    form_class = GameStateForm
    template_name = TPL_RENPY_STATUS_ADD
    success_url = reverse_lazy(URL_RENPY_STATUS_LST)
    title = 'Editar Estado del Juego'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Estado del juego editado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_STATUS
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameStateListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = GameState
    template_name = TPL_RENPY_STATUS_LST
    context_object_name = 'game_statuses'
    title = 'Lista de Estados'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for game_statu in context['game_statuses']:
            if game_statu.name_esp:
                game_statu.display_name = f"{game_statu.name} ({game_statu.name_esp})"
            else:
                game_statu.display_name = game_statu.name

        context['title'] = self.title
        context['class'] = BG_RENPY_STATUS
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_STATUS
        context['key_map'] = KEY_RENPY_STATUS
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_STATUS_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameStateDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = GameState
    template_name = TPL_RENPY_STATUS_DTL
    context_object_name = 'game_statu'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El estado de juego que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_STATUS_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GameState, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_count'] = self.object.get_num_games()
        context['class'] = BG_RENPY_STATUS
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] = reverse_lazy(URL_RENPY_STATUS_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    Platform
class PlatformCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Platform
    form_class = PlatformForm
    template_name = TPL_RENPY_PLATFORM_ADD
    success_url = reverse_lazy(URL_RENPY_PLATFORM_LST)
    title = 'Añadir Plataforma'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Plataforma creada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_PLATFORM
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PlatformUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Platform
    form_class = PlatformForm
    template_name = TPL_RENPY_PLATFORM_ADD
    success_url = reverse_lazy(URL_RENPY_PLATFORM_LST)
    title = 'Editar Plataforma'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Plataforma editada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_PLATFORM
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class PlatformListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Platform
    template_name = TPL_RENPY_PLATFORM_LST
    context_object_name = 'platforms'
    title = 'Lista de Plataformas'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for platform in context['platforms']:
            if platform.name_esp:
                platform.display_name = f"{platform.name} ({platform.name_esp})"
            else:
                platform.display_name = platform.name

        context['title'] = self.title
        context['class'] = BG_RENPY_PLATFORM
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_PLATFORM
        context['key_map'] = KEY_RENPY_PLATFORM
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PLATFORM_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class PlatformDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Platform
    template_name = TPL_RENPY_PLATFORM_DTL
    context_object_name = 'platform'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'La plataforma que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_PLATFORM_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Platform, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_count'] = self.object.get_num_games()
        context['class'] = BG_RENPY_PLATFORM
        context['objeto'] = self.object
        context['title'] = self.object.name
        context['listURL'] = reverse_lazy(URL_RENPY_PLATFORM_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    Game
class GameCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = TPL_RENPY_GAME_ADD
    success_url = reverse_lazy(URL_RENPY_GAME_LST)
    title = 'Añadir Juego'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        name = form.cleaned_data.get('title')
        url_f95 = form.cleaned_data.get('f95zone_link')
        url_steam = form.cleaned_data.get('steam_link')
        version = form.cleaned_data.get('version')

        if url_f95:
            short_url, post_id = process_f95_url(url_f95)
            if short_url is None or post_id is None:
                messages.error(self.request, 'URL de F95Zone no válida.')
                return self.form_invalid(form)

            game = form.save(commit=False)
            game.f95zone_link = short_url
            game.f95_id = post_id
        else:
            game = form.save(commit=False)
            game.f95_id = generate_unique_negative_id()  # Usa la función utilitaria

        game.version_txt = version
        game.save()

        messages.success(self.request, f'Juego "{name}" creado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_GAME
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = TPL_RENPY_GAME_ADD
    success_url = reverse_lazy(URL_RENPY_GAME_LST)
    title = 'Editar Juego'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        objeto = self.get_object()
        img_url = objeto.get_img_url() if objeto else None

        # Guardar el formulario sin comprometer
        game = form.save(commit=False)

        # Procesar la URL de F95Zone
        url_f95 = form.cleaned_data.get('f95zone_link')

        if url_f95:
            short_url, post_id = process_f95_url(url_f95)
            if short_url is None or post_id is None:
                return self.form_invalid(form)

            game.f95zone_link = short_url
            game.f95_id = post_id
        else:
            # Generar un ID negativo único si no hay enlace de F95Zone
            if game.f95_id is None:
                game.f95_id = generate_unique_negative_id()

        # Actualizar la versión y version_txt
        new_version = form.cleaned_data.get('version')
        game.version_txt = new_version  # Siempre actualizamos version_txt

        # Manejo de la imagen, si es necesario
        if 'cover' in self.request.FILES and img_url:
            try:
                delete_previous_media(img_url)
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la imagen anterior: {e}')

        # Guardar el juego
        game.save()
        name = form.cleaned_data.get('title')
        messages.success(self.request, f'Juego "{name}" editado exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        media_url = None
        form = self.get_form()
        if 'cover' in form.fields:
            objeto = self.get_object()
            media_url = objeto.get_img_url() if objeto and objeto.get_img_url() else None

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        context['class'] = BG_RENPY_GAME
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_LST
    context_object_name = 'games'
    title = 'Lista de Juegos'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Agregar lógica para formatear animes y mangas
        for game in context['games']:
            # Formatear los nombres de los animes
            game.developer_names = ', '.join(dev.name for dev in game.developers.all())
            # Obtener los nombres de los estados del juego
            game.state_names = ', '.join(status.name for status in game.states.all())

            # Obtener los nombres de los motores
            game.engine_names = ', '.join(engine.name for engine in game.engines.all())

            # Obtener los nombres de los géneros
            game.genre_names = ', '.join(genre.name for genre in game.genres.all())

            # Obtener los nombres de las plataformas
            game.platform_names = ', '.join(platform.name for platform in game.platforms.all())

            # Obtener los nombres de los idiomas originales
            game.language_names = ', '.join(lang.name for lang in game.languages.all())

            # Obtener los nombres de los traductores
            game.translator_names = ', '.join(translator.name for translator in game.translators.all())

        context['title'] = self.title
        context['class'] = BG_RENPY_GAME
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_GAME
        context['key_map'] = KEY_RENPY_GAME
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_GAME_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URL_RENPY_GAME_LOAD),
                'label': 'Cargar desde F95',
                'icon': 'bi bi-cloud-arrow-down',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class GameDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Game
    template_name = TPL_RENPY_GAME_DTL
    context_object_name = 'game'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'El juego que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_GAME_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Game, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.object  # Obtén el objeto de juego actual
        # Obtener los nombres de los desarrolladores
        game.developer_names = ', '.join(dev.name for dev in game.developers.all())
        # Obtener los nombres de los estados del juego
        game.state_names = ', '.join(status.name for status in game.states.all())
        # Obtener los nombres de los motores
        game.engine_names = ', '.join(engine.name for engine in game.engines.all())
        # Obtener los nombres de los géneros
        game.genre_names = ', '.join(genre.name for genre in game.genres.all())
        # Obtener los nombres de las plataformas
        game.platform_names = ', '.join(platform.name for platform in game.platforms.all())
        # Obtener los nombres de los idiomas originales
        game.language_names = ', '.join(lang.name for lang in game.languages.all())
        # Obtener los nombres de los traductores
        game.translator_names = ', '.join(translator.name for translator in game.translators.all())
        # Obtener las imágenes activas asociadas al juego
        game.images = game.images_as_game.filter(is_active=True)  # Filtrar solo imágenes activas
        # Agregar el juego al contexto

        context['game'] = game
        context['class'] = BG_RENPY_GAME
        context['objeto'] = self.object
        context['title'] = self.object.title
        context['listURL'] = reverse_lazy(URL_RENPY_GAME_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################    GameImage
class GameImageCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = GameImage
    form_class = GameImageForm
    template_name = TPL_RENPY_GAME_IMG_ADD
    success_url = reverse_lazy(URL_RENPY_GAME_IMG_LST)
    title = 'Añadir Imagen del Juego'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Imagen del juego creada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_GAME_IMG
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GameImage
    form_class = GameImageForm
    template_name = TPL_RENPY_GAME_IMG_ADD
    success_url = reverse_lazy(URL_RENPY_GAME_IMG_LST)
    title = 'Editar Imagen del Juego'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        objeto = self.get_object()
        media_url = objeto.get_img_url() if objeto else None

        self.object = form.save()
        if 'img' in self.request.FILES and media_url:
            try:
                delete_previous_media(media_url)
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la imagen anterior: {e}')

        messages.success(self.request, f'Imagen  editado exitosamente!')
        return super().form_valid(form)


    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        media_url = None
        form = self.get_form()
        if 'img' in form.fields:
            objeto = self.get_object()
            media_url = objeto.get_img_url() if objeto and objeto.get_img_url() else None

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        context['class'] = BG_RENPY_GAME_IMG
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class GameImageListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = GameImage
    template_name = TPL_RENPY_GAME_IMG_LST
    context_object_name = 'game_images'
    title = 'Lista de Imágenes de Juego'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.title
        context['class'] = BG_RENPY_GAME_IMG
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_GAME_IMG
        context['key_map'] = KEY_RENPY_GAME_IMG
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_GAME_IMG_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context


class GameImageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = GameImage
    template_name = TPL_RENPY_GAME_IMG_DTL
    context_object_name = 'game_image'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            messages.error(self.request, 'La imagen del juego que buscas no se encontró.')
            return redirect(reverse_lazy(URL_RENPY_GAME_IMG_LST))

        return super().get(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(GameImage, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_size'] = self.object.file_size  # Agregar tamaño del archivo al contexto
        context['dimensions'] = self.object.dimensions  # Agregar dimensiones de la imagen al contexto
        juego = self.object.game.title
        title = f'Img. de {juego}'
        context['class'] = BG_RENPY_GAME_IMG
        context['objeto'] = self.object
        context['title'] = title
        context['listURL'] = reverse_lazy(URL_RENPY_GAME_IMG_LST)
        context['homeURL'] = reverse_lazy(URL_RENPY_HOME)
        return context

############################################################################################################################################ Game Cover
class CoverGameCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CoverGame
    form_class = CoverGameForm
    template_name = 'renpy/cover_game/cover_game_form.html'
    success_url = reverse_lazy(URL_RENPY_COVER_GAME_LST)
    title = 'Añadir portada Juegos'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Portada de juego creada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_COVER_GAME
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class CoverGameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CoverGame
    form_class = CoverGameForm
    template_name = 'renpy/cover_game/cover_game_form.html'
    success_url = reverse_lazy(URL_RENPY_COVER_GAME_LST)
    title = 'Editar portada Juegos'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def form_valid(self, form):
        messages.success(self.request, 'Portada de juego editada exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = BG_RENPY_COVER_GAME
        context['title'] = self.title

        form = self.get_form()
        have_media_file = 'image' in form.fields
        media_url = None
        if have_media_file:
            objeto = self.get_object()
            if objeto and objeto.get_img_url():
                media_url = objeto.get_img_url()

        context['media_file_table'] = bool(media_url)
        context['media_url'] = media_url
        context['cancel_url'] = self.success_url
        return context

class CoverGameListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CoverGame
    template_name = 'renpy/cover_game/cover_game_list.html'
    context_object_name = 'covers'
    title = 'Lista de Portadas de Juegos'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for img in context['covers']:
            # Si la relación 'juego' es un ForeignKey, accedemos directamente a la propiedad 'juego'
            img.juego_names = img.juego.title if img.juego else "No asignado"

            # Obtener el nombre y la extensión de la imagen
            img.image_name = img.get_image_name() if hasattr(img, 'get_image_name') else None
            img.image_extension = img.get_image_extension() if hasattr(img, 'get_image_extension') else None

            # Obtener la URL de la imagen si está disponible
            img.image_urls = img.image_url if img.image_url else None
            img.image_url = img.image.url if img.image else None

        context['title'] = self.title
        context['class'] = BG_RENPY_COVER_GAME
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_OTAKU_COVER_ANIME
        context['key_map'] = KEY_OTAKU_COVER_ANIME
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_COVER_GAME_ADD),
                'label': 'Añadir',
                'icon': 'bi bi-plus-circle',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

class CoverGameDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CoverGame
    template_name = 'renpy/cover_game/cover_game_detail.html'
    context_object_name = 'image_game'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URL_RENPY_HOME)

    def get_object(self):
        try:
            return get_object_or_404(CoverGame, pk=self.kwargs['pk'])
        except Http404:
            messages.error(
                self.request, 'La imagen que buscas no se encontró.')
            return redirect(URL_OTAKU_IMAGEN_ANIME_LST)

    def get_game_name(self, image):
        juegos = image.juego.all()  # Accede a los juegos relacionados
        juego_names = [juego.title for juego in juegos]  # Crea una lista de títulos
        return ", ".join(juego_names)  # Une los nombres con comas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar los detalles de la imagen normal al contexto
        juego_names = self.get_game_name(self.object)

        # Pasar la lista de nombres al contexto
        context['juego'] = juego_names
        context['image'] = self.object.get_img_url()
        context['image_name'] = self.object.get_image_name()
        context['image_extension'] = self.object.get_image_extension()
        context['image_file_size'] = self.object.image_file_size
        context['image_dimensions'] = self.object.image_dimensions
        context['class'] = BG_OTAKU_COVER_ANIME
        context['objeto'] = self.object
        context['title'] = (f"Portada Juegos {juego_names}")
        context['listURL'] = reverse_lazy(URL_OTAKU_IMAGEN_ANIME_LST)
        context['homeURL'] = reverse_lazy(URL_OTAKU_HOME_ANIME)
        return context

############################################################################################################################################ Game By
class GamesByDeveloperListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(developers__id=self.kwargs['developer_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        developer = Developer.objects.get(id=self.kwargs['developer_id'])
        context['developer'] = developer
        context['title'] = f'Lista de Juegos de "{developer.name}"'
        context['class'] = BG_RENPY_DEVELOPER
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_DEVELOPER
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_DEVELOPER_LST),
                'label': 'Desarrolladores',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GamesByStatesListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(states__id=self.kwargs['status_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = GameState.objects.get(id=self.kwargs['status_id'])
        context['status'] = status

        context['title'] = f'Lista de Juegos con estado: {status.name}'
        context['class'] = BG_RENPY_STATUS
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_STATUS
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_STATUS_LST),
                'label': 'Estados',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GamesByPlatformListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(platforms__id=self.kwargs['platform_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        platform = Platform.objects.get(id=self.kwargs['platform_id'])
        context['platform'] = platform

        context['title'] = f'Lista de Juegos para: {platform.name}'
        context['class'] = BG_RENPY_PLATFORM
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_PLATFORM
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PLATFORM_LST),
                'label': 'Plataformas',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GamesByEngineListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(engine__id=self.kwargs['engine_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        engine = GameEngine.objects.get(id=self.kwargs['engine_id'])
        context['engine'] = engine

        context['title'] = f'Lista de Juegos desarrollados con: {engine.name}'
        context['class'] = BG_RENPY_ENGINE
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_ENGINE
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_ENGINE_LST),
                'label': 'Motores de Desarrollo',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GamesByGenreListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(genres__id=self.kwargs['genre_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = GenreRenpy.objects.get(id=self.kwargs['genre_id'])
        context['genre'] = genre

        context['title'] = f'Lista de Juegos con género: {genre.name}'
        context['class'] = BG_RENPY_GENRE
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_GENRE
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_GENRE_LST),
                'label': 'Géneros',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GamesByTranslatorListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(translators__id=self.kwargs['translator_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        translator = Translator.objects.get(id=self.kwargs['translator_id'])
        context['translator'] = translator

        context['title'] = f'Lista de Juegos traducidos por: {translator.name}'
        context['class'] = BG_RENPY_TRANSLATOR
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_TRANSLATOR
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_TRANSLATOR_LST),
                'label': 'Traductores',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

class GamesByPublisherListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Game
    template_name = TPL_RENPY_GAME_BY
    context_object_name = 'games'

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, 'Debes estar logueado para acceder a esta página.')
        return redirect(URL_RENPY_HOME)

    def get_queryset(self):
        return Game.objects.filter(publishers__id=self.kwargs['publisher_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publisher = Publisher.objects.get(id=self.kwargs['publisher_id'])
        context['publisher'] = publisher

        context['title'] = f'Lista de Juegos Editados por: {publisher.name}'
        context['class'] = BG_RENPY_PUBLISHER
        context['js_action'] = JS_ACTIONS
        context['js_script'] = JS_CONFIG_RENPY_PUBLISHER
        context['key_map'] = KEY_RENPY_GAME
        context['encabezados'] = ['ID', 'Título', 'Desarrollador', 'Versión', 'Fecha Lanzamiento', 'Estado', 'Activo', 'Acciones']
        context['buttons'] = [
            {
                'url': reverse_lazy(URL_RENPY_HOME),
                'label': 'Inicio',
                'class': 'btn btn-warning btn-lg me-2',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URL_RENPY_PUBLISHER_LST),
                'label': 'Editores',
                'class': 'btn btn-success btn-lg',
                'icon': 'bi bi-list-ul',
                'show': True
            },
        ]
        return context

############################################################################################################################################
class GamesLoadView(View):
    template_name = TPL_RENPY_GAME_LOAD
    title = 'Cargar Juegos desde F95'
    cancel_url = reverse_lazy(URL_RENPY_GAME_LST)

    def get(self, request, *args, **kwargs):
        ultimo_digito = 1
        inicio = int(request.GET.get("inicio", ultimo_digito))  # Parámetro de inicio
        fin = int(request.GET.get("fin", ultimo_digito + 100))  # Parámetro de fin

        context = {
            'inicio': inicio,
            'fin': fin,
            'title': self.title,
            'cancel_url': self.cancel_url,  # Agregar cancel_url al contexto
            'class': 'bg-renpy-game',
            'cargar': True,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ultimo_digito = obtener_ultimo_id() or 1
        inicio = int(request.POST.get("inicio", ultimo_digito))
        fin = int(request.POST.get("fin", inicio + 10))

        # Validación simple
        if fin < inicio:
            context = {
                'error': 'El valor de fin debe ser mayor o igual que inicio.',
                'cancel_url': self.cancel_url,
                'title': self.title
            }
            return render(request, self.template_name, context)


        iniciar_scraper(inicio, fin)

        return redirect(URL_RENPY_HOME)



