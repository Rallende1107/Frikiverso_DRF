from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (
    Genre, GameEngine, Censorship, Prefix, Status, Platform, Developer, Translator, Publisher, Game,
    TitleGame, DeveloperLink, TranslatorLink, PublisherLink,
    GameImage, GameImageExtra, DeveloperImage, DeveloperImageExtra, TranslatorImage, TranslatorImageExtra, PublisherImage, PublisherImageExtra,
    F95GameFetchStatus,
    )
# impot Resource
from .resources import (
    GenreResource, GameEngineResource, CensorshipResource, PrefixResource, StatusResource, PlatformResource, DeveloperResource, TranslatorResource, PublisherResource, GameResource,
    TitleGameResource, DeveloperLinkResource, TranslatorLinkResource, PublisherLinkResource,
    GameImageResource, GameImageExtraResource, DeveloperImageResource, DeveloperImageExtraResource, TranslatorImageResource, TranslatorImageExtraResource, PublisherImageResource, PublisherImageExtraResource,
    F95GameFetchStatusResource,
    )
# impot Inline
from apps.renpy.utils.inline import (
    DeveloperLinkInline, DeveloperImageInline, DeveloperImageExtraInline,
    TranslatorLinkInline, TranslatorImageInline, TranslatorImageExtraInline,
    PublisherLinkInline, PublisherImageInline, PublisherImageExtraInline,
    GameImageInline, GameImageExtraInline, TitleGameInline
    )
# Register your models here.
########################################################################################################    Admin para Genre
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource

    list_display = ('name', 'name_esp', 'parent', 'explicit', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'explicit', 'parent')
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'name_esp', 'parent', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active', 'explicit')
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

