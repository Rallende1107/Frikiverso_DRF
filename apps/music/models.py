# Imports estándar de Python
import os
import uuid
# Imports de terceros (Django, PIL, etc.)
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage
# # Imports locales del proyecto
from apps.common.models import Person, ImageSize
from core.utils.utils import BaseLog, obtener_inicial, YearField
from .utils.uploads import song_path, album_image_path, album_image_extra_path, artist_image_path, artist_image_extra_path

# Create your models here.
########################################################################################################    Log
class MusicLog(BaseLog):
    """Model definition for MusicLog."""
    class Meta:
        """Definición de meta datos para MusicLog."""
        verbose_name = _('Log Música')
        verbose_name_plural = _('Logs Música')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Music'

########################################################################################################    Modelo para Genre
class Genre(models.Model):
    """Model definition for Genre."""
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'is_active': True}, related_name='childrens', on_delete=models.CASCADE, verbose_name=_('Padre'))
    name = models.CharField(max_length=40, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=40, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=40, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Genre."""
        verbose_name = _('Género')
        verbose_name_plural = _('Géneros')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Genre."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Genre."""
        # Obtener el objeto original si existe
        old = Genre.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Genre."""
        return reverse('music_app:genre_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_artists(self):
        return self.artists_as_genres.count()

########################################################################################################    Modelo para Role
class Role(models.Model):
    """Model definition for Role."""
    name = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=30, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Role."""
        verbose_name = _('Rol')
        verbose_name_plural = _('Roles')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Genre."""
        return self.name

    def save(self, *args, **kwargs):
        """Unicode representation of Role."""
        # Obtener el objeto original si existe
        old = Role.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()

        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Role."""
        return reverse('music_app:role_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_persons(self):
        return self.persons_role_memberships.count()

########################################################################################################    Modelo para AlbumType
class AlbumType(models.Model):
    """Model definition for AlbumType."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AlbumType."""
        verbose_name = _('Tipo Álbum')
        verbose_name_plural = _('Tipos Álbumes')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of AlbumType."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for AlbumType."""
        # Obtener el objeto original si existe
        old = AlbumType.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for AlbumType."""
        return reverse('music_app:album_type_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_albums(self):
        return self.albums_as_types.count()

########################################################################################################    Modelo para ArtistType
class ArtistType(models.Model):
    """Model definition for ArtistType."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for ArtistType."""
        verbose_name = _('Tipo Artista')
        verbose_name_plural = _('Tipos Artistas')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of ArtistType."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for ArtistType."""
        # Obtener el objeto original si existe
        old = ArtistType.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for ArtistType."""
        return reverse('music_app:artist_type_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_artists(self):
        return self.artist_memberships.count()

########################################################################################################    Modelo para Artist
class Artist(models.Model):
    """Model definition for Artist."""
    name = models.CharField(max_length=150, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    biography = models.TextField(blank=True, verbose_name=_('Biografía'))
    start_year = YearField(blank=True, null=True, verbose_name=_('Año inicio'))
    year_end = YearField(blank=True, null=True, verbose_name=_('Año término'))
    artist_type = models.ForeignKey(ArtistType, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='artits_as_types', on_delete=models.CASCADE, verbose_name=_('Tipo Artista'))
    genre = models.ManyToManyField(Genre, blank=True, limit_choices_to={'is_active': True}, related_name='artists_as_genres', verbose_name=_('Géneros'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Artist."""
        verbose_name = _("Artista")
        verbose_name_plural = _("Artistas")
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('initial', 'name',),)

    def __str__(self):
        """Unicode representation of Artist."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Artist."""
        # Obtener el objeto original si existe
        old = Artist.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Artist."""
        return reverse('music_app:artist_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_member_count(self):
        """Devuelve el número de miembros del artista."""
        return self.memberships.count()

    def album_count(self):
        """Devuelve el número de álbumes del artista."""
        return self.albums_as_artists.count()

########################################################################################################    Modelo para ArtistMember
class ArtistMember(models.Model):
    """Model definition for ArtistMember. representa la relación entre un artista (grupo) y sus miembros (personas individuales) con rol."""
    artist = models.ForeignKey(Artist, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='artist_memberships', on_delete=models.CASCADE, verbose_name=_('Artista'))
    # Esto permitirá acceder a los miembros desde Artist con artist.memberships.all()
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_role_memberships', on_delete=models.CASCADE, verbose_name=_('Persona'))
    role = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='roles_persons_memberships', on_delete=models.CASCADE, verbose_name=_('Rol'))
    join_date = models.DateField(blank=True, null=True, verbose_name=_('Fecha Ingreso'))
    leave_date = models.DateField(blank=True, null=True, verbose_name=_('Fecha Salida'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for ArtistMember."""
        verbose_name = _('Miembro de Artista')
        verbose_name_plural = _('Miembros de Artistas')
        ordering = ['artist', 'person', 'role', ]
        unique_together = (('artist', 'person', 'role',),)

    def __str__(self):
        """Unicode representation of ArtistMember."""
        return f"{self.person.full_name} es {self.role.name} en {self.artist.name}"

    def save(self, *args, **kwargs):
        """Save method for ArtistMember."""
        # Aquí puedes agregar lógica si en el futuro necesitas, como validar fechas, normalizar texto, etc.
        if self.leave_date and self.join_date and self.leave_date < self.join_date:
            raise ValueError("La fecha de salida no puede ser anterior a la de ingreso.")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for ArtistMember."""
        return reverse('music_app:artist_member_detail', kwargs={'pk': self.pk})

########################################################################################################    Modelo para Album
class Album(models.Model):
    """Model definition for Album."""
    title = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=255, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    artist = models.ForeignKey(Artist, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='albums_as_artists', on_delete=models.CASCADE, verbose_name=_('Artista'))
    album_type = models.ForeignKey(AlbumType, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='albums_as_types', on_delete=models.CASCADE, verbose_name=_('Tipo'))
    release_date = models.DateField(blank=True, null=True, verbose_name=_('Fecha Lanzamiento'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Album."""
        verbose_name = _('Álbum')
        verbose_name_plural = _('Álbumes')
        ordering = ['artist', 'title',]
        unique_together = (('artist', 'album_type', 'title',),)

    def __str__(self):
        """Unicode representation of Album."""
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Album."""
        # Obtener el objeto original si existe
        old = Album.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.title:
            self.title = self.title.strip()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Album."""
        return reverse('music_app:album_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_img_url(self):
        if self.cover_image:
            return settings.MEDIA_URL + str(self.cover_image)
        return None

    def song_count(self):
        """Devuelve el número de canciones del álbum."""
        return self.songs_as_albums.count()

########################################################################################################    Modelo para Song
class Song(models.Model):
    """Model definition for Song."""
    title = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=255, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    lyrics = models.TextField(blank=True, verbose_name=_('Letra'))
    album_song_id = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('ID Canción Álbum'))
    release_date = models.DateField(blank=True, null=True, verbose_name=_('Fecha Lanzamiento'))
    album = models.ForeignKey(Album, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='songs_as_albums', on_delete=models.PROTECT, verbose_name=_('Álbum'))
    audio_file = models.FileField(blank=True, null=True, upload_to=song_path, verbose_name=_('Archivo Audio'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Song."""
        verbose_name = _('Canción')
        verbose_name_plural = _('Canciones')
        ordering = ['album_song_id', 'album',]
        unique_together = (('album_song_id', 'title', 'album',),)

    def __str__(self):
        """Unicode representation of Song."""
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Song."""
        # Obtener el objeto original si existe
        old = Song.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.title:
            self.title = self.title.strip()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Song."""
        return reverse('music_app:song_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_media_url(self):
        if self.audio_file:
            return settings.MEDIA_URL + str(self.audio_file)
        return None

#######################################################################################################    Modelo para AlbumImage
class AlbumImage(models.Model):
    """Model definition for AlbumImage."""
    album = models.ForeignKey(Album, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='albums_as_images', on_delete=models.CASCADE, verbose_name=_('Álbum'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='albums_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=album_image_path, verbose_name=_('Imagen Álbum'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AlbumImage."""
        verbose_name = _('Imagen Álbum')
        verbose_name_plural = _('Imágenes Álbumes')
        ordering = ['album', 'size_image', 'name',]
        unique_together = (('album', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of AlbumImage."""
        return self.name if self.album else _('Imagen sin Álbum')

    def save(self, *args, **kwargs):
        """Save method for AlbumImage."""
        old = AlbumImage.objects.filter(pk=self.pk).first() if self.pk else None
        # Guardar inicialmente si no hay pk para obtener path de imagen
        if not self.pk:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = temp_image
        # Actualizar nombre si no existe o si cambió el archivo
        if self.image:
            filename = os.path.basename(self.image.name)
            if not self.name or (old and old.image.name != self.image.name):
                self.name = filename
        # Regenerar slug si no existe o si cambió el nombre
        if not self.slug or (old and old.name != self.name):
            self.slug = slugify(self.name) or str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for AlbumImage."""
        return reverse('album_app:album_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.album:
            return self.album.title
        return None

    def get_img_url(self):
        if self.image:
            return settings.MEDIA_URL + str(self.image)
        return None

    def get_image_name(self):
        if self.name:
            base_name = os.path.splitext(os.path.basename(self.name))[0]
            return base_name
        return None

    def get_image_extension(self):
        if self.name:
            ext = os.path.splitext(self.name)[1]
            return ext.lower()
        return None

    @property
    def image_file_size(self):
        if self.image and self.image.size:
            size = self.image.size
            for unit in ['bytes', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.2f} {unit}"
                size /= 1024.0
            return f"{size:.2f} TB"
        return "Tamaño desconocido"

    @property
    def image_dimensions(self):
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            try:
                with PILImage.open(self.image) as img:
                    return img.size
            except Exception as e:
                print(f"Error al abrir la imagen: {e}")
        return (0, 0)

########################################################################################################    Modelo para AlbumImageExtra
class AlbumImageExtra(models.Model):
    """Model definition for AlbumImageExtra."""
    album = models.ForeignKey(Album, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='albums_as_images_extra', on_delete=models.CASCADE, verbose_name=_('Álbum'))
    image = models.ImageField(blank=False, null=False, upload_to=album_image_extra_path, verbose_name=_('Imagen Extra Álbum'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AlbumImageExtra."""
        verbose_name = _('Imagen Extra Álbum')
        verbose_name_plural = _('Imágenes Extra Álbumes')
        ordering = ['album', 'name',]
        unique_together = (('album', 'name',),)

    def __str__(self):
        """Unicode representation of AlbumImageExtra."""
        return self.name if self.album else _('Imagen sin Álbum')

    def save(self, *args, **kwargs):
        """Save method for AlbumImageExtra."""
        old = AlbumImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
        # Guardar inicialmente si no hay pk para obtener path de imagen
        if not self.pk:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = temp_image
        # Actualizar nombre si no existe o si cambió el archivo
        if self.image:
            filename = os.path.basename(self.image.name)
            if not self.name or (old and old.image.name != self.image.name):
                self.name = filename
        # Regenerar slug si no existe o si cambió el nombre
        if not self.slug or (old and old.name != self.name):
            self.slug = slugify(self.name) or str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for AlbumImageExtra."""
        return reverse('music_app:album_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.album:
            return self.album.title
        return None

    def get_img_url(self):
        if self.image:
            return settings.MEDIA_URL + str(self.image)
        return None

    def get_image_name(self):
        if self.name:
            base_name = os.path.splitext(os.path.basename(self.name))[0]
            return base_name
        return None

    def get_image_extension(self):
        if self.name:
            ext = os.path.splitext(self.name)[1]
            return ext.lower()
        return None

    @property
    def image_file_size(self):
        if self.image and self.image.size:
            size = self.image.size
            for unit in ['bytes', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.2f} {unit}"
                size /= 1024.0
            return f"{size:.2f} TB"
        return "Tamaño desconocido"

    @property
    def image_dimensions(self):
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            try:
                with PILImage.open(self.image) as img:
                    return img.size
            except Exception as e:
                print(f"Error al abrir la imagen: {e}")
        return (0, 0)

#######################################################################################################    Modelo para ArtistImage
class ArtistImage(models.Model):
    """Model definition for ArtistImage."""
    artist = models.ForeignKey(Artist, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='artists_as_images', on_delete=models.CASCADE, verbose_name=_('Artista'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='artists_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=artist_image_path, verbose_name=_('Imagen Artista'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for ArtistImage."""
        verbose_name = _('Imagen Artista')
        verbose_name_plural = _('Imágenes Artistas')
        ordering = ['artist', 'size_image', 'name',]
        unique_together = (('artist', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of ArtistImage."""
        return self.name if self.artist else _('Imagen sin Artista')

    def save(self, *args, **kwargs):
        """Save method for ArtistImage."""
        old = ArtistImage.objects.filter(pk=self.pk).first() if self.pk else None
        # Guardar inicialmente si no hay pk para obtener path de imagen
        if not self.pk:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = temp_image
        # Actualizar nombre si no existe o si cambió el archivo
        if self.image:
            filename = os.path.basename(self.image.name)
            if not self.name or (old and old.image.name != self.image.name):
                self.name = filename
        # Regenerar slug si no existe o si cambió el nombre
        if not self.slug or (old and old.name != self.name):
            self.slug = slugify(self.name) or str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for ArtistImage."""
        return reverse('music_app:artist_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.artist:
            return self.artist.name
        return None

    def get_img_url(self):
        if self.image:
            return settings.MEDIA_URL + str(self.image)
        return None

    def get_image_name(self):
        if self.name:
            base_name = os.path.splitext(os.path.basename(self.name))[0]
            return base_name
        return None

    def get_image_extension(self):
        if self.name:
            ext = os.path.splitext(self.name)[1]
            return ext.lower()
        return None

    @property
    def image_file_size(self):
        if self.image and self.image.size:
            size = self.image.size
            for unit in ['bytes', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.2f} {unit}"
                size /= 1024.0
            return f"{size:.2f} TB"
        return "Tamaño desconocido"

    @property
    def image_dimensions(self):
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            try:
                with PILImage.open(self.image) as img:
                    return img.size
            except Exception as e:
                print(f"Error al abrir la imagen: {e}")
        return (0, 0)

########################################################################################################    Modelo para ArtistImageExtra
class ArtistImageExtra(models.Model):
    """Model definition for ArtistImageExtra."""
    artist = models.ForeignKey(Artist, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='artists_as_images_extra', on_delete=models.CASCADE, verbose_name=_('Artista'))
    image = models.ImageField(blank=False, null=False, upload_to=artist_image_extra_path, verbose_name=_('Imagen Extra Artista'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for ArtistImageExtra."""
        verbose_name = _('Imagen Extra Artista')
        verbose_name_plural = _('Imágenes Extra Artista')
        ordering = ['artist', 'name',]
        unique_together = (('artist', 'name',),)

    def __str__(self):
        """Unicode representation of ArtistImageExtra."""
        return self.name if self.artist else _('Imagen sin Artista')

    def save(self, *args, **kwargs):
        """Save method for ArtistImageExtra."""
        old = ArtistImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
        # Guardar inicialmente si no hay pk para obtener path de imagen
        if not self.pk:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = temp_image
        # Actualizar nombre si no existe o si cambió el archivo
        if self.image:
            filename = os.path.basename(self.image.name)
            if not self.name or (old and old.image.name != self.image.name):
                self.name = filename
        # Regenerar slug si no existe o si cambió el nombre
        if not self.slug or (old and old.name != self.name):
            self.slug = slugify(self.name) or str(uuid.uuid4())
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for ArtistImageExtra."""
        return reverse('music_app:artist_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.artist:
            return self.artist.name
        return None

    def get_img_url(self):
        if self.image:
            return settings.MEDIA_URL + str(self.image)
        return None

    def get_image_name(self):
        if self.name:
            base_name = os.path.splitext(os.path.basename(self.name))[0]
            return base_name
        return None

    def get_image_extension(self):
        if self.name:
            ext = os.path.splitext(self.name)[1]
            return ext.lower()
        return None

    @property
    def image_file_size(self):
        if self.image and self.image.size:
            size = self.image.size
            for unit in ['bytes', 'KB', 'MB', 'GB']:
                if size < 1024.0:
                    return f"{size:.2f} {unit}"
                size /= 1024.0
            return f"{size:.2f} TB"
        return "Tamaño desconocido"

    @property
    def image_dimensions(self):
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            try:
                with PILImage.open(self.image) as img:
                    return img.size
            except Exception as e:
                print(f"Error al abrir la imagen: {e}")
        return (0, 0)