from django.contrib import admin
from apps.renpy.models import (
    DeveloperLink, TranslatorLink, PublisherLink,
    GameImage, GameImageExtra, DeveloperImage, DeveloperImageExtra, TranslatorImage, TranslatorImageExtra, PublisherImage, PublisherImageExtra,
    TitleGame
)

class DeveloperLinkInline(admin.TabularInline):
    model = DeveloperLink
    extra = 1
    fields = ('name', 'url', 'is_active')
    readonly_fields = ('slug', 'initial')

class TranslatorLinkInline(admin.TabularInline):
    model = TranslatorLink
    extra = 1
    fields = ('name', 'url', 'is_active')
    readonly_fields = ('slug', 'initial')

class PublisherLinkInline(admin.TabularInline):
    model = PublisherLink
    extra = 1
    fields = ('name', 'url', 'is_active')
    readonly_fields = ('slug', 'initial')

class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class GameImageExtraInline(admin.TabularInline):
    model = GameImageExtra
    extra = 1
    fields = ('image', 'is_active')
    show_change_link = True

class DeveloperImageInline(admin.TabularInline):
    model = DeveloperImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class DeveloperImageExtraInline(admin.TabularInline):
    model = DeveloperImageExtra
    extra = 1
    fields = ('image', 'is_active')
    show_change_link = True

class TranslatorImageInline(admin.TabularInline):
    model = TranslatorImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class TranslatorImageExtraInline(admin.TabularInline):
    model = TranslatorImageExtra
    extra = 1
    fields = ('image', 'is_active')
    show_change_link = True

class PublisherImageInline(admin.TabularInline):
    model = PublisherImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class PublisherImageExtraInline(admin.TabularInline):
    model = PublisherImageExtra
    extra = 1
    fields = ('image', 'is_active')
    show_change_link = True

class TitleGameInline(admin.TabularInline):
    model = TitleGame
    extra = 1
    readonly_fields = ('slug', 'initial')
    fields = ('game', 'language', 'title', 'slug', 'initial', 'is_active')
    show_change_link = True
