from import_export import resources
from .models import (
    Role, Year, Genre, Theme, Demographic, Type, Rating, Season, Status, Source, RelationType, SeasonFull,
    Producer, Licensor, Studio, Serialization, Anime, Manga, TitleAnime, TitleManga, AnimeSong, MediaRelation,
    Character, CharacterNickname, OtakuPerson, OtakuPersonNickname,
    AnimeCharacter, MangaCharacter, VoiceCharacter, AnimeStaff, AuthorManga,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra, OtakuPersonImage, OtakuPersonImageExtra, CharacterImage, CharacterImageExtra,
    DataAnime, DataAnimeCharacters, DataAnimePictures, DataAnimeStaff, DataManga, DataMangaCharacters, DataMangaPictures, DataCharacter,
    DataCharacterPictures, DataOtakuPerson, DataOtakuPersonPictures, DataImageURL, Temp_OtakuPersons, Temp_Characters
    )
# Register your models here.
########################################################################################################    Resource para Role
class RoleResource(resources.ModelResource):
    class Meta:
        model = Role
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'role_staff', 'role_chara', 'role_manga', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'role_staff', 'role_chara', 'role_manga', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Year
class YearResource(resources.ModelResource):
    class Meta:
        model = Year
        fields = ('id', 'year', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'year', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Genre
class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'explicit', 'parent', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'explicit', 'parent', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Theme
class ThemeResource(resources.ModelResource):
    class Meta:
        model = Theme
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'explicit', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'explicit', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Demographic
class DemographicResource(resources.ModelResource):
    class Meta:
        model = Demographic
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'explicit', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'explicit', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Type
class TypeResource(resources.ModelResource):
    class Meta:
        model = Type
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Rating
class RatingResource(resources.ModelResource):
    class Meta:
        model = Rating
        fields = ('id', 'acronym', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'acronym', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Season
class SeasonResource(resources.ModelResource):
    class Meta:
        model = Season
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Status
class StatusResource(resources.ModelResource):
    class Meta:
        model = Status
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Source
class SourceResource(resources.ModelResource):
    class Meta:
        model = Source
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para RelationType
class RelationTypeResource(resources.ModelResource):
    class Meta:
        model = RelationType
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para SeasonFull
class SeasonFullResource(resources.ModelResource):
    class Meta:
        model = SeasonFull
        fields = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'name_esp', 'slug', 'description', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Producer
class ProducerResource(resources.ModelResource):
    class Meta:
        model = Producer
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Licensor
class LicensorResource(resources.ModelResource):
    class Meta:
        model = Licensor
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Studio
class StudioResource(resources.ModelResource):
    class Meta:
        model = Studio
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Serialization
class SerializationResource(resources.ModelResource):
    class Meta:
        model = Serialization
        fields = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'name', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Anime
class AnimeResource(resources.ModelResource):
    class Meta:
        model = Anime
        fields = ('id', 'title', 'title_eng', 'title_jap', 'episodes', 'from_date', 'to_date', 'synopsis', 'slug', 'initial',
                  'anime_type', 'status', 'season', 'season_full', 'year', 'source', 'rating', 'url', 'mal_id', 'p_mal_id',
                  'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'title_eng', 'title_jap', 'episodes', 'from_date', 'to_date', 'synopsis', 'slug', 'initial',
                        'anime_type', 'status', 'season', 'season_full', 'year', 'source', 'rating', 'url', 'mal_id', 'p_mal_id',
                        'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Manga
class MangaResource(resources.ModelResource):
    class Meta:
        model = Manga
        fields = ('id', 'title', 'title_eng', 'title_jap', 'chapters', 'volumes', 'synopsis', 'slug', 'initial',
                  'manga_type', 'year', 'status', 'season', 'season_full', 'source', 'rating', 'url', 'mal_id', 'p_mal_id',
                  'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'title', 'title_eng', 'title_jap', 'chapters', 'volumes', 'synopsis', 'slug', 'initial',
                        'manga_type', 'year', 'status', 'season', 'season_full', 'source', 'rating', 'url', 'mal_id', 'p_mal_id',
                        'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TitleAnime
class TitleAnimeResource(resources.ModelResource):
    class Meta:
        model = TitleAnime
        fields = ('id', 'anime', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'anime', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para TitleManga
class TitleMangaResource(resources.ModelResource):
    class Meta:
        model = TitleManga
        fields = ('id', 'manga', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'manga', 'title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para Character
class CharacterResource(resources.ModelResource):
    class Meta:
        model = Character
        fields = ('id', 'full_name', 'name_kanji', 'biography', 'slug', 'initial', 'url', 'mal_id', 'p_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para CharacterNickname
class CharacterNicknameResource(resources.ModelResource):
    class Meta:
        model = CharacterNickname
        fields = ('id', 'character', 'nickname', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para OtakuPerson
class OtakuPersonResource(resources.ModelResource):
    class Meta:
        model = OtakuPerson
        fields = ('id', 'full_name', 'name_kanji', 'biography', 'slug', 'initial', 'birth_date', 'voice_actor', 'author', 'staff', 'url', 'mal_id', 'p_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para OtakuPersonNickname
class OtakuPersonNicknameResource(resources.ModelResource):
    class Meta:
        model = OtakuPersonNickname
        fields = ('id', 'person', 'nickname', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AnimeSong
class AnimeSongResource(resources.ModelResource):
    class Meta:
        model = AnimeSong
        fields = ('id', 'anime', 'song_type', 'song_id', 'title', 'artist', 'title_kanji', 'title_eng', 'slug', 'song_title', 'cls_title', 'cls_song_title', 'cls_title_kanji', 'cls_title_eng', 'revisado', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AnimeCharacter
class AnimeCharacterResource(resources.ModelResource):
    class Meta:
        model = AnimeCharacter
        fields = ('id', 'character', 'anime', 'role', 'character_mal_id', 'anime_mal_id', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'character', 'anime', 'role', 'character_mal_id', 'anime_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MangaCharacter
class MangaCharacterResource(resources.ModelResource):
    class Meta:
        model = MangaCharacter
        fields = ('id', 'character', 'manga', 'role', 'character_mal_id', 'manga_mal_id', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'character', 'manga', 'role', 'character_mal_id', 'manga_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para VoiceCharacter
class VoiceCharacterResource(resources.ModelResource):
    class Meta:
        model = VoiceCharacter
        fields = ('id', 'person', 'anime', 'character', 'language', 'person_mal_id', 'anime_mal_id', 'character_mal_id', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'person', 'anime', 'character', 'language', 'person_mal_id', 'anime_mal_id', 'character_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AnimeStaff
class AnimeStaffResource(resources.ModelResource):
    class Meta:
        model = AnimeStaff
        fields = ('id', 'person', 'anime', 'character', 'position', 'person_mal_id', 'anime_mal_id', 'character_mal_id', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'person', 'anime', 'character', 'position', 'person_mal_id', 'anime_mal_id', 'character_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AuthorManga
class AuthorMangaResource(resources.ModelResource):
    class Meta:
        model = AuthorManga
        fields = ('id', 'person', 'manga', 'position', 'person_mal_id', 'manga_mal_id', 'is_active', 'created_at', 'updated_at')
        export_order = ('id', 'person', 'manga', 'position', 'person_mal_id', 'manga_mal_id', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MediaRelation
class MediaRelationResource(resources.ModelResource):
    class Meta:
        model = MediaRelation
        fields = (
            'id', 'relation_type', 'from_entry_mal_id', 'from_entry_mal_id_p', 'from_entry_type',
            'to_entry_mal_id', 'to_entry_mal_id_p', 'to_entry_type',
            'is_active', 'created_at', 'updated_at'
        )
        export_order = (
            'id', 'relation_type', 'from_entry_mal_id', 'from_entry_mal_id_p', 'from_entry_type',
            'to_entry_mal_id', 'to_entry_mal_id_p', 'to_entry_type',
            'is_active', 'created_at', 'updated_at'
        )

########################################################################################################    Resource para AnimeImage
class AnimeImageResource(resources.ModelResource):
    class Meta:
        model = AnimeImage
        fields = ('id', 'anime', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para AnimeImageExtra
class AnimeImageExtraResource(resources.ModelResource):
    class Meta:
        model = AnimeImageExtra
        fields = ('id', 'anime', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MangaImage
class MangaImageResource(resources.ModelResource):
    class Meta:
        model = MangaImage
        fields = ('id', 'manga', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para MangaImageExtra
class MangaImageExtraResource(resources.ModelResource):
    class Meta:
        model = MangaImageExtra
        fields = ('id', 'manga', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para OtakuPersonImage
class OtakuPersonImageResource(resources.ModelResource):
    class Meta:
        model = OtakuPersonImage
        fields = ('id', 'person', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para OtakuPersonImageExtra
class OtakuPersonImageExtraResource(resources.ModelResource):
    class Meta:
        model = OtakuPersonImageExtra
        fields = ('id', 'person', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para CharacterImage
class CharacterImageResource(resources.ModelResource):
    class Meta:
        model = CharacterImage
        fields = ('id', 'character', 'size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para CharacterImageExtra
class CharacterImageExtraResource(resources.ModelResource):
    class Meta:
        model = CharacterImageExtra
        fields = ('id', 'character', 'image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')

########################################################################################################    Resource para DataAnime
class DataAnimeResource(resources.ModelResource):
    class Meta:
        model = DataAnime
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataAnimeCharacters
class DataAnimeCharactersResource(resources.ModelResource):
    class Meta:
        model = DataAnimeCharacters
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataAnimePictures
class DataAnimePicturesResource(resources.ModelResource):
    class Meta:
        model = DataAnimePictures
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataAnimeStaff
class DataAnimeStaffResource(resources.ModelResource):
    class Meta:
        model = DataAnimeStaff
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataManga
class DataMangaResource(resources.ModelResource):
    class Meta:
        model = DataManga
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataMangaCharacters
class DataMangaCharactersResource(resources.ModelResource):
    class Meta:
        model = DataMangaCharacters
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataMangaPictures
class DataMangaPicturesResource(resources.ModelResource):
    class Meta:
        model = DataMangaPictures
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataCharacter
class DataCharacterResource(resources.ModelResource):
    class Meta:
        model = DataCharacter
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataCharacterPictures
class DataCharacterPicturesResource(resources.ModelResource):
    class Meta:
        model = DataCharacterPictures
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataOtakuPerson
class DataOtakuPersonResource(resources.ModelResource):
    class Meta:
        model = DataOtakuPerson
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataOtakuPersonPictures
class DataOtakuPersonPicturesResource(resources.ModelResource):
    class Meta:
        model = DataOtakuPersonPictures
        fields = ('id', 'mal_id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para DataImageURL
class DataImageURLResource(resources.ModelResource):
    class Meta:
        model = DataImageURL
        fields = ('id', 'url', 'status', 'data', 'processed', 'created_at', 'updated_at')

########################################################################################################    Resource para Temp_OtakuPersons
class Temp_OtakuPersonsResource(resources.ModelResource):
    class Meta:
        model = Temp_OtakuPersons
        fields = ('id', 'mal_id_person', 'lenguaje')

########################################################################################################    Resource para Temp_Characters
class Temp_CharactersResource(resources.ModelResource):
    class Meta:
        model = Temp_Characters
        fields = ('id', 'mal_id_character')