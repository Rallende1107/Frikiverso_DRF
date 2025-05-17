from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap


class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Peliculas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.MOVIE
        context['title'] = self.title
        card_sections = {

            'Metadatos' :[
                {
                    'title': 'Géneros de Películas',
                    'img_url': ImageCards.Movie.GENRE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los géneros asignados a las películas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos de Películas',
                    'img_url': ImageCards.Movie.TYPE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los diferentes tipos o categorías de películas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Clasificaciones de Películas',
                    'img_url': ImageCards.Movie.RATING,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las clasificaciones de edad y contenido de las películas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Compañías de Películas',
                    'img_url': ImageCards.Movie.COMPANY,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las compañías productoras o distribuidoras.',
                    'extra_buttons': [],
                },
            ],

            'Contenido' :[
                {
                    'title': 'Películas',
                    'img_url': ImageCards.Movie.MOVIE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las películas registradas en el sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Títulos de Películas',
                    'img_url': ImageCards.Movie.TITLE_MOVIE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los títulos y traducciones de las películas.',
                    'extra_buttons': [],
                }
            ],

            'Personal y Reparto' :[
                {
                    'title': 'Roles de Películas',
                    'img_url': ImageCards.Movie.ROLE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los diferentes roles dentro de las películas (director, guionista, etc.).',
                    'extra_buttons': [],
                },

                {
                    'title': 'Personal de Películas',
                    'img_url': ImageCards.Movie.MOVIE_STAFF,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona el personal involucrado en la producción de las películas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Reparto de Películas',
                    'img_url': ImageCards.Movie.MOVIE_CAST,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona el reparto de actores y actrices en las películas.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia' :[
                {
                    'title': 'Imágenes de Películas',
                    'img_url': ImageCards.Movie.MOVIE_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes principales asociadas a las películas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Películas',
                    'img_url': ImageCards.Movie.MOVIE_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales o promocionales de las películas.',
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

