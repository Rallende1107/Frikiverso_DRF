# Imports estándar de Python
import os, uuid
# Imports de terceros (Django, PIL, etc.)
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage
# Imports locales del proyecto
from apps.common.models import Language, ImageSize
from core.models import BaseLog, YearField
from core.utils.utils import obtener_inicial
from .utils.uploads import developer_image_path, developer_image_extra_path, translator_image_path, translator_image_extra_path, publisher_image_path, publisher_image_extra_path, game_image_path, game_image_extra_path

# Create your models here.
########################################################################################################    Log
class RenpyLog(BaseLog):
    """Model definition for RenpyLog."""
    class Meta:
        """Meta definition for RenpyLog."""
        verbose_name = _('Log Renpy')
        verbose_name_plural = _('Logs Renpy')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Renpy'

########################################################################################################    Modelo para Genre
class Genre(models.Model):
    """Model definition for Genre."""
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'is_active': True}, related_name='childrens', on_delete=models.CASCADE, verbose_name=_('Padre'))
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    explicit = models.BooleanField(default=False, verbose_name=_('Explicito'))
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
        old = Genre.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        if self.name_esp:
            self.name_esp = self.name_esp.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Genre."""
        return reverse('renpy_app:genre_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_genre.count()

########################################################################################################    Modelo para GameEngine
class GameEngine(models.Model):
    """Model definition for GameEngine."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for GameEngine."""
        verbose_name = _('Motor Desarrollo')
        verbose_name_plural = _('Motores Desarrollo')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of GameEngine."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for GameEngine."""
        old = GameEngine.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for GameEngine."""
        return reverse('renpy_app:game_engine_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_engine.count()

########################################################################################################    Modelo para Censorship
class Censorship(models.Model):
    """Model definition for Censorship."""
    name = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=30, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Censorship."""
        verbose_name = _('Censura')
        verbose_name_plural = _('Censuras')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Censorship."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Censorship."""
        old = Censorship.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Censorship."""
        return reverse('renpy_app:censorship_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_censorship.count()

########################################################################################################    Modelo para prefix
class Prefix(models.Model):
    """Model definition for Prefix."""
    name = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=30, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Prefix."""
        verbose_name = _('Prefijo')
        verbose_name_plural = _('Prefijos')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Prefix."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Prefix."""
        old = Prefix.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        if self.name_esp:
            self.name_esp = self.name_esp.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Prefix."""
        return reverse('renpy_app:prefix_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here

########################################################################################################    Modelo para Status
class Status(models.Model):
    """Model definition for Status."""
    name = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=30, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Status."""
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Status."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Status."""
        old = Status.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Status."""
        return reverse('renpy_app:status_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_status.count()

########################################################################################################    Modelo para Platform
class Platform(models.Model):
    """Model definition for Platform."""
    name = models.CharField(max_length=30, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=30, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Platform."""
        verbose_name = _('Plataforma')
        verbose_name_plural = _('Plataformas')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Platform."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Platform."""
        old = Platform.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        if self.name_esp:
            self.name_esp = self.name_esp.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Platform."""
        return reverse('renpy_app:platform_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_platforms.count()

########################################################################################################    Modelo para Developer
class Developer(models.Model):
    """Model definition for Developer."""
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Developer."""
        verbose_name = _('Desarrollador')
        verbose_name_plural = _('Desarrolladores')
        ordering = ['-created_at', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Developer."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Developer."""
        old = Developer.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Developer."""
        return reverse('renpy_app:developer_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_developed.count()

    def get_num_links(self):
        return self.developers_as_links.count()

########################################################################################################    Modelo para Translator
class Translator(models.Model):
    """Model definition for Translator."""
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Translator."""
        verbose_name = _('Traductor')
        verbose_name_plural = _('Traductores')
        ordering = ['-created_at', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Translator."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Translator."""
        old = Translator.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Translator."""
        return reverse('renpy_app:translator_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_translated.count()

    def get_num_links(self):
        return self.translators_as_links.count()

########################################################################################################    Modelo para Publisher
class Publisher(models.Model):
    """Model definition for Publisher."""
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Publisher."""
        verbose_name = _('Editor')
        verbose_name_plural = _('Editores')
        ordering = ['-created_at', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Publisher."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Publisher."""
        old = Publisher.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Publisher."""
        return reverse('renpy_app:publisher_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_games(self):
        return self.games_as_published.count()

    def get_num_links(self):
        return self.publishers_as_links.count()

########################################################################################################    Modelo para Game
class Game(models.Model):
    """Model definition for Game."""
    title = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=255, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    version = models.CharField(max_length=50, unique=False, null=True, blank=True, default='0.0.1', verbose_name=_('Versión'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    release_date = models.DateField(blank=False, null=True, verbose_name=_('Fecha Lanzamiento'))
    synopsis = models.TextField(blank=True, verbose_name=_('Sinopsis'))
    background = models.TextField(blank=True, verbose_name=_('Reseña'))
    status = models.ForeignKey(Status, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='games_as_status', on_delete=models.CASCADE, verbose_name=_('Estado'))
    engine = models.ForeignKey(GameEngine, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='games_as_engine', on_delete=models.CASCADE, verbose_name=_('Motor Desarrollado'))
    platforms = models.ManyToManyField(Platform, blank=True, limit_choices_to={'is_active': True}, related_name='games_as_platforms', verbose_name=_('Plataformas'))
    developers = models.ManyToManyField(Developer, blank=True, limit_choices_to={'is_active': True}, related_name='games_as_develop', verbose_name=_('Desarrollador'))
    publishers = models.ManyToManyField(Publisher, blank=True, limit_choices_to={'is_active': True}, related_name='games_as_publishers', verbose_name=_('Editor'))
    languages = models.ManyToManyField(Language, blank=True, limit_choices_to={'is_active': True}, related_name='games_as_original_language', verbose_name=_('Idioma'))
    translators = models.ManyToManyField(Translator, blank=True, limit_choices_to={'is_active': True}, related_name='games_as_tranlators', verbose_name=_('Traductores'))
    genres = models.ManyToManyField(Genre, blank=True, limit_choices_to={'is_active': True}, related_name='games_as_genres', verbose_name=_('Géneros'))
    censored = models.ForeignKey(Censorship, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='games_as_censored', on_delete=models.CASCADE, verbose_name=_('Censura'))

    url_fzone = models.URLField(max_length=255, blank=True, null=False, verbose_name=_('URL F95'))
    url_steam = models.URLField(max_length=255, blank=True, null=False, verbose_name=_('URL Steam'))
    fzone_id = models.IntegerField(unique=True, null=False, blank=False, default=0, verbose_name=_('ID F95-Zone'))
    version_txt = models.CharField(max_length=50, unique=False, null=True, blank=True, default='0.0.1', verbose_name=_('Versión Text'))

    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Game."""
        verbose_name = _('Juego')
        verbose_name_plural = _('Juegos')
        ordering = ['-created_at', 'title',]
        unique_together = (('fzone_id', 'url_fzone', 'title',),)

    def __str__(self):
        """Unicode representation of Game."""
        developers_names = ", ".join([str(developer) for developer in self.developers.all()])
        return f'{self.title} - [{self.version}] by {developers_names if developers_names else _('Sin Desarrolladores')}'

    def save(self, *args, **kwargs):
        """Save method for Game."""
        old = Game.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Game."""
        return reverse('renpy_app:game_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here

########################################################################################################    Modelo para GameImage
class GameImage(models.Model):
    """Model definition for GameImage."""
    game = models.ForeignKey(Game, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='games_as_images', on_delete=models.CASCADE, verbose_name=_('Juego'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='games_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=game_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for GameImage."""
        verbose_name = _('Imagen Juego')
        verbose_name_plural = _('Imágenes Juegos')
        ordering = ['game', 'size_image', 'name',]
        unique_together = (('game', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of GameImage."""
        return self.name if self.game else _('Imagen sin Juego')

    def save(self, *args, **kwargs):
        """Save method for GameImage."""
        old = GameImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for GameImage."""
        return reverse('renpy_app:game_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.game:
            return self.game.title
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

########################################################################################################    Modelo para DeveloperImage
class GameImageExtra(models.Model):
    """Model definition for GameImageExtra."""
    game = models.ForeignKey(Game, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='games_as_exta_images', on_delete=models.CASCADE, verbose_name=_('Juego'))
    image = models.ImageField(blank=False, null=False, upload_to=game_image_extra_path, verbose_name=_('Imagen Extra Juego'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for GameImageExtra."""
        verbose_name = _('Imagen Extra Juego')
        verbose_name_plural = _('Imágenes Extra Juegos')
        ordering = ['game', 'name',]
        unique_together = (('game', 'name',),)

    def __str__(self):
        """Unicode representation of GameImageExtra."""
        return self.name if self.game else _('Imagen sin Juego')

    def save(self, *args, **kwargs):
        """Save method for GameImageExtra."""
        old = GameImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for GameImageExtra."""
        return reverse('renpy_app:game_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.game:
            return self.game.title
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

########################################################################################################    Modelo para DeveloperLink
class DeveloperLink(models.Model):
    """Model definition for DeveloperLink."""
    developer = models.ForeignKey(Developer, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='developers_as_links', on_delete=models.CASCADE, verbose_name=_('Desarrollador'))
    name = models.CharField(max_length=150, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    url = models.URLField(max_length=2500, blank=False, null=False, verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for DeveloperLink."""
        verbose_name = _('Enlace Desarrollador')
        verbose_name_plural = _('Enlaces Desarrolladores')
        ordering = ['developer', 'initial', 'name',]
        unique_together = (('developer', 'name', 'url',),)

    def __str__(self):
        """Unicode representation of DeveloperLink."""
        return f"{self.developer.name} - {self.name}"

    def save(self, *args, **kwargs):
        """Save method for DeveloperLink."""
        old = DeveloperLink.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip()

        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for DeveloperLink."""
        return reverse('renpy_app:developer_link_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here

########################################################################################################    Modelo para TranslatorLink
class TranslatorLink(models.Model):
    """Model definition for TranslatorLink."""
    translator = models.ForeignKey(Translator, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='translators_as_links', on_delete=models.CASCADE, verbose_name=_('Traductor'))
    name = models.CharField(max_length=150, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    url = models.URLField(max_length=2500, blank=False, null=False, verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TranslatorLink."""
        verbose_name = _('Enlace Traductor')
        verbose_name_plural = _('Enlaces Traductores')
        ordering = ['translator', 'initial', 'name',]
        unique_together = (('translator', 'name', 'url',),)

    def __str__(self):
        """Unicode representation of TranslatorLink."""
        return f"{self.translator.name} - {self.name}"

    def save(self, *args, **kwargs):
        """Save method for TranslatorLink."""
        old = TranslatorLink.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip()

        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for TranslatorLink."""
        return reverse('renpy_app:translator_link_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here

########################################################################################################    Modelo para PublisherLink
class PublisherLink(models.Model):
    """Model definition for PublisherLink."""
    publisher = models.ForeignKey(Publisher, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='publishers_as_links', on_delete=models.CASCADE, verbose_name=_('Editor'))
    name = models.CharField(max_length=150, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    url = models.URLField(max_length=2500, blank=False, null=False, verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TranslatorLink."""
        verbose_name = _('Enlace Editor')
        verbose_name_plural = _('Enlaces Editores')
        ordering = ['publisher', 'initial', 'name',]
        unique_together = (('publisher', 'name', 'url',),)

    def __str__(self):
        """Unicode representation of PublisherLink."""
        return f"{self.publisher.name} - {self.name}"

    def save(self, *args, **kwargs):
        """Save method for PublisherLink."""
        old = PublisherLink.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip()

        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for PublisherLink."""
        return reverse('renpy_app:publisher_link_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here

########################################################################################################    Modelo para DeveloperImage
class DeveloperImage(models.Model):
    """Model definition for DeveloperImage."""
    developer = models.ForeignKey(Developer, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='developers_as_images', on_delete=models.CASCADE, verbose_name=_('Desarrollador'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='developers_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=developer_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for DeveloperImage."""
        verbose_name = _('Imagen Desarrollador')
        verbose_name_plural = _('Imágenes Desarrolladores')
        ordering = ['developer', 'size_image', 'name',]
        unique_together = (('developer', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of DeveloperImage."""
        return self.name if self.developer else _('Imagen sin Desarrollador')

    def save(self, *args, **kwargs):
        """Save method for DeveloperImage."""
        old = DeveloperImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for DeveloperImage."""
        return reverse('renpy_app:developer_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.developer:
            return self.developer.name
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

########################################################################################################    Modelo para DeveloperImageExtra
class DeveloperImageExtra(models.Model):
    """Model definition for DeveloperImageExtra."""
    developer = models.ForeignKey(Developer, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='developers_as_images_extra', on_delete=models.CASCADE, verbose_name=_('Desarrollador'))
    image = models.ImageField(blank=False, null=False, upload_to=developer_image_extra_path, verbose_name=_('Imagen Extra Desarrollador'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for DeveloperImageExtra."""
        verbose_name = _('Imagen Extra Desarrollador')
        verbose_name_plural = _('Imágenes Extra Desarrolladores')
        ordering = ['developer', 'name',]
        unique_together = (('developer', 'name',),)

    def __str__(self):
        """Unicode representation of DeveloperImageExtra."""
        return self.name if self.developer else _('Imagen sin Desarrollador')

    def save(self, *args, **kwargs):
        """Save method for DeveloperImageExtra."""
        old = DeveloperImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for DeveloperImageExtra."""
        return reverse('renpy_app:developer_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.developer:
            return self.developer.name
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

########################################################################################################    Modelo para TranslatorImage
class TranslatorImage(models.Model):
    """Model definition for TranslatorImage."""
    translator = models.ForeignKey(Translator, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='translators_as_images', on_delete=models.CASCADE, verbose_name=_('Traductor'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='translators_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=translator_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TranslatorImage."""
        verbose_name = _('Imagen Traductor')
        verbose_name_plural = _('Imágenes Traductores')
        ordering = ['translator', 'size_image', 'name',]
        unique_together = (('translator', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of TranslatorImage."""
        return self.name if self.translator else _('Imagen sin Traductor')

    def save(self, *args, **kwargs):
        """Save method for TranslatorImage."""
        old = TranslatorImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for TranslatorImage."""
        return reverse('renpy_app:translator_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.translator:
            return self.translator.full_name
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

########################################################################################################    Modelo para TranslatorImageExtra
class TranslatorImageExtra(models.Model):
    """Model definition for TranslatorImageExtra."""
    translator = models.ForeignKey(Translator, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='translators_as_images_extra', on_delete=models.CASCADE, verbose_name=_('Traductor'))
    image = models.ImageField(blank=False, null=False, upload_to=translator_image_extra_path, verbose_name=_('Imagen Extra Traductor'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TranslatorImageExtra."""
        verbose_name = _('Imagen Extra Traductor')
        verbose_name_plural = _('Imágenes Extra Traductores')
        ordering = ['translator', 'name',]
        unique_together = (('translator', 'name',),)

    def __str__(self):
        """Unicode representation of TranslatorImageExtra."""
        return self.name if self.translator else _('Imagen sin Traductor')

    def save(self, *args, **kwargs):
        """Save method for TranslatorImageExtra."""
        old = TranslatorImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for TranslatorImageExtra."""
        return reverse('renpy_app:translator_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.translator:
            return self.translator.name
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

########################################################################################################    Modelo para PublisherImage
class PublisherImage(models.Model):
    """Model definition for PublisherImage."""
    publisher = models.ForeignKey(Publisher, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='publishers_as_images', on_delete=models.CASCADE, verbose_name=_('Editor'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='publishers_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=publisher_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PublisherImage."""
        verbose_name = _('Imagen Editor')
        verbose_name_plural = _('Imágenes Editores')
        ordering = ['publisher', 'size_image', 'name',]
        unique_together = (('publisher', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of PublisherImage."""
        return self.name if self.publisher else _('Imagen sin Editor')

    def save(self, *args, **kwargs):
        """Save method for PublisherImage."""
        old = PublisherImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for PublisherImage."""
        return reverse('renpy_app:publisher_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.publisher:
            return self.publisher.name
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

########################################################################################################    Modelo para PublisherImageExtra
class PublisherImageExtra(models.Model):
    """Model definition for PublisherImageExtra."""
    publisher = models.ForeignKey(Publisher, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='publishers_as_images_extra', on_delete=models.CASCADE, verbose_name=_('Editor'))
    image = models.ImageField(blank=False, null=False, upload_to=publisher_image_extra_path, verbose_name=_('Imagen Extra Editor'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PublisherImageExtra."""
        verbose_name = _('Imagen Extra Editor')
        verbose_name_plural = _('Imágenes Extra Editores')
        ordering = ['publisher', 'name',]
        unique_together = (('publisher', 'name',),)

    def __str__(self):
        """Unicode representation of PublisherImageExtra."""
        return self.name if self.publisher else _('Imagen sin Editor')

    def save(self, *args, **kwargs):
        """Save method for PublisherImageExtra."""
        old = PublisherImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for PublisherImageExtra."""
        return reverse('renpy_app:publisher_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.publisher:
            return self.publisher.name
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

########################################################################################################    TitleGame
class TitleGame(models.Model):
    """Model definition for TitleGame."""
    game = models.ForeignKey(Game, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='titles_as_games', on_delete=models.CASCADE, verbose_name=_('Juego'))
    language = models.ForeignKey(Language, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='titles_games_as_languages', on_delete=models.CASCADE, verbose_name=_('Lenguaje'))
    title = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TitleGame."""
        verbose_name = 'Título Juego'
        verbose_name_plural = 'Títulos Juego'
        ordering = ['language', 'title',]
        unique_together = (('language', 'title', 'game',),)

    def __str__(self):
        """Unicode representation of TitleGame."""
        return f"{self.language.name} - {self.title}"

    def save(self, *args, **kwargs):
        """Save method for TitleGame."""
        old = TitleGame.objects.filter(pk=self.pk).first() if self.pk else None

        if self.title:
            self.title = self.title.strip()

        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for TitleGame."""
        return reverse('renpy_app:title_game_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.game:
            return self.game.title
        return None

########################################################################################################    F95GameFetchStatus
class F95GameFetchStatus(models.Model):
    """Model definition for F95GameFetchStatus."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    f95_id = models.IntegerField(verbose_name=_('ID F95Zone'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALPersonPicturesFetchStatus."""
        verbose_name = _('Estado de obtención de juego (F95)')
        verbose_name_plural = _('Estados de obtención de juegos (F95)')
        ordering = ['-created_at', 'f95_id',]
        unique_together = (('f95_id', 'url', 'status',),)

    def __str__(self):
        """Unicode representation of F95GameFetchStatus."""
        return f"{self.f95_id} - {self.status}"
