common_app = 'common_app:'
movie_app = 'movie_app:'
music_app = 'music_app:'
otaku_app = 'otaku_app:'
renpy_app = 'renpy_app:'
serie_app = 'serie_app:'
users_app = 'users_app:'
pages_app = 'pages_app:'

####################################################    Templates
class Templates:
    HOME = 'home/home.html'

    class Users:
        prefix = 'users/user/'
        LOGIN       = prefix + 'user_login.html'

        LST = prefix + 'user_list.html'
        ADD = prefix + 'user_form.html'
        UPT = prefix + 'user_update.html'
        DTL = prefix + 'user_detail.html'
        CHANGE_PASS = prefix + 'user_password_change.html'

    class Common:
        class Format:
            prefix = 'common/format/'

            LST = prefix + 'format_list.html'
            ADD = prefix + 'format_form.html'
            UPT = prefix + 'format_form.html'
            DTL = prefix + 'format_detail.html'

        class Language:
            prefix = 'common/language/'

            LST = prefix + 'language_list.html'
            ADD = prefix + 'language_form.html'
            UPT = prefix + 'language_form.html'
            DTL = prefix + 'language_detail.html'

        class Country:
            prefix = 'common/country/'

            LST = prefix + 'country_list.html'
            ADD = prefix + 'country_form.html'
            UPT = prefix + 'country_form.html'
            DTL = prefix + 'country_detail.html'

####################################################    URLS
class URLS:
    class Main:
        LOGIN = 'users_app:login'
        INDEX = pages_app + 'index'

    class Home:
        COMMON = common_app + 'home'
        MOVIE = movie_app + 'home'
        MUSIC = music_app + 'home'
        OTAKU = otaku_app + 'home'
        RENPY = renpy_app + 'home'
        SERIE = serie_app + 'home'
        USERS = users_app + 'home'
        # OTAKU_DATA = otaku_app + 'data_home'
        # OTAKU_ANIME = otaku_app + 'anime_home'
        # OTAKU_MANGA = otaku_app + 'manga_home'
        # OTAKU_PERSON_CHARACTER = otaku_app + 'persons_characters_home'
        # OTAKU_RELATION = otaku_app + 'relation_home'

    class Users:
        LST = users_app + 'users_list'
        ADD = users_app + 'users_create'
        UPD = users_app + 'users_update'
        DTL = users_app + 'users_detail'
        ADD_SUPER = users_app + 'superuser_create'
        ADD_STAFF = users_app + 'staffuser_create'

    class Common:
        class Country:
            LST = common_app + 'country_list'
            ADD = common_app + 'country_create'
            UPD = common_app + 'country_update'
            DTL = common_app + 'country_detail'

        class Format:
            LST = common_app + 'format_list'
            ADD = common_app + 'format_create'
            UPD = common_app + 'format_update'
            DTL = common_app + 'format_detail'

        class ImageSize:
            LST = common_app + 'image_size_list'
            ADD = common_app + 'image_size_create'
            UPD = common_app + 'image_size_update'
            DTL = common_app + 'image_size_detail'

        class Language:
            LST = common_app + 'language_list'
            ADD = common_app + 'language_create'
            UPD = common_app + 'language_update'
            DTL = common_app + 'language_detail'

        class Person:
            LST = common_app + 'person_list'
            ADD = common_app + 'person_create'
            UPD = common_app + 'person_update'
            DTL = common_app + 'person_detail'

        class PersonImage:
            LST = common_app + 'person_image_list'
            ADD = common_app + 'person_image_create'
            UPD = common_app + 'person_image_update'
            DTL = common_app + 'person_image_detail'

        class PersonImageExtra:
            LST = common_app + 'person_image_extra_list'
            ADD = common_app + 'person_image_extra_create'
            UPD = common_app + 'person_image_extra_update'
            DTL = common_app + 'person_image_extra_detail'

        class PersonNickname:
            LST = common_app + 'person_nickname_list'
            ADD = common_app + 'person_nickname_create'
            UPD = common_app + 'person_nickname_update'
            DTL = common_app + 'person_nickname_detail'

        class Quality:
            LST = common_app + 'quality_list'
            ADD = common_app + 'quality_create'
            UPD = common_app + 'quality_update'
            DTL = common_app + 'quality_detail'

        class Website:
            LST = common_app + 'website_list'
            ADD = common_app + 'website_create'
            UPD = common_app + 'website_update'
            DTL = common_app + 'website_detail'

    class Music:
        pass

    class Movie:
        pass

    class Otaku:
        class Anime:
            LST = otaku_app + 'anime_list'

        class Manga:
            LST = otaku_app + 'manga_list'

        class Person:
            LST = otaku_app + 'person_list'

        class Character:
            LST = otaku_app + 'character_list'

    class OtakuLoad:
            ANIME = otaku_app + 'anime_load'
            MANGA = otaku_app + 'manga_load'
            PERSON = otaku_app + 'person_load'
            CHARACTER = otaku_app + 'character_load'

    class Renpy:
        pass

    class Serie:
        pass

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
        COUNTRY = 'js/DataTables/config/common/country_config.js'
        FORMAT = 'js/DataTables/config/common/format_config.js'
        IMAGE_SIZE = 'js/DataTables/config/common/image_size_config.js'
        LANGUAGE = 'js/DataTables/config/common/language_config.js'
        PERSON = 'js/DataTables/config/common/person_config.js'
        PERSON_IMAGE = 'js/DataTables/config/common/person_image_config.js'
        PERSON_IMAGE_EXTRA = 'js/DataTables/config/common/person_image_extra_config.js'
        PERSON_NICKNAME = 'js/DataTables/config/common/person_nickname_config.js'
        QUALITY = 'js/DataTables/config/common/quality_config.js'
        WEBSITE = 'js/DataTables/config/common/website_config.js'

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

    class OtakuHome:
        ANIME =             'img/screen/wide/bg-home-otaku-anime.webp'
        DATA =              'img/screen/wide/bg-home-otaku-data.webp'
        IMAGEN =            'img/screen/wide/bg-home-otaku-imagen.webp'
        MANGA =             'img/screen/wide/bg-home-otaku-manga.webp'
        PERSON_CHARACTER =  'img/screen/wide/bg-home-otaku-person_character.webp'
        RELATION =          'img/screen/wide/bg-home-otaku-relation.webp'

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
        COUNTRY = 'País'
        FORMAT = 'Formato'
        IMAGE_SIZE = 'Tamaño Img.'
        LANGUAGE = 'Idioma'
        PERSON = 'Persona'
        PERSON_IMAGE = 'Imagen de Persona'
        PERSON_IMAGE_EXTRA = 'Imagen extra de Persona'
        PERSON_NICKNAME = 'Apodo de Persona'
        QUALITY = 'Calidad'
        WEBSITE = 'Sitio Web'


