from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import View
from django.contrib import messages
from django.utils.translation import gettext as _
# Importando modelos User
from apps.users.models import CustomUser
from core.utils.send_emails import notify_password_reset, notify_blocked_user, notify_activated_user, notify_deleted_user
# Importando modelos Common
from apps.common.models import (
    Country, Format, ImageSize, Language, Person, PersonImage,
    PersonImageExtra, PersonNickname, Quality, Website
)

# Importando modelos Movie
from apps.movie.models import (
    Genre as GenreMovie, Type as TypeMovie, Role as RoleMovie, Rating as RatingMovie, Company as CompanyMovie,
    Movie, TitleMovie, MovieStaff, MovieCast, MovieImage, MovieImageExtra
)

# Importando modelos Music
from apps.music.models import (
    Genre as GenreMusic, Role as RoleMusic, AlbumType, ArtistType,
    Artist, ArtistMember, Album, Song,
    AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra
)

# Importando modelos Otaku
from apps.otaku.models import (
    Role as RoleOtaku, Year, Genre as GenreOtaku, Theme, Demographic,
    Type as TypeOtaku, Rating as RatingOtaku, Season, Status as StatusOtaku, Source, RelationType, SeasonFull,
    Producer, Licensor, Studio, Serialization,
    Anime, Manga, TitleAnime, TitleManga, AnimeSong, MediaRelation,
    Character, CharacterNickname, OtakuPerson, OtakuPersonNickname,
    AnimeCharacter, MangaCharacter, VoiceCharacter, AnimeStaff, AuthorManga,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra,
    OtakuPersonImage, OtakuPersonImageExtra, CharacterImage, CharacterImageExtra,
    DataAnime, DataAnimeCharacters, DataAnimePictures, DataAnimeStaff,
    DataManga, DataMangaCharacters, DataMangaPictures,
    DataCharacter, DataCharacterPictures, DataOtakuPerson, DataOtakuPersonPictures,
    DataImageURL, Temp_OtakuPersons, Temp_Characters
)

# Importando modelos Renpy
from apps.renpy.models import (
    Genre as GenreRenpy, GameEngine, Censorship, Prefix,
    Status as StatusRenpy, Platform,
    Developer, Translator, Publisher, Game,
    GameImage, GameImageExtra,
    DeveloperLink, TranslatorLink, PublisherLink,
    DeveloperImage, DeveloperImageExtra,
    TranslatorImage, TranslatorImageExtra,
    PublisherImage, PublisherImageExtra,
    TitleGame, F95GameFetchStatus
)

# Importando modelos Serie
from apps.serie.models import (
    Genre as GenreSerie, Type as TypeSerie, Role as RoleSerie,
    Rating as RatingSerie, Company as CompanySerie,
    Serie, TitleSerie, SerieStaff, SerieCast, SerieImage, SerieImageExtra
)

