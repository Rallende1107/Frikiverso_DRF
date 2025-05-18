####################################################    Templates
class Templates:
    class PasswordRecover:
        FORGET_PASSWORD  = 'users/password_reset/password_reset_form.html'
        RESET_COMPLETE  = 'users/password_reset/password_reset_complete.html'
        RESET_DONE  = 'users/password_reset/password_reset_done.html'
        RESET_CONFIRM  = 'users/password_reset/password_reset_confirm.html'

    class Main:
        INDEX = 'pages/index.html'
        CONTACT = 'pages/contact.html'
        ABOUT = 'pages/about.html'
        TERMS = 'pages/terms.html'
        PRIVACY = 'pages/privacy.html'

    class emailBoddy:
        PASSWORD_RECOVERY = 'emails/body/password_recovery.txt'
        RESET_PASSWORD = 'emails/body/reset_password.txt'
        USER_BLOCKED = 'emails/body/user_blocked.txt'
        USER_ACTIVATED = 'emails/body/user_activated.txt'
        DELETED_USER = 'emails/body/deleted_user.txt'
        PASSWORD_CHANGED = 'emails/body/password_changed.txt'
        CONTACT = 'emails/body/contact.txt'
    class emailSubject:
        PASSWORD_RECOVERY = 'emails/subject/password_recovery.txt'
        RESET_PASSWORD = 'emails/subject/reset_password.txt'
        USER_BLOCKED = 'emails/subject/user_blocked.txt'
        USER_ACTIVATED = 'emails/subject/user_activated.txt'
        DELETED_USER = 'emails/subject/deleted_user.txt'
        PASSWORD_CHANGED = 'emails/subject/password_changed.txt'
        CONTACT = 'emails/subject/contact.txt'
    class Home:
        HOME =  'home/home.html'
    class Users:
        LOGIN  = 'users/user/user_login.html'

        LST = 'users/user/user_list.html'
        ADD = 'users/user/user_form.html'
        UPT = 'users/user/user_update.html'
        DTL = 'users/user/user_detail.html'
        CHANGE_PASS = 'users/user/user_password_change.html'

    class Common:
        class Country:
            LST = 'common/country/country_list.html'
            ADD = 'common/country/country_form.html'
            UPT = 'common/country/country_form.html'
            DTL = 'common/country/country_detail.html'
        class Format:
            LST = 'common/format/format_list.html'
            ADD = 'common/format/format_form.html'
            UPT = 'common/format/format_form.html'
            DTL = 'common/format/format_detail.html'
        class ImageSize:
            LST = 'common/image_size/image_size_list.html'
            ADD = 'common/image_size/image_size_form.html'
            UPT = 'common/image_size/image_size_form.html'
            DTL = 'common/image_size/image_size_detail.html'
        class Language:
            LST = 'common/language/language_list.html'
            ADD = 'common/language/language_form.html'
            UPT = 'common/language/language_form.html'
            DTL = 'common/language/language_detail.html'
        class Person:
            LST = 'common/person/person_list.html'
            ADD = 'common/person/person_form.html'
            UPT = 'common/person/person_form.html'
            DTL = 'common/person/person_detail.html'
        class PersonImage:
            LST = 'common/person_image/person_image_list.html'
            ADD = 'common/person_image/person_image_form.html'
            UPT = 'common/person_image/person_image_form.html'
            DTL = 'common/person_image/person_image_detail.html'
        class PersonImageExtra:
            LST = 'common/person_image_extra/person_image_extra_list.html'
            ADD = 'common/person_image_extra/person_image_extra_form.html'
            UPT = 'common/person_image_extra/person_image_extra_form.html'
            DTL = 'common/person_image_extra/person_image_extra_detail.html'
        class PersonNickname:
            LST = 'common/person_nickname/person_nickname_list.html'
            ADD = 'common/person_nickname/person_nickname_form.html'
            UPT = 'common/person_nickname/person_nickname_form.html'
            DTL = 'common/person_nickname/person_nickname_detail.html'
        class Quality:
            LST = 'common/quality/quality_list.html'
            ADD = 'common/quality/quality_form.html'
            UPT = 'common/quality/quality_form.html'
            DTL = 'common/quality/quality_detail.html'
        class Website:
            LST = 'common/website/website_list.html'
            ADD = 'common/website/website_form.html'
            UPT = 'common/website/website_form.html'
            DTL = 'common/website/website_detail.html'

    class Movie:
        class Company:
            LST = 'movie/company/company_list.html'
            ADD = 'movie/company/company_form.html'
            UPT = 'movie/company/company_form.html'
            DTL = 'movie/company/company_detail.html'
        class Genre:
            LST = 'movie/genre/genre_list.html'
            ADD = 'movie/genre/genre_form.html'
            UPT = 'movie/genre/genre_form.html'
            DTL = 'movie/genre/genre_detail.html'
        class Movie:
            LST = 'movie/movie/movie_list.html'
            ADD = 'movie/movie/movie_form.html'
            UPT = 'movie/movie/movie_form.html'
            DTL = 'movie/movie/movie_detail.html'
        class MovieCast:
            LST = 'movie/movie_cast/movie_cast_list.html'
            ADD = 'movie/movie_cast/movie_cast_form.html'
            UPT = 'movie/movie_cast/movie_cast_form.html'
            DTL = 'movie/movie_cast/movie_cast_detail.html'
        class MovieImage:
            LST = 'movie/movie_image/movie_image_list.html'
            ADD = 'movie/movie_image/movie_image_form.html'
            UPT = 'movie/movie_image/movie_image_form.html'
            DTL = 'movie/movie_image/movie_image_detail.html'
        class MovieImageExtra:
            LST = 'movie/movie_image_extra/movie_image_extra_list.html'
            ADD = 'movie/movie_image_extra/movie_image_extra_form.html'
            UPT = 'movie/movie_image_extra/movie_image_extra_form.html'
            DTL = 'movie/movie_image_extra/movie_image_extra_detail.html'
        class MovieStaff:
            LST = 'movie/movie_staff/movie_staff_list.html'
            ADD = 'movie/movie_staff/movie_staff_form.html'
            UPT = 'movie/movie_staff/movie_staff_form.html'
            DTL = 'movie/movie_staff/movie_staff_detail.html'
        class Rating:
            LST = 'movie/rating/rating_list.html'
            ADD = 'movie/rating/rating_form.html'
            UPT = 'movie/rating/rating_form.html'
            DTL = 'movie/rating/rating_detail.html'
        class Role:
            LST = 'movie/role/role_list.html'
            ADD = 'movie/role/role_form.html'
            UPT = 'movie/role/role_form.html'
            DTL = 'movie/role/role_detail.html'
        class TitleMovie:
            LST = 'movie/title_movie/title_movie_list.html'
            ADD = 'movie/title_movie/title_movie_form.html'
            UPT = 'movie/title_movie/title_movie_form.html'
            DTL = 'movie/title_movie/title_movie_detail.html'
        class Type:
            LST = 'movie/type/type_list.html'
            ADD = 'movie/type/type_form.html'
            UPT = 'movie/type/type_form.html'
            DTL = 'movie/type/type_detail.html'

    class Music:
        class Album:
            LST = 'music/album/album_list.html'
            ADD = 'music/album/album_form.html'
            UPT = 'music/album/album_form.html'
            DTL = 'music/album/album_detail.html'

        class AlbumImage:
            LST = 'music/album_image/album_image_list.html'
            ADD = 'music/album_image/album_image_form.html'
            UPT = 'music/album_image/album_image_form.html'
            DTL = 'music/album_image/album_image_detail.html'

        class AlbumImageExtra:
            LST = 'music/album_image_extra/album_image_extra_list.html'
            ADD = 'music/album_image_extra/album_image_extra_form.html'
            UPT = 'music/album_image_extra/album_image_extra_form.html'
            DTL = 'music/album_image_extra/album_image_extra_detail.html'

        class AlbumType:
            LST = 'music/album_type/album_type_list.html'
            ADD = 'music/album_type/album_type_form.html'
            UPT = 'music/album_type/album_type_form.html'
            DTL = 'music/album_type/album_type_detail.html'

        class Artist:
            LST = 'music/album_type/artist_list.html'
            ADD = 'music/album_type/artist_form.html'
            UPT = 'music/album_type/artist_form.html'
            DTL = 'music/album_type/artist_detail.html'

        class ArtistImage:
            LST = 'music/artist_image/artist_image_list.html'
            ADD = 'music/artist_image/artist_image_form.html'
            UPT = 'music/artist_image/artist_image_form.html'
            DTL = 'music/artist_image/artist_image_detail.html'

        class ArtistImageExtra:
            LST = 'music/artist_image_extra/artist_image_extra_list.html'
            ADD = 'music/artist_image_extra/artist_image_extra_form.html'
            UPT = 'music/artist_image_extra/artist_image_extra_form.html'
            DTL = 'music/artist_image_extra/artist_image_extra_detail.html'

        class ArtistMember:
            LST = 'music/artist_member/artist_member_list.html'
            ADD = 'music/artist_member/artist_member_form.html'
            UPT = 'music/artist_member/artist_member_form.html'
            DTL = 'music/artist_member/artist_member_detail.html'

        class ArtistType:
            LST = 'music/artist_type/artist_type_list.html'
            ADD = 'music/artist_type/artist_type_form.html'
            UPT = 'music/artist_type/artist_type_form.html'
            DTL = 'music/artist_type/artist_type_detail.html'

        class Genre:
            LST = 'music/genre/genre_list.html'
            ADD = 'music/genre/genre_form.html'
            UPT = 'music/genre/genre_form.html'
            DTL = 'music/genre/genre_detail.html'

        class Role:
            LST = 'music/role/role_list.html'
            ADD = 'music/role/role_form.html'
            UPT = 'music/role/role_form.html'
            DTL = 'music/role/role_detail.html'

        class Song:
            LST = 'music/song/song_list.html'
            ADD = 'music/song/song_form.html'
            UPT = 'music/song/song_form.html'
            DTL = 'music/song/song_detail.html'

    class Otaku:
        class Anime:
            LST = 'otaku/anime/anime_list.html'
            ADD = 'otaku/anime/anime_form.html'
            UPT = 'otaku/anime/anime_form.html'
            DTL = 'otaku/anime/anime_deta.html'
        class AnimeCharacter:
            LST = 'otaku/anime_character/anime_character_list.html'
            ADD = 'otaku/anime_character/anime_character_form.html'
            UPT = 'otaku/anime_character/anime_character_form.html'
            DTL = 'otaku/anime_character/anime_character_deta.html'
        class AnimeImage:
            LST = 'otaku/anime_image/anime_image_list.html'
            ADD = 'otaku/anime_image/anime_image_form.html'
            UPT = 'otaku/anime_image/anime_image_form.html'
            DTL = 'otaku/anime_image/anime_image_deta.html'
        class AnimeImageExtra:
            LST = 'otaku/anime_image_extra/anime_image_extra_list.html'
            ADD = 'otaku/anime_image_extra/anime_image_extra_form.html'
            UPT = 'otaku/anime_image_extra/anime_image_extra_form.html'
            DTL = 'otaku/anime_image_extra/anime_image_extra_deta.html'
        class AnimeSong:
            LST = 'otaku/anime_song/anime_song_list.html'
            ADD = 'otaku/anime_song/anime_song_form.html'
            UPT = 'otaku/anime_song/anime_song_form.html'
            DTL = 'otaku/anime_song/anime_song_deta.html'
        class AnimeStaff:
            LST = 'otaku/anime_staff/anime_staff_list.html'
            ADD = 'otaku/anime_staff/anime_staff_form.html'
            UPT = 'otaku/anime_staff/anime_staff_form.html'
            DTL = 'otaku/anime_staff/anime_staff_deta.html'
        class AuthorManga:
            LST = 'otaku/author_manga/author_manga_list.html'
            ADD = 'otaku/author_manga/author_manga_form.html'
            UPT = 'otaku/author_manga/author_manga_form.html'
            DTL = 'otaku/author_manga/author_manga_deta.html'
        class Character:
            LST = 'otaku/character/character_list.html'
            ADD = 'otaku/character/character_form.html'
            UPT = 'otaku/character/character_form.html'
            DTL = 'otaku/character/character_deta.html'
        class CharacterImage:
            LST = 'otaku/character_image/character_image_list.html'
            ADD = 'otaku/character_image/character_image_form.html'
            UPT = 'otaku/character_image/character_image_form.html'
            DTL = 'otaku/character_image/character_image_deta.html'
        class CharacterImageExtra:
            LST = 'otaku/character_image_extra/character_image_extra_list.html'
            ADD = 'otaku/character_image_extra/character_image_extra_form.html'
            UPT = 'otaku/character_image_extra/character_image_extra_form.html'
            DTL = 'otaku/character_image_extra/character_image_extra_deta.html'
        class CharacterNickname:
            LST = 'otaku/character_nickname/character_nickname_list.html'
            ADD = 'otaku/character_nickname/character_nickname_form.html'
            UPT = 'otaku/character_nickname/character_nickname_form.html'
            DTL = 'otaku/character_nickname/character_nickname_deta.html'
        class Demographic:
            LST = 'otaku/demographic/demographic_list.html'
            ADD = 'otaku/demographic/demographic_form.html'
            UPT = 'otaku/demographic/demographic_form.html'
            DTL = 'otaku/demographic/demographic_deta.html'
        class Genre:
            LST = 'otaku/genre/genre_list.html'
            ADD = 'otaku/genre/genre_form.html'
            UPT = 'otaku/genre/genre_form.html'
            DTL = 'otaku/genre/genre_deta.html'
        class Licensor:
            LST = 'otaku/licensor/licensor_list.html'
            ADD = 'otaku/licensor/licensor_form.html'
            UPT = 'otaku/licensor/licensor_form.html'
            DTL = 'otaku/licensor/licensor_deta.html'
        class Manga:
            LST = 'otaku/manga/manga_list.html'
            ADD = 'otaku/manga/manga_form.html'
            UPT = 'otaku/manga/manga_form.html'
            DTL = 'otaku/manga/manga_deta.html'
        class MangaCharacter:
            LST = 'otaku/manga_character/manga_character_list.html'
            ADD = 'otaku/manga_character/manga_character_form.html'
            UPT = 'otaku/manga_character/manga_character_form.html'
            DTL = 'otaku/manga_character/manga_character_deta.html'
        class MangaImage:
            LST = 'otaku/manga_image/manga_image_list.html'
            ADD = 'otaku/manga_image/manga_image_form.html'
            UPT = 'otaku/manga_image/manga_image_form.html'
            DTL = 'otaku/manga_image/manga_image_deta.html'
        class MangaImageExtra:
            LST = 'otaku/manga_image_extra/manga_image_extra_list.html'
            ADD = 'otaku/manga_image_extra/manga_image_extra_form.html'
            UPT = 'otaku/manga_image_extra/manga_image_extra_form.html'
            DTL = 'otaku/manga_image_extra/manga_image_extra_deta.html'
        class MediaRelation:
            LST = 'otaku/media_relation/media_relation_list.html'
            ADD = 'otaku/media_relation/media_relation_form.html'
            UPT = 'otaku/media_relation/media_relation_form.html'
            DTL = 'otaku/media_relation/media_relation_deta.html'
        class Person:
            LST = 'otaku/person/person_list.html'
            ADD = 'otaku/person/person_form.html'
            UPT = 'otaku/person/person_form.html'
            DTL = 'otaku/person/person_deta.html'
        class PersonImage:
            LST = 'otaku/person_image/person_image_list.html'
            ADD = 'otaku/person_image/person_image_form.html'
            UPT = 'otaku/person_image/person_image_form.html'
            DTL = 'otaku/person_image/person_image_deta.html'
        class PersonImageExtra:
            LST = 'otaku/person_image_extra/person_image_extra_list.html'
            ADD = 'otaku/person_image_extra/person_image_extra_form.html'
            UPT = 'otaku/person_image_extra/person_image_extra_form.html'
            DTL = 'otaku/person_image_extra/person_image_extra_deta.html'
        class PersonNickname:
            LST = 'otaku/person_nickname/person_nickname_list.html'
            ADD = 'otaku/person_nickname/person_nickname_form.html'
            UPT = 'otaku/person_nickname/person_nickname_form.html'
            DTL = 'otaku/person_nickname/person_nickname_deta.html'
        class Producer:
            LST = 'otaku/producer/producer_list.html'
            ADD = 'otaku/producer/producer_form.html'
            UPT = 'otaku/producer/producer_form.html'
            DTL = 'otaku/producer/producer_deta.html'
        class Rating:
            LST = 'otaku/rating/rating_list.html'
            ADD = 'otaku/rating/rating_form.html'
            UPT = 'otaku/rating/rating_form.html'
            DTL = 'otaku/rating/rating_deta.html'
        class RelationType:
            LST = 'otaku/relation_type/relation_type_list.html'
            ADD = 'otaku/relation_type/relation_type_form.html'
            UPT = 'otaku/relation_type/relation_type_form.html'
            DTL = 'otaku/relation_type/relation_type_deta.html'
        class Role:
            LST = 'otaku/role/role_list.html'
            ADD = 'otaku/role/role_form.html'
            UPT = 'otaku/role/role_form.html'
            DTL = 'otaku/role/role_deta.html'
        class Season:
            LST = 'otaku/season/season_list.html'
            ADD = 'otaku/season/season_form.html'
            UPT = 'otaku/season/season_form.html'
            DTL = 'otaku/season/season_deta.html'
        class SeasonFull:
            LST = 'otaku/season_full/season_full_list.html'
            ADD = 'otaku/season_full/season_full_form.html'
            UPT = 'otaku/season_full/season_full_form.html'
            DTL = 'otaku/season_full/season_full_deta.html'
        class Serialization:
            LST = 'otaku/serialization/serialization_list.html'
            ADD = 'otaku/serialization/serialization_form.html'
            UPT = 'otaku/serialization/serialization_form.html'
            DTL = 'otaku/serialization/serialization_deta.html'
        class Source:
            LST = 'otaku/source/source_list.html'
            ADD = 'otaku/source/source_form.html'
            UPT = 'otaku/source/source_form.html'
            DTL = 'otaku/source/source_deta.html'
        class Status:
            LST = 'otaku/status/status_list.html'
            ADD = 'otaku/status/status_form.html'
            UPT = 'otaku/status/status_form.html'
            DTL = 'otaku/status/status_deta.html'
        class Studio:
            LST = 'otaku/studio/studio_list.html'
            ADD = 'otaku/studio/studio_form.html'
            UPT = 'otaku/studio/studio_form.html'
            DTL = 'otaku/studio/studio_deta.html'
        class Theme:
            LST = 'otaku/theme/theme_list.html'
            ADD = 'otaku/theme/theme_form.html'
            UPT = 'otaku/theme/theme_form.html'
            DTL = 'otaku/theme/theme_deta.html'
        class TitleAnime:
            LST = 'otaku/title_anime/title_anime_list.html'
            ADD = 'otaku/title_anime/title_anime_form.html'
            UPT = 'otaku/title_anime/title_anime_form.html'
            DTL = 'otaku/title_anime/title_anime_deta.html'
        class TitleManga:
            LST = 'otaku/title_manga/title_manga_list.html'
            ADD = 'otaku/title_manga/title_manga_form.html'
            UPT = 'otaku/title_manga/title_manga_form.html'
            DTL = 'otaku/title_manga/title_manga_deta.html'
        class Type:
            LST = 'otaku/type/type_list.html'
            ADD = 'otaku/type/type_form.html'
            UPT = 'otaku/type/type_form.html'
            DTL = 'otaku/type/type_deta.html'
        class VoiceCharacter:
            LST = 'otaku/voice_character/voice_character_list.html'
            ADD = 'otaku/voice_character/voice_character_form.html'
            UPT = 'otaku/voice_character/voice_character_form.html'
            DTL = 'otaku/voice_character/voice_character_deta.html'
        class Year:
            LST = 'otaku/year/year_list.html'
            ADD = 'otaku/year/year_form.html'
            UPT = 'otaku/year/year_form.html'
            DTL = 'otaku/year/year_deta.html'


            # DataAnime = 'otaku/data/anime'
            # DataAnimeCharacters = 'otaku/data/anime_characters'
            # DataAnimePictures = 'otaku/data/anime_pictures'
            # DataAnimeStaff = 'otaku/data/anime_staff'
            # DataCharacter = 'otaku/data/character'
            # DataCharacterPictures = 'otaku/data/character_pictures'
            # DataImageURL = 'otaku/data/image_url'
            # DataManga = 'otaku/data/manga'
            # DataMangaCharacters = 'otaku/data/manga_characters'
            # DataMangaPictures = 'otaku/data/manga_pictures'
            # DataOtakuPerson = 'otaku/data/person'
            # DataOtakuPersonPictures = 'otaku/data/person_pictures'
            # Temp_Characters = 'otaku/temp/characters'
            # Temp_OtakuPersons = 'otaku/temp/person'

        class DataAnime:
            pass
        class DataAnimeCharacters:
            pass
        class DataAnimePictures:
            pass
        class DataAnimeStaff:
            pass
        class DataCharacter:
            pass
        class DataCharacterPictures:
            pass
        class DataImageURL:
            pass
        class DataManga:
            pass
        class DataMangaCharacters:
            pass
        class DataMangaPictures:
            pass
        class DataOtakuPerson:
            pass
        class DataOtakuPersonPictures:
            pass
        class Temp_Characters:
            pass
        class Temp_OtakuPersons:
            pass

    class Renpy:
        class Censorship:
            LST = 'renpy/censorship/censorship_list.html'
            ADD = 'renpy/censorship/censorship_form.html'
            UPT = 'renpy/censorship/censorship_form.html'
            DTL = 'renpy/censorship/censorship_deta.html'
        class Developer:
            LST = 'renpy/developer/developer_list.html'
            ADD = 'renpy/developer/developer_form.html'
            UPT = 'renpy/developer/developer_form.html'
            DTL = 'renpy/developer/developer_deta.html'
        class DeveloperImage:
            LST = 'renpy/developer_image/developer_image_list.html'
            ADD = 'renpy/developer_image/developer_image_form.html'
            UPT = 'renpy/developer_image/developer_image_form.html'
            DTL = 'renpy/developer_image/developer_image_deta.html'
        class DeveloperImageExtra:
            LST = 'renpy/developer_image_extra/developer_image_extra_list.html'
            ADD = 'renpy/developer_image_extra/developer_image_extra_form.html'
            UPT = 'renpy/developer_image_extra/developer_image_extra_form.html'
            DTL = 'renpy/developer_image_extra/developer_image_extra_deta.html'
        class DeveloperLink:
            LST = 'renpy/developer_link/developer_link_list.html'
            ADD = 'renpy/developer_link/developer_link_form.html'
            UPT = 'renpy/developer_link/developer_link_form.html'
            DTL = 'renpy/developer_link/developer_link_deta.html'
        class Game:
            LST = 'renpy/game/game_list.html'
            ADD = 'renpy/game/game_form.html'
            UPT = 'renpy/game/game_form.html'
            DTL = 'renpy/game/game_deta.html'
        class GameEngine:
            LST = 'renpy/game_engine/game_engine_list.html'
            ADD = 'renpy/game_engine/game_engine_form.html'
            UPT = 'renpy/game_engine/game_engine_form.html'
            DTL = 'renpy/game_engine/game_engine_deta.html'
        class GameImage:
            LST = 'renpy/game_image/game_image_list.html'
            ADD = 'renpy/game_image/game_image_form.html'
            UPT = 'renpy/game_image/game_image_form.html'
            DTL = 'renpy/game_image/game_image_deta.html'
        class GameImageExtra:
            LST = 'renpy/game_image_extra/game_image_extra_list.html'
            ADD = 'renpy/game_image_extra/game_image_extra_form.html'
            UPT = 'renpy/game_image_extra/game_image_extra_form.html'
            DTL = 'renpy/game_image_extra/game_image_extra_deta.html'
        class Genre:
            LST = 'renpy/genre/genre_list.html'
            ADD = 'renpy/genre/genre_form.html'
            UPT = 'renpy/genre/genre_form.html'
            DTL = 'renpy/genre/genre_deta.html'
        class Platform:
            LST = 'renpy/platform/platform_list.html'
            ADD = 'renpy/platform/platform_form.html'
            UPT = 'renpy/platform/platform_form.html'
            DTL = 'renpy/platform/platform_deta.html'
        class Prefix:
            LST = 'renpy/prefix/prefix_list.html'
            ADD = 'renpy/prefix/prefix_form.html'
            UPT = 'renpy/prefix/prefix_form.html'
            DTL = 'renpy/prefix/prefix_deta.html'
        class Publisher:
            LST = 'renpy/publisher/publisher_list.html'
            ADD = 'renpy/publisher/publisher_form.html'
            UPT = 'renpy/publisher/publisher_form.html'
            DTL = 'renpy/publisher/publisher_deta.html'
        class PublisherImage:
            LST = 'renpy/publisher_image/publisher_image_list.html'
            ADD = 'renpy/publisher_image/publisher_image_form.html'
            UPT = 'renpy/publisher_image/publisher_image_form.html'
            DTL = 'renpy/publisher_image/publisher_image_deta.html'
        class PublisherImageExtra:
            LST = 'renpy/publisher_image_extra/publisher_image_extra_list.html'
            ADD = 'renpy/publisher_image_extra/publisher_image_extra_form.html'
            UPT = 'renpy/publisher_image_extra/publisher_image_extra_form.html'
            DTL = 'renpy/publisher_image_extra/publisher_image_extra_deta.html'
        class PublisherLink:
            LST = 'renpy/publisher_link/publisher_link_list.html'
            ADD = 'renpy/publisher_link/publisher_link_form.html'
            UPT = 'renpy/publisher_link/publisher_link_form.html'
            DTL = 'renpy/publisher_link/publisher_link_deta.html'
        class Status:
            LST = 'renpy/status/status_list.html'
            ADD = 'renpy/status/status_form.html'
            UPT = 'renpy/status/status_form.html'
            DTL = 'renpy/status/status_deta.html'
        class TitleGame:
            LST = 'renpy/title_game/title_game_list.html'
            ADD = 'renpy/title_game/title_game_form.html'
            UPT = 'renpy/title_game/title_game_form.html'
            DTL = 'renpy/title_game/title_game_deta.html'
        class Translator:
            LST = 'renpy/translator/translator_list.html'
            ADD = 'renpy/translator/translator_form.html'
            UPT = 'renpy/translator/translator_form.html'
            DTL = 'renpy/translator/translator_deta.html'
        class TranslatorImage:
            LST = 'renpy/translator_image/translator_image_list.html'
            ADD = 'renpy/translator_image/translator_image_form.html'
            UPT = 'renpy/translator_image/translator_image_form.html'
            DTL = 'renpy/translator_image/translator_image_deta.html'
        class TranslatorImageExtra:
            LST = 'renpy/translator_image_extra/translator_image_extra_list.html'
            ADD = 'renpy/translator_image_extra/translator_image_extra_form.html'
            UPT = 'renpy/translator_image_extra/translator_image_extra_form.html'
            DTL = 'renpy/translator_image_extra/translator_image_extra_deta.html'
        class TranslatorLink:
            LST = 'renpy/translator_link/translator_link_list.html'
            ADD = 'renpy/translator_link/translator_link_form.html'
            UPT = 'renpy/translator_link/translator_link_form.html'
            DTL = 'renpy/translator_link/translator_link_deta.html'
        class GameData:
            LST = 'renpy/game_data/game_data_list.html'
            ADD = 'renpy/game_data/game_data_form.html'
            UPT = 'renpy/game_data/game_data_form.html'
            DTL = 'renpy/game_data/game_data_deta.html'

    class Serie:
        class Company:
            LST = 'serie/company/company_list.html'
            ADD = 'serie/company/company_form.html'
            UPT = 'serie/company/company_form.html'
            DTL = 'serie/company/company_deta.html'
        class Genre:
            LST = 'serie/genre/genre_list.html'
            ADD = 'serie/genre/genre_form.html'
            UPT = 'serie/genre/genre_form.html'
            DTL = 'serie/genre/genre_deta.html'
        class Rating:
            LST = 'serie/rating/rating_list.html'
            ADD = 'serie/rating/rating_form.html'
            UPT = 'serie/rating/rating_form.html'
            DTL = 'serie/rating/rating_deta.html'

        class Role:
            LST = 'serie/role/role_list.html'
            ADD = 'serie/role/role_form.html'
            UPT = 'serie/role/role_form.html'
            DTL = 'serie/role/role_deta.html'

        class Serie:
            LST = 'serie/serie/serie_list.html'
            ADD = 'serie/serie/serie_form.html'
            UPT = 'serie/serie/serie_form.html'
            DTL = 'serie/serie/serie_deta.html'

        class SerieCast:
            LST = 'serie/serie_cast/serie_cast_list.html'
            ADD = 'serie/serie_cast/serie_cast_form.html'
            UPT = 'serie/serie_cast/serie_cast_form.html'
            DTL = 'serie/serie_cast/serie_cast_deta.html'

        class SerieImage:
            LST = 'serie/serie_image/serie_image_list.html'
            ADD = 'serie/serie_image/serie_image_form.html'
            UPT = 'serie/serie_image/serie_image_form.html'
            DTL = 'serie/serie_image/serie_image_deta.html'

        class SerieImageExtra:
            LST = 'serie/serie_image_extra/serie_image_extra_list.html'
            ADD = 'serie/serie_image_extra/serie_image_extra_form.html'
            UPT = 'serie/serie_image_extra/serie_image_extra_form.html'
            DTL = 'serie/serie_image_extra/serie_image_extra_deta.html'

        class SerieStaff:
            LST = 'serie/serie_staff/serie_staff_list.html'
            ADD = 'serie/serie_staff/serie_staff_form.html'
            UPT = 'serie/serie_staff/serie_staff_form.html'
            DTL = 'serie/serie_staff/serie_staff_deta.html'

        class TitleSerie:
            LST = 'serie/title_serie/title_serie_list.html'
            ADD = 'serie/title_serie/title_serie_form.html'
            UPT = 'serie/title_serie/title_serie_form.html'
            DTL = 'serie/title_serie/title_serie_deta.html'

        class Type:
            LST = 'serie/type/type_list.html'
            ADD = 'serie/type/type_form.html'
            UPT = 'serie/type/type_form.html'
            DTL = 'serie/type/type_deta.html'

