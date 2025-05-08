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
