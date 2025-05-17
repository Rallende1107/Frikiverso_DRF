from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap


class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = 'Musica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.MUSIC
        context['title'] = self.title
        context['title'] = self.title
        card_sections = {

            'Metadatos' :[
                {
                    'title': 'Géneros Musicales',
                    'img_url': ImageCards.Music.GENRE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los géneros musicales disponibles en el sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Roles Artistas',
                    'img_url': ImageCards.Music.ROLE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Define los distintos roles que puede tener un artista (vocalista, guitarrista, productor, etc.).',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos de Álbumes',
                    'img_url': ImageCards.Music.ALBUM_TYPE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Clasifica los álbumes por tipo: EP, LP, compilación, sencillo, etc.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos de Artistas',
                    'img_url': ImageCards.Music.ARTIST_TYPE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Define si un artista es solista, banda, dúo, colectivo, etc.',
                    'extra_buttons': [],
                },
            ],

            'Artistas' :[
                {
                    'title': 'Artistas',
                    'img_url': ImageCards.Music.ARTIST,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los artistas registrados en el sistema.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Miembros del Artista',
                    'img_url': ImageCards.Music.ARTIST_MEMBER,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los miembros que componen un grupo musical.',
                    'extra_buttons': [],
                },
            ],

            'Producciones Musicales' :[
                {
                    'title': 'Álbumes',
                    'img_url': ImageCards.Music.ALBUM,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los álbumes musicales de los artistas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Canciones',
                    'img_url': ImageCards.Music.SONG,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las canciones individuales asociadas a los álbumes o artistas.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia' :[
                {
                    'title': 'Imágenes de Álbumes',
                    'img_url': ImageCards.Music.ALBUM_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Sube y administra las portadas oficiales de los álbumes.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Álbumes',
                    'img_url': ImageCards.Music.ALBUM_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales o promocionales de los álbumes.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes de Artistas',
                    'img_url': ImageCards.Music.ARTIST_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Administra las imágenes oficiales de los artistas.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Artistas',
                    'img_url': ImageCards.Music.ARTIST_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona imágenes adicionales de artistas, como sesiones fotográficas o banners.',
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



