from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from apps.common.models import Language, Website, Format, Quality
from .serializers import FormatListSerializer, FormatSerializer
from .serializers import LanguageSerializer, LanguageListSerializer
from django.utils.translation import gettext_lazy as _

class TestView(APIView):

    def get(self, request, *args, **kwargs):
        return Response('Hey Friki!!')


class LanguageCreateView(CreateAPIView):
    """Vista para crear un nuevo idioma."""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def create(self, request, *args, **kwargs):
        # Deserializar los datos
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Guardar el objeto en la base de datos
        self.perform_create(serializer)

        # Preparar la respuesta con los datos del objeto creado
        response_data = {
            'message': _('¡Idioma creado exitosamente!'),
            'data': serializer.data,
            'codigo': status.HTTP_201_CREATED
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class FormatListView(ListAPIView):
    queryset = Format.objects.all()
    serializer_class = FormatListSerializer

class FormatDetailView(RetrieveAPIView):
    queryset = Format.objects.all()
    serializer_class = FormatSerializer
    lookup_field = 'slug'













class LanguageListView(ListAPIView):
    """Vista para obtener un listado de todos los idiomas."""
    queryset = Language.objects.all()
    serializer_class = LanguageListSerializer

    def list(self, request, *args, **kwargs):
        # Llamamos al método list() de la vista base
        response = super().list(request, *args, **kwargs)

        # Personalizamos la respuesta
        response.data = {
            'message': 'Listado de idiomas obtenido exitosamente.',
            'codigo': status.HTTP_200_OK,
            'data': response.data,
        }

        # Regresamos la respuesta con el código HTTP 200 (OK)
        return Response(response.data, status=status.HTTP_200_OK)


class LanguageDetailView(RetrieveAPIView):
    """Vista para obtener los detalles de un idioma específico."""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'  # Usamos slug para la búsqueda

    def retrieve(self, request, *args, **kwargs):
        # Llamamos al método retrieve() de la vista base
        response = super().retrieve(request, *args, **kwargs)

        # Personalizamos la respuesta
        response.data = {
            'message': 'Idioma encontrado exitosamente.',
            'data': response.data
        }

        # Regresamos la respuesta con el código HTTP 200 (OK)
        return Response(response.data, status=status.HTTP_200_OK)


class LanguageUpdateView(UpdateAPIView):
    """Vista para actualizar un idioma existente."""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'  # Usamos slug para la búsqueda

    def update(self, request, *args, **kwargs):
        # Llamamos al método update() de la vista base
        response = super().update(request, *args, **kwargs)

        # Personalizamos la respuesta
        response.data = {
            'message': 'Idioma actualizado exitosamente.',
            'data': response.data
        }

        # Regresamos la respuesta con el código HTTP 200 (OK)
        return Response(response.data, status=status.HTTP_200_OK)



class LanguageDeleteView(DestroyAPIView):
    """Vista para eliminar un idioma existente."""
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'  # Usamos slug para la búsqueda

    def destroy(self, request, *args, **kwargs):
        # Llamamos al método destroy() de la vista base
        response = super().destroy(request, *args, **kwargs)

        # Personalizamos la respuesta
        response.data = {
            'message': 'Idioma eliminado exitosamente.'
        }

        # Regresamos la respuesta con el código HTTP 204 (No Content)
        return Response(response.data, status=status.HTTP_204_NO_CONTENT)
