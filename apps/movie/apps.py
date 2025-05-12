from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.movie'
    verbose_name = "Películas"  # Este es el nombre que aparecerá en el admin
