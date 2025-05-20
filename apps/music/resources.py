from core.resources import BaseFullResource
from .models import Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra

########################################################################################################    Resource para Genre
class GenreResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Genre

########################################################################################################    Resource para Role
class RoleResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Role

########################################################################################################    Resource para AlbumType
class AlbumTypeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AlbumType

########################################################################################################    Resource para ArtistType
class ArtistTypeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = ArtistType

########################################################################################################    Resource para Artist
class ArtistResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Artist

########################################################################################################    Resource para ArtistMember
class ArtistMemberResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = ArtistMember

########################################################################################################    Resource para Album
class AlbumResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Album

########################################################################################################    Resource para Song
class SongResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Song

########################################################################################################    Resource para AlbumImage
class AlbumImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AlbumImage

########################################################################################################    Resource para AlbumImageExtra
class AlbumImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AlbumImageExtra

########################################################################################################    Resource para ArtistImage
class ArtistImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = ArtistImage

########################################################################################################    Resource para ArtistImageExtra
class ArtistImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = ArtistImageExtra
