from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import View
from django.contrib import messages
from django.utils.translation import gettext as _
# Importando modelos User
from apps.users.models import CustomUser

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
            },
########################################################################################    COMMON
            'País': {
                'model': Country,
                'listas_url': 'common_app:country_list',
                'update_url': 'common_app:country_update',
                'detail_url': 'common_app:country_detail',
            },
            'Formato': {
                'model': Format,
                'listas_url': 'common_app:format_list',
                'update_url': 'common_app:format_update',
                'detail_url': 'common_app:format_detail',
            },

            'Tamaño Imagen.': {
                'model': ImageSize,
                'listas_url': 'common_app:image_size_list',
                'update_url': 'common_app:image_size_update',
                'detail_url': 'common_app:image_size_detail',
            },

            'Idioma': {
                'model': Language,
                'listas_url': 'common_app:language_list',
                'update_url': 'common_app:language_update',
                'detail_url': 'common_app:language_detail',
            },

            'Persona': {
                'model': Person,
                'listas_url': 'common_app:person_list',
                'update_url': 'common_app:person_update',
                'detail_url': 'common_app:person_detail',
            },

            'Imagen de Persona': {
                'model': PersonImage,
                'listas_url': 'common_app:person_image_list',
                'update_url': 'common_app:person_image_update',
                'detail_url': 'common_app:person_image_detail',
            },

            'Imagen extra de Persona': {
                'model': PersonImageExtra,
                'listas_url': 'common_app:person_image_extra_list',
                'update_url': 'common_app:person_image_extra_update',
                'detail_url': 'common_app:person_image_extra_detail',
            },
            'Apodo de Persona': {
                'model': PersonNickname,
                'listas_url': 'common_app:person_nickname_list',
                'update_url': 'common_app:person_nickname_update',
                'detail_url': 'common_app:person_nickname_detail',
            },
            'Calidad': {
                'model': Quality,
                'listas_url': 'common_app:quality_list',
                'update_url': 'common_app:quality_update',
                'detail_url': 'common_app:quality_detail',
            },
            'Sitio Web': {
                'model': Website,
                'listas_url': 'common_app:website_list',
                'update_url': 'common_app:website_update',
                'detail_url': 'common_app:website_detail',
            },
