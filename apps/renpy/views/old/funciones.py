import os
import re
import asyncio
from io import BytesIO
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from channels.db import database_sync_to_async  # O usa asgiref.sync.sync_to_async
from asgiref.sync import sync_to_async
from PIL import Image
from django.core.files.base import ContentFile

from apps.core.models import Language
from .models import GenreRenpy, Developer, Game, GameEngine, GameState, Platform, GameImage, DeveloperLink
from .utils import *
# Cargar variables de entorno desde el archivo .env
load_dotenv()
F95_USER = os.getenv("F95USER")
F95_PASS = os.getenv("F95PASS")

import re
import random
from .models import Game


def process_f95_url(f95_url):
    """
    Procesa una URL de F95Zone y devuelve una URL corta y el ID de la publicación.

    Args:
        f95_url (str): La URL completa de F95Zone.

    Returns:
        tuple: Una tupla que contiene la URL corta y el ID extraído.
    """
    # Usa expresiones regulares para extraer el ID de la URL
    match = re.search(r'(\d+)(?=/)', f95_url)  # Captura el primer número antes de la barra '/'
    if match:
        post_id = match.group(1)  # El ID es el primer grupo de la expresión regular
        short_url = f'https://f95zone.to/threads/{post_id}/'
        return short_url, post_id
    else:
        return None, None  # Devuelve None si no se encuentra un ID



def generate_unique_negative_id():
    """
    Genera un número negativo único que no existe en la tabla Game.
    """
    while True:
        negative_id = random.randint(-1_000_000, -1)
        if not Game.objects.filter(f95_id=negative_id).exists():
            return negative_id


@sync_to_async
def save_languages(language_names):
    languages = []
    for lang_name in language_names:
        lang, created = Language.objects.get_or_create(name=lang_name)
        languages.append(lang)
    return languages

@sync_to_async
def save_developers(developer_names, developer_info):
    developers = []
    for dev_name in developer_names:
        dev, created = Developer.objects.get_or_create(name=dev_name)
        developers.append(dev)

        # Si hay información adicional del desarrollador, procesar los enlaces
        if developer_info:
            # Obtener el nombre principal del desarrollador si está disponible
            main_developer_name = developer_info.get('main_developer')

            # Si no hay un main_developer, usar el nombre del primer enlace si existe
            if not main_developer_name and developer_info.get('dev_links'):
                main_developer_name = developer_info['dev_links'][0]['name']

            # Si el nombre coincide con el desarrollador actual, procesar los enlaces
            if main_developer_name == dev_name:
                dev_links = developer_info.get('dev_links', [])
                for dev_link in dev_links:
                    # Crear o actualizar un DeveloperLink relacionado con el desarrollador
                    DeveloperLink.objects.update_or_create(
                        developer=dev,
                        name=dev_link['name'],
                        defaults={'url': dev_link['link']}
                    )

    return developers

@sync_to_async
def save_engines(engine_names):
    engines = []
    for engine_name in engine_names:
        engine, created = GameEngine.objects.get_or_create(name=engine_name)
        engines.append(engine)
    return engines

@sync_to_async
def save_genres(genre_names):
    genres = []
    for genre_name in genre_names:
        genre, created = GenreRenpy.objects.get_or_create(name=genre_name)
        genres.append(genre)
    return genres

@sync_to_async
def save_statuses(status_names):
    statuses = []
    for status_name in status_names:
        status, created = GameState.objects.get_or_create(name=status_name)
        statuses.append(status)
    return statuses

@sync_to_async
def save_platforms(platform_names):
    platforms = []
    for platform_name in platform_names:
        platform, created = Platform.objects.get_or_create(name=platform_name)
        platforms.append(platform)
    return platforms

