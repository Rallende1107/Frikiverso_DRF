from core.resources import BaseFullResource
from .models import (
    Role, Year, Genre, Theme, Demographic, Type, Rating, Season, Status, Source, RelationType, SeasonFull,
    Anime, Manga, TitleAnime, TitleManga, AnimeSong, MediaRelation,
    Character, CharacterNickname, Person, PersonNickname,
    AnimeCharacter, MangaCharacter, VoiceCharacter, AnimeStaff, AuthorManga,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra, PersonImage, PersonImageExtra, CharacterImage, CharacterImageExtra,
    DataAnime, DataAnimeCharacters, DataAnimePictures, DataAnimeStaff, DataManga, DataMangaCharacters, DataMangaPictures, DataCharacter,
    DataCharacterPictures, DataPerson, DataPersonPictures, DataImageURL, Temp_Persons, Temp_Characters
    )
# Register your models here.
########################################################################################################    Resource para Role
class RoleResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Role

########################################################################################################    Resource para Year
class YearResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Year

########################################################################################################    Resource para Genre
class GenreResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Genre

########################################################################################################    Resource para Theme
class ThemeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Theme

########################################################################################################    Resource para Demographic
class DemographicResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Demographic

########################################################################################################    Resource para Type
class TypeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Type

########################################################################################################    Resource para Rating
class RatingResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Rating

########################################################################################################    Resource para Season
class SeasonResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Season

########################################################################################################    Resource para Status
class StatusResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Status

########################################################################################################    Resource para Source
class SourceResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Source

########################################################################################################    Resource para RelationType
class RelationTypeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = RelationType

########################################################################################################    Resource para SeasonFull
class SeasonFullResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = SeasonFull

########################################################################################################    Resource para Anime
class AnimeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Anime

########################################################################################################    Resource para Manga
class MangaResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Manga

########################################################################################################    Resource para TitleAnime
class TitleAnimeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = TitleAnime

########################################################################################################    Resource para TitleManga
class TitleMangaResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = TitleManga

########################################################################################################    Resource para Character
class CharacterResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Character
########################################################################################################    Resource para CharacterNickname
class CharacterNicknameResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = CharacterNickname
########################################################################################################    Resource para Person
class PersonResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Person
########################################################################################################    Resource para PersonNickname
class PersonNicknameResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = PersonNickname
########################################################################################################    Resource para AnimeSong
class AnimeSongResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AnimeSong
########################################################################################################    Resource para AnimeCharacter
class AnimeCharacterResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AnimeCharacter

########################################################################################################    Resource para MangaCharacter
class MangaCharacterResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MangaCharacter

########################################################################################################    Resource para VoiceCharacter
class VoiceCharacterResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = VoiceCharacter

########################################################################################################    Resource para AnimeStaff
class AnimeStaffResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AnimeStaff

########################################################################################################    Resource para AuthorManga
class AuthorMangaResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AuthorManga

########################################################################################################    Resource para MediaRelation
class MediaRelationResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MediaRelation

########################################################################################################    Resource para AnimeImage
class AnimeImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AnimeImage

########################################################################################################    Resource para AnimeImageExtra
class AnimeImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = AnimeImageExtra

########################################################################################################    Resource para MangaImage
class MangaImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MangaImage

########################################################################################################    Resource para MangaImageExtra
class MangaImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = MangaImageExtra

########################################################################################################    Resource para PersonImage
class PersonImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = PersonImage

########################################################################################################    Resource para PersonImageExtra
class PersonImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = PersonImageExtra

########################################################################################################    Resource para CharacterImage
class CharacterImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = CharacterImage
########################################################################################################    Resource para CharacterImageExtra
class CharacterImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = CharacterImageExtra

########################################################################################################    Resource para DataAnime
class DataAnimeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataAnime

########################################################################################################    Resource para DataAnimeCharacters
class DataAnimeCharactersResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataAnimeCharacters

########################################################################################################    Resource para DataAnimePictures
class DataAnimePicturesResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataAnimePictures

########################################################################################################    Resource para DataAnimeStaff
class DataAnimeStaffResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataAnimeStaff

########################################################################################################    Resource para DataManga
class DataMangaResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataManga

########################################################################################################    Resource para DataMangaCharacters
class DataMangaCharactersResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataMangaCharacters

########################################################################################################    Resource para DataMangaPictures
class DataMangaPicturesResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataMangaPictures

########################################################################################################    Resource para DataCharacter
class DataCharacterResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataCharacter

########################################################################################################    Resource para DataCharacterPictures
class DataCharacterPicturesResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataCharacterPictures

########################################################################################################    Resource para DataPerson
class DataPersonResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataPerson

########################################################################################################    Resource para DataPersonPictures
class DataPersonPicturesResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataPersonPictures

########################################################################################################    Resource para DataImageURL
class DataImageURLResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = DataImageURL

########################################################################################################    Resource para Temp_Persons
class Temp_PersonsResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Temp_Persons

########################################################################################################    Resource para Temp_Characters
class Temp_CharactersResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Temp_Characters