# ########################################################################################    Musica
#             'Album': {
#                 'model': Album,
#                 'listas_url': 'music_app:album_list',
#                 'update_url': 'music_app:album_update',
#                 'detail_url': 'music_app:album_detail',
#             },
#             'Artista': {
#                 'model': Artist,
#                 'listas_url': 'music_app:artist_list',
#                 'update_url': 'music_app:artist_update',
#                 'detail_url': 'music_app:artist_detail',
#             },
#             'Género Musical': {
#                 'model': GenreMusic,
#                 'listas_url': 'music_app:genre_list',
#                 'update_url': 'music_app:genre_update',
#                 'detail_url': 'music_app:genre_detail',
#             },
#             'Miembro': {
#                 'model': Member,
#                 'listas_url': 'music_app:member_list',
#                 'update_url': 'music_app:member_update',
#                 'detail_url': 'music_app:member_detail',
#             },
#             'Canción': {
#                 'model': Song,
#                 'listas_url': 'music_app:song_list',
#                 'update_url': 'music_app:song_update',
#                 'detail_url': 'music_app:song_detail',
#             },
#             'Membresia': {
#                 'model': Membership,
#                 'listas_url': 'music_app:membership_list',
#                 'update_url': 'music_app:membership_update',
#                 'detail_url': 'music_app:membership_detail',
#             },
#             'Apodo del Miembro': {
#                 'model': MemberNickname,
#                 'listas_url': 'music_app:member_nickname_list',
#                 'update_url': 'music_app:member_nickname_update',
#                 'detail_url': 'music_app:member_nickname_detail',
#             },
# ########################################################################################    Juegos Renpy
#             'Desarrollador': {
#                 'model': Developer,
#                 'listas_url': 'renpy_app:developer_list',
#                 'update_url': 'renpy_app:developer_update',
#                 'detail_url': 'renpy_app:developer_detail',
#             },
#             'Traductor': {
#                 'model': Translator,
#                 'listas_url': 'renpy_app:translator_list',
#                 'update_url': 'renpy_app:translator_update',
#                 'detail_url': 'renpy_app:translator_detail',
#             },
#             'Editor': {
#                 'model': Publisher,
#                 'listas_url': 'renpy_app:publisher_list',
#                 'update_url': 'renpy_app:publisher_update',
#                 'detail_url': 'renpy_app:publisher_detail',
#             },
#             'Link de Desarrollador': {
#                 'model': DeveloperLink,
#                 'listas_url': 'renpy_app:developer_link_list',
#                 'update_url': 'renpy_app:developer_link_update',
#                 'detail_url': 'renpy_app:developer_link_detail',
#             },
#             'Link de Traductor': {
#                 'model': TranslatorLink,
#                 'listas_url': 'renpy_app:translator_link_list',
#                 'update_url': 'renpy_app:translator_link_update',
#                 'detail_url': 'renpy_app:translator_link_detail',
#             },
#             'Link de Editor': {
#                 'model': PublisherLink,
#                 'listas_url': 'renpy_app:publisher_link_list',
#                 'update_url': 'renpy_app:publisher_link_update',
#                 'detail_url': 'renpy_app:publisher_link_detail',
#             },
#             'Género de Juego': {
#                 'model': GenreRenpy,
#                 'listas_url': 'renpy_app:genre_list',
#                 'update_url': 'renpy_app:genre_update',
#                 'detail_url': 'renpy_app:genre_detail',
#             },
#             'Motor de Desarrollo': {
#                 'model': GameEngine,
#                 'listas_url': 'renpy_app:engine_list',
#                 'update_url': 'renpy_app:engine_update',
#                 'detail_url': 'renpy_app:engine_detail',
#             },
#             'Estado de Juego': {
#                 'model': GameState,
#                 'listas_url': 'renpy_app:game_statu_list',
#                 'update_url': 'renpy_app:game_statu_update',
#                 'detail_url': 'renpy_app:game_statu_detail',
#             },
#             'Plataforma': {
#                 'model': Platform,
#                 'listas_url': 'renpy_app:platform_list',
#                 'update_url': 'renpy_app:platform_update',
#                 'detail_url': 'renpy_app:platform_detail',
#             },
#             'Juego Renpy': {
#                 'model': Game,
#                 'listas_url': 'renpy_app:game_list',
#                 'update_url': 'renpy_app:game_update',
#                 'detail_url': 'renpy_app:game_detail',
#             },
#             'Imagen de Juego': {
#                 'model': GameImage,
#                 'listas_url': 'renpy_app:game_image_list',
#                 'update_url': 'renpy_app:game_image_update',
#                 'detail_url': 'renpy_app:game_image_detail',
#             },
# ########################################################################################    Otaku Data
#             'Genéro Otaku': {
#                 'model': Genre,
#                 'listas_url': 'otaku_app:genre_list',
#                 'update_url': 'otaku_app:genre_update',
#                 'detail_url': 'otaku_app:genre_detail',
#             },
#             'Tema Otaku': {
#                 'model': Theme,
#                 'listas_url': 'otaku_app:theme_list',
#                 'update_url': 'otaku_app:theme_update',
#                 'detail_url': 'otaku_app:theme_detail',
#             },
#             'Demografía Otaku': {
#                 'model': Demographic,
#                 'listas_url': 'otaku_app:demographic_list',
#                 'update_url': 'otaku_app:demographic_update',
#                 'detail_url': 'otaku_app:demographic_detail',
#             },
#             'Año': {
#                 'model': Year,
#                 'listas_url': 'otaku_app:year_list',
#                 'update_url': 'otaku_app:year_update',
#                 'detail_url': 'otaku_app:year_detail',
#             },
#             'Temporada': {
#                 'model': Season,
#                 'listas_url': 'otaku_app:season_list',
#                 'update_url': 'otaku_app:season_update',
#                 'detail_url': 'otaku_app:season_detail',
#             },
#             'Temporada Completa': {
#                 'model': SeasonFull,
#                 'listas_url': 'otaku_app:seasonfull_list',
#                 'update_url': 'otaku_app:seasonfull_update',
#                 'detail_url': 'otaku_app:seasonfull_detail',
#             },
#             'Título': {
#                 'model': Title,
#                 'listas_url': 'otaku_app:title_list',
#                 'update_url': 'otaku_app:title_update',
#                 'detail_url': 'otaku_app:title_detail',
#             },
#             'Tipo': {
#                 'model': Type,
#                 'listas_url': 'otaku_app:type_list',
#                 'update_url': 'otaku_app:type_update',
#                 'detail_url': 'otaku_app:type_detail',
#             },
#             'Estado': {
#                 'model': State,
#                 'listas_url': 'otaku_app:statu_list',
#                 'update_url': 'otaku_app:statu_update',
#                 'detail_url': 'otaku_app:statu_detail',
#             },
#             'Tipo de Relación': {
#                 'model': RelationType,
#                 'listas_url': 'otaku_app:relation_type_list',
#                 'update_url': 'otaku_app:relation_type_update',
#                 'detail_url': 'otaku_app:relation_type_detail',
#             },
# ########################################################################################    Otaku Companies
#             'Productora': {
#                 'model': Producer,
#                 'listas_url': 'otaku_app:producer_list',
#                 'update_url': 'otaku_app:producer_update',
#                 'detail_url': 'otaku_app:producer_detail',
#             },
#             'Licenciante': {
#                 'model': Licensor,
#                 'listas_url': 'otaku_app:licensor_list',
#                 'update_url': 'otaku_app:licensor_update',
#                 'detail_url': 'otaku_app:licensor_detail',
#             },
#             'Estudio': {
#                 'model': Studio,
#                 'listas_url': 'otaku_app:studio_list',
#                 'update_url': 'otaku_app:studio_update',
#                 'detail_url': 'otaku_app:studio_detail',
#             },
#             'Serializadora': {
#                 'model': Serialization,
#                 'listas_url': 'otaku_app:serialization_list',
#                 'update_url': 'otaku_app:serialization_update',
#                 'detail_url': 'otaku_app:serialization_detail',
#             },
# ########################################################################################    Otaku Chara-Voice
#             'Fuente': {
#                 'model': Source,
#                 'listas_url': 'otaku_app:source_list',
#                 'update_url': 'otaku_app:source_update',
#                 'detail_url': 'otaku_app:source_detail',
#             },
#             'Clasificación de Anime': {
#                 'model': Rating,
#                 'listas_url': 'otaku_app:rating_list',
#                 'update_url': 'otaku_app:rating_update',
#                 'detail_url': 'otaku_app:rating_detail',
#             },
# ########################################################################################    Otaku Chara-Voice
#             'Personaje': {
#                 'model': Character,
#                 'listas_url': 'otaku_app:character_anime_list',
#                 'update_url': 'otaku_app:character_update',
#                 'detail_url': 'otaku_app:character_detail',
#             },
#             'Personaje de Anime': {
#                 'model': Character,
#                 'listas_url': 'otaku_app:character_anime_list',
#                 'update_url': 'otaku_app:character_update',
#                 'detail_url': 'otaku_app:character_detail',
#             },
#             'Personaje de Manga': {
#                 'model': Character,
#                 'listas_url': 'otaku_app:character_manga_list',
#                 'update_url': 'otaku_app:character_update',
#                 'detail_url': 'otaku_app:character_detail',
#             },
#             'Persona': {
#                 'model': Person,
#                 'listas_url': 'otaku_app:person_list',
#                 'update_url': 'otaku_app:person_update',
#                 'detail_url': 'otaku_app:person_detail',
#             },
#             'Actor de voz': {
#                 'model': PersonVoiceCharacter,
#                 'listas_url': 'otaku_app:voice_actors_list',
#                 'update_url': 'otaku_app:voice_actors_update',
#                 'detail_url': 'otaku_app:person_detail',
#             },
#             'Personal de Anime': {
#                 'model': PersonStaffAnime,
#                 'listas_url': 'otaku_app:animestaff_list',
#                 'update_url': 'otaku_app:animestaff_update',
#                 'detail_url': 'otaku_app:person_detail',
#             },
#             'Autor de Manga': {
#                 'model': PersonAuthorManga,
#                 'listas_url': 'otaku_app:author_list',
#                 'update_url': 'otaku_app:author_update',
#                 'detail_url': 'otaku_app:person_detail',
#             },
#             'Apodo de Persona': {
#                 'model': NicknamePerson,
#                 'listas_url': 'otaku_app:nickname_person_list',
#                 'update_url': 'otaku_app:nickname_person_update',
#             },
#             'Apodo de Personaje': {
#                 'model': NicknameCharacter,
#                 'listas_url': 'otaku_app:nickname_character_list',
#                 'update_url': 'otaku_app:nickname_character_update',
#             },
# ########################################################################################    Otaku Anime
#             'Portada de Anime': {
#                 'model': CoverAnime,
#                 'listas_url': 'otaku_app:cover_anime_list',
#                 'update_url': 'otaku_app:cover_anime_update',
#                 'detail_url': 'otaku_app:cover_anime_detail',
#             },
#             'Portada de Manga': {
#                 'model': CoverManga,
#                 'listas_url': 'otaku_app:cover_manga_list',
#                 'update_url': 'otaku_app:cover_manga_update',
#                 'detail_url': 'otaku_app:cover_manga_detail',
#             },
#             'Foto de Personaje': {
#                 'model': CoverCharacter,
#                 'listas_url': 'otaku_app:cover_character_list',
#                 'update_url': 'otaku_app:cover_character_update',
#                 'detail_url': 'otaku_app:cover_character_detail',
#             },
#             'Foto de Persona': {
#                 'model': CoverPerson,
#                 'listas_url': 'otaku_app:cover_person_list',
#                 'update_url': 'otaku_app:cover_person_update',
#                 'detail_url': 'otaku_app:cover_person_detail',
#             },
# ########################################################################################    Otaku Anime
#             'Imagen de Anime': {
#                 'model': ExtraImageAnime,
#                 'listas_url': 'otaku_app:anime_image_list',
#                 'update_url': 'otaku_app:anime_image_update',
#                 'detail_url': 'otaku_app:anime_image_detail',
#             },
#             'Imagen de Manga': {
#                 'model': ExtraImageManga,
#                 'listas_url': 'otaku_app:anime_image_list',
#                 'update_url': 'otaku_app:anime_image_update',
#                 'detail_url': 'otaku_app:anime_image_detail',
#             },
#             'Imagen de Personaje': {
#                 'model': ExtraImageCharacter,
#                 'listas_url': 'otaku_app:anime_image_list',
#                 'update_url': 'otaku_app:anime_image_update',
#                 'detail_url': 'otaku_app:anime_image_detail',
#             },
#             'Imagen de Persona': {
#                 'model': ExtraImagePerson,
#                 'listas_url': 'otaku_app:anime_image_list',
#                 'update_url': 'otaku_app:anime_image_update',
#                 'detail_url': 'otaku_app:anime_image_detail',
#             },
# ########################################################################################    Otaku AnimeSong
#             'Canción de Anime': {
#                 'model': AnimeSong,
#                 'listas_url': 'otaku_app:anime_song_list',
#                 'update_url': 'otaku_app:anime_song_update',
#                 'detail_url': 'otaku_app:anime_song_detail',
#             },
#             'Opening': {
#                 'model': AnimeSong,
#                 'listas_url': 'otaku_app:anime_song_op_list',
#                 'update_url': 'otaku_app:anime_song_op_update',
#                 'detail_url': 'otaku_app:anime_song_detail',
#             },
#             'Ending': {
#                 'model': AnimeSong,
#                 'listas_url': 'otaku_app:anime_song_ed_list',
#                 'update_url': 'otaku_app:anime_song_ed_update',
#                 'detail_url': 'otaku_app:anime_song_detail',
#             },
#             'Insert Song': {
#                 'model': AnimeSong,
#                 'listas_url': 'otaku_app:anime_song_in_list',
#                 'update_url': 'otaku_app:anime_song_in_update',
#                 'detail_url': 'otaku_app:anime_song_detail',
#             },
# ########################################################################################    Peliculas
#             'Anime': {
#                 'model': Anime,
#                 'listas_url': 'otaku_app:anime_list',
#                 'update_url': 'otaku_app:anime_update',
#                 'detail_url': 'otaku_app:anime_detail',
#             },
#             'Manga': {
#                 'model': Manga,
#                 'listas_url': 'otaku_app:manga_list',
#                 'update_url': 'otaku_app:manga_update',
#                 'detail_url': 'otaku_app:manga_detail',
#             },
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
                    instance.is_active = True
                    instance.save()
                    messages.success(request, _('El %(modelo)s %(name)s ha sido activado.') % {'modelo': modelo, 'name': name})

                elif action == "4":  # Desactivar
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
                    new_password = 'frikiverso'
                    instance.set_password(new_password)
                    instance.save()
                    messages.success(request, _('La contraseña de %(modelo)s %(name)s ha sido reiniciada.') % {'modelo': modelo, 'name': name})

                elif action == "99":  # Eliminar
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