####################################################    URLS
class URLS:
    class Main:
        INDEX = 'pages_app:index'
        CONTAC = 'pages_app:contac'
        TERMS = 'pages_app:terms'

    class PasswordRecover:
        FORGET_PASSWORD  = 'users_app:forget_password'
        FORGET_PASSWORD_DONE  = 'users_app:forget_password_done'
        PASSWORD_RESET_CONFIRM  = 'users_app:password_reset_confirm'
        PASSWORD_RESET_COMPLETE  = 'users_app:password_reset_complete'

    class Home:
        COMMON =    'common_app:home'
        MOVIE =     'movie_app:home'
        MUSIC =     'music_app:home'
        OTAKU =     'otaku_app:home'
        RENPY =     'renpy_app:home'
        SERIE =     'serie_app :home'
        USERS =     'users_app:home'

    class Users:
        LOGIN =     'users_app:login'
        LST =       'users_app:users_list'
        ADD =       'users_app:users_create'
        UPD =       'users_app:users_update'
        DTL =       'users_app:users_detail'
        ADD_SUPER = 'users_app:superuser_create'
        ADD_STAFF = 'users_app:staffuser_create'

    class Common:
        class Country:
            LST = 'common_app:country_list'
            ADD = 'common_app:country_create'
            UPD = 'common_app:country_update'
            DTL = 'common_app:country_detail'

        class Format:
            LST = 'common_app:format_list'
            ADD = 'common_app:format_create'
            UPD = 'common_app:format_update'
            DTL = 'common_app:format_detail'

        class ImageSize:
            LST = 'common_app:image_size_list'
            ADD = 'common_app:image_size_create'
            UPD = 'common_app:image_size_update'
            DTL = 'common_app:image_size_detail'

        class Language:
            LST = 'common_app:language_list'
            ADD = 'common_app:language_create'
            UPD = 'common_app:language_update'
            DTL = 'common_app:language_detail'

        class Person:
            LST = 'common_app:person_list'
            ADD = 'common_app:person_create'
            UPD = 'common_app:person_update'
            DTL = 'common_app:person_detail'

        class PersonImage:
            LST = 'common_app:person_image_list'
            ADD = 'common_app:person_image_create'
            UPD = 'common_app:person_image_update'
            DTL = 'common_app:person_image_detail'

        class PersonImageExtra:
            LST = 'common_app:person_image_extra_list'
            ADD = 'common_app:person_image_extra_create'
            UPD = 'common_app:person_image_extra_update'
            DTL = 'common_app:person_image_extra_detail'

        class PersonNickname:
            LST = 'common_app:person_nickname_list'
            ADD = 'common_app:person_nickname_create'
            UPD = 'common_app:person_nickname_update'
            DTL = 'common_app:person_nickname_detail'

        class Quality:
            LST = 'common_app:quality_list'
            ADD = 'common_app:quality_create'
            UPD = 'common_app:quality_update'
            DTL = 'common_app:quality_detail'

        class Website:
            LST = 'common_app:website_list'
            ADD = 'common_app:website_create'
            UPD = 'common_app:website_update'
            DTL = 'common_app:website_detail'

    class Movie:
        class Company:
            LST = 'movie_app:company_list'
            ADD = 'movie_app:company_create'
            UPD = 'movie_app:company_update'
            DTL = 'movie_app:company_detail'

        class Genre:
            LST = 'movie_app:genre_list'
            ADD = 'movie_app:genre_create'
            UPD = 'movie_app:genre_update'
            DTL = 'movie_app:genre_detail'

        class Movie:
            LST = 'movie_app:movie_list'
            ADD = 'movie_app:movie_create'
            UPD = 'movie_app:movie_update'
            DTL = 'movie_app:movie_detail'

        class MovieCast:
            LST = 'movie_app:movie_cast_list'
            ADD = 'movie_app:movie_cast_create'
            UPD = 'movie_app:movie_cast_update'
            DTL = 'movie_app:movie_cast_detail'

        class MovieImage:
            LST = 'movie_app:movie_image_list'
            ADD = 'movie_app:movie_image_create'
            UPD = 'movie_app:movie_image_update'
            DTL = 'movie_app:movie_image_detail'

        class MovieImageExtra:
            LST = 'movie_app:movie_image_extra_list'
            ADD = 'movie_app:movie_image_extra_create'
            UPD = 'movie_app:movie_image_extra_update'
            DTL = 'movie_app:movie_image_extra_detail'

        class MovieStaff:
            LST = 'movie_app:movie_image_staff_list'
            ADD = 'movie_app:movie_image_staff_create'
            UPD = 'movie_app:movie_image_staff_update'
            DTL = 'movie_app:movie_image_staff_detail'

        class Rating:
            LST = 'movie_app:rating_list'
            ADD = 'movie_app:rating_create'
            UPD = 'movie_app:rating_update'
            DTL = 'movie_app:rating_detail'

        class Role:
            LST = 'movie_app:role_list'
            ADD = 'movie_app:role_create'
            UPD = 'movie_app:role_update'
            DTL = 'movie_app:role_detail'

        class TitleMovie:
            LST = 'movie_app:title_movie_list'
            ADD = 'movie_app:title_movie_create'
            UPD = 'movie_app:title_movie_update'
            DTL = 'movie_app:title_movie_detail'

        class Type:
            LST = 'movie_app:type_list'
            ADD = 'movie_app:type_create'
            UPD = 'movie_app:type_update'
            DTL = 'movie_app:type_detail'

    class Music:
        class Album:
            LST = 'music_app:album_list'
            ADD = 'music_app:album_create'
            UPD = 'music_app:album_update'
            DTL = 'music_app:album_detail'

        class AlbumImage:
            LST = 'music_app:album_image_list'
            ADD = 'music_app:album_image_create'
            UPD = 'music_app:album_image_update'
            DTL = 'music_app:album_image_detail'

        class AlbumImageExtra:
            LST = 'music_app:album_image_extra_list'
            ADD = 'music_app:album_image_extra_create'
            UPD = 'music_app:album_image_extra_update'
            DTL = 'music_app:album_image_extra_detail'

        class AlbumType:
            LST = 'music_app:album_image_type_list'
            ADD = 'music_app:album_image_type_create'
            UPD = 'music_app:album_image_type_update'
            DTL = 'music_app:album_image_type_detail'

        class Artist:
            LST = 'music_app:artist_list'
            ADD = 'music_app:artist_create'
            UPD = 'music_app:artist_update'
            DTL = 'music_app:artist_detail'

        class ArtistImage:
            LST = 'music_app:artist_image_list'
            ADD = 'music_app:artist_image_create'
            UPD = 'music_app:artist_image_update'
            DTL = 'music_app:artist_image_detail'

        class ArtistImageExtra:
            LST = 'music_app:artist_image_extra_list'
            ADD = 'music_app:artist_image_extra_create'
            UPD = 'music_app:artist_image_extra_update'
            DTL = 'music_app:artist_image_extra_detail'

        class ArtistMember:
            LST = 'music_app:artist_member_list'
            ADD = 'music_app:artist_member_create'
            UPD = 'music_app:artist_member_update'
            DTL = 'music_app:artist_member_detail'

        class ArtistType:
            LST = 'music_app:artist_type_list'
            ADD = 'music_app:artist_type_create'
            UPD = 'music_app:artist_type_update'
            DTL = 'music_app:artist_type_detail'

        class Genre:
            LST = 'music_app:genre_list'
            ADD = 'music_app:genre_create'
            UPD = 'music_app:genre_update'
            DTL = 'music_app:genre_detail'

        class Role:
            LST = 'music_app:role_list'
            ADD = 'music_app:role_create'
            UPD = 'music_app:role_update'
            DTL = 'music_app:role_detail'

        class Song:
            LST = 'music_app:song_list'
            ADD = 'music_app:song_create'
            UPD = 'music_app:song_update'
            DTL = 'music_app:song_detail'

    class Otaku:
        class Load:
            ANIME = 'otaku_app:anime_load'
            MANGA = 'otaku_app:manga_load'
            PERSON = 'otaku_app:person_load'
            CHARACTER = 'otaku_app:character_load'

        class Anime:
            LST = 'otaku_app:anime_list'
            ADD = 'otaku_app:anime_create'
            UPD = 'otaku_app:anime_update'
            DTL = 'otaku_app:anime_detail'

        class AnimeCharacter:
            LST = 'otaku_app:anime_character_list'
            ADD = 'otaku_app:anime_character_create'
            UPD = 'otaku_app:anime_character_update'
            DTL = 'otaku_app:anime_character_detail'

        class AnimeImage:
            LST = 'otaku_app:anime_image_list'
            ADD = 'otaku_app:anime_image_create'
            UPD = 'otaku_app:anime_image_update'
            DTL = 'otaku_app:anime_image_detail'

        class AnimeImageExtra:
            LST = 'otaku_app:anime_image_extra_list'
            ADD = 'otaku_app:anime_image_extra_create'
            UPD = 'otaku_app:anime_image_extra_update'
            DTL = 'otaku_app:anime_image_extra_detail'

        class AnimeSong:
            LST = 'otaku_app:anime_image_song_list'
            ADD = 'otaku_app:anime_image_song_create'
            UPD = 'otaku_app:anime_image_song_update'
            DTL = 'otaku_app:anime_image_song_detail'

        class AnimeStaff:
            LST = 'otaku_app:anime_staff_list'
            ADD = 'otaku_app:anime_staff_create'
            UPD = 'otaku_app:anime_staff_update'
            DTL = 'otaku_app:anime_staff_detail'

        class AuthorManga:
            LST = 'otaku_app:author_manga_list'
            ADD = 'otaku_app:author_manga_create'
            UPD = 'otaku_app:author_manga_update'
            DTL = 'otaku_app:author_manga_detail'

        class Character:
            LST = 'otaku_app:character_list'
            ADD = 'otaku_app:character_create'
            UPD = 'otaku_app:character_update'
            DTL = 'otaku_app:character_detail'

        class CharacterImage:
            LST = 'otaku_app:character_image_list'
            ADD = 'otaku_app:character_image_create'
            UPD = 'otaku_app:character_image_update'
            DTL = 'otaku_app:character_image_detail'

        class CharacterImageExtra:
            LST = 'otaku_app:character_image_extra_list'
            ADD = 'otaku_app:character_image_extra_create'
            UPD = 'otaku_app:character_image_extra_update'
            DTL = 'otaku_app:character_image_extra_detail'

        class CharacterNickname:
            LST = 'otaku_app:character_nickname_list'
            ADD = 'otaku_app:character_nickname_create'
            UPD = 'otaku_app:character_nickname_update'
            DTL = 'otaku_app:character_nickname_detail'

        class Demographic:
            LST = 'otaku_app:demographic_list'
            ADD = 'otaku_app:demographic_create'
            UPD = 'otaku_app:demographic_update'
            DTL = 'otaku_app:demographic_detail'

        class Genre:
            LST = 'otaku_app:genre_list'
            ADD = 'otaku_app:genre_create'
            UPD = 'otaku_app:genre_update'
            DTL = 'otaku_app:genre_detail'

        class Licensor:
            LST = 'otaku_app:licensor_list'
            ADD = 'otaku_app:licensor_create'
            UPD = 'otaku_app:licensor_update'
            DTL = 'otaku_app:licensor_detail'

        class Manga:
            LST = 'otaku_app:manga_list'
            ADD = 'otaku_app:manga_create'
            UPD = 'otaku_app:manga_update'
            DTL = 'otaku_app:manga_detail'

        class MangaCharacter:
            LST = 'otaku_app:manga_character_list'
            ADD = 'otaku_app:manga_character_create'
            UPD = 'otaku_app:manga_character_update'
            DTL = 'otaku_app:manga_character_detail'

        class MangaImage:
            LST = 'otaku_app:manga_image_list'
            ADD = 'otaku_app:manga_image_create'
            UPD = 'otaku_app:manga_image_update'
            DTL = 'otaku_app:manga_image_detail'

        class MangaImageExtra:
            LST = 'otaku_app:manga_image_extra_list'
            ADD = 'otaku_app:manga_image_extra_create'
            UPD = 'otaku_app:manga_image_extra_update'
            DTL = 'otaku_app:manga_image_extra_detail'

        class MediaRelation:
            LST = 'otaku_app:media_relation_list'
            ADD = 'otaku_app:media_relation_create'
            UPD = 'otaku_app:media_relation_update'
            DTL = 'otaku_app:media_relation_detail'

        class Person:
            LST = 'otaku_app:person_list'
            ADD = 'otaku_app:person_create'
            UPD = 'otaku_app:person_update'
            DTL = 'otaku_app:person_detail'

        class PersonImage:
            LST = 'otaku_app:person_image_list'
            ADD = 'otaku_app:person_image_create'
            UPD = 'otaku_app:person_image_update'
            DTL = 'otaku_app:person_image_detail'

        class PersonImageExtra:
            LST = 'otaku_app:person_image_extra_list'
            ADD = 'otaku_app:person_image_extra_create'
            UPD = 'otaku_app:person_image_extra_update'
            DTL = 'otaku_app:person_image_extra_detail'

        class PersonNickname:
            LST = 'otaku_app:person_nickname_list'
            ADD = 'otaku_app:person_nickname_create'
            UPD = 'otaku_app:person_nickname_update'
            DTL = 'otaku_app:person_nickname_detail'

        class Producer:
            LST = 'otaku_app:producer_list'
            ADD = 'otaku_app:producer_create'
            UPD = 'otaku_app:producer_update'
            DTL = 'otaku_app:producer_detail'

        class Rating:
            LST = 'otaku_app:rating_list'
            ADD = 'otaku_app:rating_create'
            UPD = 'otaku_app:rating_update'
            DTL = 'otaku_app:rating_detail'

        class RelationType:
            LST = 'otaku_app:relation_type_list'
            ADD = 'otaku_app:relation_type_create'
            UPD = 'otaku_app:relation_type_update'
            DTL = 'otaku_app:relation_type_detail'

        class Role:
            LST = 'otaku_app:role_list'
            ADD = 'otaku_app:role_create'
            UPD = 'otaku_app:role_update'
            DTL = 'otaku_app:role_detail'

        class Season:
            LST = 'otaku_app:season_list'
            ADD = 'otaku_app:season_create'
            UPD = 'otaku_app:season_update'
            DTL = 'otaku_app:season_detail'

        class SeasonFull:
            LST = 'otaku_app:season_full_list'
            ADD = 'otaku_app:season_full_create'
            UPD = 'otaku_app:season_full_update'
            DTL = 'otaku_app:season_full_detail'

        class Serialization:
            LST = 'otaku_app:serialization_list'
            ADD = 'otaku_app:serialization_create'
            UPD = 'otaku_app:serialization_update'
            DTL = 'otaku_app:serialization_detail'

        class Source:
            LST = 'otaku_app:source_list'
            ADD = 'otaku_app:source_create'
            UPD = 'otaku_app:source_update'
            DTL = 'otaku_app:source_detail'

        class Status:
            LST = 'otaku_app:status_list'
            ADD = 'otaku_app:status_create'
            UPD = 'otaku_app:status_update'
            DTL = 'otaku_app:status_detail'

        class Studio:
            LST = 'otaku_app:studio_list'
            ADD = 'otaku_app:studio_create'
            UPD = 'otaku_app:studio_update'
            DTL = 'otaku_app:studio_detail'

        class Theme:
            LST = 'otaku_app:theme_list'
            ADD = 'otaku_app:theme_create'
            UPD = 'otaku_app:theme_update'
            DTL = 'otaku_app:theme_detail'

        class TitleAnime:
            LST = 'otaku_app:title_anime_list'
            ADD = 'otaku_app:title_anime_create'
            UPD = 'otaku_app:title_anime_update'
            DTL = 'otaku_app:title_anime_detail'

        class TitleManga:
            LST = 'otaku_app:title_manga_list'
            ADD = 'otaku_app:title_manga_create'
            UPD = 'otaku_app:title_manga_update'
            DTL = 'otaku_app:title_manga_detail'

        class Type:
            LST = 'otaku_app:type_list'
            ADD = 'otaku_app:type_create'
            UPD = 'otaku_app:type_update'
            DTL = 'otaku_app:type_detail'

        class VoiceCharacter:
            LST = 'otaku_app:voice_character_list'
            ADD = 'otaku_app:voice_character_create'
            UPD = 'otaku_app:voice_character_update'
            DTL = 'otaku_app:voice_character_detail'

        class Year:
            LST = 'otaku_app:year_list'
            ADD = 'otaku_app:year_create'
            UPD = 'otaku_app:year_update'
            DTL = 'otaku_app:year_detail'

        class Temp_Characters:
            pass

        class Temp_OtakuPersons:
            pass

        class DataAnime:
            pass

        class DataAnimeCharacters:
            pass

        class DataAnimePictures:
            pass

        class DataAnimeStaff:
            pass

        class DataCharacter:
            pass

        class DataCharacterPictures:
            pass

        class DataImageURL:
            pass

        class DataManga:
            pass

        class DataMangaCharacters:
            pass

        class DataMangaPictures:
            pass

        class DataOtakuPerson:
            pass

        class DataOtakuPersonPictures:
            pass

    class Renpy:
        class Censorship:
            LST = 'renpy_app:censorship_list'
            ADD = 'renpy_app:censorship_create'
            UPD = 'renpy_app:censorship_update'
            DTL = 'renpy_app:censorship_detail'

        class Developer:
            LST = 'renpy_app:developer_list'
            ADD = 'renpy_app:developer_create'
            UPD = 'renpy_app:developer_update'
            DTL = 'renpy_app:developer_detail'

        class DeveloperImage:
            LST = 'renpy_app:developer_image_list'
            ADD = 'renpy_app:developer_image_create'
            UPD = 'renpy_app:developer_image_update'
            DTL = 'renpy_app:developer_image_detail'

        class DeveloperImageExtra:
            LST = 'renpy_app:developer_image_extra_list'
            ADD = 'renpy_app:developer_image_extra_create'
            UPD = 'renpy_app:developer_image_extra_update'
            DTL = 'renpy_app:developer_image_extra_detail'

        class DeveloperLink:
            LST = 'renpy_app:developer_link_list'
            ADD = 'renpy_app:developer_link_create'
            UPD = 'renpy_app:developer_link_update'
            DTL = 'renpy_app:developer_link_detail'

        class Game:
            LST = 'renpy_app:game_list'
            ADD = 'renpy_app:game_create'
            UPD = 'renpy_app:game_update'
            DTL = 'renpy_app:game_detail'

        class GameEngine:
            LST = 'renpy_app:game_engine_list'
            ADD = 'renpy_app:game_engine_create'
            UPD = 'renpy_app:game_engine_update'
            DTL = 'renpy_app:game_engine_detail'

        class GameImage:
            LST = 'renpy_app:game_image_list'
            ADD = 'renpy_app:game_image_create'
            UPD = 'renpy_app:game_image_update'
            DTL = 'renpy_app:game_image_detail'

        class GameImageExtra:
            LST = 'renpy_app:game_image_extra_list'
            ADD = 'renpy_app:game_image_extra_create'
            UPD = 'renpy_app:game_image_extra_update'
            DTL = 'renpy_app:game_image_extra_detail'

        class Genre:
            LST = 'renpy_app:genre_list'
            ADD = 'renpy_app:genre_create'
            UPD = 'renpy_app:genre_update'
            DTL = 'renpy_app:genre_detail'

        class Platform:
            LST = 'renpy_app:platform_list'
            ADD = 'renpy_app:platform_create'
            UPD = 'renpy_app:platform_update'
            DTL = 'renpy_app:platform_detail'

        class Prefix:
            LST = 'renpy_app:prefix_list'
            ADD = 'renpy_app:prefix_create'
            UPD = 'renpy_app:prefix_update'
            DTL = 'renpy_app:prefix_detail'

        class Publisher:
            LST = 'renpy_app:publisher_list'
            ADD = 'renpy_app:publisher_create'
            UPD = 'renpy_app:publisher_update'
            DTL = 'renpy_app:publisher_detail'

        class PublisherImage:
            LST = 'renpy_app:publisher_image_list'
            ADD = 'renpy_app:publisher_image_create'
            UPD = 'renpy_app:publisher_image_update'
            DTL = 'renpy_app:publisher_image_detail'

        class PublisherImageExtra:
            LST = 'renpy_app:publisher_image_extra_list'
            ADD = 'renpy_app:publisher_image_extra_create'
            UPD = 'renpy_app:publisher_image_extra_update'
            DTL = 'renpy_app:publisher_image_extra_detail'

        class PublisherLink:
            LST = 'renpy_app:publisher_link_list'
            ADD = 'renpy_app:publisher_link_create'
            UPD = 'renpy_app:publisher_link_update'
            DTL = 'renpy_app:publisher_link_detail'

        class Status:
            LST = 'renpy_app:status_list'
            ADD = 'renpy_app:status_create'
            UPD = 'renpy_app:status_update'
            DTL = 'renpy_app:status_detail'

        class TitleGame:
            LST = 'renpy_app:title_game_list'
            ADD = 'renpy_app:title_game_create'
            UPD = 'renpy_app:title_game_update'
            DTL = 'renpy_app:title_game_detail'

        class Translator:
            LST = 'renpy_app:translator_list'
            ADD = 'renpy_app:translator_create'
            UPD = 'renpy_app:translator_update'
            DTL = 'renpy_app:translator_detail'

        class TranslatorImage:
            LST = 'renpy_app:translator_image_list'
            ADD = 'renpy_app:translator_image_create'
            UPD = 'renpy_app:translator_image_update'
            DTL = 'renpy_app:translator_image_detail'

        class TranslatorImageExtra:
            LST = 'renpy_app:translator_image_extra_list'
            ADD = 'renpy_app:translator_image_extra_create'
            UPD = 'renpy_app:translator_image_extra_update'
            DTL = 'renpy_app:translator_image_extra_detail'

        class TranslatorLink:
            LST = 'renpy_app:translator_link_list'
            ADD = 'renpy_app:translator_link_create'
            UPD = 'renpy_app:translator_link_update'
            DTL = 'renpy_app:translator_link_detail'

        class F95GameFetchStatus:
            LST = 'renpy_app:game_data_list'
            ADD = 'renpy_app:game_data_create'
            UPD = 'renpy_app:game_data_update'
            DTL = 'renpy_app:game_data_detail'

    class Serie:
        class Company:
            LST = 'serie_app :company_list'
            ADD = 'serie_app :company_create'
            UPD = 'serie_app :company_update'
            DTL = 'serie_app :company_detail'

        class Genre:
            LST = 'serie_app :genre_list'
            ADD = 'serie_app :genre_create'
            UPD = 'serie_app :genre_update'
            DTL = 'serie_app :genre_detail'

        class Rating:
            LST = 'serie_app :rating_list'
            ADD = 'serie_app :rating_create'
            UPD = 'serie_app :rating_update'
            DTL = 'serie_app :rating_detail'

        class Role:
            LST = 'serie_app :role_list'
            ADD = 'serie_app :role_create'
            UPD = 'serie_app :role_update'
            DTL = 'serie_app :role_detail'

        class Serie:
            LST = 'serie_app :serie_list'
            ADD = 'serie_app :serie_create'
            UPD = 'serie_app :serie_update'
            DTL = 'serie_app :serie_detail'

        class SerieCast:
            LST = 'serie_app :serie_cast_list'
            ADD = 'serie_app :serie_cast_create'
            UPD = 'serie_app :serie_cast_update'
            DTL = 'serie_app :serie_cast_detail'

        class SerieImage:
            LST = 'serie_app :serie_image_list'
            ADD = 'serie_app :serie_image_create'
            UPD = 'serie_app :serie_image_update'
            DTL = 'serie_app :serie_image_detail'

        class SerieImageExtra:
            LST = 'serie_app :serie_image_extra_list'
            ADD = 'serie_app :serie_image_extra_create'
            UPD = 'serie_app :serie_image_extra_update'
            DTL = 'serie_app :serie_image_extra_detail'

        class SerieStaff:
            LST = 'serie_app :serie_staff_list'
            ADD = 'serie_app :serie_staff_create'
            UPD = 'serie_app :serie_staff_update'
            DTL = 'serie_app :serie_staff_detail'

        class TitleSerie:
            LST = 'serie_app :title_serie_list'
            ADD = 'serie_app :title_serie_create'
            UPD = 'serie_app :title_serie_update'
            DTL = 'serie_app :title_serie_detail'

        class Type:
            LST = 'serie_app :type_list'
            ADD = 'serie_app :type_create'
            UPD = 'serie_app :type_update'
            DTL = 'serie_app :type_detail'

