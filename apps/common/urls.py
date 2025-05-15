from django.urls import path, include
from .views import HomeView

from .views_action import ActionView
from .views import (
    CountryListView, CountryCreateView, CountryUpdateView, CountryDetailView,
    FormatListView, FormatCreateView, FormatUpdateView, FormatDetailView,

    # ImageSizeListView, ImageSizeCreateView, ImageSizeUpdateView, ImageSizeDetailView,
    LanguageListView, LanguageCreateView, LanguageUpdateView, LanguageDetailView,
    # PersonListView, PersonCreateView, PersonUpdateView, PersonDetailView,
    # PersonImageListView, PersonImageCreateView, PersonImageUpdateView, PersonImageDetailView,
    # PersonImageExtraListView, PersonImageExtraCreateView, PersonImageExtraUpdateView, PersonImageExtraDetailView,
    # PersonNicknameListView, PersonNicknameCreateView, PersonNicknameUpdateView, PersonNicknameDetailView,
    # QualityListView, QualityCreateView, QualityUpdateView, QualityDetailView,
    # WebsiteListView, WebsiteCreateView, WebsiteUpdateView, WebsiteDetailView,
)
app_name = 'common_app'




urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('action/', ActionView.as_view(), name='action'),

    path('country/list/', CountryListView.as_view(), name='country_list'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),

    path('format/list/', FormatListView.as_view(), name='format_list'),
    path('format/create/', FormatCreateView.as_view(), name='format_create'),
    path('format/update/<int:pk>/', FormatUpdateView.as_view(), name='format_update'),
    path('format/<int:pk>/', FormatDetailView.as_view(), name='format_detail'),

    # path('imagesize/list/', ImageSizeListView.as_view(),   name='image_size_list'),
    # path('imagesize/create/', ImageSizeCreateView.as_view(), name='image_size_create'),
    # path('imagesize/update/<int:pk>/', ImageSizeUpdateView.as_view(), name='image_size_update'),
    # path('imagesize/<int:pk>/', ImageSizeDetailView.as_view(), name='image_size_detail'),

    path('language/list/', LanguageListView.as_view(), name='language_list'),
    path('language/create/', LanguageCreateView.as_view(), name='language_create'),
    path('language/update/<int:pk>/', LanguageUpdateView.as_view(), name='language_update'),
    path('language/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),

    # path('person/list/', PersonListView.as_view(), name='person_list'),
    # path('person/create/', PersonCreateView.as_view(), name='person_create'),
    # path('person/update/<int:pk>/', PersonUpdateView.as_view(), name='person_update'),
    # path('person/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),

    # path('person/image/list/', PersonImageListView.as_view(), name='person_image_list'),
    # path('person/image/create/', PersonImageCreateView.as_view(), name='person_image_create'),
    # path('person/image/update/<int:pk>/', PersonImageUpdateView.as_view(), name='person_image_update'),
    # path('person/image/<int:pk>/', PersonImageDetailView.as_view(), name='person_image_detail'),

    # path('person/image/extra/list/', PersonImageExtraListView.as_view(), name='person_image_extra_list'),
    # path('person/image/extra/create/', PersonImageExtraCreateView.as_view(), name='person_image_extra_create'),
    # path('person/image/extra/update/<int:pk>/', PersonImageExtraUpdateView.as_view(), name='person_image_extra_update'),
    # path('person/image/extra/<int:pk>/', PersonImageExtraDetailView.as_view(), name='person_image_extra_detail'),

    # path('person/nickname/list/', PersonNicknameListView.as_view(), name='person_nickname_list'),
    # path('person/nickname/create/', PersonNicknameCreateView.as_view(), name='person_nickname_create'),
    # path('person/nickname/update/<int:pk>/', PersonNicknameUpdateView.as_view(), name='person_nickname_update'),
    # path('person/nickname/<int:pk>/', PersonNicknameDetailView.as_view(), name='person_nickname_detail'),

    # path('quality/list/', QualityListView.as_view(), name='quality_list'),
    # path('quality/create/', QualityCreateView.as_view(), name='quality_create'),
    # path('quality/update/<int:pk>/', QualityUpdateView.as_view(), name='quality_update'),
    # path('quality/<int:pk>/', QualityDetailView.as_view(), name='quality_detail'),

    # path('website/list/', WebsiteListView.as_view(), name='website_list'),
    # path('website/create/', WebsiteCreateView.as_view(), name='website_create'),
    # path('website/update/<int:pk>/', WebsiteUpdateView.as_view(), name='website_update'),
    # path('website/<int:pk>/', WebsiteDetailView.as_view(), name='website_detail'),

    # apis url


]
