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
        (_('Información básica'), {
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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar motores de desarrollo seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d motor(es) de desarrollo.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún motor de desarrollo para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar motores de desarrollo seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d motor(es) de desarrollo.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún motor de desarrollo para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar censuras seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d censura(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún censura para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar censuras seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d censura(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún censura para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar prefijos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d prefijo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún prefijo para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar prefijos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d prefijo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún prefijo para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar plataformas seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d plataforma(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún plataforma para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar plataformas seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d plataforma(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún plataforma para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar desarrolladores seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d desarrollador(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún desarrollador para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar desarrolladores seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d desarrollador(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún desarrollador para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar traductores seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d traductor(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún traductor para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar traductores seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d traductor(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún traductor para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar editores seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d editor(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún editor para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar editores seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d editor(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún editor para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar juegos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d juego(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún juego para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar juegos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d juego(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún juego para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar enlaces de desarrollador seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d enlace(s) de desarrollador.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún enlace de desarrollador para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar enlaces de desarrollador seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d enlace(s) de desarrollador.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún enlace de desarrollador para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar enlaces de traductor seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d enlace(s) de traductor.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún enlace de traductor para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar enlaces de traductor seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d enlace(s) de traductor.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún enlace de traductor para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar enlaces de editor seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d enlace(s) de editor.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún enlace de editor para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar enlaces de editor seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d enlace(s) de editor.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún enlace de editor para desactivar.'), messages.WARNING)

########################################################################################################    Admin para GameImage
@admin.register(GameImage)
class GameImageAdmin(ImportExportModelAdmin):
    resource_class = GameImageResource

    list_display = ('game', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'game', 'size_image')
    search_fields = ('game__title',)
    ordering = ('game', 'size_image',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('game', 'size_image', 'image', 'image_url',)
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
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

########################################################################################################    Admin para GameImageExtra
@admin.register(GameImageExtra)
class GameImageExtraAdmin(ImportExportModelAdmin):
    resource_class = GameImageExtraResource

    list_display = ('game', 'is_active', 'created_at')
    list_filter = ('is_active', 'game')
    search_fields = ('game__title',)
    ordering = ('game',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('game', 'image',)
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
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

########################################################################################################    Admin para DeveloperImage
@admin.register(DeveloperImage)
class DeveloperImageAdmin(ImportExportModelAdmin):
    resource_class = DeveloperImageResource

    list_display = ('developer', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'developer', 'size_image')
    search_fields = ('developer__name',)
    ordering = ('developer', 'size_image',)
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('developer', 'size_image', 'image', 'image_url', 'name')
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
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
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

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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

    @admin.action(description=_('Activar títulos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} título(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún título para activar.", messages.WARNING)

    @admin.action(description=_('Desactivar títulos seleccionados'))
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

    @admin.action(description=_('Activar estados de obtención seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(status=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} estado(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún estado para activar.", messages.WARNING)

    @admin.action(description=_('Desactivar estados de obtención seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(status=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} estado(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún estado para desactivar.", messages.WARNING)
