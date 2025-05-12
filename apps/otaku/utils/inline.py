from django.contrib import admin
# impot Modelos
from apps.otaku.models import (TitleManga, TitleAnime, CharacterNickname, OtakuPersonNickname,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra,
    OtakuPersonImage, OtakuPersonImageExtra, CharacterImage, CharacterImageExtra,
                               )
# impot Resource
########################################################################################################    Inline Person
class TitleMangaInline(admin.TabularInline):
    model = TitleManga
    extra = 0
    fields = ('title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'initial', 'created_at', 'updated_at')
    autocomplete_fields = ('title_lang',)
    show_change_link = True

class TitleAnimeInline(admin.TabularInline):
    model = TitleAnime
    extra = 0
    fields = ('title_lang', 'title', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'initial', 'created_at', 'updated_at')
    autocomplete_fields = ('title_lang',)
    show_change_link = True

class CharacterNicknameInline(admin.TabularInline):
    model = CharacterNickname
    extra = 0
    fields = ('nickname', 'slug', 'initial', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'initial', 'created_at', 'updated_at')
    show_change_link = True

class OtakuPersonNicknameInline(admin.TabularInline):
    model = OtakuPersonNickname
    extra = 1  # Muestra 1 formulario vacío por defecto
    fields = ('nickname', 'is_active')  # Campos que se mostrarán en el inline
    readonly_fields = ('slug', 'initial')  # Campos solo lectura
    show_change_link = True  # Permite ver el detalle del apodo

class AnimeImageInline(admin.TabularInline):
    model = AnimeImage
    extra = 1  # Número de formularios vacíos que se mostrarán por defecto.
    fk_name = 'anime'  # Nombre del campo de relación
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class AnimeImageExtraInline(admin.TabularInline):
    model = AnimeImageExtra
    extra = 1
    fk_name = 'anime'
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class MangaImageInline(admin.TabularInline):
    model = MangaImage
    extra = 1
    fk_name = 'manga'
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class MangaImageExtraInline(admin.TabularInline):
    model = MangaImageExtra
    extra = 1
    fk_name = 'manga'
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class OtakuPersonImageInline(admin.TabularInline):
    model = OtakuPersonImage
    extra = 1
    fk_name = 'person'
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class OtakuPersonImageExtraInline(admin.TabularInline):
    model = OtakuPersonImageExtra
    extra = 1
    fk_name = 'person'
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class CharacterImageInline(admin.TabularInline):
    model = CharacterImage
    extra = 1
    fk_name = 'character'
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')

class CharacterImageExtraInline(admin.TabularInline):
    model = CharacterImageExtra
    extra = 1
    fk_name = 'character'
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('name', 'slug')
