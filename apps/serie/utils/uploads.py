# Imports estándar de Python
import os
from django.utils.text import slugify
# Generador de Base Media
BASE_MEDIA = os.path.join('app_serie', 'serie')

def get_serie_slug(serie):
    """Devuelve el slug de la serie, o convierte el title slug."""
    return serie.slug or slugify(serie.title)

# Imagen principal de serie
def serie_image_path(instance, filename):
    """
    Ruta para imágenes principales.
    Formato: app_serie/serie/{slug}/image/{size_image}/{slug}-{n}.{ext}
    """
    from apps.serie.models import SerieImage

    # Obtener la película y el slug
    serie = instance.serie
    serie_slug = get_serie_slug(serie)

    # Obtener la extensión del archivo
    ext = os.path.splitext(filename)[1].lower()

    # Obtener el nombre del tamaño de imagen
    size_name = instance.size_image.slug.strip().lower()

    # Contador para la cantidad de imágenes ya asociadas a la pelicula
    count = SerieImage.objects.filter(serie=serie, size_image=instance.size_image).count() + 1

    # Crear el nuevo nombre de archivo con el contador
    new_filename = f"{serie_slug}-{count}{ext}"

    # Incluir el tamaño de la imagen en la ruta (subcarpeta según 'size_image')
    return os.path.join(BASE_MEDIA, serie_slug, 'image', size_name, new_filename)


# Imagen adicional de serie
def serie_image_extra_path(instance, filename):
    """
    Ruta para imágenes extra.
    Formato: app_serie/serie/{slug}/image_extra/{slug}-{n}.{ext}
    """
    from apps.serie.models import SerieImageExtra

    serie = instance.serie
    serie_slug = get_serie_slug(serie)
    ext = os.path.splitext(filename)[1].lower()

    count = SerieImageExtra.objects.filter(serie=serie).count() + 1
    new_filename = f"{serie_slug}-{count}{ext}"

    return os.path.join(BASE_MEDIA, serie_slug, 'image_extra', new_filename)