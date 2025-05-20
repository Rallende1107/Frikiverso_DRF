from django.urls import path, include
from .views.views import HomeView
from .views.create_views import (GenreCreateView, RoleCreateView, AlbumTypeCreateView, ArtistTypeCreateView, ArtistCreateView, ArtistMemberCreateView, AlbumCreateView, SongCreateView, AlbumImageCreateView, AlbumImageExtraCreateView, ArtistImageCreateView, ArtistImageExtraCreateView,)
from .views.list_views import (GenreListView, RoleListView, AlbumTypeListView, ArtistTypeListView, ArtistListView, ArtistMemberListView, AlbumListView, SongListView, AlbumImageListView, AlbumImageExtraListView, ArtistImageListView, ArtistImageExtraListView,)
from .views.update_views import (GenreUpdateView, RoleUpdateView, AlbumTypeUpdateView, ArtistTypeUpdateView, ArtistUpdateView, ArtistMemberUpdateView, AlbumUpdateView, SongUpdateView, AlbumImageUpdateView, AlbumImageExtraUpdateView, ArtistImageUpdateView, ArtistImageExtraUpdateView,)
from .views.detail_views import (ArtistImageDetailView)

app_name = 'music_app'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('role/create/', RoleCreateView.as_view(), name='role_create'),
    path('album/type/create/', AlbumTypeCreateView.as_view(), name='album_type_create'),
    path('artist/type/create/', ArtistTypeCreateView.as_view(), name='artist_type_create'),
    path('artist/create/', ArtistCreateView.as_view(), name='artist_create'),
    path('artist/member/create/', ArtistMemberCreateView.as_view(), name='artist_member_create'),
    path('album/create/', AlbumCreateView.as_view(), name='album_create'),
    path('song/create/', SongCreateView.as_view(), name='song_create'),
    path('album/image/create/', AlbumImageCreateView.as_view(), name='album_image_create'),
    path('album/imageextra/create/', AlbumImageExtraCreateView.as_view(), name='album_image_extra_create'),
    path('artist/image/create/', ArtistImageCreateView.as_view(), name='artist_image_create'),
    path('artist/imageextra/create/', ArtistImageExtraCreateView.as_view(), name='artist_image_extra_create'),

    path('genre/list/', GenreListView.as_view(), name='genre_list'),
    path('role/list/', RoleListView.as_view(), name='role_list'),
    path('album/type/list/', AlbumTypeListView.as_view(), name='album_type_list'),
    path('artist/type/list/', ArtistTypeListView.as_view(), name='artist_type_list'),
    path('artist/list/', ArtistListView.as_view(), name='artist_list'),
    path('artist/member/list/', ArtistMemberListView.as_view(), name='artist_member_list'),
    path('album/list/', AlbumListView.as_view(), name='album_list'),
    path('song/list/', SongListView.as_view(), name='song_list'),
    path('album/image/list/', AlbumImageListView.as_view(), name='album_image_list'),
    path('album/imageextra/list/', AlbumImageExtraListView.as_view(), name='album_image_extra_list'),
    path('artist/image/list/', ArtistImageListView.as_view(), name='artist_image_list'),
    path('artist/imageextra/list/', ArtistImageExtraListView.as_view(), name='artist_image_extra_list'),

    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('role/update/<int:pk>/', RoleUpdateView.as_view(), name='role_update'),
    path('album/type/update/<int:pk>/', AlbumTypeUpdateView.as_view(), name='album_type_update'),
    path('artist/type/update/<int:pk>/', ArtistTypeUpdateView.as_view(), name='artist_type_update'),
    path('artist/update/<int:pk>/', ArtistUpdateView.as_view(), name='artist_update'),
    path('artist/member/update/<int:pk>/', ArtistMemberUpdateView.as_view(), name='artist_member_update'),
    path('album/update/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('song/update/<int:pk>/', SongUpdateView.as_view(), name='song_update'),
    path('album/image/update/<int:pk>/', AlbumImageUpdateView.as_view(), name='album_image_update'),
    path('album/image/extra/update/<int:pk>/', AlbumImageExtraUpdateView.as_view(), name='album_image_extra_update'),
    path('artist/image/update/<int:pk>/', ArtistImageUpdateView.as_view(), name='artist_image_update'),
    path('artist/image/extra/update/<int:pk>/', ArtistImageExtraUpdateView.as_view(), name='artist_image_extra_update'),

    path('artist/image/<int:pk>/', ArtistImageDetailView.as_view(), name='artist_image_detail'),

    # apis url
    path('api/', include('apps.music.api.urls')),
]
"""
path('',





















"""