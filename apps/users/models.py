# Imports estándar de Python
import os, uuid
from datetime import date
# Imports de terceros (Django, PIL, etc.)
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage
# Imports locales del proyecto
from core.models import BaseLog, YearField
from core.utils.utils import obtener_inicial
from .utils.uploads import user_img_upload_path
# Create your models here.

########################################################################################################    Log
class UserLog(BaseLog):
    """Model definition for UserLog."""

    class Meta:
        """Meta definition for UserLog."""
        verbose_name = _('Log Usuario')
        verbose_name_plural = _('Logs Usuarios')
        ordering = ['-timestamp']
        unique_together = (('level', 'process', 'timestamp',),)
        db_table = 'log_Usuario'

########################################################################################################    CustomUser
class CustomUser(AbstractUser):
    """Model definition for CustomUser."""
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Apellidos')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Correo Electrónico')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    birth_year = YearField(blank=True, null=True, verbose_name='Año nacimiento')
    avatar = models.ImageField(upload_to=user_img_upload_path,height_field=None, width_field=None, max_length=None, blank=True,  verbose_name='Avatar')
    slug = models.SlugField(max_length=150, unique=True, null=False, blank=True, editable=False, verbose_name=_('Nombre Slug'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        """Meta definition for CustomUser."""
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ['-created_at', 'username']
        unique_together = [['username', 'email']]

    def __str__(self):
        """Unicode representation of CustomUser."""
        return f'{self.username} - {self.email}'

    def save(self, *args, **kwargs):
        """Save method for CustomUser."""
        # Obtener el objeto original si existe
        old = CustomUser.objects.filter(pk=self.pk).first() if self.pk else None
        # Slug automático si está vacío o el nombre cambió
        if not self.slug or (old and self.username != old.username):
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Genre."""
        return reverse('users_app:user_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    # custom methods
    def get_edad_by_year(self):
        if self.birth_year:
            today = date.today()
            age = today.year - self.birth_year
            if today.month < 1 or (today.month == 1 and today.day < 1):
                age -= 1
            return age
        return _('Desconocida')

    def get_edad(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return _('Desconocida')

    def get_img_url(self):
        if self.avatar:
            return settings.MEDIA_URL + str(self.avatar)
        return None

