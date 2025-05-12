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
from apps.music.models import Artist
from core.utils.utils import BaseLog, obtener_inicial, YearField
from .utils.uploads import anime_image_path, anime_image_extra_path, manga_image_path, manga_image_extra_path, character_image_path, character_image_extra_path, otaku_person_image_path, otaku_person_image_extra_path

# Create your models here.
########################################################################################################    Log
class OtakuLog(BaseLog):
    """Model definition for OtakuLog."""
    class Meta:
        """Definición de meta datos para OtakuLog."""
        verbose_name = _('Log Otaku')
        verbose_name_plural = _('Logs Otaku')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Otaku'

########################################################################################################    Modelo para Role
class Role(models.Model):
    """Model definition for Role."""
    name = models.CharField(max_length=40, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=40, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=40, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    role_staff = models.BooleanField(default=False, verbose_name=_('Rol Personal'))
    role_chara = models.BooleanField(default=False, verbose_name=_('Rol Personaje'))
    role_manga = models.BooleanField(default=False, verbose_name=_('Rol Mangas'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Role."""
        verbose_name = _('Rol')
        verbose_name_plural = _('Roles')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp', 'role_staff', 'role_chara', 'role_manga',),)

    def __str__(self):
        """Unicode representation of Role."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Role."""
        # Obtener el objeto original si existe
        old = Role.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Role."""
        return reverse('otaku_app:role_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_movie_staff(self):
        return self.persons_as_movie_staff_roles.count()

    def get_num_movie_cast(self):
        return self.persons_as_movie_cast_roles.count()

########################################################################################################    Modelo para Year
class Year(models.Model):
    """Model definition for Year."""
    year = YearField(blank=False, null=False, verbose_name=_('Año'))
    slug = models.SlugField(max_length=6, unique=True, null=False, blank=True, editable=False, verbose_name=_('Año Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Year."""
        verbose_name = 'Año'
        verbose_name_plural = 'Años'
        ordering = ['-year',]
        unique_together = (('year',),)

    def __str__(self):
        """Unicode representation of Year."""
        return str(self.year)

    def save(self, *args, **kwargs):
        """Save method for Year."""
        # Obtener el objeto original si existe
        old = Year.objects.filter(pk=self.pk).first() if self.pk else None

        year_str=str(self.year)

        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and year_str != str(old.year)):
            self.slug = slugify(year_str)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Year."""
        return reverse('otaku_app:year_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_years.count()

    def get_num_mangas(self):
        return self.mangas_as_years.count()

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
        return reverse('otaku_app:genre_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_genre.count()

    def get_num_mangas(self):
        return self.mangas_as_genre.count()

########################################################################################################    Modelo para Theme
class Theme(models.Model):
    """Model definition for Theme."""
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
        """Meta definition for Theme."""
        verbose_name = _('Tema')
        verbose_name_plural = _('Temas')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Theme."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Theme."""
        old = Theme.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Theme."""
        return reverse('otaku_app:theme_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_theme.count()

    def get_num_mangas(self):
        return self.mangas_as_theme.count()

########################################################################################################    Modelo para Demographic
class Demographic(models.Model):
    """Model definition for Demographic."""
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
        """Meta definition for Demographic."""
        verbose_name = _('Demografía')
        verbose_name_plural = _('Demografías')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Demographic."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Demographic."""
        old = Demographic.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Demographic."""
        return reverse('otaku_app:demographic_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_demographic.count()

    def get_num_mangas(self):
        return self.mangas_as_demographic.count()

########################################################################################################    Modelo para Type
class Type(models.Model):
    """Model definition for Type."""
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'is_active': True}, related_name='childrens', on_delete=models.CASCADE, verbose_name=_('Padre'))
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Type."""
        verbose_name = _('Tipo')
        verbose_name_plural = _('Tipos')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Type."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Type."""
        old = Type.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Type."""
        return reverse('otaku_app:type_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_types.count()

    def get_num_mangas(self):
        return self.mangas_as_types.count()

########################################################################################################    Modelo para Rating
class Rating(models.Model):
    """Model definition for Rating."""
    acronym = models.CharField(max_length=5, unique=True, null=False, blank=False, verbose_name=_('Acrónimo'))
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    # initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Rating."""
        verbose_name = _('Clasificación')
        verbose_name_plural = _('Clasificaciones')
        ordering = ['acronym', 'name',]
        unique_together = (('acronym', 'name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Rating."""
        return (f'{self.acronym} - {self.name}')

    def save(self, *args, **kwargs):
        """Save method for Rating."""
        old = Rating.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del names
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Normalización del acronym
        if self.acronym:
            self.acronym = self.acronym.strip().upper()
        # Inicial automática si está acronym
        if not self.acronym:
            self.acronym = self._generate_acronym(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Rating."""
        return reverse('otaku_app:rating_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_ratings.count()

########################################################################################################    Modelo para Season
class Season(models.Model):
    """Model definition for Season."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Season."""
        verbose_name = _('Temporada')
        verbose_name_plural = _('Temporadas')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Season."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Season."""
        # Obtener el objeto original si existe
        old = Season.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Rating."""
        return reverse('otaku_app:season_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_seasons.count()

    def get_num_mangas(self):
        return self.mangas_as_seasons.count()

########################################################################################################    Modelo para Status
class Status(models.Model):
    """Model definition for Status."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Status."""
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Status."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Status."""
        # Obtener el objeto original si existe
        old = Status.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Status."""
        return reverse('otaku_app:status_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_status.count()

    def get_num_mangas(self):
        return self.mangas_as_status.count()

########################################################################################################    Modelo para Source
class Source(models.Model):
    """Model definition for Source."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Source."""
        verbose_name = _('Fuente')
        verbose_name_plural = _('Fuentes')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Source."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Source."""
        # Obtener el objeto original si existe
        old = Source.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Source."""
        return reverse('otaku_app:source_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_sources.count()

########################################################################################################    Modelo para RelationType
class RelationType(models.Model):
    """Model definition for RelationType."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for RelationType."""
        verbose_name = _('Tipo Relación')
        verbose_name_plural = _('Tipos Relaciones')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of RelationType."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for RelationType."""
        # Obtener el objeto original si existe
        old = RelationType.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for RelationType."""
        return reverse('otaku_app:relation_type_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def count_relations(self):
        """Cuenta cuántas veces se ha utilizado este tipo de relación en MediaRelation."""
        return self.mediarelation_set.count()

########################################################################################################    Modelo para SeasonFull
class SeasonFull(models.Model):
    """Model definition for SeasonFull."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SeasonFull."""
        verbose_name = _('Temporada Completa')
        verbose_name_plural = _('Temporadas Completas')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of SeasonFull."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for SeasonFull."""
        # Obtener el objeto original si existe
        old = SeasonFull.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for SeasonFull."""
        return reverse('otaku_app:season_full_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_season_fulls.count()

    def get_num_mangas(self):
        return self.mangas_as_season_fulls.count()

########################################################################################################    Modelo para Producer
class Producer(models.Model):
    """Model definition for Producer."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Producer."""
        verbose_name = _('Productora')
        verbose_name_plural = _('Productoras')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Producer."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Producer."""
        old = Producer.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Producer."""
        return reverse('otaku_app:producer_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_producers.count()

########################################################################################################    Modelo para Licensor
class Licensor(models.Model):
    """Model definition for Licensor."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Licensor."""
        verbose_name = _('Licenciante')
        verbose_name_plural = _('Licenciantes')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Licensor."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Licensor."""
        old = Licensor.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Licensor."""
        return reverse('otaku_app:licensor_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_licensors.count()

########################################################################################################    Modelo para Studio
class Studio(models.Model):
    """Model definition for Studio."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Studio."""
        verbose_name = _('Estudio')
        verbose_name_plural = _('Estudios')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Studio."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Studio."""
        old = Studio.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Studio."""
        return reverse('otaku_app:studio_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_animes(self):
        return self.animes_as_studios.count()

########################################################################################################    Modelo para Serialization
class Serialization(models.Model):
    """Model definition for Serialization."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Serialization."""
        verbose_name = _('Serializadora')
        verbose_name_plural = _('Serializadoras')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Serialization."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Serialization."""
        old = Serialization.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Serialization."""
        return reverse('otaku_app:serialization_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_mangas(self):
        return self.mangas_as_serializations.count()

########################################################################################################    Modelo para Anime
class Anime(models.Model):
    """Model definition for Anime."""
    title = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Título'))
    title_eng = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Título Ingles'))
    title_jap = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Título Japones'))
    episodes = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('Episodios'))
    from_date = models.DateField(blank=True, null=True, verbose_name=_('Desde'))
    to_date = models.DateField(blank=True, null=True, verbose_name=_('Hasta'))
    synopsis = models.TextField(blank=True, verbose_name=_('Sinopsis'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    # Datos FK
    anime_type = models.ForeignKey(Type, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_type', on_delete=models.SET_NULL, verbose_name=_('Tipo'))
    status = models.ForeignKey(Status, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_status', on_delete=models.SET_NULL, verbose_name=_('Estado'))
    season = models.ForeignKey(Season, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_seasons', on_delete=models.SET_NULL, verbose_name=_('Temporada'))
    season_full = models.ForeignKey(SeasonFull, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_season_fulls', on_delete=models.SET_NULL, verbose_name=_('Temporada Año'))
    year = models.ForeignKey(Year, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_years', on_delete=models.SET_NULL, verbose_name=_('Año'))
    source = models.ForeignKey(Source, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_sources', on_delete=models.SET_NULL, verbose_name=_('Fuente'))
    rating = models.ForeignKey(Rating, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='animes_as_ratings', on_delete=models.SET_NULL, verbose_name=_('Clasificación'))
    # Datos ManyToMany
    producers = models.ManyToManyField(Producer, blank=True, limit_choices_to={'is_active': True}, related_name='animes_as_producers', verbose_name=_('Productoras'))
    licensors = models.ManyToManyField(Licensor, blank=True, limit_choices_to={'is_active': True}, related_name='animes_as_licensors', verbose_name=_('Licenciantes'))
    studios = models.ManyToManyField(Studio, blank=True, limit_choices_to={'is_active': True}, related_name='animes_as_studios', verbose_name=_('Estudios'))
    genres = models.ManyToManyField(Genre, blank=True, limit_choices_to={'is_active': True}, related_name='animes_as_genre', verbose_name=_('Géneros'))
    themes = models.ManyToManyField(Theme, blank=True, limit_choices_to={'is_active': True}, related_name='animes_as_theme', verbose_name=_('Temas'))
    demographics = models.ManyToManyField(Demographic, blank=True, limit_choices_to={'is_active': True}, related_name='animes_as_demographic', verbose_name=_('Demografías'))
    # Datos MAL
    url = models.URLField(max_length=20000, blank=False, null=False, verbose_name=_('URL MyAnimeList'))
    mal_id = models.IntegerField(unique=True, null=False, blank=False, default=0, verbose_name=_('ID MyAnimesList'))
    p_mal_id = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name=_('ID MyAnimesList Prefijo'))
    # Datos Base
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Anime."""
        verbose_name = _('Anime')
        verbose_name_plural = _('Animes')
        ordering = ['-created_at', 'title',]
        unique_together = (('mal_id', 'url', 'title',),)

    def __str__(self):
        """Unicode representation of Anime."""
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Anime."""
        # Obtener el objeto original si existe
        old = Anime.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.title:
            self.title = self.title.strip()
        if self.title_eng:
            self.title_eng = self.title_eng.strip()
        if self.title_jap:
            self.title_jap = self.title_jap.strip()

        # Generar p_mal_id automáticamente
        if not self.p_mal_id:
            base_id = f"A{self.mal_id}"
            suffix = ''
            i = 1
            while Anime.objects.filter(p_mal_id=base_id + suffix).exclude(pk=self.pk).exists():
                suffix = f"_{i}"
                i += 1
            self.p_mal_id = base_id + suffix

        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Anime."""
        return reverse('otaku_app:anime_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods - Funciones Campos Directas
    def get_active(self):
        return self.is_active

    def get_url(self):
        return self.url

    def get_created(self):
        return self.created_at.strftime("%d %b del %Y")

    def get_updated(self):
        return self.updated_at.strftime("%d %b del %Y")

    def get_synopsis(self):
        return self.synopsis if self.synopsis else _('Sin sinopsis disponible')

    def get_episodios(self):
        return str(self.episodes or 0)

    def get_mal_id(self):
        return str(self.mal_id or 0)

    def get_aired(self):
        if self.from_date and self.to_date:
            return f"{self.from_date:%b %d, %Y} - {self.to_date:%b %d, %Y}"
        if self.from_date:
            return f"{self.from_date:%b %d, %Y} - ??"
        if self.to_date:
            return f"?? - {self.to_date:%b %d, %Y}"
        return _('Fecha Emisión no disponible')

    # custom methods - Funciones Campos FK
    def get_type(self):
        return self.anime_type.name if self.anime_type else _('Sin Tipo')

    def get_status(self):
        return self.status.name if self.status else _('Sin Estado')

    def get_season(self):
        return self.season.name if self.season else _('Sin Temporada de Emisión')

    def get_season_full(self):
        return self.season_full.name if self.season_full else _('Sin Temporada Completa de Emisión')

    def get_year(self):
        return self.year.year if self.year else _('Sin Año')

    def get_source(self):
        return self.source.name if self.source else _('Sin Fuente')

    def get_rating(self):
        return self.rating.name if self.rating else _('Sin Clasificación')

    # custom methods - Funciones Campos ManyToMany
    def get_producers(self):
        return [{"id": p.id, "name": p.name} for p in self.producers.all()]

    def get_licensors(self):
        return [{"id": l.id, "name": l.name} for l in self.licensors.all()]

    def get_studios(self):
        return [{"id": s.id, "name": s.name} for s in self.studios.all()]

    def get_genres(self):
        return [{"id": g.id, "name": g.name} for g in self.genres.all()]

    def get_themes(self):
        return [{"id": t.id, "name": t.name} for t in self.themes.all()]

    def get_demographics(self):
        return [{"id": d.id, "name": d.name} for d in self.demographics.all()]

    # custom methods - Tablas Intermedias
    def get_titles_grouped_by_lang(self):
        titles_grouped_by_lang = {}
        titles = self.animes_as_title.filter(is_active=True).select_related('title_lang')

        for title_obj in titles:
            lang_name = title_obj.title_lang.name if title_obj.title_lang else _('Desconocido')

            if lang_name not in titles_grouped_by_lang:
                titles_grouped_by_lang[lang_name] = []

            titles_grouped_by_lang[lang_name].append(title_obj.title)

        return titles_grouped_by_lang

    def get_characters_count(self):
        return self.anime_characters.count()

    def get_main_characters_with_voices(self):
        personajes = self.anime_characters.filter(role__iexact='Main')
        data = []

        for personaje in personajes:
            character = personaje.character

            # Imagen del personaje (normal)
            character_image = character.character_images.filter(
                is_active=True,
                size_image__name__iexact='normal'
            ).first()
            character_image_url = character_image.image.url if character_image and character_image.image else None

            # Actores de voz en japonés para este personaje en este anime
            voice_actors = character.voice_roles.filter(
                anime=self,
                language__iexact='Japanese'
            )

            voces = []
            for va in voice_actors:
                person = va.person
                if person:
                    # Imagen del actor de voz (normal)
                    person_image = person.person_images.filter(
                        is_active=True,
                        size_image__name__iexact='normal'
                    ).first()
                    person_image_url = person_image.image.url if person_image and person_image.image else None
                else:
                    person_image_url = None

                voces.append({
                    'full_name': person.full_name if person else None,
                    'language': va.language,
                    'image': person_image_url
                })

            data.append({
                'full_name': character.full_name,
                'role': personaje.role,
                'image': character_image_url,
                'voice_actors': voces
            })

        return data

    def get_all_characters_with_voices(self):
        personajes = self.anime_characters.all()
        data = []

        for personaje in personajes:
            character = personaje.character

            # Obtiene imagen del personaje (normal)
            character_image = character.character_images.filter(
                is_active=True,
                size_image__name__iexact='normal'
            ).first()
            character_image_url = character_image.image.url if character_image and character_image.image else None

            # Actores de voz para este personaje en este anime
            voice_actors = character.voice_roles.filter(anime=self)

            voces = []
            for va in voice_actors:
                person = va.person
                if person:
                    # Obtiene imagen del actor de voz (normal)
                    person_image = person.person_images.filter(
                        is_active=True,
                        size_image__name__iexact='normal'
                    ).first()
                    person_image_url = person_image.image.url if person_image and person_image.image else None
                else:
                    person_image_url = None

                voces.append({
                    'full_name': person.full_name if person else None,
                    'language': va.language,
                    'image': person_image_url
                })

            data.append({
                'full_name': character.full_name,
                'role': personaje.role,
                'image': character_image_url,
                'voice_actors': voces
            })

        return data

    def get_image_urls(self):
        """
        Devuelve una lista combinada de todas las URLs de imágenes de un anime,
        incluyendo portadas clasificadas por tamaño y otras imágenes extra.
        """
        # === Portadas desde AnimeImage ===
        images = self.animes_as_images.filter(is_active=True)
        cover_urls = [None, None]  # Índices: 0 = normal, 1 = large
        extra_urls = []

        for img in images:
            url = img.image.url if img.image else img.image_url
            if not url:
                continue

            size_name = img.size_image.name.lower()
            if size_name == 'large':
                cover_urls[1] = url
            elif size_name == 'normal':
                cover_urls[0] = url
            else:
                extra_urls.append(url)

        # === Imágenes extra desde AnimeImageExtra ===
        extras = self.animes_as_extra_images.filter(is_active=True)
        for extra in extras:
            if extra.image:
                extra_urls.append(extra.image.url)

        # Limpieza y retorno
        return [u for u in cover_urls if u] + extra_urls

########################################################################################################    Modelo para Manga
class Manga(models.Model):
    """Model definition for Manga."""
    title = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Título'))
    title_eng = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Título Ingles'))
    title_jap = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Título Japones'))
    chapters = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('Capítulos'))
    volumes = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('volúmenes'))
    synopsis = models.TextField(blank=True, verbose_name=_('Sinopsis'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    # Datos FK
    manga_type = models.ForeignKey(Type, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_types', on_delete=models.SET_NULL, verbose_name=_('Tipo'))
    year = models.ForeignKey(Year, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_years', on_delete=models.SET_NULL, verbose_name=_('Año'))
    status = models.ForeignKey(Status, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_status', on_delete=models.SET_NULL, verbose_name=_('Estado'))
    season = models.ForeignKey(Season, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_seasons', on_delete=models.SET_NULL, verbose_name=_('Temporada'))
    season_full = models.ForeignKey(SeasonFull, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_season_fulls', on_delete=models.SET_NULL, verbose_name=_('Temporada Año'))
    source = models.ForeignKey(Source, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_sources', on_delete=models.SET_NULL, verbose_name=_('Fuente'))
    rating = models.ForeignKey(Rating, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='mangas_as_ratings', on_delete=models.SET_NULL, verbose_name=_('Clasificación'))
    # Datos ManyToMany
    serializations = models.ManyToManyField(Serialization, blank=True, limit_choices_to={'is_active': True}, related_name='mangas_as_serializations', verbose_name=_('Serializadoras'))
    genres = models.ManyToManyField(Genre, blank=True, limit_choices_to={'is_active': True}, related_name='mangas_as_genre', verbose_name=_('Géneros'))
    themes = models.ManyToManyField(Theme, blank=True, limit_choices_to={'is_active': True}, related_name='mangas_as_theme', verbose_name=_('Temas'))
    demographics = models.ManyToManyField(Demographic, blank=True, limit_choices_to={'is_active': True}, related_name='mangas_as_demographic', verbose_name=_('Demografías'))
    published_from = models.DateField(blank=True, null=True, verbose_name=_('Publicado Desde'))
    published_to = models.DateField(blank=True, null=True, verbose_name=_('Publicado Hasta'))
    # Datos MAL
    url = models.URLField(max_length=20000, blank=False, null=False, verbose_name=_('URL MyAnimeList'))
    mal_id = models.IntegerField(unique=True, null=False, blank=False, default=0, verbose_name=_('ID MyAnimesList'))
    p_mal_id = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name=_('ID MyAnimesList Prefijo'))
    # Datos Base
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Manga."""
        verbose_name = _('Manga')
        verbose_name_plural = _('Mangas')
        ordering = ['-created_at', 'title',]
        unique_together = (('mal_id', 'url', 'title',),)

    def __str__(self):
        """Unicode representation of Manga."""
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Manga."""
        # Obtener el objeto original si existe
        old = Manga.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.title:
            self.title = self.title.strip()
        if self.title_eng:
            self.title_eng = self.title_eng.strip()
        if self.title_jap:
            self.title_jap = self.title_jap.strip()

        # Generar p_mal_id automáticamente
        if not self.p_mal_id:
            base_id = f"M{self.mal_id}"
            suffix = ''
            i = 1
            while Manga.objects.filter(p_mal_id=base_id + suffix).exclude(pk=self.pk).exists():
                suffix = f"_{i}"
                i += 1
            self.p_mal_id = base_id + suffix

        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Manga."""
        return reverse('otaku_app:manga_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods - Funciones Campos Directas
    def get_active(self):
        return self.is_active

    def get_url(self):
        return self.url

    def get_created(self):
        return self.created_at.strftime("%d %b del %Y")

    def get_updated(self):
        return self.updated_at.strftime("%d %b del %Y")

    def get_synopsis(self):
        return self.synopsis if self.synopsis else _('Sin sinopsis disponible')

    def get_chapters(self):
        return str(self.chapters or 0)

    def get_volumes(self):
        return str(self.volumes or 0)

    def get_mal_id(self):
        return str(self.mal_id or 0)

    def get_published(self):
        if self.published_from and self.published_to:
            return f"{self.published_from:%b %d, %Y} - {self.published_to:%b %d, %Y}"
        if self.published_from:
            return f"{self.published_from:%b %d, %Y} - ??"
        if self.published_to:
            return f"?? - {self.published_to:%b %d, %Y}"
        return _('Fecha publicación no disponible')

    # custom methods - Funciones Campos FK
    def get_type(self):
        return self.manga_type.name if self.manga_type else _('Sin Tipo')

    def get_status(self):
        return self.status.name if self.status else _('Sin Estado')

    def get_season(self):
        return self.season.name if self.season else _('Sin Temporada de Emisión')

    def get_season_full(self):
        return self.season_full.name if self.season_full else _('Sin Temporada Completa de Emisión')

    def get_year(self):
        return self.year.year if self.year else _('Sin Año')

    def get_source(self):
        return self.source.name if self.source else _('Sin Fuente')

    def get_rating(self):
        return self.rating.name if self.rating else _('Sin Clasificación')

    # custom methods - Funciones Campos ManyToMany
    def get_serializations(self):
        return [{"id": s.id, "name": s.name} for s in self.serializations.all()]

    def get_genres(self):
        return [{"id": g.id, "name": g.name} for g in self.genres.all()]

    def get_themes(self):
        return [{"id": t.id, "name": t.name} for t in self.themes.all()]

    def get_demographics(self):
        return [{"id": d.id, "name": d.name} for d in self.demographics.all()]

    # custom methods - Tablas Intermedias
    def get_titles_grouped_by_lang(self):
        titles_grouped_by_lang = {}
        titles = self.mangas_as_title.filter(is_active=True).select_related('title_lang')

        for title_obj in titles:
            lang_name = title_obj.title_lang.name if title_obj.title_lang else _('Desconocido')

            if lang_name not in titles_grouped_by_lang:
                titles_grouped_by_lang[lang_name] = []

            titles_grouped_by_lang[lang_name].append(title_obj.title)

        return titles_grouped_by_lang

    def get_characters_count(self):
        return self.manga_characters.count()

    def get_characters(self):
        personajes = self.manga_characters.all()

        data = []
        for personaje in personajes:
            character = personaje.character

            # Obtener imagen del personaje (normal)
            character_image = character.character_images.filter(
                is_active=True,
                size_image__name__iexact='normal'
            ).first()
            character_image_url = character_image.image.url if character_image and character_image.image else None

            data.append({
                'full_name': character.full_name,
                'role': personaje.role,
                'image': character_image_url,
            })

        return data

    def get_main_characters(self):
        personajes = self.manga_characters.filter(role__iexact='Main')

        data = []
        for personaje in personajes:
            character = personaje.character

            # Obtener imagen del personaje (normal)
            character_image = character.character_images.filter(
                is_active=True,
                size_image__name__iexact='normal'
            ).first()
            character_image_url = character_image.image.url if character_image and character_image.image else None

            data.append({
                'full_name': character.full_name,
                'role': personaje.role,
                'image': character_image_url,
            })

        return data

    def get_image_urls(self):
        """
        Devuelve una lista combinada de todas las URLs de imágenes de un anime,
        incluyendo portadas clasificadas por tamaño y otras imágenes extra.
        """
        # === Portadas desde AnimeImage ===
        images = self.mangas_as_images.filter(is_active=True)
        cover_urls = [None, None]  # Índices: 0 = normal, 1 = large
        extra_urls = []

        for img in images:
            url = img.image.url if img.image else img.image_url
            if not url:
                continue

            size_name = img.size_image.name.lower()
            if size_name == 'large':
                cover_urls[1] = url
            elif size_name == 'normal':
                cover_urls[0] = url
            else:
                extra_urls.append(url)

        # === Imágenes extra desde AnimeImageExtra ===
        extras = self.mangas_as_extra_images.filter(is_active=True)
        for extra in extras:
            if extra.image:
                extra_urls.append(extra.image.url)

        # Limpieza y retorno
        return [u for u in cover_urls if u] + extra_urls

########################################################################################################    Modelo para TitleAnime
class TitleAnime(models.Model):
    """Model definition for TitleAnime."""
    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='animes_as_title', on_delete=models.CASCADE, verbose_name=_('Anime'))
    title_lang = models.ForeignKey(Language, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='titles_animes_as_languages', on_delete=models.CASCADE, verbose_name=_('Lenguaje'))
    title = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TitleAnime."""
        verbose_name = _('Título Anime')
        verbose_name_plural = _('Títulos Anime')
        ordering = ['anime', 'title_lang', 'initial', 'title',]
        unique_together = (('anime', 'title_lang', 'title',),)

    def __str__(self):
        """Unicode representation of TitleAnime."""
        return f'{self.anime.title} - A.k.a {self.title} ({self.title_lang.name})'

    def save(self, *args, **kwargs):
        """Save method for TitleAnime."""
        old = TitleAnime.objects.filter(pk=self.pk).first() if self.pk else None

        if self.title:
            self.title = self.title.strip()

        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for TitleAnime."""
        return reverse('otaku_app:title_anime_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.anime:
            return self.anime.title
        return None

########################################################################################################    Modelo para TitleManga
class TitleManga(models.Model):
    """Model definition for TitleManga."""
    manga = models.ForeignKey(Manga, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='mangas_as_title', on_delete=models.CASCADE, verbose_name=_('Manga'))
    title_lang = models.ForeignKey(Language, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='titles_mangas_as_languages', on_delete=models.CASCADE, verbose_name=_('Lenguaje'))
    title = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TitleManga."""
        verbose_name = _('Título Manga')
        verbose_name_plural = _('Títulos Manga')
        ordering = ['manga', 'title_lang', 'initial', 'title',]
        unique_together = (('manga', 'title_lang', 'title',),)

    def __str__(self):
        """Unicode representation of TitleManga."""
        return f'{self.manga.title} - A.k.a {self.title} ({self.title_lang.name})'

    def save(self, *args, **kwargs):
        """Save method for TitleManga."""
        old = TitleManga.objects.filter(pk=self.pk).first() if self.pk else None

        if self.title:
            self.title = self.title.strip()

        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for TitleManga."""
        return reverse('otaku_app:title_manga_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.manga:
            return self.manga.title
        return None

########################################################################################################    Modelo para Character
class Character(models.Model):
    """Model definition for Character."""
    full_name = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Nombre Completo'))
    name_kanji = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Nombre Kanji'))
    biography = models.TextField(blank=True, verbose_name=_('Biografía'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    # Datos MAL
    url = models.URLField(max_length=20000, blank=False, null=False, verbose_name=_('URL MyAnimeList'))
    mal_id = models.IntegerField(unique=True, null=False, blank=False, default=0, verbose_name=_('ID MyAnimesList'))
    p_mal_id = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name=_('ID MyAnimesList Prefijo'))
    # Datos Base
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Character."""
        verbose_name = _('Personaje')
        verbose_name_plural = _('Personajes')
        ordering = ['-created_at', 'initial','full_name',]
        unique_together = (('mal_id', 'initial', 'full_name', 'url',),)

    def __str__(self):
        """Unicode representation of Character."""
        return self.full_name

    def save(self, *args, **kwargs):
        """Save method for Character."""
        # Obtener el objeto original si existe
        old = Character.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.full_name:
            self.full_name = self.full_name.strip()
        # Generar p_mal_id automáticamente
        if not self.p_mal_id:
            base_id = f"C{self.mal_id}"
            suffix = ''
            i = 1
            while Character.objects.filter(p_mal_id=base_id + suffix).exclude(pk=self.pk).exists():
                suffix = f"_{i}"
                i += 1
            self.p_mal_id = base_id + suffix

        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Character."""
        return reverse('otaku_app:character_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here
    def get_image_urls(self):
        """
        Devuelve una lista combinada de todas las URLs de imágenes de un anime,
        incluyendo portadas clasificadas por tamaño y otras imágenes extra.
        """
        # === Portadas desde AnimeImage ===
        images = self.characters_as_images.filter(is_active=True)
        cover_urls = [None, None]  # Índices: 0 = normal, 1 = large
        extra_urls = []

        for img in images:
            url = img.image.url if img.image else img.image_url
            if not url:
                continue

            size_name = img.size_image.name.lower()
            if size_name == 'large':
                cover_urls[1] = url
            elif size_name == 'normal':
                cover_urls[0] = url
            else:
                extra_urls.append(url)

        # === Imágenes extra desde AnimeImageExtra ===
        extras = self.characters_as_extra_images.filter(is_active=True)
        for extra in extras:
            if extra.image:
                extra_urls.append(extra.image.url)

        # Limpieza y retorno
        return [u for u in cover_urls if u] + extra_urls

########################################################################################################    Modelo para CharacterNickname
class CharacterNickname(models.Model):
    """Model definition for CharacterNickname."""
    character = models.ForeignKey(Character, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='characters_as_nicknames', on_delete=models.CASCADE, verbose_name=_('Personaje'))
    nickname = models.CharField(max_length=100, unique=False, null=False, blank=False, verbose_name=_('Apodo'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=100, unique=False, null=False, blank=True, editable=False, verbose_name=_('Apodo Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for CharacterNickname."""
        verbose_name = _('Apodo Personaje')
        verbose_name_plural = _('Apodos Personajes')
        ordering = ['initial','nickname',]
        unique_together = (('character', 'initial', 'nickname',),)

    def __str__(self):
        """Unicode representation of CharacterNickname."""
        return f"{self.character.full_name} A.k.A ({self.nickname})"

    def save(self, *args, **kwargs):
        """Save method for CharacterNickname."""
        # Obtener el objeto original si existe
        old = CharacterNickname.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nickname
        if self.nickname:
            self.nickname = self.nickname.strip()
        # Obtener inicial solo si está vacía o el nickname cambió
        if not self.initial or (old and self.nickname != old.nickname):
            self.initial = obtener_inicial(self.nickname).upper()
        # Slug automático solo si está vacío o el nickname cambió
        if not self.slug or (old and self.nickname != old.nickname):
            self.slug = slugify(self.nickname)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for CharacterNickname."""
        return reverse('common_app:nickname_character_detail', kwargs={'pk': self.pk, 'slug': self.slug})

########################################################################################################    Modelo para OtakuPerson
class OtakuPerson(models.Model):
    """Model definition for OtakuPerson."""
    full_name = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name=_('Nombre Completo'))
    name_kanji = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Nombre Kanji'))
    biography = models.TextField(blank=True, verbose_name=_('Biografía'))
    slug = models.SlugField(max_length=20000, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_('Fecha Nacimiento'))
    voice_actor = models.BooleanField(default=False, verbose_name='Actor de voz')
    author = models.BooleanField(default=False, verbose_name='Autor')
    staff = models.BooleanField(default=False, verbose_name='Staff Anime')
    # Datos MAL
    url = models.URLField(max_length=20000, blank=False, null=False, verbose_name=_('URL MyAnimeList'))
    mal_id = models.IntegerField(unique=True, null=False, blank=False, default=0, verbose_name=_('ID MyAnimesList'))
    p_mal_id = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name=_('ID MyAnimesList Prefijo'))
    # Datos Base
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for OtakuPerson."""
        verbose_name = _(' Persona')
        verbose_name_plural = _('Personas')
        ordering = ['-created_at', 'initial','full_name',]
        unique_together = (('mal_id', 'initial', 'full_name', 'url',),)

    def __str__(self):
        """Unicode representation of OtakuPerson."""
        return self.full_name

    def save(self, *args, **kwargs):
        """Save method for OtakuPerson."""
        # Obtener el objeto original si existe
        old = OtakuPerson.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.full_name:
            self.full_name = self.full_name.strip()
        # Generar p_mal_id automáticamente
        if not self.p_mal_id:
            base_id = f"P{self.mal_id}"
            suffix = ''
            i = 1
            while OtakuPerson.objects.filter(p_mal_id=base_id + suffix).exclude(pk=self.pk).exists():
                suffix = f"_{i}"
                i += 1
            self.p_mal_id = base_id + suffix

        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for OtakuPerson."""
        return reverse('otaku_app:person_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here
    def get_image_urls(self):
        """
        Devuelve una lista combinada de todas las URLs de imágenes de un anime,
        incluyendo portadas clasificadas por tamaño y otras imágenes extra.
        """
        # === Portadas desde AnimeImage ===
        images = self.otaku_persons_as_images.filter(is_active=True)
        cover_urls = [None, None]  # Índices: 0 = normal, 1 = large
        extra_urls = []

        for img in images:
            url = img.image.url if img.image else img.image_url
            if not url:
                continue

            size_name = img.size_image.name.lower()
            if size_name == 'large':
                cover_urls[1] = url
            elif size_name == 'normal':
                cover_urls[0] = url
            else:
                extra_urls.append(url)

        # === Imágenes extra desde AnimeImageExtra ===
        extras = self.otaku_persons_as_extra_images.filter(is_active=True)
        for extra in extras:
            if extra.image:
                extra_urls.append(extra.image.url)

        # Limpieza y retorno
        return [u for u in cover_urls if u] + extra_urls

########################################################################################################    Modelo para OtakuPersonNickname
class OtakuPersonNickname(models.Model):
    """Model definition for OtakuPersonNickname."""
    person = models.ForeignKey(OtakuPerson, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='otaku_persons_as_nicknames', on_delete=models.CASCADE, verbose_name=_('Persona'))
    nickname = models.CharField(max_length=100, unique=False, null=False, blank=False, verbose_name=_('Apodo'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=100, unique=False, null=False, blank=True, editable=False, verbose_name=_('Apodo Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for OtakuPersonNickname."""
        verbose_name = _('Apodo Persona')
        verbose_name_plural = _('Apodos Persona')
        ordering = ['initial','nickname',]
        unique_together = (('person', 'initial', 'nickname',),)

    def __str__(self):
        """Unicode representation of OtakuPersonNickname."""
        return f"{self.person.full_name} AKA ({self.nickname})"

    def save(self, *args, **kwargs):
        """Save method for OtakuPersonNickname."""
        # Obtener el objeto original si existe
        old = OtakuPersonNickname.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nickname
        if self.nickname:
            self.nickname = self.nickname.strip()
        # Obtener inicial solo si está vacía o el nickname cambió
        if not self.initial or (old and self.nickname != old.nickname):
            self.initial = obtener_inicial(self.nickname).upper()
        # Slug automático solo si está vacío o el nickname cambió
        if not self.slug or (old and self.nickname != old.nickname):
            self.slug = slugify(self.nickname)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for OtakuPersonNickname."""
        return reverse('common_app:nickname_otaku_person_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # TODO: Define custom methods here

########################################################################################################    Modelo para AnimeSong
class AnimeSong(models.Model):
    """Model definition for AnimeSong."""
    SONG_TYPE_CHOICES = [
        ('OP', 'Opening'),
        ('ED', 'Ending'),
        ('IN', 'Insert Song'),
    ]

    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='animes_as_songs', on_delete=models.CASCADE, verbose_name=_('Anime'))
    song_type = models.CharField(max_length=3, blank=False, null=False, choices=SONG_TYPE_CHOICES, verbose_name='Tipo de Canción')
    song_id = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('ID Canción'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    artist = models.ManyToManyField(Artist, blank=True, limit_choices_to={'is_active': True}, related_name='songs_as_artists', verbose_name=_('Artista'))
    slug = models.SlugField(max_length=20000, unique=False, null=True, blank=True, editable=False, verbose_name=_('Título Slug'))
    # Datos CSL
    title = models.CharField(max_length=20000, unique=False, null=True, blank=False, verbose_name=_('Título'))
    title_kanji = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Título Kanji'))
    title_eng = models.CharField(max_length=20000, unique=False, null=True, blank=True, verbose_name=_('Título Ingles'))
    # Datos
    title_full = models.CharField(max_length=20000, unique=False, null=False, blank=False, verbose_name='Título de la Canción Completo')
    # Datos Base
    revisado = models.IntegerField(default=0, verbose_name='Revisado Temporal')
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AnimeSong."""
        verbose_name = _('Canción Anime')
        verbose_name_plural = _('Canciones Anime')
        ordering = ['anime', 'song_type', 'song_id', 'title',]
        unique_together = (('anime', 'song_type', 'song_id', 'title',),)

    def __str__(self):
        """Unicode representation of AnimeSong."""
        return f"{self.anime.title} - {self.get_song_type_display()}{self.song_id} - {self.song_title}"

    def save(self, *args, **kwargs):
        """Save method for AnimeSong."""
        old = AnimeSong.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del title
        if self.title:
            self.title = self.title.strip()
        # Obtener inicial solo si está vacía o el title cambió
        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático solo si está vacío o el title cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for AnimeSong."""
        return reverse('otaku_app:anime_song_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def titulo_a_mostrar(self):
        titulo = self.song_title.strip() if self.song_title else ''

        title_eng = self.title_eng.strip() if self.title_eng else ''
        title_kanji = self.title_kanji.strip() if self.title_kanji else ''

        if title_eng:
            if title_kanji:
                titulo += f" ({title_eng} ({title_kanji}))"
            else:
                titulo += f" ({title_eng})"
        elif title_kanji:
            titulo += f" ({title_kanji})"

        return titulo

########################################################################################################    Modelo para AnimeCharacter
class AnimeCharacter(models.Model):
    """Model definition for AnimeCharacter."""
    character = models.ForeignKey(Character, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='characters_animes', on_delete=models.CASCADE, verbose_name=_('Personaje'))
    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='anime_characters', on_delete=models.CASCADE, verbose_name=_('Anime'))
    role = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True, 'role_chara': True,}, related_name='characters_anime_roles', on_delete=models.CASCADE, verbose_name=_('Rol'))
    # mal ids
    character_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Personaje'))
    anime_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Anime'))
    # Base Data
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AnimeCharacter."""
        verbose_name = _('Personaje Anime')
        verbose_name_plural = _('Personajes Animes')
        ordering = ['character_mal_id','anime_mal_id',]
        unique_together = (('character_mal_id', 'anime_mal_id',),)

    def __str__(self):
        """Unicode representation of AnimeCharacter."""
        pass

########################################################################################################    Modelo para MangaCharacter
class MangaCharacter(models.Model):
    """Model definition for MangaCharacter."""
    character = models.ForeignKey(Character, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='characters_mangas', on_delete=models.CASCADE, verbose_name=_('Personaje'))
    manga = models.ForeignKey(Manga, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='manga_characters', on_delete=models.CASCADE, verbose_name=_('Manga'))
    role = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True, 'role_chara': True,}, related_name='characters_manga_roles', on_delete=models.CASCADE, verbose_name=_('Rol'))
    # mal ids
    character_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Personaje'))
    manga_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Manga'))
    # Base Data
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MangaCharacter."""
        verbose_name = _('Personaje Manga')
        verbose_name_plural = _('Personajes Mangas')
        ordering = ['character_mal_id','manga_mal_id',]
        unique_together = (('character_mal_id', 'manga_mal_id',),)

    def __str__(self):
        """Unicode representation of MangaCharacter."""
        pass

########################################################################################################    Modelo para VoiceCharacter
class VoiceCharacter(models.Model):
    """Model definition for VoiceCharacter."""
    person = models.ForeignKey(OtakuPerson, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='person_voice_roles', on_delete=models.CASCADE, verbose_name=_('Persona'))
    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='voice_characters', on_delete=models.CASCADE, verbose_name=_('Anime'))
    character = models.ForeignKey(Character, blank=False, null=False, limit_choices_to={'is_active': True,}, related_name='character_voice_roles', on_delete=models.CASCADE, verbose_name=_('Personaje'))
    language = models.ForeignKey(Language, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='languages_voice_roles', on_delete=models.CASCADE, verbose_name=_('Idioma'))
    # mal ids
    person_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Persona'))
    anime_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Anime'))
    character_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Personaje'))
    # Base Data
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for VoiceCharacter."""
        verbose_name = _('Actor de Voz')
        verbose_name_plural = _('Actores de Voz')
        ordering = ['anime_mal_id', 'character_mal_id', 'person_mal_id',]
        unique_together = (('person_mal_id', 'character_mal_id', 'anime_mal_id',),)

    def __str__(self):
        """Unicode representation of VoiceCharacter."""
        return f" como {self.character_mal_id} en Anime ID {self.anime_mal_id}"

    # def save(self):
    #     """Save method for VoiceCharacter."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for VoiceCharacter."""
    #     return ('')

    # TODO: Define custom methods here

########################################################################################################    Modelo para AnimeStaff
class AnimeStaff(models.Model):
    """Model definition for AnimeStaff."""
    person = models.ForeignKey(OtakuPerson, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='anime_staff_positions', on_delete=models.CASCADE, verbose_name=_('Persona'))
    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='staff_members', on_delete=models.CASCADE, verbose_name=_('Anime'))
    position = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True, 'role_staff': True,}, related_name='anime_person_role_staff', on_delete=models.CASCADE, verbose_name=_('Rol'))
    # mal ids
    person_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Persona'))
    anime_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Anime'))
    # Base Data
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AnimeStaff."""
        verbose_name = _('Personal de Anime')
        verbose_name_plural = _('Personal de Animes')
        ordering = ['anime_mal_id', 'position', 'person_mal_id',]
        unique_together = (('anime_mal_id', 'person_mal_id', 'position',),)

    def __str__(self):
        """Unicode representation of AnimeStaff."""
        return f"({self.position}) en Anime ID {self.anime_mal_id}"

    # def save(self):
    #     """Save method for AnimeStaff."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for AnimeStaff."""
    #     return ('')

    # TODO: Define custom methods here

########################################################################################################    Modelo para AuthorManga
class AuthorManga(models.Model):
    """Model definition for AuthorManga."""
    person = models.ForeignKey(OtakuPerson, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='manga_author_roles', on_delete=models.CASCADE, verbose_name=_('Persona'))
    manga = models.ForeignKey(Manga, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='authors', on_delete=models.CASCADE, verbose_name=_('Manga'))
    position = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True, 'role_manga': True,}, related_name='manga_person_role_manga', on_delete=models.CASCADE, verbose_name=_('Rol'))
    # mal ids
    person_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Persona'))
    manga_mal_id = models.IntegerField(blank=True, null=True, verbose_name=_('MAL ID Manga'))
    # Base Data
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AuthorManga."""
        verbose_name = 'Autor Manga'
        verbose_name_plural = 'Autores Mangas'
        ordering = ['manga_mal_id', 'position', 'person_mal_id',]
        unique_together = (('person_mal_id', 'manga_mal_id', 'position',),)

    def __str__(self):
        """Unicode representation of AuthorManga."""
        return f"{self.person.full_name} ({self.position}) en Manga ID {self.manga_mal_id}"

    # def save(self):
    #     """Save method for AuthorManga."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for AuthorManga."""
    #     return ('')

    # TODO: Define custom methods here

########################################################################################################    Modelo para MediaRelation
class MediaRelation(models.Model):
    ENTRY_TYPE_CHOICES = [
        ('anime', 'Anime'),
        ('manga', 'Manga'),
    ]

    relation_type = models.ForeignKey(RelationType, on_delete=models.CASCADE, verbose_name=_('Tipo de relación'))
    from_entry_mal_id = models.IntegerField(verbose_name=_('MAL ID Desde'))
    from_entry_type = models.CharField(max_length=50, choices=ENTRY_TYPE_CHOICES, verbose_name=_('Tipo Desde'))
    to_entry_mal_id = models.IntegerField(verbose_name=_('MAL ID Hacia'))
    to_entry_type = models.CharField(max_length=50, choices=ENTRY_TYPE_CHOICES, verbose_name=_('Tipo Hacia'))
    from_entry_mal_id_p = models.CharField(max_length=20, verbose_name='MAL ID prefijo Desde')
    to_entry_mal_id_p = models.CharField(max_length=20, verbose_name='MAL ID prefijo Hacia')
    # Base Data
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))


    class Meta:
        verbose_name = 'Relación de Media'
        verbose_name_plural = 'Relaciones de Media'
        ordering = ['-created_at']
        unique_together = (('from_entry_mal_id', 'to_entry_mal_id', 'relation_type'),)

    def __str__(self):
        return f"[{self.get_from_entry_type_display()} #{self.from_entry_mal_id}] {self.relation_type} → [{self.get_to_entry_type_display()} #{self.to_entry_mal_id}]"

    # def save(self):
    #     """Save method for MediaRelation."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MediaRelation."""
    #     return ('')

    # TODO: Define custom methods here

################################################################################################################################################################################################################
########################################################################################################    Modelo para AnimeImage
class AnimeImage(models.Model):
    """Model definition for AnimeImage."""
    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='animes_as_images', on_delete=models.CASCADE, verbose_name=_('Anime'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='animes_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=anime_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AnimeImage."""
        verbose_name = _('Imagen Anime')
        verbose_name_plural = _('Imágenes Animes')
        ordering = ['anime', 'size_image', 'name',]
        unique_together = (('anime', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of AnimeImage."""
        return self.name if self.anime else _('Imagen sin Anime')

    def save(self, *args, **kwargs):
        """Save method for AnimeImage."""
        old = AnimeImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for AnimeImage."""
        return reverse('otaku_app:anime_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.anime:
            return self.anime.title
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

########################################################################################################    Modelo para AnimeImageExtra
class AnimeImageExtra(models.Model):
    """Model definition for AnimeImageExtra."""
    anime = models.ForeignKey(Anime, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='animes_as_extra_images', on_delete=models.CASCADE, verbose_name=_('Anime'))
    image = models.ImageField(blank=False, null=False, upload_to=anime_image_extra_path, verbose_name=_('Imagen Extra Anime'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for AnimeImageExtra."""
        verbose_name = _('Imagen Extra Anime')
        verbose_name_plural = _('Imágenes Extra Anime')
        ordering = ['anime', 'name',]
        unique_together = (('anime', 'name',),)

    def __str__(self):
        """Unicode representation of AnimeImageExtra."""
        return self.name if self.anime else _('Imagen sin Anime')

    def save(self, *args, **kwargs):
        """Save method for AnimeImageExtra."""
        old = AnimeImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for AnimeImageExtra."""
        return reverse('otaku_app:anime_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.anime:
            return self.anime.title
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

########################################################################################################    Modelo para MangaImage
class MangaImage(models.Model):
    """Model definition for MangaImage."""
    manga = models.ForeignKey(Manga, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='mangas_as_images', on_delete=models.CASCADE, verbose_name=_('Manga'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='mangas_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=manga_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MangaImage."""
        verbose_name = _('Imagen Manga')
        verbose_name_plural = _('Imágenes Mangas')
        ordering = ['manga', 'size_image', 'name',]
        unique_together = (('manga', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of MangaImage."""
        return self.name if self.manga else _('Imagen sin Manga')

    def save(self, *args, **kwargs):
        """Save method for MangaImage."""
        old = MangaImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for MangaImage."""
        return reverse('otaku_app:manga_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.manga:
            return self.manga.title
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

########################################################################################################    Modelo para MangaImageExtra
class MangaImageExtra(models.Model):
    """Model definition for MangaImageExtra."""
    manga = models.ForeignKey(Manga, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='mangas_as_extra_images', on_delete=models.CASCADE, verbose_name=_('Manga'))
    image = models.ImageField(blank=False, null=False, upload_to=manga_image_extra_path, verbose_name=_('Imagen Extra Manga'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MangaImageExtra."""
        verbose_name = _('Imagen Extra Manga')
        verbose_name_plural = _('Imágenes Extra Manga')
        ordering = ['manga', 'name',]
        unique_together = (('manga', 'name',),)

    def __str__(self):
        """Unicode representation of MangaImageExtra."""
        return self.name if self.manga else _('Imagen sin Manga')

    def save(self, *args, **kwargs):
        """Save method for MangaImageExtra."""
        old = MangaImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        return reverse('otaku_app:manga_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.manga:
            return self.manga.title
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

########################################################################################################    Modelo para OtakuPersonImage
class OtakuPersonImage(models.Model):
    """Model definition for OtakuPersonImage."""
    person = models.ForeignKey(OtakuPerson, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='otaku_persons_as_images', on_delete=models.CASCADE, verbose_name=_('Persona'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='otaku_persons_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=otaku_person_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for OtakuPersonImage."""
        verbose_name = _('Imagen Persona')
        verbose_name_plural = _('Imágenes Personas')
        ordering = ['person', 'size_image', 'name',]
        unique_together = (('person', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of OtakuPersonImage."""
        return self.name if self.person else _('Imagen sin Persona')

    def save(self, *args, **kwargs):
        """Save method for OtakuPersonImage."""
        old = OtakuPersonImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for OtakuPersonImage."""
        return reverse('otaku_app:otaku_person_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.person:
            return self.person.full_name
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

########################################################################################################    Modelo para OtakuPersonImageExtra
class OtakuPersonImageExtra(models.Model):
    """Model definition for OtakuPersonImageExtra."""
    person = models.ForeignKey(OtakuPerson, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='otaku_persons_as_extra_images', on_delete=models.CASCADE, verbose_name=_('Persona'))
    image = models.ImageField(blank=False, null=False, upload_to=otaku_person_image_extra_path, verbose_name=_('Imagen Extra Persona'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for OtakuPersonImageExtra."""
        verbose_name = _('Imagen Extra Persona')
        verbose_name_plural = _('Imágenes Extra Personas')
        ordering = ['person', 'name',]
        unique_together = (('person', 'name',),)

    def __str__(self):
        """Unicode representation of OtakuPersonImageExtra."""
        return self.name if self.person else _('Imagen sin Persona')

    def save(self, *args, **kwargs):
        """Save method for OtakuPersonImageExtra."""
        old = OtakuPersonImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for OtakuPersonImageExtra."""
        return reverse('otaku_app:otaku_person_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.person:
            return self.person.full_name
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

########################################################################################################    Modelo para CharacterImage
class CharacterImage(models.Model):
    """Model definition for CharacterImage."""
    character = models.ForeignKey(Character, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='characters_as_images', on_delete=models.CASCADE, verbose_name=_('Personaje'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='characters_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=character_image_path, verbose_name=_('Imagen'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for CharacterImage."""
        verbose_name = _('Imagen Personaje')
        verbose_name_plural = _('Imágenes Personajes')
        ordering = ['character', 'size_image', 'name',]
        unique_together = (('character', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of CharacterImage."""
        return self.name if self.Character else _('Imagen sin Personaje')

    def save(self, *args, **kwargs):
        """Save method for CharacterImage."""
        old = CharacterImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for CharacterImage."""
        return reverse('otaku_app:character_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.character:
            return self.character.full_name
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

########################################################################################################    Modelo para CharacterImageExtra
class CharacterImageExtra(models.Model):
    """Model definition for CharacterImageExtra."""
    character = models.ForeignKey(Character, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='characters_as_extra_images', on_delete=models.CASCADE, verbose_name=_('Personaje'))
    image = models.ImageField(blank=False, null=False, upload_to=character_image_extra_path, verbose_name=_('Imagen Extra Personaje'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for CharacterImageExtra."""
        verbose_name = _('Imagen Extra Personaje')
        verbose_name_plural = _('Imágenes Extra Personajes')
        ordering = ['character', 'name',]
        unique_together = (('character', 'name',),)

    def __str__(self):
        """Unicode representation of  CharacterImageExtra."""
        return self.name if self.character else _('Imagen sin Personaje')

    def save(self, *args, **kwargs):
        """Save method for CharacterImageExtra."""
        old = CharacterImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for CharacterImageExtra."""
        return reverse('otaku_app:character_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.character:
            return self.character.full_name
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

########################################################################################################    Modelo para MALAnime
class DataAnime(models.Model):
    """Model definition for MALAnime."""
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALAnime."""
        verbose_name = _('Dato de anime (MAL)')
        verbose_name_plural = _('Datos de animes (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_anime'

    def __str__(self):
        """Unicode representation of MALAnime."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALAnimeCharacters
class DataAnimeCharacters(models.Model):
    """Model definition for MALAnimeCharacters."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALAnimeCharacters."""
        verbose_name = _('Dato de personaje de anime (MAL)')
        verbose_name_plural = _('Datos de personajes de animes (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_anime_characters'

    def __str__(self):
        """Unicode representation of MALAnimeCharacters."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALAnimePictures
class DataAnimePictures(models.Model):
    """Model definition for MALAnimePictures."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALAnimePictures."""
        verbose_name = _('Dato de imagen de anime (MAL)')
        verbose_name_plural = _('Datos de imágenes de animes (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_anime_pictures'

    def __str__(self):
        """Unicode representation of MALAnimePictures."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALAnimeStaff
class DataAnimeStaff(models.Model):
    """Model definition for MALAnimeStaff."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALAnimeStaff."""
        verbose_name = _('Dato de personal de anime (MAL)')
        verbose_name_plural = _('Datos de personal de animes (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_anime_staff'

    def __str__(self):
        """Unicode representation of MALAnimeStaff."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALManga
class DataManga(models.Model):
    """Model definition for MALManga."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALManga."""
        verbose_name = _('Dato de manga (MAL)')
        verbose_name_plural = _('Datos de mangas (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_manga'

    def __str__(self):
        """Unicode representation of MALManga."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALMangaCharacters
class DataMangaCharacters(models.Model):
    """Model definition for MALMangaCharacters."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALMangaCharacters."""
        verbose_name = _('Dato de personaje de manga (MAL)')
        verbose_name_plural = _('Datos de personajes de mangas (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_manga_characters'

    def __str__(self):
        """Unicode representation of MALMangaCharacters."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALMangaPictures
class DataMangaPictures(models.Model):
    """Model definition for MALMangaPictures."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALMangaPictures."""
        verbose_name = _('Dato de imagen de manga (MAL)')
        verbose_name_plural = _('Datos de imágenes de mangas (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_manga_pictures'

    def __str__(self):
        """Unicode representation of MALMangaPictures."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALCharacter
class DataCharacter(models.Model):
    """Model definition for MALCharacter."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALCharacter."""
        verbose_name = _('Dato de personaje (MAL)')
        verbose_name_plural = _('Datos de personajes (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_character'

    def __str__(self):
        """Unicode representation of MALCharacter."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALCharacterPictures
class DataCharacterPictures(models.Model):
    """Model definition for MALCharacterPictures."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALCharacterPictures."""
        verbose_name = _('Dato de imagen de personaje (MAL)')
        verbose_name_plural = _('Datos de imágenes de personajes (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_character_pictures'

    def __str__(self):
        """Unicode representation of MALCharacterPictures."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALOtakuPerson
class DataOtakuPerson(models.Model):
    """Model definition for MALOtakuPerson."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALOtakuPerson."""
        verbose_name = _('Dato de persona (MAL)')
        verbose_name_plural = _('Datos de personas (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_otaku_person'

    def __str__(self):
        """Unicode representation of MALOtakuPerson."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALOtakuPersonPictures
class DataOtakuPersonPictures(models.Model):
    """Model definition for MALOtakuPersonPictures."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    mal_id = models.IntegerField(verbose_name=_('ID MyAnimeList'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    data = models.JSONField(blank=True, null=True, verbose_name=_("Datos"))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALOtakuPersonPictures."""
        verbose_name = _('Dato de imagen de persona (MAL)')
        verbose_name_plural = _('Datos de imágenes de personas (MAL)')
        ordering = ['-created_at', 'mal_id',]
        unique_together = (('mal_id', 'url', 'status',),)
        db_table = 'fetch_otaku_person_pictures'

    def __str__(self):
        """Unicode representation of MALOtakuPersonPictures."""
        return f"{self.mal_id} - {self.status}"

########################################################################################################    Modelo para MALImageURL
class DataImageURL(models.Model):
    """Model definition for MALImageURL."""
    url = models.URLField(max_length=20000, blank=True, null=True, verbose_name=_('URL'))
    status = models.BooleanField(default=False, verbose_name=_('Estado'))
    processed = models.BooleanField(default=False, verbose_name=_('Procesado'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MALImageURL."""
        verbose_name = _('Dato de imagen URL (MAL)')
        verbose_name_plural = _('Datos de imágenes de URL (MAL)')
        ordering = ['-created_at', 'url',]
        unique_together = (('url', 'status',),)
        db_table = 'fetch_image_url'

    def __str__(self):
        """Unicode representation of MALImageURL."""
        return f"{self.url} - {self.status}"

########################################################################################################    Modelo para Temp_OtakuPersons
class Temp_OtakuPersons(models.Model):
    """Model definition for TempOtakuPersons."""
    mal_id_person = models.IntegerField()  # Ya no es único
    lenguaje = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        """Meta definition for TempOtakuPersons."""
        verbose_name = _('Temp. Otaku Persona')
        verbose_name_plural = _('Temp. Otaku Personas')
        unique_together = (('mal_id_person', 'lenguaje',),)
        db_table = 'temp_otaku_persons'

########################################################################################################    Modelo para Temp_Characters
class Temp_Characters(models.Model):
    """Model definition for TempCharacters."""
    mal_id_character = models.IntegerField(unique=True)

    class Meta:
        """Meta definition for TempCharacters."""
        verbose_name = _('Temp. Personaje')
        verbose_name_plural = _('Temp. Personajes')
        db_table = 'temp_characters'
