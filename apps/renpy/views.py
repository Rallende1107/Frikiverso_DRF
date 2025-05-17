# Django imports
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

# Local app imports - models and forms
# from .models import ()
# from .forms import ()

# Project-level imports - mixins and utilities
from core.mixins import PermissionRequiredMessageMixin
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Juegos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.RENPY
        context['title'] = self.title
        card_sections = {

            'Gestión Principal': [
                {
                    'title': 'Juegos',
                    'img_url': ImageCards.Renpy.GAME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los juegos disponibles en el sistema.',
                    'extra_buttons': [
                        {
                            'url': URLS.Otaku.Load.ANIME,
                            'label': 'Cargar Juegos de F95',
                            'icon': 'bi bi-cloud-arrow-up',
                            'show': self.request.user.is_superuser,
                            'btn_class': 'btn-danger'
                        }
                    ],
                },

                {
                    'title': 'Títulos de Juegos',
                    'img_url': ImageCards.Renpy.TITLE_GAME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los diferentes títulos y traducciones de los juegos.',
                    'extra_buttons': [],
                },
            ],

            'Metadatos': [
                {
                    'title': 'Géneros Juegos',
                    'img_url': ImageCards.Renpy.GENRE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los géneros asignados a los juegos del sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Motores de Desarrollo',
                    'img_url': ImageCards.Renpy.GAME_ENGINE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los motores de desarrollo utilizados para los juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Plataformas',
                    'img_url': ImageCards.Renpy.PLATFORM,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las plataformas para las que están disponibles los juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Prefijos',
                    'img_url': ImageCards.Renpy.PREFIX,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los prefijos utilizados para identificar juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Censura',
                    'img_url': ImageCards.Renpy.CENSORSHIP,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los niveles o tipos de censura aplicados a los juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Estados',
                    'img_url': ImageCards.Renpy.STATUS,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los estados en que pueden encontrarse los juegos.',
                    'extra_buttons': [],
                },
            ],

            'Entidades': [
                {
                    'title': 'Desarrolladores',
                    'img_url': ImageCards.Renpy.DEVELOPER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los desarrolladores asociados a los juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Traductores',
                    'img_url': ImageCards.Renpy.TRANSLATOR,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los traductores responsables de las versiones localizadas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Editores',
                    'img_url': ImageCards.Renpy.PUBLISHER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los editores o publicadores de los juegos.',
                    'extra_buttons': [],
                },
            ],

            'Webs Oficiales': [
                {
                    'title': "Webs Desarrolladores",
                    'img_url': ImageCards.Renpy.DEVELOPER_LINKS,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los enlaces oficiales de los desarrolladores.',
                    'extra_buttons': [],
                },

                {
                    'title': "Webs Traductores",
                    'img_url': ImageCards.Renpy.TRANSLATOR_LINKS,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los enlaces oficiales de los traductores.',
                    'extra_buttons': [],
                },

                {
                    'title': "Webs Editores",
                    'img_url': ImageCards.Renpy.PUBLISHER_LINKS,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los enlaces oficiales de los editores.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia': [
                {
                    'title': 'Imágenes de Juegos',
                    'img_url': ImageCards.Renpy.GAME_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes principales asociadas a los juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Juegos',
                    'img_url': ImageCards.Renpy.GAME_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales o promocionales de los juegos.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes de Desarrolladores',
                    'img_url': ImageCards.Renpy.DEVELOPER_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes oficiales de los desarrolladores.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Desarrolladores',
                    'img_url': ImageCards.Renpy.DEVELOPER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales de los desarrolladores.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes de Traductores',
                    'img_url': ImageCards.Renpy.TRANSLATOR_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes oficiales de los traductores.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Traductores',
                    'img_url': ImageCards.Renpy.TRANSLATOR_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales de los traductores.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes de Editores',
                    'img_url': ImageCards.Renpy.PUBLISHER_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes oficiales de los editores.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Editores',
                    'img_url': ImageCards.Renpy.PUBLISHER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales de los editores.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia': [
                {
                    'title': 'cccccccccccc de Juegos',
                    'img_url': ImageCards.Renpy.GAME_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes principales asociadas a los juegos.',
                    'extra_buttons': [],
                    'show': False,
                },
            ],

            'Sección Administrativa': [
                {
                    'title': 'Datos Juegos',
                    'img_url': ImageCards.Renpy.DATA_GAME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los datos técnicos y portadas de los juegos.',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser
                },
            ]
        }

        # Filtrar tarjetas y secciones que no deben mostrarse
        filtered_sections = {}
        for section, items in card_sections.items():
            filtered_items = [item for item in items if item.get('show', True)]
            if filtered_items:
                filtered_sections[section] = filtered_items

        context['card_sections'] = filtered_sections
        return context
