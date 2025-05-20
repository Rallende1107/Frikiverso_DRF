# Django imports
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
        (_('Información básica'), {
            'fields': ('name', 'name_esp',  'code', 'numeric_code',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial', 'initial_esp'),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar países seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('%(count)d país(es) activado(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún país para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar países seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('%(count)d país(es) desactivado(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún país para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
            'fields': ('name', 'description')
        }),
        (_('Usos del formato'), {
            'fields': ('for_video', 'for_music', 'for_image', 'for_document', 'for_other')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar formatos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(
                request, _('Se activaron %(count)d formato(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(
                request, _('No se seleccionó ningún formato para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar formatos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d formato(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún formato para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
            'fields': ('name', 'name_esp')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar tamaños de imagen seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tamaño(s) de imagen.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tamaño de imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar tamaños de imagen seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tamaño(s) de imagen.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tamaño de imagen para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
            'fields': ('name', 'acronym', 'name_esp',)
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial'),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar idiomas seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d idioma(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún idioma para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar idiomas seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d idioma(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún idioma para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
            'fields': ('full_name', 'birth_date', 'country', 'biography')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('initial', 'slug'),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar personas seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d persona(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna persona para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar personas seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d persona(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna persona para desactivar.'), messages.WARNING)

########################################################################################################    Admin para PersonImage
@admin.register(PersonImage)
class PersonImageAdmin(ImportExportModelAdmin):
    resource_class = PersonImageResource  # Asegúrate de tener este resource

    list_display = ('person', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'size_image')
    search_fields = ('person__full_name',)
    ordering = ('-created_at', 'person__full_name')
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('person', 'size_image', 'image', 'image_url')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen para desactivar.'), messages.WARNING)

########################################################################################################    Admin para PersonImageExtra
@admin.register(PersonImageExtra)
class PersonImageExtraAdmin(ImportExportModelAdmin):
    resource_class = PersonImageExtraResource

    list_display = ('person', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('person__full_name',)
    ordering = ('-created_at', 'person__full_name')
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('person', 'image')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar imágenes seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar imágenes seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d imagen(es) extra.') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna imagen extra para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
            'fields': ('name', 'description')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    # Calidades
    @admin.action(description=_('Activar calidades seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d calidad(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna calidad para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar calidades seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d calidad(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna calidad para desactivar.'), messages.WARNING)

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
        (_('Información básica'), {
            'fields': ('name', 'acronym', 'url')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores generados automáticamente'), {
            'fields': ('slug', 'initial'),
            'classes': ('collapse',),
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # Websites
    @admin.action(description=_('Activar websites seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d website(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún website para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar websites seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d website(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún website para desactivar.'), messages.WARNING)