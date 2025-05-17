class Prefixes:
    img_base = 'img/screen/wide/'

    class BaseJavaScripts:
        common =    'js/DataTables/config/common/'
        movie =     'js/DataTables/config/movie/'
        music =     'js/DataTables/config/music/'
        otaku =     'js/DataTables/config/otaku/'
        renpy =     'js/DataTables/config/renpy/'
        serie =     'js/DataTables/config/serie/'
        users =     'js/DataTables/config/users/'
    class AppName:
        common_app  = 'common_app:'
        movie_app   = 'movie_app:'
        music_app   = 'music_app:'
        otaku_app   = 'otaku_app:'
        renpy_app   = 'renpy_app:'
        serie_app   = 'serie_app:'
        users_app   = 'users_app:'
        pages_app   = 'pages_app:'

    class BaseTemplates:
        HOME = 'home/'
        class Users:
            USERS = 'users/user/'
        class Common:
            Country = 'common/country/'
            Format = 'common/format/'
            ImageSize = 'common/image_size/'
            Language = 'common/language/'
            Person = 'common/person/'
            PersonImage = 'common/person_image/'
            PersonImageExtra = 'common/person_image_extra/'
            PersonNickname = 'common/person_nickname/'
            Quality  = 'common/quality/'
            Website = 'common/website/'
        class Movie:
            Company = 'movie/company'
            Genre = 'movie/genre'
            Movie = 'movie/movie'
            MovieCast = 'movie/movie_cast'
            MovieImage = 'movie/movie_image'
            MovieImageExtra = 'movie/movie_image_extra'
            MovieStaff = 'movie/movies_taff'
            Rating = 'movie/rating'
            Role = 'movie/role'
            TitleMovie = 'movie/title_movie'
            Type = 'movie/type'
        class Music:
            Album = 'music/album'
            AlbumImage = 'music/album_image'
            AlbumImageExtra = 'music/album_image_extra'
            AlbumType = 'music/album_type'
            Artist = 'music/artist'
            ArtistImage = 'music/artist_image'
            ArtistImageExtra = 'music/artist_image_extra'
            ArtistMember = 'music/artist_member'
            ArtistType = 'music/artist_type'
            Genre = 'music/genre'
            Role = 'music/role'
            Song = 'music/song'
        class Otaku:
            Anime = 'otaku/anime'
            AnimeCharacter = 'otaku/anime_character'
            AnimeImage = 'otaku/anime_image'
            AnimeImageExtra = 'otaku/anime_image_extra'
            AnimeSong = 'otaku/anime_song'
            AnimeStaff = 'otaku/anime_staff'
            AuthorManga = 'otaku/author_manga'
            Character = 'otaku/character'
            CharacterImage = 'otaku/character_image'
            CharacterImageExtra = 'otaku/character_image_extra'
            CharacterNickname = 'otaku/character_nickname'
            Demographic = 'otaku/demographic'
            Genre = 'otaku/genre'
            Licensor = 'otaku/licensor'
            Manga = 'otaku/manga'
            MangaCharacter = 'otaku/manga_character'
            MangaImage = 'otaku/manga_image'
            MangaImageExtra = 'otaku/manga_image_extra'
            MediaRelation = 'otaku/media_relation'
            Person = 'otaku/person'
            PersonImage = 'otaku/person_image'
            PersonImageExtra = 'otaku/person_image_extra'
            PersonNickname = 'otaku/person_nickname'
            Producer = 'otaku/producer'
            Rating = 'otaku/rating'
            RelationType = 'otaku/relation_type'
            Role = 'otaku/role'
            Season = 'otaku/season'
            SeasonFull = 'otaku/season_full'
            Serialization = 'otaku/serialization'
            Source = 'otaku/source'
            Status = 'otaku/status'
            Studio = 'otaku/studio'
            Theme = 'otaku/theme'
            TitleAnime = 'otaku/title_anime'
            TitleManga = 'otaku/title_manga'
            Type = 'otaku/type'
            VoiceCharacter = 'otaku/voice_character'
            Year = 'otaku/year'

            DataAnime = 'otaku/data/anime'
            DataAnimeCharacters = 'otaku/data/anime_characters'
            DataAnimePictures = 'otaku/data/anime_pictures'
            DataAnimeStaff = 'otaku/data/anime_staff'
            DataCharacter = 'otaku/data/character'
            DataCharacterPictures = 'otaku/data/character_pictures'
            DataImageURL = 'otaku/data/image_url'
            DataManga = 'otaku/data/manga'
            DataMangaCharacters = 'otaku/data/manga_characters'
            DataMangaPictures = 'otaku/data/manga_pictures'
            DataOtakuPerson = 'otaku/data/person'
            DataOtakuPersonPictures = 'otaku/data/person_pictures'
            Temp_Characters = 'otaku/temp/characters'
            Temp_OtakuPersons = 'otaku/temp/person'

        class Renpy:
            Censorship = 'renpy/censorship'
            Developer = 'renpy/developer'
            DeveloperImage = 'renpy/developer_image'
            DeveloperImageExtra = 'renpy/developer_image_extra'
            DeveloperLink = 'renpy/developer_link'
            Game = 'renpy/game'
            GameEngine = 'renpy/game_engine'
            GameImage = 'renpy/game_image'
            GameImageExtra = 'renpy/game_image_extra'
            Genre = 'renpy/genre'
            Platform = 'renpy/platform'
            Prefix = 'renpy/prefix'
            Publisher = 'renpy/publisher'
            PublisherImage = 'renpy/publisher_image'
            PublisherImageExtra = 'renpy/publisher_image_extra'
            PublisherLink = 'renpy/publisher_link'
            Status = 'renpy/status'
            TitleGame = 'renpy/title_game'
            Translator = 'renpy/translator'
            TranslatorImage = 'renpy/translator_image'
            TranslatorImageExtra = 'renpy/translator_image_extra'
            TranslatorLink = 'renpy/translator_link'
            GameData = 'renpy/data/game'

        class Serie:
            Company = 'serie/company'
            Genre = 'serie/genre'
            Rating = 'serie/rating'
            Role = 'serie/role'
            Serie = 'serie/serie'
            SerieCast = 'serie/serie_cast'
            SerieImage = 'serie/serie_image'
            SerieImageExtra = 'serie/serie_image_extra'
            SerieStaff = 'serie/serie_staff'
            TitleSerie = 'serie/title_serie'
            Type = 'serie/type'