####################################################    CSSBackground
class CSSBackground:
    class Home:
        COMMON =                    'bg-home-common'
        MOVIE =                     'bg-home-movie'
        MUSIC =                     'bg-home-music'
        OTAKU =                     'bg-home-otaku'
        OTAKU_ANIME =               'bg-home-otaku-anime'
        OTAKU_DATA =                'bg-home-otaku-data'
        OTAKU_IMAGEN =              'bg-home-otaku-imagen'
        OTAKU_MANGA =               'bg-home-otaku-manga'
        OTAKU_PERSON_CHARACTER =    'bg-home-otaku-person_character'
        OTAKU_RELATION =            'bg-home-otaku-relation'
        RENPY  =                    'bg-home-renpy'
        SERIE  =                    'bg-home-serie'

    class Users:
        USER = 'bg-users-user'

    class Common:
        COUNTRY =               'bg-common-country'
        FORMAT =                'bg-common-format'
        IMAGE_SIZE =            'bg-common-image_size'
        LANGUAGE =              'bg-common-language'
        PERSON =                'bg-common-person'
        PERSON_IMAGE =          'bg-common-person_image'
        PERSON_IMAGE_EXTRA =    'bg-common-person_image_extra'
        PERSON_NICKNAME =       'bg-common-person_nickname'
        QUALITY =               'bg-common-quality'
        WEBSITE =               'bg-common-website'

    class Movie:
        GENRE =             'bg-movie-genre'
        TYPE =              'bg-movie-type'
        ROLE =              'bg-movie-role'
        RATING =            'bg-movie-rating'
        COMPANY =           'bg-movie-company'
        MOVIE =             'bg-movie-movie'
        TITLE_MOVIE =       'bg-movie-title_movie'
        MOVIE_STAFF =       'bg-movie-movie_staff'
        MOVIE_CAST =        'bg-movie-movie_cast'
        MOVIE_IMAGE =       'bg-movie-movie_image'
        MOVIE_IMAGE_EXTRA = 'bg-movie-movie_image_extra'

    class Music:
        GENRE =                 'bg-music-genre'
        ROLE =                  'bg-music-role'
        ALBUM_TYPE =            'bg-music-album_type'
        ARTIST_TYPE =           'bg-music-artist_type'
        ARTIST =                'bg-music-artist'
        ARTIST_MEMBER =         'bg-music-artist_member'
        ALBUM =                 'bg-music-album'
        SONG =                  'bg-music-song'
        ALBUM_IMAGE =           'bg-music-album_image'
        ALBUM_IMAGE_EXTRA =     'bg-music-album_image_extra'
        ARTIST_IMAGE =          'bg-music-artist_image'
        ARTIST_IMAGE_EXTRA =    'bg-music-artist_image_extra'

    class Otaku:
        ROLE =                      'bg-otaku-role'
        YEAR =                      'bg-otaku-year'
        GENRE =                     'bg-otaku-genre'
        THEME =                     'bg-otaku-theme'
        DEMOGRAPHIC =               'bg-otaku-demographic'
        TYPE =                      'bg-otaku-type'
        RATING =                    'bg-otaku-rating'
        SEASON =                    'bg-otaku-season'
        STATUS =                    'bg-otaku-status'
        SOURCE =                    'bg-otaku-source'
        RELATION_TYPE =             'bg-otaku-relation_type'
        SEASON_FULL =               'bg-otaku-season_full'
        PRODUCER =                  'bg-otaku-producer'
        LICENSOR =                  'bg-otaku-licensor'
        STUDIO =                    'bg-otaku-studio'
        SERIALIZATION =             'bg-otaku-serialization'
        ANIME =                     'bg-otaku-anime'
        MANGA =                     'bg-otaku-manga'
        TITLE_ANIME =               'bg-otaku-title_anime'
        TITLE_MANGA =               'bg-otaku-title_manga'
        CHARACTER =                 'bg-otaku-character'
        CHARACTER_NICKNAME =        'bg-otaku-character_nickname'
        PERSON =                    'bg-otaku-person'
        PERSON_NICKNAME =           'bg-otaku-person_nickname'
        SONG =                      'bg-otaku-song'
        SONG_OP =                   'bg-otaku-song_OP'
        SONG_ED =                   'bg-otaku-song_ED'
        SONG_IN =                   'bg-otaku-song_IN'
        ANIME_CHARACTER =           'bg-otaku-anime_character'
        MANGA_CHARACTER =           'bg-otaku-manga_character'
        VOICE_CHARACTER =           'bg-otaku-voice_character'
        ANIME_STAFF =               'bg-otaku-anime_staff'
        AUTHOR_MANGA =              'bg-otaku-author_manga'
        MEDIA_RELATION =            'bg-otaku-media_relation'
        MEDIA_RELATION_ANIME =      'bg-otaku-media_relation_anime'
        MEDIA_RELATION_MANGA =      'bg-otaku-media_relation_manga'
        ANIME_IMAGE =               'bg-otaku-anime_image'
        ANIME_IMAGE_EXTRA =         'bg-otaku-anime_image_extra'
        MANGA_IMAGE =               'bg-otaku-manga_image'
        MANGA_IMAGE_EXTRA =         'bg-otaku-manga_image_extra'
        PERSON_IMAGE =              'bg-otaku-person_image'
        PERSON_IMAGE_EXTRA =        'bg-otaku-person_image_extra'
        CHARACTER_IMAGE =           'bg-otaku-character_image'
        CHARACTER_IMAGE_EXTRA =     'bg-otaku-character_image_extra'
        DATA_ANIME =                'bg-otaku-data_anime'
        DATA_ANIME_CHARACTERS =     'bg-otaku-data_anime_characters'
        DATA_ANIME_PICTURES =       'bg-otaku-data_anime_pictures'
        DATA_ANIME_STAFF =          'bg-otaku-data_anime_staff'
        DATA_MANGA =                'bg-otaku-data_manga'
        DATA_MANGA_CHARACTERS =     'bg-otaku-data_manga_characters'
        DATA_MANGA_PICTURES =       'bg-otaku-data_manga_pictures'
        DATA_CHARACTER =            'bg-otaku-data_character'
        DATA_CHARACTER_PICTURES =   'bg-otaku-data_character_pictures'
        DATA_PERSON =               'bg-otaku-data_person'
        DATA_PERSON_PICTURES =      'bg-otaku-data_person_pictures'
        DATA_IMAGE_URL =            'bg-otaku-data_image_url'
        TEMP_PERSONS =              'bg-otaku-temp_persons'
        TEMP_CHARACTER =            'bg-otaku-temp_character'

    class Renpy:
        GENRE =                     'bg-renpy-genre'
        GAME_ENGINE =               'bg-renpy-game_engine'
        CENSORSHIP =                'bg-renpy-censorship'
        PREFIX =                    'bg-renpy-prefix'
        STATUS =                    'bg-renpy-status'
        PLATFORM =                  'bg-renpy-platform'
        DEVELOPER =                 'bg-renpy-developer'
        TRANSLATOR =                'bg-renpy-translator'
        PUBLISHER =                 'bg-renpy-publisher'
        GAME =                      'bg-renpy-game'
        GAME_IMAGE =                'bg-renpy-game_image'
        GAME_IMAGE_EXTRA =          'bg-renpy-game_image_extra'
        DEVELOPER_LINK =            'bg-renpy-developer_link'
        TRANSLATOR_LINKS =          'bg-renpy-translator_links'
        PUBLISHER_LINKS =           'bg-renpy-publisher_links'
        DEVELOPER_IMAGE =           'bg-renpy-developer_image'
        DEVELOPER_IMAGE_EXTRA =     'bg-renpy-developer_image_extra'
        TRANSLATOR_IMAGE =          'bg-renpy-translator_image'
        TRANSLATOR_IMAGE_EXTRA =    'bg-renpy-translator_image_extra'
        PUBLISHER_IMAGE =           'bg-renpy-publisher_image'
        PUBLISHER_IMAGE_EXTRA =     'bg-renpy-publisher_image_extra'
        TITLE_GAME =                'bg-renpy-title_game'
        DATA_GAME =                 'bg-renpy-data_game'

    class Serie:
        GENRE =             'bg-serie-genre'
        TYPE =              'bg-serie-type'
        ROLE =              'bg-serie-role'
        RATING =            'bg-serie-rating'
        COMPANY =           'bg-serie-company'
        SERIE =             'bg-serie-serie'
        TITLE_SERIE =       'bg-serie-title_serie'
        SERIE_STAFF =       'bg-serie-serie_staff'
        SERIE_CAST =        'bg-serie-serie_cast'
        SERIE_IMAGE =       'bg-serie-serie_image'
        SERIE_IMAGE_EXTRA = 'bg-serie-serie_image_extra'

