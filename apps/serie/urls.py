from django.urls import path, include
from .views.views import HomeView
from .views.create_views import (
    GenreCreateView, SerieCreateView, SerieCastCreateView, SerieImageCreateView, SerieImageExtraCreateView, SerieStaffCreateView,
    RatingCreateView, RoleCreateView, TitleSerieCreateView, TypeCreateView, DistributorCreateView, ProducerCreateView,
    )

from .views.update_views import (
    GenreUpdateView, SerieUpdateView, SerieCastUpdateView, SerieImageUpdateView, SerieImageExtraUpdateView, SerieStaffUpdateView,
    RatingUpdateView, RoleUpdateView, TitleSerieUpdateView, TypeUpdateView, DistributorUpdateView, ProducerUpdateView,
    )

from .views.list_views import (
    GenreListView, SerieListView, SerieCastListView, SerieImageListView, SerieImageExtraListView, SerieStaffListView,
    RatingListView, RoleListView, TitleSerieListView, TypeListView, DistributorListView, ProducerListView,
    )

from .views.detail_views import (
    GenreDetailView, SerieDetailView, SerieCastDetailView, SerieImageDetailView, SerieImageExtraDetailView, SerieStaffDetailView,
    RatingDetailView, RoleDetailView, TitleSerieDetailView, TypeDetailView, DistributorDetailView, ProducerDetailView,
    )

app_name = 'serie_app'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    # apis url
    path('api/', include('apps.serie.api.urls')),

    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('serie/create/', SerieCreateView.as_view(), name='serie_create'),
    path('serie/cast/create/', SerieCastCreateView.as_view(), name='serie_cast_create'),
    path('serie/image/create/', SerieImageCreateView.as_view(), name='serie_image_create'),
    path('serie/image/extra/create/', SerieImageExtraCreateView.as_view(), name='serie_image_extra_create'),
    path('serie/staff/create/', SerieStaffCreateView.as_view(), name='serie_staff_create'),
    path('rating/create/', RatingCreateView.as_view(), name='rating_create'),
    path('role/create/', RoleCreateView.as_view(), name='role_create'),
    path('title/serie/create/', TitleSerieCreateView.as_view(), name='title_serie_create'),
    path('type/create/', TypeCreateView.as_view(), name='type_create'),
    path('distributor/create/', DistributorCreateView.as_view(), name='distributor_create'),
    path('producer/create/', ProducerCreateView.as_view(), name='producer_create'),

    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('serie/update/<int:pk>/', SerieUpdateView.as_view(), name='serie_update'),
    path('serie/cast/update/<int:pk>/', SerieCastUpdateView.as_view(), name='serie_cast_update'),
    path('serie/image/update/<int:pk>/', SerieImageUpdateView.as_view(), name='serie_image_update'),
    path('serie/image/extra/update/<int:pk>/', SerieImageExtraUpdateView.as_view(), name='serie_image_extra_update'),
    path('serie/staff/update/<int:pk>/', SerieStaffUpdateView.as_view(), name='serie_staff_update'),
    path('rating/update/<int:pk>/', RatingUpdateView.as_view(), name='rating_update'),
    path('role/update/<int:pk>/', RoleUpdateView.as_view(), name='role_update'),
    path('title/serie/update/<int:pk>/', TitleSerieUpdateView.as_view(), name='title_serie_update'),
    path('type/update/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
    path('distributor/update/<int:pk>/', DistributorUpdateView.as_view(), name='distributor_update'),
    path('producer/update/<int:pk>', ProducerUpdateView.as_view(), name='producer_update'),

    path('genre/list/', GenreListView.as_view(), name='genre_list'),
    path('serie/list/', SerieListView.as_view(), name='serie_list'),
    path('serie/cast/list/', SerieCastListView.as_view(), name='serie_cast_list'),
    path('serie/image/list/', SerieImageListView.as_view(), name='serie_image_list'),
    path('serie/image/extra/list/', SerieImageExtraListView.as_view(), name='serie_image_extra_list'),
    path('serie/staff/list/', SerieStaffListView.as_view(), name='serie_staff_list'),
    path('rating/list/', RatingListView.as_view(), name='rating_list'),
    path('role/list/', RoleListView.as_view(), name='role_list'),
    path('title/serie/list/', TitleSerieListView.as_view(), name='title_serie_list'),
    path('type/list/', TypeListView.as_view(), name='type_list'),
    path('distributor/list/', DistributorListView.as_view(), name='distributor_list'),
    path('producer/list/', ProducerListView.as_view(), name='producer_list'),

    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('serie/<int:pk>/', SerieDetailView.as_view(), name='serie_detail'),
    path('serie/cast/<int:pk>/', SerieCastDetailView.as_view(), name='serie_cast_detail'),
    path('serie/image/<int:pk>/', SerieImageDetailView.as_view(), name='serie_image_detail'),
    path('serie/image/extra/<int:pk>/', SerieImageExtraDetailView.as_view(), name='serie_image_extra_detail'),
    path('serie/staff/<int:pk>/', SerieStaffDetailView.as_view(), name='serie_staff_detail'),
    path('rating/<int:pk>/', RatingDetailView.as_view(), name='rating_detail'),
    path('role/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('title/serie/<int:pk>/', TitleSerieDetailView.as_view(), name='title_serie_detail'),
    path('type/<int:pk>/', TypeDetailView.as_view(), name='type_detail'),
    path('distributor/<int:pk>/', DistributorDetailView.as_view(), name='distributor_detail'),
    path('producer/<int:pk>/', ProducerDetailView.as_view(), name='producer_detail'),

]
