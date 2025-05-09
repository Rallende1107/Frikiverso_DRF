from apps.movie.models import Genre, Type, Role, Rating
from .base_data import (
    default_movie_genres,
    default_movie_types,
    default_movie_roles,
    default_movie_ratings,
)

def run():

    if Genre and default_movie_genres:
        print("➤ Seed: Géneros de Películas")
        seed_default_movie_genres(Genre, default_movie_genres)
        print("✅ Géneros de Películas cargados correctamente")

    if Type and default_movie_types:
        print("➤ Seed: Tipos de Películas")
        seed_default_movie_types(Type, default_movie_types)
        print("✅ Tipos de Películas cargados correctamente")

    if Role and default_movie_roles:
        print("➤ Seed: Roles de Películas")
        seed_default_movie_roles(Role, default_movie_roles)
        print("✅ Roles de Películas cargados correctamente")

    if Rating and default_movie_ratings:
        print("➤ Seed: Clasificaciones de Películas")
        seed_default_movie_ratings(Rating, default_movie_ratings)
        print("✅ Clasificaciones de Películas cargados correctamente")


def seed_default_movie_genres(modelo, items):
    proceso= 'Cargar Géneros de Películas Predeterminados'
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

def seed_default_movie_types(modelo, items):
    proceso= 'Cargar Tipos de Películas Predeterminados'
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

def seed_default_movie_roles(modelo, items):
    proceso= 'Cargar Roles de Películas Predeterminados'
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

def seed_default_movie_ratings(modelo, items):
    proceso= 'Cargar Clasificaciones de Películas Predeterminadas'
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
