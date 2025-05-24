from django.urls import path, include
from .views.views import HomeView
from .views.create_views import (CompanyCreateView, CountryCreateView, FormatCreateView, ImageSizeCreateView, LanguageCreateView, PersonCreateView,
    PersonImageCreateView, PersonImageExtraCreateView, PersonNicknameCreateView, QualityCreateView, WebsiteCreateView,
    ContextCreateView, GenreCreateView, RatingCreateView, TypeCreateView, StatusCreateView,
)
from .views.list_views import (CompanyListView, CountryListView, FormatListView, ImageSizeListView, LanguageListView, PersonListView,
    PersonImageListView, PersonImageExtraListView, PersonNicknameListView, QualityListView, WebsiteListView,
    ContextListView, GenreListView, RatingListView, TypeListView, StatusListView,
)
from .views.update_views import (CompanyUpdateView, CountryUpdateView, FormatUpdateView, ImageSizeUpdateView, LanguageUpdateView, PersonUpdateView,
    PersonImageUpdateView, PersonImageExtraUpdateView, PersonNicknameUpdateView, QualityUpdateView, WebsiteUpdateView,
    ContextUpdateView, GenreUpdateView, RatingUpdateView, TypeUpdateView, StatusUpdateView,
)
from .views.detail_views import (CompanyDetailView, CountryDetailView, FormatDetailView, ImageSizeDetailView, LanguageDetailView, PersonDetailView,
    PersonImageDetailView, PersonImageExtraDetailView, PersonNicknameDetailView, QualityDetailView, WebsiteDetailView,
    ContextDetailView, GenreDetailView, RatingDetailView, TypeDetailView, StatusDetailView,
)








# from .views_action import ActionView
from .views.actions_views import ActionView

app_name = 'common_app'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('action/', ActionView.as_view(), name='action'),

    path('company/list/', CompanyListView.as_view(), name='company_list'),
    path('company/create/', CompanyCreateView.as_view(), name='company_create'),
    path('company/update/<int:pk>/', CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),

    path('country/list/', CountryListView.as_view(), name='country_list'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),

    path('format/list/', FormatListView.as_view(), name='format_list'),
    path('format/create/', FormatCreateView.as_view(), name='format_create'),
    path('format/update/<int:pk>/', FormatUpdateView.as_view(), name='format_update'),
    path('format/<int:pk>/', FormatDetailView.as_view(), name='format_detail'),

    path('imagesize/list/', ImageSizeListView.as_view(),   name='image_size_list'),
    path('imagesize/create/', ImageSizeCreateView.as_view(), name='image_size_create'),
    path('imagesize/update/<int:pk>/', ImageSizeUpdateView.as_view(), name='image_size_update'),
    path('imagesize/<int:pk>/', ImageSizeDetailView.as_view(), name='image_size_detail'),

    path('language/list/', LanguageListView.as_view(), name='language_list'),
    path('language/create/', LanguageCreateView.as_view(), name='language_create'),
    path('language/update/<int:pk>/', LanguageUpdateView.as_view(), name='language_update'),
    path('language/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),

    path('person/list/', PersonListView.as_view(), name='person_list'),
    path('person/create/', PersonCreateView.as_view(), name='person_create'),
    path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),

    path('person/image/list/', PersonImageListView.as_view(), name='person_image_list'),
    path('person/image/create/', PersonImageCreateView.as_view(), name='person_image_create'),
    path('person/image/update/<int:pk>/', PersonImageUpdateView.as_view(), name='person_image_update'),
    path('person/image/<int:pk>/', PersonImageDetailView.as_view(), name='person_image_detail'),

    path('person/image/extra/list/', PersonImageExtraListView.as_view(), name='person_image_extra_list'),
    path('person/image/extra/create/', PersonImageExtraCreateView.as_view(), name='person_image_extra_create'),
    path('person/image/extra/update/<int:pk>/', PersonImageExtraUpdateView.as_view(), name='person_image_extra_update'),
    path('person/image/extra/<int:pk>/', PersonImageExtraDetailView.as_view(), name='person_image_extra_detail'),

    path('person/nickname/list/', PersonNicknameListView.as_view(), name='person_nickname_list'),
    path('person/nickname/create/', PersonNicknameCreateView.as_view(), name='person_nickname_create'),
    path('person/nickname/update/<int:pk>/', PersonNicknameUpdateView.as_view(), name='person_nickname_update'),
    path('person/nickname/<int:pk>/', PersonNicknameDetailView.as_view(), name='person_nickname_detail'),

    path('quality/list/', QualityListView.as_view(), name='quality_list'),
    path('quality/create/', QualityCreateView.as_view(), name='quality_create'),
    path('quality/update/<int:pk>/', QualityUpdateView.as_view(), name='quality_update'),
    path('quality/<int:pk>/', QualityDetailView.as_view(), name='quality_detail'),

    path('website/list/', WebsiteListView.as_view(), name='website_list'),
    path('website/create/', WebsiteCreateView.as_view(), name='website_create'),
    path('website/update/<int:pk>/', WebsiteUpdateView.as_view(), name='website_update'),
    path('website/<int:pk>/', WebsiteDetailView.as_view(), name='website_detail'),


    path('context/list/', ContextListView.as_view(), name='context_list'),
    path('context/create/', ContextCreateView.as_view(), name='context_create'),
    path('context/update/<int:pk>/', ContextUpdateView.as_view(), name='context_update'),
    path('context/<int:pk>/', ContextDetailView.as_view(), name='context_detail'),


    path('genre/list/', GenreListView.as_view(), name='genre_list'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),

    path('rating/list/', RatingListView.as_view(), name='rating_list'),
    path('rating/create/', RatingCreateView.as_view(), name='rating_create'),
    path('rating/update/<int:pk>/', RatingUpdateView.as_view(), name='rating_update'),
    path('rating/<int:pk>/', RatingDetailView.as_view(), name='rating_detail'),

    path('type/list/', TypeListView.as_view(), name='type_list'),
    path('type/create/', TypeCreateView.as_view(), name='type_create'),
    path('type/update/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/', TypeDetailView.as_view(), name='type_detail'),

    path('status/list/', StatusListView.as_view(), name='status_list'),
    path('status/create/', StatusCreateView.as_view(), name='status_create'),
    path('status/update/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/', StatusDetailView.as_view(), name='status_detail'),


    # apis url
    path('api/', include('apps.common.api.urls')),
]

