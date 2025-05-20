
from .models import Game_F95_ID, Game
from apps.core.models import Log
from django.db.models import Max

from bs4 import BeautifulSoup
import requests
import re
from dateutil import parser
from datetime import datetime


def agregar_entrada_log(level, message, process):
    """
    Agrega una entrada de registro (log) en la base de datos.

    Args:
        level (str): El nivel del registro ('ERROR' 'INFO', 'WARR').
        message (str): El mensaje a registrar.
        process (str): El proceso o contexto en el que se generó el registro.

    Returns:
        None
    """
    try:
        application = 'RenpyAPP'
        timestamp = timezone.now()
        Log.objects.create(
            timestamp=timestamp,
            level=level,
            process=process,
            message=message,
            application=application
        )
        # print(message)
    except Exception as e:
        print(f"Error al crear entrada de registro ->: {e}")


def obtener_ultimo_id():
    """
    Obtiene el último F95 ID.

    Args:

    Returns:
        int: Último mal_id.
    """
    # crear_carpeta_multimedia()

    max_mal_id = Game.objects.aggregate(Max('f95_id'))['f95_id__max']
    # print(max_mal_id)
    max_id_not_exist = Game_F95_ID.objects.aggregate(Max('f95_id'))['f95_id__max']
    # print(max_id_not_exist)

    max_mal_id = max_mal_id or 0
    max_id_not_exist = max_id_not_exist or 0

    if max_mal_id > max_id_not_exist:
        return max_mal_id

    else:
        return max_id_not_exist or 1

def clean_string(input_string):
    # Eliminar caracteres no deseados y limpiar espacios en blanco
    # Reemplaza múltiples espacios en blanco con uno solo
    cleaned = re.sub(r'\s+', ' ', input_string)
    cleaned = cleaned.replace('\u200b', '')  # Eliminar el carácter invisible
    return cleaned.strip()  # Elimina espacios al inicio y al final

def parse_date(date_str):
    try:
        # Convierte la cadena a un objeto de tipo 'date' usando el formato adecuado (por ejemplo, YYYY-MM-DD)
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        # Si ocurre un error durante la conversión, devuelve None
        return None


def validate_page(soup, game_id):
    # Verificar si el título es "Oops! We ran into some problems."
    full_title_element = soup.find('h1', class_='p-title-value')
    if full_title_element and full_title_element.get_text(strip=True) == "Oops! We ran into some problems.":
        print(f"Juego con ID {game_id} no válido, saltando...")
        return False  # Indica que no se procesará este ID

    # Verificar si existe el selector .bbWrapper en la página
    bb_wrapper = soup.find('div', class_='bbWrapper')
    if not bb_wrapper:
        print(f"Página con ID {game_id} no contiene el selector .bbWrapper, saltando...")
        return False  # Indica que no se procesará este ID

    # Verificar si existe el selector .p-description en la página
    p_description = soup.find('div', class_='p-description')
    if p_description:
        # Verificar si hay al menos 3 <li> o un <li> con .tagList dentro de .p-description
        li_elements = p_description.find_all('li')
        has_tag_list = any(li.find(class_='tagList') for li in li_elements)

        if len(li_elements) < 3 and not has_tag_list:
            print(f"Página con ID {game_id} no tiene suficientes <li> en .p-description, saltando...")
            return False  # Indica que no se procesará este ID
    else:
        print(f"Página con ID {game_id} no contiene el selector .p-description, saltando...")
        return False  # Indica que no se procesará este ID

    # Si todas las verificaciones pasan, se puede proceder
    return True

def get_title_categories(soup):
    title_element = soup.find('h1', class_='p-title-value')
    titulo_completo = ""
    categories = []
    status = "In Development"
    if title_element:
        titulo_completo = title_element.get_text(separator=' ', strip=True)
        categories = [span.text.strip() for span in title_element.find_all('span') if span.text.strip()]

    lastCategory = categories[-1]

    if (lastCategory == 'Completed' or lastCategory == 'Abandoned' or lastCategory == 'Onhold'):
        categories.pop()
        status = lastCategory

    return titulo_completo, categories, status

def clear_title(titulo_completo, categories):
    for category in categories:
        titulo_completo = titulo_completo.replace(category, '').strip()
    return titulo_completo

def get_title_data(titulo_completo):
    match = re.match(r'^(.*?)\s*\[(.*?)\]\s*\[(.*?)\]$', titulo_completo)
    if match:
        return match.group(1).strip(), match.group(2).strip(), match.group(3).strip()
    return "", "", ""

