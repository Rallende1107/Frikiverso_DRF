# Django imports
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Project-level imports - mixins and utilities
from core.utils.constants import Templates, URLS, CSSBackground, ImageCards

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
                    'view_url': URLS.Users.LIST,
                    'add_url': URLS.Users.CREATE,
                    'text': _('Gestionar usuarios del sistema.'),
                    'extra_buttons': [
                        {
                            'url': URLS.Users.CREATE_STAFF,
                            'label': _('Crear usuario del equipo'),
                            'icon': 'bi bi-plus-circle',
                            'show': self.request.user.is_staff or self.request.user.is_superuser,
                            'btn_class': 'btn-danger',
                        },
                        {
                            'url': URLS.Users.CREATE_SUPER,
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
                    'title': _('Compañias'),
                    'img_url': ImageCards.Common.COMPANY,
                    'go_url': None,
                    'view_url': URLS.Common.Company.LIST,
                    'add_url': URLS.Common.Company.CREATE,
                    'text': _('Gestionar Compañias del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Países'),
                    'img_url': ImageCards.Common.COUNTRY,
                    'go_url': None,
                    'view_url': URLS.Common.Country.LIST,
                    'add_url': URLS.Common.Country.CREATE,
                    'text': _('Gestionar países del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Formatos'),
                    'img_url': ImageCards.Common.FORMAT,
                    'go_url': None,
                    'view_url': URLS.Common.Format.LIST,
                    'add_url': URLS.Common.Format.CREATE,
                    'text': _('Gestionar formatos del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Tamaños de imagen'),
                    'img_url': ImageCards.Common.IMAGE_SIZE,
                    'go_url': None,
                    'view_url': URLS.Common.ImageSize.LIST,
                    'add_url': URLS.Common.ImageSize.CREATE,
                    'text': _('Gestionar tamaños de imagen del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Idiomas'),
                    'img_url': ImageCards.Common.LANGUAGE,
                    'go_url': None,
                    'view_url': URLS.Common.Language.LIST,
                    'add_url': URLS.Common.Language.CREATE,
                    'text': _('Gestionar Idiomas del sistema.'),
                    'extra_buttons': [],
                },
            ],

            _('Gestión de Personas'): [
                {
                    'title': _('Personas'),
                    'img_url': ImageCards.Common.PERSON,
                    'go_url': None,
                    'view_url': URLS.Common.Person.LIST,
                    'add_url': URLS.Common.Person.CREATE,
                    'text': _('Gestionar personas del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de personas'),
                    'img_url': ImageCards.Common.PERSON_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Common.PersonImage.LIST,
                    'add_url': URLS.Common.PersonImage.CREATE,
                    'text': _('Gestionar imágenes de personas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes extra de personas'),
                    'img_url': ImageCards.Common.PERSON_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Common.PersonImageExtra.LIST,
                    'add_url': URLS.Common.PersonImageExtra.CREATE,
                    'text': _('Gestionar imágenes adicionales de personas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Apodos de personas'),
                    'img_url': ImageCards.Common.PERSON_NICKNAME,
                    'go_url': None,
                    'view_url': URLS.Common.PersonNickname.LIST,
                    'add_url': URLS.Common.PersonNickname.CREATE,
                    'text': _('Gestionar apodeos de las personas.'),
                    'extra_buttons': [],
                },
            ],

            _('Configuración Adicional'): [
                {
                    'title': _('Calidades'),
                    'img_url': ImageCards.Common.QUALITY,
                    'go_url': None,
                    'view_url': URLS.Common.Quality.LIST,
                    'add_url': URLS.Common.Quality.CREATE,
                    'text': _('Gestionar calidades del sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Sitios web'),
                    'img_url': ImageCards.Common.WEBSITE,
                    'go_url': None,
                    'view_url': URLS.Common.Website.LIST,
                    'add_url': URLS.Common.Website.CREATE,
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
