from django.urls import path, include
from .views.views import HomeView
from .views.create_views import (
    CensorshipCreateView, DeveloperCreateView, DeveloperImageCreateView, DeveloperImageExtraCreateView, DeveloperLinkCreateView,
    GameCreateView, GameEngineCreateView, GameImageCreateView, GameImageExtraCreateView, GenreCreateView,
    PlatformCreateView, PrefixCreateView, PublisherCreateView, PublisherImageCreateView, PublisherImageExtraCreateView,
    PublisherLinkCreateView, StatusCreateView, TranslatorCreateView, TranslatorImageCreateView, TranslatorImageExtraCreateView,
    TranslatorLinkCreateView, TitleGameCreateView,
    )
from .views.list_views import (
    CensorshipListView, DeveloperListView, DeveloperImageListView, DeveloperImageExtraListView, DeveloperLinkListView,
    GameListView, GameEngineListView, GameImageListView, GameImageExtraListView, GenreListView,
    PlatformListView, PrefixListView, PublisherListView, PublisherImageListView, PublisherImageExtraListView,
    PublisherLinkListView, StatusListView, TranslatorListView, TranslatorImageListView, TranslatorImageExtraListView,
    TranslatorLinkListView, TitleGameListView,
    )

from .views.update_views import (
    CensorshipUpdateView, DeveloperUpdateView, DeveloperImageUpdateView, DeveloperImageExtraUpdateView, DeveloperLinkUpdateView,
    GameUpdateView, GameEngineUpdateView, GameImageUpdateView, GameImageExtraUpdateView, GenreUpdateView,
    PlatformUpdateView, PrefixUpdateView, PublisherUpdateView, PublisherImageUpdateView, PublisherImageExtraUpdateView,
    PublisherLinkUpdateView, StatusUpdateView, TranslatorUpdateView, TranslatorImageUpdateView, TranslatorImageExtraUpdateView,
    TranslatorLinkUpdateView, TitleGameUpdateView,
    )

from .views.detail_views import (
    CensorshipDetailView, DeveloperDetailView, DeveloperImageDetailView, DeveloperImageExtraDetailView, DeveloperLinkDetailView,
    GameDetailView, GameEngineDetailView, GameImageDetailView, GameImageExtraDetailView, GenreDetailView,
    PlatformDetailView, PrefixDetailView, PublisherDetailView, PublisherImageDetailView, PublisherImageExtraDetailView,
    PublisherLinkDetailView, StatusDetailView, TranslatorDetailView, TranslatorImageDetailView, TranslatorImageExtraDetailView,
    TranslatorLinkDetailView, TitleGameDetailView,
    )

from .views.list_by_views import (
GameByDeveloperListView, GameByStatusListView, GameByPlatformListView, GameByEngineListView, GameByGenreListView, GameByTranslatorListView, GameByPublisherListView,
)

from .views.fetch_views import (GamesLoadView)

