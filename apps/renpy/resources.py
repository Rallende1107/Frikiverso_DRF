from import_export import resources
from .models import (Genre, GameEngine, Censorship, Prefix, Status, Platform, Developer, Translator, Publisher, Game,
    GameImage, GameImageExtra, DeveloperLink, TranslatorLink, PublisherLink, DeveloperImage, DeveloperImageExtra,
    TranslatorImage, TranslatorImageExtra, PublisherImage, PublisherImageExtra, TitleGame, F95GameFetchStatus,
)
# Register your models here.
########################################################################################################    Resource para Genre
class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'explicit', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'parent', 'name', 'name_esp', 'initial', 'slug', 'description', 'explicit', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para GameEngine
class GameEngineResource(resources.ModelResource):
    class Meta:
        model = GameEngine
        fields = ('id', 'name', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Censorship
class CensorshipResource(resources.ModelResource):
    class Meta:
        model = Censorship
        fields = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Prefix
class PrefixResource(resources.ModelResource):
    class Meta:
        model = Prefix
        fields = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Status
class StatusResource(resources.ModelResource):
    class Meta:
        model = Status
        fields = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Platform
class PlatformResource(resources.ModelResource):
    class Meta:
        model = Platform
        fields = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'initial', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Developer
class DeveloperResource(resources.ModelResource):
    class Meta:
        model = Developer
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Translator
class TranslatorResource(resources.ModelResource):
    class Meta:
        model = Translator
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Publisher
class PublisherResource(resources.ModelResource):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Game
class GameResource(resources.ModelResource):
    class Meta:
        model = Game
        fields = (
            'id', 'title', 'slug', 'version', 'initial', 'release_date', 'synopsis', 'background',
            'status', 'engine', 'platforms', 'developers', 'publishers', 'languages', 'translators',
            'genres', 'censored', 'url_fzone', 'url_steam', 'fzone_id', 'version_txt', 'is_active',
            'created_at', 'updated_at'
        )
        export_order = (
            'id', 'title', 'slug', 'version', 'initial', 'release_date', 'synopsis', 'background',
            'status', 'engine', 'platforms', 'developers', 'publishers', 'languages', 'translators',
            'genres', 'censored', 'url_fzone', 'url_steam', 'fzone_id', 'version_txt', 'is_active',
            'created_at', 'updated_at'
        )

########################################################################################################    Resource para GameImage
class GameImageResource(resources.ModelResource):
    class Meta:
        model = GameImage
        fields = ('id', 'game', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'game', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para GameImageExtra
class GameImageExtraResource(resources.ModelResource):
    class Meta:
        model = GameImageExtra
        fields = ('id', 'game', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'game', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para DeveloperLink
class DeveloperLinkResource(resources.ModelResource):
    class Meta:
        model = DeveloperLink
        fields = ('id', 'developer', 'name', 'slug', 'initial', 'url', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'developer', 'name', 'slug', 'initial', 'url', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TranslatorLink
class TranslatorLinkResource(resources.ModelResource):
    class Meta:
        model = TranslatorLink
        fields = ('id', 'translator', 'name', 'slug', 'initial', 'url', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'translator', 'name', 'slug', 'initial', 'url', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para PublisherLink
class PublisherLinkResource(resources.ModelResource):
    class Meta:
        model = PublisherLink
        fields = ('id', 'publisher', 'name', 'slug', 'initial', 'url', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'publisher', 'name', 'slug', 'initial', 'url', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para DeveloperImage
class DeveloperImageResource(resources.ModelResource):
    class Meta:
        model = DeveloperImage
        fields = ('id', 'developer', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'developer', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para DeveloperImageExtra
class DeveloperImageExtraResource(resources.ModelResource):
    class Meta:
        model = DeveloperImageExtra
        fields = ('id', 'developer', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'developer', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TranslatorImage
class TranslatorImageResource(resources.ModelResource):
    class Meta:
        model = TranslatorImage
        fields = ('id', 'translator', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'translator', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TranslatorImageExtra
class TranslatorImageExtraResource(resources.ModelResource):
    class Meta:
        model = TranslatorImageExtra
        fields = ('id', 'translator', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'translator', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para PublisherImage
class PublisherImageResource(resources.ModelResource):
    class Meta:
        model = PublisherImage
        fields = ('id', 'publisher', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'publisher', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para PublisherImageExtra
class PublisherImageExtraResource(resources.ModelResource):
    class Meta:
        model = PublisherImageExtra
        fields = ('id', 'publisher', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'publisher', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TitleGame
class TitleGameResource(resources.ModelResource):
    class Meta:
        model = TitleGame
        fields = ('id', 'game', 'language', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'game', 'language', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para F95GameFetchStatus
class F95GameFetchStatusResource(resources.ModelResource):
    class Meta:
        model = F95GameFetchStatus
        fields = ('id', 'url', 'f95_id', 'status', 'data', 'processed', 'created_at', 'updated_at')
        export_order = ('id', 'url', 'f95_id', 'status', 'data', 'processed', 'created_at', 'updated_at')