####################################################    Templates
class Templates:
    class Home:
        HOME =  Prefixes.BaseTemplates.HOME +'home.html'
    class Users:
        LOGIN  = Prefixes.BaseTemplates.Users.USERS + 'user_login.html'

        LST = Prefixes.BaseTemplates.Users.USERS + 'user_list.html'
        ADD = Prefixes.BaseTemplates.Users.USERS + 'user_form.html'
        UPT = Prefixes.BaseTemplates.Users.USERS + 'user_update.html'
        DTL = Prefixes.BaseTemplates.Users.USERS + 'user_detail.html'
        CHANGE_PASS = Prefixes.BaseTemplates.Users.USERS + 'user_password_change.html'

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
            LST = Prefixes.BaseTemplates.Music.Album + 'album_list.html'
            ADD = Prefixes.BaseTemplates.Music.Album + 'album_form.html'
            UPT = Prefixes.BaseTemplates.Music.Album + 'album_form.html'
            DTL = Prefixes.BaseTemplates.Music.Album + 'album_detail.html'

        class AlbumImage:
            LST = Prefixes.BaseTemplates.Music.AlbumImage + 'album_image_list.html'
            ADD = Prefixes.BaseTemplates.Music.AlbumImage + 'album_image_form.html'
            UPT = Prefixes.BaseTemplates.Music.AlbumImage + 'album_image_form.html'
            DTL = Prefixes.BaseTemplates.Music.AlbumImage + 'album_image_detail.html'

        class AlbumImageExtra:
            LST = Prefixes.BaseTemplates.Music.AlbumImageExtra + 'album_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Music.AlbumImageExtra + 'album_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Music.AlbumImageExtra + 'album_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Music.AlbumImageExtra + 'album_image_extra_detail.html'

        class AlbumType:
            LST = Prefixes.BaseTemplates.Music.AlbumType + 'album_type_list.html'
            ADD = Prefixes.BaseTemplates.Music.AlbumType + 'album_type_form.html'
            UPT = Prefixes.BaseTemplates.Music.AlbumType + 'album_type_form.html'
            DTL = Prefixes.BaseTemplates.Music.AlbumType + 'album_type_detail.html'

        class Artist:
            LST = Prefixes.BaseTemplates.Music.Artist + 'artist_list.html'
            ADD = Prefixes.BaseTemplates.Music.Artist + 'artist_form.html'
            UPT = Prefixes.BaseTemplates.Music.Artist + 'artist_form.html'
            DTL = Prefixes.BaseTemplates.Music.Artist + 'artist_detail.html'

        class ArtistImage:
            LST = Prefixes.BaseTemplates.Music.ArtistImage + 'artist_image_list.html'
            ADD = Prefixes.BaseTemplates.Music.ArtistImage + 'artist_image_form.html'
            UPT = Prefixes.BaseTemplates.Music.ArtistImage + 'artist_image_form.html'
            DTL = Prefixes.BaseTemplates.Music.ArtistImage + 'artist_image_detail.html'

        class ArtistImageExtra:
            LST = Prefixes.BaseTemplates.Music.ArtistImageExtra + 'artist_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Music.ArtistImageExtra + 'artist_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Music.ArtistImageExtra + 'artist_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Music.ArtistImageExtra + 'artist_image_extra_detail.html'

        class ArtistMember:
            LST = Prefixes.BaseTemplates.Music.ArtistMember + 'artist_member_list.html'
            ADD = Prefixes.BaseTemplates.Music.ArtistMember + 'artist_member_form.html'
            UPT = Prefixes.BaseTemplates.Music.ArtistMember + 'artist_member_form.html'
            DTL = Prefixes.BaseTemplates.Music.ArtistMember + 'artist_member_detail.html'

        class ArtistType:
            LST = Prefixes.BaseTemplates.Music.ArtistType + 'artist_type_list.html'
            ADD = Prefixes.BaseTemplates.Music.ArtistType + 'artist_type_form.html'
            UPT = Prefixes.BaseTemplates.Music.ArtistType + 'artist_type_form.html'
            DTL = Prefixes.BaseTemplates.Music.ArtistType + 'artist_type_detail.html'

        class Genre:
            LST = Prefixes.BaseTemplates.Music.Genre + 'genre_list.html'
            ADD = Prefixes.BaseTemplates.Music.Genre + 'genre_form.html'
            UPT = Prefixes.BaseTemplates.Music.Genre + 'genre_form.html'
            DTL = Prefixes.BaseTemplates.Music.Genre + 'genre_detail.html'

        class Role:
            LST = Prefixes.BaseTemplates.Music.Role + 'role_list.html'
            ADD = Prefixes.BaseTemplates.Music.Role + 'role_form.html'
            UPT = Prefixes.BaseTemplates.Music.Role + 'role_form.html'
            DTL = Prefixes.BaseTemplates.Music.Role + 'role_detail.html'

        class Song:
            LST = Prefixes.BaseTemplates.Music.Song + 'song_list.html'
            ADD = Prefixes.BaseTemplates.Music.Song + 'song_form.html'
            UPT = Prefixes.BaseTemplates.Music.Song + 'song_form.html'
            DTL = Prefixes.BaseTemplates.Music.Song + 'song_detail.html'

    class Otaku:
        class Anime:
            LST = Prefixes.BaseTemplates.Otaku.Anime + 'anime_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Anime + 'anime_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Anime + 'anime_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Anime + 'anime_detail.html'
        class AnimeCharacter:
            LST = Prefixes.BaseTemplates.Otaku.AnimeCharacter + 'anime_character_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.AnimeCharacter + 'anime_character_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.AnimeCharacter + 'anime_character_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.AnimeCharacter + 'anime_character_detail.html'
        class AnimeImage:
            LST = Prefixes.BaseTemplates.Otaku.AnimeImage + 'anime_image_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.AnimeImage + 'anime_image_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.AnimeImage + 'anime_image_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.AnimeImage + 'anime_image_detail.html'
        class AnimeImageExtra:
            LST = Prefixes.BaseTemplates.Otaku.AnimeImageExtra + 'anime_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.AnimeImageExtra + 'anime_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.AnimeImageExtra + 'anime_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.AnimeImageExtra + 'anime_image_extra_detail.html'
        class AnimeSong:
            LST = Prefixes.BaseTemplates.Otaku.AnimeSong + 'anime_song_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.AnimeSong + 'anime_song_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.AnimeSong + 'anime_song_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.AnimeSong + 'anime_song_detail.html'
        class AnimeStaff:
            LST = Prefixes.BaseTemplates.Otaku.AnimeStaff + 'anime_staff_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.AnimeStaff + 'anime_staff_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.AnimeStaff + 'anime_staff_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.AnimeStaff + 'anime_staff_detail.html'
        class AuthorManga:
            LST = Prefixes.BaseTemplates.Otaku.AuthorManga + 'author_manga_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.AuthorManga + 'author_manga_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.AuthorManga + 'author_manga_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.AuthorManga + 'author_manga_detail.html'
        class Character:
            LST = Prefixes.BaseTemplates.Otaku.Character + 'character_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Character + 'character_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Character + 'character_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Character + 'character_detail.html'
        class CharacterImage:
            LST = Prefixes.BaseTemplates.Otaku.CharacterImage + 'character_image_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.CharacterImage + 'character_image_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.CharacterImage + 'character_image_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.CharacterImage + 'character_image_detail.html'
        class CharacterImageExtra:
            LST = Prefixes.BaseTemplates.Otaku.CharacterImageExtra + 'character_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.CharacterImageExtra + 'character_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.CharacterImageExtra + 'character_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.CharacterImageExtra + 'character_image_extra_detail.html'
        class CharacterNickname:
            LST = Prefixes.BaseTemplates.Otaku.CharacterNickname + 'character_nickname_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.CharacterNickname + 'character_nickname_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.CharacterNickname + 'character_nickname_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.CharacterNickname + 'character_nickname_detail.html'
        class Demographic:
            LST = Prefixes.BaseTemplates.Otaku.Demographic + 'demographic_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Demographic + 'demographic_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Demographic + 'demographic_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Demographic + 'demographic_detail.html'
        class Genre:
            LST = Prefixes.BaseTemplates.Otaku.Genre + 'denre_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Genre + 'denre_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Genre + 'denre_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Genre + 'denre_detail.html'
        class Licensor:
            LST = Prefixes.BaseTemplates.Otaku.Licensor + 'licensor_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Licensor + 'licensor_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Licensor + 'licensor_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Licensor + 'licensor_detail.html'
        class Manga:
            LST = Prefixes.BaseTemplates.Otaku.Manga + 'manga_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Manga + 'manga_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Manga + 'manga_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Manga + 'manga_detail.html'
        class MangaCharacter:
            LST = Prefixes.BaseTemplates.Otaku.MangaCharacter + 'manga_character_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.MangaCharacter + 'manga_character_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.MangaCharacter + 'manga_character_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.MangaCharacter + 'manga_character_detail.html'
        class MangaImage:
            LST = Prefixes.BaseTemplates.Otaku.MangaImage + 'manga_image_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.MangaImage + 'manga_image_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.MangaImage + 'manga_image_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.MangaImage + 'manga_image_detail.html'
        class MangaImageExtra:
            LST = Prefixes.BaseTemplates.Otaku.MangaImageExtra + 'manga_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.MangaImageExtra + 'manga_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.MangaImageExtra + 'manga_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.MangaImageExtra + 'manga_image_extra_detail.html'
        class MediaRelation:
            LST = Prefixes.BaseTemplates.Otaku.MediaRelation + 'media_relation_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.MediaRelation + 'media_relation_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.MediaRelation + 'media_relation_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.MediaRelation + 'media_relation_detail.html'
        class Person:
            LST = Prefixes.BaseTemplates.Otaku.Person + 'person_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Person + 'person_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Person + 'person_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Person + 'person_detail.html'
        class PersonImage:
            LST = Prefixes.BaseTemplates.Otaku.PersonImage + 'person_image_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.PersonImage + 'person_image_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.PersonImage + 'person_image_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.PersonImage + 'person_image_detail.html'
        class PersonImageExtra:
            LST = Prefixes.BaseTemplates.Otaku.PersonImageExtra + 'person_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.PersonImageExtra + 'person_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.PersonImageExtra + 'person_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.PersonImageExtra + 'person_image_extra_detail.html'
        class PersonNickname:
            LST = Prefixes.BaseTemplates.Otaku.PersonNickname + 'person_nickname_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.PersonNickname + 'person_nickname_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.PersonNickname + 'person_nickname_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.PersonNickname + 'person_nickname_detail.html'
        class Producer:
            LST = Prefixes.BaseTemplates.Otaku.Producer + 'producer_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Producer + 'producer_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Producer + 'producer_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Producer + 'producer_detail.html'
        class Rating:
            LST = Prefixes.BaseTemplates.Otaku.Rating + 'rating_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Rating + 'rating_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Rating + 'rating_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Rating + 'rating_detail.html'
        class RelationType:
            LST = Prefixes.BaseTemplates.Otaku.RelationType + 'relation_type_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.RelationType + 'relation_type_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.RelationType + 'relation_type_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.RelationType + 'relation_type_detail.html'
        class Role:
            LST = Prefixes.BaseTemplates.Otaku.Role + 'role_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Role + 'role_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Role + 'role_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Role + 'role_detail.html'
        class Season:
            LST = Prefixes.BaseTemplates.Otaku.Season + 'season_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Season + 'season_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Season + 'season_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Season + 'season_detail.html'
        class SeasonFull:
            LST = Prefixes.BaseTemplates.Otaku.SeasonFull + 'season_full_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.SeasonFull + 'season_full_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.SeasonFull + 'season_full_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.SeasonFull + 'season_full_detail.html'
        class Serialization:
            LST = Prefixes.BaseTemplates.Otaku.Serialization + 'serialization_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Serialization + 'serialization_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Serialization + 'serialization_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Serialization + 'serialization_detail.html'
        class Source:
            LST = Prefixes.BaseTemplates.Otaku.Source + 'source_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Source + 'source_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Source + 'source_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Source + 'source_detail.html'
        class Status:
            LST = Prefixes.BaseTemplates.Otaku.Status + 'status_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Status + 'status_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Status + 'status_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Status + 'status_detail.html'
        class Studio:
            LST = Prefixes.BaseTemplates.Otaku.Studio + 'studio_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Studio + 'studio_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Studio + 'studio_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Studio + 'studio_detail.html'
        class Theme:
            LST = Prefixes.BaseTemplates.Otaku.Theme + 'theme_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Theme + 'theme_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Theme + 'theme_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Theme + 'theme_detail.html'
        class TitleAnime:
            LST = Prefixes.BaseTemplates.Otaku.TitleAnime + 'title_anime_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.TitleAnime + 'title_anime_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.TitleAnime + 'title_anime_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.TitleAnime + 'title_anime_detail.html'
        class TitleManga:
            LST = Prefixes.BaseTemplates.Otaku.TitleManga + 'title_manga_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.TitleManga + 'title_manga_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.TitleManga + 'title_manga_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.TitleManga + 'title_manga_detail.html'
        class Type:
            LST = Prefixes.BaseTemplates.Otaku.Type + 'type_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Type + 'type_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Type + 'type_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Type + 'type_detail.html'
        class VoiceCharacter:
            LST = Prefixes.BaseTemplates.Otaku.VoiceCharacter + 'voice_character_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.VoiceCharacter + 'voice_character_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.VoiceCharacter + 'voice_character_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.VoiceCharacter + 'voice_character_detail.html'
        class Year:
            LST = Prefixes.BaseTemplates.Otaku.Year + 'year_list.html'
            ADD = Prefixes.BaseTemplates.Otaku.Year + 'year_form.html'
            UPT = Prefixes.BaseTemplates.Otaku.Year + 'year_form.html'
            DTL = Prefixes.BaseTemplates.Otaku.Year + 'year_detail.html'

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
            LST = Prefixes.BaseTemplates.Renpy.Censorship + 'censorship_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Censorship + 'censorship_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Censorship + 'censorship_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Censorship + 'censorship_detail.html'
        class Developer:
            LST = Prefixes.BaseTemplates.Renpy.Developer + 'developer_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Developer + 'developer_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Developer + 'developer_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Developer + 'developer_detail.html'
        class DeveloperImage:
            LST = Prefixes.BaseTemplates.Renpy.DeveloperImage + 'developer_image_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.DeveloperImage + 'developer_image_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.DeveloperImage + 'developer_image_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.DeveloperImage + 'developer_image_detail.html'
        class DeveloperImageExtra:
            LST = Prefixes.BaseTemplates.Renpy.DeveloperImageExtra + 'developer_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.DeveloperImageExtra + 'developer_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.DeveloperImageExtra + 'developer_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.DeveloperImageExtra + 'developer_image_extra_detail.html'
        class DeveloperLink:
            LST = Prefixes.BaseTemplates.Renpy.DeveloperLink + 'developer_link_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.DeveloperLink + 'developer_link_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.DeveloperLink + 'developer_link_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.DeveloperLink + 'developer_link_detail.html'
        class Game:
            LST = Prefixes.BaseTemplates.Renpy.Game + 'game_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Game + 'game_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Game + 'game_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Game + 'game_detail.html'
        class GameEngine:
            LST = Prefixes.BaseTemplates.Renpy.GameEngine + 'game_engine_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.GameEngine + 'game_engine_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.GameEngine + 'game_engine_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.GameEngine + 'game_engine_detail.html'
        class GameImage:
            LST = Prefixes.BaseTemplates.Renpy.GameImage + 'game_image_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.GameImage + 'game_image_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.GameImage + 'game_image_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.GameImage + 'game_image_detail.html'
        class GameImageExtra:
            LST = Prefixes.BaseTemplates.Renpy.GameImageExtra + 'game_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.GameImageExtra + 'game_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.GameImageExtra + 'game_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.GameImageExtra + 'game_image_extra_detail.html'
        class Genre:
            LST = Prefixes.BaseTemplates.Renpy.Genre + 'genre_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Genre + 'genre_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Genre + 'genre_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Genre + 'genre_detail.html'
        class Platform:
            LST = Prefixes.BaseTemplates.Renpy.Platform + 'platform_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Platform + 'platform_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Platform + 'platform_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Platform + 'platform_detail.html'
        class Prefix:
            LST = Prefixes.BaseTemplates.Renpy.Prefix + 'prefix_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Prefix + 'prefix_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Prefix + 'prefix_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Prefix + 'prefix_detail.html'
        class Publisher:
            LST = Prefixes.BaseTemplates.Renpy.Publisher + 'publisher_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Publisher + 'publisher_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Publisher + 'publisher_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Publisher + 'publisher_detail.html'
        class PublisherImage:
            LST = Prefixes.BaseTemplates.Renpy.PublisherImage + 'publisher_image_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.PublisherImage + 'publisher_image_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.PublisherImage + 'publisher_image_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.PublisherImage + 'publisher_image_detail.html'
        class PublisherImageExtra:
            LST = Prefixes.BaseTemplates.Renpy.PublisherImageExtra + 'publisher_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.PublisherImageExtra + 'publisher_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.PublisherImageExtra + 'publisher_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.PublisherImageExtra + 'publisher_image_extra_detail.html'
        class PublisherLink:
            LST = Prefixes.BaseTemplates.Renpy.PublisherLink + 'publisher_link_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.PublisherLink + 'publisher_link_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.PublisherLink + 'publisher_link_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.PublisherLink + 'publisher_link_detail.html'
        class Status:
            LST = Prefixes.BaseTemplates.Renpy.Status + 'status_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Status + 'status_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Status + 'status_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Status + 'status_detail.html'
        class TitleGame:
            LST = Prefixes.BaseTemplates.Renpy.TitleGame + 'title_game_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.TitleGame + 'title_game_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.TitleGame + 'title_game_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.TitleGame + 'title_game_detail.html'
        class Translator:
            LST = Prefixes.BaseTemplates.Renpy.Translator + 'translator_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.Translator + 'translator_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.Translator + 'translator_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.Translator + 'translator_detail.html'
        class TranslatorImage:
            LST = Prefixes.BaseTemplates.Renpy.TranslatorImage + 'translator_image_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.TranslatorImage + 'translator_image_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.TranslatorImage + 'translator_image_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.TranslatorImage + 'translator_image_detail.html'
        class TranslatorImageExtra:
            LST = Prefixes.BaseTemplates.Renpy.TranslatorImageExtra + 'translator_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.TranslatorImageExtra + 'translator_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.TranslatorImageExtra + 'translator_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.TranslatorImageExtra + 'translator_image_extra_detail.html'
        class TranslatorLink:
            LST = Prefixes.BaseTemplates.Renpy.TranslatorLink + 'translator_link_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.TranslatorLink + 'translator_link_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.TranslatorLink + 'translator_link_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.TranslatorLink + 'translator_link_detail.html'
        class GameData:
            LST = Prefixes.BaseTemplates.Renpy.GameData + 'game_data_list.html'
            ADD = Prefixes.BaseTemplates.Renpy.GameData + 'game_data_form.html'
            UPT = Prefixes.BaseTemplates.Renpy.GameData + 'game_data_form.html'
            DTL = Prefixes.BaseTemplates.Renpy.GameData + 'game_data_detail.html'

    class Serie:
        class Company:
            LST = Prefixes.BaseTemplates.Serie.Company + 'company_list.html'
            ADD = Prefixes.BaseTemplates.Serie.Company + 'company_form.html'
            UPT = Prefixes.BaseTemplates.Serie.Company + 'company_form.html'
            DTL = Prefixes.BaseTemplates.Serie.Company + 'company_detail.html'
        class Genre:
            LST = Prefixes.BaseTemplates.Serie.Genre + 'genre_list.html'
            ADD = Prefixes.BaseTemplates.Serie.Genre + 'genre_form.html'
            UPT = Prefixes.BaseTemplates.Serie.Genre + 'genre_form.html'
            DTL = Prefixes.BaseTemplates.Serie.Genre + 'genre_detail.html'
        class Rating:
            LST = Prefixes.BaseTemplates.Serie.Rating + 'rating_list.html'
            ADD = Prefixes.BaseTemplates.Serie.Rating + 'rating_form.html'
            UPT = Prefixes.BaseTemplates.Serie.Rating + 'rating_form.html'
            DTL = Prefixes.BaseTemplates.Serie.Rating + 'rating_detail.html'

        class Role:
            LST = Prefixes.BaseTemplates.Serie.Role + 'role_list.html'
            ADD = Prefixes.BaseTemplates.Serie.Role + 'role_form.html'
            UPT = Prefixes.BaseTemplates.Serie.Role + 'role_form.html'
            DTL = Prefixes.BaseTemplates.Serie.Role + 'role_detail.html'

        class Serie:
            LST = Prefixes.BaseTemplates.Serie.Serie + 'serie_list.html'
            ADD = Prefixes.BaseTemplates.Serie.Serie + 'serie_form.html'
            UPT = Prefixes.BaseTemplates.Serie.Serie + 'serie_form.html'
            DTL = Prefixes.BaseTemplates.Serie.Serie + 'serie_detail.html'

        class SerieCast:
            LST = Prefixes.BaseTemplates.Serie.SerieCast + 'serie_cast_list.html'
            ADD = Prefixes.BaseTemplates.Serie.SerieCast + 'serie_cast_form.html'
            UPT = Prefixes.BaseTemplates.Serie.SerieCast + 'serie_cast_form.html'
            DTL = Prefixes.BaseTemplates.Serie.SerieCast + 'serie_cast_detail.html'

        class SerieImage:
            LST = Prefixes.BaseTemplates.Serie.SerieImage + 'serie_image_list.html'
            ADD = Prefixes.BaseTemplates.Serie.SerieImage + 'serie_image_form.html'
            UPT = Prefixes.BaseTemplates.Serie.SerieImage + 'serie_image_form.html'
            DTL = Prefixes.BaseTemplates.Serie.SerieImage + 'serie_image_detail.html'

        class SerieImageExtra:
            LST = Prefixes.BaseTemplates.Serie.SerieImageExtra + 'serie_image_extra_list.html'
            ADD = Prefixes.BaseTemplates.Serie.SerieImageExtra + 'serie_image_extra_form.html'
            UPT = Prefixes.BaseTemplates.Serie.SerieImageExtra + 'serie_image_extra_form.html'
            DTL = Prefixes.BaseTemplates.Serie.SerieImageExtra + 'serie_image_extra_detail.html'

        class SerieStaff:
            LST = Prefixes.BaseTemplates.Serie.SerieStaff + 'serie_staff_list.html'
            ADD = Prefixes.BaseTemplates.Serie.SerieStaff + 'serie_staff_form.html'
            UPT = Prefixes.BaseTemplates.Serie.SerieStaff + 'serie_staff_form.html'
            DTL = Prefixes.BaseTemplates.Serie.SerieStaff + 'serie_staff_detail.html'

        class TitleSerie:
            LST = Prefixes.BaseTemplates.Serie.TitleSerie + 'title_serie_list.html'
            ADD = Prefixes.BaseTemplates.Serie.TitleSerie + 'title_serie_form.html'
            UPT = Prefixes.BaseTemplates.Serie.TitleSerie + 'title_serie_form.html'
            DTL = Prefixes.BaseTemplates.Serie.TitleSerie + 'title_serie_detail.html'

        class Type:
            LST = Prefixes.BaseTemplates.Serie.Type + 'type_list.html'
            ADD = Prefixes.BaseTemplates.Serie.Type + 'type_form.html'
            UPT = Prefixes.BaseTemplates.Serie.Type + 'type_form.html'
            DTL = Prefixes.BaseTemplates.Serie.Type + 'type_detail.html'