app_name = 'renpy_app'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('censorship/create/', CensorshipCreateView.as_view(), name='censorship_create'),
    path('developer/create/', DeveloperCreateView.as_view(), name='developer_create'),
    path('developer/image/create/', DeveloperImageCreateView.as_view(), name='developer_image_create'),
    path('developer/image/extra/create/', DeveloperImageExtraCreateView.as_view(), name='developer_image_extra_create'),
    path('developer/link/create/', DeveloperLinkCreateView.as_view(), name='developer_link_create'),
    path('game/create/', GameCreateView.as_view(), name='game_create'),
    path('game/engine/create/', GameEngineCreateView.as_view(), name='game_engine_create'),
    path('game/image/create/', GameImageCreateView.as_view(), name='game_image_create'),
    path('game/image/extra/create/', GameImageExtraCreateView.as_view(), name='game_image_extra_create'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('platform/create/', PlatformCreateView.as_view(), name='platform_create'),
    path('prefix/create/', PrefixCreateView.as_view(), name='prefix_create'),
    path('publisher/create/', PublisherCreateView.as_view(), name='publisher_create'),
    path('publisher/image/create/', PublisherImageCreateView.as_view(), name='publisher_image_create'),
    path('publisher/image/extra/create/', PublisherImageExtraCreateView.as_view(), name='publisher_image_extra_create'),
    path('publisher/link/create/', PublisherLinkCreateView.as_view(), name='publisher_link_create'),
    path('status/create/', StatusCreateView.as_view(), name='status_create'),
    path('translator/create/', TranslatorCreateView.as_view(), name='translator_create'),
    path('translator/image/create/', TranslatorImageCreateView.as_view(), name='translator_image_create'),
    path('translator/image/extra/create/', TranslatorImageExtraCreateView.as_view(), name='translator_image_extra_create'),
    path('translator/link/create/', TranslatorLinkCreateView.as_view(), name='translator_link_create'),
    path('title/game/create/', TitleGameCreateView.as_view(), name='title_game_create'),

    path('censorship/list/', CensorshipListView.as_view(), name='censorship_list'),
    path('developer/list/', DeveloperListView.as_view(), name='developer_list'),
    path('developer/image/list/', DeveloperImageListView.as_view(), name='developer_image_list'),
    path('developer/image/extra/list/', DeveloperImageExtraListView.as_view(), name='developer_image_extra_list'),
    path('developer/link/list/', DeveloperLinkListView.as_view(), name='developer_link_list'),
    path('game/list/', GameListView.as_view(), name='game_list'),
    path('game/engine/list/', GameEngineListView.as_view(), name='game_engine_list'),
    path('game/image/list/', GameImageListView.as_view(), name='game_image_list'),
    path('game/image/extra/list/', GameImageExtraListView.as_view(), name='game_image_extra_list'),
    path('genre/list/', GenreListView.as_view(), name='genre_list'),
    path('platform/list/', PlatformListView.as_view(), name='platform_list'),
    path('prefix/list/', PrefixListView.as_view(), name='prefix_list'),
    path('publisher/list/', PublisherListView.as_view(), name='publisher_list'),
    path('publisher/image/list/', PublisherImageListView.as_view(), name='publisher_image_list'),
    path('publisher/image/extra/list/', PublisherImageExtraListView.as_view(), name='publisher_image_extra_list'),
    path('publisher/link/list/', PublisherLinkListView.as_view(), name='publisher_link_list'),
    path('status/list/', StatusListView.as_view(), name='status_list'),
    path('translator/list/', TranslatorListView.as_view(), name='translator_list'),
    path('translator/image/list/', TranslatorImageListView.as_view(), name='translator_image_list'),
    path('translator/image/extra/list/', TranslatorImageExtraListView.as_view(), name='translator_image_extra_list'),
    path('translator/link/list/', TranslatorLinkListView.as_view(), name='translator_link_list'),
    path('title/game/list/', TitleGameListView.as_view(), name='title_game_list'),

    path('censorship/update/<int:pk>/', CensorshipUpdateView.as_view(), name='censorship_update'),
    path('developer/update/<int:pk>/', DeveloperUpdateView.as_view(), name='developer_update'),
    path('developer/image/update/<int:pk>/', DeveloperImageUpdateView.as_view(), name='developer_image_update'),
    path('developer/image/extra/update/<int:pk>/', DeveloperImageExtraUpdateView.as_view(), name='developer_image_extra_update'),
    path('developer/link/update/<int:pk>/', DeveloperLinkUpdateView.as_view(), name='developer_link_update'),
    path('game/update/<int:pk>/', GameUpdateView.as_view(), name='game_update'),
    path('game/engine/update/<int:pk>/', GameEngineUpdateView.as_view(), name='game_engine_update'),
    path('game/image/update/<int:pk>/', GameImageUpdateView.as_view(), name='game_image_update'),
    path('game/image/extra/update/<int:pk>/', GameImageExtraUpdateView.as_view(), name='game_image_extra_update'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('platform/update/<int:pk>/', PlatformUpdateView.as_view(), name='platform_update'),
    path('prefix/update/<int:pk>/', PrefixUpdateView.as_view(), name='prefix_update'),
    path('publisher/update/<int:pk>/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/image/update/<int:pk>/', PublisherImageUpdateView.as_view(), name='publisher_image_update'),
    path('publisher/image/extra/update/<int:pk>/', PublisherImageExtraUpdateView.as_view(), name='publisher_image_extra_update'),
    path('publisher/link/update/<int:pk>/', PublisherLinkUpdateView.as_view(), name='publisher_link_update'),
    path('status/update/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
    path('translator/update/<int:pk>/', TranslatorUpdateView.as_view(), name='translator_update'),
    path('translator/image/update/<int:pk>/', TranslatorImageUpdateView.as_view(), name='translator_image_update'),
    path('translator/image/extra/update/<int:pk>/', TranslatorImageExtraUpdateView.as_view(), name='translator_image_extra_update'),
    path('translator/link/update/<int:pk>/', TranslatorLinkUpdateView.as_view(), name='translator_link_update'),
    path('title/game/update/<int:pk>/', TitleGameUpdateView.as_view(), name='title_game_update'),

    path('censorship<int:pk>/', CensorshipDetailView.as_view(), name='censorship_detail'),
    path('developer<int:pk>/', DeveloperDetailView.as_view(), name='developer_detail'),
    path('developer/image<int:pk>/', DeveloperImageDetailView.as_view(), name='developer_image_detail'),
    path('developer/image/extra<int:pk>/', DeveloperImageExtraDetailView.as_view(), name='developer_image_extra_detail'),
    path('developer/link<int:pk>/', DeveloperLinkDetailView.as_view(), name='developer_link_detail'),
    path('game<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('game/engine<int:pk>/', GameEngineDetailView.as_view(), name='game_engine_detail'),
    path('game/image<int:pk>/', GameImageDetailView.as_view(), name='game_image_detail'),
    path('game/image/extra<int:pk>/', GameImageExtraDetailView.as_view(), name='game_image_extra_detail'),
    path('genre<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('platform<int:pk>/', PlatformDetailView.as_view(), name='platform_detail'),
    path('prefix<int:pk>/', PrefixDetailView.as_view(), name='prefix_detail'),
    path('publisher<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publisher/image<int:pk>/', PublisherImageDetailView.as_view(), name='publisher_image_detail'),
    path('publisher/image/extra<int:pk>/', PublisherImageExtraDetailView.as_view(), name='publisher_image_extra_detail'),
    path('publisher/link<int:pk>/', PublisherLinkDetailView.as_view(), name='publisher_link_detail'),
    path('status<int:pk>/', StatusDetailView.as_view(), name='status_detail'),
    path('translator<int:pk>/', TranslatorDetailView.as_view(), name='translator_detail'),
    path('translator/image<int:pk>/', TranslatorImageDetailView.as_view(), name='translator_image_detail'),
    path('translator/image/extra<int:pk>/', TranslatorImageExtraDetailView.as_view(), name='translator_image_extra_detail'),
    path('translator/link<int:pk>/', TranslatorLinkDetailView.as_view(), name='translator_link_detail'),
    path('title/game<int:pk>/', TitleGameDetailView.as_view(), name='title_game_detail'),

    path('game/load/', GamesLoadView.as_view(), name='game_load'),

    # apis url

    path('games/developer/<int:developer_id>/', GameByDeveloperListView.as_view(), name='game_by_developer'),
    path('games/status/<int:status_id>/', GameByStatusListView.as_view(), name='game_by_status'),
    path('games/platform/<int:platform_id>/', GameByPlatformListView.as_view(), name='game_by_platform'),
    path('games/engine/<int:engine_id>/', GameByEngineListView.as_view(), name='game_by_engine'),
    path('games/genre/<int:genre_id>/', GameByGenreListView.as_view(), name='game_by_genre'),
    path('games/translator/<int:translator_id>/', GameByTranslatorListView.as_view(), name='game_by_translator'),
    path('games/publisher/<int:publisher_id>/', GameByPublisherListView.as_view(), name='game_by_publisher'),

    # apis url
    path('api/', include('apps.renpy.api.urls')),
]


