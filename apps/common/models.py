# Imports estándar de Python
import os
from datetime import date
# Imports de terceros (Django, PIL, etc.)
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage
# Imports locales del proyecto
from core.utils.utils import obtener_inicial
from core.models import BaseLog, YearField
from .utils.uploads import person_image_path, person_image_extra_path

# Create your models here.
########################################################################################################    Log
class CommonLog(BaseLog):
    """Model definition for CommonLog."""

    class Meta:
        """Definición de meta datos para CommonLog."""
        verbose_name = _('Log General')
        verbose_name_plural = _('Logs General')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Common'

########################################################################################################    Modelo para Country
class Country(models.Model):
    """Model definition for Country."""
    name = models.CharField(max_length=60, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=60, unique=True, null=False, blank=False, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    initial_esp = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial Español'))
    slug = models.SlugField(max_length=60, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    code = models.CharField(max_length=4, unique=False, null=False, blank=True, verbose_name=_('Código'))
    numeric_code = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('Código Numérico'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Country."""
        verbose_name = _('País')
        verbose_name_plural = _('Países')
        ordering = ['initial', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Country."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Country."""
        # Obtener el objeto original si existe
        old = Country.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nombre
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        if self.code:
            self.code = self.code.strip().upper()

        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        if not self.initial_esp or (old and self.name_esp != old.name_esp):
            self.initial_esp = obtener_inicial(self.name_esp).upper()

        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Country."""
        return reverse('common_app:country_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    @property
    def display_name(self):
        if self.code:
            return f"{self.name} ({self.code})"
        return self.name

    @property
    def display_name_esp(self):
        display_name = self.name_esp if self.name_esp else self.name
        if self.code:
            return f"{display_name} ({self.code})"
        return display_name

########################################################################################################    Modelo para Company
class Company(models.Model):
    """Model definition for Company."""
    name = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=250, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    founded_year = YearField(blank=True, null=True, verbose_name=_('Año Fundación'))
    disolved_year = YearField(blank=True, null=True, verbose_name=_('Año Disolución'))
    country = models.ForeignKey(Country, blank=True,  null=True,  limit_choices_to={'is_active': True}, related_name='Companies_as_countries', on_delete=models.CASCADE, verbose_name=_('País'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Company."""
        verbose_name = _('Compañía')
        verbose_name_plural = _('Compañías')
        ordering = ['-created_at', 'initial', 'name',]
        unique_together = (('name', 'country',),)

    def __str__(self):
        """Unicode representation of Company."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Company."""
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
        return reverse('common_app:company_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def years_of_activity(self):
        """
        Retorna el rango de años de actividad de la compañía.
        Formato: 'YYYY - YYYY' si tiene ambos años.
        'YYYY - Presente' si solo tiene año de fundación.
        'Desconocido - YYYY' si solo tiene año de disolución.
        'Desconocido' si no tiene ninguno.
        """
        founded = self.founded_year
        disolved = self.disolved_year

        if founded and disolved:
            return f"{founded} - {disolved}"
        elif founded and not disolved:
            return f"{founded} - {_('Presente')}"
        elif not founded and disolved:
            return f"{_('Desconocido')} - {disolved}"
        else:
            return _("Desconocido")

    def get_num_animes_produced(self):
        return self.animes_as_producers.count()

    def get_num_animes_licensed(self):
        return self.animes_as_licensors.count()

    def get_num_animes_in_studio(self):
        return self.animes_as_studios.count()

    def get_num_mangas_serialized(self):
        return self.mangas_as_serializations.count()

    def get_num_movies_produced(self):
        return self.movies_as_producers.count()

    def get_num_movies_distributed(self):
        return self.movies_as_distributors.count()

    def get_num_series_produced(self):
        return self.series_as_producers.count()

    def get_num_series_distributed(self):
        return self.series_as_distributors.count()

########################################################################################################    Modelo para Format
class Format(models.Model):
    """Model definition for Format."""
    name = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    for_video = models.BooleanField(default=False, verbose_name=_('Videos'))
    for_music = models.BooleanField(default=False, verbose_name=_('Música'))
    for_image = models.BooleanField(default=False, verbose_name=_('Imágenes'))
    for_document = models.BooleanField(default=False, verbose_name=_('Documentos'))
    for_other = models.BooleanField(default=False, verbose_name=_('Otros'))
    slug = models.CharField(max_length=20, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Format."""
        verbose_name = _('Formato')
        verbose_name_plural = _('Formatos')
        ordering = ['-created_at', 'name', ]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Format."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Format."""
        # Obtener el objeto original si existe
        old = Format.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nombre
        if self.name:
            self.name = self.name.strip().upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Format."""
        return reverse('common_app:format_detail', kwargs={'pk': self.pk, 'slug': self.slug})

########################################################################################################    Modelo para Quality
class ImageSize(models.Model):
    """Model definition for ImageSize."""
    name = models.CharField(max_length=20, unique=True, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=20, verbose_name=_('Nombre Español'))
    slug = models.CharField(max_length=20, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for ImageSize."""
        verbose_name = _('Tamaño de Imagen')
        verbose_name_plural = _('Tamaños de Imágenes')
        ordering = ['name',]
        unique_together = (('name', 'name_esp',),)

    def __str__(self):
        return self.name_esp

    def save(self, *args, **kwargs):
        """Save method for ImageSize."""
        # Obtener el objeto original si existe
        old = ImageSize.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nombre
        if self.name:
            self.name = self.name.strip().title()

        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()

        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for ImageSize."""
        return reverse('common_app:image_size_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    @property
    def display_name(self):
        if self.name_esp:
            return f"{self.name} ({self.name_esp})"
        return self.name

########################################################################################################    Modelo para Language
class Language(models.Model):
    """Model definition for Language."""
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=150, unique=True, null=True, blank=True, verbose_name=_('Nombre Español'))
    acronym = models.CharField(max_length=10, unique=True, null=True, blank=True, verbose_name=_('Acrónimo'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=100, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for MODELNAME."""
        verbose_name = _('Idioma')
        verbose_name_plural = _('Idiomas')
        ordering = ['created_at', 'name',]
        unique_together = (("name", "acronym", "name_esp",),)

    def __str__(self):
        """Unicode representation of Language."""
        if self.acronym:
            return f"{self.name} ({self.acronym})"
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Language."""
        # Obtener el objeto original si existe
        old = Language.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización de nombres
        if self.name:
            self.name = self.name.strip().title()
        if self.name_esp:
            self.name_esp = self.name_esp.strip().title()
        # Acrónimo en inglés
        if not self.acronym or (old and self.name != old.name):
            self.acronym = self._generate_acronym(self.name).upper()
        else:
            self.acronym = self.acronym.strip().upper()
        # Inicial automático si está vacío o el nombre cambió
        if not self.initial or (old and self.name != old.name):
            self.initial = obtener_inicial(self.name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Language."""
        return reverse('common_app:language_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    @property
    def display_name(self):
        if self.acronym:
            return f"{self.name} ({self.acronym})"
        return self.name

    @property
    def display_name_esp(self):
        display_name = self.name_esp if self.name_esp else self.name
        if self.acronym:
            return f"{display_name} ({self.acronym})"
        return display_name

########################################################################################################    Modelo para Peson
class Person(models.Model):
    """Model definition for Person."""
    full_name = models.CharField(max_length=255, unique=False, null=False, blank=False, verbose_name=_('Nombre Completo'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    biography = models.TextField(blank=True, verbose_name=_('Biografía'))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_('Fecha Nacimiento'))
    country = models.ForeignKey(Country, blank=True, null=True, limit_choices_to={'is_active': True}, related_name='persons_as_countries', on_delete=models.SET_NULL, verbose_name=_('País'))
    slug = models.SlugField(max_length=255, unique=False, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Person."""
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')
        ordering = ['initial', 'full_name',]
        unique_together = (('initial', 'full_name',),)

    def __str__(self):
        """Unicode representation of Person."""
        return self.full_name

    def save(self, *args, **kwargs):
        """Save method for Person."""
        # Obtener el objeto original si existe
        old = Person.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del full_name
        if self.full_name:
            self.full_name = self.full_name.strip()
        # Inicial automática si está vacía o el nombre cambió
        if not self.initial or (old and self.full_name != old.full_name):
            self.initial = obtener_inicial(self.full_name).upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.full_name != old.full_name):
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Person."""
        return reverse('common_app:person_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_img_url(self):
        if self.img:
            return settings.MEDIA_URL + str(self.img)
        return None

    def get_age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return 0

########################################################################################################    Modelo para PersonImage
class PersonImage(models.Model):
    """Model definition for PersonImage."""
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_as_images', on_delete=models.CASCADE, verbose_name=_('Persona'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=person_image_path, verbose_name=_('Imagen Persona'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PersonImage."""
        verbose_name = _('Imagen Persona')
        verbose_name_plural = _('Imágenes Personas')
        ordering = ['person', 'size_image',]

    def __str__(self):
        """Unicode representation of PersonImage."""
        if self.person and self.person.full_name:
            return _('Imagen de %(name)s') % {'name': self.person.full_name}
        elif self.image:
            return os.path.basename(self.image.name)
        return _('Imagen sin asignar')

    def save(self, *args, **kwargs):
        """Save method for PersonImage."""
        if self.pk:
            old = PersonImage.objects.filter(pk=self.pk).first()
            if old and old.image and self.image and old.image.name != self.image.name:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for PersonImage."""
        return reverse('common_app:person_image_detail', kwargs={'pk': self.pk})

    # custom methods
    def get_object_name(self):
        if self.person:
            return self.person.full_name
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

########################################################################################################    Modelo para PersonImageExtra
class PersonImageExtra(models.Model):
    """Model definition for PersonImageExtra."""
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_as_exta_images', on_delete=models.CASCADE, verbose_name=_('Persona'))
    image = models.ImageField(blank=False, null=False, upload_to=person_image_extra_path, verbose_name=_('Imagen Extra Persona'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PersonImageExtra."""
        verbose_name = _('Imagen extra persona')
        verbose_name_plural = _('Imágenes extras de personas')
        ordering = ['person',]

    def __str__(self):
        """Unicode representation of PersonImageExtra."""
        if self.person and self.person.full_name:
            return _('Imagen de %(name)s') % {'name': self.person.full_name}
        elif self.image:
            return os.path.basename(self.image.name)
        return _('Imagen sin asignar')

    def save(self, *args, **kwargs):
        """Save method for PersonImageExtra."""
        if self.pk:
            old = PersonImageExtra.objects.filter(pk=self.pk).first()
            if old and old.image and self.image and old.image.name != self.image.name:
                if os.path.isfile(old.image.path):
                    os.remove(old.image.path)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for PersonImageExtra."""
        return reverse('common_app:person_image_extra_detail', kwargs={'pk': self.pk})

    # custom methods
    def get_object_name(self):
        if self.person:
            return self.person.full_name
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

########################################################################################################    Modelo para PersonNickname
class PersonNickname(models.Model):
    """Model definition for PersonNickname."""
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_as_nicknames', on_delete=models.CASCADE, verbose_name=_('Persona'))
    nickname = models.CharField(max_length=100, unique=False, null=False, blank=False, verbose_name=_('Apodo'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=100, unique=False, null=False, blank=True, editable=False, verbose_name=_('Apodo Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PersonNickname."""
        verbose_name = _('Apodo Persona')
        verbose_name_plural = _('Apodos Persona')
        ordering = ['initial','nickname',]
        unique_together = (('person', 'initial', 'nickname',),)

    def __str__(self):
        """Unicode representation of PersonNickname."""
        return f"{self.person.full_name} AKA ({self.nickname})"

    def save(self, *args, **kwargs):
        """Save method for PersonNickname."""
        # Obtener el objeto original si existe
        old = PersonNickname.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for PersonNickname."""
        return reverse('common_app:nickname_person_detail', kwargs={'pk': self.pk, 'slug': self.slug})

########################################################################################################    Modelo para Quality
class Quality(models.Model):
    """Model definition for Quality."""
    name = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    slug = models.CharField(max_length=10, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Quality."""
        verbose_name = _('Calidad')
        verbose_name_plural = _('Calidades')
        ordering = ['-created_at', 'name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of Quality."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Quality."""
        # Obtener el objeto original si existe
        old = Quality.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nombre
        if self.name:
            self.name = self.name.strip().upper()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Quality."""
        return reverse('common_app:quality_detail', kwargs={'pk': self.pk, 'slug': self.slug})

########################################################################################################    Modelo para Website
class Website(models.Model):
    """Model definition for Website."""
    name = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name=_('Nombre'))
    acronym = models.CharField(max_length=5, unique=True, null=False, blank=False, verbose_name=_('Acrónimo'))
    url = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name=_('URL'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Website."""
        verbose_name = _('Sitio Web')
        verbose_name_plural = _('Sitios Webs')
        ordering = ['-created_at', 'name',]
        unique_together = (('name', 'acronym', 'url',),)

    def __str__(self):
        """Unicode representation of Website."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for Person."""
        # Obtener el objeto original si existe
        old = Website.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for Website."""
        return reverse('common_app:website_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    @property
    def display_name(self):
        """
        Retorna el nombre del sitio web combinado con su acrónimo, si existe.
        Ej: 'MyWebsite (MW)' o 'AnotherWebsite'.
        """
        if self.acronym:
            return f"{self.name} ({self.acronym})"
        return self.name

    @property
    def display_link_text(self):
        """
        Retorna el texto a mostrar para el enlace.
        Usa el acrónimo si existe, de lo contrario, el nombre.
        """
        return self.acronym if self.acronym else self.name



class ContextApp(models.Model):
    """Model definition for ContextApp."""
    APPS = [
        ('movie', 'Películas'),
        ('music', 'Música'),
        ('otaku', 'Otaku'),
        ('game', 'Juegos'),
        ('serie', 'Serie'),
    ]
    name = models.CharField(max_length=20, unique=True, choices=APPS, verbose_name=_('Nombre'))
    slug = models.CharField(max_length=20, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for ContextApp."""
        verbose_name = _('Contexto')
        verbose_name_plural = _('Contextos')
        ordering = ['name',]
        unique_together = (('name',),)

    def __str__(self):
        """Unicode representation of ContextApp."""
        return self.name

    def save(self, *args, **kwargs):
        """Save method for ContextApp."""
        old = ContextApp.objects.filter(pk=self.pk).first() if self.pk else None
        # Normalización del nombre
        if self.name:
            self.name = self.name.strip().title()
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.name != old.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for ContextApp."""
        return reverse('common_app:context_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    @property
    def display_name(self):
        if self.slug:
            return f"{self.name} ({self.slug})"
        return self.name


class Genre(models.Model):
    """Model definition for Genre."""
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'is_active': True}, related_name='childrens', on_delete=models.CASCADE, verbose_name=_('Padre'))
    name = models.CharField(max_length=50, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=False, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    explicit = models.BooleanField(default=False, verbose_name=_('Explicito'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    contexts = models.ManyToManyField(ContextApp, related_name='genres_as_contexts', verbose_name=_('ContextAppos'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Genre."""
        verbose_name = _('Género')
        verbose_name_plural = _('Géneros')
        ordering = ['initial', 'name',]

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
        return reverse('common_app:genre_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    @property
    def display_name(self):
        base_name = self.name
        if self.name_esp:
            base_name = f"{self.name} ({self.name_esp})"
        if self.parent:
            return f"{base_name} Nacido de: {self.parent.name}"
        return base_name

    @property
    def get_usage(self):
        apps_list = [app.get_name_display() for app in self.contexts.all()]
        return ", ".join(apps_list) if apps_list else _("No asociado a ninguna aplicación")

    @property
    def get_active(self):
        if self.is_active:
            return _('Sí')
        else:
            return _('No')

    @property
    def get_explicit(self):
        if self.explicit:
            return _('Sí') # Aquí falta algo
        else:
            return _('No') # Y aquí también

    # @property
    # def get_num_movies(self):
    #     return self.movies_as_genre.count()

    # @property
    # def has_music(self):
    #     return _('Sí') if self.music_as_genre.exists() else _('No') # For

    # @property
    # def has_music(self):
    #     return _('Sí') if self.music_as_genre.exists() else _('No') # For

class Type(models.Model):
    """Model definition for Type."""
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={'is_active': True}, related_name='childrens', on_delete=models.CASCADE, verbose_name=_('Padre'))
    name = models.CharField(max_length=50, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=False, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    contexts = models.ManyToManyField(ContextApp, related_name='types_as_contexts', verbose_name=_('ContextAppos'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Type."""
        verbose_name = _('Tipo Película')
        verbose_name_plural = _('Tipos Películas')
        ordering = ['-created_at', 'name',]

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
        return reverse('movie_app:movie_type_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    @property
    def display_name(self):
        base_name = self.name
        if self.name_esp:
            base_name = f"{self.name} ({self.name_esp})"
        if self.parent:
            return f"{base_name} - Nacido de: {self.parent.name}"
        return base_name

    @property
    def get_usage(self):
        apps_list = [app.get_name_display() for app in self.contexts.all()]
        return ", ".join(apps_list) if apps_list else _("No asociado a ninguna aplicación")

    @property
    def get_active(self):
        if self.is_active:
            return _('Sí')
        else:
            return _('No')


    # def get_num_movies(self):
    #     return self.movies_as_types.count()


class Rating(models.Model):
    """Model definition for Rating."""
    acronym = models.CharField(max_length=15, unique=False, null=False, blank=False, verbose_name=_('Acrónimo'))
    name = models.CharField(max_length=60, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=60, unique=False, null=True, blank=True, verbose_name=_('Nombre Español'))
    slug = models.SlugField(max_length=60, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    contexts = models.ManyToManyField(ContextApp, related_name='ratings_as_contexts', verbose_name=_('ContextAppos'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Rating."""
        verbose_name = _('Clasificación')
        verbose_name_plural = _('Clasificaciones')
        ordering = ['acronym', 'name',]

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
        return reverse('movie_app:rating_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    # custom methods
    @property
    def display_name(self):
        base_name = self.name
        if self.name_esp:
            base_name = f"{self.acronym} - {self.name} ({self.name_esp})"
        return base_name

    @property
    def get_usage(self):
        apps_list = [app.get_name_display() for app in self.contexts.all()]
        return ", ".join(apps_list) if apps_list else _("No asociado a ninguna aplicación")

    @property
    def get_active(self):
        if self.is_active:
            return _('Sí')
        else:
            return _('No')

class Status(models.Model):
    """Model definition for Status."""
    name = models.CharField(max_length=50, unique=False, null=False, blank=False, verbose_name=_('Nombre'))
    name_esp = models.CharField(max_length=50, unique=False, null=True, blank=True, verbose_name=_('Nombre Español'))
    initial = models.CharField(max_length=1, unique=False, null=False, blank=True, editable=False, verbose_name=_('Inicial'))
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    description = models.TextField(blank=True, verbose_name=_('Descripción'))
    contexts = models.ManyToManyField(ContextApp, related_name='status_as_contexts', verbose_name=_('ContextAppos'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for Status."""
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')
        ordering = ['name',]

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

    # custom methods
    @property
    def display_name(self):
        base_name = self.name
        if self.name_esp:
            base_name = f"{self.name} ({self.name_esp})"
        return base_name

    @property
    def get_usage(self):
        apps_list = [app.get_name_display() for app in self.contexts.all()]
        return ", ".join(apps_list) if apps_list else _("No asociado a ninguna aplicación")

    @property
    def get_active(self):
        if self.is_active:
            return _('Sí')
        else:
            return _('No')