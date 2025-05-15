from django.db import models
from django.core.exceptions import ValidationError
from core.utils.utils import validate_year
from django.utils.translation import gettext_lazy as _

class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        # Asegúrate de que el validador no se agregue si ya existe
        validators = kwargs.get('validators', [])
        if validate_year not in validators:
            validators.append(validate_year)
        kwargs['validators'] = validators

        # Llama al constructor de la clase base
        super().__init__(*args, **kwargs)

########################################################################################################    Modelo para BaseLog
class BaseLog(models.Model):
    """Model definition for BaseLog."""
    LEVELS = ['INFO', 'ERROR', 'WARNING', 'DEBUG']

    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('fecha Añadido'))
    process = models.TextField(default='', verbose_name=_('Proceso'))
    level = models.CharField(max_length=10, default='INFO', verbose_name=_('Nivel'))
    message = models.TextField(verbose_name=_('Mensaje'))

    class Meta:
        abstract = True

    def __str__(self):
        """Representación del objeto Log."""
        return f"{self.level} - {self.process} - {self.message}"

########################################################################################################    Modelo para BaseMALFetchStatus
class BaseMALFetchStatus(models.Model):
    """Model definition for BaseMALFetchStatus."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        abstract = True

