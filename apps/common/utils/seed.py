from apps.common.models import Country, Format, ImageSize, Language, Quality, Website
from .base_data import (
    default_common_size_imanges,
    default_common_qualities,
    default_common_formats,
    default_common_websites,
    default_common_countries,
    default_common_languages,
)

def run():

    if ImageSize and default_common_size_imanges:
        print("➤ Seed: Tamaños de Imágenes")
        seed_defaults_size_imanges(ImageSize, default_common_size_imanges)
        print("✅ Tamaños de Imágenes cargados correctamente")

    if Quality and default_common_qualities:
        print("➤ Seed: Calidades")
        seed_defaults_calidades(Quality, default_common_qualities)
        print("✅ Calidades cargados correctamente")

    if Format and default_common_formats:
        print("➤ Seed: Formatos")
        seed_defaults_formatos(Format, default_common_formats)
        print("✅ Formatos cargados correctamente")

    if Website and default_common_websites:
        print("➤ Seed: Sitios Web")
        seed_defaults_websites(Website, default_common_websites)
        print("✅ Sitios Web cargados correctamente")

    if Country and default_common_countries:
        print("➤ Seed: Países")
        seed_defaults_countries(Country, default_common_countries)
        print("✅ Países cargados correctamente")

    if Language and default_common_languages:
        print("➤ Seed: Idiomas")
        seed_defaults_languages(Language, default_common_languages)
        print("✅ Idiomas cargados correctamente")

def seed_defaults_size_imanges(modelo, items):
    proceso = 'Cargar Tamaños Imágenes Predeterminados'
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

def seed_defaults_calidades(modelo, items):
    proceso = ' Cargar Calidades Predeterminadas'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().upper()
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

def seed_defaults_formatos(modelo, items):
    proceso = ' Cargar Formatos Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().upper()
        for_video = item.get('for_video')
        for_music = item.get('for_music')
        for_image = item.get('for_image')
        for_document = item.get('for_document')
        for_other = item.get('for_other')
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'for_video' :for_video,
                'for_music' :for_music,
                'for_image' :for_image,
                'for_document' :for_document,
                'for_other' :for_other,
                'is_active' :is_active,
            }
        )

def seed_defaults_websites(modelo, items):
    proceso = ' Sitios Web Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip()
        acronym = item['acronym'].strip().upper()
        URL = item['URL'].strip()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'acronym': acronym,
                'url': URL,
                'is_active': is_active,
            }
        )

def seed_defaults_countries(modelo, items):
    proceso = ' Cargar Paid Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        code = item['code'].strip().upper()
        numeric_code = item['numeric_code']
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'code': code,
                'numeric_code': numeric_code,
                'is_active': is_active,
            }
        )

def seed_defaults_languages(modelo, items):
    proceso = 'Cargar Idiomas Predeterminados'
    for item in items:
        # Normalizamos antes de buscar o insertar
        name = item['name'].strip().title()
        name_esp = item['name_esp'].strip().title()
        acronym = item['acronym'].strip().upper()
        is_active = item.get('is_active')
        # Update or create sobre el campo normalizado
        modelo.objects.update_or_create(
            name=name,
            defaults={
                'name_esp': name_esp,
                'acronym': acronym,
                'is_active': is_active,
            }
        )

