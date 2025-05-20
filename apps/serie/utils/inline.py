from django.contrib import admin
# impot Modelos
from apps.serie.models import (TitleSerie, SerieImage, SerieImageExtra, SerieStaff, SerieCast)
# impot Resource
########################################################################################################    Inline Person
class TitleSerieInline(admin.TabularInline):
    model = TitleSerie
    extra = 1
    fields = ('title_lang', 'title', 'slug', 'initial', 'is_active')
    readonly_fields = ('slug', 'initial')
    autocomplete_fields = ('title_lang',)
    show_change_link = True


class SerieImageInline(admin.TabularInline):
    model = SerieImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    autocomplete_fields = ('size_image',)
    readonly_fields = ('created_at', 'updated_at')
    show_change_link = True

class SerieImageExtraInline(admin.TabularInline):
    model = SerieImageExtra
    extra = 1
    fields = ('image', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    show_change_link = True

class SerieStaffInline(admin.TabularInline):
    model = SerieStaff
    extra = 1
    autocomplete_fields = ['person', 'role']
    fields = ['person', 'role', 'is_active']
    ordering = ['role', 'person']
    verbose_name = 'Personal'
    verbose_name_plural = 'Personal'

class SerieCastInline(admin.TabularInline):
    model = SerieCast
    extra = 1
    autocomplete_fields = ['actor', 'role']
    fields = ['actor', 'role', 'character_name', 'is_active']
    ordering = ['actor', 'character_name']
    verbose_name = 'Reparto'
    verbose_name_plural = 'Reparto'
