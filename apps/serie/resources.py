from import_export import resources
from .models import Genre, Type, Role, Rating, Company, Serie, TitleSerie, SerieStaff, SerieCast, SerieImage, SerieImageExtra
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

########################################################################################################    Resource para Serie
class SerieResource(resources.ModelResource):
    class Meta:
        model = Serie
        fields = ('id', 'title', 'title_secundary', 'release_year', 'synopsis', 'serie_types', 'serie_rating', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'title_secundary', 'release_year', 'synopsis', 'serie_types', 'serie_rating', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TitleSerie
class TitleSerieResource(resources.ModelResource):
    class Meta:
        model = TitleSerie
        fields = ('id', 'serie', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'serie', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para SerieStaff
class SerieStaffResource(resources.ModelResource):
    class Meta:
        model = SerieStaff
        fields = ('id', 'serie', 'person', 'role', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'serie', 'person', 'role', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para SerieCast
class SerieCastResource(resources.ModelResource):
    class Meta:
        model = SerieCast
        fields = ('id', 'serie', 'actor', 'role', 'character_name', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'serie', 'actor', 'role', 'character_name', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para SerieImage
class SerieImageResource(resources.ModelResource):
    class Meta:
        model = SerieImage
        fields = ('id', 'serie', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'serie', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para SerieImageExtra
class SerieImageExtraResource(resources.ModelResource):
    class Meta:
        model = SerieImageExtra
        fields = ('id', 'serie', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'serie', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