class ActionView(View):
    def post(self, request, *args, **kwargs):
        this_id = request.POST.get('id')
        action = request.POST.get('action')
        modelo = request.POST.get('model')
        name = request.POST.get('name')

        model_map = {
########################################################################################    USERS
            'Usuario': {
                'model': CustomUser,
                'listas_url': 'users_app:users_list',
                'update_url': 'users_app:users_update',
                'detail_url': 'users_app:users_detail',
                'es_usuario': True,
            },
########################################################################################    COMMON
            'País': {
                'model': Country,
                'listas_url': 'common_app:country_list',
                'update_url': 'common_app:country_update',
                'detail_url': 'common_app:country_detail',
                'es_usuario': False,
            },
            'Formato': {
                'model': Format,
                'listas_url': 'common_app:format_list',
                'update_url': 'common_app:format_update',
                'detail_url': 'common_app:format_detail',
                'es_usuario': False,
            },

            'Tamaño Imagen.': {
                'model': ImageSize,
                'listas_url': 'common_app:image_size_list',
                'update_url': 'common_app:image_size_update',
                'detail_url': 'common_app:image_size_detail',
                'es_usuario': False,
            },

            'Idioma': {
                'model': Language,
                'listas_url': 'common_app:language_list',
                'update_url': 'common_app:language_update',
                'detail_url': 'common_app:language_detail',
                'es_usuario': False,
            },

            'Persona': {
                'model': Person,
                'listas_url': 'common_app:person_list',
                'update_url': 'common_app:person_update',
                'detail_url': 'common_app:person_detail',
                'es_usuario': False,
            },

            'Imagen de Persona': {
                'model': PersonImage,
                'listas_url': 'common_app:person_image_list',
                'update_url': 'common_app:person_image_update',
                'detail_url': 'common_app:person_image_detail',
                'es_usuario': False,
            },

            'Imagen extra de Persona': {
                'model': PersonImageExtra,
                'listas_url': 'common_app:person_image_extra_list',
                'update_url': 'common_app:person_image_extra_update',
                'detail_url': 'common_app:person_image_extra_detail',
                'es_usuario': False,
            },
            'Apodo de Persona': {
                'model': PersonNickname,
                'listas_url': 'common_app:person_nickname_list',
                'update_url': 'common_app:person_nickname_update',
                'detail_url': 'common_app:person_nickname_detail',
                'es_usuario': False,
            },
            'Calidad': {
                'model': Quality,
                'listas_url': 'common_app:quality_list',
                'update_url': 'common_app:quality_update',
                'detail_url': 'common_app:quality_detail',
                'es_usuario': False,
            },
            'Sitio Web': {
                'model': Website,
                'listas_url': 'common_app:website_list',
                'update_url': 'common_app:website_update',
                'detail_url': 'common_app:website_detail',
                'es_usuario': False,
            },
# ########################################################################################    Musica
#             'Album': {
#                 'model': Album,
#                 'listas_url': 'music_app:album_list',
#                 'update_url': 'music_app:album_update',
#                 'detail_url': 'music_app:album_detail',
#                  'es_usuario': False,
##             },
##             'Artista': {
##                 'model': Artist,
##                 'listas_url': 'music_app:artist_list',
##                 'update_url': 'music_app:artist_update',
##                 'detail_url': 'music_app:artist_detail',
#                  'es_usuario': False,
##             },
##             'Género Musical': {
##                 'model': GenreMusic,
##                 'listas_url': 'music_app:genre_list',
##                 'update_url': 'music_app:genre_update',
##                 'detail_url': 'music_app:genre_detail',
#                  'es_usuario': False,
##             },
##             'Miembro': {
##                 'model': Member,
##                 'listas_url': 'music_app:member_list',
##                 'update_url': 'music_app:member_update',
##                 'detail_url': 'music_app:member_detail',
#                  'es_usuario': False,
##             },
##             'Canción': {
##                 'model': Song,
##                 'listas_url': 'music_app:song_list',
##                 'update_url': 'music_app:song_update',
##                 'detail_url': 'music_app:song_detail',
#                  'es_usuario': False,
##             },
##             'Membresia': {
##                 'model': Membership,
##                 'listas_url': 'music_app:membership_list',
##                 'update_url': 'music_app:membership_update',
##                 'detail_url': 'music_app:membership_detail',
#                  'es_usuario': False,
##             },
##             'Apodo del Miembro': {
##                 'model': MemberNickname,
##                 'listas_url': 'music_app:member_nickname_list',
##                 'update_url': 'music_app:member_nickname_update',
##                 'detail_url': 'music_app:member_nickname_detail',
#                  'es_usuario': False,
##             },
########################################################################################    Juegos Renpy
            'Censura': {
                'model': Censorship,
                'listas_url': 'renpy_app:censorship_list',
                'update_url': 'renpy_app:censorship_update',
                'detail_url': 'renpy_app:censorship_detail',
                'es_usuario': False,
            },

            'Desarrollador': {
                'model': Developer,
                'listas_url': 'renpy_app:developer_list',
                'update_url': 'renpy_app:developer_update',
                'detail_url': 'renpy_app:developer_detail',
                'es_usuario': False,
            },

            'Imagen del desarrollador': {
                'model': DeveloperImage,
                'listas_url': 'renpy_app:developer_image_list',
                'update_url': 'renpy_app:developer_image_update',
                'detail_url': 'renpy_app:developer_image_detail',
                'es_usuario': False,
            },

            'Imagen adicional del desarrollador': {
                'model': DeveloperImageExtra,
                'listas_url': 'renpy_app:developer_image_extra_list',
                'update_url': 'renpy_app:developer_image_extra_update',
                'detail_url': 'renpy_app:developer_image_extra_detail',
                'es_usuario': False,
            },

            'Enlace del desarrollador': {
                'model': DeveloperLink,
                'listas_url': 'renpy_app:developer_link_list',
                'update_url': 'renpy_app:developer_link_update',
                'detail_url': 'renpy_app:developer_link_detail',
                'es_usuario': False,
            },

            'Juego Renpy': {
                'model': Game,
                'listas_url': 'renpy_app:game_list',
                'update_url': 'renpy_app:game_update',
                'detail_url': 'renpy_app:game_detail',
                'es_usuario': False,
            },

            'Motor de desarrollo': {
                'model': GameEngine,
                'listas_url': 'renpy_app:game_engine_list',
                'update_url': 'renpy_app:game_engine_update',
                'detail_url': 'renpy_app:game_engine_detail',
                'es_usuario': False,
            },

            'Imagen del juego': {
                'model': GameImage,
                'listas_url': 'renpy_app:game_image_list',
                'update_url': 'renpy_app:game_image_update',
                'detail_url': 'renpy_app:game_image_detail',
                'es_usuario': False,
            },

            'Imagen adicional del juego': {
                'model': GameImageExtra,
                'listas_url': 'renpy_app:game_image_extra_list',
                'update_url': 'renpy_app:game_image_extra_update',
                'detail_url': 'renpy_app:game_image_extra_detail',
                'es_usuario': False,
            },

            'Género del juego': {
                'model': GenreRenpy,
                'listas_url': 'renpy_app:genre_list',
                'update_url': 'renpy_app:genre_update',
                'detail_url': 'renpy_app:genre_detail',
                'es_usuario': False,
            },

            'Plataforma del juego': {
                'model': Platform,
                'listas_url': 'renpy_app:platform_list',
                'update_url': 'renpy_app:platform_update',
                'detail_url': 'renpy_app:platform_detail',
                'es_usuario': False,
            },

            'Prefijo del juego': {
                'model': Prefix,
                'listas_url': 'renpy_app:prefix_list',
                'update_url': 'renpy_app:prefix_update',
                'detail_url': 'renpy_app:prefix_detail',
                'es_usuario': False,
            },

            'Editor': {
                'model': Publisher,
                'listas_url': 'renpy_app:publisher_list',
                'update_url': 'renpy_app:publisher_update',
                'detail_url': 'renpy_app:publisher_detail',
                'es_usuario': False,
            },

            'Imagen del editor': {
                'model': PublisherImage,
                'listas_url': 'renpy_app:publisher_image_list',
                'update_url': 'renpy_app:publisher_image_update',
                'detail_url': 'renpy_app:publisher_image_detail',
                'es_usuario': False,
            },

            'Imagen adicional del editor': {
                'model': PublisherImageExtra,
                'listas_url': 'renpy_app:publisher_image_extra_list',
                'update_url': 'renpy_app:publisher_image_extra_update',
                'detail_url': 'renpy_app:publisher_image_extra_detail',
                'es_usuario': False,
            },

            'Enlace del editor': {
                'model': PublisherLink,
                'listas_url': 'renpy_app:publisher_link_list',
                'update_url': 'renpy_app:publisher_link_update',
                'detail_url': 'renpy_app:publisher_link_detail',
                'es_usuario': False,
            },

            'Estado de juego': {
                'model': StatusRenpy,
                'listas_url': 'renpy_app:status_list',
                'update_url': 'renpy_app:status_update',
                'detail_url': 'renpy_app:status_detail',
                'es_usuario': False,
            },

            'Traductor': {
                'model': Translator,
                'listas_url': 'renpy_app:translator_list',
                'update_url': 'renpy_app:translator_update',
                'detail_url': 'renpy_app:translator_detail',
                'es_usuario': False,
            },

            'Imagen del traductor': {
                'model': TranslatorImage,
                'listas_url': 'renpy_app:translator_image_list',
                'update_url': 'renpy_app:translator_image_update',
                'detail_url': 'renpy_app:translator_image_detail',
                'es_usuario': False,
            },

            'Imagen adicional del traductor': {
                'model': TranslatorImageExtra,
                'listas_url': 'renpy_app:translator_image_extra_list',
                'update_url': 'renpy_app:translator_image_extra_update',
                'detail_url': 'renpy_app:translator_image_extra_detail',
                'es_usuario': False,
            },

            'Enlace del traductor': {
                'model': TranslatorLink,
                'listas_url': 'renpy_app:translator_link__list',
                'update_url': 'renpy_app:translator_link__update',
                'detail_url': 'renpy_app:translator_link__detail',
                'es_usuario': False,
            },

            'Título del juego': {
                'model': TitleGame,
                'listas_url': 'renpy_app:title_game_list',
                'update_url': 'renpy_app:title_game_update',
                'detail_url': 'renpy_app:title_game_detail',
                'es_usuario': False,
            },

## ########################################################################################    Otaku Data
##             'Genéro Otaku': {
##                 'model': Genre,
##                 'listas_url': 'otaku_app:genre_list',
##                 'update_url': 'otaku_app:genre_update',
##                 'detail_url': 'otaku_app:genre_detail',
#                  'es_usuario': False,
##             },
##             'Tema Otaku': {
##                 'model': Theme,
##                 'listas_url': 'otaku_app:theme_list',
##                 'update_url': 'otaku_app:theme_update',
##                 'detail_url': 'otaku_app:theme_detail',
#                  'es_usuario': False,
##             },
##             'Demografía Otaku': {
##                 'model': Demographic,
##                 'listas_url': 'otaku_app:demographic_list',
##                 'update_url': 'otaku_app:demographic_update',
##                 'detail_url': 'otaku_app:demographic_detail',
#                  'es_usuario': False,
##             },
##             'Año': {
##                 'model': Year,
##                 'listas_url': 'otaku_app:year_list',
##                 'update_url': 'otaku_app:year_update',
##                 'detail_url': 'otaku_app:year_detail',
#                  'es_usuario': False,
##             },
##             'Temporada': {
##                 'model': Season,
##                 'listas_url': 'otaku_app:season_list',
##                 'update_url': 'otaku_app:season_update',
##                 'detail_url': 'otaku_app:season_detail',
#                  'es_usuario': False,
##             },
##             'Temporada Completa': {
##                 'model': SeasonFull,
##                 'listas_url': 'otaku_app:seasonfull_list',
##                 'update_url': 'otaku_app:seasonfull_update',
##                 'detail_url': 'otaku_app:seasonfull_detail',
#                  'es_usuario': False,
##             },
##             'Título': {
##                 'model': Title,
##                 'listas_url': 'otaku_app:title_list',
##                 'update_url': 'otaku_app:title_update',
##                 'detail_url': 'otaku_app:title_detail',
#                  'es_usuario': False,
##             },
##             'Tipo': {
##                 'model': Type,
##                 'listas_url': 'otaku_app:type_list',
##                 'update_url': 'otaku_app:type_update',
##                 'detail_url': 'otaku_app:type_detail',
#                  'es_usuario': False,
##             },
##             'Estado': {
##                 'model': State,
##                 'listas_url': 'otaku_app:statu_list',
##                 'update_url': 'otaku_app:statu_update',
##                 'detail_url': 'otaku_app:statu_detail',
#                  'es_usuario': False,
##             },
##             'Tipo de Relación': {
##                 'model': RelationType,
##                 'listas_url': 'otaku_app:relation_type_list',
##                 'update_url': 'otaku_app:relation_type_update',
##                 'detail_url': 'otaku_app:relation_type_detail',
#                  'es_usuario': False,
##             },
## ########################################################################################    Otaku Companies
##             'Productora': {
##                 'model': Producer,
##                 'listas_url': 'otaku_app:producer_list',
##                 'update_url': 'otaku_app:producer_update',
##                 'detail_url': 'otaku_app:producer_detail',
#                  'es_usuario': False,
##             },
##             'Licenciante': {
##                 'model': Licensor,
##                 'listas_url': 'otaku_app:licensor_list',
##                 'update_url': 'otaku_app:licensor_update',
##                 'detail_url': 'otaku_app:licensor_detail',
#                  'es_usuario': False,
##             },
##             'Estudio': {
##                 'model': Studio,
##                 'listas_url': 'otaku_app:studio_list',
##                 'update_url': 'otaku_app:studio_update',
##                 'detail_url': 'otaku_app:studio_detail',
#                  'es_usuario': False,
##             },
##             'Serializadora': {
##                 'model': Serialization,
##                 'listas_url': 'otaku_app:serialization_list',
##                 'update_url': 'otaku_app:serialization_update',
##                 'detail_url': 'otaku_app:serialization_detail',
#                  'es_usuario': False,
##             },
## ########################################################################################    Otaku Chara-Voice
##             'Fuente': {
##                 'model': Source,
##                 'listas_url': 'otaku_app:source_list',
##                 'update_url': 'otaku_app:source_update',
##                 'detail_url': 'otaku_app:source_detail',
#                  'es_usuario': False,
##             },
##             'Clasificación de Anime': {
##                 'model': Rating,
##                 'listas_url': 'otaku_app:rating_list',
##                 'update_url': 'otaku_app:rating_update',
##                 'detail_url': 'otaku_app:rating_detail',
#                  'es_usuario': False,
##             },
## ########################################################################################    Otaku Chara-Voice
##             'Personaje': {
##                 'model': Character,
##                 'listas_url': 'otaku_app:character_anime_list',
##                 'update_url': 'otaku_app:character_update',
##                 'detail_url': 'otaku_app:character_detail',
#                  'es_usuario': False,
##             },
##             'Personaje de Anime': {
##                 'model': Character,
##                 'listas_url': 'otaku_app:character_anime_list',
##                 'update_url': 'otaku_app:character_update',
##                 'detail_url': 'otaku_app:character_detail',
#                  'es_usuario': False,
##             },
##             'Personaje de Manga': {
##                 'model': Character,
##                 'listas_url': 'otaku_app:character_manga_list',
##                 'update_url': 'otaku_app:character_update',
##                 'detail_url': 'otaku_app:character_detail',
#                  'es_usuario': False,
##             },
##             'Persona': {
##                 'model': Person,
##                 'listas_url': 'otaku_app:person_list',
##                 'update_url': 'otaku_app:person_update',
##                 'detail_url': 'otaku_app:person_detail',
#                  'es_usuario': False,
##             },
##             'Actor de voz': {
##                 'model': PersonVoiceCharacter,
##                 'listas_url': 'otaku_app:voice_actors_list',
##                 'update_url': 'otaku_app:voice_actors_update',
##                 'detail_url': 'otaku_app:person_detail',
#                  'es_usuario': False,
##             },
##             'Personal de Anime': {
##                 'model': PersonStaffAnime,
##                 'listas_url': 'otaku_app:animestaff_list',
##                 'update_url': 'otaku_app:animestaff_update',
##                 'detail_url': 'otaku_app:person_detail',
#                  'es_usuario': False,
##             },
##             'Autor de Manga': {
##                 'model': PersonAuthorManga,
##                 'listas_url': 'otaku_app:author_list',
##                 'update_url': 'otaku_app:author_update',
##                 'detail_url': 'otaku_app:person_detail',
#                  'es_usuario': False,
##             },
##             'Apodo de Persona': {
##                 'model': NicknamePerson,
##                 'listas_url': 'otaku_app:nickname_person_list',
##                 'update_url': 'otaku_app:nickname_person_update',
##             },
##             'Apodo de Personaje': {
##                 'model': NicknameCharacter,
##                 'listas_url': 'otaku_app:nickname_character_list',
##                 'update_url': 'otaku_app:nickname_character_update',
##             },
## ########################################################################################    Otaku Anime
##             'Portada de Anime': {
##                 'model': CoverAnime,
##                 'listas_url': 'otaku_app:cover_anime_list',
##                 'update_url': 'otaku_app:cover_anime_update',
##                 'detail_url': 'otaku_app:cover_anime_detail',
#                  'es_usuario': False,
##             },
##             'Portada de Manga': {
##                 'model': CoverManga,
##                 'listas_url': 'otaku_app:cover_manga_list',
##                 'update_url': 'otaku_app:cover_manga_update',
##                 'detail_url': 'otaku_app:cover_manga_detail',
#                  'es_usuario': False,
##             },
##             'Foto de Personaje': {
##                 'model': CoverCharacter,
##                 'listas_url': 'otaku_app:cover_character_list',
##                 'update_url': 'otaku_app:cover_character_update',
##                 'detail_url': 'otaku_app:cover_character_detail',
#                  'es_usuario': False,
##             },
##             'Foto de Persona': {
##                 'model': CoverPerson,
##                 'listas_url': 'otaku_app:cover_person_list',
##                 'update_url': 'otaku_app:cover_person_update',
##                 'detail_url': 'otaku_app:cover_person_detail',
#                  'es_usuario': False,
##             },
## ########################################################################################    Otaku Anime
##             'Imagen de Anime': {
##                 'model': ExtraImageAnime,
##                 'listas_url': 'otaku_app:anime_image_list',
##                 'update_url': 'otaku_app:anime_image_update',
##                 'detail_url': 'otaku_app:anime_image_detail',
#                  'es_usuario': False,
##             },
##             'Imagen de Manga': {
##                 'model': ExtraImageManga,
##                 'listas_url': 'otaku_app:anime_image_list',
##                 'update_url': 'otaku_app:anime_image_update',
##                 'detail_url': 'otaku_app:anime_image_detail',
#                  'es_usuario': False,
##             },
##             'Imagen de Personaje': {
##                 'model': ExtraImageCharacter,
##                 'listas_url': 'otaku_app:anime_image_list',
##                 'update_url': 'otaku_app:anime_image_update',
##                 'detail_url': 'otaku_app:anime_image_detail',
#                  'es_usuario': False,
##             },
##             'Imagen de Persona': {
##                 'model': ExtraImagePerson,
##                 'listas_url': 'otaku_app:anime_image_list',
##                 'update_url': 'otaku_app:anime_image_update',
##                 'detail_url': 'otaku_app:anime_image_detail',
#                  'es_usuario': False,
##             },
## ########################################################################################    Otaku AnimeSong
##             'Canción de Anime': {
##                 'model': AnimeSong,
##                 'listas_url': 'otaku_app:anime_song_list',
##                 'update_url': 'otaku_app:anime_song_update',
##                 'detail_url': 'otaku_app:anime_song_detail',
#                  'es_usuario': False,
##             },
##             'Opening': {
##                 'model': AnimeSong,
##                 'listas_url': 'otaku_app:anime_song_op_list',
##                 'update_url': 'otaku_app:anime_song_op_update',
##                 'detail_url': 'otaku_app:anime_song_detail',
#                  'es_usuario': False,
##             },
##             'Ending': {
##                 'model': AnimeSong,
##                 'listas_url': 'otaku_app:anime_song_ed_list',
##                 'update_url': 'otaku_app:anime_song_ed_update',
##                 'detail_url': 'otaku_app:anime_song_detail',
#                  'es_usuario': False,
##             },
##             'Insert Song': {
##                 'model': AnimeSong,
##                 'listas_url': 'otaku_app:anime_song_in_list',
##                 'update_url': 'otaku_app:anime_song_in_update',
##                 'detail_url': 'otaku_app:anime_song_detail',
#                  'es_usuario': False,
##             },
## ########################################################################################    Peliculas
##             'Anime': {
##                 'model': Anime,
##                 'listas_url': 'otaku_app:anime_list',
##                 'update_url': 'otaku_app:anime_update',
##                 'detail_url': 'otaku_app:anime_detail',
#                  'es_usuario': False,
##             },
##             'Manga': {
##                 'model': Manga,
##                 'listas_url': 'otaku_app:manga_list',
##                 'update_url': 'otaku_app:manga_update',
##                 'detail_url': 'otaku_app:manga_detail',
#                  'es_usuario': False,
##             },
########################################################################################    Peliculas
        }
        try:
            if modelo in model_map:
                model_data = model_map[modelo]
                instance = get_object_or_404(model_data['model'], pk=this_id)

                if action == "1":  # Ver
                    return redirect(reverse(model_data['detail_url'], kwargs={'pk': instance.id}))

                elif action == "2":  # Editar
                    return redirect(reverse(model_data['update_url'], kwargs={'pk': instance.id}))

                elif action == "3":  # Activar
                    if model_data.get('es_usuario'):
                        instance.is_active = True
                        instance.save()
                        notify_activated_user(instance)
                    else:
                        instance.is_active = True
                        instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s ha sido activado.') % {'modelo': modelo, 'name': name})

                elif action == "4":  # Desactivar
                    if model_data.get('es_usuario'):
                        instance.is_active = False
                        instance.save()
                        notify_blocked_user(instance)
                    else:
                        instance.is_active = False
                        instance.save()

                    messages.success(request, _('El %(modelo)s %(name)s ha sido desactivado.') % {'modelo': modelo, 'name': name})

                elif action == "5":  # Hacer Explicito Solo Generos
                    instance.explicit = True
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s es explícito.') % {'modelo': modelo, 'name': name})

                elif action == "6":  # Hacer No Explicito Solo Generos
                    instance.explicit = False
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s ya no es explícito.') % {'modelo': modelo, 'name': name})

                elif action == "7":  # Hacer Staff Solo User
                    instance.is_staff = True
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s es miembro del equipo ahora.') % {'modelo': modelo, 'name': name})

                elif action == "8":  # Quitar de Staff Solo User
                    instance.is_staff = False
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s ya no es miembro del equipo.') % {'modelo': modelo, 'name': name})

                elif action == "9":  # Hacer Super User Solo User
                    instance.is_superuser = True
                    instance.is_staff = True
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s es superusuario ahora.') % {'modelo': modelo, 'name': name})

                elif action == "10":  # Quitar Super User Solo User
                    instance.is_superuser = False
                    instance.is_staff = False
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s ya no es superusuario.') % {'modelo': modelo, 'name': name})

                elif action == "11":  # Reiniciar contraseña
                    new_password = 'Frikiverso'
                    instance.set_password(new_password)
                    instance.save()
                    notify_password_reset(instance, new_password)
                    messages.success(request, _('La contraseña de %(modelo)s %(name)s ha sido reiniciada.') % {'modelo': modelo, 'name': name})

                # elif action == "99":  # Eliminar
                #     instance.delete()
                #     messages.success(request, _('El %(modelo)s %(name)s ha sido eliminado.') % {'modelo': modelo, 'name': name})


                elif action == "99":  # Eliminar
                    if model_data.get('es_usuario'):
                        instance.delete()
                        notify_deleted_user(instance)
                    else:
                        instance.delete()
                    messages.success(request, _('El %(modelo)s %(name)s ha sido eliminado.') % {'modelo': modelo, 'name': name})

                else:
                    messages.error(request, _('Acción no válida.'))

                return redirect(model_data['listas_url'])

            else:
                messages.error(request, _('Modelo "%(modelo)s" no encontrado en el mapa.') % {'modelo': modelo})
                return redirect('home_app:home')

        except model_data['model'].DoesNotExist:
            messages.error(request, _('%(modelo)s no encontrado.') % {'modelo': modelo})

        return redirect('home_app:home')