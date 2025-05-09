from apps.serie.models import Genre, Type, Role, Rating
from .base_data import (
    default_serie_genres,
    default_serie_types,
    default_serie_roles,
    default_serie_ratings,
)


def run():

    if Genre and default_serie_genres:
        print("➤ Seed: Géneros de Series")
        seed_default_serie_genres(Genre, default_serie_genres)
        print("✅ Géneros de Series cargados correctamente")

    if Type and default_serie_types:
        print("➤ Seed: Tipos de Series")
        seed_default_serie_types(Type, default_serie_types)
        print("✅ Tipos de Series cargados correctamente")

    if Role and default_serie_roles:
        print("➤ Seed: Roles de Series")
        seed_default_serie_roles(Role, default_serie_roles)
        print("✅ Roles de Series cargados correctamente")

    if Rating and default_serie_ratings:
        print("➤ Seed: Clasificaciones de Series")
        seed_default_serie_ratings(Rating, default_serie_ratings)
        print("✅ Clasificaciones de Series cargados correctamente")


def seed_default_serie_genres(modelo, items):
    proceso= 'Cargar Géneros de Series Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        description = item['description'].strip()
        is_active = item.get('is_active')
        explicit = item.get('explicit')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'is_active': is_active,
                'explicit': explicit,
                'description': description,
            }
        )

def seed_default_serie_types(modelo, items):
    proceso= 'Cargar Tipos de Series Predeterminados'
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

def seed_default_serie_roles(modelo, items):
    proceso= 'Cargar Roles de Series Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        description = item['description'].strip()
        role_cast = item.get('role_cast')
        role_staff = item.get('role_staff')
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'role_cast': role_cast,
                'role_staff': role_staff,
                'is_active': is_active,
            }
        )

def seed_default_serie_ratings(modelo, items):
    proceso= 'Cargar Clasificaciones de Series Predeterminadas'
    for item in items:
        # Normalizamos antes de buscar o insertar
        acronym = item['acronym'].strip().upper()
        name = item['name'].strip()
        name_esp = item['name_esp'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            acronym=acronym,  # Filtro de búsqueda
            defaults={
                'name': name,
                'name_esp': name_esp,
                'is_active': is_active,
            }
        )
