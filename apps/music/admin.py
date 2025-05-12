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
        ('Información Básica', {
            'fields': ('parent', 'name', 'name_esp', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug', 'initial',)
        }),
        ('Fechas', {
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
        ('Información Básica', {
            'fields': ('name', 'name_esp')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug', 'initial',)
        }),
        ('Fechas', {
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
        ('Información Básica', {
            'fields': ('name', 'name_esp', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar tipos de álbum seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tipo(s) de álbum activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tipo de álbum para activar.", messages.WARNING)

    @admin.action(description='Desactivar tipos de álbum seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tipo(s) de álbum desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tipo de álbum para desactivar.", messages.WARNING)

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
        ('Información Básica', {
            'fields': ('name', 'name_esp', 'description')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar tipos de artistas seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tipo(s) de artista activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tipo de artista para activar.", messages.WARNING)

    @admin.action(description='Desactivar tipos de artistas seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tipo(s) de artista desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tipo de artista para desactivar.", messages.WARNING)

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
        ('Información Básica', {
            'fields': ('name', 'biography', 'start_year', 'year_end', 'artist_type', 'genre')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug', 'initial',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar artistas seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} artista(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún artista para activar.", messages.WARNING)

    @admin.action(description='Desactivar artistas seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} artista(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún artista para desactivar.", messages.WARNING)

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
        ('Información de Asociación', {
            'fields': ('artist', 'person', 'role')
        }),
        ('Fechas de Participación', {
            'fields': ('join_date', 'leave_date')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Fechas del Sistema', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar miembros seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} miembro(s) activado(s)." if actualizados else "No se seleccionó ningún miembro para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar miembros seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} miembro(s) desactivado(s)." if actualizados else "No se seleccionó ningún miembro para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)

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
        ('Información Básica', {
            'fields': ('title', 'artist', 'album_type', 'release_date')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug', 'initial')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar álbumes seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} álbum(es) activado(s)." if actualizados else "No se seleccionó ningún álbum para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar álbumes seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} álbum(es) desactivado(s)." if actualizados else "No se seleccionó ningún álbum para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)

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
        ('Información Básica', {
            'fields': ('title', 'album', 'album_song_id', 'release_date', 'audio_file', 'lyrics')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug', 'initial')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar canciones seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} canción(es) activada(s)." if actualizados else "No se seleccionó ninguna canción para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar canciones seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} canción(es) desactivada(s)." if actualizados else "No se seleccionó ninguna canción para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para AlbumImage
@admin.register(AlbumImage)
class AlbumImageAdmin(ImportExportModelAdmin):
    resource_class = AlbumImageResource

    list_display = ('album', 'size_image', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'size_image', 'album')
    search_fields = ('name', 'slug', 'album__title')
    ordering = ('album', 'size_image', 'name')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        ('Información de Imagen', {
            'fields': ('album', 'size_image', 'image', 'image_url')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('name', 'slug')
        }),
        ('Fechas del Sistema', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} imagen(es) activada(s)." if actualizados else "No se seleccionó ninguna imagen para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar imágenes seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} imagen(es) desactivada(s)." if actualizados else "No se seleccionó ninguna imagen para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para AlbumImageExtra
@admin.register(AlbumImageExtra)
class AlbumImageExtraAdmin(ImportExportModelAdmin):
    resource_class = AlbumImageExtraResource

    list_display = ('album', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'album')
    search_fields = ('name', 'slug', 'album__title')
    ordering = ('album', 'name')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        ('Información de Imagen Extra', {
            'fields': ('album', 'image')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('name', 'slug')
        }),
        ('Fechas del Sistema', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} imagen(es) activada(s)." if actualizados else "No se seleccionó ninguna imagen para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar imágenes extra seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} imagen(es) desactivada(s)." if actualizados else "No se seleccionó ninguna imagen para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para ArtistImage
@admin.register(ArtistImage)
class ArtistImageAdmin(ImportExportModelAdmin):
    resource_class = ArtistImageResource

    list_display = ('artist', 'size_image', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'size_image', 'artist')
    search_fields = ('name', 'slug', 'artist__name')
    ordering = ('artist', 'size_image', 'name')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        ('Información de Imagen', {
            'fields': ('artist', 'size_image', 'image', 'image_url')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('name', 'slug')
        }),
        ('Fechas del Sistema', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} imagen(es) activada(s)." if actualizados else "No se seleccionó ninguna imagen para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar imágenes seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} imagen(es) desactivada(s)." if actualizados else "No se seleccionó ninguna imagen para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)

########################################################################################################    Admin para ArtistImageExtra
@admin.register(ArtistImageExtra)
class ArtistImageExtraAdmin(ImportExportModelAdmin):
    resource_class = ArtistImageExtraResource

    list_display = ('artist', 'name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'artist')
    search_fields = ('name', 'slug', 'artist__name')
    ordering = ('artist', 'name')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        ('Información de Imagen Extra', {
            'fields': ('artist', 'image')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('name', 'slug')
        }),
        ('Fechas del Sistema', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} imagen(es) activada(s)." if actualizados else "No se seleccionó ninguna imagen para activar.", messages.SUCCESS if actualizados else messages.WARNING)

    @admin.action(description='Desactivar imágenes extra seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} imagen(es) desactivada(s)." if actualizados else "No se seleccionó ninguna imagen para desactivar.", messages.SUCCESS if actualizados else messages.WARNING)