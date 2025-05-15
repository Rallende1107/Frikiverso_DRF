from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

def obtener_ultimo_id():
    pass
def obtener_lotes():
    pass
def disponibilidad_celery():
    pass
def disponibilidad_worker():
    pass
def procesar_lotes_task():
    pass

def procesar_lotes ():
    pass

PERSONA = ''
PERSONAJE = ''
ANIME = ''
MANGA = ''

CeleryError = ''
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap

class AnimesLoadView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'otaku/anime/anime_load.html'
    title = 'Cargar Animes desde MAL'
    cancel_url = reverse_lazy(URLS.Otaku.Anime.LST)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.OTAKU_ANIME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir las variables adicionales de forma ordenada
        context['class'] = CSSBackground.Otaku.ANIME
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

    def get(self, request, *args, **kwargs):
        # Obtener los valores de inicio y fin desde los parámetros GET o definir por defecto
        ultimo_digito = obtener_ultimo_id(ANIME)
        inicio = int(request.GET.get("inicio", ultimo_digito))
        fin = int(request.GET.get("fin", ultimo_digito + 100))

        # Llamar a get_context_data() para preparar el contexto
        context = self.get_context_data(inicio=inicio, fin=fin)
        context['inicio'] = inicio
        context['fin'] = fin
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ultimo_digito = obtener_ultimo_id(ANIME)
        inicio = int(request.POST.get("inicio", ultimo_digito))
        fin = int(request.POST.get("fin", inicio + 10))

        # Validación de los parámetros
        if fin < inicio:
            context = self.get_context_data(inicio=inicio, fin=fin)
            context['error'] = 'El valor de fin debe ser mayor o igual que inicio.'
            return render(request, self.template_name, context)

        # Procesamiento de los lotes
        lotes = obtener_lotes(inicio, fin)
        if disponibilidad_celery() and disponibilidad_worker():
            try:
                procesar_lotes_task.delay(lotes, ANIME)
                messages.success(
                    request, "El proceso se ejecutara en segundo plano.")
            except CeleryError:
                print("Error al ejecutar Celery. Ejecutando la función directamente.")
                procesar_lotes(lotes, ANIME)
        else:
            print("Redis no disponible, ejecutando la función directamente.")
            procesar_lotes(lotes, ANIME)

        return redirect(URLS.Otaku.Anime.LST)




class MangaLoadView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'otaku/manga/manga_load.html'
    title = 'Cargar Mangas desde MAL'
    cancel_url = reverse_lazy(URLS.Otaku.Manga.LST)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.OTAKU_MANGA)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir las variables adicionales de forma ordenada
        context['class'] = CSSBackground.Otaku.MANGA
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

    def get(self, request, *args, **kwargs):
        # Obtener los valores de inicio y fin desde los parámetros GET o definir por defecto
        ultimo_digito = obtener_ultimo_id(MANGA)
        inicio = int(request.GET.get("inicio", ultimo_digito))
        fin = int(request.GET.get("fin", ultimo_digito + 100))

        # Llamar a get_context_data() para preparar el contexto
        context = self.get_context_data(inicio=inicio, fin=fin)
        context['inicio'] = inicio
        context['fin'] = fin
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ultimo_digito = obtener_ultimo_id(MANGA)
        inicio = int(request.POST.get("inicio", ultimo_digito))
        fin = int(request.POST.get("fin", inicio + 10))

        # Validación de los parámetros
        if fin < inicio:
            context = self.get_context_data(inicio=inicio, fin=fin)
            context['error'] = 'El valor de fin debe ser mayor o igual que inicio.'
            return render(request, self.template_name, context)

        # Procesamiento de los lotes
        lotes = obtener_lotes(inicio, fin)
        if disponibilidad_celery() and disponibilidad_worker():
            try:
                procesar_lotes_task.delay(lotes, MANGA)
                messages.success(
                    request, "El proceso se está ejecutando en segundo plano.")
            except CeleryError:
                print("Error al ejecutar Celery. Ejecutando la función directamente.")
                procesar_lotes(lotes, MANGA)
        else:
            print("Redis no disponible, ejecutando la función directamente.")
            procesar_lotes(lotes, MANGA)

        return redirect(URLS.Otaku.Manga.LST)