########################################################################################################    Admin para GameEngine
@admin.register(GameEngine)
class GameEngineAdmin(ImportExportModelAdmin):
    resource_class = GameEngineResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('name', 'description')
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

    @admin.action(description='Activar motores de desarrollo seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} motor(es) de desarrollo activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún motor de desarrollo para activar.", messages.WARNING)

    @admin.action(description='Desactivar motores de desarrollo seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} motor(es) de desarrollo desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún motor de desarrollo para desactivar.", messages.WARNING)

########################################################################################################    Admin para Censorship
@admin.register(Censorship)
class CensorshipAdmin(ImportExportModelAdmin):
    resource_class = CensorshipResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
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

    @admin.action(description='Activar censuras seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} censura(s) activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna censura para activar.", messages.WARNING)

    @admin.action(description='Desactivar censuras seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} censura(s) desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna censura para desactivar.", messages.WARNING)

########################################################################################################    Admin para Prefix
@admin.register(Prefix)
class PrefixAdmin(ImportExportModelAdmin):
    resource_class = PrefixResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
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

    @admin.action(description='Activar prefijos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} prefijo(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún prefijo para activar.", messages.WARNING)

    @admin.action(description='Desactivar prefijos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} prefijo(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún prefijo para desactivar.", messages.WARNING)

########################################################################################################    Admin para Status
@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
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
        if actualizados:
            self.message_user(request, f"✅ {actualizados} estado(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún estado para activar.", messages.WARNING)

    @admin.action(description='Desactivar estados seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} estado(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún estado para desactivar.", messages.WARNING)

########################################################################################################    Admin para Platform
@admin.register(Platform)
class PlatformAdmin(ImportExportModelAdmin):
    resource_class = PlatformResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
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

    @admin.action(description='Activar plataformas seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} plataforma(s) activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna plataforma para activar.", messages.WARNING)

    @admin.action(description='Desactivar plataformas seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} plataforma(s) desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna plataforma para desactivar.", messages.WARNING)

########################################################################################################    Admin para Developer
@admin.register(Developer)
class DeveloperAdmin(ImportExportModelAdmin):
    resource_class = DeveloperResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [DeveloperLinkInline, DeveloperImageInline, DeveloperImageExtraInline,]

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

    @admin.action(description='Activar desarrolladores seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} desarrollador(es) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún desarrollador para activar.", messages.WARNING)

    @admin.action(description='Desactivar desarrolladores seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} desarrollador(es) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún desarrollador para desactivar.", messages.WARNING)

########################################################################################################    Admin para Translator
@admin.register(Translator)
class TranslatorAdmin(ImportExportModelAdmin):
    resource_class = TranslatorResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [TranslatorLinkInline, TranslatorImageInline, TranslatorImageExtraInline,]

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

    @admin.action(description='Activar traductores seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} traductor(es) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún traductor para activar.", messages.WARNING)

    @admin.action(description='Desactivar traductores seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} traductor(es) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún traductor para desactivar.", messages.WARNING)

########################################################################################################    Admin para Publisher
@admin.register(Publisher)
class PublisherAdmin(ImportExportModelAdmin):
    resource_class = PublisherResource

    list_display = ('name', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [PublisherLinkInline, PublisherImageInline, PublisherImageExtraInline,]

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

    @admin.action(description='Activar editores seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} editor(es) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún editor para activar.", messages.WARNING)

    @admin.action(description='Desactivar editores seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} editor(es) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún editor para desactivar.", messages.WARNING)

########################################################################################################    Admin para Game
@admin.register(Game)
class GameAdmin(ImportExportModelAdmin):
    resource_class = GameResource

    list_display = ('title', 'version', 'release_date', 'status', 'engine', 'is_active', 'created_at')
    list_filter = ('is_active', 'status', 'engine', 'platforms', 'developers', 'publishers', 'languages', 'genres', 'censored')
    search_fields = ('title', 'slug', 'version', 'fzone_id')
    ordering = ('-created_at', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [TitleGameInline, GameImageInline, GameImageExtraInline]

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('title', 'version', 'synopsis', 'background', 'release_date')
        }),
        (_('Relaciones'), {
            'fields': ('status', 'engine', 'platforms', 'developers', 'publishers', 'languages', 'translators', 'genres', 'censored')
        }),
        (_('F95 Zone'), {
            'fields': ('url_fzone', 'fzone_id')
        }),
        (_('URL'), {
            'fields': ('url_steam',)
        }),
        (_('Estado'), {
            'fields': ('is_active',),
        }),
        (_('Valores generados automáticamente'), {
            'fields': ( 'version_txt', 'slug', 'initial'),
            'classes': ('collapse',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    @admin.action(description='Activar juegos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} juego(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún juego para activar.", messages.WARNING)

    @admin.action(description='Desactivar juegos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} juego(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún juego para desactivar.", messages.WARNING)

########################################################################################################    Admin para DeveloperLink
@admin.register(DeveloperLink)
class DeveloperLinkAdmin(ImportExportModelAdmin):
    resource_class = DeveloperLinkResource

    list_display = ('developer', 'name', 'url', 'is_active', 'created_at')
    list_filter = ('is_active', 'developer')
    search_fields = ('developer__name', 'name', 'url')
    ordering = ('developer', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('developer', 'name', 'url')
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

    @admin.action(description='Activar enlaces de desarrollador seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} enlace(s) de desarrollador activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún enlace de desarrollador para activar.", messages.WARNING)

    @admin.action(description='Desactivar enlaces de desarrollador seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} enlace(s) de desarrollador desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún enlace de desarrollador para desactivar.", messages.WARNING)

########################################################################################################    Admin para TranslatorLink
@admin.register(TranslatorLink)
class TranslatorLinkAdmin(ImportExportModelAdmin):
    resource_class = TranslatorLinkResource

    list_display = ('translator', 'name', 'url', 'is_active', 'created_at')
    list_filter = ('is_active', 'translator')
    search_fields = ('translator__name', 'name', 'url')
    ordering = ('translator', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('translator', 'name', 'url')
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

    @admin.action(description='Activar enlaces de traductor seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} enlace(s) de traductor activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún enlace de traductor para activar.", messages.WARNING)

    @admin.action(description='Desactivar enlaces de traductor seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} enlace(s) de traductor desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún enlace de traductor para desactivar.", messages.WARNING)

########################################################################################################    Admin para PublisherLink
@admin.register(PublisherLink)
class PublisherLinkAdmin(ImportExportModelAdmin):
    resource_class = PublisherLinkResource

    list_display = ('publisher', 'name', 'url', 'is_active', 'created_at')
    list_filter = ('is_active', 'publisher')
    search_fields = ('publisher__name', 'name', 'url')
    ordering = ('publisher', 'initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('publisher', 'name', 'url')
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

    @admin.action(description='Activar enlaces de editor seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} enlace(s) de editor activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún enlace de editor para activar.", messages.WARNING)

    @admin.action(description='Desactivar enlaces de editor seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} enlace(s) de editor desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún enlace de editor para desactivar.", messages.WARNING)

########################################################################################################    Admin para GameImage
@admin.register(GameImage)
class GameImageAdmin(ImportExportModelAdmin):
    resource_class = GameImageResource

    list_display = ('game', 'size_image', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'game', 'size_image')
    search_fields = ('game__name', 'name', 'slug')
    ordering = ('game', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('game', 'size_image', 'image', 'image_url', 'name')
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

    @admin.action(description='Activar imágenes de juegos seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de juego activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de juego para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de juegos seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de juego desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de juego para desactivar.", messages.WARNING)

########################################################################################################    Admin para GameImageExtra
@admin.register(GameImageExtra)
class GameImageExtraAdmin(ImportExportModelAdmin):
    resource_class = GameImageExtraResource

    list_display = ('game', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'game')
    search_fields = ('game__name', 'name', 'slug')
    ordering = ('game', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('game', 'image', 'name')
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

    @admin.action(description='Activar imágenes extra de juegos seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de juego activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de juego para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de juegos seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de juego desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de juego para desactivar.", messages.WARNING)

########################################################################################################    Admin para DeveloperImage
@admin.register(DeveloperImage)
class DeveloperImageAdmin(ImportExportModelAdmin):
    resource_class = DeveloperImageResource

    list_display = ('developer', 'size_image', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'developer', 'size_image')
    search_fields = ('developer__name', 'name', 'slug')
    ordering = ('developer', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('developer', 'size_image', 'image', 'image_url', 'name')
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

    @admin.action(description='Activar imágenes de desarrolladores seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de desarrollador activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de desarrollador para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de desarrolladores seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de desarrollador desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de desarrollador para desactivar.", messages.WARNING)

########################################################################################################    Admin para DeveloperImageExtra
@admin.register(DeveloperImageExtra)
class DeveloperImageExtraAdmin(ImportExportModelAdmin):
    resource_class = DeveloperImageExtraResource

    list_display = ('developer', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'developer')
    search_fields = ('developer__name', 'name', 'slug')
    ordering = ('developer', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('developer', 'image', 'name')
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

    @admin.action(description='Activar imágenes extra de desarrolladores seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de desarrollador activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de desarrollador para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de desarrolladores seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de desarrollador desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de desarrollador para desactivar.", messages.WARNING)

########################################################################################################    Admin para TranslatorImage
@admin.register(TranslatorImage)
class TranslatorImageAdmin(ImportExportModelAdmin):
    resource_class = TranslatorImageResource

    list_display = ('translator', 'size_image', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'translator', 'size_image')
    search_fields = ('translator__name', 'name', 'slug')
    ordering = ('translator', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('translator', 'size_image', 'image', 'image_url', 'name')
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

    @admin.action(description='Activar imágenes de traductores seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de traductor activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de traductor para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de traductores seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de traductor desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de traductor para desactivar.", messages.WARNING)

########################################################################################################    Admin para TranslatorImageExtra
@admin.register(TranslatorImageExtra)
class TranslatorImageExtraAdmin(ImportExportModelAdmin):
    resource_class = TranslatorImageExtraResource

    list_display = ('translator', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'translator')
    search_fields = ('translator__name', 'name', 'slug')
    ordering = ('translator', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('translator', 'image', 'name')
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

    @admin.action(description='Activar imágenes extra de traductores seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de traductor activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de traductor para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de traductores seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de traductor desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de traductor para desactivar.", messages.WARNING)

########################################################################################################    Admin para PublisherImage
@admin.register(PublisherImage)
class PublisherImageAdmin(ImportExportModelAdmin):
    resource_class = PublisherImageResource

    list_display = ('publisher', 'size_image', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'publisher', 'size_image')
    search_fields = ('publisher__name', 'name', 'slug')
    ordering = ('publisher', 'size_image', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('publisher', 'size_image', 'image', 'image_url', 'name')
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

    @admin.action(description='Activar imágenes de editores seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de editor activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de editor para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes de editores seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) de editor desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen de editor para desactivar.", messages.WARNING)

########################################################################################################    Admin para PublisherImageExtra
@admin.register(PublisherImageExtra)
class PublisherImageExtraAdmin(ImportExportModelAdmin):
    resource_class = PublisherImageExtraResource

    list_display = ('publisher', 'name', 'is_active', 'created_at')
    list_filter = ('is_active', 'publisher')
    search_fields = ('publisher__name', 'name', 'slug')
    ordering = ('publisher', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información Básica'), {
            'fields': ('publisher', 'image', 'name')
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

    @admin.action(description='Activar imágenes extra de editores seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de editor activada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de editor para activar.", messages.WARNING)

    @admin.action(description='Desactivar imágenes extra de editores seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} imagen(es) extra de editor desactivada(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ninguna imagen extra de editor para desactivar.", messages.WARNING)

########################################################################################################    Admin para TitleGame
@admin.register(TitleGame)
class TitleGameAdmin(ImportExportModelAdmin):
    resource_class = TitleGameResource  # Si usas la funcionalidad de importación/exportación

    list_display = ('game', 'language', 'title', 'initial', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'game', 'language')
    search_fields = ('game__name', 'title', 'slug')
    ordering = ['language', 'title']
    readonly_fields = ('slug', 'initial', 'created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información del Título'), {
            'fields': ('game', 'language', 'title')
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

    @admin.action(description='Activar títulos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} título(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún título para activar.", messages.WARNING)

    @admin.action(description='Desactivar títulos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} título(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún título para desactivar.", messages.WARNING)

########################################################################################################    Admin para F95GameFetchStatus
@admin.register(F95GameFetchStatus)
class F95GameFetchStatusAdmin(ImportExportModelAdmin):
    resource_class = F95GameFetchStatusResource  # Si usas la funcionalidad de importación/exportación

    list_display = ('f95_id', 'url', 'status', 'processed', 'created_at', 'updated_at')
    list_filter = ('status', 'processed')
    search_fields = ('url', 'f95_id')
    ordering = ['-created_at', 'f95_id']
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información de la Obtención'), {
            'fields': ('f95_id', 'url', 'status', 'data', 'processed')
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar estados de obtención seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(status=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} estado(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún estado para activar.", messages.WARNING)

    @admin.action(description='Desactivar estados de obtención seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(status=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} estado(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún estado para desactivar.", messages.WARNING)
