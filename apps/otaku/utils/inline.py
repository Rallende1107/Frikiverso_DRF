from django.contrib import admin
# impot Modelos
from apps.otaku.models import (TitleManga, TitleAnime, CharacterNickname, PersonNickname,
    AnimeImage, AnimeImageExtra, MangaImage, MangaImageExtra,
    PersonImage, PersonImageExtra, CharacterImage, CharacterImageExtra,)
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

class PersonNicknameInline(admin.TabularInline):
    model = PersonNickname
    extra = 1
    fields = ('nickname', 'is_active')
    readonly_fields = ('slug', 'initial')
    show_change_link = True

class AnimeImageInline(admin.TabularInline):
    model = AnimeImage
    extra = 1
    fk_name = 'anime'
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class AnimeImageExtraInline(admin.TabularInline):
    model = AnimeImageExtra
    extra = 1
    fk_name = 'anime'
    fields = ('image', 'is_active')
    show_change_link = True

class MangaImageInline(admin.TabularInline):
    model = MangaImage
    extra = 1
    fk_name = 'manga'
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class MangaImageExtraInline(admin.TabularInline):
    model = MangaImageExtra
    extra = 1
    fk_name = 'manga'
    fields = ('image', 'is_active')
    show_change_link = True

class PersonImageInline(admin.TabularInline):
    model = PersonImage
    extra = 1
    fk_name = 'person'
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class PersonImageExtraInline(admin.TabularInline):
    model = PersonImageExtra
    extra = 1
    fk_name = 'person'
    fields = ('image', 'is_active')
    show_change_link = True

class CharacterImageInline(admin.TabularInline):
    model = CharacterImage
    extra = 1
    fk_name = 'character'
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class CharacterImageExtraInline(admin.TabularInline):
    model = CharacterImageExtra
    extra = 1
    fk_name = 'character'
    fields = ('image', 'is_active')
    show_change_link = True
