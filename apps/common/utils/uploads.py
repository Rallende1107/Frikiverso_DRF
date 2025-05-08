import os
from django.utils.text import slugify

# BASE_MEDIA = os.path.join('media', 'common', 'person')
BASE_MEDIA = os.path.join('app_common', 'person')

def get_person_slug(person):
    """Devuelve el slug de la movie, o convierte el full_name slug."""
    return person.slug or slugify(person.full_name)

# Imagen principal de persona
def person_image_path(instance, filename):
    """
    Ruta para imágenes principales.
    Formato: app_common/person/{slug}/image/{size_image}/{slug}-{n}.{ext}
    """
    from apps.common.models import PersonImage

    # Obtener la persona y el slug
    person = instance.person
    person_slug = get_person_slug(person)

    # Obtener la extensión del archivo
    ext = os.path.splitext(filename)[1].lower()

    # Obtener el nombre del tamaño de imagen
    size_name = instance.size_image.slug.strip().lower()

    # Contador para la cantidad de imágenes ya asociadas a la persona
    count = PersonImage.objects.filter(person=person, size_image=instance.size_image).count() + 1

    # Crear el nuevo nombre de archivo con el contador
    new_filename = f"{person_slug}-{count}{ext}"

    # Incluir el tamaño de la imagen en la ruta (subcarpeta según 'size_image')
    return os.path.join(BASE_MEDIA, person_slug, 'image', size_name, new_filename)

# Imagen adicional de persona
def person_image_extra_path(instance, filename):
    """
    Ruta para imágenes extra.
    Formato: app_common/person/{slug}/image_extra/{slug}-{n}.{ext}
    """
    from apps.common.models import PersonImageExtra

    person = instance.person
    person_slug = get_person_slug(person)
    ext = os.path.splitext(filename)[1].lower()

    count = PersonImageExtra.objects.filter(person=person).count() + 1
    new_filename = f"{person_slug}-{count}{ext}"

    return os.path.join(BASE_MEDIA, person_slug, 'image_extra', new_filename)