from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (
    Role, Year, Genre, Theme, Demographic, Type, Rating, Season, Status, Source, RelationType, SeasonFull,
    Anime, Manga, TitleAnime, TitleManga, AnimeSong, MediaRelation,
    Character, CharacterNickname, Person, PersonNickname,
    AnimeCharacter, MangaCharacter, VoiceCharacter, AnimeStaff, AuthorManga,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra, PersonImage, PersonImageExtra, CharacterImage, CharacterImageExtra,
    DataAnime, DataAnimeCharacters, DataAnimePictures, DataAnimeStaff, DataManga, DataMangaCharacters, DataMangaPictures, DataCharacter,
    DataCharacterPictures, DataPerson, DataPersonPictures, DataImageURL,
    Temp_Persons, Temp_Characters
    )
# impot Resource
from .resources import (
    RoleResource, YearResource, GenreResource, ThemeResource, DemographicResource, TypeResource, RatingResource, SeasonResource, StatusResource, SourceResource, RelationTypeResource, SeasonFullResource,
    AnimeResource, MangaResource, TitleAnimeResource, TitleMangaResource, AnimeSongResource, MediaRelationResource,
    CharacterResource, CharacterNicknameResource, PersonResource, PersonNicknameResource,
    AnimeCharacterResource, MangaCharacterResource, VoiceCharacterResource, AnimeStaffResource, AuthorMangaResource,
    AnimeImageResource, AnimeImageExtraResource, MangaImageResource, MangaImageExtraResource, PersonImageResource, PersonImageExtraResource, CharacterImageResource, CharacterImageExtraResource,
    DataAnimeResource, DataAnimeCharactersResource, DataAnimePicturesResource, DataAnimeStaffResource, DataMangaResource, DataMangaCharactersResource, DataMangaPicturesResource, DataCharacterResource,
    DataCharacterPicturesResource, DataPersonResource, DataPersonPicturesResource, DataImageURLResource,
    Temp_PersonsResource, Temp_CharactersResource
    )
# impot Inline
from apps.otaku.utils.inline import (
    TitleAnimeInline, TitleMangaInline, CharacterNicknameInline, PersonNicknameInline, AnimeImageInline, AnimeImageExtraInline, MangaImageInline, MangaImageExtraInline,
    PersonImageInline, PersonImageExtraInline, CharacterImageInline, CharacterImageExtraInline
    )