class CharacterLoadView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'otaku/anime/anime_load.html'
    title = 'Cargar personajes desde MAL'
    cancel_url = reverse_lazy(URLS.Otaku.Character.LST)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.OTAKU_PERSON_CHARACTER)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir las variables adicionales de forma ordenada
        context['class'] = CSSBackground.Otaku.CHARACTER
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

    def get(self, request, *args, **kwargs):
        # Obtener los valores de inicio y fin desde los parámetros GET o definir por defecto
        ultimo_digito = obtener_ultimo_id(PERSONAJE)
        inicio = int(request.GET.get("inicio", ultimo_digito))
        fin = int(request.GET.get("fin", ultimo_digito + 100))

        # Llamar a get_context_data() para preparar el contexto
        context = self.get_context_data(inicio=inicio, fin=fin)
        context['inicio'] = inicio
        context['fin'] = fin
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ultimo_digito = obtener_ultimo_id(PERSONAJE)
        inicio = int(request.POST.get("inicio", ultimo_digito))
        fin = int(request.POST.get("fin", inicio + 10))

        # Validación de los parámetros
        if fin < inicio:
            context = self.get_context_data(inicio=inicio, fin=fin)
            context['error'] = 'El valor de fin debe ser mayor o igual que inicio.'
            return render(request, self.template_name, context)

        # Procesamiento de los lotes
        lotes = obtener_lotes(inicio, fin)
        if disponibilidad_celery() and disponibilidad_worker():
            try:
                procesar_lotes_task.delay(lotes, PERSONAJE)
                messages.success(
                    request, "El proceso se está ejecutando en segundo plano.")
            except CeleryError:
                print("Error al ejecutar Celery. Ejecutando la función directamente.")
                procesar_lotes(lotes, PERSONAJE)
        else:
            print("Redis no disponible, ejecutando la función directamente.")
            procesar_lotes(lotes, PERSONAJE)

        return redirect(URLS.Otaku.Character.LST)


class PersonLoadView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'otaku/anime/anime_load.html'
    title = 'Cargar personas desde MAL'
    cancel_url = reverse_lazy(URLS.Otaku.Person.LST)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.OTAKU_PERSON_CHARACTER)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadir las variables adicionales de forma ordenada
        context['class'] = CSSBackground.Otaku.PERSON
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

    def get(self, request, *args, **kwargs):
        # Obtener los valores de inicio y fin desde los parámetros GET o definir por defecto
        ultimo_digito = obtener_ultimo_id(PERSONA)
        inicio = int(request.GET.get("inicio", ultimo_digito))
        fin = int(request.GET.get("fin", ultimo_digito + 100))

        # Llamar a get_context_data() para preparar el contexto
        context = self.get_context_data(inicio=inicio, fin=fin)
        context['inicio'] = inicio
        context['fin'] = fin
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        ultimo_digito = obtener_ultimo_id(PERSONA)
        inicio = int(request.POST.get("inicio", ultimo_digito))
        fin = int(request.POST.get("fin", inicio + 10))

        # Validación de los parámetros
        if fin < inicio:
            context = self.get_context_data(inicio=inicio, fin=fin)
            messages.error(
                self.request, 'El valor de fin debe ser mayor o igual que inicio.')
            return render(request, self.template_name, context)

        # Procesamiento de los lotes
        lotes = obtener_lotes(inicio, fin)
        if disponibilidad_celery() and disponibilidad_worker():
            try:
                procesar_lotes_task.delay(lotes, PERSONA)
                messages.success(
                    request, "El proceso se está ejecutando en segundo plano.")
            except CeleryError:
                print("Error al ejecutar Celery. Ejecutando la función directamente.")
                procesar_lotes(lotes, PERSONA)
        else:
            print("Redis no disponible, ejecutando la función directamente.")
            procesar_lotes(lotes, PERSONA)

        return redirect(URLS.Otaku.Person.LST)


