from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap


class HomeView(TemplateView):
    template_name = Templates.HOME
    title = 'Serie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.SERIE
        context['title'] = self.title
        card_sections = {

            'Metadatos': [
                {
                    'title': 'Géneros de Series',
                    'img_url': ImageCards.Serie.GENRE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los géneros disponibles para las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos de Series',
                    'img_url': ImageCards.Serie.TYPE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Define los diferentes tipos o formatos de series (animación, drama, documental, etc.).',
                    'extra_buttons': [],
                },

                {
                    'title': 'Clasificaciones de Series',
                    'img_url': ImageCards.Serie.RATING,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las clasificaciones o ratings de contenido para las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Compañías de Series',
                    'img_url': ImageCards.Serie.COMPANY,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Administra las compañías productoras o distribuidoras de las series.',
                    'extra_buttons': [],
                },
            ],

            'Contenido': [
                {
                    'title': 'Series',
                    'img_url': ImageCards.Serie.SERIE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las series registradas en el sistema.',
                    'extra_buttons': [],
                },
                {
                    'title': 'Títulos de Series',
                    'img_url': ImageCards.Serie.TITLE_SERIE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona los distintos títulos o traducciones de las series.',
                    'extra_buttons': [],
                },

            ],

            'Personal y Reparto': [
                {
                    'title': 'Roles de Series',
                    'img_url': ImageCards.Serie.ROLE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Define los roles del personal y reparto (director, guionista, actor, etc.).',
                    'extra_buttons': [],
                },

                {
                    'title': 'Personal de Series',
                    'img_url': ImageCards.Serie.SERIE_STAFF,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona el personal que trabaja en la producción de las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Reparto de Series',
                    'img_url': ImageCards.Serie.SERIE_CAST,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona el reparto de actores y sus personajes en las series.',
                    'extra_buttons': [],
                },
            ],

            'Multimedia': [
                {
                    'title': 'Imágenes de Series',
                    'img_url': ImageCards.Serie.SERIE_IMAGE,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Gestiona las imágenes oficiales y portadas de las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Series',
                    'img_url': ImageCards.Serie.SERIE_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': 'Administra imágenes adicionales o promocionales relacionadas con las series.',
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
