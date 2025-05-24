# Django imports
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

# Project-level imports - mixins and utilities
from core.utils.constants import Templates, URLS, CSSBackground, ImageCards

# Create your views here.
############################################################################################################################################    HomeView
class HomeView(TemplateView):
    template_name = Templates.Home.HOME
    title = _('Películas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Home.MOVIE
        context['title'] = self.title
        card_sections = {

            _('Metadatos') :[
                {
                    'title': _('Géneros de Películas'),
                    'img_url': ImageCards.Movie.GENRE,
                    'go_url': None,
                    'view_url': URLS.Movie.Genre.LIST,
                    'add_url': URLS.Movie.Genre.CREATE,
                    'text': _('Gestiona los géneros asignados a las películas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Tipos de Películas'),
                    'img_url': ImageCards.Movie.TYPE,
                    'go_url': None,
                    'view_url': URLS.Movie.Type.LIST,
                    'add_url': URLS.Movie.Type.CREATE,
                    'text': _('Gestiona los diferentes tipos o categorías de películas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Clasificaciones de Películas'),
                    'img_url': ImageCards.Movie.RATING,
                    'go_url': None,
                    'view_url': URLS.Movie.Rating.LIST,
                    'add_url': URLS.Movie.Rating.CREATE,
                    'text': _('Gestiona las clasificaciones de edad y contenido de las películas.'),
                    'extra_buttons': [],
                },

            ],

            _('Contenido') :[
                {
                    'title': _('Películas'),
                    'img_url': ImageCards.Movie.MOVIE,
                    'go_url': None,
                    'view_url': URLS.Movie.Movie.LIST,
                    'add_url': URLS.Movie.Movie.CREATE,
                    'text': _('Gestiona las películas registradas en el sistema.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Títulos de Películas'),
                    'img_url': ImageCards.Movie.TITLE_MOVIE,
                    'go_url': None,
                    'view_url': URLS.Movie.TitleMovie.LIST,
                    'add_url': URLS.Movie.TitleMovie.CREATE,
                    'text': _('Gestiona los títulos y traducciones de las películas.'),
                    'extra_buttons': [],
                }
            ],

            _('Personal y Reparto') :[
                {
                    'title': _('Roles de Películas'),
                    'img_url': ImageCards.Movie.ROLE,
                    'go_url': None,
                    'view_url': URLS.Movie.Role.LIST,
                    'add_url': URLS.Movie.Role.CREATE,
                    'text': _('Gestiona los diferentes roles dentro de las películas (director, guionista, etc.).'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Personal de Películas'),
                    'img_url': ImageCards.Movie.MOVIE_STAFF,
                    'go_url': None,
                    'view_url': URLS.Movie.MovieStaff.LIST,
                    'add_url': URLS.Movie.MovieStaff.CREATE,
                    'text': _('Gestiona el personal involucrado en la producción de las películas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Reparto de Películas'),
                    'img_url': ImageCards.Movie.MOVIE_CAST,
                    'go_url': None,
                    'view_url': URLS.Movie.MovieCast.LIST,
                    'add_url': URLS.Movie.MovieCast.CREATE,
                    'text': _('Gestiona el reparto de actores y actrices en las películas.'),
                    'extra_buttons': [],
                },
            ],

            _('Organizaciones') :[
                {
                    'title': _('Productoras'),
                    'img_url': ImageCards.Movie.PRODUCER,
                    'go_url': None,
                    'view_url': URLS.Movie.Producer.LIST,
                    'add_url': URLS.Movie.Producer.CREATE,
                    'text': _('Gestiona las compañías con rol de producción cinematográfica.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Distribuidoras'),
                    'img_url': ImageCards.Movie.DISTRIBUTOR,
                    'go_url': None,
                    'view_url': URLS.Movie.Distributor.LIST,
                    'add_url': URLS.Movie.Distributor.CREATE,
                    'text': _('Gestiona las compañías con rol de distribución cinematográfica.'),
                    'extra_buttons': [],
                },
            ],

            _('Multimedia') :[
                {
                    'title': _('Imágenes de Películas'),
                    'img_url': ImageCards.Movie.MOVIE_IMAGE,
                    'go_url': None,
                    'view_url': URLS.Movie.MovieImage.LIST,
                    'add_url': URLS.Movie.MovieImage.CREATE,
                    'text': _('Gestiona las imágenes principales asociadas a las películas.'),
                    'extra_buttons': [],
                },

                {
                    'title': _('Imágenes adicionales de Películas'),
                    'img_url': ImageCards.Movie.MOVIE_IMAGE_EXTRA,
                    'go_url': None,
                    'view_url': URLS.Movie.MovieImageExtra.LIST,
                    'add_url': URLS.Movie.MovieImageExtra.CREATE,
                    'text': _('Gestiona imágenes adicionales o promocionales de las películas.'),
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


"""
from django.views.generic import ListView
from movie.models import Genre
from common.models import ContextApp

class GenreByContextListView(ListView):
    model = Genre
    template_name = 'movie/genre_list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        context_slug = self.kwargs.get('slug')  # lo tomas desde la URL
        return Genre.objects.filter(contexts__slug=context_slug).distinct()


"""
