from import_export import resources
from .models import Genre, Type, Role, Rating, Company, Movie, TitleMovie, MovieStaff, MovieCast, MovieImage, MovieImageExtra
# Register your models here.
########################################################################################################    Resource para Genre
class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'explicit', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'explicit', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Type
class TypeResource(resources.ModelResource):
    class Meta:
        model = Type
        fields = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Role
class RoleResource(resources.ModelResource):
    class Meta:
        model = Role
        fields = ('id', 'name', 'name_esp', 'slug', 'initial', 'role_staff', 'role_cast', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'initial', 'role_staff', 'role_cast', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Rating
class RatingResource(resources.ModelResource):
    class Meta:
        model = Rating
        fields = ('id', 'acronym', 'name', 'name_esp', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'acronym', 'name', 'name_esp', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Company
class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
        fields = ('id', 'name', 'slug', 'initial', 'country', 'founded_year', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'slug', 'initial', 'country', 'founded_year', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Movie
class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_secundary', 'release_year', 'duration_minutes', 'synopsis', 'movie_types', 'movie_rating', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'title_secundary', 'release_year', 'duration_minutes', 'synopsis', 'movie_types', 'movie_rating', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TitleMovie
class TitleMovieResource(resources.ModelResource):
    class Meta:
        model = TitleMovie
        fields = ('id', 'movie', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'movie', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MovieStaff
class MovieStaffResource(resources.ModelResource):
    class Meta:
        model = MovieStaff
        fields = ('id', 'movie', 'person', 'role', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'movie', 'person', 'role', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MovieCast
class MovieCastResource(resources.ModelResource):
    class Meta:
        model = MovieCast
        fields = ('id', 'movie', 'actor', 'role', 'character_name', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'movie', 'actor', 'role', 'character_name', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MovieImage
class MovieImageResource(resources.ModelResource):
    class Meta:
        model = MovieImage
        fields = ('id', 'movie', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'movie', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MovieImageExtra
class MovieImageExtraResource(resources.ModelResource):
    class Meta:
        model = MovieImageExtra
        fields = ('id', 'movie', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'movie', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
