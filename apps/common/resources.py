from import_export import resources
from apps.common.models import Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website
# Register your models here.
########################################################################################################    Resource para Country
class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        # Exporta todos los campos automáticamente
        export_order = (
            'id', 'name', 'name_esp', 'initial', 'initial_esp',
            'slug', 'code', 'numeric_code', 'is_active',
            'created_at', 'updated_at',
        )

########################################################################################################    Resource para Format
class FormatResource(resources.ModelResource):
    class Meta:
        model = Format
        export_order = (
            'id', 'name', 'for_video', 'for_music', 'for_image',
            'for_document', 'for_other', 'slug',
            'is_active', 'created_at', 'updated_at',
        )

########################################################################################################    Resource para ImageSize
class ImageSizeResource(resources.ModelResource):
    class Meta:
        model = ImageSize
        export_order = (
            'id', 'name', 'name_esp', 'slug', 'is_active',
        )

########################################################################################################    Resource para Language
class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language
        export_order = (
            'id', 'name', 'name_esp', 'acronym', 'initial', 'slug', 'is_active', 'created_at', 'updated_at'
        )

########################################################################################################    Resource para Person
class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        export_order = (
            'id', 'full_name', 'initial', 'biography', 'birth_date',
            'country', 'slug', 'is_active', 'created_at', 'updated_at'
        )

########################################################################################################    Resource para PersonImage
class PersonImageResource(resources.ModelResource):
    class Meta:
        model = PersonImage
        export_order = (
            'id', 'person', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at',
        )

########################################################################################################    Resource para PersonImageExtra
class PersonImageExtraResource(resources.ModelResource):
    class Meta:
        model = PersonImageExtra
        export_order = (
            'id', 'person', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at',
        )

########################################################################################################    Resource para PersonNickname
class PersonNicknameResource(resources.ModelResource):
    class Meta:
        model = PersonNickname
        export_order = (
            'id', 'person', 'nickname', 'initial', 'slug', 'is_active', 'created_at', 'updated_at',
        )

########################################################################################################    Resource para Quality
class QualityResource(resources.ModelResource):
    class Meta:
        model = Quality
        export_order = (
            'id', 'name', 'description', 'slug', 'is_active', 'created_at', 'updated_at',
        )

########################################################################################################    Resource para Website
class WebsiteResource(resources.ModelResource):
    class Meta:
        model = Website
        export_order = (
            'id', 'name', 'acronym', 'url', 'initial', 'slug', 'is_active', 'created_at', 'updated_at',
        )