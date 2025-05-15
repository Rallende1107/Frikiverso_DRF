# Imports estándar de Python
import os, uuid
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
from core.models import BaseLog
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
    numeric_code = models.PositiveIntegerField(null=False, blank=True, default=0, verbose_name=_('Código Numerico'))
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
        return None

########################################################################################################    Modelo para PersonImage
class PersonImage(models.Model):
    """Model definition for PersonImage."""
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_as_images', on_delete=models.CASCADE, verbose_name=_('Persona'))
    size_image = models.ForeignKey(ImageSize, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_images_as_sizes', on_delete=models.PROTECT, verbose_name=_('Tamaño'))
    image = models.ImageField(blank=False, null=False, upload_to=person_image_path, verbose_name=_('Imagen Persona'))
    image_url = models.URLField(max_length=2000, blank=True, null=True, verbose_name=_('URL'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PersonImage."""
        verbose_name = _('Imagen Persona')
        verbose_name_plural = _('Imágenes Personas')
        ordering = ['person', 'size_image', 'name',]
        unique_together = (('person', 'size_image', 'name',),)

    def __str__(self):
        """Unicode representation of PersonImage."""
        return self.name if self.person else _('Imagen sin Persona')

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)  # Guardar primero para que self.image.name sea definitivo

        filename = os.path.basename(self.image.name) if self.image else None

        # Actualizar name y slug si es necesario
        updated_fields = []

        if filename and (not self.name or self.name != filename):
            self.name = filename
            updated_fields.append('name')

        if self.name and (not self.slug or slugify(self.name) != self.slug):
            self.slug = slugify(self.name) or str(uuid.uuid4())
            updated_fields.append('slug')

        # Guardar solo si se modificó algo
        if updated_fields:
            super().save(update_fields=updated_fields)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for PersonImage."""
        return reverse('common_app:person_image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

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

########################################################################################################    Modelo para PersonImageExtra
class PersonImageExtra(models.Model):
    """Model definition for PersonImageExtra."""
    person = models.ForeignKey(Person, blank=False, null=False, limit_choices_to={'is_active': True}, related_name='persons_as_exta_images', on_delete=models.CASCADE, verbose_name=_('Persona'))
    image = models.ImageField(blank=False, null=False, upload_to=person_image_extra_path, verbose_name=_('Imagen Extra Persona'))
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, editable=False, verbose_name=_('Nombre'))
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creado'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Actualizado'))

    class Meta:
        """Meta definition for PersonImageExtra."""
        verbose_name = _('Imágen extra persona')
        verbose_name_plural = _('Imágenes extras de personas')
        ordering = ['person', 'name',]
        unique_together = (('person', 'name',),)

    def __str__(self):
        """Unicode representation of PersonImageExtra."""
        return self.name if self.person else _('Imagen sin Persona')

    def save(self, *args, **kwargs):
        """Save method for PersonImageExtra."""
        old = PersonImageExtra.objects.filter(pk=self.pk).first() if self.pk else None
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
        """Return absolute url for PersonImageExtra."""
        return reverse('common_app:person_image_extra_detail', kwargs={'pk': self.pk, 'slug': self.slug})

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
