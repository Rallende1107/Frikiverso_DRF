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
from apps.common.models import Country, Person, Language, ImageSize
from core.utils.utils import BaseLog, obtener_inicial, YearField
from .utils.uploads import serie_image_extra_path, serie_image_path

# Create your models here.

########################################################################################################    Log
class SerieLog(BaseLog):
    """Model definition for SerieLog."""

    class Meta:
        """Meta definition for SerieLog."""
        verbose_name = _('Log Serie')
        verbose_name_plural = _('Logs Serie')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Serie'

########################################################################################################    Modelo para Genre
class Genre(models.Model):
    """Model definition for Genre."""
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='childrens', verbose_name=_('Padre'))
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
        return reverse('serie_app:genre_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_series(self):
        return self.series_as_genre.count()

########################################################################################################    Modelo para Type
class Type(models.Model):
    """Model definition for Type."""
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='childrens', verbose_name=_('Padre'))
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))
    delete = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Type."""
        verbose_name = _('Tipo Serie')
        verbose_name_plural = _('Tipos Series')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        """Unicode representation of Type."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Type."""
        # Obtener el objeto original si existe
        old = Type.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Type."""
        return reverse('serie_app:serie_type_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_series(self):
        return self.series_as_types.count()

########################################################################################################    Modelo para SerieRole
class Role(models.Model):
    """Model definition for Role."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    role_staff = models.BooleanField(default=False, verbose_name=_('Rol Personal'))
    role_cast = models.BooleanField(default=False, verbose_name=_('Rol Elenco'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Role."""
        verbose_name = _('Ros Película')
        verbose_name_plural = _('Roles Películas')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'name_esp', 'role_staff', 'role_cast',),)

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
        return reverse('serie_app:role_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_serie_staff(self):
        return self.persons_as_serie_staff_roles.count()

    def get_num_serie_cast(self):
        return self.persons_as_serie_cast_roles.count()

########################################################################################################    Modelo para Rating
class Rating(models.Model):
    """Model definition for Rating."""
    acronym = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name=_('Acrónimo'))
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=100, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
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
        # Obtener el objeto original si existe
        old = Rating.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.acronym:
            self.acronym = self.acronym.strip().upper()
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.acronym != old.acronym):
            self.slug = slugify(self.acronym)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Rating."""
        return reverse('serie_app:rating_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_num_series(self):
        return self.series_as_ratings.count()

########################################################################################################    Modelo para Company
class Company(models.Model):
    """Model definition for Company."""
    name = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=255,  unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='seriess_as_countries', verbose_name=_('País'))
    founded_year = YearField(blank=True, null=True, verbose_name=_('Año Fundación'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Company."""
        verbose_name = _('Compañia')
        verbose_name_plural = _('Compañias')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Company."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Company."""
        # Obtener el objeto original si existe
        old = Company.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Company."""
        return reverse('serie_app:company_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_producer_series(self):
        return self.series_as_producers.count()

    def get_distributor_series(self):
        return self.series_as_distributors.count()

########################################################################################################    Modelo para Serie
class Serie(models.Model):
    """Model definition for Serie."""
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Título Original'))
    title_secundary = models.CharField(max_length=255,null=True, blank=True, verbose_name=_('Título Secundario'))
    release_year = YearField(null=True, blank=True, verbose_name=_('Año Lanzamiento'))
    ending_year = YearField(null=True, blank=True, verbose_name=_('Año Termino'))
    episodes = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Episodios'))
    synopsis = models.TextField(blank=True, verbose_name=_('Sinopsis'))
    serie_types = models.ForeignKey(Type, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_types', on_delete=models.CASCADE, verbose_name=_('Tipo Serie'))
    serie_rating = models.ForeignKey(Rating, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_ratings', on_delete=models.CASCADE, verbose_name=_('Clasificación Serie'))
    genres = models.ManyToManyField(Genre, blank=True, limit_choices_to={'is_active': True}, related_name='series_as_genre', verbose_name=_('Géneros'))
    producers = models.ManyToManyField(Company, blank=True, limit_choices_to={'is_active': True}, related_name='series_as_producers', verbose_name=_('Productoras'))
    distributors = models.ManyToManyField(Company, blank=True, limit_choices_to={'is_active': True}, related_name='series_as_distributors',  verbose_name=_('Distribuidoras'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Serie."""
        verbose_name = _('Serie')
        verbose_name_plural = _('Series')
        ordering = ['-created_at', 'title',]
        unique_together = (('title', 'title_secundary', 'release_year',),)

    def __str__(self):
        """Unicode representation of Serie."""
        if self.release_year and self.ending_year:
            return (f'{self.title} ({self.release_year} - {self.ending_year})')
        if self.release_year and not self.ending_year:
            return (f'{self.title} ({self.release_year})')
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Serie."""
        old = Serie.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.title:
            self.title = self.title.strip().title()
        # if self.title_secundary:
            self.title_secundary = self.title_secundary.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Serie."""
        return reverse('serie_app:serie_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_main_cast(self):
        return self.series_as_casts.filter(role='lead', is_active=True)

    def get_second_cast(self):
        return self.series_as_casts.filter(role='supporting', is_active=True)

    def get_extra_cast(self):
        return self.series_as_casts.filter(role='extra', is_active=True)

    def get_cameo_cast(self):
        return self.series_as_casts.filter(role='cameo', is_active=True)

    def get_full_cast(self):
        return self.series_as_casts.filter(is_active=True)

    def get_credit_series(self):
        return self.series_as_staffs.count()

########################################################################################################    Modelo para Title
class TitleSerie(models.Model):
    """Model definition for Title."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_title', on_delete=models.CASCADE, verbose_name=_('Serie'))
    title_lang = models.ForeignKey(Language, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='titles_series_as_languages', on_delete=models.CASCADE, verbose_name=_('Lenguaje'))
    title = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=255, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Title."""
        verbose_name = _('Título')
        verbose_name_plural = _('Títulos')
        ordering = ['title_lang', 'initial', 'title',]
        unique_together = (('title_lang', 'title', 'serie',),)

    def __str__(self):
        """Unicode representation of Title."""
        return f'{self.serie.title} - {self.title_lang.name} - {self.title}'

    def save(self, *args, **kwargs):
        """Save method for Title."""
        old = TitleSerie.objects.filter(pk=self.pk).first() if self.pk else None

        if self.title:
            self.title = self.title.strip()

        if not self.initial or (old and self.title != old.title):
            self.initial = obtener_inicial(self.title).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.title != old.title):
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Title."""
        return reverse('serie_app:title_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
        return None

########################################################################################################    Modelo para SerieStaff
class SerieStaff(models.Model):
    """Model definition for SerieStaff."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_staffs', on_delete=models.CASCADE, verbose_name=_('Serie'))
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_persons', on_delete=models.CASCADE, verbose_name=_('Persona'))
    role = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True, 'role_staff': True}, related_name='persons_as_serie_staff_roles', on_delete=models.CASCADE, verbose_name=_('Rol'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SerieStaff."""
        verbose_name = _('Personal Película')
        verbose_name_plural = _('Personal Películas')
        ordering = ['serie', 'role', 'person',]
        unique_together = (('serie', 'role', 'person',),)

    def __str__(self):
        """Unicode representation of SerieStaff."""
        return f'{self.person.full_name} Es: {self.role.name} de: {self.serie.title}'

    def get_absolute_url(self):
        """Return absolute url for SerieStaff."""
        return reverse('serie_app:serie_staff_detail', kwargs={'pk': self.pk})

    # custom methods
    def get_serie_title(self):
        if self.serie:
            return self.serie.title
        return None

    def get_person_name(self):
        if self.person:
            return self.person.full_name
        return None

    def get_role_name(self):
        if self.role:
            return self.role.name
        return None

########################################################################################################    Modelo para SerieCast
class SerieCast(models.Model):
    """Model definition for SerieCast."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_casts', on_delete=models.CASCADE, verbose_name=_('Serie'))
    actor = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_as_serie_cast_roles', on_delete=models.CASCADE, verbose_name=_('Actor'))
    role = models.ForeignKey(Role, blank=False, null=False, limit_choices_to={'is_active': True, 'role_cast': True}, related_name='actors_as_roles', on_delete=models.CASCADE, verbose_name=_('Rol'))
    character_name = models.CharField(max_length=100, unique=False, null=False, blank=False, verbose_name=_('Personaje'))
    slug = models.SlugField(max_length=100, unique=False, null=False, blank=True, editable=False, verbose_name=_('Personaje Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SerieCast."""
        verbose_name = _('Reparto Serie')
        verbose_name_plural = _('Reparto Series')
        ordering = ['serie', 'actor', 'character_name',]
        unique_together = (('serie', 'actor', 'role', 'character_name',),)

    def __str__(self):
        """Unicode representation of SerieCast."""
        return f"{self.actor.full_name}, como: {self.character_name}, en: {self.serie.title} ({self.role.name})"

    def save(self, *args, **kwargs):
        """Save method for SerieCast."""
        old = SerieCast.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.character_name:
            self.character_name = self.character_name.strip().title()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.character_name != old.character_name):
            self.initial = obtener_inicial(self.character_name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.character_name != old.character_name):
            self.slug = slugify(self.character_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for SerieCast."""
        return reverse('serie_app:serie_cast_detail', kwargs={'pk': self.pk})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
        return None

########################################################################################################    Modelo para SerieImage
class SerieImage(models.Model):
    """Model definition for SerieImage."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_images', on_delete=models.CASCADE, verbose_name=_('Serie'))
    image = models.ImageField(blank=False, null=False, upload_to=serie_image_path, verbose_name=_('Imagen Serie'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SerieImage."""
        verbose_name = _('Imagen Serie')
        verbose_name_plural = _('Imágenes Series')
        ordering = ['serie', 'size_image', 'name',]
        unique_together = (('serie', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of SerieImage."""
        return self.name if self.serie else _('Imagen sin Serie')

    def save(self, *args, **kwargs):
        """Save method for SerieImage."""
        old = SerieImage.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for SerieImage."""
        return reverse('serie_app:serie_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
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

########################################################################################################    Modelo para SerieImageExtra
class SerieImageExtra(models.Model):
    """Model definition for SerieImageExtra."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_images_exta', on_delete=models.CASCADE, verbose_name=_('Serie'))
    image = models.ImageField(blank=False, null=False, upload_to=serie_image_extra_path, verbose_name=_('Imagen Extra Serie'))
    name = models.CharField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, blank=False, null=False, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SerieImageExtra."""
        verbose_name = _('Imagen Extra Serie')
        verbose_name_plural = _('Imágenes Extra Series')
        ordering = ['serie', 'name',]
        unique_together = (('serie', 'name',),)

    def __str__(self, *args, **kwargs):
        """Unicode representation of SerieImageExtra."""
        old = SerieImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for SerieImageExtra."""
        return reverse('serie_app:serie_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
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