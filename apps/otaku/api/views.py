from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


from django.utils.translation import gettext_lazy as _

class TestView(APIView):

    def get(self, request, *args, **kwargs):
        return Response('Test Otaku App!!')