def get_tags(soup):
    tag_list = soup.find(class_='js-tagList')
    tags = []
    if tag_list:
        tags = [tag.text.strip() for tag in tag_list.find_all('a')]
    return tags


def get_overviews(soup):
    # Esta función se encarga de extraer el overview y los extras si es necesario
    overview = ""
    extra = ""  # Inicializamos una variable para el extra
    overview_div = soup.find('div', style='text-align: center')

    if overview_div:
        # Extraemos el texto del div y limpiamos
        full_overview = overview_div.get_text(separator=' ', strip=True)
        full_overview = full_overview.replace('Overview: ', '')  # Limpiar "Overview: "

        # Hacemos el split en la palabra "Spoiler"
        partes = full_overview.split('Spoiler')
        partes = [parte.strip() for parte in partes]  # Limpiamos espacios en blanco

        # La primera parte es el overview
        if partes:
            overview = partes[0]  # Tomamos la primera parte como el overview

        # Unimos las partes restantes como un solo extra
        extra = 'Spoiler'.join(partes[1:]) if len(partes) > 1 else ''

    return full_overview.strip(), overview.strip(), extra.strip(),

def get_first_image(soup):
    # Encontrar la imagen dentro del div con clase "bbWrapper" y centrado
    bb_wrapper = soup.find('div', class_='bbWrapper')
    if bb_wrapper:
        # Buscar el elemento <img> dentro del div
        img_tag = bb_wrapper.find('img')
        if img_tag and 'src' in img_tag.attrs:
            return img_tag['src']
    return None

def get_thread_updated(soup):
    for b_tag in soup.find_all('b'):
        if "Thread Updated" in b_tag.get_text(strip=True):
            return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
        if "Updated" in b_tag.get_text(strip=True):
            return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
    return ""

def get_release_date(soup):
    for b_tag in soup.find_all('b'):
        if "Release Date" in b_tag.get_text(strip=True):
            return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
    return ""

def standardize_date(fecha_str):
    try:
        # Intenta parsear la fecha en diferentes formatos
        fecha = parser.parse(fecha_str, dayfirst=True)
        # Devuelve la fecha en formato estandarizado (YYYY-MM-DD)
        return fecha.strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        # Si no se puede parsear, retorna una cadena vacía
        return ""

def get_developer(soup):
    for b_tag in soup.find_all('b'):
        if "Developer" in b_tag.get_text(strip=True):
            developer_name = b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
            # Validar que el nombre no termine con un guion
            if developer_name.endswith('-'):
                return ""  # O cualquier otra acción que desees, como lanzar una excepción
            return developer_name
    return ""


def get_version(soup):
    for b_tag in soup.find_all('b'):
        if "Version" in b_tag.get_text(strip=True):
            return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
    return ""

