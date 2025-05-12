from django.contrib import admin
from apps.renpy.models import (
    DeveloperLink, TranslatorLink, PublisherLink,
    GameImage, GameImageExtra,
    DeveloperImage, DeveloperImageExtra,
    TranslatorImage, TranslatorImageExtra,
    PublisherImage, PublisherImageExtra,
    TitleGame
)
# Inline para DeveloperLink
class DeveloperLinkInline(admin.TabularInline):
    model = DeveloperLink
    extra = 1
    fields = ('name', 'url', 'is_active')
    readonly_fields = ('slug', 'initial')

# Inline para TranslatorLink
class TranslatorLinkInline(admin.TabularInline):
    model = TranslatorLink
    extra = 1
    fields = ('name', 'url', 'is_active')
    readonly_fields = ('slug', 'initial')

# Inline para PublisherLink
class PublisherLinkInline(admin.TabularInline):
    model = PublisherLink
    extra = 1
    fields = ('name', 'url', 'is_active')
    readonly_fields = ('slug', 'initial')

# Inline para GameImage
class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True


# Inline para GameImageExtra
class GameImageExtraInline(admin.TabularInline):
    model = GameImageExtra
    extra = 1
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True


# Inline para DeveloperImage
class DeveloperImageInline(admin.TabularInline):
    model = DeveloperImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True


# Inline para DeveloperImageExtra
class DeveloperImageExtraInline(admin.TabularInline):
    model = DeveloperImageExtra
    extra = 1
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True


# Inline para TranslatorImage
class TranslatorImageInline(admin.TabularInline):
    model = TranslatorImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True


# Inline para TranslatorImageExtra
class TranslatorImageExtraInline(admin.TabularInline):
    model = TranslatorImageExtra
    extra = 1
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True


# Inline para PublisherImage
class PublisherImageInline(admin.TabularInline):
    model = PublisherImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True

# Inline para PublisherImageExtra
class PublisherImageExtraInline(admin.TabularInline):
    model = PublisherImageExtra
    extra = 1
    fields = ('image', 'name', 'slug', 'is_active')
    readonly_fields = ('slug',)
    show_change_link = True

class TitleGameInline(admin.TabularInline):  # También puedes usar `StackedInline` si prefieres un diseño más detallado
    model = TitleGame
    extra = 1  # Esto controla cuántos formularios vacíos se muestran por defecto.
    readonly_fields = ('slug', 'initial')  # Hacer estos campos de solo lectura
    fields = ('game', 'language', 'title', 'slug', 'initial', 'is_active')  # Los campos a mostrar
    show_change_link = True  # Permite un enlace rápido para editar el título
