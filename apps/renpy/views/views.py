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
                    'view_url': URLS.Renpy.Game.LST,
                    'add_url': URLS.Renpy.Game.ADD,
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
                    'view_url': URLS.Renpy.TitleGame.LST,
                    'add_url': URLS.Renpy.TitleGame.ADD,
                    'text': _('Gestiona los diferentes títulos y traducciones de los juegos.'),
                    'extra_buttons': [],
                },
            ],

            _('Metadatos'): [
                {
                    'title': _('Géneros Juegos'),
                    'img_url': ImageCards.Renpy.GENRE,
                    'go_url': None,
                    'view_url': URLS.Renpy.Genre.LST,
                    'add_url': URLS.Renpy.Genre.ADD,
                    'text': _('Gestiona los géneros asignados a los juegos del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Motores de Desarrollo'),
                    'img_url': ImageCards.Renpy.GAME_ENGINE,
                    'go_url': None,
                    'view_url': URLS.Renpy.GameEngine.LST,
                    'add_url': URLS.Renpy.GameEngine.ADD,
                    'text': _('Gestiona los motores de desarrollo utilizados para los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Plataformas'),
                    'img_url': ImageCards.Renpy.PLATFORM,
                    'go_url': None,
                    'view_url': URLS.Renpy.Platform.LST,
                    'add_url': URLS.Renpy.Platform.ADD,
                    'text': _('Gestiona las plataformas para las que están disponibles los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Prefijos'),
                    'img_url': ImageCards.Renpy.PREFIX,
                    'go_url': None,
                    'view_url': URLS.Renpy.Prefix.LST,
                    'add_url': URLS.Renpy.Prefix.ADD,
                    'text': _('Gestiona los prefijos utilizados para identificar juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Censura'),
                    'img_url': ImageCards.Renpy.CENSORSHIP,
                    'go_url': None,
                    'view_url': URLS.Renpy.Censorship.LST,
                    'add_url': URLS.Renpy.Censorship.ADD,
                    'text': _('Gestiona los niveles o tipos de censura aplicados a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Estados'),
                    'img_url': ImageCards.Renpy.STATUS,
                    'go_url': None,
                    'view_url': URLS.Renpy.Status.LST,
                    'add_url': URLS.Renpy.Status.ADD,
                    'text': _('Gestiona los estados en que pueden encontrarse los juegos.'),
                    'extra_buttons': [],
                },
            ],

            _('Entidades'): [
                {
                    'title': _('Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER,
                    'go_url': None,
                    'view_url': URLS.Renpy.Developer.LST,
                    'add_url': URLS.Renpy.Developer.ADD,
                    'text': _('Gestiona los desarrolladores asociados a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR,
                    'go_url': None,
                    'view_url': URLS.Renpy.Translator.LST,
                    'add_url': URLS.Renpy.Translator.ADD,
                    'text': _('Gestiona los traductores responsables de las versiones localizadas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER,
                    'go_url': None,
                    'view_url': URLS.Renpy.Publisher.LST,
                    'add_url': URLS.Renpy.Publisher.ADD,
                    'text': _('Gestiona los editores o publicadores de los juegos.'),
                    'extra_buttons': [],
                },
            ],

            _('Webs Oficiales'): [
                {
                    'title': _('Webs Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER_LINK,
                    'go_url': None,
                    'view_url': URLS.Renpy.DeveloperLink.LST,
                    'add_url': URLS.Renpy.DeveloperLink.ADD,
                    'text': _('Gestiona los enlaces oficiales de los desarrolladores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Webs Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR_LINK,
                    'go_url': None,
                    'view_url': URLS.Renpy.TranslatorLink.LST,
                    'add_url': URLS.Renpy.TranslatorLink.ADD,
                    'text': _('Gestiona los enlaces oficiales de los traductores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Webs Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER_LINK,
                    'go_url': None,
                    'view_url': URLS.Renpy.PublisherLink.LST,
                    'add_url': URLS.Renpy.PublisherLink.ADD,
                    'text': _('Gestiona los enlaces oficiales de los editores.'),
                    'extra_buttons': [],
                },
            ],

            _('Multimedia'): [
                {
                    'title': _('Imágenes de Juegos'),
                    'img_url': ImageCards.Renpy.GAME_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.GameImage.LST,
                    'add_url': URLS.Renpy.GameImage.ADD,
                    'text': _('Gestiona las imágenes principales asociadas a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Juegos'),
                    'img_url': ImageCards.Renpy.GAME_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.GameImageExtra.LST,
                    'add_url': URLS.Renpy.GameImageExtra.ADD,
                    'text': _('Gestiona las imágenes principales asociadas a los juegos.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.DeveloperImage.LST,
                    'add_url': URLS.Renpy.DeveloperImage.ADD,
                    'text': _('Gestiona las imágenes oficiales de los desarrolladores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Desarrolladores'),
                    'img_url': ImageCards.Renpy.DEVELOPER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.DeveloperImageExtra.LST,
                    'add_url': URLS.Renpy.DeveloperImageExtra.ADD,
                    'text': _('Gestiona imágenes adicionales de los desarrolladores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.TranslatorImage.LST,
                    'add_url': URLS.Renpy.TranslatorImage.ADD,
                    'text': _('Gestiona las imágenes oficiales de los traductores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Traductores'),
                    'img_url': ImageCards.Renpy.TRANSLATOR_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.TranslatorImageExtra.LST,
                    'add_url': URLS.Renpy.TranslatorImageExtra.ADD,
                    'text': _('Gestiona imágenes adicionales de los traductores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Renpy.PublisherImage.LST,
                    'add_url': URLS.Renpy.PublisherImage.ADD,
                    'text': _('Gestiona las imágenes oficiales de los editores.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Editores'),
                    'img_url': ImageCards.Renpy.PUBLISHER_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Renpy.PublisherImageExtra.LST,
                    'add_url': URLS.Renpy.PublisherImageExtra.ADD,
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
