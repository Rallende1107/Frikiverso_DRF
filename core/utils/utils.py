import os, datetime,  re, random
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validators import validate_url

def normalize_text(text):
    """Normaliza el texto: elimina espacios y lo convierte a mayúsculas."""
    return ''.join(text.upper().split())

def to_title_text(text: str) -> str:
    """Aplica formato título (primera letra en mayúscula de cada palabra)."""
    return ' '.join(text.strip().title().split())

def to_upper_text(text: str) -> str:
    """Convierte todo el texto a mayúsculas, limpiando espacios extra."""
    return ' '.join(text.strip().upper().split())

def to_capitalized_sentence(text: str) -> str:
    """Capitaliza solo la primera palabra del texto, dejando el resto igual."""
    return text.strip().capitalize()

# to_title_text("  archivo de música mkv  ")  →  "Archivo De Música Mkv"
# to_upper_text("  mKv   file ")  →  "MKV FILE"
# to_capitalized_sentence("  nacion unida de EEUU ")  →  "Nacion unida de eeuu"



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

def procesar_urls(url: str, tipo: int):
    """
    Procesa URLs de F95Zone, MAL Anime o MAL Manga.

    Parámetros:
        url (str): URL a procesar (puede ser None o cadena vacía).
        tipo (int):
            1 = F95Zone
            2 = MyAnimeList (Anime)
            3 = MyAnimeList (Manga)

    Retorna:
        tuple[str, int]: URL limpia y ID extraído.

    Excepciones:
        ValueError: Si no se puede extraer el ID o tipo inválido.
    """

    if tipo == 1:  # F95Zone
        if url:
            match = re.search(r'/threads/(?:.*?)(\d{4,})/?', url)
            if match:
                resource_id = int(match.group(1))
                clean_url = f"https://f95zone.to/threads/{resource_id}/"
                return validate_url(clean_url), resource_id
            else:
                raise ValueError("URL de F95Zone no válida. Asegúrese de que contiene un ID.")
        else:
            resource_id = -random.randint(1, 9999999)
            clean_url = f"https://f95zone.to/threads/{abs(resource_id)}/"
            return validate_url(clean_url), resource_id

    elif tipo == 2:  # MyAnimeList Anime
        if url:
            match = re.search(r'/anime/(\d+)/?', url)
            if match:
                resource_id = int(match.group(1))
                clean_url = f"https://myanimelist.net/anime/{resource_id}"
                return validate_url(clean_url), resource_id
            else:
                raise ValueError("URL de MAL Anime no válida. Asegúrese de que contiene un ID.")
        else:
            resource_id = -random.randint(1, 9999999)
            clean_url = f"https://myanimelist.net/anime/{abs(resource_id)}"
            return validate_url(clean_url), resource_id

    elif tipo == 3:  # MyAnimeList Manga
        if url:
            match = re.search(r'/manga/(\d+)/?', url)
            if match:
                resource_id = int(match.group(1))
                clean_url = f"https://myanimelist.net/manga/{resource_id}"
                return validate_url(clean_url), resource_id
            else:
                raise ValueError("URL de MAL Manga no válida. Asegúrese de que contiene un ID.")
        else:
            resource_id = -random.randint(1, 9999999)
            clean_url = f"https://myanimelist.net/manga/{abs(resource_id)}"
            return validate_url(clean_url), resource_id

    else:
        raise ValueError("Tipo inválido. Use 1 para F95, 2 para Anime, o 3 para Manga.")

def get_media_context(view, field_name='image', method_name='get_img_url'):
    """
    Retorna si hay media y su URL para ser usado en el contexto de una vista basada en clase.

    Args:
        view: Instancia de la CBV (ej: self).
        field_name: Nombre del campo de archivo multimedia (por defecto 'image').
        method_name: Método del modelo que devuelve la URL (por defecto 'get_img_url').

    Returns:
        Tuple (bool, str or None): (hay_media, url_media)
    """
    form = view.get_form()
    media_url = None

    if field_name in form.fields:
        obj = view.get_object()
        if obj and hasattr(obj, method_name):
            method = getattr(obj, method_name)
            if callable(method):
                media_url = method()

    return bool(media_url), media_url