# Register your models here.
########################################################################################################    Admin para Role
@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'role_staff', 'role_chara', 'role_manga', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial', 'role_staff', 'role_chara', 'role_manga')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Aplicación del Rol'), {
            'fields': ('role_staff', 'role_chara', 'role_manga')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar roles seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d rol(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún rol para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar roles seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d rol(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún rol para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Year
@admin.register(Year)
class YearAdmin(ImportExportModelAdmin):
    resource_class = YearResource

    list_display = ('year', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('year', 'slug')
    ordering = ('year',)
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('year',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar años seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d año(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún año para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar años seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d año(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún año para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Genre
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'explicit', 'is_active', 'created_at')
    list_filter = ('is_active', 'explicit', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('parent', 'name', 'name_esp', 'description')
        }),
        (_('Atributos'), {
            'fields': ('explicit',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar géneros seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d género(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar géneros seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d género(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Theme
@admin.register(Theme)
class ThemeAdmin(ImportExportModelAdmin):
    resource_class = ThemeResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'explicit', 'is_active', 'created_at')
    list_filter = ('is_active', 'explicit', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('parent', 'name', 'name_esp', 'description')
        }),
        (_('Atributos'), {
            'fields': ('explicit',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar temas seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tema(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tema para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar temas seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tema(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tema para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Demographic
@admin.register(Demographic)
class DemographicAdmin(ImportExportModelAdmin):
    resource_class = DemographicResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'explicit', 'is_active', 'created_at')
    list_filter = ('is_active', 'explicit', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('parent', 'name', 'name_esp', 'description')
        }),
        (_('Atributos'), {
            'fields': ('explicit',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar demografías seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d demografía(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún demografía para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar demografías seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d demografía(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún demografía para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Type
@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    resource_class = TypeResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('parent', 'name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar tipos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tipo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar tipos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tipo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Rating
@admin.register(Rating)
class RatingAdmin(ImportExportModelAdmin):
    resource_class = RatingResource

    list_display = ('acronym', 'name', 'name_esp', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('acronym', 'name', 'name_esp', 'slug')
    ordering = ('created_at', 'acronym', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('acronym', 'name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', )
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar clasificaciones seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d clasificación(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún clasificación para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar clasificaciones seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d clasificación(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún clasificación para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Season
@admin.register(Season)
class SeasonAdmin(ImportExportModelAdmin):
    resource_class = SeasonResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar temporadas seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d temporada(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún temporada para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar temporadas seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d temporada(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún temporada para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Status
@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar estados seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d estado(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún estado para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar estados seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d estado(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún estado para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Source
@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    resource_class = SourceResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar fuentes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d fuente(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún fuente para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar fuentes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d fuente(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún fuente para desactivar.'), messages.WARNING)

########################################################################################################    Admin para RelationType
@admin.register(RelationType)
class RelationTypeAdmin(ImportExportModelAdmin):
    resource_class = RelationTypeResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar tipos de relación seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tipo(s) de relación.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo de relación para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar tipos de relación seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tipo(s) de relación.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo de relación para desactivar.'), messages.WARNING)

########################################################################################################    Admin para SeasonFull
@admin.register(SeasonFull)
class SeasonFullAdmin(ImportExportModelAdmin):
    resource_class = SeasonFullResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('created_at', 'name',)
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar temporadas completas seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d temporada(s) completa(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún temporada completa para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar temporadas completas seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d temporada(s) completa(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún temporada completa para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Anime
@admin.register(Anime)
class AnimeAdmin(ImportExportModelAdmin):
    resource_class = AnimeResource

    inlines = [TitleAnimeInline, AnimeImageInline, AnimeImageExtraInline,]

    list_display = ('title', 'anime_type', 'status', 'season', 'year', 'episodes', 'is_active', 'created_at')
    list_filter = ('anime_type', 'status', 'season', 'year', 'is_active')
    search_fields = ('title', 'title_eng', 'title_jap', 'mal_id', 'p_mal_id', 'url')
    ordering = ('-created_at', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('title', 'title_eng', 'title_jap', 'episodes', 'from_date', 'to_date', 'synopsis')
        }),
        (_('Relaciones'), {
            'fields': (
                'anime_type', 'status', 'season', 'season_full', 'year',
                'source', 'rating', 'producers', 'licensors', 'studios',
                'genres', 'themes', 'demographics'
            )
        }),
        (_('Información MAL'), {
            'fields': ('url', 'mal_id', 'p_mal_id')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar animes seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d anime(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún anime para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar animes seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d anime(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún anime para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Manga
@admin.register(Manga)
class MangaAdmin(ImportExportModelAdmin):
    resource_class = MangaResource

    inlines = [TitleMangaInline, MangaImageInline, MangaImageExtraInline,]

    list_display = ('title', 'manga_type', 'status', 'year', 'chapters', 'volumes', 'is_active', 'created_at')
    list_filter = ('manga_type', 'status', 'year', 'is_active')
    search_fields = ('title', 'title_eng', 'title_jap', 'mal_id', 'p_mal_id', 'url')
    ordering = ('-created_at', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('title', 'title_eng', 'title_jap', 'chapters', 'volumes', 'published_from', 'published_to', 'synopsis')
        }),
        (_('Relaciones'), {
            'fields': (
                'manga_type', 'status', 'season', 'season_full', 'year',
                'source', 'rating', 'serializations',
                'genres', 'themes', 'demographics'
            )
        }),
        (_('Información MAL'), {
            'fields': ('url', 'mal_id', 'p_mal_id')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar mangas seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d manga(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún manga para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar mangas seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d manga(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún manga para desactivar.'), messages.WARNING)

########################################################################################################    Admin para TitleAnime
@admin.register(TitleAnime)
class TitleAnimeAdmin(ImportExportModelAdmin):
    resource_class = TitleAnimeResource

    list_display = ('title', 'anime', 'title_lang', 'initial', 'is_active', 'created_at')
    list_filter = ('title_lang', 'is_active')
    search_fields = ('title', 'anime__title', 'slug')
    ordering = ('anime', 'title_lang', 'initial', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Relación y Título'), {
            'fields': ('anime', 'title_lang', 'title')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar títulos de anime seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d título(s) de anime.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún título de anime para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar títulos de anime seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d título(s) de anime.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún título de anime para desactivar.'), messages.WARNING)

########################################################################################################    Admin para TitleManga
@admin.register(TitleManga)
class TitleMangaAdmin(ImportExportModelAdmin):
    resource_class = TitleMangaResource

    list_display = ('title', 'manga', 'title_lang', 'initial', 'is_active', 'created_at')
    list_filter = ('title_lang', 'is_active')
    search_fields = ('title', 'manga__title', 'slug')
    ordering = ('manga', 'title_lang', 'initial', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Relación y Título'), {
            'fields': ('manga', 'title_lang', 'title')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar títulos de manga seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d título(s) de manga.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún título de manga para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar títulos de manga seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d título(s) de manga.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún título de manga para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Character
@admin.register(Character)
class CharacterAdmin(ImportExportModelAdmin):
    resource_class = CharacterResource  # Si usas django-import-export

    inlines = [CharacterNicknameInline, CharacterImageInline, CharacterImageExtraInline, ]

    list_display = ('full_name', 'mal_id', 'p_mal_id', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'name_kanji', 'mal_id')
    ordering = ('-created_at', 'initial', 'full_name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('full_name', 'name_kanji', 'biography',)
        }),
        (_('Información MAL'), {
            'fields': ('url', 'mal_id', 'p_mal_id')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar personajes seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d personaje(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún personaje para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar personajes seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d personaje(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún personaje para desactivar.'), messages.WARNING)

########################################################################################################    Admin para CharacterNickname
@admin.register(CharacterNickname)
class CharacterNicknameAdmin(ImportExportModelAdmin):
    resource_class = CharacterNicknameResource  # Si usas django-import-export

    list_display = ('character', 'nickname', 'initial', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial', 'character')
    search_fields = ('nickname', 'character__full_name', 'character__mal_id', 'character__p_mal_id')
    ordering = ('initial', 'nickname')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character', 'nickname')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar apodos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d apodo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún apodo para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar apodos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d apodo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún apodo para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Person
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource  # Si usas django-import-export

    list_display = ('full_name', 'mal_id', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'name_kanji', 'mal_id')
    ordering = ('-created_at', 'initial', 'full_name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('full_name', 'name_kanji', 'biography',)
        }),
        (_('Información MAL'), {
            'fields': ('url', 'mal_id', 'p_mal_id')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    inlines = [PersonNicknameInline, PersonImageInline, PersonImageExtraInline,]

    @admin.action(description=_('Activar personas seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d persona(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún persona para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar personas seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d persona(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún persona para desactivar.'), messages.WARNING)

########################################################################################################    Admin para PersonNickname
@admin.register(PersonNickname)
class PersonNicknameAdmin(ImportExportModelAdmin):
    resource_class = PersonNicknameResource  # Si usas django-import-export

    list_display = ('person', 'nickname', 'initial', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial', 'person')
    search_fields = ('nickname', 'person__full_name', 'person__mal_id', 'person__p_mal_id')
    ordering = ('initial', 'nickname')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person', 'nickname')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar apodos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d apodo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún apodo para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar apodos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d apodo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún apodo para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AnimeSong
@admin.register(AnimeSong)
class AnimeSongAdmin(ImportExportModelAdmin):
    resource_class = AnimeSongResource

    list_display = ('anime', 'song_type', 'song_id', 'title', 'is_active', 'created_at')
    list_filter = ('is_active', 'song_type', 'anime')
    search_fields = ('title', 'anime__title', 'anime__mal_id', 'song_id', 'artist__name')
    ordering = ('anime', 'song_type', 'song_id', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('anime', 'song_type', 'song_id', 'title', 'title_kanji', 'title_eng', 'artist',)
        }),
        ('Datos Completos', {
            'fields': ('title_full',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug', 'initial')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar canciones seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d canción(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún canción para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar canciones seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d canción(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún canción para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AnimeCharacter
@admin.register(AnimeCharacter)
class AnimeCharacterAdmin(ImportExportModelAdmin):
    resource_class = AnimeCharacterResource

    list_display = ('character', 'anime', 'role', 'character_mal_id', 'anime_mal_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime', 'role')
    search_fields = ('character__full_name', 'anime__title', 'role__name', 'character_mal_id', 'anime_mal_id')
    ordering = ('anime', 'role', 'character_mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character', 'anime', 'role',)
        }),
        (_('Información MAL'), {
            'fields': ('character_mal_id', 'anime_mal_id',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar personajes seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d personaje(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún personaje para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar personajes seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d personaje(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún personaje para desactivar.'), messages.WARNING)

########################################################################################################    Admin para MangaCharacter
@admin.register(MangaCharacter)
class MangaCharacterAdmin(ImportExportModelAdmin):
    resource_class = MangaCharacterResource

    list_display = ('character', 'manga', 'role', 'character_mal_id', 'manga_mal_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'manga', 'role')
    search_fields = ('character__full_name', 'manga__title', 'role__name', 'character_mal_id', 'manga_mal_id')
    ordering = ('manga', 'role', 'character_mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character', 'manga', 'role',)
        }),
        (_('Información MAL'), {
            'fields': ('character_mal_id', 'manga_mal_id',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar personajes seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d personaje(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún personaje para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar personajes seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d personaje(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún personaje para desactivar.'), messages.WARNING)

########################################################################################################    Admin para VoiceCharacter
@admin.register(VoiceCharacter)
class VoiceCharacterAdmin(ImportExportModelAdmin):
    resource_class = VoiceCharacterResource

    list_display = ('person', 'anime', 'character', 'language', 'person_mal_id', 'anime_mal_id', 'character_mal_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime', 'language', 'person')
    search_fields = ('person__full_name', 'anime__title', 'character__full_name', 'language__name', 'person_mal_id', 'anime_mal_id', 'character_mal_id')
    ordering = ('anime', 'character', 'person')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person', 'anime', 'character', 'language', )
        }),
        (_('Información MAL'), {
            'fields': ('person_mal_id', 'anime_mal_id', 'character_mal_id')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar actores de voz seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d actor(es) de voz.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún actor de voz para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar actores de voz seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d actor(es) de voz.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún actor de voz para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AnimeStaff
@admin.register(AnimeStaff)
class AnimeStaffAdmin(ImportExportModelAdmin):
    resource_class = AnimeStaffResource

    list_display = ('person', 'anime', 'position', 'person_mal_id', 'anime_mal_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime', 'position', 'person')
    search_fields = ('person__full_name', 'anime__title', 'position__name', 'person_mal_id', 'anime_mal_id',)
    ordering = ('anime', 'position', 'person')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person', 'anime', 'position',)
        }),
        (_('Información MAL'), {
            'fields': ('person_mal_id', 'anime_mal_id',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar staff de anime seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d miembro(s) de personal.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún miembro de personal para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar staff de anime seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d miembro(s) de personal.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún miembro de personal para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AuthorManga
@admin.register(AuthorManga)
class AuthorMangaAdmin(ImportExportModelAdmin):
    resource_class = AuthorMangaResource

    list_display = ('person', 'manga', 'position', 'person_mal_id', 'manga_mal_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'manga', 'position', 'person')
    search_fields = ('person__full_name', 'manga__title', 'position__name', 'person_mal_id', 'manga_mal_id')
    ordering = ('manga', 'position', 'person')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person', 'manga', 'position',)
        }),
        (_('Información MAL'), {
            'fields': ('person_mal_id', 'manga_mal_id',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar autores de manga seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d autor(es) de manga.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún autor de manga para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar autores de manga seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d autor(es) de manga.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún autor de manga para desactivar.'), messages.WARNING)

########################################################################################################    Admin para MediaRelation
@admin.register(MediaRelation)
class MediaRelationAdmin(ImportExportModelAdmin):
    resource_class = MediaRelationResource

    list_display = ('relation_type','from_entry_mal_id', 'from_entry_type', 'to_entry_mal_id', 'to_entry_type', 'is_active', 'created_at')
    list_filter = ('is_active', 'relation_type', 'from_entry_type', 'to_entry_type')
    search_fields = ('from_entry_mal_id', 'to_entry_mal_id', 'from_entry_mal_id_p', 'to_entry_mal_id_p')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_('Relación de Media'), {
            'fields': (
                'relation_type',
                ('from_entry_type', 'from_entry_mal_id', 'from_entry_mal_id_p',),
                ('to_entry_type', 'to_entry_mal_id', 'to_entry_mal_id_p',),
            )
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )
    actions = ['activar', 'desactivar']

    @admin.action(description=_('✅ Activar relaciones seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d relación(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún relación para activar.'), messages.WARNING)

    @admin.action(description=_('❌ Desactivar relaciones seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d relación(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún relación para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AnimeImage
@admin.register(AnimeImage)
class AnimeImageAdmin(ImportExportModelAdmin):
    resource_class = AnimeImageResource

    list_display = ('anime', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime', 'size_image')
    search_fields = ('anime__title', 'image_url')
    ordering = ('anime', 'size_image',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('anime', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AnimeImageExtra
@admin.register(AnimeImageExtra)
class AnimeImageExtraAdmin(ImportExportModelAdmin):
    resource_class = AnimeImageExtraResource

    list_display = ('anime', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime')
    search_fields = ('anime__title',)
    ordering = ('anime',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('anime',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para MangaImage
@admin.register(MangaImage)
class MangaImageAdmin(ImportExportModelAdmin):
    resource_class = MangaImageResource

    list_display = ('manga', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'manga', 'size_image')
    search_fields = ('manga__title', 'image_url')
    ordering = ('manga', 'size_image',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('manga', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para MangaImageExtra
@admin.register(MangaImageExtra)
class MangaImageExtraAdmin(ImportExportModelAdmin):
    resource_class = MangaImageExtraResource

    list_display = ('manga', 'is_active', 'created_at')
    list_filter = ('is_active', 'manga')
    search_fields = ('manga__title',)
    ordering = ('manga',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('manga',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para PersonImage
@admin.register(PersonImage)
class PersonImageAdmin(ImportExportModelAdmin):
    resource_class = PersonImageResource

    list_display = ('person', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'person', 'size_image')
    search_fields = ('person__full_name', 'image_url')
    ordering = ('person', 'size_image',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para PersonImageExtra
@admin.register(PersonImageExtra)
class PersonImageExtraAdmin(ImportExportModelAdmin):
    resource_class = PersonImageExtraResource
# 'name', 'slug',
    list_display = ('person', 'is_active', 'created_at')
    list_filter = ('is_active', 'person')
    search_fields = ('person__full_name',)
    ordering = ('person',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para CharacterImage
@admin.register(CharacterImage)
class CharacterImageAdmin(ImportExportModelAdmin):
    resource_class = CharacterImageResource

    list_display = ('character', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'character', 'size_image')
    search_fields = ('character__full_name', 'image_url')
    ordering = ('character', 'size_image',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para CharacterImageExtra
@admin.register(CharacterImageExtra)
class CharacterImageExtraAdmin(ImportExportModelAdmin):
    resource_class = CharacterImageExtraResource

    list_display = ('character', 'is_active', 'created_at')
    list_filter = ('is_active', 'character')
    search_fields = ('character__full_name',)
    ordering = ('character',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para DataAnime
@admin.register(DataAnime)
class DataAnimeAdmin(ImportExportModelAdmin):
    resource_class = DataAnimeResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para DataAnimeCharacters
@admin.register(DataAnimeCharacters)
class DataAnimeCharactersAdmin(admin.ModelAdmin):
    resource_class = DataAnimeCharactersResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataAnimePictures
@admin.register(DataAnimePictures)
class DataAnimePicturesAdmin(admin.ModelAdmin):
    resource_class = DataAnimePicturesResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataAnimeStaff
@admin.register(DataAnimeStaff)
class DataAnimeStaffAdmin(admin.ModelAdmin):
    resource_class = DataAnimeStaffResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataManga
@admin.register(DataManga)
class DataMangaAdmin(admin.ModelAdmin):
    resource_class = DataMangaResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataMangaCharacters
@admin.register(DataMangaCharacters)
class DataMangaCharactersAdmin(admin.ModelAdmin):
    resource_class = DataMangaCharactersResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataMangaPictures
@admin.register(DataMangaPictures)
class DataMangaPicturesAdmin(admin.ModelAdmin):
    resource_class = DataMangaPicturesResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataCharacter
@admin.register(DataCharacter)
class DataCharacterAdmin(admin.ModelAdmin):
    resource_class = DataCharacterResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataCharacterPictures
@admin.register(DataCharacterPictures)
class DataCharacterPicturesAdmin(admin.ModelAdmin):
    resource_class = DataCharacterPicturesResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataPerson
@admin.register(DataPerson)
class DataPersonAdmin(admin.ModelAdmin):
    resource_class = DataPersonResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataPersonPictures
@admin.register(DataPersonPictures)
class DataPersonPicturesAdmin(admin.ModelAdmin):
    resource_class = DataPersonPicturesResource

    list_display = ('mal_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('mal_id', 'url')
    ordering = ('-created_at', 'mal_id')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('mal_id', 'url', 'data',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para DataImageURL
@admin.register(DataImageURL)
class DataImageURLAdmin(admin.ModelAdmin):
    resource_class = DataImageURLResource

    list_display = ('url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('url',)
    ordering = ('-created_at', 'url')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['marcar_como_procesado', 'marcar_como_no_procesado']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('url',)
        }),
        (_('Estado'), {
            'fields': ('status', 'processed',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description=_('Marcar como procesado'))
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, _('Se marcaron como procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como procesado.'), messages.WARNING)

    @admin.action(description=_('Marcar como no procesado'))
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, _('Se marcaron como no procesado(s) %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún egistro para marcar como no procesado.'), messages.WARNING)

########################################################################################################    Admin para Temp_Persons
@admin.register(Temp_Persons)
class TempPersonsAdmin(ImportExportModelAdmin):
    resource_class = Temp_PersonsResource

    list_display = ('mal_id_person', 'lenguaje')
    list_filter = ('lenguaje',)
    search_fields = ('mal_id_person', 'lenguaje')
    ordering = ('mal_id_person', 'lenguaje')

    actions = ['eliminar_duplicados']

    fieldsets = (
        ('Datos Temporales', {
            'fields': ('mal_id_person', 'lenguaje')
        }),
    )

    @admin.action(description=_('🧹 Eliminar duplicados'))
    def eliminar_duplicados(self, request, queryset):
        vistos = set()
        eliminados = 0
        for obj in queryset:
            key = (obj.mal_id_person, obj.lenguaje)
            if key in vistos:
                obj.delete()
                eliminados += 1
            else:
                vistos.add(key)
        if eliminados:
            self.message_user(request, f"✅ {eliminados} duplicado(s) eliminado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se encontraron duplicados para eliminar.", messages.INFO)

########################################################################################################    Admin para Temp_Characters
@admin.register(Temp_Characters)
class TempCharactersAdmin(ImportExportModelAdmin):
    resource_class = Temp_CharactersResource

    list_display = ('mal_id_character',)
    search_fields = ('mal_id_character',)
    ordering = ('mal_id_character',)

    actions = ['eliminar_seleccionados']

    fieldsets = (
        ('Datos Temporales', {
            'fields': ('mal_id_character',)
        }),
    )

    @admin.action(description=_('🗑️ Eliminar personajes seleccionados'))
    def eliminar_seleccionados(self, request, queryset):
        cantidad = queryset.count()
        queryset.delete()
        self.message_user(request, f"✅ {cantidad} personaje(s) eliminado(s).", messages.SUCCESS)
