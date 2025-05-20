# Django imports
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = _('Juegos Renpy')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.RENPY
        context['title'] = self.title
        card_sections = {

            _('Gestión Principal'): [
                {
                    'title': _('Juegos'),
                    'img_url': ImageCards.Renpy.GAME,
                    'go_url': None,
                    'view_url': URLS.Renpy.Game.LIST,
                    'add_url': URLS.Renpy.Game.CREATE,
                    'text': _('Gestiona los juegos disponibles en el sistema.'),
                    'extra_buttons': [
                        {
                            'url': URLS.Renpy.Game.LOAD,
                            'label': _('Cargar Juegos de F95Zone'),
                            'icon': 'bi bi-cloud-arrow-up',
                            'show': self.request.user.is_superuser,
                            'btn_class': 'btn-danger'
                        }
                    ],
                },

                {
                    'title': _('Títulos de Juegos'),
                    'img_url': ImageCards.Renpy.TITLE_GAME,
                    'go_url': None,
                    'view_url': URLS.Renpy.TitleGame.LIST,
                    'add_url': URLS.Renpy.TitleGame.CREATE,
                    'text': _('Gestiona los diferentes títulos y traducciones de los juegos.'),
                    'extra_buttons': [],
                },
            ],

            _('Metadatos'): [
                {
                    'title': _('Géneros Juegos'),
                    'img_url': ImageCards.Renpy.GENRE,
                    'go_url': None,
                    'view_url': URLS.Renpy.Genre.LIST,
                    'add_url': URLS.Renpy.Genre.CREATE,
                    'text': _('Gestiona los géneros asignados a los juegos del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Motores de Desarrollo'),
                    'img_url': ImageCards.Renpy.GAME_ENGINE,
                    'go_url': None,
                    'view_url': URLS.Renpy.GameEngine.LIST,
                    'add_url': URLS.Renpy.GameEngine.CREATE,
                    'text': _('Gestiona los motores de desarrollo utilizados para los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Plataformas'),
                    'img_url': ImageCards.Renpy.PLATFORM,
                    'go_url': None,
                    'view_url': URLS.Renpy.Platform.LIST,
                    'add_url': URLS.Renpy.Platform.CREATE,
                    'text': _('Gestiona las plataformas para las que están disponibles los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Prefijos'),
                    'img_url': ImageCards.Renpy.PREFIX,
                    'go_url': None,
                    'view_url': URLS.Renpy.Prefix.LIST,
                    'add_url': URLS.Renpy.Prefix.CREATE,
                    'text': _('Gestiona los prefijos utilizados para identificar juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Censura'),
                    'img_url': ImageCards.Renpy.CENSORSHIP,
                    'go_url': None,
                    'view_url': URLS.Renpy.Censorship.LIST,
                    'add_url': URLS.Renpy.Censorship.CREATE,
                    'text': _('Gestiona los niveles o tipos de censura aplicados a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Estados'),
                    'img_url': ImageCards.Renpy.STATUS,
                    'go_url': None,
                    'view_url': URLS.Renpy.Status.LIST,
                    'add_url': URLS.Renpy.Status.CREATE,
                    'text': _('Gestiona los estados en que pueden encontrarse los juegos.'),
                    'extra_buttons': [],
                },
            ],

            _('Entidades'): [
                {
                    'title': _('Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER,
                    'go_url': None,
                    'view_url': URLS.Renpy.Developer.LIST,
                    'add_url': URLS.Renpy.Developer.CREATE,
                    'text': _('Gestiona los desarrolladores asociados a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR,
                    'go_url': None,
                    'view_url': URLS.Renpy.Translator.LIST,
                    'add_url': URLS.Renpy.Translator.CREATE,
                    'text': _('Gestiona los traductores responsables de las versiones localizadas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER,
                    'go_url': None,
                    'view_url': URLS.Renpy.Publisher.LIST,
                    'add_url': URLS.Renpy.Publisher.CREATE,
                    'text': _('Gestiona los editores o publicadores de los juegos.'),
                    'extra_buttons': [],
                },
            ],

            _('Webs Oficiales'): [
                {
                    'title': _('Webs Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER_LINK,
                    'go_url': None,
                    'view_url': URLS.Renpy.DeveloperLink.LIST,
                    'add_url': URLS.Renpy.DeveloperLink.CREATE,
                    'text': _('Gestiona los enlaces oficiales de los desarrolladores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Webs Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR_LINK,
                    'go_url': None,
                    'view_url': URLS.Renpy.TranslatorLink.LIST,
                    'add_url': URLS.Renpy.TranslatorLink.CREATE,
                    'text': _('Gestiona los enlaces oficiales de los traductores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Webs Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER_LINK,
                    'go_url': None,
                    'view_url': URLS.Renpy.PublisherLink.LIST,
                    'add_url': URLS.Renpy.PublisherLink.CREATE,
                    'text': _('Gestiona los enlaces oficiales de los editores.'),
                    'extra_buttons': [],
                },
            ],

            _('Multimedia'): [
                {
                    'title': _('Imágenes de Juegos'),
                    'img_url': ImageCards.Renpy.GAME_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.GameImage.LIST,
                    'add_url': URLS.Renpy.GameImage.CREATE,
                    'text': _('Gestiona las imágenes principales asociadas a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Juegos'),
                    'img_url': ImageCards.Renpy.GAME_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.GameImageExtra.LIST,
                    'add_url': URLS.Renpy.GameImageExtra.CREATE,
                    'text': _('Gestiona las imágenes principales asociadas a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.DeveloperImage.LIST,
                    'add_url': URLS.Renpy.DeveloperImage.CREATE,
                    'text': _('Gestiona las imágenes oficiales de los desarrolladores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.DeveloperImageExtra.LIST,
                    'add_url': URLS.Renpy.DeveloperImageExtra.CREATE,
                    'text': _('Gestiona imágenes adicionales de los desarrolladores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.TranslatorImage.LIST,
                    'add_url': URLS.Renpy.TranslatorImage.CREATE,
                    'text': _('Gestiona las imágenes oficiales de los traductores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.TranslatorImageExtra.LIST,
                    'add_url': URLS.Renpy.TranslatorImageExtra.CREATE,
                    'text': _('Gestiona imágenes adicionales de los traductores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.PublisherImage.LIST,
                    'add_url': URLS.Renpy.PublisherImage.CREATE,
                    'text': _('Gestiona las imágenes oficiales de los editores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.PublisherImageExtra.LIST,
                    'add_url': URLS.Renpy.PublisherImageExtra.CREATE,
                    'text': _('Gestiona imágenes adicionales de los editores.'),
                    'extra_buttons': [],
                },

            ],

            _('Sección Administrativa'): [
                {
                    'title': _('Datos Juegos'),
                    'img_url': ImageCards.Renpy.DATA_GAME,
                    'go_url': None,
                    'view_url': None,
                    'add_url': None,
                    'text': _('Gestiona los datos técnicos y portadas de los juegos.'),
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
        context['labels'] = {
            'go': _('Ir'),
            'view_all': _('Todos'),
            'add': _('Añadir'),
        }

        return context
