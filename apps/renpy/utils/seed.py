from apps.renpy.models import Genre, GameEngine, Censorship, Prefix, Status, Platform
from .base_data import (
    default_renpy_engines,
    default_renpy_status,
    default_renpy_genres,
    default_renpy_platforms,
    default_renpy_prefix,
    default_renpy_censored,
)


def run():


    if Genre and default_renpy_genres:
        print("➤ Seed: Géneros Ren\'py Predeterminados")
        seed_default_renpy_genres(Genre, default_renpy_genres)
        print("✅ Géneros Ren\'py cargados correctamente")

    if GameEngine and default_renpy_engines:
        print("➤ Seed: Motores de Desarrollo Predeterminados")
        seed_default_renpy_engines(GameEngine, default_renpy_engines)
        print("✅ Motores de Desarrollo cargados correctamente")

    if Censorship  and default_renpy_censored:
        print("➤ Seed: Censuras Predeterminados")
        seed_default_renpy_censored(Censorship, default_renpy_censored)
        print("✅ Censuras cargados correctamente")

    if Prefix and default_renpy_prefix:
        print("➤ Seed: Prefijos Predeterminados")
        seed_default_renpy_prefix(Prefix, default_renpy_prefix)
        print("✅ Prefijos cargados correctamente")

    if Status and default_renpy_status:
        print("➤ Seed: Estados Predeterminados")
        seed_default_renpy_status(Status, default_renpy_status)
        print("✅ Estados cargados correctamente")


    if Platform and default_renpy_platforms:
        print("➤ Seed: Plataformas Predeterminados")
        seed_default_renpy_platforms(Platform, default_renpy_platforms)
        print("✅ Plataformas cargados correctamente")


def seed_default_renpy_engines(modelo, items):
    proceso = ('Cargar Motores de Desarrollo Predeterminados')
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip()
        description = item['description'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'description': description,
                'is_active': is_active,
            }
        )

def seed_default_renpy_status(modelo, items):
    proceso = ('Cargar Predeterminados')
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        description = item['description'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'is_active': is_active,
            }
        )

def seed_default_renpy_genres(modelo, items):
    proceso = ('Cargar Géneros Ren\'py Predeterminados')
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip()
        name_esp = item['name_esp'].strip()
        explicit = item.get('explicit')
        is_active = item.get('is_active')
        description = item['description'].strip()
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'explicit': explicit,
                'is_active': is_active,
            }
        )

def seed_default_renpy_platforms(modelo, items):
    proceso = ('Cargar Predeterminados')
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name_esp'].strip()
        name_esp = item['name_esp'].strip()
        description = item['description'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'is_active': is_active,
            }
        )

def seed_default_renpy_prefix(modelo, items):
    proceso = ('Cargar Predeterminados')
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip()
        name_esp = item['name_esp'].strip()
        description = item['description'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'is_active': is_active,
            }
        )

def seed_default_renpy_censored(modelo, items):
    proceso = ('Cargar Predeterminados')
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip()
        name_esp = item['name_esp'].strip()
        description = item['description'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'is_active': is_active,
            }
        )

