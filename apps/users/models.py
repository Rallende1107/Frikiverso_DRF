from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from core.utils.utils import YearField
from .utils.uploads import user_img_upload_path
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    """Model definition for CustomUser."""
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Apellidos')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Correo Electrónico')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    birth_year = YearField(blank=True, null=True, verbose_name='Año nacimiento')
    avatar = models.ImageField(upload_to=user_img_upload_path,height_field=None, width_field=None, max_length=None, blank=True,  verbose_name='Avatar')
    address = models.CharField(max_length=250,null=True, blank=True, verbose_name='Teléfono')
    acepto_terminos = models.BooleanField(verbose_name='Acepta Términos', default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    def __str__(self):
        """Unicode representation of CustomUser."""
        return f'{self.username} - {self.first_name} {self.last_name}, {self.email}'

    def get_edad_by_year(self):
        if self.birth_year:
            today = date.today()
            age = today.year - self.birth_year
            if today.month < 1 or (today.month == 1 and today.day < 1):
                age -= 1
            return age
        return 'Desconocida'

    def get_edad(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return 'Desconocida'


    def get_img_url(self):
        if self.avatar:
            return settings.MEDIA_URL + str(self.avatar)
        return None

    class Meta:
        """Meta definition for CustomUser."""
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at', 'username']
        unique_together = [['username', 'email']]