####################################################    URLS
class URLS:
    class Main:
        INDEX = Prefixes.AppName.pages_app + 'index'
        CONTAC = Prefixes.AppName.pages_app + 'contac'

    class Home:
        COMMON =    Prefixes.AppName.common_app + 'home'
        MOVIE =     Prefixes.AppName.movie_app + 'home'
        MUSIC =     Prefixes.AppName.music_app + 'home'
        OTAKU =     Prefixes.AppName.otaku_app + 'home'
        RENPY =     Prefixes.AppName.renpy_app + 'home'
        SERIE =     Prefixes.AppName.serie_app + 'home'
        USERS =     Prefixes.AppName.users_app + 'home'

    class Users:
        LOGIN =     Prefixes.AppName.users_app + 'login'
        LST =       Prefixes.AppName.users_app + 'users_list'
        ADD =       Prefixes.AppName.users_app + 'users_create'
        UPD =       Prefixes.AppName.users_app + 'users_update'
        DTL =       Prefixes.AppName.users_app + 'users_detail'
        ADD_SUPER = Prefixes.AppName.users_app + 'superuser_create'
        ADD_STAFF = Prefixes.AppName.users_app + 'staffuser_create'

    class Common:
        class Country:
            LST = Prefixes.AppName.common_app + 'country_list'
            ADD = Prefixes.AppName.common_app + 'country_create'
            UPD = Prefixes.AppName.common_app + 'country_update'
            DTL = Prefixes.AppName.common_app + 'country_detail'

        class Format:
            LST = Prefixes.AppName.common_app + 'format_list'
            ADD = Prefixes.AppName.common_app + 'format_create'
            UPD = Prefixes.AppName.common_app + 'format_update'
            DTL = Prefixes.AppName.common_app + 'format_detail'

        class ImageSize:
            LST = Prefixes.AppName.common_app + 'image_size_list'
            ADD = Prefixes.AppName.common_app + 'image_size_create'
            UPD = Prefixes.AppName.common_app + 'image_size_update'
            DTL = Prefixes.AppName.common_app + 'image_size_detail'

        class Language:
            LST = Prefixes.AppName.common_app + 'language_list'
            ADD = Prefixes.AppName.common_app + 'language_create'
            UPD = Prefixes.AppName.common_app + 'language_update'
            DTL = Prefixes.AppName.common_app + 'language_detail'

        class Person:
            LST = Prefixes.AppName.common_app + 'person_list'
            ADD = Prefixes.AppName.common_app + 'person_create'
            UPD = Prefixes.AppName.common_app + 'person_update'
            DTL = Prefixes.AppName.common_app + 'person_detail'

        class PersonImage:
            LST = Prefixes.AppName.common_app + 'person_image_list'
            ADD = Prefixes.AppName.common_app + 'person_image_create'
            UPD = Prefixes.AppName.common_app + 'person_image_update'
            DTL = Prefixes.AppName.common_app + 'person_image_detail'

        class PersonImageExtra:
            LST = Prefixes.AppName.common_app + 'person_image_extra_list'
            ADD = Prefixes.AppName.common_app + 'person_image_extra_create'
            UPD = Prefixes.AppName.common_app + 'person_image_extra_update'
            DTL = Prefixes.AppName.common_app + 'person_image_extra_detail'

        class PersonNickname:
            LST = Prefixes.AppName.common_app + 'person_nickname_list'
            ADD = Prefixes.AppName.common_app + 'person_nickname_create'
            UPD = Prefixes.AppName.common_app + 'person_nickname_update'
            DTL = Prefixes.AppName.common_app + 'person_nickname_detail'

        class Quality:
            LST = Prefixes.AppName.common_app + 'quality_list'
            ADD = Prefixes.AppName.common_app + 'quality_create'
            UPD = Prefixes.AppName.common_app + 'quality_update'
            DTL = Prefixes.AppName.common_app + 'quality_detail'

        class Website:
            LST = Prefixes.AppName.common_app + 'website_list'
            ADD = Prefixes.AppName.common_app + 'website_create'
            UPD = Prefixes.AppName.common_app + 'website_update'
            DTL = Prefixes.AppName.common_app + 'website_detail'

    class Movie:
        class Company:
            LST = Prefixes.AppName.movie_app + 'company_list'
            ADD = Prefixes.AppName.movie_app + 'company_create'
            UPD = Prefixes.AppName.movie_app + 'company_update'
            DTL = Prefixes.AppName.movie_app + 'company_detail'

        class Genre:
            LST = Prefixes.AppName.movie_app + 'genre_list'
            ADD = Prefixes.AppName.movie_app + 'genre_create'
            UPD = Prefixes.AppName.movie_app + 'genre_update'
            DTL = Prefixes.AppName.movie_app + 'genre_detail'

        class Movie:
            LST = Prefixes.AppName.movie_app + 'movie_list'
            ADD = Prefixes.AppName.movie_app + 'movie_create'
            UPD = Prefixes.AppName.movie_app + 'movie_update'
            DTL = Prefixes.AppName.movie_app + 'movie_detail'

        class MovieCast:
            LST = Prefixes.AppName.movie_app + 'movie_cast_list'
            ADD = Prefixes.AppName.movie_app + 'movie_cast_create'
            UPD = Prefixes.AppName.movie_app + 'movie_cast_update'
            DTL = Prefixes.AppName.movie_app + 'movie_cast_detail'

        class MovieImage:
            LST = Prefixes.AppName.movie_app + 'movie_image_list'
            ADD = Prefixes.AppName.movie_app + 'movie_image_create'
            UPD = Prefixes.AppName.movie_app + 'movie_image_update'
            DTL = Prefixes.AppName.movie_app + 'movie_image_detail'

        class MovieImageExtra:
            LST = Prefixes.AppName.movie_app + 'movie_image_extra_list'
            ADD = Prefixes.AppName.movie_app + 'movie_image_extra_create'
            UPD = Prefixes.AppName.movie_app + 'movie_image_extra_update'
            DTL = Prefixes.AppName.movie_app + 'movie_image_extra_detail'

        class MovieStaff:
            LST = Prefixes.AppName.movie_app + 'movie_image_staff_list'
            ADD = Prefixes.AppName.movie_app + 'movie_image_staff_create'
            UPD = Prefixes.AppName.movie_app + 'movie_image_staff_update'
            DTL = Prefixes.AppName.movie_app + 'movie_image_staff_detail'

        class Rating:
            LST = Prefixes.AppName.movie_app + 'rating_list'
            ADD = Prefixes.AppName.movie_app + 'rating_create'
            UPD = Prefixes.AppName.movie_app + 'rating_update'
            DTL = Prefixes.AppName.movie_app + 'rating_detail'

        class Role:
            LST = Prefixes.AppName.movie_app + 'role_list'
            ADD = Prefixes.AppName.movie_app + 'role_create'
            UPD = Prefixes.AppName.movie_app + 'role_update'
            DTL = Prefixes.AppName.movie_app + 'role_detail'

        class TitleMovie:
            LST = Prefixes.AppName.movie_app + 'title_movie_list'
            ADD = Prefixes.AppName.movie_app + 'title_movie_create'
            UPD = Prefixes.AppName.movie_app + 'title_movie_update'
            DTL = Prefixes.AppName.movie_app + 'title_movie_detail'

        class Type:
            LST = Prefixes.AppName.movie_app + 'type_list'
            ADD = Prefixes.AppName.movie_app + 'type_create'
            UPD = Prefixes.AppName.movie_app + 'type_update'
            DTL = Prefixes.AppName.movie_app + 'type_detail'

    class Music:
        class Album:
            LST = Prefixes.AppName.music_app + 'album_list'
            ADD = Prefixes.AppName.music_app + 'album_create'
            UPD = Prefixes.AppName.music_app + 'album_update'
            DTL = Prefixes.AppName.music_app + 'album_detail'

        class AlbumImage:
            LST = Prefixes.AppName.music_app + 'album_image_list'
            ADD = Prefixes.AppName.music_app + 'album_image_create'
            UPD = Prefixes.AppName.music_app + 'album_image_update'
            DTL = Prefixes.AppName.music_app + 'album_image_detail'

        class AlbumImageExtra:
            LST = Prefixes.AppName.music_app + 'album_image_extra_list'
            ADD = Prefixes.AppName.music_app + 'album_image_extra_create'
            UPD = Prefixes.AppName.music_app + 'album_image_extra_update'
            DTL = Prefixes.AppName.music_app + 'album_image_extra_detail'

        class AlbumType:
            LST = Prefixes.AppName.music_app + 'album_image_type_list'
            ADD = Prefixes.AppName.music_app + 'album_image_type_create'
            UPD = Prefixes.AppName.music_app + 'album_image_type_update'
            DTL = Prefixes.AppName.music_app + 'album_image_type_detail'

        class Artist:
            LST = Prefixes.AppName.music_app + 'artist_list'
            ADD = Prefixes.AppName.music_app + 'artist_create'
            UPD = Prefixes.AppName.music_app + 'artist_update'
            DTL = Prefixes.AppName.music_app + 'artist_detail'

        class ArtistImage:
            LST = Prefixes.AppName.music_app + 'artist_image_list'
            ADD = Prefixes.AppName.music_app + 'artist_image_create'
            UPD = Prefixes.AppName.music_app + 'artist_image_update'
            DTL = Prefixes.AppName.music_app + 'artist_image_detail'

        class ArtistImageExtra:
            LST = Prefixes.AppName.music_app + 'artist_image_extra_list'
            ADD = Prefixes.AppName.music_app + 'artist_image_extra_create'
            UPD = Prefixes.AppName.music_app + 'artist_image_extra_update'
            DTL = Prefixes.AppName.music_app + 'artist_image_extra_detail'

        class ArtistMember:
            LST = Prefixes.AppName.music_app + 'artist_member_list'
            ADD = Prefixes.AppName.music_app + 'artist_member_create'
            UPD = Prefixes.AppName.music_app + 'artist_member_update'
            DTL = Prefixes.AppName.music_app + 'artist_member_detail'

        class ArtistType:
            LST = Prefixes.AppName.music_app + 'artist_type_list'
            ADD = Prefixes.AppName.music_app + 'artist_type_create'
            UPD = Prefixes.AppName.music_app + 'artist_type_update'
            DTL = Prefixes.AppName.music_app + 'artist_type_detail'

        class Genre:
            LST = Prefixes.AppName.music_app + 'genre_list'
            ADD = Prefixes.AppName.music_app + 'genre_create'
            UPD = Prefixes.AppName.music_app + 'genre_update'
            DTL = Prefixes.AppName.music_app + 'genre_detail'

        class Role:
            LST = Prefixes.AppName.music_app + 'role_list'
            ADD = Prefixes.AppName.music_app + 'role_create'
            UPD = Prefixes.AppName.music_app + 'role_update'
            DTL = Prefixes.AppName.music_app + 'role_detail'

        class Song:
            LST = Prefixes.AppName.music_app + 'song_list'
            ADD = Prefixes.AppName.music_app + 'song_create'
            UPD = Prefixes.AppName.music_app + 'song_update'
            DTL = Prefixes.AppName.music_app + 'song_detail'

    class Otaku:
        class Load:
            ANIME = Prefixes.AppName.otaku_app + 'anime_load'
            MANGA = Prefixes.AppName.otaku_app + 'manga_load'
            PERSON = Prefixes.AppName.otaku_app + 'person_load'
            CHARACTER = Prefixes.AppName.otaku_app + 'character_load'

        class Anime:
            LST = Prefixes.AppName.otaku_app + 'anime_list'
            ADD = Prefixes.AppName.otaku_app + 'anime_create'
            UPD = Prefixes.AppName.otaku_app + 'anime_update'
            DTL = Prefixes.AppName.otaku_app + 'anime_detail'

        class AnimeCharacter:
            LST = Prefixes.AppName.otaku_app + 'anime_character_list'
            ADD = Prefixes.AppName.otaku_app + 'anime_character_create'
            UPD = Prefixes.AppName.otaku_app + 'anime_character_update'
            DTL = Prefixes.AppName.otaku_app + 'anime_character_detail'

        class AnimeImage:
            LST = Prefixes.AppName.otaku_app + 'anime_image_list'
            ADD = Prefixes.AppName.otaku_app + 'anime_image_create'
            UPD = Prefixes.AppName.otaku_app + 'anime_image_update'
            DTL = Prefixes.AppName.otaku_app + 'anime_image_detail'

        class AnimeImageExtra:
            LST = Prefixes.AppName.otaku_app + 'anime_image_extra_list'
            ADD = Prefixes.AppName.otaku_app + 'anime_image_extra_create'
            UPD = Prefixes.AppName.otaku_app + 'anime_image_extra_update'
            DTL = Prefixes.AppName.otaku_app + 'anime_image_extra_detail'

        class AnimeSong:
            LST = Prefixes.AppName.otaku_app + 'anime_image_song_list'
            ADD = Prefixes.AppName.otaku_app + 'anime_image_song_create'
            UPD = Prefixes.AppName.otaku_app + 'anime_image_song_update'
            DTL = Prefixes.AppName.otaku_app + 'anime_image_song_detail'

        class AnimeStaff:
            LST = Prefixes.AppName.otaku_app + 'anime_staff_list'
            ADD = Prefixes.AppName.otaku_app + 'anime_staff_create'
            UPD = Prefixes.AppName.otaku_app + 'anime_staff_update'
            DTL = Prefixes.AppName.otaku_app + 'anime_staff_detail'

        class AuthorManga:
            LST = Prefixes.AppName.otaku_app + 'author_manga_list'
            ADD = Prefixes.AppName.otaku_app + 'author_manga_create'
            UPD = Prefixes.AppName.otaku_app + 'author_manga_update'
            DTL = Prefixes.AppName.otaku_app + 'author_manga_detail'

        class Character:
            LST = Prefixes.AppName.otaku_app + 'character_list'
            ADD = Prefixes.AppName.otaku_app + 'character_create'
            UPD = Prefixes.AppName.otaku_app + 'character_update'
            DTL = Prefixes.AppName.otaku_app + 'character_detail'

        class CharacterImage:
            LST = Prefixes.AppName.otaku_app + 'character_image_list'
            ADD = Prefixes.AppName.otaku_app + 'character_image_create'
            UPD = Prefixes.AppName.otaku_app + 'character_image_update'
            DTL = Prefixes.AppName.otaku_app + 'character_image_detail'

        class CharacterImageExtra:
            LST = Prefixes.AppName.otaku_app + 'character_image_extra_list'
            ADD = Prefixes.AppName.otaku_app + 'character_image_extra_create'
            UPD = Prefixes.AppName.otaku_app + 'character_image_extra_update'
            DTL = Prefixes.AppName.otaku_app + 'character_image_extra_detail'

        class CharacterNickname:
            LST = Prefixes.AppName.otaku_app + 'character_nickname_list'
            ADD = Prefixes.AppName.otaku_app + 'character_nickname_create'
            UPD = Prefixes.AppName.otaku_app + 'character_nickname_update'
            DTL = Prefixes.AppName.otaku_app + 'character_nickname_detail'

        class Demographic:
            LST = Prefixes.AppName.otaku_app + 'demographic_list'
            ADD = Prefixes.AppName.otaku_app + 'demographic_create'
            UPD = Prefixes.AppName.otaku_app + 'demographic_update'
            DTL = Prefixes.AppName.otaku_app + 'demographic_detail'

        class Genre:
            LST = Prefixes.AppName.otaku_app + 'genre_list'
            ADD = Prefixes.AppName.otaku_app + 'genre_create'
            UPD = Prefixes.AppName.otaku_app + 'genre_update'
            DTL = Prefixes.AppName.otaku_app + 'genre_detail'

        class Licensor:
            LST = Prefixes.AppName.otaku_app + 'licensor_list'
            ADD = Prefixes.AppName.otaku_app + 'licensor_create'
            UPD = Prefixes.AppName.otaku_app + 'licensor_update'
            DTL = Prefixes.AppName.otaku_app + 'licensor_detail'

        class Manga:
            LST = Prefixes.AppName.otaku_app + 'manga_list'
            ADD = Prefixes.AppName.otaku_app + 'manga_create'
            UPD = Prefixes.AppName.otaku_app + 'manga_update'
            DTL = Prefixes.AppName.otaku_app + 'manga_detail'

        class MangaCharacter:
            LST = Prefixes.AppName.otaku_app + 'manga_character_list'
            ADD = Prefixes.AppName.otaku_app + 'manga_character_create'
            UPD = Prefixes.AppName.otaku_app + 'manga_character_update'
            DTL = Prefixes.AppName.otaku_app + 'manga_character_detail'

        class MangaImage:
            LST = Prefixes.AppName.otaku_app + 'manga_image_list'
            ADD = Prefixes.AppName.otaku_app + 'manga_image_create'
            UPD = Prefixes.AppName.otaku_app + 'manga_image_update'
            DTL = Prefixes.AppName.otaku_app + 'manga_image_detail'

        class MangaImageExtra:
            LST = Prefixes.AppName.otaku_app + 'manga_image_extra_list'
            ADD = Prefixes.AppName.otaku_app + 'manga_image_extra_create'
            UPD = Prefixes.AppName.otaku_app + 'manga_image_extra_update'
            DTL = Prefixes.AppName.otaku_app + 'manga_image_extra_detail'

        class MediaRelation:
            LST = Prefixes.AppName.otaku_app + 'media_relation_list'
            ADD = Prefixes.AppName.otaku_app + 'media_relation_create'
            UPD = Prefixes.AppName.otaku_app + 'media_relation_update'
            DTL = Prefixes.AppName.otaku_app + 'media_relation_detail'

        class Person:
            LST = Prefixes.AppName.otaku_app + 'person_list'
            ADD = Prefixes.AppName.otaku_app + 'person_create'
            UPD = Prefixes.AppName.otaku_app + 'person_update'
            DTL = Prefixes.AppName.otaku_app + 'person_detail'

        class PersonImage:
            LST = Prefixes.AppName.otaku_app + 'person_image_list'
            ADD = Prefixes.AppName.otaku_app + 'person_image_create'
            UPD = Prefixes.AppName.otaku_app + 'person_image_update'
            DTL = Prefixes.AppName.otaku_app + 'person_image_detail'

        class PersonImageExtra:
            LST = Prefixes.AppName.otaku_app + 'person_image_extra_list'
            ADD = Prefixes.AppName.otaku_app + 'person_image_extra_create'
            UPD = Prefixes.AppName.otaku_app + 'person_image_extra_update'
            DTL = Prefixes.AppName.otaku_app + 'person_image_extra_detail'

        class PersonNickname:
            LST = Prefixes.AppName.otaku_app + 'person_nickname_list'
            ADD = Prefixes.AppName.otaku_app + 'person_nickname_create'
            UPD = Prefixes.AppName.otaku_app + 'person_nickname_update'
            DTL = Prefixes.AppName.otaku_app + 'person_nickname_detail'

        class Producer:
            LST = Prefixes.AppName.otaku_app + 'producer_list'
            ADD = Prefixes.AppName.otaku_app + 'producer_create'
            UPD = Prefixes.AppName.otaku_app + 'producer_update'
            DTL = Prefixes.AppName.otaku_app + 'producer_detail'

        class Rating:
            LST = Prefixes.AppName.otaku_app + 'rating_list'
            ADD = Prefixes.AppName.otaku_app + 'rating_create'
            UPD = Prefixes.AppName.otaku_app + 'rating_update'
            DTL = Prefixes.AppName.otaku_app + 'rating_detail'

        class RelationType:
            LST = Prefixes.AppName.otaku_app + 'relation_type_list'
            ADD = Prefixes.AppName.otaku_app + 'relation_type_create'
            UPD = Prefixes.AppName.otaku_app + 'relation_type_update'
            DTL = Prefixes.AppName.otaku_app + 'relation_type_detail'

        class Role:
            LST = Prefixes.AppName.otaku_app + 'role_list'
            ADD = Prefixes.AppName.otaku_app + 'role_create'
            UPD = Prefixes.AppName.otaku_app + 'role_update'
            DTL = Prefixes.AppName.otaku_app + 'role_detail'

        class Season:
            LST = Prefixes.AppName.otaku_app + 'season_list'
            ADD = Prefixes.AppName.otaku_app + 'season_create'
            UPD = Prefixes.AppName.otaku_app + 'season_update'
            DTL = Prefixes.AppName.otaku_app + 'season_detail'

        class SeasonFull:
            LST = Prefixes.AppName.otaku_app + 'season_full_list'
            ADD = Prefixes.AppName.otaku_app + 'season_full_create'
            UPD = Prefixes.AppName.otaku_app + 'season_full_update'
            DTL = Prefixes.AppName.otaku_app + 'season_full_detail'

        class Serialization:
            LST = Prefixes.AppName.otaku_app + 'serialization_list'
            ADD = Prefixes.AppName.otaku_app + 'serialization_create'
            UPD = Prefixes.AppName.otaku_app + 'serialization_update'
            DTL = Prefixes.AppName.otaku_app + 'serialization_detail'

        class Source:
            LST = Prefixes.AppName.otaku_app + 'source_list'
            ADD = Prefixes.AppName.otaku_app + 'source_create'
            UPD = Prefixes.AppName.otaku_app + 'source_update'
            DTL = Prefixes.AppName.otaku_app + 'source_detail'

        class Status:
            LST = Prefixes.AppName.otaku_app + 'status_list'
            ADD = Prefixes.AppName.otaku_app + 'status_create'
            UPD = Prefixes.AppName.otaku_app + 'status_update'
            DTL = Prefixes.AppName.otaku_app + 'status_detail'

        class Studio:
            LST = Prefixes.AppName.otaku_app + 'studio_list'
            ADD = Prefixes.AppName.otaku_app + 'studio_create'
            UPD = Prefixes.AppName.otaku_app + 'studio_update'
            DTL = Prefixes.AppName.otaku_app + 'studio_detail'

        class Theme:
            LST = Prefixes.AppName.otaku_app + 'theme_list'
            ADD = Prefixes.AppName.otaku_app + 'theme_create'
            UPD = Prefixes.AppName.otaku_app + 'theme_update'
            DTL = Prefixes.AppName.otaku_app + 'theme_detail'

        class TitleAnime:
            LST = Prefixes.AppName.otaku_app + 'title_anime_list'
            ADD = Prefixes.AppName.otaku_app + 'title_anime_create'
            UPD = Prefixes.AppName.otaku_app + 'title_anime_update'
            DTL = Prefixes.AppName.otaku_app + 'title_anime_detail'

        class TitleManga:
            LST = Prefixes.AppName.otaku_app + 'title_manga_list'
            ADD = Prefixes.AppName.otaku_app + 'title_manga_create'
            UPD = Prefixes.AppName.otaku_app + 'title_manga_update'
            DTL = Prefixes.AppName.otaku_app + 'title_manga_detail'

        class Type:
            LST = Prefixes.AppName.otaku_app + 'type_list'
            ADD = Prefixes.AppName.otaku_app + 'type_create'
            UPD = Prefixes.AppName.otaku_app + 'type_update'
            DTL = Prefixes.AppName.otaku_app + 'type_detail'

        class VoiceCharacter:
            LST = Prefixes.AppName.otaku_app + 'voice_character_list'
            ADD = Prefixes.AppName.otaku_app + 'voice_character_create'
            UPD = Prefixes.AppName.otaku_app + 'voice_character_update'
            DTL = Prefixes.AppName.otaku_app + 'voice_character_detail'

        class Year:
            LST = Prefixes.AppName.otaku_app + 'year_list'
            ADD = Prefixes.AppName.otaku_app + 'year_create'
            UPD = Prefixes.AppName.otaku_app + 'year_update'
            DTL = Prefixes.AppName.otaku_app + 'year_detail'

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
            LST = Prefixes.AppName.renpy_app + 'censorship_list'
            ADD = Prefixes.AppName.renpy_app + 'censorship_create'
            UPD = Prefixes.AppName.renpy_app + 'censorship_update'
            DTL = Prefixes.AppName.renpy_app + 'censorship_detail'

        class Developer:
            LST = Prefixes.AppName.renpy_app + 'developer_list'
            ADD = Prefixes.AppName.renpy_app + 'developer_create'
            UPD = Prefixes.AppName.renpy_app + 'developer_update'
            DTL = Prefixes.AppName.renpy_app + 'developer_detail'

        class DeveloperImage:
            LST = Prefixes.AppName.renpy_app + 'developer_image_list'
            ADD = Prefixes.AppName.renpy_app + 'developer_image_create'
            UPD = Prefixes.AppName.renpy_app + 'developer_image_update'
            DTL = Prefixes.AppName.renpy_app + 'developer_image_detail'

        class DeveloperImageExtra:
            LST = Prefixes.AppName.renpy_app + 'developer_image_extra_list'
            ADD = Prefixes.AppName.renpy_app + 'developer_image_extra_create'
            UPD = Prefixes.AppName.renpy_app + 'developer_image_extra_update'
            DTL = Prefixes.AppName.renpy_app + 'developer_image_extra_detail'

        class DeveloperLink:
            LST = Prefixes.AppName.renpy_app + 'developer_link_list'
            ADD = Prefixes.AppName.renpy_app + 'developer_link_create'
            UPD = Prefixes.AppName.renpy_app + 'developer_link_update'
            DTL = Prefixes.AppName.renpy_app + 'developer_link_detail'

        class Game:
            LST = Prefixes.AppName.renpy_app + 'game_list'
            ADD = Prefixes.AppName.renpy_app + 'game_create'
            UPD = Prefixes.AppName.renpy_app + 'game_update'
            DTL = Prefixes.AppName.renpy_app + 'game_detail'

        class GameEngine:
            LST = Prefixes.AppName.renpy_app + 'game_engine_list'
            ADD = Prefixes.AppName.renpy_app + 'game_engine_create'
            UPD = Prefixes.AppName.renpy_app + 'game_engine_update'
            DTL = Prefixes.AppName.renpy_app + 'game_engine_detail'

        class GameImage:
            LST = Prefixes.AppName.renpy_app + 'game_image_list'
            ADD = Prefixes.AppName.renpy_app + 'game_image_create'
            UPD = Prefixes.AppName.renpy_app + 'game_image_update'
            DTL = Prefixes.AppName.renpy_app + 'game_image_detail'

        class GameImageExtra:
            LST = Prefixes.AppName.renpy_app + 'game_image_extra_list'
            ADD = Prefixes.AppName.renpy_app + 'game_image_extra_create'
            UPD = Prefixes.AppName.renpy_app + 'game_image_extra_update'
            DTL = Prefixes.AppName.renpy_app + 'game_image_extra_detail'

        class Genre:
            LST = Prefixes.AppName.renpy_app + 'genre_list'
            ADD = Prefixes.AppName.renpy_app + 'genre_create'
            UPD = Prefixes.AppName.renpy_app + 'genre_update'
            DTL = Prefixes.AppName.renpy_app + 'genre_detail'

        class Platform:
            LST = Prefixes.AppName.renpy_app + 'platform_list'
            ADD = Prefixes.AppName.renpy_app + 'platform_create'
            UPD = Prefixes.AppName.renpy_app + 'platform_update'
            DTL = Prefixes.AppName.renpy_app + 'platform_detail'

        class Prefix:
            LST = Prefixes.AppName.renpy_app + 'prefix_list'
            ADD = Prefixes.AppName.renpy_app + 'prefix_create'
            UPD = Prefixes.AppName.renpy_app + 'prefix_update'
            DTL = Prefixes.AppName.renpy_app + 'prefix_detail'

        class Publisher:
            LST = Prefixes.AppName.renpy_app + 'publisher_list'
            ADD = Prefixes.AppName.renpy_app + 'publisher_create'
            UPD = Prefixes.AppName.renpy_app + 'publisher_update'
            DTL = Prefixes.AppName.renpy_app + 'publisher_detail'

        class PublisherImage:
            LST = Prefixes.AppName.renpy_app + 'publisher_image_list'
            ADD = Prefixes.AppName.renpy_app + 'publisher_image_create'
            UPD = Prefixes.AppName.renpy_app + 'publisher_image_update'
            DTL = Prefixes.AppName.renpy_app + 'publisher_image_detail'

        class PublisherImageExtra:
            LST = Prefixes.AppName.renpy_app + 'publisher_image_extra_list'
            ADD = Prefixes.AppName.renpy_app + 'publisher_image_extra_create'
            UPD = Prefixes.AppName.renpy_app + 'publisher_image_extra_update'
            DTL = Prefixes.AppName.renpy_app + 'publisher_image_extra_detail'

        class PublisherLink:
            LST = Prefixes.AppName.renpy_app + 'publisher_link_list'
            ADD = Prefixes.AppName.renpy_app + 'publisher_link_create'
            UPD = Prefixes.AppName.renpy_app + 'publisher_link_update'
            DTL = Prefixes.AppName.renpy_app + 'publisher_link_detail'

        class Status:
            LST = Prefixes.AppName.renpy_app + 'status_list'
            ADD = Prefixes.AppName.renpy_app + 'status_create'
            UPD = Prefixes.AppName.renpy_app + 'status_update'
            DTL = Prefixes.AppName.renpy_app + 'status_detail'

        class TitleGame:
            LST = Prefixes.AppName.renpy_app + 'title_game_list'
            ADD = Prefixes.AppName.renpy_app + 'title_game_create'
            UPD = Prefixes.AppName.renpy_app + 'title_game_update'
            DTL = Prefixes.AppName.renpy_app + 'title_game_detail'

        class Translator:
            LST = Prefixes.AppName.renpy_app + 'translator_list'
            ADD = Prefixes.AppName.renpy_app + 'translator_create'
            UPD = Prefixes.AppName.renpy_app + 'translator_update'
            DTL = Prefixes.AppName.renpy_app + 'translator_detail'

        class TranslatorImage:
            LST = Prefixes.AppName.renpy_app + 'translator_image_list'
            ADD = Prefixes.AppName.renpy_app + 'translator_image_create'
            UPD = Prefixes.AppName.renpy_app + 'translator_image_update'
            DTL = Prefixes.AppName.renpy_app + 'translator_image_detail'

        class TranslatorImageExtra:
            LST = Prefixes.AppName.renpy_app + 'translator_image_extra_list'
            ADD = Prefixes.AppName.renpy_app + 'translator_image_extra_create'
            UPD = Prefixes.AppName.renpy_app + 'translator_image_extra_update'
            DTL = Prefixes.AppName.renpy_app + 'translator_image_extra_detail'

        class TranslatorLink:
            LST = Prefixes.AppName.renpy_app + 'translator_link_list'
            ADD = Prefixes.AppName.renpy_app + 'translator_link_create'
            UPD = Prefixes.AppName.renpy_app + 'translator_link_update'
            DTL = Prefixes.AppName.renpy_app + 'translator_link_detail'

        class F95GameFetchStatus:
            LST = Prefixes.AppName.renpy_app + 'game_data_list'
            ADD = Prefixes.AppName.renpy_app + 'game_data_create'
            UPD = Prefixes.AppName.renpy_app + 'game_data_update'
            DTL = Prefixes.AppName.renpy_app + 'game_data_detail'

    class Serie:
        class Company:
            LST = Prefixes.AppName.serie_app + 'company_list'
            ADD = Prefixes.AppName.serie_app + 'company_create'
            UPD = Prefixes.AppName.serie_app + 'company_update'
            DTL = Prefixes.AppName.serie_app + 'company_detail'

        class Genre:
            LST = Prefixes.AppName.serie_app + 'genre_list'
            ADD = Prefixes.AppName.serie_app + 'genre_create'
            UPD = Prefixes.AppName.serie_app + 'genre_update'
            DTL = Prefixes.AppName.serie_app + 'genre_detail'

        class Rating:
            LST = Prefixes.AppName.serie_app + 'rating_list'
            ADD = Prefixes.AppName.serie_app + 'rating_create'
            UPD = Prefixes.AppName.serie_app + 'rating_update'
            DTL = Prefixes.AppName.serie_app + 'rating_detail'

        class Role:
            LST = Prefixes.AppName.serie_app + 'role_list'
            ADD = Prefixes.AppName.serie_app + 'role_create'
            UPD = Prefixes.AppName.serie_app + 'role_update'
            DTL = Prefixes.AppName.serie_app + 'role_detail'

        class Serie:
            LST = Prefixes.AppName.serie_app + 'serie_list'
            ADD = Prefixes.AppName.serie_app + 'serie_create'
            UPD = Prefixes.AppName.serie_app + 'serie_update'
            DTL = Prefixes.AppName.serie_app + 'serie_detail'

        class SerieCast:
            LST = Prefixes.AppName.serie_app + 'serie_cast_list'
            ADD = Prefixes.AppName.serie_app + 'serie_cast_create'
            UPD = Prefixes.AppName.serie_app + 'serie_cast_update'
            DTL = Prefixes.AppName.serie_app + 'serie_cast_detail'

        class SerieImage:
            LST = Prefixes.AppName.serie_app + 'serie_image_list'
            ADD = Prefixes.AppName.serie_app + 'serie_image_create'
            UPD = Prefixes.AppName.serie_app + 'serie_image_update'
            DTL = Prefixes.AppName.serie_app + 'serie_image_detail'

        class SerieImageExtra:
            LST = Prefixes.AppName.serie_app + 'serie_image_extra_list'
            ADD = Prefixes.AppName.serie_app + 'serie_image_extra_create'
            UPD = Prefixes.AppName.serie_app + 'serie_image_extra_update'
            DTL = Prefixes.AppName.serie_app + 'serie_image_extra_detail'

        class SerieStaff:
            LST = Prefixes.AppName.serie_app + 'serie_staff_list'
            ADD = Prefixes.AppName.serie_app + 'serie_staff_create'
            UPD = Prefixes.AppName.serie_app + 'serie_staff_update'
            DTL = Prefixes.AppName.serie_app + 'serie_staff_detail'

        class TitleSerie:
            LST = Prefixes.AppName.serie_app + 'title_serie_list'
            ADD = Prefixes.AppName.serie_app + 'title_serie_create'
            UPD = Prefixes.AppName.serie_app + 'title_serie_update'
            DTL = Prefixes.AppName.serie_app + 'title_serie_detail'

        class Type:
            LST = Prefixes.AppName.serie_app + 'type_list'
            ADD = Prefixes.AppName.serie_app + 'type_create'
            UPD = Prefixes.AppName.serie_app + 'type_update'
            DTL = Prefixes.AppName.serie_app + 'type_detail'

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
        COUNTRY =               Prefixes.BaseJavaScripts.common + 'country_config.js'
        FORMAT =                Prefixes.BaseJavaScripts.common + 'format_config.js'
        IMAGE_SIZE =            Prefixes.BaseJavaScripts.common + 'image_size_config.js'
        LANGUAGE =              Prefixes.BaseJavaScripts.common + 'language_config.js'
        PERSON =                Prefixes.BaseJavaScripts.common + 'person_config.js'
        PERSON_IMAGE =          Prefixes.BaseJavaScripts.common + 'person_image_config.js'
        PERSON_IMAGE_EXTRA =    Prefixes.BaseJavaScripts.common + 'person_image_extra_config.js'
        PERSON_NICKNAME =       Prefixes.BaseJavaScripts.common + 'person_nickname_config.js'
        QUALITY =               Prefixes.BaseJavaScripts.common + 'quality_config.js'
        WEBSITE =               Prefixes.BaseJavaScripts.common + 'website_config.js'

    class Movie:
        COMPANY =           Prefixes.BaseJavaScripts.movie + 'movie_company.js'
        GENRE =             Prefixes.BaseJavaScripts.movie + 'movie_genre.js'
        MOVIE =             Prefixes.BaseJavaScripts.movie + 'movie_movie.js'
        MOVIE_CAST =        Prefixes.BaseJavaScripts.movie + 'movie_movie_cast.js'
        MOVIE_IMAGE =       Prefixes.BaseJavaScripts.movie + 'movie_movie_image.js'
        MOVIE_IMAGE_EXTRA = Prefixes.BaseJavaScripts.movie + 'movie_movie_image_extra.js'
        MOVIE_STAFF =       Prefixes.BaseJavaScripts.movie + 'movie_movie_staff.js'
        RATING =            Prefixes.BaseJavaScripts.movie + 'movie_rating.js'
        ROLE =              Prefixes.BaseJavaScripts.movie + 'movie_role.js'
        TITLE_MOVIE =       Prefixes.BaseJavaScripts.movie + 'movie_title_movie.js'
        TYPE =              Prefixes.BaseJavaScripts.movie + 'movie_type.js'

    class Music:
        ALBUM =                 Prefixes.BaseJavaScripts.music + 'music_album.js'
        ALBUM_IMAGE =           Prefixes.BaseJavaScripts.music + 'music_album_image.js'
        ALBUM_IMAGE_EXTRA =     Prefixes.BaseJavaScripts.music + 'music_album_image_extra.js'
        ALBUM_TYPE =            Prefixes.BaseJavaScripts.music + 'music_album_type.js'
        ARTIST =                Prefixes.BaseJavaScripts.music + 'music_artist.js'
        ARTIST_IMAGE =          Prefixes.BaseJavaScripts.music + 'music_artist_image.js'
        ARTIST_IMAGE_EXTRA =    Prefixes.BaseJavaScripts.music + 'music_artist_image_extra.js'
        ARTIST_MEMBER =         Prefixes.BaseJavaScripts.music + 'music_artist_member.js'
        ARTIST_TYPE =           Prefixes.BaseJavaScripts.music + 'music_artist_type.js'
        GENRE =                 Prefixes.BaseJavaScripts.music + 'music_genre.js'
        ROLE =                  Prefixes.BaseJavaScripts.music + 'music_role.js'
        SONG =                  Prefixes.BaseJavaScripts.music + 'music_song.js'

    class Otaku:
        ANIME =                     Prefixes.BaseJavaScripts.otaku + 'otaku_anime.js'
        ANIME_CHARACTER =           Prefixes.BaseJavaScripts.otaku + 'otaku_anime_character.js'
        ANIME_IMAGE =               Prefixes.BaseJavaScripts.otaku + 'otaku_anime_image.js'
        ANIME_IMAGE_EXTRA =         Prefixes.BaseJavaScripts.otaku + 'otaku_anime_image_extra.js'
        ANIME_STAFF =               Prefixes.BaseJavaScripts.otaku + 'otaku_anime_staff.js'
        AUTHOR_MANGA =              Prefixes.BaseJavaScripts.otaku + 'otaku_author_manga.js'
        CHARACTER =                 Prefixes.BaseJavaScripts.otaku + 'otaku_character.js'
        CHARACTER_IMAGE =           Prefixes.BaseJavaScripts.otaku + 'otaku_character_image.js'
        CHARACTER_IMAGE_EXTRA =     Prefixes.BaseJavaScripts.otaku + 'otaku_character_image_extra.js'
        CHARACTER_NICKNAME =        Prefixes.BaseJavaScripts.otaku + 'otaku_character_nickname.js'
        DATA_ANIME =                Prefixes.BaseJavaScripts.otaku + 'otaku_data_anime.js'
        DATA_ANIME_CHARACTERS =     Prefixes.BaseJavaScripts.otaku + 'otaku_data_anime_characters.js'
        DATA_ANIME_PICTURES =       Prefixes.BaseJavaScripts.otaku + 'otaku_data_anime_pictures.js'
        DATA_ANIME_STAFF =          Prefixes.BaseJavaScripts.otaku + 'otaku_data_anime_staff.js'
        DATA_CHARACTER =            Prefixes.BaseJavaScripts.otaku + 'otaku_data_character.js'
        DATA_CHARACTER_PICTURES =   Prefixes.BaseJavaScripts.otaku + 'otaku_data_character_pictures.js'
        DATA_IMAGE_URL =            Prefixes.BaseJavaScripts.otaku + 'otaku_data_image_url.js'
        DATA_MANGA =                Prefixes.BaseJavaScripts.otaku + 'otaku_data_manga.js'
        DATA_MANGA_CHARACTERS =     Prefixes.BaseJavaScripts.otaku + 'otaku_data_manga_characters.js'
        DATA_MANGA_PICTURES =       Prefixes.BaseJavaScripts.otaku + 'otaku_data_manga_pictures.js'
        DATA_PERSON =               Prefixes.BaseJavaScripts.otaku + 'otaku_data_person.js'
        DATA_PERSON_PICTURES =      Prefixes.BaseJavaScripts.otaku + 'otaku_data_person_pictures.js'
        DEMOGRAPHIC =               Prefixes.BaseJavaScripts.otaku + 'otaku_demographic.js'
        GENRE =                     Prefixes.BaseJavaScripts.otaku + 'otaku_genre.js'
        LICENSOR =                  Prefixes.BaseJavaScripts.otaku + 'otaku_licensor.js'
        MANGA =                     Prefixes.BaseJavaScripts.otaku + 'otaku_manga.js'
        MANGA_CHARACTER =           Prefixes.BaseJavaScripts.otaku + 'otaku_manga_character.js'
        MANGA_IMAGE =               Prefixes.BaseJavaScripts.otaku + 'otaku_manga_image.js'
        MANGA_IMAGE_EXTRA =         Prefixes.BaseJavaScripts.otaku + 'otaku_manga_image_extra.js'
        MEDIA_RELATION =            Prefixes.BaseJavaScripts.otaku + 'otaku_media_relation.js'
        MEDIA_RELATION_ANIME =      Prefixes.BaseJavaScripts.otaku + 'otaku_media_relation_anime.js'
        MEDIA_RELATION_MANGA =      Prefixes.BaseJavaScripts.otaku + 'otaku_media_relation_manga.js'
        PERSON =                    Prefixes.BaseJavaScripts.otaku + 'otaku_person.js'
        PERSON_IMAGE =              Prefixes.BaseJavaScripts.otaku + 'otaku_person_image.js'
        PERSON_IMAGE_EXTRA =        Prefixes.BaseJavaScripts.otaku + 'otaku_person_image_extra.js'
        PERSON_NICKNAME =           Prefixes.BaseJavaScripts.otaku + 'otaku_person_nickname.js'
        PRODUCER =                  Prefixes.BaseJavaScripts.otaku + 'otaku_producer.js'
        RATING =                    Prefixes.BaseJavaScripts.otaku + 'otaku_rating.js'
        RELATION_TYPE =             Prefixes.BaseJavaScripts.otaku + 'otaku_relation_type.js'
        ROLE =                      Prefixes.BaseJavaScripts.otaku + 'otaku_role.js'
        SEASON =                    Prefixes.BaseJavaScripts.otaku + 'otaku_season.js'
        SEASON_FULL =               Prefixes.BaseJavaScripts.otaku + 'otaku_season_full.js'
        SERIALIZATION =             Prefixes.BaseJavaScripts.otaku + 'otaku_serialization.js'
        SONG =                      Prefixes.BaseJavaScripts.otaku + 'otaku_song.js'
        SONG_ED =                   Prefixes.BaseJavaScripts.otaku + 'otaku_song_ED.js'
        SONG_IN =                   Prefixes.BaseJavaScripts.otaku + 'otaku_song_IN.js'
        SONG_OP =                   Prefixes.BaseJavaScripts.otaku + 'otaku_song_OP.js'
        SOURCE =                    Prefixes.BaseJavaScripts.otaku + 'otaku_source.js'
        STATUS =                    Prefixes.BaseJavaScripts.otaku + 'otaku_status.js'
        STUDIO =                    Prefixes.BaseJavaScripts.otaku + 'otaku_studio.js'
        TEMP_CHARACTER =            Prefixes.BaseJavaScripts.otaku + 'otaku_temp_character.js'
        TEMP_PERSONS =              Prefixes.BaseJavaScripts.otaku + 'otaku_temp_persons.js'
        THEME =                     Prefixes.BaseJavaScripts.otaku + 'otaku_theme.js'
        TITLE_ANIME =               Prefixes.BaseJavaScripts.otaku + 'otaku_title_anime.js'
        TITLE_MANGA =               Prefixes.BaseJavaScripts.otaku + 'otaku_title_manga.js'
        TYPE =                      Prefixes.BaseJavaScripts.otaku + 'otaku_type.js'
        VOICE_CHARACTER =           Prefixes.BaseJavaScripts.otaku + 'otaku_voice_character.js'
        YEAR =                      Prefixes.BaseJavaScripts.otaku + 'otaku_year.js'

    class Renpy:
        CENSORSHIP =                Prefixes.BaseJavaScripts.renpy + 'renpy_censorship.js'
        DATA_GAME =                 Prefixes.BaseJavaScripts.renpy + 'renpy_data_game.js'
        DEVELOPER =                 Prefixes.BaseJavaScripts.renpy + 'renpy_developer.js'
        DEVELOPER_IMAGE =           Prefixes.BaseJavaScripts.renpy + 'renpy_developer_image.js'
        DEVELOPER_IMAGE_EXTRA =     Prefixes.BaseJavaScripts.renpy + 'renpy_developer_image_extra.js'
        DEVELOPER_LINKS =           Prefixes.BaseJavaScripts.renpy + 'renpy_developer_links.js'
        GAME =                      Prefixes.BaseJavaScripts.renpy + 'renpy_game.js'
        GAME_ENGINE =               Prefixes.BaseJavaScripts.renpy + 'renpy_game_engine.js'
        GAME_IMAGE =                Prefixes.BaseJavaScripts.renpy + 'renpy_game_image.js'
        GAME_IMAGE_EXTRA =          Prefixes.BaseJavaScripts.renpy + 'renpy_game_image_extra.js'
        GENRE =                     Prefixes.BaseJavaScripts.renpy + 'renpy_genre.js'
        PLATFORM =                  Prefixes.BaseJavaScripts.renpy + 'renpy_platform.js'
        PREFIX =                    Prefixes.BaseJavaScripts.renpy + 'renpy_prefix.js'
        PUBLISHER =                 Prefixes.BaseJavaScripts.renpy + 'renpy_publisher.js'
        PUBLISHER_IMAGE =           Prefixes.BaseJavaScripts.renpy + 'renpy_publisher_image.js'
        PUBLISHER_IMAGE_EXTRA =     Prefixes.BaseJavaScripts.renpy + 'renpy_publisher_image_extra.js'
        PUBLISHER_LINKS =           Prefixes.BaseJavaScripts.renpy + 'renpy_publisher_links.js'
        STATUS =                    Prefixes.BaseJavaScripts.renpy + 'renpy_status.js'
        TITLE_GAME =                Prefixes.BaseJavaScripts.renpy + 'renpy_title_game.js'
        TRANSLATOR =                Prefixes.BaseJavaScripts.renpy + 'renpy_translator.js'
        TRANSLATOR_IMAGE =          Prefixes.BaseJavaScripts.renpy + 'renpy_translator_image.js'
        TRANSLATOR_IMAGE_EXTRA =    Prefixes.BaseJavaScripts.renpy + 'renpy_translator_image_extra.js'
        TRANSLATOR_LINKS =          Prefixes.BaseJavaScripts.renpy + 'renpy_translator_links.js'

    class Serie:
        COMPANY =           Prefixes.BaseJavaScripts.serie + 'serie_company.js'
        GENRE =             Prefixes.BaseJavaScripts.serie + 'serie_genre.js'
        RATING =            Prefixes.BaseJavaScripts.serie + 'serie_rating.js'
        ROLE =              Prefixes.BaseJavaScripts.serie + 'serie_role.js'
        SERIE =             Prefixes.BaseJavaScripts.serie + 'serie_serie.js'
        SERIE_CAST =        Prefixes.BaseJavaScripts.serie + 'serie_serie_cast.js'
        SERIE_IMAGE =       Prefixes.BaseJavaScripts.serie + 'serie_serie_image.js'
        SERIE_IMAGE_EXTRA = Prefixes.BaseJavaScripts.serie + 'serie_serie_image_extra.js'
        SERIE_STAFF =       Prefixes.BaseJavaScripts.serie + 'serie_serie_staff.js'
        TITLE_SERIE =       Prefixes.BaseJavaScripts.serie + 'serie_title_serie.js'
        TYPE =              Prefixes.BaseJavaScripts.serie + 'serie_type.js'

