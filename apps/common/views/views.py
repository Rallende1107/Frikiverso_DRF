# Django imports
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = _('General')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.COMMON
        context['title'] = self.title
        card_sections = {

            _('Administración de Usuarios'): [
                {
                    'title': _('Usuarios'),
                    'img_url': ImageCards.Users.USER,
                    'go_url': None,
                    'view_url': URLS.Users.LST,
                    'add_url': URLS.Users.ADD,
                    'text': _('Gestionar usuarios del sistema.'),
                    'extra_buttons': [
                        {
                            'url': URLS.Users.ADD_STAFF,
                            'label': _('Crear usuario del equipo'),
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                        {
                            'url': URLS.Users.ADD_SUPER,
                            'label': _('Crear super usuario'),
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                    ],
                    'show': self.request.user.is_staff or self.request.user.is_superuser,
                },
            ],

            _('Gestión General'): [
                {
                    'title': _('Países'),
                    'img_url': ImageCards.Common.COUNTRY,
                    'go_url': None,
                    'view_url': URLS.Common.Country.LST,
                    'add_url': URLS.Common.Country.ADD,
                    'text': _('Gestionar países del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Formatos'),
                    'img_url': ImageCards.Common.FORMAT,
                    'go_url': None,
                    'view_url': URLS.Common.Format.LST,
                    'add_url': URLS.Common.Format.ADD,
                    'text': _('Gestionar formatos del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Tamaños de imagen'),
                    'img_url': ImageCards.Common.IMAGE_SIZE,
                    'go_url': None,
                    'view_url': URLS.Common.ImageSize.LST,
                    'add_url': URLS.Common.ImageSize.ADD,
                    'text': _('Gestionar tamaños de imagen del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Idiomas'),
                    'img_url': ImageCards.Common.LANGUAGE,
                    'go_url': None,
                    'view_url': URLS.Common.Language.LST,
                    'add_url': URLS.Common.Language.ADD,
                    'text': _('Gestionar Idiomas del sistema.'),
                    'extra_buttons': [],
                },
            ],

            _('Gestión de Personas'): [
                {
                    'title': _('Personas'),
                    'img_url': ImageCards.Common.PERSON,
                    'go_url': None,
                    'view_url': URLS.Common.Person.LST,
                    'add_url': URLS.Common.Person.ADD,
                    'text': _('Gestionar personas del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de personas'),
                    'img_url': ImageCards.Common.PERSON_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Common.PersonImage.LST,
                    'add_url': URLS.Common.PersonImage.ADD,
                    'text': _('Gestionar imágenes de personas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes extra de personas'),
                    'img_url': ImageCards.Common.PERSON_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Common.PersonImageExtra.LST,
                    'add_url': URLS.Common.PersonImageExtra.ADD,
                    'text': _('Gestionar imágenes adicionales de personas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Apodos de personas'),
                    'img_url': ImageCards.Common.PERSON_NICKNAME,
                    'go_url': None,
                    'view_url': URLS.Common.PersonNickname.LST,
                    'add_url': URLS.Common.PersonNickname.ADD,
                    'text': _('Gestionar apodeos de las personas.'),
                    'extra_buttons': [],
                },
            ],

            _('Configuración Adicional'): [
                {
                    'title': _('Calidades'),
                    'img_url': ImageCards.Common.QUALITY,
                    'go_url': None,
                    'view_url': URLS.Common.Quality.LST,
                    'add_url': URLS.Common.Quality.ADD,
                    'text': _('Gestionar calidades del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Sitios web'),
                    'img_url': ImageCards.Common.WEBSITE,
                    'go_url': None,
                    'view_url': URLS.Common.Website.LST,
                    'add_url': URLS.Common.Website.ADD,
                    'text': _('Gestionar sitios web del sistema.'),
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
