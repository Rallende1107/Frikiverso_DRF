# Django imports
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Project-level imports - mixins and utilities
from core.utils.constants import Templates, URLS, CSSBackground, ImageCards

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = _('Música')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.MUSIC
        context['title'] = self.title
        context['title'] = self.title
        card_sections = {

            _('Metadatos') :[
                {
                    'title': _('Géneros Musicales'),
                    'img_url': ImageCards.Music.GENRE,
                    'go_url': None,
                    'view_url': URLS.Music.Genre.LIST,
                    'add_url': URLS.Music.Genre.CREATE,
                    'text': _('Gestiona los géneros musicales disponibles en el sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Roles Artistas'),
                    'img_url': ImageCards.Music.ROLE,
                    'go_url': None,
                    'view_url': URLS.Music.Role.LIST,
                    'add_url': URLS.Music.Role.CREATE,
                    'text': _('Define los distintos roles que puede tener un artista (vocalista, guitarrista, productor, etc.).'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Tipos de Álbumes'),
                    'img_url': ImageCards.Music.ALBUM_TYPE,
                    'go_url': None,
                    'view_url': URLS.Music.AlbumType.LIST,
                    'add_url': URLS.Music.AlbumType.CREATE,
                    'text': _('Clasifica los álbumes por tipo: EP, LP, compilación, sencillo, etc.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Tipos de Artistas'),
                    'img_url': ImageCards.Music.ARTIST_TYPE,
                    'go_url': None,
                    'view_url': URLS.Music.ArtistType.LIST,
                    'add_url': URLS.Music.ArtistType.CREATE,
                    'text': _('Define si un artista es solista, banda, dúo, colectivo, etc.'),
                    'extra_buttons': [],
                },
            ],

            _('Artistas') :[
                {
                    'title': _('Artistas'),
                    'img_url': ImageCards.Music.ARTIST,
                    'go_url': None,
                    'view_url': URLS.Music.Artist.LIST,
                    'add_url': URLS.Music.Artist.CREATE,
                    'text': _('Gestiona los artistas registrados en el sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Miembros del Artista'),
                    'img_url': ImageCards.Music.ARTIST_MEMBER,
                    'go_url': None,
                    'view_url': URLS.Music.ArtistMember.LIST,
                    'add_url': URLS.Music.ArtistMember.CREATE,
                    'text': _('Gestiona los miembros que componen un grupo musical.'),
                    'extra_buttons': [],
                },
            ],

            _('Producciones Musicales') :[
                {
                    'title': _('Álbumes'),
                    'img_url': ImageCards.Music.ALBUM,
                    'go_url': None,
                    'view_url': URLS.Music.Album.LIST,
                    'add_url': URLS.Music.Album.CREATE,
                    'text': _('Gestiona los álbumes musicales de los artistas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Canciones'),
                    'img_url': ImageCards.Music.SONG,
                    'go_url': None,
                    'view_url': URLS.Music.Song.LIST,
                    'add_url': URLS.Music.Song.CREATE,
                    'text': _('Gestiona las canciones individuales asociadas a los álbumes o artistas.'),
                    'extra_buttons': [],
                },
            ],

            _('Multimedia') :[
                {
                    'title': _('Imágenes de Álbumes'),
                    'img_url': ImageCards.Music.ALBUM_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Music.AlbumImage.LIST,
                    'add_url': URLS.Music.AlbumImage.CREATE,
                    'text': _('Sube y administra las portadas oficiales de los álbumes.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Álbumes'),
                    'img_url': ImageCards.Music.ALBUM_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Music.AlbumImageExtra.LIST,
                    'add_url': URLS.Music.AlbumImageExtra.CREATE,
                    'text': _('Gestiona imágenes adicionales o promocionales de los álbumes.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes de Artistas'),
                    'img_url': ImageCards.Music.ARTIST_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Music.ArtistImage.LIST,
                    'add_url': URLS.Music.ArtistImage.CREATE,
                    'text': _('Administra las imágenes oficiales de los artistas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes Extra de Artistas'),
                    'img_url': ImageCards.Music.ARTIST_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Music.ArtistImageExtra.LIST,
                    'add_url': URLS.Music.ArtistImageExtra.CREATE,
                    'text': _('Gestiona imágenes adicionales de artistas, como sesiones fotográficas o banners.'),
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
