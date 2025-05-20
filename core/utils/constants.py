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

    class EmailBoddy:
        PASSWORD_RECOVERY = 'emails/body/password_recovery.txt'
        RESET_PASSWORD = 'emails/body/reset_password.txt'
        USER_BLOCKED = 'emails/body/user_blocked.txt'
        USER_ACTIVATED = 'emails/body/user_activated.txt'
        DELETED_USER = 'emails/body/deleted_user.txt'
        PASSWORD_CHANGED = 'emails/body/password_changed.txt'
        CONTACT = 'emails/body/contact.txt'

    class EmailSubject:
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
        LIST = 'users/user/user_list.html'
        CREATE = 'users/user/user_form.html'
        UPDATE = 'users/user/user_UPDATE.html'
        DETAIL = 'users/user/user_detail.html'
        CHANGE_PASS = 'users/user/user_password_change.html'

    class Common:
        class Country:
            LIST = 'common/country/country_list.html'
            CREATE = 'common/country/country_form.html'
            UPDATE = 'common/country/country_form.html'
            DETAIL = 'common/country/country_detail.html'
        class Format:
            LIST = 'common/format/format_list.html'
            CREATE = 'common/format/format_form.html'
            UPDATE = 'common/format/format_form.html'
            DETAIL = 'common/format/format_detail.html'
        class ImageSize:
            LIST = 'common/image_size/image_size_list.html'
            CREATE = 'common/image_size/image_size_form.html'
            UPDATE = 'common/image_size/image_size_form.html'
            DETAIL = 'common/image_size/image_size_detail.html'
        class Language:
            LIST = 'common/language/language_list.html'
            CREATE = 'common/language/language_form.html'
            UPDATE = 'common/language/language_form.html'
            DETAIL = 'common/language/language_detail.html'
        class Person:
            LIST = 'common/person/person_list.html'
            CREATE = 'common/person/person_form.html'
            UPDATE = 'common/person/person_form.html'
            DETAIL = 'common/person/person_detail.html'
        class PersonImage:
            LIST = 'common/person_image/person_image_list.html'
            CREATE = 'common/person_image/person_image_form.html'
            UPDATE = 'common/person_image/person_image_form.html'
            DETAIL = 'common/person_image/person_image_detail.html'
        class PersonImageExtra:
            LIST = 'common/person_image_extra/person_image_extra_list.html'
            CREATE = 'common/person_image_extra/person_image_extra_form.html'
            UPDATE = 'common/person_image_extra/person_image_extra_form.html'
            DETAIL = 'common/person_image_extra/person_image_extra_detail.html'
        class PersonNickname:
            LIST = 'common/person_nickname/person_nickname_list.html'
            CREATE = 'common/person_nickname/person_nickname_form.html'
            UPDATE = 'common/person_nickname/person_nickname_form.html'
            DETAIL = 'common/person_nickname/person_nickname_detail.html'
        class Quality:
            LIST = 'common/quality/quality_list.html'
            CREATE = 'common/quality/quality_form.html'
            UPDATE = 'common/quality/quality_form.html'
            DETAIL = 'common/quality/quality_detail.html'
        class Website:
            LIST = 'common/website/website_list.html'
            CREATE = 'common/website/website_form.html'
            UPDATE = 'common/website/website_form.html'
            DETAIL = 'common/website/website_detail.html'



    class Movie:
        class Company:
            LIST = 'movie/company/company_list.html'
            CREATE = 'movie/company/company_form.html'
            UPDATE = 'movie/company/company_form.html'
            DETAIL = 'movie/company/company_detail.html'
        class Genre:
            LIST = 'movie/genre/genre_list.html'
            CREATE = 'movie/genre/genre_form.html'
            UPDATE = 'movie/genre/genre_form.html'
            DETAIL = 'movie/genre/genre_detail.html'
        class Movie:
            LIST = 'movie/movie/movie_list.html'
            CREATE = 'movie/movie/movie_form.html'
            UPDATE = 'movie/movie/movie_form.html'
            DETAIL = 'movie/movie/movie_detail.html'
        class MovieCast:
            LIST = 'movie/movie_cast/movie_cast_list.html'
            CREATE = 'movie/movie_cast/movie_cast_form.html'
            UPDATE = 'movie/movie_cast/movie_cast_form.html'
            DETAIL = 'movie/movie_cast/movie_cast_detail.html'
        class MovieImage:
            LIST = 'movie/movie_image/movie_image_list.html'
            CREATE = 'movie/movie_image/movie_image_form.html'
            UPDATE = 'movie/movie_image/movie_image_form.html'
            DETAIL = 'movie/movie_image/movie_image_detail.html'
        class MovieImageExtra:
            LIST = 'movie/movie_image_extra/movie_image_extra_list.html'
            CREATE = 'movie/movie_image_extra/movie_image_extra_form.html'
            UPDATE = 'movie/movie_image_extra/movie_image_extra_form.html'
            DETAIL = 'movie/movie_image_extra/movie_image_extra_detail.html'
        class MovieStaff:
            LIST = 'movie/movie_staff/movie_staff_list.html'
            CREATE = 'movie/movie_staff/movie_staff_form.html'
            UPDATE = 'movie/movie_staff/movie_staff_form.html'
            DETAIL = 'movie/movie_staff/movie_staff_detail.html'
        class Rating:
            LIST = 'movie/rating/rating_list.html'
            CREATE = 'movie/rating/rating_form.html'
            UPDATE = 'movie/rating/rating_form.html'
            DETAIL = 'movie/rating/rating_detail.html'
        class Role:
            LIST = 'movie/role/role_list.html'
            CREATE = 'movie/role/role_form.html'
            UPDATE = 'movie/role/role_form.html'
            DETAIL = 'movie/role/role_detail.html'
        class TitleMovie:
            LIST = 'movie/title_movie/title_movie_list.html'
            CREATE = 'movie/title_movie/title_movie_form.html'
            UPDATE = 'movie/title_movie/title_movie_form.html'
            DETAIL = 'movie/title_movie/title_movie_detail.html'
        class Type:
            LIST = 'movie/type/type_list.html'
            CREATE = 'movie/type/type_form.html'
            UPDATE = 'movie/type/type_form.html'
            DETAIL = 'movie/type/type_detail.html'

    class Music:
        class Album:
            LIST = 'music/album/album_list.html'
            CREATE = 'music/album/album_form.html'
            UPDATE = 'music/album/album_form.html'
            DETAIL = 'music/album/album_detail.html'

        class AlbumImage:
            LIST = 'music/album_image/album_image_list.html'
            CREATE = 'music/album_image/album_image_form.html'
            UPDATE = 'music/album_image/album_image_form.html'
            DETAIL = 'music/album_image/album_image_detail.html'

        class AlbumImageExtra:
            LIST = 'music/album_image_extra/album_image_extra_list.html'
            CREATE = 'music/album_image_extra/album_image_extra_form.html'
            UPDATE = 'music/album_image_extra/album_image_extra_form.html'
            DETAIL = 'music/album_image_extra/album_image_extra_detail.html'

        class AlbumType:
            LIST = 'music/album_type/album_type_list.html'
            CREATE = 'music/album_type/album_type_form.html'
            UPDATE = 'music/album_type/album_type_form.html'
            DETAIL = 'music/album_type/album_type_detail.html'

        class Artist:
            LIST = 'music/artist/artist_list.html'
            CREATE = 'music/artist/artist_form.html'
            UPDATE = 'music/artist/artist_form.html'
            DETAIL = 'music/artist/artist_detail.html'

        class ArtistImage:
            LIST = 'music/artist_image/artist_image_list.html'
            CREATE = 'music/artist_image/artist_image_form.html'
            UPDATE = 'music/artist_image/artist_image_form.html'
            DETAIL = 'music/artist_image/artist_image_detail.html'

        class ArtistImageExtra:
            LIST = 'music/artist_image_extra/artist_image_extra_list.html'
            CREATE = 'music/artist_image_extra/artist_image_extra_form.html'
            UPDATE = 'music/artist_image_extra/artist_image_extra_form.html'
            DETAIL = 'music/artist_image_extra/artist_image_extra_detail.html'

        class ArtistMember:
            LIST = 'music/artist_member/artist_member_list.html'
            CREATE = 'music/artist_member/artist_member_form.html'
            UPDATE = 'music/artist_member/artist_member_form.html'
            DETAIL = 'music/artist_member/artist_member_detail.html'

        class ArtistType:
            LIST = 'music/artist_type/artist_type_list.html'
            CREATE = 'music/artist_type/artist_type_form.html'
            UPDATE = 'music/artist_type/artist_type_form.html'
            DETAIL = 'music/artist_type/artist_type_detail.html'

        class Genre:
            LIST = 'music/genre/genre_list.html'
            CREATE = 'music/genre/genre_form.html'
            UPDATE = 'music/genre/genre_form.html'
            DETAIL = 'music/genre/genre_detail.html'

        class Role:
            LIST = 'music/role/role_list.html'
            CREATE = 'music/role/role_form.html'
            UPDATE = 'music/role/role_form.html'
            DETAIL = 'music/role/role_detail.html'

        class Song:
            LIST = 'music/song/song_list.html'
            CREATE = 'music/song/song_form.html'
            UPDATE = 'music/song/song_form.html'
            DETAIL = 'music/song/song_detail.html'

    class Otaku:
        class Anime:
            LIST = 'otaku/anime/anime_list.html'
            CREATE = 'otaku/anime/anime_form.html'
            UPDATE = 'otaku/anime/anime_form.html'
            DETAIL = 'otaku/anime/anime_detail.html'
        class AnimeCharacter:
            LIST = 'otaku/anime_character/anime_character_list.html'
            CREATE = 'otaku/anime_character/anime_character_form.html'
            UPDATE = 'otaku/anime_character/anime_character_form.html'
            DETAIL = 'otaku/anime_character/anime_character_detail.html'
        class AnimeImage:
            LIST = 'otaku/anime_image/anime_image_list.html'
            CREATE = 'otaku/anime_image/anime_image_form.html'
            UPDATE = 'otaku/anime_image/anime_image_form.html'
            DETAIL = 'otaku/anime_image/anime_image_detail.html'
        class AnimeImageExtra:
            LIST = 'otaku/anime_image_extra/anime_image_extra_list.html'
            CREATE = 'otaku/anime_image_extra/anime_image_extra_form.html'
            UPDATE = 'otaku/anime_image_extra/anime_image_extra_form.html'
            DETAIL = 'otaku/anime_image_extra/anime_image_extra_detail.html'
        class AnimeSong:
            LIST = 'otaku/anime_song/anime_song_list.html'
            CREATE = 'otaku/anime_song/anime_song_form.html'
            UPDATE = 'otaku/anime_song/anime_song_form.html'
            DETAIL = 'otaku/anime_song/anime_song_detail.html'
        class AnimeStaff:
            LIST = 'otaku/anime_staff/anime_staff_list.html'
            CREATE = 'otaku/anime_staff/anime_staff_form.html'
            UPDATE = 'otaku/anime_staff/anime_staff_form.html'
            DETAIL = 'otaku/anime_staff/anime_staff_detail.html'
        class AuthorManga:
            LIST = 'otaku/author_manga/author_manga_list.html'
            CREATE = 'otaku/author_manga/author_manga_form.html'
            UPDATE = 'otaku/author_manga/author_manga_form.html'
            DETAIL = 'otaku/author_manga/author_manga_detail.html'
        class Character:
            LIST = 'otaku/character/character_list.html'
            CREATE = 'otaku/character/character_form.html'
            UPDATE = 'otaku/character/character_form.html'
            DETAIL = 'otaku/character/character_detail.html'
        class CharacterImage:
            LIST = 'otaku/character_image/character_image_list.html'
            CREATE = 'otaku/character_image/character_image_form.html'
            UPDATE = 'otaku/character_image/character_image_form.html'
            DETAIL = 'otaku/character_image/character_image_detail.html'
        class CharacterImageExtra:
            LIST = 'otaku/character_image_extra/character_image_extra_list.html'
            CREATE = 'otaku/character_image_extra/character_image_extra_form.html'
            UPDATE = 'otaku/character_image_extra/character_image_extra_form.html'
            DETAIL = 'otaku/character_image_extra/character_image_extra_detail.html'
        class CharacterNickname:
            LIST = 'otaku/character_nickname/character_nickname_list.html'
            CREATE = 'otaku/character_nickname/character_nickname_form.html'
            UPDATE = 'otaku/character_nickname/character_nickname_form.html'
            DETAIL = 'otaku/character_nickname/character_nickname_detail.html'
        class Demographic:
            LIST = 'otaku/demographic/demographic_list.html'
            CREATE = 'otaku/demographic/demographic_form.html'
            UPDATE = 'otaku/demographic/demographic_form.html'
            DETAIL = 'otaku/demographic/demographic_detail.html'
        class Genre:
            LIST = 'otaku/genre/genre_list.html'
            CREATE = 'otaku/genre/genre_form.html'
            UPDATE = 'otaku/genre/genre_form.html'
            DETAIL = 'otaku/genre/genre_detail.html'
        class Licensor:
            LIST = 'otaku/licensor/licensor_list.html'
            CREATE = 'otaku/licensor/licensor_form.html'
            UPDATE = 'otaku/licensor/licensor_form.html'
            DETAIL = 'otaku/licensor/licensor_detail.html'
        class Manga:
            LIST = 'otaku/manga/manga_list.html'
            CREATE = 'otaku/manga/manga_form.html'
            UPDATE = 'otaku/manga/manga_form.html'
            DETAIL = 'otaku/manga/manga_detail.html'
        class MangaCharacter:
            LIST = 'otaku/manga_character/manga_character_list.html'
            CREATE = 'otaku/manga_character/manga_character_form.html'
            UPDATE = 'otaku/manga_character/manga_character_form.html'
            DETAIL = 'otaku/manga_character/manga_character_detail.html'
        class MangaImage:
            LIST = 'otaku/manga_image/manga_image_list.html'
            CREATE = 'otaku/manga_image/manga_image_form.html'
            UPDATE = 'otaku/manga_image/manga_image_form.html'
            DETAIL = 'otaku/manga_image/manga_image_detail.html'
        class MangaImageExtra:
            LIST = 'otaku/manga_image_extra/manga_image_extra_list.html'
            CREATE = 'otaku/manga_image_extra/manga_image_extra_form.html'
            UPDATE = 'otaku/manga_image_extra/manga_image_extra_form.html'
            DETAIL = 'otaku/manga_image_extra/manga_image_extra_detail.html'
        class MediaRelation:
            LIST = 'otaku/media_relation/media_relation_list.html'
            CREATE = 'otaku/media_relation/media_relation_form.html'
            UPDATE = 'otaku/media_relation/media_relation_form.html'
            DETAIL = 'otaku/media_relation/media_relation_detail.html'
        class Person:
            LIST = 'otaku/person/person_list.html'
            CREATE = 'otaku/person/person_form.html'
            UPDATE = 'otaku/person/person_form.html'
            DETAIL = 'otaku/person/person_detail.html'
        class PersonImage:
            LIST = 'otaku/person_image/person_image_list.html'
            CREATE = 'otaku/person_image/person_image_form.html'
            UPDATE = 'otaku/person_image/person_image_form.html'
            DETAIL = 'otaku/person_image/person_image_detail.html'
        class PersonImageExtra:
            LIST = 'otaku/person_image_extra/person_image_extra_list.html'
            CREATE = 'otaku/person_image_extra/person_image_extra_form.html'
            UPDATE = 'otaku/person_image_extra/person_image_extra_form.html'
            DETAIL = 'otaku/person_image_extra/person_image_extra_detail.html'
        class PersonNickname:
            LIST = 'otaku/person_nickname/person_nickname_list.html'
            CREATE = 'otaku/person_nickname/person_nickname_form.html'
            UPDATE = 'otaku/person_nickname/person_nickname_form.html'
            DETAIL = 'otaku/person_nickname/person_nickname_detail.html'
        class Producer:
            LIST = 'otaku/producer/producer_list.html'
            CREATE = 'otaku/producer/producer_form.html'
            UPDATE = 'otaku/producer/producer_form.html'
            DETAIL = 'otaku/producer/producer_detail.html'
        class Rating:
            LIST = 'otaku/rating/rating_list.html'
            CREATE = 'otaku/rating/rating_form.html'
            UPDATE = 'otaku/rating/rating_form.html'
            DETAIL = 'otaku/rating/rating_detail.html'
        class RelationType:
            LIST = 'otaku/relation_type/relation_type_list.html'
            CREATE = 'otaku/relation_type/relation_type_form.html'
            UPDATE = 'otaku/relation_type/relation_type_form.html'
            DETAIL = 'otaku/relation_type/relation_type_detail.html'
        class Role:
            LIST = 'otaku/role/role_list.html'
            CREATE = 'otaku/role/role_form.html'
            UPDATE = 'otaku/role/role_form.html'
            DETAIL = 'otaku/role/role_detail.html'
        class Season:
            LIST = 'otaku/season/season_list.html'
            CREATE = 'otaku/season/season_form.html'
            UPDATE = 'otaku/season/season_form.html'
            DETAIL = 'otaku/season/season_detail.html'
        class SeasonFull:
            LIST = 'otaku/season_full/season_full_list.html'
            CREATE = 'otaku/season_full/season_full_form.html'
            UPDATE = 'otaku/season_full/season_full_form.html'
            DETAIL = 'otaku/season_full/season_full_detail.html'
        class Serialization:
            LIST = 'otaku/serialization/serialization_list.html'
            CREATE = 'otaku/serialization/serialization_form.html'
            UPDATE = 'otaku/serialization/serialization_form.html'
            DETAIL = 'otaku/serialization/serialization_detail.html'
        class Source:
            LIST = 'otaku/source/source_list.html'
            CREATE = 'otaku/source/source_form.html'
            UPDATE = 'otaku/source/source_form.html'
            DETAIL = 'otaku/source/source_detail.html'
        class Status:
            LIST = 'otaku/status/status_list.html'
            CREATE = 'otaku/status/status_form.html'
            UPDATE = 'otaku/status/status_form.html'
            DETAIL = 'otaku/status/status_detail.html'
        class Studio:
            LIST = 'otaku/studio/studio_list.html'
            CREATE = 'otaku/studio/studio_form.html'
            UPDATE = 'otaku/studio/studio_form.html'
            DETAIL = 'otaku/studio/studio_detail.html'
        class Theme:
            LIST = 'otaku/theme/theme_list.html'
            CREATE = 'otaku/theme/theme_form.html'
            UPDATE = 'otaku/theme/theme_form.html'
            DETAIL = 'otaku/theme/theme_detail.html'
        class TitleAnime:
            LIST = 'otaku/title_anime/title_anime_list.html'
            CREATE = 'otaku/title_anime/title_anime_form.html'
            UPDATE = 'otaku/title_anime/title_anime_form.html'
            DETAIL = 'otaku/title_anime/title_anime_detail.html'
        class TitleManga:
            LIST = 'otaku/title_manga/title_manga_list.html'
            CREATE = 'otaku/title_manga/title_manga_form.html'
            UPDATE = 'otaku/title_manga/title_manga_form.html'
            DETAIL = 'otaku/title_manga/title_manga_detail.html'
        class Type:
            LIST = 'otaku/type/type_list.html'
            CREATE = 'otaku/type/type_form.html'
            UPDATE = 'otaku/type/type_form.html'
            DETAIL = 'otaku/type/type_detail.html'
        class VoiceCharacter:
            LIST = 'otaku/voice_character/voice_character_list.html'
            CREATE = 'otaku/voice_character/voice_character_form.html'
            UPDATE = 'otaku/voice_character/voice_character_form.html'
            DETAIL = 'otaku/voice_character/voice_character_detail.html'
        class Year:
            LIST = 'otaku/year/year_list.html'
            CREATE = 'otaku/year/year_form.html'
            UPDATE = 'otaku/year/year_form.html'
            DETAIL = 'otaku/year/year_detail.html'


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
            LIST = 'renpy/censorship/censorship_list.html'
            CREATE = 'renpy/censorship/censorship_form.html'
            UPDATE = 'renpy/censorship/censorship_form.html'
            DETAIL = 'renpy/censorship/censorship_detail.html'
        class Developer:
            LIST = 'renpy/developer/developer_list.html'
            CREATE = 'renpy/developer/developer_form.html'
            UPDATE = 'renpy/developer/developer_form.html'
            DETAIL = 'renpy/developer/developer_detail.html'
        class DeveloperImage:
            LIST = 'renpy/developer_image/developer_image_list.html'
            CREATE = 'renpy/developer_image/developer_image_form.html'
            UPDATE = 'renpy/developer_image/developer_image_form.html'
            DETAIL = 'renpy/developer_image/developer_image_detail.html'
        class DeveloperImageExtra:
            LIST = 'renpy/developer_image_extra/developer_image_extra_list.html'
            CREATE = 'renpy/developer_image_extra/developer_image_extra_form.html'
            UPDATE = 'renpy/developer_image_extra/developer_image_extra_form.html'
            DETAIL = 'renpy/developer_image_extra/developer_image_extra_detail.html'
        class DeveloperLink:
            LIST = 'renpy/developer_link/developer_link_list.html'
            CREATE = 'renpy/developer_link/developer_link_form.html'
            UPDATE = 'renpy/developer_link/developer_link_form.html'
            DETAIL = 'renpy/developer_link/developer_link_detail.html'
        class Game:
            BASE = 'renpy/game/'
            LIST = BASE + 'game_list.html'
            CREATE = BASE + 'game_form.html'
            UPDATE = BASE + 'game_form.html'
            DETAIL = BASE + 'game_detail.html'
            LOAD = BASE + 'game_load.html'
            GAME_BY = BASE + 'games_by.html'
        class GameEngine:
            BASE = 'renpy/game_engine/'
            LIST = BASE + 'game_engine_list.html'
            CREATE = BASE + 'game_engine_form.html'
            UPDATE = BASE + 'game_engine_form.html'
            DETAIL = BASE + 'game_engine_detail.html'
        class GameImage:
            BASE = 'renpy/game_image/'
            LIST = BASE + 'game_image_list.html'
            CREATE = BASE + 'game_image_form.html'
            UPDATE = BASE + 'game_image_form.html'
            DETAIL = BASE + 'game_image_detail.html'
        class GameImageExtra:
            BASE = 'renpy/game_image_extra/'
            LIST = BASE + 'game_image_extra_list.html'
            CREATE = BASE + 'game_image_extra_form.html'
            UPDATE = BASE + 'game_image_extra_form.html'
            DETAIL = BASE + 'game_image_extra_detail.html'
        class Genre:
            LIST = 'renpy/genre/genre_list.html'
            CREATE = 'renpy/genre/genre_form.html'
            UPDATE = 'renpy/genre/genre_form.html'
            DETAIL = 'renpy/genre/genre_detail.html'
        class Platform:
            LIST = 'renpy/platform/platform_list.html'
            CREATE = 'renpy/platform/platform_form.html'
            UPDATE = 'renpy/platform/platform_form.html'
            DETAIL = 'renpy/platform/platform_detail.html'
        class Prefix:
            LIST = 'renpy/prefix/prefix_list.html'
            CREATE = 'renpy/prefix/prefix_form.html'
            UPDATE = 'renpy/prefix/prefix_form.html'
            DETAIL = 'renpy/prefix/prefix_detail.html'
        class Publisher:
            LIST = 'renpy/publisher/publisher_list.html'
            CREATE = 'renpy/publisher/publisher_form.html'
            UPDATE = 'renpy/publisher/publisher_form.html'
            DETAIL = 'renpy/publisher/publisher_detail.html'
        class PublisherImage:
            LIST = 'renpy/publisher_image/publisher_image_list.html'
            CREATE = 'renpy/publisher_image/publisher_image_form.html'
            UPDATE = 'renpy/publisher_image/publisher_image_form.html'
            DETAIL = 'renpy/publisher_image/publisher_image_detail.html'
        class PublisherImageExtra:
            LIST = 'renpy/publisher_image_extra/publisher_image_extra_list.html'
            CREATE = 'renpy/publisher_image_extra/publisher_image_extra_form.html'
            UPDATE = 'renpy/publisher_image_extra/publisher_image_extra_form.html'
            DETAIL = 'renpy/publisher_image_extra/publisher_image_extra_detail.html'
        class PublisherLink:
            LIST = 'renpy/publisher_link/publisher_link_list.html'
            CREATE = 'renpy/publisher_link/publisher_link_form.html'
            UPDATE = 'renpy/publisher_link/publisher_link_form.html'
            DETAIL = 'renpy/publisher_link/publisher_link_detail.html'
        class Status:
            LIST = 'renpy/status/status_list.html'
            CREATE = 'renpy/status/status_form.html'
            UPDATE = 'renpy/status/status_form.html'
            DETAIL = 'renpy/status/status_detail.html'
        class TitleGame:
            LIST = 'renpy/title_game/title_game_list.html'
            CREATE = 'renpy/title_game/title_game_form.html'
            UPDATE = 'renpy/title_game/title_game_form.html'
            DETAIL = 'renpy/title_game/title_game_detail.html'
        class Translator:
            LIST = 'renpy/translator/translator_list.html'
            CREATE = 'renpy/translator/translator_form.html'
            UPDATE = 'renpy/translator/translator_form.html'
            DETAIL = 'renpy/translator/translator_detail.html'
        class TranslatorImage:
            LIST = 'renpy/translator_image/translator_image_list.html'
            CREATE = 'renpy/translator_image/translator_image_form.html'
            UPDATE = 'renpy/translator_image/translator_image_form.html'
            DETAIL = 'renpy/translator_image/translator_image_detail.html'
        class TranslatorImageExtra:
            LIST = 'renpy/translator_image_extra/translator_image_extra_list.html'
            CREATE = 'renpy/translator_image_extra/translator_image_extra_form.html'
            UPDATE = 'renpy/translator_image_extra/translator_image_extra_form.html'
            DETAIL = 'renpy/translator_image_extra/translator_image_extra_detail.html'
        class TranslatorLink:
            LIST = 'renpy/translator_link/translator_link_list.html'
            CREATE = 'renpy/translator_link/translator_link_form.html'
            UPDATE = 'renpy/translator_link/translator_link_form.html'
            DETAIL = 'renpy/translator_link/translator_link_detail.html'
        class GameData:
            LIST = 'renpy/game_data/game_data_list.html'
            CREATE = 'renpy/game_data/game_data_form.html'
            UPDATE = 'renpy/game_data/game_data_form.html'
            DETAIL = 'renpy/game_data/game_data_detail.html'

    class Serie:
        class Company:
            LIST = 'serie/company/company_list.html'
            CREATE = 'serie/company/company_form.html'
            UPDATE = 'serie/company/company_form.html'
            DETAIL = 'serie/company/company_detail.html'
        class Genre:
            LIST = 'serie/genre/genre_list.html'
            CREATE = 'serie/genre/genre_form.html'
            UPDATE = 'serie/genre/genre_form.html'
            DETAIL = 'serie/genre/genre_detail.html'
        class Rating:
            LIST = 'serie/rating/rating_list.html'
            CREATE = 'serie/rating/rating_form.html'
            UPDATE = 'serie/rating/rating_form.html'
            DETAIL = 'serie/rating/rating_detail.html'

        class Role:
            LIST = 'serie/role/role_list.html'
            CREATE = 'serie/role/role_form.html'
            UPDATE = 'serie/role/role_form.html'
            DETAIL = 'serie/role/role_detail.html'

        class Serie:
            LIST = 'serie/serie/serie_list.html'
            CREATE = 'serie/serie/serie_form.html'
            UPDATE = 'serie/serie/serie_form.html'
            DETAIL = 'serie/serie/serie_detail.html'

        class SerieCast:
            LIST = 'serie/serie_cast/serie_cast_list.html'
            CREATE = 'serie/serie_cast/serie_cast_form.html'
            UPDATE = 'serie/serie_cast/serie_cast_form.html'
            DETAIL = 'serie/serie_cast/serie_cast_detail.html'

        class SerieImage:
            LIST = 'serie/serie_image/serie_image_list.html'
            CREATE = 'serie/serie_image/serie_image_form.html'
            UPDATE = 'serie/serie_image/serie_image_form.html'
            DETAIL = 'serie/serie_image/serie_image_detail.html'

        class SerieImageExtra:
            LIST = 'serie/serie_image_extra/serie_image_extra_list.html'
            CREATE = 'serie/serie_image_extra/serie_image_extra_form.html'
            UPDATE = 'serie/serie_image_extra/serie_image_extra_form.html'
            DETAIL = 'serie/serie_image_extra/serie_image_extra_detail.html'

        class SerieStaff:
            LIST = 'serie/serie_staff/serie_staff_list.html'
            CREATE = 'serie/serie_staff/serie_staff_form.html'
            UPDATE = 'serie/serie_staff/serie_staff_form.html'
            DETAIL = 'serie/serie_staff/serie_staff_detail.html'

        class TitleSerie:
            LIST = 'serie/title_serie/title_serie_list.html'
            CREATE = 'serie/title_serie/title_serie_form.html'
            UPDATE = 'serie/title_serie/title_serie_form.html'
            DETAIL = 'serie/title_serie/title_serie_detail.html'

        class Type:
            LIST = 'serie/type/type_list.html'
            CREATE = 'serie/type/type_form.html'
            UPDATE = 'serie/type/type_form.html'
            DETAIL = 'serie/type/type_detail.html'