####################################################    ImageCards
class ImageCards:
    class Users:
        USER = Prefixes.img_base + 'bg-users-user.webp'
    class Common:
        COUNTRY =            Prefixes.img_base + 'bg-common-country.webp'
        FORMAT =             Prefixes.img_base + 'bg-common-format.webp'
        IMAGE_SIZE =         Prefixes.img_base + 'bg-common-image_size.webp'
        LANGUAGE =           Prefixes.img_base + 'bg-common-language.webp'
        PERSON =             Prefixes.img_base + 'bg-common-person.webp'
        PERSON_IMAGE =       Prefixes.img_base + 'bg-common-person_image.webp'
        PERSON_IMAGE_EXTRA = Prefixes.img_base + 'bg-common-person_image_extra.webp'
        PERSON_NICKNAME =    Prefixes.img_base + 'bg-common-person_nickname.webp'
        QUALITY =            Prefixes.img_base + 'bg-common-quality.webp'
        WEBSITE =            Prefixes.img_base + 'bg-common-website.webp'

    class Movie:
        COMPANY =           Prefixes.img_base + 'bg-movie-company.webp'
        GENRE =             Prefixes.img_base + 'bg-movie-genre.webp'
        MOVIE =             Prefixes.img_base + 'bg-movie-movie.webp'
        MOVIE_CAST =        Prefixes.img_base + 'bg-movie-movie_cast.webp'
        MOVIE_IMAGE =       Prefixes.img_base + 'bg-movie-movie_image.webp'
        MOVIE_IMAGE_EXTRA = Prefixes.img_base + 'bg-movie-movie_image_extra.webp'
        MOVIE_STAFF =       Prefixes.img_base + 'bg-movie-movie_staff.webp'
        RATING =            Prefixes.img_base + 'bg-movie-rating.webp'
        ROLE =              Prefixes.img_base + 'bg-movie-role.webp'
        TITLE_MOVIE =       Prefixes.img_base + 'bg-movie-title_movie.webp'
        TYPE =              Prefixes.img_base + 'bg-movie-type.webp'

    class Music:
        ALBUM =                 Prefixes.img_base + 'bg-music-album.webp'
        ALBUM_IMAGE =           Prefixes.img_base + 'bg-music-album_image.webp'
        ALBUM_IMAGE_EXTRA =     Prefixes.img_base + 'bg-music-album_image_extra.webp'
        ALBUM_TYPE =            Prefixes.img_base + 'bg-music-album_type.webp'
        ARTIST =                Prefixes.img_base + 'bg-music-artist.webp'
        ARTIST_IMAGE =          Prefixes.img_base + 'bg-music-artist_image.webp'
        ARTIST_IMAGE_EXTRA =    Prefixes.img_base + 'bg-music-artist_image_extra.webp'
        ARTIST_MEMBER =         Prefixes.img_base + 'bg-music-artist_member.webp'
        ARTIST_TYPE =           Prefixes.img_base + 'bg-music-artist_type.webp'
        GENRE =                 Prefixes.img_base + 'bg-music-genre.webp'
        ROLE =                  Prefixes.img_base + 'bg-music-role.webp'
        SONG =                  Prefixes.img_base + 'bg-music-song.webp'

    class Otaku:
        ANIME =                     Prefixes.img_base + 'bg-otaku-anime.webp'
        ANIME_CHARACTER =           Prefixes.img_base + 'bg-otaku-anime_character.webp'
        ANIME_IMAGE =               Prefixes.img_base + 'bg-otaku-anime_image.webp'
        ANIME_IMAGE_EXTRA =         Prefixes.img_base + 'bg-otaku-anime_image_extra.webp'
        ANIME_STAFF =               Prefixes.img_base + 'bg-otaku-anime_staff.webp'
        AUTHOR_MANGA =              Prefixes.img_base + 'bg-otaku-author_manga.webp'
        CHARACTER =                 Prefixes.img_base + 'bg-otaku-character.webp'
        CHARACTER_IMAGE =           Prefixes.img_base + 'bg-otaku-character_image.webp'
        CHARACTER_IMAGE_EXTRA =     Prefixes.img_base + 'bg-otaku-character_image_extra.webp'
        CHARACTER_NICKNAME =        Prefixes.img_base + 'bg-otaku-character_nickname.webp'
        DATA_ANIME =                Prefixes.img_base + 'bg-otaku-data_anime.webp'
        DATA_ANIME_CHARACTERS =     Prefixes.img_base + 'bg-otaku-data_anime_characters.webp'
        DATA_ANIME_PICTURES =       Prefixes.img_base + 'bg-otaku-data_anime_pictures.webp'
        DATA_ANIME_STAFF =          Prefixes.img_base + 'bg-otaku-data_anime_staff.webp'
        DATA_CHARACTER =            Prefixes.img_base + 'bg-otaku-data_character.webp'
        DATA_CHARACTER_PICTURES =   Prefixes.img_base + 'bg-otaku-data_character_pictures.webp'
        DATA_IMAGE_URL =            Prefixes.img_base + 'bg-otaku-data_image_url.webp'
        DATA_MANGA =                Prefixes.img_base + 'bg-otaku-data_manga.webp'
        DATA_MANGA_CHARACTERS =     Prefixes.img_base + 'bg-otaku-data_manga_characters.webp'
        DATA_MANGA_PICTURES =       Prefixes.img_base + 'bg-otaku-data_manga_pictures.webp'
        DATA_PERSON =               Prefixes.img_base + 'bg-otaku-data_person.webp'
        DATA_PERSON_PICTURES =      Prefixes.img_base + 'bg-otaku-data_person_pictures.webp'
        DEMOGRAPHIC =               Prefixes.img_base + 'bg-otaku-demographic.webp'
        GENRE =                     Prefixes.img_base + 'bg-otaku-genre.webp'
        LICENSOR =                  Prefixes.img_base + 'bg-otaku-licensor.webp'
        MANGA =                     Prefixes.img_base + 'bg-otaku-manga.webp'
        MANGA_CHARACTER =           Prefixes.img_base + 'bg-otaku-manga_character.webp'
        MANGA_IMAGE =               Prefixes.img_base + 'bg-otaku-manga_image.webp'
        MANGA_IMAGE_EXTRA =         Prefixes.img_base + 'bg-otaku-manga_image_extra.webp'
        MEDIA_RELATION =            Prefixes.img_base + 'bg-otaku-media_relation.webp'
        MEDIA_RELATION_ANIME =      Prefixes.img_base + 'bg-otaku-media_relation_anime.webp'
        MEDIA_RELATION_MANGA =      Prefixes.img_base + 'bg-otaku-media_relation_manga.webp'
        PERSON =                    Prefixes.img_base + 'bg-otaku-person.webp'
        PERSON_IMAGE =              Prefixes.img_base + 'bg-otaku-person_image.webp'
        PERSON_IMAGE_EXTRA =        Prefixes.img_base + 'bg-otaku-person_image_extra.webp'
        PERSON_NICKNAME =           Prefixes.img_base + 'bg-otaku-person_nickname.webp'
        PRODUCER =                  Prefixes.img_base + 'bg-otaku-producer.webp'
        RATING =                    Prefixes.img_base + 'bg-otaku-rating.webp'
        RELATION_TYPE =             Prefixes.img_base + 'bg-otaku-relation_type.webp'
        ROLE =                      Prefixes.img_base + 'bg-otaku-role.webp'
        SEASON =                    Prefixes.img_base + 'bg-otaku-season.webp'
        SEASON_FULL =               Prefixes.img_base + 'bg-otaku-season_full.webp'
        SERIALIZATION =             Prefixes.img_base + 'bg-otaku-serialization.webp'
        SONG =                      Prefixes.img_base + 'bg-otaku-song.webp'
        SONG_ED =                   Prefixes.img_base + 'bg-otaku-song_ED.webp'
        SONG_IN =                   Prefixes.img_base + 'bg-otaku-song_IN.webp'
        SONG_OP =                   Prefixes.img_base + 'bg-otaku-song_OP.webp'
        SOURCE =                    Prefixes.img_base + 'bg-otaku-source.webp'
        STATUS =                    Prefixes.img_base + 'bg-otaku-status.webp'
        STUDIO =                    Prefixes.img_base + 'bg-otaku-studio.webp'
        TEMP_CHARACTER =            Prefixes.img_base + 'bg-otaku-temp_character.webp'
        TEMP_PERSONS =              Prefixes.img_base + 'bg-otaku-temp_persons.webp'
        THEME =                     Prefixes.img_base + 'bg-otaku-theme.webp'
        TITLE_ANIME =               Prefixes.img_base + 'bg-otaku-title_anime.webp'
        TITLE_MANGA =               Prefixes.img_base + 'bg-otaku-title_manga.webp'
        TYPE =                      Prefixes.img_base + 'bg-otaku-type.webp'
        VOICE_CHARACTER =           Prefixes.img_base + 'bg-otaku-voice_character.webp'
        YEAR =                      Prefixes.img_base + 'bg-otaku-year.webp'

    class Renpy:
        CENSORSHIP =                Prefixes.img_base + 'bg-renpy-censorship.webp'
        DATA_GAME =                 Prefixes.img_base + 'bg-renpy-data_game.webp'
        DEVELOPER =                 Prefixes.img_base + 'bg-renpy-developer.webp'
        DEVELOPER_IMAGE =           Prefixes.img_base + 'bg-renpy-developer_image.webp'
        DEVELOPER_IMAGE_EXTRA =     Prefixes.img_base + 'bg-renpy-developer_image_extra.webp'
        DEVELOPER_LINKS =           Prefixes.img_base + 'bg-renpy-developer_links.webp'
        GAME =                      Prefixes.img_base + 'bg-renpy-game.webp'
        GAME_ENGINE =               Prefixes.img_base + 'bg-renpy-game_engine.webp'
        GAME_IMAGE =                Prefixes.img_base + 'bg-renpy-game_image.webp'
        GAME_IMAGE_EXTRA =          Prefixes.img_base + 'bg-renpy-game_image_extra.webp'
        GENRE =                     Prefixes.img_base + 'bg-renpy-genre.webp'
        PLATFORM =                  Prefixes.img_base + 'bg-renpy-platform.webp'
        PREFIX =                    Prefixes.img_base + 'bg-renpy-prefix.webp'
        PUBLISHER =                 Prefixes.img_base + 'bg-renpy-publisher.webp'
        PUBLISHER_IMAGE =           Prefixes.img_base + 'bg-renpy-publisher_image.webp'
        PUBLISHER_IMAGE_EXTRA =     Prefixes.img_base + 'bg-renpy-publisher_image_extra.webp'
        PUBLISHER_LINKS =           Prefixes.img_base + 'bg-renpy-publisher_links.webp'
        STATUS =                    Prefixes.img_base + 'bg-renpy-status.webp'
        TITLE_GAME =                Prefixes.img_base + 'bg-renpy-title_game.webp'
        TRANSLATOR =                Prefixes.img_base + 'bg-renpy-translator.webp'
        TRANSLATOR_IMAGE =          Prefixes.img_base + 'bg-renpy-translator_image.webp'
        TRANSLATOR_IMAGE_EXTRA =    Prefixes.img_base + 'bg-renpy-translator_image_extra.webp'
        TRANSLATOR_LINKS =          Prefixes.img_base + 'bg-renpy-translator_links.webp'

    class Serie:
        COMPANY =           Prefixes.img_base + 'bg-serie-company.webp'
        GENRE =             Prefixes.img_base + 'bg-serie-genre.webp'
        RATING =            Prefixes.img_base + 'bg-serie-rating.webp'
        ROLE =              Prefixes.img_base + 'bg-serie-role.webp'
        SERIE =             Prefixes.img_base + 'bg-serie-serie.webp'
        SERIE_CAST =        Prefixes.img_base + 'bg-serie-serie_cast.webp'
        SERIE_IMAGE =       Prefixes.img_base + 'bg-serie-serie_image.webp'
        SERIE_IMAGE_EXTRA = Prefixes.img_base + 'bg-serie-serie_image_extra.webp'
        SERIE_STAFF =       Prefixes.img_base + 'bg-serie-serie_staff.webp'
        TITLE_SERIE =       Prefixes.img_base + 'bg-serie-title_serie.webp'
        TYPE =              Prefixes.img_base + 'bg-serie-type.webp'

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
