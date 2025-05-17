from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
import os


ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.webp', '.png', '.bmp', '.gif', '.tiff', '.tif', '.svg', '.rpgmvp',]
ALLOWED_AUDIO_EXTENSIONS = [".mp3", ".aac", ".ogg", ".wma", ".wav", ]
ALLOWED_VIDEO_EXTENSIONS = [".mp4", ".mkv", ".avi", ".mov", ".webm", ".wmv", ".flv",]
ALLOWED_FONT_EXTENSIONS =  ['.woff', '.woff2', '.otf', '.ttf', '.ttc',]
ALLOWED_DOCUMENT_EXTENSIONS = ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf', '.odt',]


def validate_file_extension(value, allowed_extensions):
    print('validate_file_extension')
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in allowed_extensions:
        raise ValidationError(
            _('Formato de archivo no permitido: %(ext)s. Solo se permiten: %(allowed)s'),
            params={'ext': ext, 'allowed': ', '.join(allowed_extensions)}
        )


def validate_url(value):
    """
    Valida una URL que puede no incluir http:// o https://.
    Lanza ValidationError si no es válida.
    """
    if not value:
        return None

    value = value.strip()
    to_validate = value

    if not to_validate.lower().startswith(('http://', 'https://')):
        to_validate = 'http://' + to_validate

    validator = URLValidator()
    try:
        validator(to_validate)
    except ValidationError:
        raise ValidationError(_('Debe ingresar una URL válida.'))

    return value
