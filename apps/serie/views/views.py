# Django imports
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Project-level imports - mixins and utilities
from core.utils.constants import Templates, URLS, CSSBackground, ImageCards

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
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
                    'view_url': URLS.Serie.Genre.LIST,
                    'add_url': URLS.Serie.Genre.CREATE,
                    'text': 'Gestiona los géneros disponibles para las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Tipos de Series',
                    'img_url': ImageCards.Serie.TYPE,
                    'go_url': None,
                    'view_url': URLS.Serie.Type.LIST,
                    'add_url': URLS.Serie.Type.CREATE,
                    'text': 'Define los diferentes tipos o formatos de series (animación, drama, documental, etc.).',
                    'extra_buttons': [],
                },

                {
                    'title': 'Clasificaciones de Series',
                    'img_url': ImageCards.Serie.RATING,
                    'go_url': None,
                    'view_url': URLS.Serie.Rating.LIST,
                    'add_url': URLS.Serie.Rating.CREATE,
                    'text': 'Gestiona las clasificaciones o ratings de contenido para las series.',
                    'extra_buttons': [],
                },
            ],

            'Contenido': [
                {
                    'title': 'Series',
                    'img_url': ImageCards.Serie.SERIE,
                    'go_url': None,
                    'view_url': URLS.Serie.Serie.LIST,
                    'add_url': URLS.Serie.Serie.CREATE,
                    'text': 'Gestiona las series registradas en el sistema.',
                    'extra_buttons': [],
                },
                {
                    'title': 'Títulos de Series',
                    'img_url': ImageCards.Serie.TITLE_SERIE,
                    'go_url': None,
                    'view_url': URLS.Serie.TitleSerie.LIST,
                    'add_url': URLS.Serie.TitleSerie.CREATE,
                    'text': 'Gestiona los distintos títulos o traducciones de las series.',
                    'extra_buttons': [],
                },

            ],

            'Personal y Reparto': [
                {
                    'title': 'Roles de Series',
                    'img_url': ImageCards.Serie.ROLE,
                    'go_url': None,
                    'view_url': URLS.Serie.Role.LIST,
                    'add_url': URLS.Serie.Role.CREATE,
                    'text': 'Define los roles del personal y reparto (director, guionista, actor, etc.).',
                    'extra_buttons': [],
                },

                {
                    'title': 'Personal de Series',
                    'img_url': ImageCards.Serie.SERIE_STAFF,
                    'go_url': None,
                    'view_url': URLS.Serie.SerieStaff.LIST,
                    'add_url': URLS.Serie.SerieStaff.CREATE,
                    'text': 'Gestiona el personal que trabaja en la producción de las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Reparto de Series',
                    'img_url': ImageCards.Serie.SERIE_CAST,
                    'go_url': None,
                    'view_url': URLS.Serie.SerieCast.LIST,
                    'add_url': URLS.Serie.SerieCast.CREATE,
                    'text': 'Gestiona el reparto de actores y sus personajes en las series.',
                    'extra_buttons': [],
                },
            ],
            'Organizaciones' :[
                {
                    'title': 'Productoras',
                    'img_url': ImageCards.Serie.PRODUCER,
                    'go_url': None,
                    'view_url': URLS.Serie.Producer.LIST,
                    'add_url': URLS.Serie.Producer.CREATE,
                    'text': 'Gestiona las compañías con rol de producción cinematográfica.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Distribuidoras',
                    'img_url': ImageCards.Serie.DISTRIBUTOR,
                    'go_url': None,
                    'view_url': URLS.Serie.Distributor.LIST,
                    'add_url': URLS.Serie.Distributor.CREATE,
                    'text': 'Gestiona las compañías con rol de distribución cinematográfica.',
                    'extra_buttons': [],
                },
            ],
            'Multimedia': [
                {
                    'title': 'Imágenes de Series',
                    'img_url': ImageCards.Serie.SERIE_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Serie.SerieImage.LIST,
                    'add_url': URLS.Serie.SerieImage.CREATE,
                    'text': 'Gestiona las imágenes oficiales y portadas de las series.',
                    'extra_buttons': [],
                },

                {
                    'title': 'Imágenes Extra de Series',
                    'img_url': ImageCards.Serie.SERIE_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Serie.SerieImageExtra.LIST,
                    'add_url': URLS.Serie.SerieImageExtra.CREATE,
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
        context['labels'] = {
            'go': _('Ir'),
            'view_all': _('Todos'),
            'add': _('Añadir'),
        }
        return context