def descargar_imagenes(url, nombre, ruta):
    print(f"REAA : descargar_imagenes")
    """
    Descarga una imagen desde la URL. Si la imagen ya está en formato WebP o GIF, la guarda sin conversión.
    Si la imagen tiene otro formato, intenta convertirla a WebP. Si la conversión falla, la guarda en su formato original.

    Args:
        url (str): La URL desde la cual se descargará la imagen.
        nombre (str): El nombre del archivo de imagen (incluyendo la extensión original).
        ruta (str): La ruta donde se guardará la imagen descargada.

    Returns:
        ContentFile or None: El archivo de imagen guardado como un ContentFile, o None en caso de error.
    """
    # Eliminar parámetros de URL y obtener nombre base
    nombre_sin_extension = re.sub(r'[?].*$', '', nombre)
    extension = nombre_sin_extension.split('.')[-1].lower()
    nombre_base = nombre_sin_extension.rsplit('.', 1)[0]
    print(nombre_sin_extension)

    # Si la imagen es WebP o GIF, simplemente descargarla sin convertirla
    try:
        response = requests.get(url)
        if response.status_code == 200:
            imagen_bytes = response.content
            if extension in ['webp', 'gif']:
                # Retornar la imagen descargada como ContentFile
                return ContentFile(imagen_bytes, name=nombre_sin_extension)

            # Intentar convertir la imagen a WebP
            try:
                # Crear una imagen a partir del contenido descargado
                imagen = Image.open(BytesIO(imagen_bytes))
                imagen = imagen.convert("RGBA")  # Convertir a RGBA para asegurar compatibilidad

                # Guardar la imagen en formato WebP
                with BytesIO() as output:
                    imagen.save(output, "WEBP")
                    imagen_bytes_webp = output.getvalue()

                # Retornar la imagen convertida como ContentFile
                nombre_webp = nombre_base + '.webp'
                return ContentFile(imagen_bytes_webp, name=nombre_webp)

            except Exception as e:
                print(f"Error al convertir la imagen a WebP: {str(e)}")
                # Si la conversión falla, retornar la imagen original
                return ContentFile(imagen_bytes, name=nombre_sin_extension)
        else:
            print(f"Error al descargar la imagen: Código de estado {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al descargar o convertir la imagen: {str(e)}")
        return None

@sync_to_async
def save_cover_image(cover_url, game_instance):
    # path = os.path.join('renpy', 'img', 'game', 'cover')  # Ruta donde se guardará la imagen
    path = 'renpy/img/game/cover'  # Ruta donde se guardará la imagen (relativa a MEDIA_URL)

    if not cover_url:
        print("No se proporcionó una URL para la portada.")
        return False  # Si no hay URL, no hacer nada

    # Obtener el nombre del archivo de la URL
    nombre_archivo = cover_url.split('/')[-1]

    # Verificar si el juego ya tiene una imagen de portada
    if game_instance.cover:
        # Obtener el nombre del archivo de la portada actual
        existing_image_name = os.path.basename(game_instance.cover.name)

        # Si la imagen existente tiene el mismo nombre que la nueva, no hacer nada
        if existing_image_name == nombre_archivo:
            print("La imagen de portada ya existe y es la misma. No se realizará ninguna acción.")
            return False

        # Si la imagen es diferente, eliminar la portada anterior
        try:
            # Borrar el archivo físico si existe
            if os.path.exists(game_instance.cover.path):
                os.remove(game_instance.cover.path)
                print(f"Imagen anterior eliminada: {game_instance.cover.path}")

            # Eliminar la referencia en el modelo
            game_instance.cover.delete(save=False)
            print("La imagen anterior ha sido eliminada del modelo.")
        except Exception as e:
            print(f"Error al eliminar la imagen existente: {str(e)}")

    # Descargar la nueva imagen utilizando el método de descarga existente
    imagen_file = descargar_imagenes(cover_url, nombre_archivo, path)

    if imagen_file:
        # Guardar la nueva imagen en el campo 'cover' del juego
        game_instance.cover.save(nombre_archivo, imagen_file)
        print(f"Portada guardada: {game_instance.cover.url}")
        return True
    else:
        print(f"Error al descargar la imagen de portada desde {cover_url}")
        return False
        print(f"Error al descargar la imagen de portada desde {cover_url}")

@sync_to_async
def create_game_instance(datos_scraping):
    # Crear el juego usando sync_to_async
    new_game, created = Game.objects.get_or_create(
        f95_id=datos_scraping['F95_ID'],
        defaults={
            'f95zone_link': datos_scraping['URL'],
            'title': datos_scraping['title'],
            'version': datos_scraping['version'],
            'version_txt': datos_scraping['version_text'],
            'release_date': datos_scraping['release_date'],
            'synopsis': datos_scraping['synopsis'],
            'background': datos_scraping['background'],
            'censored': datos_scraping['censored'],
        }
    )
    # Si el objeto ya existía, actualizar los campos manualmente
    if not created:
        new_game.f95zone_link = datos_scraping['URL']
        new_game.title = datos_scraping['title']
        new_game.version = datos_scraping['version']
        new_game.version_txt = datos_scraping['version_text']
        new_game.release_date = datos_scraping['release_date']
        new_game.synopsis = datos_scraping['synopsis']
        new_game.background = datos_scraping['background']
        new_game.censored = datos_scraping['censored']
        new_game.save()

    return new_game, created