####################################################    JSConstants
class JSConstants:
    ACTIONS = 'js/DataTables/acciones.js'

    class users:
        USER = 'js/DataTables/config/users/users_config.js'

    class Common:
        COUNTRY =               'js/DataTables/config/common/country_config.js'
        FORMAT =                'js/DataTables/config/common/format_config.js'
        IMAGE_SIZE =            'js/DataTables/config/common/image_size_config.js'
        LANGUAGE =              'js/DataTables/config/common/language_config.js'
        PERSON =                'js/DataTables/config/common/person_config.js'
        PERSON_IMAGE =          'js/DataTables/config/common/person_image_config.js'
        PERSON_IMAGE_EXTRA =    'js/DataTables/config/common/person_image_extra_config.js'
        PERSON_NICKNAME =       'js/DataTables/config/common/person_nickname_config.js'
        QUALITY =               'js/DataTables/config/common/quality_config.js'
        WEBSITE =               'js/DataTables/config/common/website_config.js'

    class Movie:
        COMPANY =           'js/DataTables/config/movie/movie_company.js'
        GENRE =             'js/DataTables/config/movie/movie_genre.js'
        MOVIE =             'js/DataTables/config/movie/movie_movie.js'
        MOVIE_CAST =        'js/DataTables/config/movie/movie_movie_cast.js'
        MOVIE_IMAGE =       'js/DataTables/config/movie/movie_movie_image.js'
        MOVIE_IMAGE_EXTRA = 'js/DataTables/config/movie/movie_movie_image_extra.js'
        MOVIE_STAFF =       'js/DataTables/config/movie/movie_movie_staff.js'
        RATING =            'js/DataTables/config/movie/movie_rating.js'
        ROLE =              'js/DataTables/config/movie/movie_role.js'
        TITLE_MOVIE =       'js/DataTables/config/movie/movie_title_movie.js'
        TYPE =              'js/DataTables/config/movie/movie_type.js'

    class Music:
        ALBUM =                 'js/DataTables/config/music/music_album.js'
        ALBUM_IMAGE =           'js/DataTables/config/music/music_album_image.js'
        ALBUM_IMAGE_EXTRA =     'js/DataTables/config/music/music_album_image_extra.js'
        ALBUM_TYPE =            'js/DataTables/config/music/music_album_type.js'
        ARTIST =                'js/DataTables/config/music/music_artist.js'
        ARTIST_IMAGE =          'js/DataTables/config/music/music_artist_image.js'
        ARTIST_IMAGE_EXTRA =    'js/DataTables/config/music/music_artist_image_extra.js'
        ARTIST_MEMBER =         'js/DataTables/config/music/music_artist_member.js'
        ARTIST_TYPE =           'js/DataTables/config/music/music_artist_type.js'
        GENRE =                 'js/DataTables/config/music/music_genre.js'
        ROLE =                  'js/DataTables/config/music/music_role.js'
        SONG =                  'js/DataTables/config/music/music_song.js'

    class Otaku:
        ANIME =                     'js/DataTables/config/otaku/otaku_anime.js'
        ANIME_CHARACTER =           'js/DataTables/config/otaku/otaku_anime_character.js'
        ANIME_IMAGE =               'js/DataTables/config/otaku/otaku_anime_image.js'
        ANIME_IMAGE_EXTRA =         'js/DataTables/config/otaku/otaku_anime_image_extra.js'
        ANIME_STAFF =               'js/DataTables/config/otaku/otaku_anime_staff.js'
        AUTHOR_MANGA =              'js/DataTables/config/otaku/otaku_author_manga.js'
        CHARACTER =                 'js/DataTables/config/otaku/otaku_character.js'
        CHARACTER_IMAGE =           'js/DataTables/config/otaku/otaku_character_image.js'
        CHARACTER_IMAGE_EXTRA =     'js/DataTables/config/otaku/otaku_character_image_extra.js'
        CHARACTER_NICKNAME =        'js/DataTables/config/otaku/otaku_character_nickname.js'
        DATA_ANIME =                'js/DataTables/config/otaku/otaku_data_anime.js'
        DATA_ANIME_CHARACTERS =     'js/DataTables/config/otaku/otaku_data_anime_characters.js'
        DATA_ANIME_PICTURES =       'js/DataTables/config/otaku/otaku_data_anime_pictures.js'
        DATA_ANIME_STAFF =          'js/DataTables/config/otaku/otaku_data_anime_staff.js'
        DATA_CHARACTER =            'js/DataTables/config/otaku/otaku_data_character.js'
        DATA_CHARACTER_PICTURES =   'js/DataTables/config/otaku/otaku_data_character_pictures.js'
        DATA_IMAGE_URL =            'js/DataTables/config/otaku/otaku_data_image_url.js'
        DATA_MANGA =                'js/DataTables/config/otaku/otaku_data_manga.js'
        DATA_MANGA_CHARACTERS =     'js/DataTables/config/otaku/otaku_data_manga_characters.js'
        DATA_MANGA_PICTURES =       'js/DataTables/config/otaku/otaku_data_manga_pictures.js'
        DATA_PERSON =               'js/DataTables/config/otaku/otaku_data_person.js'
        DATA_PERSON_PICTURES =      'js/DataTables/config/otaku/otaku_data_person_pictures.js'
        DEMOGRAPHIC =               'js/DataTables/config/otaku/otaku_demographic.js'
        GENRE =                     'js/DataTables/config/otaku/otaku_genre.js'
        LICENSOR =                  'js/DataTables/config/otaku/otaku_licensor.js'
        MANGA =                     'js/DataTables/config/otaku/otaku_manga.js'
        MANGA_CHARACTER =           'js/DataTables/config/otaku/otaku_manga_character.js'
        MANGA_IMAGE =               'js/DataTables/config/otaku/otaku_manga_image.js'
        MANGA_IMAGE_EXTRA =         'js/DataTables/config/otaku/otaku_manga_image_extra.js'
        MEDIA_RELATION =            'js/DataTables/config/otaku/otaku_media_relation.js'
        MEDIA_RELATION_ANIME =      'js/DataTables/config/otaku/otaku_media_relation_anime.js'
        MEDIA_RELATION_MANGA =      'js/DataTables/config/otaku/otaku_media_relation_manga.js'
        PERSON =                    'js/DataTables/config/otaku/otaku_person.js'
        PERSON_IMAGE =              'js/DataTables/config/otaku/otaku_person_image.js'
        PERSON_IMAGE_EXTRA =        'js/DataTables/config/otaku/otaku_person_image_extra.js'
        PERSON_NICKNAME =           'js/DataTables/config/otaku/otaku_person_nickname.js'
        PRODUCER =                  'js/DataTables/config/otaku/otaku_producer.js'
        RATING =                    'js/DataTables/config/otaku/otaku_rating.js'
        RELATION_TYPE =             'js/DataTables/config/otaku/otaku_relation_type.js'
        ROLE =                      'js/DataTables/config/otaku/otaku_role.js'
        SEASON =                    'js/DataTables/config/otaku/otaku_season.js'
        SEASON_FULL =               'js/DataTables/config/otaku/otaku_season_full.js'
        SERIALIZATION =             'js/DataTables/config/otaku/otaku_serialization.js'
        SONG =                      'js/DataTables/config/otaku/otaku_song.js'
        SONG_ED =                   'js/DataTables/config/otaku/otaku_song_ED.js'
        SONG_IN =                   'js/DataTables/config/otaku/otaku_song_IN.js'
        SONG_OP =                   'js/DataTables/config/otaku/otaku_song_OP.js'
        SOURCE =                    'js/DataTables/config/otaku/otaku_source.js'
        STATUS =                    'js/DataTables/config/otaku/otaku_status.js'
        STUDIO =                    'js/DataTables/config/otaku/otaku_studio.js'
        TEMP_CHARACTER =            'js/DataTables/config/otaku/otaku_temp_character.js'
        TEMP_PERSONS =              'js/DataTables/config/otaku/otaku_temp_persons.js'
        THEME =                     'js/DataTables/config/otaku/otaku_theme.js'
        TITLE_ANIME =               'js/DataTables/config/otaku/otaku_title_anime.js'
        TITLE_MANGA =               'js/DataTables/config/otaku/otaku_title_manga.js'
        TYPE =                      'js/DataTables/config/otaku/otaku_type.js'
        VOICE_CHARACTER =           'js/DataTables/config/otaku/otaku_voice_character.js'
        YEAR =                      'js/DataTables/config/otaku/otaku_year.js'

    class Renpy:
        CENSORSHIP =                'js/DataTables/config/renpy/renpy_censorship.js'
        DATA_GAME =                 'js/DataTables/config/renpy/renpy_data_game.js'
        DEVELOPER =                 'js/DataTables/config/renpy/renpy_developer.js'
        DEVELOPER_IMAGE =           'js/DataTables/config/renpy/renpy_developer_image.js'
        DEVELOPER_IMAGE_EXTRA =     'js/DataTables/config/renpy/renpy_developer_image_extra.js'
        DEVELOPER_LINKS =           'js/DataTables/config/renpy/renpy_developer_links.js'
        GAME =                      'js/DataTables/config/renpy/renpy_game.js'
        GAME_ENGINE =               'js/DataTables/config/renpy/renpy_game_engine.js'
        GAME_IMAGE =                'js/DataTables/config/renpy/renpy_game_image.js'
        GAME_IMAGE_EXTRA =          'js/DataTables/config/renpy/renpy_game_image_extra.js'
        GENRE =                     'js/DataTables/config/renpy/renpy_genre.js'
        PLATFORM =                  'js/DataTables/config/renpy/renpy_platform.js'
        PREFIX =                    'js/DataTables/config/renpy/renpy_prefix.js'
        PUBLISHER =                 'js/DataTables/config/renpy/renpy_publisher.js'
        PUBLISHER_IMAGE =           'js/DataTables/config/renpy/renpy_publisher_image.js'
        PUBLISHER_IMAGE_EXTRA =     'js/DataTables/config/renpy/renpy_publisher_image_extra.js'
        PUBLISHER_LINKS =           'js/DataTables/config/renpy/renpy_publisher_links.js'
        STATUS =                    'js/DataTables/config/renpy/renpy_status.js'
        TITLE_GAME =                'js/DataTables/config/renpy/renpy_title_game.js'
        TRANSLATOR =                'js/DataTables/config/renpy/renpy_translator.js'
        TRANSLATOR_IMAGE =          'js/DataTables/config/renpy/renpy_translator_image.js'
        TRANSLATOR_IMAGE_EXTRA =    'js/DataTables/config/renpy/renpy_translator_image_extra.js'
        TRANSLATOR_LINKS =          'js/DataTables/config/renpy/renpy_translator_links.js'

    class Serie:
        COMPANY =           'js/DataTables/config/serie/serie_company.js'
        GENRE =             'js/DataTables/config/serie/serie_genre.js'
        RATING =            'js/DataTables/config/serie/serie_rating.js'
        ROLE =              'js/DataTables/config/serie/serie_role.js'
        SERIE =             'js/DataTables/config/serie/serie_serie.js'
        SERIE_CAST =        'js/DataTables/config/serie/serie_serie_cast.js'
        SERIE_IMAGE =       'js/DataTables/config/serie/serie_serie_image.js'
        SERIE_IMAGE_EXTRA = 'js/DataTables/config/serie/serie_serie_image_extra.js'
        SERIE_STAFF =       'js/DataTables/config/serie/serie_serie_staff.js'
        TITLE_SERIE =       'js/DataTables/config/serie/serie_title_serie.js'
        TYPE =              'js/DataTables/config/serie/serie_type.js'

