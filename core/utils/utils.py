from django.db import models
from django.core.exceptions import ValidationError

def validate_year(value):
    if len(str(value)) != 4:
        raise ValidationError("El año debe tener 4 dígitos.")


class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        # Asegúrate de que el validador no se agregue si ya existe
        validators = kwargs.get('validators', [])
        if validate_year not in validators:
            validators.append(validate_year)
        kwargs['validators'] = validators

        # Llama al constructor de la clase base
        super().__init__(*args, **kwargs)


def obtener_inicial(texto):
    """Obtiene el primer carácter de un texto en mayúscula o asigna '#' si no es una letra."""

    if texto:
        first_char = texto[0].upper()  # Obtener el primer carácter en mayúscula
        if not first_char.isalpha():  # Si no es una letra (A-Z), asignar '#'
            initial = '#'
        else:
            initial = first_char
    else:
        initial = '#'

    return initial

########################################################################################################    Modelo para BaseLog
class BaseLog(models.Model):
    """Model definition for BaseLog."""
    LEVELS = ['INFO', 'ERROR', 'WARNING', 'DEBUG']

    timestamp = models.DateTimeField(auto_now_add=True)
    process = models.TextField(verbose_name='Proceso', default='')
    level = models.CharField(max_length=10, verbose_name='Nivel', default='INFO')
    message = models.TextField(verbose_name='Mensaje')

    class Meta:
        abstract = True

    def __str__(self):
        """Representación del objeto Log."""
        return f"{self.level} - {self.process} - {self.message}"