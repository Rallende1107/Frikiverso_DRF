from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (Genre, Type, Role, Rating, Company, Serie, TitleSerie, SerieStaff, SerieCast, SerieImage, SerieImageExtra)
# impot Resource
from .resources import (GenreResource, TypeResource, RoleResource, RatingResource, CompanyResource, SerieResource, TitleSerieResource, SerieStaffResource, SerieCastResource, SerieImageResource, SerieImageExtraResource)
# impot Inline
from apps.serie.utils.inline import (TitleSerieInline, SerieImageInline, SerieImageExtraInline, SerieStaffInline, SerieCastInline)
# Register your models here.
########################################################################################################    Admin para Country
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource

    list_display = ('name', 'name_esp', 'parent', 'explicit', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'explicit', 'initial', 'parent')
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'name_esp', 'parent', 'description')
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

    @admin.action(description=_('Activar géneros seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d género(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar géneros seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d género(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún género para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Type
@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    resource_class = TypeResource

    list_display = ('name', 'name_esp', 'parent', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'initial', 'parent')
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'name_esp', 'parent', 'description')
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

    @admin.action(description=_('Activar tipos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d tipo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar tipos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d tipo(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún tipo para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Role
@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource

    list_display = ('name', 'name_esp', 'role_staff', 'role_cast', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'role_staff', 'role_cast', 'initial')
    search_fields = ('name', 'name_esp', 'description')
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'name_esp', 'description')
        }),
        (_('Clasificación de rol'), {
            'fields': ('role_staff', 'role_cast')
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

    @admin.action(description=_('Activar roles seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d rol(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún rol para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar roles seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d rol(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún rol para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Rating
@admin.register(Rating)
class RatingAdmin(ImportExportModelAdmin):
    resource_class = RatingResource

    list_display = ('acronym', 'name', 'name_esp', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('acronym', 'name', 'name_esp')
    ordering = ('acronym', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('acronym', 'name', 'name_esp')
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

    @admin.action(description=_('Activar clasificaciones seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d clasificación(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna clasificación para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar clasificaciones seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d clasificación(es).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna clasificación para activar.'), messages.WARNING)

########################################################################################################    Admin para Company
@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource

    list_display = ('name', 'country', 'founded_year', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'initial', 'country')
    search_fields = ('name',)
    ordering = ('initial', 'name')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('name', 'country', 'founded_year')
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

    @admin.action(description=_('Activar compañías seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d compañía(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna compañía para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar compañías seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d compañía(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna compañía para desactivar.'), messages.WARNING)

########################################################################################################    Admin para Serie
@admin.register(Serie)
class SerieAdmin(ImportExportModelAdmin):
    resource_class = SerieResource

    list_display = ('title', 'title_secundary', 'release_year', 'duration_minutes', 'serie_types', 'serie_rating', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'release_year', 'serie_types', 'serie_rating')
    search_fields = ('title', 'title_secundary')
    ordering = ('-created_at', 'title')
    filter_horizontal = ('genres', 'producers', 'distributors')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    inlines = [TitleSerieInline, SerieImageInline, SerieImageExtraInline]
    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('title', 'title_secundary', 'release_year', 'duration_minutes', 'synopsis')
        }),
        ('Clasificación y Géneros', {
            'fields': ('serie_types', 'serie_rating', 'genres')
        }),
        ('Productoras y Distribuidoras', {
            'fields': ('producers', 'distributors')
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

    @admin.action(description=_('Activar series seleccionadas'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d serie(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna serie para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar series seleccionadas'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d serie(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ninguna serie para desactivar.'), messages.WARNING)

########################################################################################################    Admin para TitleSerie
@admin.register(TitleSerie)
class TitleSerieAdmin(ImportExportModelAdmin):
    resource_class = TitleSerieResource

    list_display = ('title', 'title_lang', 'serie', 'is_active', 'slug', 'created_at')
    list_filter = ('is_active', 'title_lang')
    search_fields = ('title', 'serie__title')
    ordering = ('serie', 'title_lang', 'title')
    readonly_fields = ('created_at', 'updated_at', 'slug', 'initial')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('serie', 'title_lang', 'title')
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

    @admin.action(description=_('Activar títulos seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d título(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún título para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar títulos seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d título(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún título para desactivar.'), messages.WARNING)

########################################################################################################    Admin para SerieStaff
@admin.register(SerieStaff)
class SerieStaffAdmin(ImportExportModelAdmin):
    resource_class = SerieStaffResource

    list_display = ('serie', 'person', 'role', 'is_active', 'created_at')
    list_filter = ('is_active', 'role')
    search_fields = ('serie__title', 'person__name', 'role__name')
    ordering = ('serie', 'role', 'person')
    autocomplete_fields = ('serie', 'person', 'role')
    readonly_fields = ('created_at', 'updated_at')
    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('serie', 'person', 'role')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Fechas'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description=_('Activar registros seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún registro para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar registros seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún registro para desactivar.'), messages.WARNING)

########################################################################################################    Admin para SerieCast
@admin.register(SerieCast)
class SerieCastAdmin(ImportExportModelAdmin):
    resource_class = SerieCastResource

    list_display = ('serie', 'actor', 'character_name', 'role', 'is_active', 'created_at')
    list_filter = ('is_active', 'role')
    search_fields = ('serie__title', 'actor__name', 'character_name')
    ordering = ('serie', 'actor', 'character_name')
    autocomplete_fields = ('serie', 'actor', 'role')
    readonly_fields = ('slug', 'initial', 'created_at', 'updated_at')
    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('serie', 'actor', 'role', 'character_name')
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

    @admin.action(description=_('Activar registros seleccionados'))
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, _('Se activaron %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún registro para activar.'), messages.WARNING)

    @admin.action(description=_('Desactivar registros seleccionados'))
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, _('Se desactivaron %(count)d registro(s).') % {'count': actualizados}, messages.SUCCESS)
        else:
            self.message_user(request, _('No se seleccionó ningún registro para desactivar.'), messages.WARNING)

########################################################################################################    Admin para SerieImage
@admin.register(SerieImage)
class SerieImageAdmin(ImportExportModelAdmin):
    resource_class = SerieImageResource

    list_display = ('serie', 'size_image', 'is_active', 'created_at')
    list_filter = ('is_active', 'size_image')
    search_fields = ('serie__title',)
    ordering = ('-created_at', 'serie__title')
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('serie', 'size_image', 'image', 'image_url')
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

########################################################################################################    Admin para SerieImageExtra
@admin.register(SerieImageExtra)
class SerieImageExtraAdmin(ImportExportModelAdmin):
    resource_class = SerieImageExtraResource

    list_display = ('serie', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('serie__title',)
    ordering = ('-created_at', 'serie__title')
    readonly_fields = ('created_at', 'updated_at',)

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información básica'), {
            'fields': ('serie', 'image')
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