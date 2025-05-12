from django.contrib import admin
# impot Modelos
from apps.music.models import (AlbumImage, AlbumImageExtra, ArtistImage, ArtistImageExtra)
# impot Resource
########################################################################################################    Inline Person
class AlbumImageInline(admin.TabularInline):
    model = AlbumImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')
    autocomplete_fields = ('size_image',)
    show_change_link = True

class AlbumImageExtraInline(admin.TabularInline):
    model = AlbumImageExtra
    extra = 1
    fields = ('image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')
    show_change_link = True

class ArtistImageInline(admin.TabularInline):
    model = ArtistImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')
    autocomplete_fields = ('size_image',)
    show_change_link = True

class ArtistImageExtraInline(admin.TabularInline):
    model = ArtistImageExtra
    extra = 1
    fields = ('image', 'name', 'slug', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('name', 'slug', 'created_at', 'updated_at')
    show_change_link = True
