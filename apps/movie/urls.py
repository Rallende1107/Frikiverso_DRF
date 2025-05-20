from django.urls import path, include
from .views.views import HomeView
from .views.create_views import (
    GenreCreateView, MovieCreateView, MovieCastCreateView, MovieImageCreateView, MovieImageExtraCreateView, MovieStaffCreateView,
    RatingCreateView, RoleCreateView, TitleMovieCreateView, TypeCreateView, DistributorCreateView, ProducerCreateView,
    )

from .views.update_views import (
    GenreUpdateView, MovieUpdateView, MovieCastUpdateView, MovieImageUpdateView, MovieImageExtraUpdateView, MovieStaffUpdateView,
    RatingUpdateView, RoleUpdateView, TitleMovieUpdateView, TypeUpdateView, DistributorUpdateView, ProducerUpdateView,
    )

from .views.list_views import (
    GenreListView, MovieListView, MovieCastListView, MovieImageListView, MovieImageExtraListView, MovieStaffListView,
    RatingListView, RoleListView, TitleMovieListView, TypeListView, DistributorListView, ProducerListView,
    )

from .views.detail_views import (
    GenreDetailView, MovieDetailView, MovieCastDetailView, MovieImageDetailView, MovieImageExtraDetailView, MovieStaffDetailView,
    RatingDetailView, RoleDetailView, TitleMovieDetailView, TypeDetailView, DistributorDetailView, ProducerDetailView,
    )

app_name = 'movie_app'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    # apis url
    path('api/', include('apps.movie.api.urls')),

    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/cast/create/', MovieCastCreateView.as_view(), name='movie_cast_create'),
    path('movie/image/create/', MovieImageCreateView.as_view(), name='movie_image_create'),
    path('movie/image/extra/create/', MovieImageExtraCreateView.as_view(), name='movie_image_extra_create'),
    path('movie/staff/create/', MovieStaffCreateView.as_view(), name='movie_staff_create'),
    path('rating/create/', RatingCreateView.as_view(), name='rating_create'),
    path('role/create/', RoleCreateView.as_view(), name='role_create'),
    path('title/movie/create/', TitleMovieCreateView.as_view(), name='title_movie_create'),
    path('type/create/', TypeCreateView.as_view(), name='type_create'),
    path('distributor/create/', DistributorCreateView.as_view(), name='distributor_create'),
    path('producer/create/', ProducerCreateView.as_view(), name='producer_create'),

    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/cast/update/<int:pk>/', MovieCastUpdateView.as_view(), name='movie_cast_update'),
    path('movie/image/update/<int:pk>/', MovieImageUpdateView.as_view(), name='movie_image_update'),
    path('movie/image/extra/update/<int:pk>/', MovieImageExtraUpdateView.as_view(), name='movie_image_extra_update'),
    path('movie/staff/update/<int:pk>/', MovieStaffUpdateView.as_view(), name='movie_staff_update'),
    path('rating/update/<int:pk>/', RatingUpdateView.as_view(), name='rating_update'),
    path('role/update/<int:pk>/', RoleUpdateView.as_view(), name='role_update'),
    path('title/movie/update/<int:pk>/', TitleMovieUpdateView.as_view(), name='title_movie_update'),
    path('type/update/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
    path('distributor/update/<int:pk>/', DistributorUpdateView.as_view(), name='distributor_update'),
    path('producer/update/<int:pk>', ProducerUpdateView.as_view(), name='producer_update'),

    path('genre/list/', GenreListView.as_view(), name='genre_list'),
    path('movie/list/', MovieListView.as_view(), name='movie_list'),
    path('movie/cast/list/', MovieCastListView.as_view(), name='movie_cast_list'),
    path('movie/image/list/', MovieImageListView.as_view(), name='movie_image_list'),
    path('movie/image/extra/list/', MovieImageExtraListView.as_view(), name='movie_image_extra_list'),
    path('movie/staff/list/', MovieStaffListView.as_view(), name='movie_staff_list'),
    path('rating/list/', RatingListView.as_view(), name='rating_list'),
    path('role/list/', RoleListView.as_view(), name='role_list'),
    path('title/movie/list/', TitleMovieListView.as_view(), name='title_movie_list'),
    path('type/list/', TypeListView.as_view(), name='type_list'),
    path('distributor/list/', DistributorListView.as_view(), name='distributor_list'),
    path('producer/list/', ProducerListView.as_view(), name='producer_list'),

    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/cast/<int:pk>/', MovieCastDetailView.as_view(), name='movie_cast_detail'),
    path('movie/image/<int:pk>/', MovieImageDetailView.as_view(), name='movie_image_detail'),
    path('movie/image/extra/<int:pk>/', MovieImageExtraDetailView.as_view(), name='movie_image_extra_detail'),
    path('movie/staff/<int:pk>/', MovieStaffDetailView.as_view(), name='movie_staff_detail'),
    path('rating/<int:pk>/', RatingDetailView.as_view(), name='rating_detail'),
    path('role/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('title/movie/<int:pk>/', TitleMovieDetailView.as_view(), name='title_movie_detail'),
    path('type/<int:pk>/', TypeDetailView.as_view(), name='type_detail'),
    path('distributor/<int:pk>/', DistributorDetailView.as_view(), name='distributor_detail'),
    path('producer/<int:pk>/', ProducerDetailView.as_view(), name='producer_detail'),

]
