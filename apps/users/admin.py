from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# impot Modelos
from .models import (CustomUser)
# impot Resource
from .resources import (CustomUserResource)
# impot Inline
# from apps.serie.utils.inline import (TitleSerieInline, SerieImageInline, SerieImageExtraInline, SerieStaffInline, SerieCastInline)
# Register your models here.
########################################################################################################    Admin para CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource

    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'birth_year', 'is_active', 'created_at')
    list_filter = ('is_active', 'birth_year')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-created_at', 'username')
    readonly_fields = ('created_at', 'updated_at', 'slug')

    actions = ['activar', 'desactivar']

    fieldsets = (
        (_('Información del Usuario'), {
            'fields': ('username', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'birth_year', 'avatar')
        }),
        (_('Estado'), {
            'fields': ('is_active',)
        }),
        (_('Valores Generados Automáticamente'), {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
        (_('Fechas'), {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    @admin.action(description='Activar usuarios seleccionados')
    def activar(self, request, queryset):
        actualizados = queryset.update(is_active=True)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} usuario(s) activado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún usuario para activar.", messages.WARNING)

    @admin.action(description='Desactivar usuarios seleccionados')
    def desactivar(self, request, queryset):
        actualizados = queryset.update(is_active=False)
        if actualizados:
            self.message_user(request, f"✅ {actualizados} usuario(s) desactivado(s).", messages.SUCCESS)
        else:
            self.message_user(request, "No se seleccionó ningún usuario para desactivar.", messages.WARNING)