def get_language(soup):
    for b_tag in soup.find_all('b'):
        if "Language" in b_tag.get_text(strip=True):
            # Limpiar y dividir la cadena antes de crear la lista
            return [lang.strip() for lang in b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').split(',') if lang.strip()]
    return []

def get_censored(soup):
    for b_tag in soup.find_all('b'):
        if "Censored" in b_tag.get_text(strip=True):
            censored_text = b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
            return "No" if censored_text == "None" else censored_text
        elif "Censorship" in b_tag.get_text(strip=True):
            censored_text = b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
            return "No" if censored_text == "None" else censored_text
    return ""  # O "No", dependiendo de tu preferencia

def get_platforms(soup):
    for b_tag in soup.find_all('b'):
        if "OS" in b_tag.get_text(strip=True):
            return [sistema.strip() for sistema in b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').split(',') if sistema.strip()]
        elif "Platform" in b_tag.get_text(strip=True):
            return [sistema.strip() for sistema in b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').split(',') if sistema.strip()]

    return []

def get_voices(soup):
    for b_tag in soup.find_all('b'):
        if "voices" in b_tag.get_text(strip=True):
            return [sistema.strip() for sistema in b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').split(',') if sistema.strip()]

    return []


def get_publishers(soup):
    for b_tag in soup.find_all('b'):
        # Verificar si el texto contiene "Original Title" o "Original Name"
        if any(keyword in b_tag.get_text(strip=True) for keyword in ["Publisher", "Publishers"]):
            # Verifica que 'next_sibling' no sea None antes de llamar a strip()
            if b_tag.next_sibling:
                return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
    return ""  # Retorna una cadena vacía si no se encuentra el texto


def get_developer_info(soup):
    # Crear un diccionario para almacenar la información del desarrollador
    developer_info = {
        'dev_links': []
    }

    # Extraer la sección que contiene los enlaces del desarrollador
    dev_section = soup.find('b', string="Developer")

    if dev_section:
        # Obtener el contenido después de la etiqueta <b>
        developer_content = dev_section.find_next_sibling(text=True)
        if developer_content:
            developer_content = developer_content.strip()  # Asegurarse de que no sea None

            developer_links = []

            # Recorrer todos los hermanos hasta encontrar el <br>
            for sibling in dev_section.find_next_siblings():
                if sibling.name == 'br':
                    break  # Salir cuando encontramos <br>
                if sibling.name == 'a':
                    # Si encontramos un enlace, almacenamos su texto y href
                    developer_links.append({
                        'name': sibling.get_text(strip=True),
                        'link': sibling['href']
                    })

            # También obtener el texto del desarrollador principal antes de los enlaces
            main_developer = developer_content.replace(':', '').strip()
            if main_developer:
                developer_info['main_developer'] = main_developer

            developer_info['dev_links'] = developer_links

    return developer_info


def get_original_title(soup):
    for b_tag in soup.find_all('b'):
        # Verificar si el texto contiene "Original Title" o "Original Name"
        if any(keyword in b_tag.get_text(strip=True) for keyword in ["Original Title", "Original Name"]):
            # Verifica que 'next_sibling' no sea None antes de llamar a strip()
            if b_tag.next_sibling:
                return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
    return ""  # Retorna una cadena vacía si no se encuentra el texto

def get_alias_title(soup):
    for b_tag in soup.find_all('b'):
        # Verificar si el texto contiene "Original Title" o "Original Name"
        if any(keyword in b_tag.get_text(strip=True) for keyword in ["Alias Title",]):
            # Verifica que 'next_sibling' no sea None antes de llamar a strip()
            if b_tag.next_sibling:
                return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
    return ""  # Retorna una cadena vacía si no se encuentra el texto

def get_translation(soup):
    for b_tag in soup.find_all('b'):
        # Verificar si el texto contiene "Translation" o "Translator"
        if any(keyword in b_tag.get_text(strip=True) for keyword in ["Translation", "Translator"]):
            # Verifica que 'next_sibling' no sea None antes de llamar a strip()
            if b_tag.next_sibling:
                return b_tag.next_sibling.strip().replace('<br>', '').lstrip(':').strip()
            else:
                return ""  # Retorna una cadena vacía si no hay siguiente hermano
    return ""  # Retorna una cadena vacía si no se encuentra el texto

def get_translator_info(soup):
    """
    Extracts translator information from the provided BeautifulSoup object.

    Parameters:
    soup (BeautifulSoup): The BeautifulSoup object containing the HTML.

    Returns:
    dict: A dictionary containing the main translator and a list of translator links.
    """
    translator_info = {
        'main_translator': None,  # Inicializar para mantener consistencia
        'translator_links': []
    }

    # Buscar la sección que contiene "Translator" o "Translation"
    translator_section = soup.find('b', string="Translator") or soup.find('b', string="Translation")

    if translator_section:
        # Obtener el contenido después de la etiqueta <b>
        translator_content = translator_section.find_next_sibling(text=True).strip()

        # Almacenar el texto del traductor principal
        main_translator = translator_content.replace(':', '').strip()
        if main_translator:
            translator_info['main_translator'] = main_translator

        # Recorrer todos los hermanos hasta encontrar el <br>
        for sibling in translator_section.find_next_siblings():
            if sibling.name == 'br':
                break  # Salir cuando encontramos <br>
            if sibling.name == 'a' and 'href' in sibling.attrs:
                # Si encontramos un enlace, almacenamos su texto y href
                translator_info['translator_links'].append({
                    'name': sibling.get_text(strip=True),
                    'link': sibling['href']
                })

    return translator_info

def get_store_info(soup):
    """
    Extracts store information from the provided BeautifulSoup object.

    Parameters:
    soup (BeautifulSoup): The BeautifulSoup object containing the HTML.

    Returns:
    dict: A dictionary containing the main store name and a list of store links.
    """
    # Crear un diccionario para almacenar la información de la tienda
    store_info = {
        'main_store': None,  # Inicializar para mantener consistencia
        'store_links': []
    }

    # Extraer la sección que contiene los enlaces de la tienda
    store_section = soup.find('b', string="Store")

    if store_section:
        # Obtener el contenido después de la etiqueta <b>
        store_content = store_section.find_next_sibling(text=True).strip()

        # Almacenar el texto de la tienda principal
        main_store = store_content.replace(':', '').strip()
        if main_store:
            store_info['main_store'] = main_store

        # Recorrer todos los hermanos hasta encontrar el <br>
        for sibling in store_section.find_next_siblings():
            if sibling.name == 'br':
                break  # Salir cuando encontramos <br>
            if sibling.name == 'a':
                # Verificar si el enlace tiene el atributo 'href'
                if 'href' in sibling.attrs:
                    store_info['store_links'].append({
                        'name': sibling.get_text(strip=True),
                        'link': sibling['href']
                    })

    return store_info

def get_publisher_info(soup):
    # Crear un diccionario para almacenar la información del publicador
    publisher_info = {
        'main_publisher': None,
        'pub_links': []
    }

    # Buscar la sección que contiene los enlaces del publicador
    pub_section = soup.find('b', string="Publisher") or soup.find('b', string="Publishers")

    if pub_section:
        # Obtener el contenido después de la etiqueta <b>
        publisher_content = pub_section.find_next_sibling(text=True).strip()
        main_publisher = publisher_content.replace(':', '').strip()
        if main_publisher:
            publisher_info['main_publisher'] = main_publisher

        # Recorrer todos los hermanos hasta encontrar el <br>
        for sibling in pub_section.find_next_siblings():
            if sibling.name == 'br':
                break
            if sibling.name == 'a' and 'href' in sibling.attrs:
                publisher_info['pub_links'].append({
                    'name': sibling.get_text(strip=True),
                    'link': sibling['href']
                })

    return publisher_info

def get_VNDB_info(soup):
    # Crear un diccionario para almacenar la información de VNDB
    VNDB_info = {
        'main_VNDB': None,
        'VNDB_links': []
    }

    # Buscar la sección que contiene los enlaces de VNDB
    VNDB_section = soup.find('b', string="VNDB")

    if VNDB_section:
        # Obtener el contenido después de la etiqueta <b>
        VNDB_content = VNDB_section.find_next_sibling(text=True).strip()

        # Obtener el texto principal de VNDB antes de los enlaces
        main_VNDB = VNDB_content.replace(':', '').strip()
        if main_VNDB:
            VNDB_info['main_VNDB'] = main_VNDB

        # Recorrer todos los hermanos hasta encontrar el <br>
        for sibling in VNDB_section.find_next_siblings():
            if sibling.name == 'br':
                break  # Salir cuando encontramos <br>
            if sibling.name == 'a' and 'href' in sibling.attrs:
                # Si encontramos un enlace, almacenamos su texto y href
                VNDB_info['VNDB_links'].append({
                    'name': sibling.get_text(strip=True),
                    'link': sibling['href']
                })

    return VNDB_info

def get_genres_info(soup):
    # Inicializamos una lista para almacenar los géneros
    genres = []

    # Buscar la sección de géneros que contiene el botón "Spoiler"
    genre_section = soup.find('b', string="Genre")

    if genre_section:
        # Buscar el primer spoiler que sigue después de la sección de género
        first_spoiler = genre_section.find_next('div', class_='bbCodeSpoiler-content')

        if first_spoiler:
            # Función recursiva para extraer géneros desde spoilers anidados
            def extract_genres(spoiler):
                # Buscar el contenido de los géneros en el spoiler actual
                genre_content = spoiler.find('div', class_='bbCodeBlock-content')
                if genre_content:
                    # Extraer el texto y dividirlo en géneros separados por coma
                    genre_text = genre_content.get_text(separator=',', strip=True)
                    genres.extend([genre.strip() for genre in genre_text.split(',')])

                # Buscar cualquier spoiler anidado dentro del contenido actual
                nested_spoilers = spoiler.find_all('div', class_='bbCodeSpoiler-content', recursive=False)
                for nested in nested_spoilers:
                    extract_genres(nested)  # Llamada recursiva para cada spoiler anidado

            # Llamar a la función recursiva para extraer los géneros desde el primer spoiler
            extract_genres(first_spoiler)

    return genres

def get_images(soup):
    # Lista para almacenar las URLs de las imágenes principales
    image_urls = []

    # Encontrar el div bbWrapper
    bb_wrapper = soup.find('div', class_='bbWrapper')

    if bb_wrapper:
        # Encontrar el div con style="text-align: center;" para omitir sus imágenes
        center_div = bb_wrapper.find('div', style="text-align: center")

        # Encontrar todos los enlaces con la clase js-lbImage dentro de bbWrapper
        all_links = bb_wrapper.find_all('a', class_='js-lbImage')

        for link in all_links:
            # Si el enlace no está dentro del div center_div, agregar su href a la lista
            if center_div and center_div not in link.parents:
                href = link.get('href', '')
                if href.startswith('http'):  # Verificar que sea un enlace HTTP o HTTPS
                    image_urls.append(href)

    return image_urls



