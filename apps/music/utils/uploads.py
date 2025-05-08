# Imports estándar de Python
import os
from django.utils.text import slugify
# Generador de Base Media
BASE_MEDIA_ALBUM = os.path.join('app_music', 'music', 'album')
BASE_MEDIA_ARTIST = os.path.join('app_music', 'music', 'artist')

def get_album_slug(album):
    """Devuelve el slug del album, o convierte el title slug."""
    return album.slug or slugify(album.title)

def get_artist_slug(artist):
    """Devuelve el slug del artist, o convierte el name slug."""
    return artist.slug or slugify(artist.name)

# Imagen principal de album
def album_image_path(instance, filename):
    """
    Ruta para imágenes principales.
    Formato: app_music/music/album/{slug}/image/{size_image}/{slug}-{n}.{ext}
    """
    from apps.music.models import AlbumImage

    # Obtener la película y el slug
    album = instance.album
    album_slug = get_album_slug(album)

    # Obtener la extensión del archivo
    ext = os.path.splitext(filename)[1].lower()

    # Obtener el nombre del tamaño de imagen
    size_name = instance.size_image.slug.strip().lower()

    # Contador para la cantidad de imágenes ya asociadas al album
    count = AlbumImage.objects.filter(album=album, size_image=instance.size_image).count() + 1

    # Crear el nuevo nombre de archivo con el contador
    new_filename = f"{album_slug}-{count}{ext}"

    # Incluir el tamaño de la imagen en la ruta (subcarpeta según 'size_image')
    return os.path.join(BASE_MEDIA_ALBUM, album_slug, 'image', size_name, new_filename)

# Imagen adicional de album
def album_image_extra_path(instance, filename):
    """
    Ruta para imágenes extra.
    Formato: app_music/music/album/{slug}/image_extra/{slug}-{n}.{ext}
    """
    from apps.music.models import AlbumImageExtra

    album = instance.album
    album_slug = get_album_slug(album)
    ext = os.path.splitext(filename)[1].lower()

    count = AlbumImageExtra.objects.filter(album=album).count() + 1
    new_filename = f"{album_slug}-{count}{ext}"

    return os.path.join(BASE_MEDIA_ALBUM, album_slug, 'image_extra', new_filename)

# Imagen principal de artista
def artist_image_path(instance, filename):
    """
    Ruta para imágenes principales.
    Formato: app_music/music/artist/{slug}/image/{size_image}/{slug}-{n}.{ext}
    """
    from apps.music.models import ArtistImage

    # Obtener la película y el slug
    artist = instance.artist
    artist_slug = get_artist_slug(artist)

    # Obtener la extensión del archivo
    ext = os.path.splitext(filename)[1].lower()

    # Obtener el nombre del tamaño de imagen
    size_name = instance.size_image.slug.strip().lower()

    # Contador para la cantidad de imágenes ya asociadas al artist
    count = ArtistImage.objects.filter(artist=artist, size_image=instance.size_image).count() + 1

    # Crear el nuevo nombre de archivo con el contador
    new_filename = f"{artist_slug}-{count}{ext}"

    # Incluir el tamaño de la imagen en la ruta (subcarpeta según 'size_image')
    return os.path.join(BASE_MEDIA_ARTIST, artist_slug, 'image', size_name, new_filename)

# Imagen adicional de artista
def artist_image_extra_path(instance, filename):
    """
    Ruta para imágenes extra.
    Formato: app_music/music/artist/{slug}/image_extra/{slug}-{n}.{ext}
    """
    from apps.music.models import ArtistImageExtra

    artist = instance.artist
    artist_slug = get_artist_slug(artist)
    ext = os.path.splitext(filename)[1].lower()

    count = ArtistImageExtra.objects.filter(artist=artist).count() + 1
    new_filename = f"{artist_slug}-{count}{ext}"

    return os.path.join(BASE_MEDIA_ARTIST, artist_slug, 'image_extra', new_filename)

# Canciones del album
def song_path(instance, filename):
    """
    Ruta para archivos de audio de canciones.
    Formato: app_music/music/album/{slug}/songs/{nombre_original}.{ext}
    """
    album = instance.album
    album_slug = slugify(album.slug if album and album.slug else 'unknown')

    base_filename, ext = os.path.splitext(filename)
    filename_final = base_filename + ext.lower()

    return os.path.join(BASE_MEDIA_ALBUM, album_slug, 'songs', filename_final)