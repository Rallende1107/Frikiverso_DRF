# Imports estándar de Python
import os
from django.utils.text import slugify
# Generador de Base Media
BASE_MEDIA = os.path.join('app_movie', 'movie')

def get_movie_slug(movie):
    """Devuelve el slug de la movie, o convierte el title slug."""
    return movie.slug or slugify(movie.title)

# Imagen principal de movie
def movie_image_path(instance, filename):
    """
    Ruta para imágenes principales.
    Formato: app_movie/movie/{slug}/image/{size_image}/{slug}-{n}.{ext}
    """
    from apps.movie.models import MovieImage

    # Obtener la película y el slug
    movie = instance.movie
    movie_slug = get_movie_slug(movie)

    # Obtener la extensión del archivo
    ext = os.path.splitext(filename)[1].lower()

    # Obtener el nombre del tamaño de imagen
    size_name = instance.size_image.slug.strip().lower()

    # Contador para la cantidad de imágenes ya asociadas a la pelicula
    count = MovieImage.objects.filter(movie=movie, size_image=instance.size_image).count() + 1

    # Crear el nuevo nombre de archivo con el contador
    new_filename = f"{movie_slug}-{count}{ext}"

    # Incluir el tamaño de la imagen en la ruta (subcarpeta según 'size_image')
    return os.path.join(BASE_MEDIA, movie_slug, 'image', size_name, new_filename)


# Imagen adicional de movie
def movie_image_extra_path(instance, filename):
    """
    Ruta para imágenes extra.
    Formato: app_movie/movie/{slug}/image_extra/{slug}-{n}.{ext}
    """
    from apps.movie.models import MovieImageExtra

    movie = instance.movie
    movie_slug = get_movie_slug(movie)
    ext = os.path.splitext(filename)[1].lower()

    count = MovieImageExtra.objects.filter(movie=movie).count() + 1
    new_filename = f"{movie_slug}-{count}{ext}"

    return os.path.join(BASE_MEDIA, movie_slug, 'image_extra', new_filename)