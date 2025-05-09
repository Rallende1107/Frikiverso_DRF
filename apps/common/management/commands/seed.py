from django.core.management.base import BaseCommand

from apps.common.utils.seed import run as seed_common
from apps.movie.utils.seed import run as seed_movie
from apps.music.utils.seed import run as seed_music
from apps.otaku.utils.seed import run as seed_otaku
from apps.renpy.utils.seed import run as seed_renpy
from apps.serie.utils.seed import run as seed_serie

class Command(BaseCommand):
    help = "Carga datos iniciales para todas las apps"

    def handle(self, *args, **kwargs):
        self.stdout.write("Cargando datos iniciales...")

        seed_common()
        seed_movie()
        seed_music()
        seed_otaku()
        seed_renpy()
        seed_serie()

        self.stdout.write(self.style.SUCCESS("✅ Seed completado exitosamente."))
