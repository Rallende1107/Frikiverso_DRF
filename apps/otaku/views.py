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
from core.utils.mixins import PermissionRequiredMessageMixin
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Inicio Otaku'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.OTAKU
        context['title'] = self.title
        card_sections = {

            'Metadatos': [
                {
                    'title': 'Géneros',
                    'img_url': ImageCards.Otaku.GENRE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de géneros de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Temas',
                    'img_url': ImageCards.Otaku.THEME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de temas de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Demografías',
                    'img_url': ImageCards.Otaku.DEMOGRAPHIC,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de demografías de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos',
                    'img_url': ImageCards.Otaku.TYPE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de tipos de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Estados',
                    'img_url': ImageCards.Otaku.STATUS,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de estados de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Años',
                    'img_url': ImageCards.Otaku.YEAR,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de años de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Temporadas',
                    'img_url': ImageCards.Otaku.SEASON,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de temporadas de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Temporadas Año',
                    'img_url': ImageCards.Otaku.SEASON_FULL,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de temporadas por año de anime y manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Clasificaciones',
                    'img_url': ImageCards.Otaku.RATING,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de clasificaciones de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Fuentes',
                    'img_url': ImageCards.Otaku.SOURCE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Fuentes de Animes.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Roles',
                    'img_url': ImageCards.Otaku.ROLE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Roles Personajes y Personal.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos Relaciones',
                    'img_url': ImageCards.Otaku.RELATION_TYPE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de tipos de relaciones de anime y manga.',
                    'extra_buttons': [],
                },
            ],

            'Animes': [
                {
                    'title': 'Animes',
                    'img_url': ImageCards.Otaku.ANIME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Animes.',
                    'extra_buttons': [
                        {
                            'url': URLS.Otaku.Load.ANIME,
                            'label': 'Cargar Animes de MAL',
                            'icon': 'bi bi-cloud-arrow-down',
                            'show': self.request.user.is_superuser,
                            'btn_class': 'btn-danger'
                        },
                    ],
                },

                {
                    'title': 'Títulos Anime',
                    'img_url': ImageCards.Otaku.TITLE_ANIME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de títulos de animes.',
                    'extra_buttons': [],
                },
            ],

            'Música Anime': [
                {
                    'title': 'Canciones Anime',
                    'img_url': ImageCards.Otaku.SONG,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de canciones de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Openings',
                    'img_url': ImageCards.Otaku.SONG_OP,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Openings de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Insert Songs',
                    'img_url': ImageCards.Otaku.SONG_IN,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Insert Songs de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Endings',
                    'img_url': ImageCards.Otaku.SONG_ED,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Endings de manga.',
                    'extra_buttons': [],
                },
            ],

            'Mangas': [
                {
                    'title': 'Mangas',
                    'img_url': ImageCards.Otaku.MANGA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Mangas.',
                    'extra_buttons': [
                        {
                            'url': URLS.Otaku.Load.MANGA,
                            'label': 'Cargar Mangas de MAL',
                            'icon': 'bi bi-cloud-arrow-down',
                            'show': self.request.user.is_superuser,
                            'btn_class': 'btn-danger'
                        },
                    ],
                },

                {
                    'title': 'Títulos Manga',
                    'img_url': ImageCards.Otaku.TITLE_MANGA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de títulos de mangas.',
                    'extra_buttons': [],
                },
            ],

            'Personajes': [
                {
                    'title': 'Personajes',
                    'img_url': ImageCards.Otaku.CHARACTER,
                    'go_url': None,
                    'view_url': URLS.Otaku.Character.LIST,
                    'add_url': URLS.Otaku.Character.LIST,
                    'text': 'Lista de personajes.',
                    'extra_buttons': [
                        {
                            'url': URLS.Otaku.Load.CHARACTER,
                            'label': 'Cargar personajes de MAL',
                            'icon': 'bi bi-cloud-arrow-down',
                            'show': self.request.user.is_superuser,
                            'btn_class': 'btn-danger'
                        },
                    ],
                },

                {
                    'title': 'Personajes de Anime',
                    'img_url': ImageCards.Otaku.ANIME_CHARACTER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Personajes de Anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Personajes de Manga',
                    'img_url': ImageCards.Otaku.MANGA_CHARACTER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Personajes de Manga.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Apodos Personajes',
                    'img_url': ImageCards.Otaku.CHARACTER_NICKNAME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Apodos Personajes.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia Personajes': [
                {
                    'title': 'Foto Personaje',
                    'img_url': ImageCards.Otaku.CHARACTER_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Fotos de Personajes.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imagenes Personajes',
                    'img_url': ImageCards.Otaku.CHARACTER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de relaciones.',
                    'extra_buttons': [],
                },
            ],

            'Personas': [
                {
                    'title': 'Personas',
                    'img_url': ImageCards.Otaku.PERSON,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Lista de personas. Actores de Voz. Autores. Staff Anime. Staff Manga.',
                    'extra_buttons': [
                        {
                            'url': URLS.Otaku.Load.PERSON,
                            'label': 'Cargar personas de MAL',
                            'icon': 'bi bi-cloud-arrow-down',
                            'show': self.request.user.is_superuser,
                            'btn_class': 'btn-danger'
                        },
                    ],
                },

                {
                    'title': 'Actores de Voz',
                    'img_url': ImageCards.Otaku.VOICE_CHARACTER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Actores de Voz de Personajes de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Personal Anime',
                    'img_url': ImageCards.Otaku.ANIME_STAFF,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Personal de animes.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Autores Mangas',
                    'img_url': ImageCards.Otaku.AUTHOR_MANGA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Autores de Mangas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Apodos Personas',
                    'img_url': ImageCards.Otaku.PERSON_NICKNAME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Apodos Personas.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia Personas': [
                {
                    'title': 'Foto Persona',
                    'img_url': ImageCards.Otaku.PERSON_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Fotos de Personas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imagenes Personas',
                    'img_url': ImageCards.Otaku.PERSON_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de relaciones.',
                    'extra_buttons': [],
                },
            ],

            'Compañias': [
                {
                    'title': 'Productoras',
                    'img_url': ImageCards.Otaku.PRODUCER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de productoras de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Licenciantes',
                    'img_url': ImageCards.Otaku.LICENSOR,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de licenciantes de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Estudios',
                    'img_url': ImageCards.Otaku.STUDIO,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de estudios de anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Serializadoras',
                    'img_url': ImageCards.Otaku.SERIALIZATION,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de serializadoras de manga.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia Anime': [
                {
                    'title': 'Caratulas Animes',
                    'img_url': ImageCards.Otaku.ANIME_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Caratulas de Animes.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imagenes Animes',
                    'img_url': ImageCards.Otaku.ANIME_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de imagenes de Animes.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia Manga': [
                {
                    'title': 'Caratulas Mangas',
                    'img_url': ImageCards.Otaku.MANGA_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Caratulas de Mangas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imagenes Mangas',
                    'img_url': ImageCards.Otaku.MANGA_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de imagenes de manga.',
                    'extra_buttons': [],
                },
            ],

            'Relaciones': [
                {
                    'title': 'Relaciones',
                    'img_url': ImageCards.Otaku.MEDIA_RELATION,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de relaciones.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Relaciones Animes',
                    'img_url': ImageCards.Otaku.MEDIA_RELATION_ANIME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Relaciones Anime con Anime.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Relaciones Mangas',
                    'img_url': ImageCards.Otaku.MEDIA_RELATION_MANGA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestión de Relaciones Anime con Manga.',
                    'extra_buttons': [],
                },
            ],

            'Administración de Datos Anime': [
                {
                    'title': 'Datos Anime',
                    'img_url': ImageCards.Otaku.DATA_ANIME,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Personajes Anime',
                    'img_url': ImageCards.Otaku.DATA_ANIME_CHARACTERS,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Imágenes Anime',
                    'img_url': ImageCards.Otaku.DATA_ANIME_PICTURES,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Personal Anime',
                    'img_url': ImageCards.Otaku.DATA_ANIME_STAFF,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },
            ],

            'Administración de Datos Manga': [
                {
                    'title': 'Datos Manga',
                    'img_url': ImageCards.Otaku.DATA_MANGA,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Personajes Manga',
                    'img_url': ImageCards.Otaku.DATA_MANGA_CHARACTERS,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Imágenes Manga',
                    'img_url': ImageCards.Otaku.DATA_MANGA_PICTURES,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                }
            ],

            'Administración de Datos Personajes': [
                {
                    'title': 'Datos Personajes',
                    'img_url': ImageCards.Otaku.DATA_CHARACTER,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Imágenes Personajes',
                    'img_url': ImageCards.Otaku.DATA_CHARACTER_PICTURES,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                }
            ],

            'Administración de Datos Personas': [
                {
                    'title': 'Datos Personas',
                    'img_url': ImageCards.Otaku.DATA_PERSON,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Imágenes Personas',
                    'img_url': ImageCards.Otaku.DATA_PERSON_PICTURES,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                }
            ],

            'Administración de Datos': [
                {
                    'title': 'URL Imagenes',
                    'img_url': ImageCards.Otaku.DATA_IMAGE_URL,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Temporales Personas',
                    'img_url': ImageCards.Otaku.TEMP_PERSONS,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },

                {
                    'title': 'Datos Temporales Personajes',
                    'img_url': ImageCards.Otaku.TEMP_CHARACTER,
                    'go_url': None,
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': '',
                    'extra_buttons': [],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                }
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


class AnimeListView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Inicio Otaku'


class MangaListView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Inicio Otaku'


class CharacterListView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Inicio Otaku'


class PersonListView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Inicio Otaku'
