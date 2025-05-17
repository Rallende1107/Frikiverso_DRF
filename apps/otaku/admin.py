from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (
    Role, Year, Genre, Theme, Demographic, Type, Rating, Season, Status, Source, RelationType, SeasonFull,
    Producer, Licensor, Studio, Serialization, Anime, Manga, TitleAnime, TitleManga, AnimeSong, MediaRelation,
    Character, CharacterNickname, OtakuPerson, OtakuPersonNickname,
    AnimeCharacter, MangaCharacter, VoiceCharacter, AnimeStaff, AuthorManga,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra, OtakuPersonImage, OtakuPersonImageExtra, CharacterImage, CharacterImageExtra,
    DataAnime, DataAnimeCharacters, DataAnimePictures, DataAnimeStaff, DataManga, DataMangaCharacters, DataMangaPictures, DataCharacter,
    DataCharacterPictures, DataOtakuPerson, DataOtakuPersonPictures, DataImageURL,
    Temp_OtakuPersons, Temp_Characters
    )
# impot Resource
from .resources import (
    RoleResource, YearResource, GenreResource, ThemeResource, DemographicResource, TypeResource, RatingResource, SeasonResource, StatusResource, SourceResource, RelationTypeResource, SeasonFullResource,
    ProducerResource, LicensorResource, StudioResource, SerializationResource, AnimeResource, MangaResource, TitleAnimeResource, TitleMangaResource, AnimeSongResource, MediaRelationResource,
    CharacterResource, CharacterNicknameResource, OtakuPersonResource, OtakuPersonNicknameResource,
    AnimeCharacterResource, MangaCharacterResource, VoiceCharacterResource, AnimeStaffResource, AuthorMangaResource,
    AnimeImageResource, AnimeImageExtraResource, MangaImageResource, MangaImageExtraResource, OtakuPersonImageResource, OtakuPersonImageExtraResource, CharacterImageResource, CharacterImageExtraResource,
    DataAnimeResource, DataAnimeCharactersResource, DataAnimePicturesResource, DataAnimeStaffResource, DataMangaResource, DataMangaCharactersResource, DataMangaPicturesResource, DataCharacterResource,
    DataCharacterPicturesResource, DataOtakuPersonResource, DataOtakuPersonPicturesResource, DataImageURLResource,
    Temp_OtakuPersonsResource, Temp_CharactersResource
    )