####################################################    ImageCards
class ImageCards:
    class Users:
        USER = 'img/screen/wide/bg-users-user.webp'
    class Common:
        COUNTRY =            'img/screen/wide/bg-common-country.webp'
        FORMAT =             'img/screen/wide/bg-common-format.webp'
        IMAGE_SIZE =         'img/screen/wide/bg-common-image_size.webp'
        LANGUAGE =           'img/screen/wide/bg-common-language.webp'
        PERSON =             'img/screen/wide/bg-common-person.webp'
        PERSON_IMAGE =       'img/screen/wide/bg-common-person_image.webp'
        PERSON_IMAGE_EXTRA = 'img/screen/wide/bg-common-person_image_extra.webp'
        PERSON_NICKNAME =    'img/screen/wide/bg-common-person_nickname.webp'
        QUALITY =            'img/screen/wide/bg-common-quality.webp'
        WEBSITE =            'img/screen/wide/bg-common-website.webp'

    class Movie:
        COMPANY =           'img/screen/wide/bg-movie-company.webp'
        GENRE =             'img/screen/wide/bg-movie-genre.webp'
        MOVIE =             'img/screen/wide/bg-movie-movie.webp'
        MOVIE_CAST =        'img/screen/wide/bg-movie-movie_cast.webp'
        MOVIE_IMAGE =       'img/screen/wide/bg-movie-movie_image.webp'
        MOVIE_IMAGE_EXTRA = 'img/screen/wide/bg-movie-movie_image_extra.webp'
        MOVIE_STAFF =       'img/screen/wide/bg-movie-movie_staff.webp'
        RATING =            'img/screen/wide/bg-movie-rating.webp'
        ROLE =              'img/screen/wide/bg-movie-role.webp'
        TITLE_MOVIE =       'img/screen/wide/bg-movie-title_movie.webp'
        TYPE =              'img/screen/wide/bg-movie-type.webp'

    class Music:
        ALBUM =                 'img/screen/wide/bg-music-album.webp'
        ALBUM_IMAGE =           'img/screen/wide/bg-music-album_image.webp'
        ALBUM_IMAGE_EXTRA =     'img/screen/wide/bg-music-album_image_extra.webp'
        ALBUM_TYPE =            'img/screen/wide/bg-music-album_type.webp'
        ARTIST =                'img/screen/wide/bg-music-artist.webp'
        ARTIST_IMAGE =          'img/screen/wide/bg-music-artist_image.webp'
        ARTIST_IMAGE_EXTRA =    'img/screen/wide/bg-music-artist_image_extra.webp'
        ARTIST_MEMBER =         'img/screen/wide/bg-music-artist_member.webp'
        ARTIST_TYPE =           'img/screen/wide/bg-music-artist_type.webp'
        GENRE =                 'img/screen/wide/bg-music-genre.webp'
        ROLE =                  'img/screen/wide/bg-music-role.webp'
        SONG =                  'img/screen/wide/bg-music-song.webp'

    class Otaku:
        ANIME =                     'img/screen/wide/bg-otaku-anime.webp'
        ANIME_CHARACTER =           'img/screen/wide/bg-otaku-anime_character.webp'
        ANIME_IMAGE =               'img/screen/wide/bg-otaku-anime_image.webp'
        ANIME_IMAGE_EXTRA =         'img/screen/wide/bg-otaku-anime_image_extra.webp'
        ANIME_STAFF =               'img/screen/wide/bg-otaku-anime_staff.webp'
        AUTHOR_MANGA =              'img/screen/wide/bg-otaku-author_manga.webp'
        CHARACTER =                 'img/screen/wide/bg-otaku-character.webp'
        CHARACTER_IMAGE =           'img/screen/wide/bg-otaku-character_image.webp'
        CHARACTER_IMAGE_EXTRA =     'img/screen/wide/bg-otaku-character_image_extra.webp'
        CHARACTER_NICKNAME =        'img/screen/wide/bg-otaku-character_nickname.webp'
        DATA_ANIME =                'img/screen/wide/bg-otaku-data_anime.webp'
        DATA_ANIME_CHARACTERS =     'img/screen/wide/bg-otaku-data_anime_characters.webp'
        DATA_ANIME_PICTURES =       'img/screen/wide/bg-otaku-data_anime_pictures.webp'
        DATA_ANIME_STAFF =          'img/screen/wide/bg-otaku-data_anime_staff.webp'
        DATA_CHARACTER =            'img/screen/wide/bg-otaku-data_character.webp'
        DATA_CHARACTER_PICTURES =   'img/screen/wide/bg-otaku-data_character_pictures.webp'
        DATA_IMAGE_URL =            'img/screen/wide/bg-otaku-data_image_url.webp'
        DATA_MANGA =                'img/screen/wide/bg-otaku-data_manga.webp'
        DATA_MANGA_CHARACTERS =     'img/screen/wide/bg-otaku-data_manga_characters.webp'
        DATA_MANGA_PICTURES =       'img/screen/wide/bg-otaku-data_manga_pictures.webp'
        DATA_PERSON =               'img/screen/wide/bg-otaku-data_person.webp'
        DATA_PERSON_PICTURES =      'img/screen/wide/bg-otaku-data_person_pictures.webp'
        DEMOGRAPHIC =               'img/screen/wide/bg-otaku-demographic.webp'
        GENRE =                     'img/screen/wide/bg-otaku-genre.webp'
        LICENSOR =                  'img/screen/wide/bg-otaku-licensor.webp'
        MANGA =                     'img/screen/wide/bg-otaku-manga.webp'
        MANGA_CHARACTER =           'img/screen/wide/bg-otaku-manga_character.webp'
        MANGA_IMAGE =               'img/screen/wide/bg-otaku-manga_image.webp'
        MANGA_IMAGE_EXTRA =         'img/screen/wide/bg-otaku-manga_image_extra.webp'
        MEDIA_RELATION =            'img/screen/wide/bg-otaku-media_relation.webp'
        MEDIA_RELATION_ANIME =      'img/screen/wide/bg-otaku-media_relation_anime.webp'
        MEDIA_RELATION_MANGA =      'img/screen/wide/bg-otaku-media_relation_manga.webp'
        PERSON =                    'img/screen/wide/bg-otaku-person.webp'
        PERSON_IMAGE =              'img/screen/wide/bg-otaku-person_image.webp'
        PERSON_IMAGE_EXTRA =        'img/screen/wide/bg-otaku-person_image_extra.webp'
        PERSON_NICKNAME =           'img/screen/wide/bg-otaku-person_nickname.webp'
        PRODUCER =                  'img/screen/wide/bg-otaku-producer.webp'
        RATING =                    'img/screen/wide/bg-otaku-rating.webp'
        RELATION_TYPE =             'img/screen/wide/bg-otaku-relation_type.webp'
        ROLE =                      'img/screen/wide/bg-otaku-role.webp'
        SEASON =                    'img/screen/wide/bg-otaku-season.webp'
        SEASON_FULL =               'img/screen/wide/bg-otaku-season_full.webp'
        SERIALIZATION =             'img/screen/wide/bg-otaku-serialization.webp'
        SONG =                      'img/screen/wide/bg-otaku-song.webp'
        SONG_ED =                   'img/screen/wide/bg-otaku-song_ED.webp'
        SONG_IN =                   'img/screen/wide/bg-otaku-song_IN.webp'
        SONG_OP =                   'img/screen/wide/bg-otaku-song_OP.webp'
        SOURCE =                    'img/screen/wide/bg-otaku-source.webp'
        STATUS =                    'img/screen/wide/bg-otaku-status.webp'
        STUDIO =                    'img/screen/wide/bg-otaku-studio.webp'
        TEMP_CHARACTER =            'img/screen/wide/bg-otaku-temp_character.webp'
        TEMP_PERSONS =              'img/screen/wide/bg-otaku-temp_persons.webp'
        THEME =                     'img/screen/wide/bg-otaku-theme.webp'
        TITLE_ANIME =               'img/screen/wide/bg-otaku-title_anime.webp'
        TITLE_MANGA =               'img/screen/wide/bg-otaku-title_manga.webp'
        TYPE =                      'img/screen/wide/bg-otaku-type.webp'
        VOICE_CHARACTER =           'img/screen/wide/bg-otaku-voice_character.webp'
        YEAR =                      'img/screen/wide/bg-otaku-year.webp'

    class Renpy:
        CENSORSHIP =                'img/screen/wide/bg-renpy-censorship.webp'
        DATA_GAME =                 'img/screen/wide/bg-renpy-data_game.webp'
        DEVELOPER =                 'img/screen/wide/bg-renpy-developer.webp'
        DEVELOPER_IMAGE =           'img/screen/wide/bg-renpy-developer_image.webp'
        DEVELOPER_IMAGE_EXTRA =     'img/screen/wide/bg-renpy-developer_image_extra.webp'
        DEVELOPER_LINKS =           'img/screen/wide/bg-renpy-developer_links.webp'
        GAME =                      'img/screen/wide/bg-renpy-game.webp'
        GAME_ENGINE =               'img/screen/wide/bg-renpy-game_engine.webp'
        GAME_IMAGE =                'img/screen/wide/bg-renpy-game_image.webp'
        GAME_IMAGE_EXTRA =          'img/screen/wide/bg-renpy-game_image_extra.webp'
        GENRE =                     'img/screen/wide/bg-renpy-genre.webp'
        PLATFORM =                  'img/screen/wide/bg-renpy-platform.webp'
        PREFIX =                    'img/screen/wide/bg-renpy-prefix.webp'
        PUBLISHER =                 'img/screen/wide/bg-renpy-publisher.webp'
        PUBLISHER_IMAGE =           'img/screen/wide/bg-renpy-publisher_image.webp'
        PUBLISHER_IMAGE_EXTRA =     'img/screen/wide/bg-renpy-publisher_image_extra.webp'
        PUBLISHER_LINKS =           'img/screen/wide/bg-renpy-publisher_links.webp'
        STATUS =                    'img/screen/wide/bg-renpy-status.webp'
        TITLE_GAME =                'img/screen/wide/bg-renpy-title_game.webp'
        TRANSLATOR =                'img/screen/wide/bg-renpy-translator.webp'
        TRANSLATOR_IMAGE =          'img/screen/wide/bg-renpy-translator_image.webp'
        TRANSLATOR_IMAGE_EXTRA =    'img/screen/wide/bg-renpy-translator_image_extra.webp'
        TRANSLATOR_LINKS =          'img/screen/wide/bg-renpy-translator_links.webp'

    class Serie:
        COMPANY =           'img/screen/wide/bg-serie-company.webp'
        GENRE =             'img/screen/wide/bg-serie-genre.webp'
        RATING =            'img/screen/wide/bg-serie-rating.webp'
        ROLE =              'img/screen/wide/bg-serie-role.webp'
        SERIE =             'img/screen/wide/bg-serie-serie.webp'
        SERIE_CAST =        'img/screen/wide/bg-serie-serie_cast.webp'
        SERIE_IMAGE =       'img/screen/wide/bg-serie-serie_image.webp'
        SERIE_IMAGE_EXTRA = 'img/screen/wide/bg-serie-serie_image_extra.webp'
        SERIE_STAFF =       'img/screen/wide/bg-serie-serie_staff.webp'
        TITLE_SERIE =       'img/screen/wide/bg-serie-title_serie.webp'
        TYPE =              'img/screen/wide/bg-serie-type.webp'

