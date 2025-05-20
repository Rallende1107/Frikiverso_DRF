from django.contrib import admin
# impot Modelos
from apps.movie.models import (TitleMovie, MovieImage, MovieImageExtra, MovieStaff, MovieCast)
# impot Resource
########################################################################################################    Inline Person
class TitleMovieInline(admin.TabularInline):
    model = TitleMovie
    extra = 1
    fields = ('title_lang', 'title', 'slug', 'initial', 'is_active')
    readonly_fields = ('slug', 'initial')
    autocomplete_fields = ('title_lang',)
    show_change_link = True


class MovieImageInline(admin.TabularInline):
    model = MovieImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    autocomplete_fields = ('size_image',)
    readonly_fields = ('created_at', 'updated_at')
    show_change_link = True

class MovieImageExtraInline(admin.TabularInline):
    model = MovieImageExtra
    extra = 1
    fields = ('image', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    show_change_link = True

class MovieStaffInline(admin.TabularInline):
    model = MovieStaff
    extra = 1
    autocomplete_fields = ['person', 'role']
    fields = ['person', 'role', 'is_active']
    ordering = ['role', 'person']
    verbose_name = 'Personal'
    verbose_name_plural = 'Personal'

class MovieCastInline(admin.TabularInline):
    model = MovieCast
    extra = 1
    autocomplete_fields = ['actor', 'role']
    fields = ['actor', 'role', 'character_name', 'is_active']
    ordering = ['actor', 'character_name']
    verbose_name = 'Reparto'
    verbose_name_plural = 'Reparto'
