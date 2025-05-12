from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, Quality, Website)
# impot Resource
from .resources import (CountryResource, FormatResource, ImageSizeResource, LanguageResource, PersonResource, PersonImageResource, PersonImageExtraResource, QualityResource, WebsiteResource)
# impot Inline
from apps.common.utils.inline import (PersonNicknameInline, PersonImageInline, PersonImageExtraInline)
# Register your models here.
########################################################################################################    Admin para Country
@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

    list_display = ('name', 'name_esp', 'code', 'numeric_code', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'initial', 'initial_esp')
    search_fields = ('name', 'name_esp', 'code', 'numeric_code', )
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial', 'initial_esp', )

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('name', 'name_esp',  'code', 'numeric_code',)
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug', 'initial', 'initial_esp')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar países seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} país(es) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún país para activar.", messages.WARNING)

    @admin.action(description='Desactivar países seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} país(es) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún país para desactivar.", messages.WARNING)

########################################################################################################    Admin para Format
@admin.register(Format)
class FormatAdmin(ImportExportModelAdmin):
    resource_class = FormatResource

    list_display = ('name', 'for_video', 'for_music', 'for_image', 'for_document', 'for_other', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'for_video', 'for_music', 'for_image', 'for_document', 'for_other')
    search_fields = ('name', 'slug', 'description')
    ordering = ('-created_at', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar',]

    fieldsets = (
        ('Información general', {
            'fields': ('name', 'description')
        }),
        ('Usos del formato', {
            'fields': ('for_video', 'for_music', 'for_image', 'for_document', 'for_other')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('slug',)
        }),
        ('Tiempos', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar formatos seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} formato(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún formato para activar.", messages.WARNING)

    @admin.action(description='Desactivar formatos seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} formato(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún formato para desactivar.", messages.WARNING)

########################################################################################################    Admin para ImageSize
@admin.register(ImageSize)
class ImageSizeAdmin(ImportExportModelAdmin):
    resource_class = ImageSizeResource

    list_display = ('name', 'name_esp', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'name_esp')
    ordering = ('name',)
    readonly_fields = ('slug', 'created_at', 'updated_at')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('name', 'name_esp')
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

    @admin.action(description='Activar tamaños de imagen seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tamaño(s) de imagen activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tamaño de imagen para activar.", messages.WARNING)

    @admin.action(description='Desactivar tamaños de imagen seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} tamaño(s) de imagen desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún tamaño de imagen para desactivar.", messages.WARNING)

########################################################################################################    Admin para Language
@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource

    list_display = ('name', 'name_esp', 'acronym', 'initial', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'acronym', 'name_esp')
    ordering = ('-created_at', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('name', 'acronym', 'name_esp',)
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

    @admin.action(description='Activar idiomas seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} idioma(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún idioma para activar.", messages.WARNING)

    @admin.action(description='Desactivar idiomas seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} idioma(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún idioma para desactivar.", messages.WARNING)

########################################################################################################    Admin para Person
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource  # O elimínalo si no usas import-export

    list_display = ('full_name', 'initial', 'country', 'birth_date', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'country')
    search_fields = ('full_name', 'biography')
    ordering = ('initial', 'full_name')
    readonly_fields = ('initial', 'slug', 'created_at', 'updated_at')
    inlines = [PersonNicknameInline, PersonImageInline, PersonImageExtraInline]

    actions = ['activar', 'desactivar']

    fieldsets = (
        ('Datos personales', {
            'fields': ('full_name', 'birth_date', 'country', 'biography')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('initial', 'slug')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar personas seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} persona(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningúna persona para activar.", messages.WARNING)

    @admin.action(description='Desactivar personas seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} persona(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningúna persona para desactivar.", messages.WARNING)

########################################################################################################    Admin para PersonImage
@admin.register(PersonImage)
class PersonImageAdmin(ImportExportModelAdmin):
    resource_class = PersonImageResource  # Asegúrate de tener este resource

    list_display = ('name', 'person', 'size_image', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'size_image')
    search_fields = ('name', 'slug', 'person__full_name')
    ordering = ('-created_at', 'person__full_name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('person', 'size_image', 'image', 'image_url')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('name', 'slug')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(
            request,
            f"✅ {actualizados} imagen(es) activada(s)." if actualizados else "No se seleccionó ninguna imagen para activar.",
            messages.SUCCESS if actualizados else messages.WARNING
        )

    @admin.action(description='Desactivar imágenes seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(
            request,
            f"✅ {actualizados} imagen(es) desactivada(s)." if actualizados else "No se seleccionó ninguna imagen para desactivar.",
            messages.SUCCESS if actualizados else messages.WARNING
        )

########################################################################################################    Admin para PersonImageExtra
@admin.register(PersonImageExtra)
class PersonImageExtraAdmin(ImportExportModelAdmin):
    resource_class = PersonImageExtraResource

    list_display = ('name', 'person', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'slug', 'person__full_name')
    ordering = ('-created_at', 'person__full_name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'name')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('person', 'image')
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Valores generados automáticamente', {
            'fields': ('name', 'slug')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar imágenes extra seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(
            request,
            f"✅ {actualizados} imagen(es) extra activada(s)." if actualizados else "No se seleccionó ninguna imagen extra para activar.",
            messages.SUCCESS if actualizados else messages.WARNING
        )

    @admin.action(description='Desactivar imágenes extra seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(
            request,
            f"✅ {actualizados} imagen(es) extra desactivada(s)." if actualizados else "No se seleccionó ninguna imagen extra para desactivar.",
            messages.SUCCESS if actualizados else messages.WARNING
        )

########################################################################################################    Admin para Quality
@admin.register(Quality)
class QualityAdmin(ImportExportModelAdmin):
    resource_class = QualityResource

    list_display = ('name', 'description', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)
    ordering = ('-created_at', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('name', 'description')
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

    @admin.action(description='Activar calidades seleccionadas')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} calidad(es) activada(s).", messages.SUCCESS)

    @admin.action(description='Desactivar calidades seleccionadas')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} calidad(es) desactivada(s).", messages.SUCCESS)

########################################################################################################    Admin para Website
@admin.register(Website)
class WebsiteAdmin(ImportExportModelAdmin):
    resource_class = WebsiteResource

    list_display = ('name', 'acronym', 'url', 'initial', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'acronym', 'url')
    ordering = ('-created_at', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (None, {
            'fields': ('name', 'acronym', 'url')
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

    @admin.action(description='Activar websites seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        self.message_user(request, f"✅ {actualizados} website(s) activado(s).", messages.SUCCESS)

    @admin.action(description='Desactivar websites seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        self.message_user(request, f"✅ {actualizados} website(s) desactivado(s).", messages.SUCCESS)
