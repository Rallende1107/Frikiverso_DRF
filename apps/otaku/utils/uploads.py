
import os
from django.utils.text import slugify

def anime_image_path(instance, filename):
    mal_id = instance.anime.id if instance.anime else '0'
    size = dict(instance.SIZE_CHOISE).get(instance.size_image, 'Unknown')
    path = os.path.join('otaku', 'img', 'anime', 'cover', size, str(mal_id))
    return os.path.join(path, filename)

def manga_image_path(instance, filename):
    mal_id = instance.manga.id if instance.manga else '0'
    size = dict(instance.SIZE_CHOISE).get(instance.size_image, 'Unknown')
    path = os.path.join('otaku', 'img', 'manga', 'cover', size, str(mal_id))
    return os.path.join(path, filename)

def person_image_path(instance, filename):
    mal_id = instance.person.id if instance.person else '0'
    size = dict(instance.SIZE_CHOISE).get(instance.size_image, 'Unknown')
    path = os.path.join('otaku', 'img', 'person', 'cover', size, str(mal_id))
    return os.path.join(path, filename)

def character_image_path(instance, filename):
    mal_id = instance.character.id if instance.character else '0'
    size = dict(instance.SIZE_CHOISE).get(instance.size_image, 'Unknown')
    path = os.path.join('otaku', 'img', 'character', 'cover', size, str(mal_id))
    return os.path.join(path, filename)

def anime_image_extra_path(instance, filename):
    mal_id = instance.anime.id if instance.anime else '0'
    path = os.path.join('otaku', 'img', 'anime', 'pictures', str(mal_id))
    return os.path.join(path, filename)

def manga_image_extra_path(instance, filename):
    mal_id = instance.manga.id if instance.manga else '0'
    path = os.path.join('otaku', 'img', 'manga', 'pictures', str(mal_id))
    return os.path.join(path, filename)

def person_image_extra_path(instance, filename):
    mal_id = instance.person.id if instance.person else '0'
    path = os.path.join('otaku', 'img', 'person', 'pictures', str(mal_id))
    return os.path.join(path, filename)

def character_image_extra_path(instance, filename):
    mal_id = instance.character.id if instance.character else '0'
    path = os.path.join('otaku', 'img', 'character', 'pictures', str(mal_id))
    return os.path.join(path, filename)