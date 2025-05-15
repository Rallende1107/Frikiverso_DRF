from django.urls import path, include
from .views import HomeView
from .views import AnimeListView, MangaListView, CharacterListView, PersonListView
from .fetch_views import AnimesLoadView, MangaLoadView, CharacterLoadView, PersonLoadView

app_name = 'otaku_app'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('anime/list/', AnimeListView.as_view(), name='anime_list'),
    path('manga/list/', MangaListView.as_view(), name='manga_list'),

    path('person/list/', PersonListView.as_view(), name='person_list'),
    path('character/list/', CharacterListView.as_view(), name='character_list'),
    # apis url
    # path('api/', include('apps.music.api.urls')),


    path('anime/load/', AnimesLoadView.as_view(), name='anime_load'),
    path('manga/load/', MangaLoadView.as_view(), name='manga_load'),
    path('person/load/', PersonLoadView.as_view(), name='person_load'),
    path('character/load/', CharacterLoadView.as_view(), name='character_load'),


]


