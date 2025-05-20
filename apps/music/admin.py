from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (Genre, Role, AlbumType, ArtistType, Artist, ArtistMember, Album, Song, AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra)
# impot Resource
from .resources import (GenreResource, RoleResource, AlbumTypeResource, ArtistTypeResource, ArtistResource, ArtistMemberResource, AlbumResource, SongResource, AlbumImageResource, AlbumImageExtraResource, ArtistImageResource, ArtistImageExtraResource)
# impot Inline
from apps.music.utils.inline import (AlbumImageInline, AlbumImageExtraInline, ArtistImageInline, ArtistImageExtraInline,)
# Register your models here.
########################################################################################################    Admin para Genre
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource

    list_display = ('name', 'name_esp', 'parent', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial', 'parent')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('parent', 'name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
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

########################################################################################################    Admin para Role
@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource

    list_display = ('name', 'name_esp', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'name_esp')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar roles seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d rol(es)).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún rol para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar roles seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d rol(es)).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún rol para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AlbumType
@admin.register(AlbumType)
class AlbumTypeAdmin(ImportExportModelAdmin):
    resource_class = AlbumTypeResource

    list_display = ('name', 'name_esp', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'name')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar tipos de álbumes seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tipo(s) de álbum(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo de álbum para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar tipos de álbumes seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tipo(s) de álbum(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo de álbum para desactivar.'), messages.WARNING)

########################################################################################################    Admin para ArtistType
@admin.register(ArtistType)
class ArtistTypeAdmin(ImportExportModelAdmin):
    resource_class = ArtistTypeResource

    list_display = ('name', 'name_esp', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'name')
    search_fields = ('name', 'name_esp', 'slug')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar tipos de artistas seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tipo(s) de artista(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo de artista para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar tipos de artistas seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tipo(s) de artista(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo de artista para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Artist
@admin.register(Artist)
class ArtistAdmin(ImportExportModelAdmin):
    resource_class = ArtistResource

    list_display = ('name', 'slug', 'initial', 'artist_type', 'is_active', 'created_at')
    list_filter = ('is_active', 'initial', 'artist_type', 'genre')
    search_fields = ('name', 'slug', 'initial')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [ArtistImageInline, ArtistImageExtraInline]

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'biography', 'start_year', 'year_end', 'artist_type', 'genre')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar artistas seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d artista(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún artista para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar artistas seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d artista(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún artista para desactivar.'), messages.WARNING)

########################################################################################################    Admin para ArtistMember
@admin.register(ArtistMember)
class ArtistMemberAdmin(ImportExportModelAdmin):
    resource_class = ArtistMemberResource

    list_display = ('artist', 'person', 'role', 'join_date', 'leave_date', 'is_active', 'created_at')
    list_filter = ('is_active', 'role', 'artist')
    search_fields = ('artist__name', 'person__name', 'role__name')
    ordering = ('artist', 'person', 'role')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica asociación'), {
            'fields': ('artist', 'person', 'role')
        }),
        (_('Fechas de participación'), {
            'fields': ('join_date', 'leave_date')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar miembros seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d miembro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún miembro para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar miembros seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d miembro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún miembro para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Album
@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    resource_class = AlbumResource

    list_display = ('title', 'artist', 'album_type', 'release_date', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'album_type', 'artist', 'initial')
    search_fields = ('title', 'slug', 'artist__name')
    ordering = ('artist', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [AlbumImageInline, AlbumImageExtraInline]

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('title', 'artist', 'album_type', 'release_date')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial'),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar álbumes seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d álbum(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún álbum para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar álbumes seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d álbum(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún álbum para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Song
@admin.register(Song)
class SongAdmin(ImportExportModelAdmin):
    resource_class = SongResource

    list_display = ('title', 'album', 'album_song_id', 'release_date', 'initial', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'album', 'release_date', 'initial')
    search_fields = ('title', 'slug', 'album__title')
    ordering = ('album', 'album_song_id')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('title', 'album', 'album_song_id', 'release_date', 'audio_file', 'lyrics')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial'),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar canciones seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d canción(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún canción para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar canciones seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d canción(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún canción para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AlbumImage
@admin.register(AlbumImage)
class AlbumImageAdmin(ImportExportModelAdmin):
    resource_class = AlbumImageResource

    list_display = ('album', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'size_image', 'album')
    search_fields = ('album__title',)
    ordering = ('album', 'size_image',)
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('album', 'size_image', 'image', 'image_url')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para desactivar.'), messages.WARNING)

########################################################################################################    Admin para AlbumImageExtra
@admin.register(AlbumImageExtra)
class AlbumImageExtraAdmin(ImportExportModelAdmin):
    resource_class = AlbumImageExtraResource

    list_display = ('album', 'is_active', 'created_at')
    list_filter = ('is_active', 'album')
    search_fields = ('album__title',)
    ordering = ('album',)
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('album', 'image')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para desactivar.'), messages.WARNING)

########################################################################################################    Admin para ArtistImage
@admin.register(ArtistImage)
class ArtistImageAdmin(ImportExportModelAdmin):
    resource_class = ArtistImageResource

    list_display = ('artist', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'size_image', 'artist')
    search_fields = ('artist__name',)
    ordering = ('artist', 'size_image')
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('artist', 'size_image', 'image', 'image_url')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para desactivar.'), messages.WARNING)

########################################################################################################    Admin para ArtistImageExtra
@admin.register(ArtistImageExtra)
class ArtistImageExtraAdmin(ImportExportModelAdmin):
    resource_class = ArtistImageExtraResource

    list_display = ('artist', 'is_active', 'created_at')
    list_filter = ('is_active', 'artist')
    search_fields = ('artist__name',)
    ordering = ('artist',)
    readonly_fields = ('created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('artist', 'image')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para desactivar.'), messages.WARNING)