####################################################    URLS
class URLS:
    class Main:
        INDEX = 'pages_app:index'
        CONTACT = 'pages_app:contact'
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
        LIST =       'users_app:users_list'
        CREATE =       'users_app:users_create'
        UPDATE =       'users_app:users_UPDATE'
        DETAIL =       'users_app:users_detail'
        CREATE_SUPER = 'users_app:superuser_create'
        CREATE_STAFF = 'users_app:staffuser_create'

    class Common:
        class Country:
            LIST = 'common_app:country_list'
            CREATE = 'common_app:country_create'
            UPDATE = 'common_app:country_UPDATE'
            DETAIL = 'common_app:country_detail'

        class Format:
            LIST = 'common_app:format_list'
            CREATE = 'common_app:format_create'
            UPDATE = 'common_app:format_UPDATE'
            DETAIL = 'common_app:format_detail'

        class ImageSize:
            LIST = 'common_app:image_size_list'
            CREATE = 'common_app:image_size_create'
            UPDATE = 'common_app:image_size_UPDATE'
            DETAIL = 'common_app:image_size_detail'

        class Language:
            LIST = 'common_app:language_list'
            CREATE = 'common_app:language_create'
            UPDATE = 'common_app:language_UPDATE'
            DETAIL = 'common_app:language_detail'

        class Person:
            LIST = 'common_app:person_list'
            CREATE = 'common_app:person_create'
            UPDATE = 'common_app:person_UPDATE'
            DETAIL = 'common_app:person_detail'

        class PersonImage:
            LIST = 'common_app:person_image_list'
            CREATE = 'common_app:person_image_create'
            UPDATE = 'common_app:person_image_UPDATE'
            DETAIL = 'common_app:person_image_detail'

        class PersonImageExtra:
            LIST = 'common_app:person_image_extra_list'
            CREATE = 'common_app:person_image_extra_create'
            UPDATE = 'common_app:person_image_extra_UPDATE'
            DETAIL = 'common_app:person_image_extra_detail'

        class PersonNickname:
            LIST = 'common_app:person_nickname_list'
            CREATE = 'common_app:person_nickname_create'
            UPDATE = 'common_app:person_nickname_UPDATE'
            DETAIL = 'common_app:person_nickname_detail'

        class Quality:
            LIST = 'common_app:quality_list'
            CREATE = 'common_app:quality_create'
            UPDATE = 'common_app:quality_UPDATE'
            DETAIL = 'common_app:quality_detail'

        class Website:
            LIST = 'common_app:website_list'
            CREATE = 'common_app:website_create'
            UPDATE = 'common_app:website_UPDATE'
            DETAIL = 'common_app:website_detail'

    class Movie:
        class Company:
            LIST = 'movie_app:company_list'
            CREATE = 'movie_app:company_create'
            UPDATE = 'movie_app:company_UPDATE'
            DETAIL = 'movie_app:company_detail'

        class Genre:
            LIST = 'movie_app:genre_list'
            CREATE = 'movie_app:genre_create'
            UPDATE = 'movie_app:genre_UPDATE'
            DETAIL = 'movie_app:genre_detail'

        class Movie:
            LIST = 'movie_app:movie_list'
            CREATE = 'movie_app:movie_create'
            UPDATE = 'movie_app:movie_UPDATE'
            DETAIL = 'movie_app:movie_detail'

        class MovieCast:
            LIST = 'movie_app:movie_cast_list'
            CREATE = 'movie_app:movie_cast_create'
            UPDATE = 'movie_app:movie_cast_UPDATE'
            DETAIL = 'movie_app:movie_cast_detail'

        class MovieImage:
            LIST = 'movie_app:movie_image_list'
            CREATE = 'movie_app:movie_image_create'
            UPDATE = 'movie_app:movie_image_UPDATE'
            DETAIL = 'movie_app:movie_image_detail'

        class MovieImageExtra:
            LIST = 'movie_app:movie_image_extra_list'
            CREATE = 'movie_app:movie_image_extra_create'
            UPDATE = 'movie_app:movie_image_extra_UPDATE'
            DETAIL = 'movie_app:movie_image_extra_detail'

        class MovieStaff:
            LIST = 'movie_app:movie_image_staff_list'
            CREATE = 'movie_app:movie_image_staff_create'
            UPDATE = 'movie_app:movie_image_staff_UPDATE'
            DETAIL = 'movie_app:movie_image_staff_detail'

        class Rating:
            LIST = 'movie_app:rating_list'
            CREATE = 'movie_app:rating_create'
            UPDATE = 'movie_app:rating_UPDATE'
            DETAIL = 'movie_app:rating_detail'

        class Role:
            LIST = 'movie_app:role_list'
            CREATE = 'movie_app:role_create'
            UPDATE = 'movie_app:role_UPDATE'
            DETAIL = 'movie_app:role_detail'

        class TitleMovie:
            LIST = 'movie_app:title_movie_list'
            CREATE = 'movie_app:title_movie_create'
            UPDATE = 'movie_app:title_movie_UPDATE'
            DETAIL = 'movie_app:title_movie_detail'

        class Type:
            LIST = 'movie_app:type_list'
            CREATE = 'movie_app:type_create'
            UPDATE = 'movie_app:type_UPDATE'
            DETAIL = 'movie_app:type_detail'

    class Music:
        class Album:
            LIST = 'music_app:album_list'
            CREATE = 'music_app:album_create'
            UPDATE = 'music_app:album_UPDATE'
            DETAIL = 'music_app:album_detail'

        class AlbumImage:
            LIST = 'music_app:album_image_list'
            CREATE = 'music_app:album_image_create'
            UPDATE = 'music_app:album_image_UPDATE'
            DETAIL = 'music_app:album_image_detail'

        class AlbumImageExtra:
            LIST = 'music_app:album_image_extra_list'
            CREATE = 'music_app:album_image_extra_create'
            UPDATE = 'music_app:album_image_extra_UPDATE'
            DETAIL = 'music_app:album_image_extra_detail'

        class AlbumType:
            LIST = 'music_app:album_type_list'
            CREATE = 'music_app:album_type_create'
            UPDATE = 'music_app:album_type_UPDATE'
            DETAIL = 'music_app:album_type_detail'

        class Artist:
            LIST = 'music_app:artist_list'
            CREATE = 'music_app:artist_create'
            UPDATE = 'music_app:artist_UPDATE'
            DETAIL = 'music_app:artist_detail'

        class ArtistImage:
            LIST = 'music_app:artist_image_list'
            CREATE = 'music_app:artist_image_create'
            UPDATE = 'music_app:artist_image_UPDATE'
            DETAIL = 'music_app:artist_image_detail'

        class ArtistImageExtra:
            LIST = 'music_app:artist_image_extra_list'
            CREATE = 'music_app:artist_image_extra_create'
            UPDATE = 'music_app:artist_image_extra_UPDATE'
            DETAIL = 'music_app:artist_image_extra_detail'

        class ArtistMember:
            LIST = 'music_app:artist_member_list'
            CREATE = 'music_app:artist_member_create'
            UPDATE = 'music_app:artist_member_UPDATE'
            DETAIL = 'music_app:artist_member_detail'

        class ArtistType:
            LIST = 'music_app:artist_type_list'
            CREATE = 'music_app:artist_type_create'
            UPDATE = 'music_app:artist_type_UPDATE'
            DETAIL = 'music_app:artist_type_detail'

        class Genre:
            LIST = 'music_app:genre_list'
            CREATE = 'music_app:genre_create'
            UPDATE = 'music_app:genre_UPDATE'
            DETAIL = 'music_app:genre_detail'

        class Role:
            LIST = 'music_app:role_list'
            CREATE = 'music_app:role_create'
            UPDATE = 'music_app:role_UPDATE'
            DETAIL = 'music_app:role_detail'

        class Song:
            LIST = 'music_app:song_list'
            CREATE = 'music_app:song_create'
            UPDATE = 'music_app:song_UPDATE'
            DETAIL = 'music_app:song_detail'

    class Otaku:
        class Load:
            ANIME = 'otaku_app:anime_load'
            MANGA = 'otaku_app:manga_load'
            PERSON = 'otaku_app:person_load'
            CHARACTER = 'otaku_app:character_load'

        class Anime:
            LIST = 'otaku_app:anime_list'
            CREATE = 'otaku_app:anime_create'
            UPDATE = 'otaku_app:anime_UPDATE'
            DETAIL = 'otaku_app:anime_detail'

        class AnimeCharacter:
            LIST = 'otaku_app:anime_character_list'
            CREATE = 'otaku_app:anime_character_create'
            UPDATE = 'otaku_app:anime_character_UPDATE'
            DETAIL = 'otaku_app:anime_character_detail'

        class AnimeImage:
            LIST = 'otaku_app:anime_image_list'
            CREATE = 'otaku_app:anime_image_create'
            UPDATE = 'otaku_app:anime_image_UPDATE'
            DETAIL = 'otaku_app:anime_image_detail'

        class AnimeImageExtra:
            LIST = 'otaku_app:anime_image_extra_list'
            CREATE = 'otaku_app:anime_image_extra_create'
            UPDATE = 'otaku_app:anime_image_extra_UPDATE'
            DETAIL = 'otaku_app:anime_image_extra_detail'

        class AnimeSong:
            LIST = 'otaku_app:anime_image_song_list'
            CREATE = 'otaku_app:anime_image_song_create'
            UPDATE = 'otaku_app:anime_image_song_UPDATE'
            DETAIL = 'otaku_app:anime_image_song_detail'

        class AnimeStaff:
            LIST = 'otaku_app:anime_staff_list'
            CREATE = 'otaku_app:anime_staff_create'
            UPDATE = 'otaku_app:anime_staff_UPDATE'
            DETAIL = 'otaku_app:anime_staff_detail'

        class AuthorManga:
            LIST = 'otaku_app:author_manga_list'
            CREATE = 'otaku_app:author_manga_create'
            UPDATE = 'otaku_app:author_manga_UPDATE'
            DETAIL = 'otaku_app:author_manga_detail'

        class Character:
            LIST = 'otaku_app:character_list'
            CREATE = 'otaku_app:character_create'
            UPDATE = 'otaku_app:character_UPDATE'
            DETAIL = 'otaku_app:character_detail'

        class CharacterImage:
            LIST = 'otaku_app:character_image_list'
            CREATE = 'otaku_app:character_image_create'
            UPDATE = 'otaku_app:character_image_UPDATE'
            DETAIL = 'otaku_app:character_image_detail'

        class CharacterImageExtra:
            LIST = 'otaku_app:character_image_extra_list'
            CREATE = 'otaku_app:character_image_extra_create'
            UPDATE = 'otaku_app:character_image_extra_UPDATE'
            DETAIL = 'otaku_app:character_image_extra_detail'

        class CharacterNickname:
            LIST = 'otaku_app:character_nickname_list'
            CREATE = 'otaku_app:character_nickname_create'
            UPDATE = 'otaku_app:character_nickname_UPDATE'
            DETAIL = 'otaku_app:character_nickname_detail'

        class Demographic:
            LIST = 'otaku_app:demographic_list'
            CREATE = 'otaku_app:demographic_create'
            UPDATE = 'otaku_app:demographic_UPDATE'
            DETAIL = 'otaku_app:demographic_detail'

        class Genre:
            LIST = 'otaku_app:genre_list'
            CREATE = 'otaku_app:genre_create'
            UPDATE = 'otaku_app:genre_UPDATE'
            DETAIL = 'otaku_app:genre_detail'

        class Licensor:
            LIST = 'otaku_app:licensor_list'
            CREATE = 'otaku_app:licensor_create'
            UPDATE = 'otaku_app:licensor_UPDATE'
            DETAIL = 'otaku_app:licensor_detail'

        class Manga:
            LIST = 'otaku_app:manga_list'
            CREATE = 'otaku_app:manga_create'
            UPDATE = 'otaku_app:manga_UPDATE'
            DETAIL = 'otaku_app:manga_detail'

        class MangaCharacter:
            LIST = 'otaku_app:manga_character_list'
            CREATE = 'otaku_app:manga_character_create'
            UPDATE = 'otaku_app:manga_character_UPDATE'
            DETAIL = 'otaku_app:manga_character_detail'

        class MangaImage:
            LIST = 'otaku_app:manga_image_list'
            CREATE = 'otaku_app:manga_image_create'
            UPDATE = 'otaku_app:manga_image_UPDATE'
            DETAIL = 'otaku_app:manga_image_detail'

        class MangaImageExtra:
            LIST = 'otaku_app:manga_image_extra_list'
            CREATE = 'otaku_app:manga_image_extra_create'
            UPDATE = 'otaku_app:manga_image_extra_UPDATE'
            DETAIL = 'otaku_app:manga_image_extra_detail'

        class MediaRelation:
            LIST = 'otaku_app:media_relation_list'
            CREATE = 'otaku_app:media_relation_create'
            UPDATE = 'otaku_app:media_relation_UPDATE'
            DETAIL = 'otaku_app:media_relation_detail'

        class Person:
            LIST = 'otaku_app:person_list'
            CREATE = 'otaku_app:person_create'
            UPDATE = 'otaku_app:person_UPDATE'
            DETAIL = 'otaku_app:person_detail'

        class PersonImage:
            LIST = 'otaku_app:person_image_list'
            CREATE = 'otaku_app:person_image_create'
            UPDATE = 'otaku_app:person_image_UPDATE'
            DETAIL = 'otaku_app:person_image_detail'

        class PersonImageExtra:
            LIST = 'otaku_app:person_image_extra_list'
            CREATE = 'otaku_app:person_image_extra_create'
            UPDATE = 'otaku_app:person_image_extra_UPDATE'
            DETAIL = 'otaku_app:person_image_extra_detail'

        class PersonNickname:
            LIST = 'otaku_app:person_nickname_list'
            CREATE = 'otaku_app:person_nickname_create'
            UPDATE = 'otaku_app:person_nickname_UPDATE'
            DETAIL = 'otaku_app:person_nickname_detail'

        class Producer:
            LIST = 'otaku_app:producer_list'
            CREATE = 'otaku_app:producer_create'
            UPDATE = 'otaku_app:producer_UPDATE'
            DETAIL = 'otaku_app:producer_detail'

        class Rating:
            LIST = 'otaku_app:rating_list'
            CREATE = 'otaku_app:rating_create'
            UPDATE = 'otaku_app:rating_UPDATE'
            DETAIL = 'otaku_app:rating_detail'

        class RelationType:
            LIST = 'otaku_app:relation_type_list'
            CREATE = 'otaku_app:relation_type_create'
            UPDATE = 'otaku_app:relation_type_UPDATE'
            DETAIL = 'otaku_app:relation_type_detail'

        class Role:
            LIST = 'otaku_app:role_list'
            CREATE = 'otaku_app:role_create'
            UPDATE = 'otaku_app:role_UPDATE'
            DETAIL = 'otaku_app:role_detail'

        class Season:
            LIST = 'otaku_app:season_list'
            CREATE = 'otaku_app:season_create'
            UPDATE = 'otaku_app:season_UPDATE'
            DETAIL = 'otaku_app:season_detail'

        class SeasonFull:
            LIST = 'otaku_app:season_full_list'
            CREATE = 'otaku_app:season_full_create'
            UPDATE = 'otaku_app:season_full_UPDATE'
            DETAIL = 'otaku_app:season_full_detail'

        class Serialization:
            LIST = 'otaku_app:serialization_list'
            CREATE = 'otaku_app:serialization_create'
            UPDATE = 'otaku_app:serialization_UPDATE'
            DETAIL = 'otaku_app:serialization_detail'

        class Source:
            LIST = 'otaku_app:source_list'
            CREATE = 'otaku_app:source_create'
            UPDATE = 'otaku_app:source_UPDATE'
            DETAIL = 'otaku_app:source_detail'

        class Status:
            LIST = 'otaku_app:status_list'
            CREATE = 'otaku_app:status_create'
            UPDATE = 'otaku_app:status_UPDATE'
            DETAIL = 'otaku_app:status_detail'

        class Studio:
            LIST = 'otaku_app:studio_list'
            CREATE = 'otaku_app:studio_create'
            UPDATE = 'otaku_app:studio_UPDATE'
            DETAIL = 'otaku_app:studio_detail'

        class Theme:
            LIST = 'otaku_app:theme_list'
            CREATE = 'otaku_app:theme_create'
            UPDATE = 'otaku_app:theme_UPDATE'
            DETAIL = 'otaku_app:theme_detail'

        class TitleAnime:
            LIST = 'otaku_app:title_anime_list'
            CREATE = 'otaku_app:title_anime_create'
            UPDATE = 'otaku_app:title_anime_UPDATE'
            DETAIL = 'otaku_app:title_anime_detail'

        class TitleManga:
            LIST = 'otaku_app:title_manga_list'
            CREATE = 'otaku_app:title_manga_create'
            UPDATE = 'otaku_app:title_manga_UPDATE'
            DETAIL = 'otaku_app:title_manga_detail'

        class Type:
            LIST = 'otaku_app:type_list'
            CREATE = 'otaku_app:type_create'
            UPDATE = 'otaku_app:type_UPDATE'
            DETAIL = 'otaku_app:type_detail'

        class VoiceCharacter:
            LIST = 'otaku_app:voice_character_list'
            CREATE = 'otaku_app:voice_character_create'
            UPDATE = 'otaku_app:voice_character_UPDATE'
            DETAIL = 'otaku_app:voice_character_detail'

        class Year:
            LIST = 'otaku_app:year_list'
            CREATE = 'otaku_app:year_create'
            UPDATE = 'otaku_app:year_UPDATE'
            DETAIL = 'otaku_app:year_detail'

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
            LIST = 'renpy_app:censorship_list'
            CREATE = 'renpy_app:censorship_create'
            UPDATE = 'renpy_app:censorship_UPDATE'
            DETAIL = 'renpy_app:censorship_detail'

        class Developer:
            LIST = 'renpy_app:developer_list'
            CREATE = 'renpy_app:developer_create'
            UPDATE = 'renpy_app:developer_UPDATE'
            DETAIL = 'renpy_app:developer_detail'

        class DeveloperImage:
            LIST = 'renpy_app:developer_image_list'
            CREATE = 'renpy_app:developer_image_create'
            UPDATE = 'renpy_app:developer_image_UPDATE'
            DETAIL = 'renpy_app:developer_image_detail'

        class DeveloperImageExtra:
            LIST = 'renpy_app:developer_image_extra_list'
            CREATE = 'renpy_app:developer_image_extra_create'
            UPDATE = 'renpy_app:developer_image_extra_UPDATE'
            DETAIL = 'renpy_app:developer_image_extra_detail'

        class DeveloperLink:
            LIST = 'renpy_app:developer_link_list'
            CREATE = 'renpy_app:developer_link_create'
            UPDATE = 'renpy_app:developer_link_UPDATE'
            DETAIL = 'renpy_app:developer_link_detail'

        class Game:
            LIST = 'renpy_app:game_list'
            CREATE = 'renpy_app:game_create'
            UPDATE = 'renpy_app:game_UPDATE'
            DETAIL = 'renpy_app:game_detail'
            LOAD = 'renpy_app:game_load'

        class GameEngine:
            LIST = 'renpy_app:game_engine_list'
            CREATE = 'renpy_app:game_engine_create'
            UPDATE = 'renpy_app:game_engine_UPDATE'
            DETAIL = 'renpy_app:game_engine_detail'

        class GameImage:
            LIST = 'renpy_app:game_image_list'
            CREATE = 'renpy_app:game_image_create'
            UPDATE = 'renpy_app:game_image_UPDATE'
            DETAIL = 'renpy_app:game_image_detail'

        class GameImageExtra:
            LIST = 'renpy_app:game_image_extra_list'
            CREATE = 'renpy_app:game_image_extra_create'
            UPDATE = 'renpy_app:game_image_extra_UPDATE'
            DETAIL = 'renpy_app:game_image_extra_detail'

        class Genre:
            LIST = 'renpy_app:genre_list'
            CREATE = 'renpy_app:genre_create'
            UPDATE = 'renpy_app:genre_UPDATE'
            DETAIL = 'renpy_app:genre_detail'

        class Platform:
            LIST = 'renpy_app:platform_list'
            CREATE = 'renpy_app:platform_create'
            UPDATE = 'renpy_app:platform_UPDATE'
            DETAIL = 'renpy_app:platform_detail'

        class Prefix:
            LIST = 'renpy_app:prefix_list'
            CREATE = 'renpy_app:prefix_create'
            UPDATE = 'renpy_app:prefix_UPDATE'
            DETAIL = 'renpy_app:prefix_detail'

        class Publisher:
            LIST = 'renpy_app:publisher_list'
            CREATE = 'renpy_app:publisher_create'
            UPDATE = 'renpy_app:publisher_UPDATE'
            DETAIL = 'renpy_app:publisher_detail'

        class PublisherImage:
            LIST = 'renpy_app:publisher_image_list'
            CREATE = 'renpy_app:publisher_image_create'
            UPDATE = 'renpy_app:publisher_image_UPDATE'
            DETAIL = 'renpy_app:publisher_image_detail'

        class PublisherImageExtra:
            LIST = 'renpy_app:publisher_image_extra_list'
            CREATE = 'renpy_app:publisher_image_extra_create'
            UPDATE = 'renpy_app:publisher_image_extra_UPDATE'
            DETAIL = 'renpy_app:publisher_image_extra_detail'

        class PublisherLink:
            LIST = 'renpy_app:publisher_link_list'
            CREATE = 'renpy_app:publisher_link_create'
            UPDATE = 'renpy_app:publisher_link_UPDATE'
            DETAIL = 'renpy_app:publisher_link_detail'

        class Status:
            LIST = 'renpy_app:status_list'
            CREATE = 'renpy_app:status_create'
            UPDATE = 'renpy_app:status_UPDATE'
            DETAIL = 'renpy_app:status_detail'

        class TitleGame:
            LIST = 'renpy_app:title_game_list'
            CREATE = 'renpy_app:title_game_create'
            UPDATE = 'renpy_app:title_game_UPDATE'
            DETAIL = 'renpy_app:title_game_detail'

        class Translator:
            LIST = 'renpy_app:translator_list'
            CREATE = 'renpy_app:translator_create'
            UPDATE = 'renpy_app:translator_UPDATE'
            DETAIL = 'renpy_app:translator_detail'

        class TranslatorImage:
            LIST = 'renpy_app:translator_image_list'
            CREATE = 'renpy_app:translator_image_create'
            UPDATE = 'renpy_app:translator_image_UPDATE'
            DETAIL = 'renpy_app:translator_image_detail'

        class TranslatorImageExtra:
            LIST = 'renpy_app:translator_image_extra_list'
            CREATE = 'renpy_app:translator_image_extra_create'
            UPDATE = 'renpy_app:translator_image_extra_UPDATE'
            DETAIL = 'renpy_app:translator_image_extra_detail'

        class TranslatorLink:
            LIST = 'renpy_app:translator_link_list'
            CREATE = 'renpy_app:translator_link_create'
            UPDATE = 'renpy_app:translator_link_UPDATE'
            DETAIL = 'renpy_app:translator_link_detail'

        class F95GameFetchStatus:
            LIST = 'renpy_app:game_data_list'
            CREATE = 'renpy_app:game_data_create'
            UPDATE = 'renpy_app:game_data_UPDATE'
            DETAIL = 'renpy_app:game_data_detail'

    class Serie:
        class Company:
            LIST = 'serie_app :company_list'
            CREATE = 'serie_app :company_create'
            UPDATE = 'serie_app :company_UPDATE'
            DETAIL = 'serie_app :company_detail'

        class Genre:
            LIST = 'serie_app :genre_list'
            CREATE = 'serie_app :genre_create'
            UPDATE = 'serie_app :genre_UPDATE'
            DETAIL = 'serie_app :genre_detail'

        class Rating:
            LIST = 'serie_app :rating_list'
            CREATE = 'serie_app :rating_create'
            UPDATE = 'serie_app :rating_UPDATE'
            DETAIL = 'serie_app :rating_detail'

        class Role:
            LIST = 'serie_app :role_list'
            CREATE = 'serie_app :role_create'
            UPDATE = 'serie_app :role_UPDATE'
            DETAIL = 'serie_app :role_detail'

        class Serie:
            LIST = 'serie_app :serie_list'
            CREATE = 'serie_app :serie_create'
            UPDATE = 'serie_app :serie_UPDATE'
            DETAIL = 'serie_app :serie_detail'

        class SerieCast:
            LIST = 'serie_app :serie_cast_list'
            CREATE = 'serie_app :serie_cast_create'
            UPDATE = 'serie_app :serie_cast_UPDATE'
            DETAIL = 'serie_app :serie_cast_detail'

        class SerieImage:
            LIST = 'serie_app :serie_image_list'
            CREATE = 'serie_app :serie_image_create'
            UPDATE = 'serie_app :serie_image_UPDATE'
            DETAIL = 'serie_app :serie_image_detail'

        class SerieImageExtra:
            LIST = 'serie_app :serie_image_extra_list'
            CREATE = 'serie_app :serie_image_extra_create'
            UPDATE = 'serie_app :serie_image_extra_UPDATE'
            DETAIL = 'serie_app :serie_image_extra_detail'

        class SerieStaff:
            LIST = 'serie_app :serie_staff_list'
            CREATE = 'serie_app :serie_staff_create'
            UPDATE = 'serie_app :serie_staff_UPDATE'
            DETAIL = 'serie_app :serie_staff_detail'

        class TitleSerie:
            LIST = 'serie_app :title_serie_list'
            CREATE = 'serie_app :title_serie_create'
            UPDATE = 'serie_app :title_serie_UPDATE'
            DETAIL = 'serie_app :title_serie_detail'

        class Type:
            LIST = 'serie_app :type_list'
            CREATE = 'serie_app :type_create'
            UPDATE = 'serie_app :type_UPDATE'
            DETAIL = 'serie_app :type_detail'

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
        TRANSLATOR_LINK =           'bg-renpy-translator_link'
        PUBLISHER_LINK =            'bg-renpy-publisher_link'
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
        DEVELOPER_LINK =            'js/DataTables/config/renpy/renpy_developer_links.js'
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
        PUBLISHER_LINK =            'js/DataTables/config/renpy/renpy_publisher_links.js'
        STATUS =                    'js/DataTables/config/renpy/renpy_status.js'
        TITLE_GAME =                'js/DataTables/config/renpy/renpy_title_game.js'
        TRANSLATOR =                'js/DataTables/config/renpy/renpy_translator.js'
        TRANSLATOR_IMAGE =          'js/DataTables/config/renpy/renpy_translator_image.js'
        TRANSLATOR_IMAGE_EXTRA =    'js/DataTables/config/renpy/renpy_translator_image_extra.js'
        TRANSLATOR_LINK =           'js/DataTables/config/renpy/renpy_translator_links.js'

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
        DEVELOPER_LINK =            'img/screen/wide/bg-renpy-developer_link.webp'
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
        PUBLISHER_LINK =            'img/screen/wide/bg-renpy-publisher_link.webp'
        STATUS =                    'img/screen/wide/bg-renpy-status.webp'
        TITLE_GAME =                'img/screen/wide/bg-renpy-title_game.webp'
        TRANSLATOR =                'img/screen/wide/bg-renpy-translator.webp'
        TRANSLATOR_IMAGE =          'img/screen/wide/bg-renpy-translator_image.webp'
        TRANSLATOR_IMAGE_EXTRA =    'img/screen/wide/bg-renpy-translator_image_extra.webp'
        TRANSLATOR_LINK =           'img/screen/wide/bg-renpy-translator_link.webp'

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
        DEVELOPER_LINK =            'Enlace del desarrollador'
        GAME =                      'Juego Renpy'
        GAME_ENGINE =               'Motor de desarrollo'
        GAME_IMAGE =                'Imagen del juego'
        GAME_IMAGE_EXTRA =          'Imagen adicional del juego'
        GENRE =                     'Género del juego'
        PLATFORM =                  'Plataforma del juego'
        PREFIX =                    'Prefijo del juego'
        PUBLISHER =                 'Editor'
        PUBLISHER_IMAGE =           'Imagen del editor'
        PUBLISHER_IMAGE_EXTRA =     'Imagen adicional del editor'
        PUBLISHER_LINK =            'Enlace del editor'
        STATUS =                    'Estado de juego'
        TITLE_GAME =                'Título del juego'
        TRANSLATOR =                'Traductor'
        TRANSLATOR_IMAGE =          'Imagen del traductor'
        TRANSLATOR_IMAGE_EXTRA =    'Imagen adicional del traductor'
        TRANSLATOR_LINK =           'Enlace del traductor'
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
