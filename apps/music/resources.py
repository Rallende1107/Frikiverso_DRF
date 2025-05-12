from import_export import resources
from .models import Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra
# Register your models here.
########################################################################################################    Resource para Genre
class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Role
class RoleResource(resources.ModelResource):
    class Meta:
        model = Role
        fields = ('id', 'name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AlbumType
class AlbumTypeResource(resources.ModelResource):
    class Meta:
        model = AlbumType
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para ArtistType
class ArtistTypeResource(resources.ModelResource):
    class Meta:
        model = ArtistType
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Artist
class ArtistResource(resources.ModelResource):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'slug', 'initial', 'biography', 'start_year', 'year_end', 'artist_type', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'slug', 'initial', 'biography', 'start_year', 'year_end', 'artist_type', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para ArtistMember
class ArtistMemberResource(resources.ModelResource):
    class Meta:
        model = ArtistMember
        fields = ('id', 'artist', 'person', 'role', 'join_date', 'leave_date', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'artist', 'person', 'role', 'join_date', 'leave_date', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Album
class AlbumResource(resources.ModelResource):
    class Meta:
        model = Album
        fields = ('id', 'title', 'slug', 'initial', 'artist', 'album_type', 'release_date', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'slug', 'initial', 'artist', 'album_type', 'release_date', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Song
class SongResource(resources.ModelResource):
    class Meta:
        model = Song
        fields = ('id', 'title', 'slug', 'initial', 'lyrics', 'album_song_id', 'release_date', 'album', 'audio_file', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'slug', 'initial', 'lyrics', 'album_song_id', 'release_date', 'album', 'audio_file', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AlbumImage
class AlbumImageResource(resources.ModelResource):
    class Meta:
        model = AlbumImage
        fields = ('id', 'album', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'album', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AlbumImageExtra
class AlbumImageExtraResource(resources.ModelResource):
    class Meta:
        model = AlbumImageExtra
        fields = ('id', 'album', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'album', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para ArtistImage
class ArtistImageResource(resources.ModelResource):
    class Meta:
        model = ArtistImage
        fields = ('id', 'artist', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'artist', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para ArtistImageExtra
class ArtistImageExtraResource(resources.ModelResource):
    class Meta:
        model = ArtistImageExtra
        fields = ('id', 'artist', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'artist', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