# impot Inline
from apps.otaku.utils.inline import (
    TitleAnimeInline, TitleMangaInline, CharacterNicknameInline, OtakuPersonNicknameInline, AnimeImageInline, AnimeImageExtraInline, MangaImageInline, MangaImageExtraInline,
    OtakuPersonImageInline, OtakuPersonImageExtraInline, CharacterImageInline, CharacterImageExtraInline
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

    @admin.action(description='Activar roles seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} rol(es) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún rol para activar.", messages.WARNING)

    @admin.action(description='Desactivar roles seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} rol(es) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún rol para desactivar.", messages.WARNING)

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

    @admin.action(description='Activar años seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} año(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún año para activar.", messages.WARNING)

    @admin.action(description='Desactivar años seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} año(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún año para desactivar.", messages.WARNING)

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

    @admin.action(description='Activar géneros seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} género(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún género para activar.", messages.WARNING)

    @admin.action(description='Desactivar géneros seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} género(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún género para desactivar.", messages.WARNING)

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

    @admin.action(description='Activar temas seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tema(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tema para activar.", messages.WARNING)

    @admin.action(description='Desactivar temas seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tema(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tema para desactivar.", messages.WARNING)

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

    @admin.action(description='Activar demografías seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} demografía(s) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar demografías seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} demografía(s) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar tipos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} tipo(s) activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar tipos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} tipo(s) desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar clasificaciones seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} clasificación(es) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar clasificaciones seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} clasificación(es) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar temporadas seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} temporada(s) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar temporadas seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} temporada(s) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar estados seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} estado(s) activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar estados seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} estado(s) desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar fuentes seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} fuente(s) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar fuentes seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} fuente(s) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar tipos de relación seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} tipo(s) de relación activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar tipos de relación seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} tipo(s) de relación desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar temporadas completas seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} temporada(s) completa(s) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar temporadas completas seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} temporada(s) completa(s) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para Producer
@admin.register(Producer)
class ProducerAdmin(ImportExportModelAdmin):
    resource_class = ProducerResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'slug')
    ordering = ('created_at', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name',)
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

    @admin.action(description='Activar productoras seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} productora(s) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar productoras seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} productora(s) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para Licensor
@admin.register(Licensor)
class LicensorAdmin(ImportExportModelAdmin):
    resource_class = LicensorResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'slug')
    ordering = ('-created_at', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name',)
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

    @admin.action(description='Activar licenciantes seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} licenciante(s) activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar licenciantes seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} licenciante(s) desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para Studio
@admin.register(Studio)
class StudioAdmin(ImportExportModelAdmin):
    resource_class = StudioResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'slug')
    ordering = ('-created_at', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name',)
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

    @admin.action(description='Activar estudios seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} estudio(s) activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar estudios seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} estudio(s) desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para Serialization
@admin.register(Serialization)
class SerializationAdmin(ImportExportModelAdmin):
    resource_class = SerializationResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'slug')
    ordering = ('-created_at', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name',)
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

    @admin.action(description='Activar serializadoras seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} serializadora(s) activada(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar serializadoras seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} serializadora(s) desactivada(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar animes seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} anime(s) activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar animes seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} anime(s) desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar mangas seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} manga(s) activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar mangas seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} manga(s) desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar títulos de anime seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} título(s) de anime activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar títulos de anime seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} título(s) de anime desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar títulos de manga seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} título(s) de manga activado(s).", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar títulos de manga seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} título(s) de manga desactivado(s).", messages.SUCCESS if actualizados else messages.WARNING)

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

    @admin.action(description='Activar personajes seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje para activar.", messages.WARNING)

    @admin.action(description='Desactivar personajes seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje para desactivar.", messages.WARNING)

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

    @admin.action(description='Activar apodos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} apodo(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún apodo para activar.", messages.WARNING)

    @admin.action(description='Desactivar apodos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} apodo(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún apodo para desactivar.", messages.WARNING)

########################################################################################################    Admin para OtakuPerson
@admin.register(OtakuPerson)
class OtakuPersonAdmin(ImportExportModelAdmin):
    resource_class = OtakuPersonResource  # Si usas django-import-export

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

    inlines = [OtakuPersonNicknameInline, OtakuPersonImageInline, OtakuPersonImageExtraInline,]

    @admin.action(description='Activar personas seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} persona(s) activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna persona para activar.", messages.WARNING)

    @admin.action(description='Desactivar personas seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} persona(s) desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna persona para desactivar.", messages.WARNING)

########################################################################################################    Admin para OtakuPersonNickname
@admin.register(OtakuPersonNickname)
class OtakuPersonNicknameAdmin(ImportExportModelAdmin):
    resource_class = OtakuPersonNicknameResource  # Si usas django-import-export

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

    @admin.action(description='Activar apodos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} apodo(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún apodo para activar.", messages.WARNING)

    @admin.action(description='Desactivar apodos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} apodo(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún apodo para desactivar.", messages.WARNING)

########################################################################################################    Admin para AnimeSong
@admin.register(AnimeSong)
class AnimeSongAdmin(ImportExportModelAdmin):
    resource_class = AnimeSongResource  # Si estás utilizando django-import-export

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

    @admin.action(description='Activar canciones seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} canción(es) activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna canción para activar.", messages.WARNING)

    @admin.action(description='Desactivar canciones seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} canción(es) desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna canción para desactivar.", messages.WARNING)

########################################################################################################    Admin para AnimeCharacter
@admin.register(AnimeCharacter)
class AnimeCharacterAdmin(ImportExportModelAdmin):
    resource_class = AnimeCharacterResource  # Si estás utilizando django-import-export

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

    @admin.action(description='Activar personajes en anime seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje en anime para activar.", messages.WARNING)

    @admin.action(description='Desactivar personajes en anime seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje en anime para desactivar.", messages.WARNING)

########################################################################################################    Admin para MangaCharacter
@admin.register(MangaCharacter)
class MangaCharacterAdmin(ImportExportModelAdmin):
    resource_class = MangaCharacterResource  # Si estás utilizando django-import-export

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

    @admin.action(description='Activar personajes en manga seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje en manga para activar.", messages.WARNING)

    @admin.action(description='Desactivar personajes en manga seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje en manga para desactivar.", messages.WARNING)

########################################################################################################    Admin para VoiceCharacter
@admin.register(VoiceCharacter)
class VoiceCharacterAdmin(ImportExportModelAdmin):
    resource_class = VoiceCharacterResource  # Si estás utilizando django-import-export

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

    @admin.action(description='Activar actores de voz seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} actor(es) de voz activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún actor de voz para activar.", messages.WARNING)

    @admin.action(description='Desactivar actores de voz seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} actor(es) de voz desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún actor de voz para desactivar.", messages.WARNING)

########################################################################################################    Admin para AnimeStaff
@admin.register(AnimeStaff)
class AnimeStaffAdmin(ImportExportModelAdmin):
    resource_class = AnimeStaffResource  # Si estás utilizando django-import-export

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

    @admin.action(description='Activar staff de anime seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} miembro(s) de staff activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún miembro de staff para activar.", messages.WARNING)

    @admin.action(description='Desactivar staff de anime seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} miembro(s) de staff desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún miembro de staff para desactivar.", messages.WARNING)

########################################################################################################    Admin para AuthorManga
@admin.register(AuthorManga)
class AuthorMangaAdmin(ImportExportModelAdmin):
    resource_class = AuthorMangaResource  # Si estás utilizando django-import-export

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

    @admin.action(description='Activar autores de manga seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} autor(es) de manga activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún autor de manga para activar.", messages.WARNING)

    @admin.action(description='Desactivar autores de manga seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} autor(es) de manga desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún autor de manga para desactivar.", messages.WARNING)

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
        ('Relación de Media', {
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

    @admin.action(description='✅ Activar relaciones seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} relación(es) activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "⚠️ No se activó ninguna relación.", messages.WARNING)

    @admin.action(description='❌ Desactivar relaciones seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"❌ {actualizados} relación(es) desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "⚠️ No se desactivó ninguna relación.", messages.WARNING)

    actions = ['activar', 'desactivar']

########################################################################################################    Admin para AnimeImage
@admin.register(AnimeImage)
class AnimeImageAdmin(ImportExportModelAdmin):
    resource_class = AnimeImageResource  # Si estás utilizando django-import-export

    list_display = ('anime', 'size_image', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime', 'size_image')
    search_fields = ('anime__title', 'name', 'slug', 'image_url')
    ordering = ('anime', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('anime', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes de anime seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de anime activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de anime para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de anime seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de anime desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de anime para desactivar.", messages.WARNING)

########################################################################################################    Admin para AnimeImageExtra
@admin.register(AnimeImageExtra)
class AnimeImageExtraAdmin(ImportExportModelAdmin):
    resource_class = AnimeImageExtraResource  # Si estás utilizando django-import-export

    list_display = ('anime', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'anime')
    search_fields = ('anime__title', 'name', 'slug')
    ordering = ('anime', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('anime',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra de anime seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de anime activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de anime para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de anime seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de anime desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de anime para desactivar.", messages.WARNING)

########################################################################################################    Admin para MangaImage
@admin.register(MangaImage)
class MangaImageAdmin(ImportExportModelAdmin):
    resource_class = MangaImageResource  # Si estás utilizando django-import-export

    list_display = ('manga', 'size_image', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'manga', 'size_image')
    search_fields = ('manga__title', 'name', 'slug', 'image_url')
    ordering = ('manga', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('manga', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes de manga seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de manga activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de manga para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de manga seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de manga desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de manga para desactivar.", messages.WARNING)

########################################################################################################    Admin para MangaImageExtra
@admin.register(MangaImageExtra)
class MangaImageExtraAdmin(ImportExportModelAdmin):
    resource_class = MangaImageExtraResource  # Si estás utilizando django-import-export

    list_display = ('manga', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'manga')
    search_fields = ('manga__title', 'name', 'slug')
    ordering = ('manga', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('manga',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra de manga seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de manga activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de manga para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de manga seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de manga desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de manga para desactivar.", messages.WARNING)

########################################################################################################    Admin para OtakuPersonImage
@admin.register(OtakuPersonImage)
class OtakuPersonImageAdmin(ImportExportModelAdmin):
    resource_class = OtakuPersonImageResource  # Si estás utilizando django-import-export

    list_display = ('person', 'size_image', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'person', 'size_image')
    search_fields = ('person__name', 'name', 'slug', 'image_url')
    ordering = ('person', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes de persona seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de persona activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de persona para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de persona seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de persona desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de persona para desactivar.", messages.WARNING)

########################################################################################################    Admin para OtakuPersonImageExtra
@admin.register(OtakuPersonImageExtra)
class OtakuPersonImageExtraAdmin(ImportExportModelAdmin):
    resource_class = OtakuPersonImageExtraResource  # Si estás utilizando django-import-export

    list_display = ('person', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'person')
    search_fields = ('person__name', 'name', 'slug')
    ordering = ('person', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('person',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra de persona seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de persona activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de persona para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de persona seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de persona desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de persona para desactivar.", messages.WARNING)

########################################################################################################    Admin para CharacterImage
@admin.register(CharacterImage)
class CharacterImageAdmin(ImportExportModelAdmin):
    resource_class = CharacterImageResource  # Si estás utilizando django-import-export

    list_display = ('character', 'size_image', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'character', 'size_image')
    search_fields = ('character__name', 'name', 'slug', 'image_url')
    ordering = ('character', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character', 'size_image', 'image', 'image_url',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes de personaje seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de personaje activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de personaje para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de personaje seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de personaje desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de personaje para desactivar.", messages.WARNING)

########################################################################################################    Admin para CharacterImageExtra
@admin.register(CharacterImageExtra)
class CharacterImageExtraAdmin(ImportExportModelAdmin):
    resource_class = CharacterImageExtraResource

    list_display = ('character', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'character')
    search_fields = ('character__name', 'name', 'slug')
    ordering = ('character', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('character',  'image',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'classes': ('collapse',),
            'fields': ('name', 'slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra de personaje seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de personaje activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de personaje para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de personaje seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de personaje desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de personaje para desactivar.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} anime(s) marcado(s) como procesados.", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún anime para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} anime(s) marcado(s) como no procesados.", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún anime para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) de anime(s) marcado(s) como procesados.", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje de anime para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) de anime(s) marcado(s) como no procesados.", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje de anime para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de anime marcada(s) como procesadas.", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de anime para marcar como procesada.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de anime marcada(s) como no procesadas.", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de anime para marcar como no procesada.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} staff(s) de anime(s) marcado(s) como procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún staff de anime para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} staff(s) de anime(s) marcado(s) como no procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún staff de anime para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} manga(s) marcado(s) como procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún manga para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} manga(s) marcado(s) como no procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún manga para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personajes de manga(s) marcado(s) como procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje de manga para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personajes de manga(s) marcado(s) como no procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje de manga para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imágenes de manga(s) marcado(s) como procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de manga para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imágenes de manga(s) marcado(s) como no procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de manga para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) de manga(s) marcado(s) como procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje de manga para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} personaje(s) de manga(s) marcado(s) como no procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún personaje de manga para marcar como no procesado.", messages.WARNING)

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de personaje(s) de manga(s) marcado(s) como procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de personaje de manga para marcar como procesado.", messages.WARNING)

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de personaje(s) de manga(s) marcado(s) como no procesado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de personaje de manga para marcar como no procesado.", messages.WARNING)

########################################################################################################    Admin para DataOtakuPerson
@admin.register(DataOtakuPerson)
class DataOtakuPersonAdmin(admin.ModelAdmin):
    resource_class = DataOtakuPersonResource

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        self._notificar(request, actualizados, 'persona(s)')

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        self._notificar(request, actualizados, 'persona(s)', procesado=False)

    def _notificar(self, request, total, objeto, procesado=True):
        if total:
            estado = "procesado(s)" if procesado else "no procesado(s)"
            self.message_user(request, f"✅ {total} {objeto} marcado(s) como {estado}.", messages.SUCCESS)
        else:
            self.message_user(request, f"⚠️ No se seleccionó ninguna {objeto} para actualizar.", messages.WARNING)

########################################################################################################    Admin para DataOtakuPersonPictures
@admin.register(DataOtakuPersonPictures)
class DataOtakuPersonPicturesAdmin(admin.ModelAdmin):
    resource_class = DataOtakuPersonPicturesResource

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

    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        self._notificar(request, actualizados, 'imagen(es) de persona')

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        self._notificar(request, actualizados, 'imagen(es) de persona', procesado=False)

    def _notificar(self, request, total, objeto, procesado=True):
        if total:
            estado = "procesado(s)" if procesado else "no procesado(s)"
            self.message_user(request, f"✅ {total} {objeto} marcado(s) como {estado}.", messages.SUCCESS)
        else:
            self.message_user(request, f"⚠️ No se seleccionó ninguna {objeto} para actualizar.", messages.WARNING)

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


    @admin.action(description='Marcar como procesado')
    def marcar_como_procesado(self, request, queryset):
        actualizados = queryset.update(processed=True)
        self._notificar(request, actualizados, 'URL(s) de imagen')

    @admin.action(description='Marcar como no procesado')
    def marcar_como_no_procesado(self, request, queryset):
        actualizados = queryset.update(processed=False)
        self._notificar(request, actualizados, 'URL(s) de imagen', procesado=False)

    def _notificar(self, request, total, objeto, procesado=True):
        if total:
            estado = "procesado(s)" if procesado else "no procesado(s)"
            self.message_user(request, f"✅ {total} {objeto} marcado(s) como {estado}.", messages.SUCCESS)
        else:
            self.message_user(request, f"⚠️ No se seleccionó ninguna {objeto} para actualizar.", messages.WARNING)

########################################################################################################    Admin para Temp_OtakuPersons
@admin.register(Temp_OtakuPersons)
class TempOtakuPersonsAdmin(ImportExportModelAdmin):
    resource_class = Temp_OtakuPersonsResource

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

    @admin.action(description='🧹 Eliminar duplicados')
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

    @admin.action(description='🗑️ Eliminar personajes seleccionados')
    def eliminar_seleccionados(self, request, queryset):
        cantidad = queryset.count()
        queryset.delete()
        self.message_user(request, f"✅ {cantidad} personaje(s) eliminado(s).", messages.SUCCESS)
