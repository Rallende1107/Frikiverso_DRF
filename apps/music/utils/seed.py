from apps.music.models import Genre, Role, AlbumType, ArtistType
from .base_data import (
    default_music_genres,
    default_music_roles,
    default_music_albums_types,
    default_music_artist_types,
)

def run():

    if Genre and default_music_genres:
        print("➤ Seed: Géneros de Musicales")
        seed_default_music_genres(Genre, default_music_genres)
        print("✅ Géneros de Musicales cargados correctamente")

    if Role and default_music_roles:
        print("➤ Seed: Roles Musicales")
        seed_default_music_roles(Role, default_music_roles)
        print("✅ Roles Musicales cargados correctamente")

    if AlbumType and default_music_albums_types:
        print("➤ Seed: Tipos de Albumnes")
        seed_default_music_albums_types(AlbumType, default_music_albums_types)
        print("✅ Tipos de Albumnes cargados correctamente")

    if ArtistType and default_music_artist_types:
        print("➤ Seed: Tipos de Artistas")
        seed_default_music_artist_types(ArtistType, default_music_artist_types)
        print("✅ Tipos de Artistas cargados correctamente")



def seed_default_music_genres(modelo, items):
    proceso= 'Cargar Géneros Musicales Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'is_active': active,
            }
        )

def seed_default_music_roles(modelo, items):
    proceso= 'Cargar Roles Musicales Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'is_active': is_active,
            }
        )

def seed_default_music_albums_types(modelo, items):
    proceso= 'Cargar Tipos de Albumnes Musicales Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'is_active': is_active,
            }
        )

def seed_default_music_artist_types(modelo, items):
    proceso= 'Cargar Tipos de Artistas Musicales Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'is_active': is_active,
            }
        )
