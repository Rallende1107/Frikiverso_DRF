from django.contrib import admin
# impot Modelos
from apps.common.models import (PersonImage, PersonImageExtra, PersonNickname)
# impot Resource
########################################################################################################    Inline Person
class PersonNicknameInline(admin.TabularInline):  # Puedes usar StackedInline si prefieres estilo vertical
    model = PersonNickname
    extra = 1
    fields = ('nickname', 'initial', 'slug', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('initial', 'slug', 'created_at', 'updated_at')
    show_change_link = True

class PersonImageInline(admin.TabularInline):
    model = PersonImage
    extra = 1
    fields = ('size_image', 'image', 'image_url', 'is_active')
    show_change_link = True

class PersonImageExtraInline(admin.TabularInline):
    model = PersonImageExtra
    extra = 1
    fields = ('image', 'is_active')
    show_change_link = True
