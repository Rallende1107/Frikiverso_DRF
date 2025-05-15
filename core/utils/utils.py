import os, datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_year(value):
    if len(str(value)) != 4:
        raise ValidationError("El año debe tener 4 dígitos.")

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

def delete_previous_media(media_url):
    try:
        # Obtener la ruta del archivo desde la URL
        img_path = os.path.join(settings.MEDIA_ROOT, media_url[len(settings.MEDIA_URL):])

        # Verificar si el archivo existe y eliminarlo
        if os.path.isfile(img_path):
            os.remove(img_path)
    except Exception as e:
        # Manejar cualquier excepción que pueda ocurrir al eliminar el archivo
        print(f"Error al eliminar la imagen anterior: {str(e)}")

def formato_fecha(date):
    """Esta función toma un objeto de fecha como entrada y devuelve una representación de cadena formateada de la fecha.

    Args:
        date (datetime.date o datetime.datetime): La fecha que se formateará.

    Returns:
        str: La fecha formateada como una cadena de texto, o 'Invalid date' si la entrada no es válida.
    """
    if not isinstance(date, (datetime.date, datetime)):
        return 'Invalid date'

    try:
        return date.strftime("%d, %b %Y")
    except Exception as e:
        return f"Error al formatear la fecha: {e}"