####################################################    KeyMap
class KeyMap:
    class Users:
        USER = 'Usuario'

    class Common:
        COUNTRY =               'País'
        FORMAT =                'Formato'
        IMAGE_SIZE =            'Tamaño imagen'
        LANGUAGE =              'Idioma'
        PERSON =                'Persona'
        PERSON_IMAGE =          'Imagen de Persona'
        PERSON_IMAGE_EXTRA =    'Imagen extra de Persona'
        PERSON_NICKNAME =       'Apodo de Persona'
        QUALITY =               'Calidad'
        WEBSITE =               'Sitio Web'

    class Movie:
        COMPANY =           'Compañía cinematográfica'
        GENRE =             'Género cinematográfico'
        MOVIE =             'Película'
        MOVIE_CAST =        'Reparto cinematográfico'
        MOVIE_IMAGE =       'Imagen de película'
        MOVIE_IMAGE_EXTRA = 'Imagen adicional de película'
        MOVIE_STAFF =       'Personal cinematográfico'
        RATING =            'Clasificación cinematográfica'
        ROLE =              'Rol cinematográfico'
        TITLE_MOVIE =       'Título de película'
        TYPE =              'Tipo de película'

    class Music:
        ALBUM =                 'Álbum'
        ALBUM_IMAGE =           'Imagen del álbum'
        ALBUM_IMAGE_EXTRA =     'Imagen adicional del álbum'
        ALBUM_TYPE =            'Tipo de álbum'
        ARTIST =                'Artista'
        ARTIST_IMAGE =          'Imagen del artista'
        ARTIST_IMAGE_EXTRA =    'Imagen adicional del artista'
        ARTIST_MEMBER =         'Miembro del artista'
        ARTIST_TYPE =           'Tipo de artista'
        GENRE =                 'Género'
        ROLE =                  'Rol musical'
        SONG =                  'Canción'

    class Otaku:
        ANIME =                     'Anime'
        ANIME_CHARACTER =           'Personaje del anime'
        ANIME_IMAGE =               'Imagen del anime'
        ANIME_IMAGE_EXTRA =         'Imagen adicional del anime'
        ANIME_STAFF =               'Personal del anime'
        AUTHOR_MANGA =              'Autor de manga'
        CHARACTER =                 'Personaje'
        CHARACTER_IMAGE =           'Imagen del personaje'
        CHARACTER_IMAGE_EXTRA =     'Imagen adicional del personaje'
        CHARACTER_NICKNAME =        'Apodo del personaje'
        DEMOGRAPHIC =               'Demografía'
        GENRE =                     'Género'
        LICENSOR =                  'Licenciante'
        MANGA =                     'Manga'
        MANGA_CHARACTER =           'Personaje del manga'
        MANGA_IMAGE =               'Imagen del manga'
        MANGA_IMAGE_EXTRA =         'Imagen adicional del manga'
        MEDIA_RELATION =            'relación de medias'
        MEDIA_RELATION_ANIME =      'relación de media de anime'
        MEDIA_RELATION_MANGA =      'relación de media de manga'
        PERSON =                    'Persona.'
        PERSON_IMAGE =              'Imagen de la persona.'
        PERSON_IMAGE_EXTRA =        'Imagen adicional de la persona.'
        PERSON_NICKNAME =           'Apodo de la persona.'
        PRODUCER =                  'Productora'
        RATING =                    'Calificación otaku'
        RELATION_TYPE =             'Tipo de relación'
        ROLE =                      'Rol Otaku'
        SEASON =                    'Temporada'
        SEASON_FULL =               'Temporada Completa'
        SERIALIZATION =             'Publicadora'
        SONG =                      'Canción Anime'
        SONG_ED =                   'Ending'
        SONG_IN =                   'Insert Song'
        SONG_OP =                   'Opening'
        SOURCE =                    'Fuente'
        STATUS =                    'Estado Anime Manga'
        STUDIO =                    'Estudio'
        THEME =                     'Tema'
        TITLE_ANIME =               'Título Anime'
        TITLE_MANGA =               'Título Manga'
        TYPE =                      'Tipo Anime Manga'
        VOICE_CHARACTER =           'Actor de Voz'
        YEAR =                      'Año'

        TEMP_CHARACTER =            'temp_character.webp'
        TEMP_PERSONS =              'temp_persons.webp'
        DATA_ANIME =                'data_anime.webp'
        DATA_ANIME_CHARACTERS =     'data_anime_characters.webp'
        DATA_ANIME_PICTURES =       'data_anime_pictures.webp'
        DATA_ANIME_STAFF =          'data_anime_staff.webp'
        DATA_CHARACTER =            'data_character.webp'
        DATA_CHARACTER_PICTURES =   'data_character_pictures.webp'
        DATA_IMAGE_URL =            'data_image_url.webp'
        DATA_MANGA =                'data_manga.webp'
        DATA_MANGA_CHARACTERS =     'data_manga_characters.webp'
        DATA_MANGA_PICTURES =       'data_manga_pictures.webp'
        DATA_PERSON =               'data_person.webp'
        DATA_PERSON_PICTURES =      'data_person_pictures.webp'

    class Renpy:
        CENSORSHIP =                'Censura'
        DEVELOPER =                 'Desarrollador'
        DEVELOPER_IMAGE =           'Imagen del desarrollador'
        DEVELOPER_IMAGE_EXTRA =     'Imagen adicional del desarrollador'
        DEVELOPER_LINKS =           'Enlace del desarrollador'
        GAME =                      'Juego'
        GAME_ENGINE =               'Motor de desarrollo'
        GAME_IMAGE =                'Imagen del juego'
        GAME_IMAGE_EXTRA =          'Imagen adicional del juego'
        GENRE =                     'Género del juego'
        PLATFORM =                  'Plataforma del juego'
        PREFIX =                    'Prefijo del juego'
        PUBLISHER =                 'Editor'
        PUBLISHER_IMAGE =           'Imagen del editor'
        PUBLISHER_IMAGE_EXTRA =     'Imagen adicional del editor'
        PUBLISHER_LINKS =           'Enlace del editor'
        STATUS =                    'Estado de juego'
        TITLE_GAME =                'Título del juego'
        TRANSLATOR =                'Traductor'
        TRANSLATOR_IMAGE =          'Imagen del traductor'
        TRANSLATOR_IMAGE_EXTRA =    'Imagen adicional del traductor'
        TRANSLATOR_LINKS =          'Enlace del traductor'
        DATA_GAME =                 'datos del juego'

    class Serie:
        COMPANY =           'Compañía de producción televisiva'
        GENRE =             'Género televisivo'
        RATING =            'Clasificación televisiva'
        ROLE =              'Rol televisivo'
        SERIE =             'Serie'
        SERIE_CAST =        'Reparto televisivo'
        SERIE_IMAGE =       'Imagen de serie'
        SERIE_IMAGE_EXTRA = 'Imagen adicional de serie'
        SERIE_STAFF =       'Personal televisivo'
        TITLE_SERIE =       'Título de serie'
        TYPE =              'Tipo de serie'
