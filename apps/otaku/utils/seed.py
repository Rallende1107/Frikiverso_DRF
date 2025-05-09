from datetime import datetime

from apps.otaku.models import Role, Year, Genre, Theme, Demographic, Type, Rating, Season, Status, Source, RelationType, SeasonFull
from .base_data import (
    default_otaku_genres,
    default_otaku_themes,
    default_otaku_demographics,
    default_otaku_types,
    default_otaku_ratings,
    default_otaku_seasons,
    default_otaku_status,
    default_otaku_sources,
    default_otaku_relations_types,
    default_otaku_roles,
)

def run():

    if Role and default_otaku_roles:
        print("➤ Seed: Roles Otaku")
        seed_default_otaku_roles(Role, default_otaku_roles)
        print("✅ Roles Otaku cargados correctamente")

    if Year:
        print("➤ Seed: Años Otaku")
        seed_default_otaku_years(Year)
        print("✅ Años Otaku cargados correctamente")

    if Genre and default_otaku_genres:
        print("➤ Seed: Géneros Otaku")
        seed_default_otaku_genres(Genre, default_otaku_genres)
        print("✅ Géneros cargados correctamente")

    if Theme and default_otaku_themes:
        print("➤ Seed: Temas Otaku")
        seed_default_otaku_themes(Theme, default_otaku_themes)
        print("✅ Temas Otaku cargados correctamente")

    if Demographic and default_otaku_demographics:
        print("➤ Seed: Demografías Otaku")
        seed_default_otaku_demographics(Demographic, default_otaku_demographics)
        print("✅ Demografías Otaku cargados correctamente")

    if Type and default_otaku_types:
        print("➤ Seed: Tipos Otaku")
        seed_default_otaku_types(Type, default_otaku_types)
        print("✅ Tipos Otaku cargados correctamente")

    if Rating and default_otaku_ratings:
        print("➤ Seed: Clasificaciones Otaku")
        seed_default_otaku_ratings(Rating, default_otaku_ratings)
        print("✅ Clasificaciones Otaku cargados correctamente")

    if Season and default_otaku_seasons:
        print("➤ Seed: Temporadas Otaku")
        seed_default_otaku_seasons(Season, default_otaku_seasons)
        print("✅ Temporadas Otaku cargados correctamente")

    if Status and default_otaku_status:
        print("➤ Seed: Estados Otaku")
        seed_default_otaku_status(Status, default_otaku_status)
        print("✅ Estados Otaku cargados correctamente")

    if Source and default_otaku_sources:
        print("➤ Seed: Fuentes Otaku")
        seed_default_otaku_sources(Source, default_otaku_sources)
        print("✅ Fuentes Otaku cargados correctamente")

    if RelationType and default_otaku_relations_types:
        print("➤ Seed: Tipos de Relaciones Otaku")
        seed_default_otaku_relations_types(RelationType, default_otaku_relations_types)
        print("✅ Tipos de Relaciones Otaku cargados correctamente")

    if SeasonFull and (Season and Year):
        seasons = Season.objects.all()
        years = Year.objects.all().order_by('id')
        if seasons and years:
            print("➤ Seed: Temporadas Completas Otaku")
            seed_default_otaku_seasons_full(SeasonFull, years, seasons)
            print("✅ Temporadas Completas Otaku cargados correctamente")



def seed_default_otaku_roles(modelo, items):
    proceso = 'Cargar Roles Otaku Predeterminadas'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        description = item['description'].strip()
        role_staff = item.get('role_staff')
        role_chara = item.get('role_chara')
        role_manga = item.get('role_manga')
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            # acronym=acronym,
            name=name,
            defaults={
                'name_esp': name_esp,
                'role_staff':role_staff,
                'role_chara':role_chara,
                'role_manga':role_manga,
                'is_active':is_active,
                'description':description,
            }
        )

def seed_default_otaku_years(modelo):
    proceso = 'Cargar Años Otaku Predeterminadas'
    this_year = datetime.now().year
    first_year = 1960
    years_to_insert = range(first_year, this_year+4)
    for y in years_to_insert:
        modelo.objects.update_or_create(year=y)

def seed_default_otaku_genres(modelo, items):
    proceso = 'Cargar Géneros Otaku Predeterminados'
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
                'name_esp': name_esp,
                'explicit': explicit,
                'is_active': is_active,
                'description': description,
            }
        )

def seed_default_otaku_themes(modelo, items):
    proceso = 'Cargar Temas Otaku Predeterminados'
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
                'description': description,
                'is_active': is_active,
                'explicit': explicit,
            }
        )

def seed_default_otaku_demographics(modelo, items):
    proceso = 'Cargar Demografías Otaku Predeterminadas'
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

def seed_default_otaku_types(modelo, items):
    proceso = 'Cargar Tipos Otaku Predeterminados'
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

def seed_default_otaku_ratings(modelo, items):
    proceso = 'Cargar Clasificaciones Otaku Predeterminadas'
    for item in items:
        # Normalizamos antes de buscar o insertar
        acronym = item['acronym'].strip().upper()
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        description = item['description'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            acronym=acronym,
            name=name,
            defaults={
                'name_esp': name_esp,
                'description': description,
                'is_active': is_active,
            }
        )

def seed_default_otaku_seasons(modelo, items):
    proceso = 'Cargar Temporadas Otaku Predeterminadas'
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

def seed_default_otaku_status(modelo, items):
    proceso = 'Cargar Estados Otaku Predeterminados'
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

def seed_default_otaku_sources(modelo, items):
    proceso = 'Cargar Fuentes Otaku Predeterminadas'
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

def seed_default_otaku_relations_types(modelo, items):
    proceso = 'Cargar Tipo de Relaciones Otaku Predeterminadas'
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
                'description':description,
                'is_active':is_active,
            }
        )

def seed_default_otaku_seasons_full(modelo, anios, temporadas):
    proceso = 'Cargar Temporadas Completas Otaku Predeterminadas'

    for year in anios:
        for season in temporadas:
            if season.name.strip().lower() == 'unknown':
                continue  # Saltar esta iteración si la temporada es "desconocida"

            name = f"{season.name} {year.year}"
            name_esp = f"{season.name_esp or season.name} {year.year}"

            modelo.objects.update_or_create(
                name=name,
                defaults={
                    'name_esp': name_esp,
                }
            )