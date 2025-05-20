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
from apps.common.models import Country, Person, Language, ImageSize, Company
from core.utils.utils import obtener_inicial
from core.models import BaseLog, YearField
from .utils.uploads import serie_image_extra_path, serie_image_path

# Create your models here.
########################################################################################################    Log
class SerieLog(BaseLog):
    """Model definition for SerieLog."""

    class Meta:
        """Definición de meta datos para SerieLog."""
        verbose_name = _('Log Serie')
        verbose_name_plural = _('Logs Series')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Serie'

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

########################################################################################################    Modelo para Role
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
        verbose_name = _('Rol Serie')
        verbose_name_plural = _('Roles Series')
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
    name = models.CharField(max_length=60, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=60, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=60, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
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

########################################################################################################    Modelo para Serie
class Serie(models.Model):
    """Model definition for Serie."""
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Título Original'))
    title_secundary = models.CharField(max_length=255,null=True, blank=True, verbose_name=_('Título Secundario'))
    release_year = YearField(blank=True, null=True, verbose_name=_('Año Lanzamiento'))
    duration_minutes = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('Duración Minutos'))
    synopsis = models.TextField(blank=True, verbose_name=_('Sinopsis'))
    serie_types = models.ForeignKey(Type, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_types', on_delete=models.CASCADE, verbose_name=_('Tipo Serie'))
    serie_rating = models.ForeignKey(Rating, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_ratings', on_delete=models.CASCADE, verbose_name=_('Clasificación Serie'))
    genres = models.ManyToManyField(Genre, blank=True, limit_choices_to={'is_active': True}, related_name='series_as_genre', verbose_name=_('Géneros'))
    producers = models.ManyToManyField(Company, blank=True, limit_choices_to={'is_active': True}, related_name='series_as_producers', verbose_name=_('Productoras'))
    distributors = models.ManyToManyField(Company, blank=True, limit_choices_to={'is_active': True}, related_name='series_as_distributors', verbose_name=_('Distribuidoras'))
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
        if self.release_year:
            return (f'{self.title} ({self.release_year})')
        return self.title

    def save(self, *args, **kwargs):
        """Save method for Serie."""
        old = Serie.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.title:
            self.title = self.title.strip().title()
        if self.title_secundary:
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

########################################################################################################    Modelo para TitleSerie
class TitleSerie(models.Model):
    """Model definition for TitleSerie."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_title', on_delete=models.CASCADE, verbose_name=_('Serie'))
    title_lang = models.ForeignKey(Language, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='titles_series_as_languages', on_delete=models.CASCADE, verbose_name=_('Idioma'))
    title = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_('Título'))
    slug = models.SlugField(max_length=255, unique=False, null=False, blank=True, editable=False, verbose_name=_('Título Slug'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for TitleSerie."""
        verbose_name = _('Título')
        verbose_name_plural = _('Títulos')
        ordering = ['serie', 'title_lang', 'initial', 'title',]
        unique_together = (('title_lang', 'title', 'serie',),)

    def __str__(self):
        """Unicode representation of TitleSerie."""
        return f'{self.serie.title} - {self.title_lang.name} - {self.title}'

    def save(self, *args, **kwargs):
        """Save method for TitleSerie."""
        # Obtener el objeto original si existe
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
        """Return absolute url for TitleSerie."""
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
        verbose_name = _('Personal Serie')
        verbose_name_plural = _('Personal Series')
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
        return reverse('serie_app:serie_cast_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
        return None

########################################################################################################    Modelo para SerieImage
class SerieImage(models.Model):
    """Model definition for SerieImage."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_images', on_delete=models.CASCADE, verbose_name=_('Serie'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_images_as_sizes', on_delete=models.CASCADE, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=serie_image_path, verbose_name=_('Imagen Serie'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SerieImage."""
        verbose_name = _('Imagen Serie')
        verbose_name_plural = _('Imágenes Series')
        ordering = ['serie', 'size_image',]
        unique_together = (('serie', 'size_image',),)

    def __str__(self):
        """Unicode representation of SerieImage."""
        if self.serie and self.serie.title:
            return _('Imagen de %(name)s') % {'name': self.serie.title}
        elif self.image:
            return os.path.basename(self.image.name)
        return _('Imagen sin asignar')

    def save(self, *args, **kwargs):
        """Save method for SerieImage."""
        if self.pk:
            old = SerieImage.objects.filter(pk=self.pk).first()
            if old and old.image and self.image and old.image.name != self.image.name:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for SerieImage."""
        return reverse('serie_app:serie_image_detail', kwargs={'pk': self.pk})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
        return _('No Asignado')

    def get_img_url(self):
        return self.image.url if self.image else None

    def get_image_name(self):
        if self.image:
            return os.path.splitext(os.path.basename(self.image.name))[0]
        return None

    def get_image_extension(self):
        if self.image:
            return os.path.splitext(self.image.name)[1].lower()
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
        return _('Tamaño desconocido')

    @property
    def image_dimensions(self):
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            try:
                with PILImage.open(self.image) as img:
                    return img.size
            except Exception as e:
                print(_('Error al abrir la imagen: %(error)s') % {'error': e})
        return (0, 0)

########################################################################################################    Modelo para SerieImageExtra
class SerieImageExtra(models.Model):
    """Model definition for SerieImageExtra."""
    serie = models.ForeignKey(Serie, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='series_as_exta_images', on_delete=models.CASCADE, verbose_name=_('Serie'))
    image = models.ImageField(blank=False, null=False, upload_to=serie_image_extra_path, verbose_name=_('Imagen Extra Serie'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for SerieImageExtra."""
        verbose_name = _('Imagen Extra Serie')
        verbose_name_plural = _('Imágenes Extra Series')
        ordering = ['serie',]

    def __str__(self):
        """Unicode representation of SerieImageExtra."""
        if self.serie and self.serie.title:
            return _('Imagen de %(name)s') % {'name': self.serie.title}
        elif self.image:
            return os.path.basename(self.image.name)
        return _('Imagen sin asignar')

    def save(self, *args, **kwargs):
        """Save method for SerieImageExtra."""
        if self.pk:
            old = SerieImageExtra.objects.filter(pk=self.pk).first()
            if old and old.image and self.image and old.image.name != self.image.name:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for SerieImageExtra."""
        return reverse('serie_app:serie_image_extra_detail', kwargs={'pk': self.pk})

    # custom methods
    def get_object_name(self):
        if self.serie:
            return self.serie.title
        return _('No Asignado')

    def get_img_url(self):
        return self.image.url if self.image else None

    def get_image_name(self):
        if self.image:
            return os.path.splitext(os.path.basename(self.image.name))[0]
        return None

    def get_image_extension(self):
        if self.image:
            return os.path.splitext(self.image.name)[1].lower()
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
        return _('Tamaño desconocido')

    @property
    def image_dimensions(self):
        if self.image and hasattr(self.image, 'path') and os.path.isfile(self.image.path):
            try:
                with PILImage.open(self.image) as img:
                    return img.size
            except Exception as e:
                print(_('Error al abrir la imagen: %(error)s') % {'error': e})
        return (0, 0)

