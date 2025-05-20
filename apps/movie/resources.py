from core.resources import BaseFullResource
from .models import Genre, Type, Role, Rating, Company, Movie, TitleMovie, MovieStaff, MovieCast, MovieImage, MovieImageExtra
# Register your models here.
########################################################################################################    Resource para Genre
class GenreResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Genre

########################################################################################################    Resource para Type
class TypeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Type

########################################################################################################    Resource para Role
class RoleResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Role

########################################################################################################    Resource para Rating
class RatingResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Rating

########################################################################################################    Resource para Company
class CompanyResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Company

########################################################################################################    Resource para Movie
class MovieResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Movie

########################################################################################################    Resource para TitleMovie
class TitleMovieResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = TitleMovie

########################################################################################################    Resource para MovieStaff
class MovieStaffResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MovieStaff

########################################################################################################    Resource para MovieCast
class MovieCastResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MovieCast

########################################################################################################    Resource para MovieImage
class MovieImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MovieImage

########################################################################################################    Resource para MovieImageExtra
class MovieImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MovieImageExtra