@sync_to_async
def save_additional_images(image_urls, game_instance):
    # Especificar la carpeta de destino para las imágenes adicionales
    path = os.path.join('renpy', 'img', 'game', 'image')

    # Crear el directorio si no existe
    if not os.path.exists(path):
        os.makedirs(path)

    # Eliminar todas las imágenes adicionales asociadas con el juego
    existing_images = GameImage.objects.filter(game=game_instance)
    for existing_image in existing_images:
        try:
            # Borrar la imagen anterior del sistema de archivos
            if os.path.exists(existing_image.img.path):
                os.remove(existing_image.img.path)
                print(f"Imagen existente eliminada: {existing_image.img.path}")

            # Eliminar el objeto de la base de datos
            existing_image.delete()
            print(f"Imagen existente eliminada de la base de datos para {game_instance.title}")
        except Exception as e:
            print(f"Error al eliminar la imagen existente para {game_instance.title}: {str(e)}")

    # Descargar y guardar las nuevas imágenes
    for image_url in image_urls:
        try:
            # Extraer el nombre del archivo de la URL
            nombre_archivo = image_url.split('/')[-1]

            # Descargar la imagen utilizando la función existente
            imagen_file = descargar_imagenes(image_url, nombre_archivo, path)

            if imagen_file:
                # Crear un nuevo objeto GameImage y asociarlo con el juego
                game_image = GameImage(game=game_instance, img=imagen_file)
                game_image.save()
                print(f"Imagen adicional guardada para {game_instance.title}: {game_image.img.url}")
            else:
                print(f"Error al descargar la imagen desde {image_url}")

        except Exception as e:
            # Captura cualquier error que ocurra al procesar cada imagen
            print(f"Error al guardar la imagen {nombre_archivo} para {game_instance.title}: {str(e)}")

@sync_to_async
def set_many_to_many_relations(game_instance, developers, statuses, engines, genres, platforms, languages):
    game_instance.developer.set(developers)
    game_instance.state.set(statuses)
    game_instance.engine.set(engines)
    game_instance.genres.set(genres)
    game_instance.platforms.set(platforms)
    game_instance.original_language.set(languages)
    game_instance.save()


async def save_game_data(datos_scraping):
    try:
        # developers = await save_developers(datos_scraping['developer'])
        developers = await save_developers(datos_scraping['developer'], datos_scraping.get('developer_info'))
        statuses = await save_statuses(datos_scraping['gameState'])
        engines = await save_engines(datos_scraping['Engine'])
        genres = await save_genres(datos_scraping['genres'])
        platforms = await save_platforms(datos_scraping['platforms'])
        languages = await save_languages(datos_scraping['language'])
        new_game, created = await create_game_instance(datos_scraping)
        await set_many_to_many_relations(new_game, developers, statuses, engines, genres, platforms, languages)

        # Guardar la imagen de portada
        await save_cover_image(datos_scraping.get('coverimg'), new_game)
        # Guardar imágenes adicionales si existen
        if 'images' in datos_scraping and datos_scraping['images']:
            await save_additional_images(datos_scraping['images'], new_game)

        print(f"Juego guardado: {new_game.title}")

    except Exception as e:
        print(f"Error al guardar el juego {datos_scraping['title']}: {str(e)}")


async def scrape_data_range(page, start_id, end_id):
    print('scrape_data_range')
    base_url = 'https://f95zone.to/threads/'

    for f95_id in range(start_id, end_id + 1):
        url = f"{base_url}{f95_id}/"
        # print(f"Accediendo a: {url}")

        # Navegar a la URL actual
        await page.goto(url)
        # Esperar a que la página se cargue completamente
        await page.wait_for_load_state('load')

        # Obtener el contenido HTML de la página
        html = await page.content()

        if html:
            soup = BeautifulSoup(html, 'html.parser')
            # Validar la página antes de extraer datos
            if validate_page(soup, f95_id):
                # Si la página es válida, proceder con la extracción de datos
                full_title, categories, status = get_title_categories(soup)  # OK
                full_title = clear_title(full_title, categories)  # OK
                title_title, title_version, title_developer = get_title_data(full_title)  # OK
                tags = get_tags(soup)  # OK
                full_overview, overview_main, overview_extra = get_overviews(soup)  # OK
                cover = get_first_image(soup)  # OK
                thread_updated_date = get_thread_updated(soup)
                release_date = get_release_date(soup)
                date_updated_date = standardize_date(thread_updated_date)
                date_release_date = standardize_date(release_date)
                developer = get_developer(soup)  # OK
                version = get_version(soup)  # OK
                language = get_language(soup)  # OK
                censored = get_censored(soup)  # OK
                platforms = get_platforms(soup)  # OK
                voices = get_voices(soup)  # OK
                developer_info = get_developer_info(soup) # OK
                genres_info = get_genres_info(soup)  # OK
                images = get_images(soup)
                dev = []
                statu = []
                languages = []
                final_title = ''
                final_version = ''
                genres_set = set()
                synopsis = ''
                background = ''
                final_release_date = None
                final_censored = ''
                final_year = None

                # Agregar los tags, asegurando que no haya duplicados y capitalizando correctamente
                if tags:
                    genres_set.update(tag.title() for tag in tags)

                # Agregar los genres_info, asegurando que no haya duplicados y capitalizando correctamente
                if genres_info:
                    genres_set.update(genre.title() for genre in genres_info)

                # Unir los arreglos 'language' y 'voices' en un solo arreglo 'languages'
                if language:
                    languages.extend(lang.title() for lang in language)

                if voices:
                    languages.extend(voice.title() for voice in voices)

                # Eliminar categorías de 'genres' si están en 'categories'
                genres = [genre for genre in genres_set if genre not in [category.capitalize() for category in categories]]

                # Eliminar plataformas de 'genres' si están en 'platforms'
                genres = [genre for genre in genres if genre not in [platform.title() for platform in platforms]]

                # Eliminar lenguajes de 'genres' si están en 'languages'
                genres = [genre for genre in genres if genre not in [language.title() for language in languages]]

                if title_version:
                    final_version = title_version
                else:
                    final_version = '0'
                # Si existe una versión extraída del contenido
                if version:
                    # Limpiar la versión si contiene la final_version
                    version_final = version.replace(final_version, "").strip()
                else:
                    version_final = '0'

                if final_title == '':
                    final_title = full_title

                # Limpiar el título si incluye el estado del juego (status)
                if status in title_title:
                    final_title = title_title.replace(status, "").strip()

                # Agregar el desarrollador al arreglo
                if title_developer:
                    dev.append(title_developer)

                # Si el desarrollador extraído del contenido es diferente al del título, agregarlo
                if developer and developer != title_developer:
                    dev.append(developer)

                if status:
                    statu.append(status)

                if overview_main:
                    synopsis = clean_string(overview_main)

                if overview_extra:
                    background = clean_string(overview_extra)

                if censored:
                    final_censored = censored
                else:
                    final_censored = None

                # Asignar la fecha de lanzamiento final basada en la disponibilidad de las fechas
                if date_release_date:
                    # Asigna la fecha de lanzamiento si está disponible
                    final_release_date = date_release_date
                elif date_updated_date:
                    # Si no hay fecha de lanzamiento, asigna la fecha de actualización
                    final_release_date = date_updated_date
                else:
                    final_release_date = None  # Si ninguna fecha está disponible, asigna None

                # Obtener el año de 'final_release_date' o asignar 0 si no existe
                if final_release_date:
                    parsed_date = parse_date(final_release_date)
                    final_year = parsed_date.year if parsed_date else 0
                else:
                    final_year = 0

                # print("-" * 150)
                datos_scraping = {
                    'F95_ID': f95_id,
                    'URL': url,
                    'full_title': full_title,
                    'title': final_title,
                    'developer': dev,
                    'developer_info': developer_info,
                    'version': final_version,
                    'version_text': version_final,
                    'Engine': categories,
                    'gameState': statu,
                    'genres': genres,
                    'coverimg': cover,
                    'release_date': final_release_date,
                    'release_year': final_year,
                    'platforms': platforms,
                    'censored': final_censored,
                    'language': languages,
                    'synopsis': synopsis,
                    'background': background,
                    'images': images,
                }
                # print(datos_scraping)
                await save_game_data(datos_scraping)
            else:
                # print(f"Página con ID {f95_id} no válida o no cumple las condiciones, saltando...")
                print(f"#")
        else:
            # print(f"No se pudo obtener el contenido HTML para la página con ID {f95_id}")
            print(f"#")

async def login_and_scrape(username, password, inicio, final):
    async with async_playwright() as p:
        # Cambia a True si quieres que no se abra el navegador
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navegar a la página de inicio de sesión
        await page.goto('https://f95zone.to/login')

        # Intentar iniciar sesión hasta 3 veces
        for attempt in range(3):
            # Completar el formulario de inicio de sesión
            await page.fill('input[name="login"]', username)
            await page.fill('input[name="password"]', password)
            await page.click('button.button--primary')

            # Esperar a que se complete la navegación después de iniciar sesión
            # Espera hasta 60 segundos
            await page.wait_for_load_state('load', timeout=60000)

            # Obtener la página después de iniciar sesión
            html = await page.content()

            # Verificar si el inicio de sesión fue exitoso
            soup = BeautifulSoup(html, 'html.parser')
            login_link = soup.find('a', href='/login/')
            if login_link:
                print(f"El intento {attempt + 1} de inicio de sesión falló.")
                # Regresar a la página de inicio de sesión para reintentar
                await page.goto('https://f95zone.to/login')
            else:
                print("Inicio de sesión exitoso.")

                # Llamar a la función para obtener datos en el rango de páginas
                await scrape_data_range(page, inicio, final)
                break  # Salir del bucle si el inicio de sesión fue exitoso

        else:
            print("Se han agotado los intentos de inicio de sesión.")

        await browser.close()  # Cerrar el navegador al final


def iniciar_scraper(inicio, fin):
    username = F95_USER
    password = F95_PASS
    asyncio.run(login_and_scrape(username, password, inicio, fin))

