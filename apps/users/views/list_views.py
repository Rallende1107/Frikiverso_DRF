# Django imports
from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, ListView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
# Local app imports
from apps.users.models import CustomUser
# from .forms import UserForm, StaffUserForm, SuperUserForm, UserUpdateForm
# Local app imports
from core.utils.utils import delete_previous_media
from core.utils.texts import WITHOUT_PERMISSION
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, KeyMap

############################################################################################################################################    User Create
class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = Templates.Users.LST
    context_object_name = 'usuarios'
    title = 'Lista de Usuarios'

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.is_staff)

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = self.get_queryset()

        # Añadir la combinación "Edad (Fecha de Nacimiento)" para cada usuario
        for user in context['usuarios']:

            # Concatenar nombres si están disponibles
            if user.first_name and user.last_name:
                user.full_name = f"{user.first_name} {user.last_name}"
            else:
                user.full_name = user.first_name or user.last_name or "Sin Información"

            if user.birth_date:
                # Usar el método `get_edad` para obtener la edad
                age = user.get_edad()
                # Asignar el formato "Edad (Fecha de Nacimiento)"
                user.display_age_birthdate = f"{age} años ({user.birth_date})"
            else:
                user.display_age_birthdate = "Sin Información"

        context['title'] = self.title
        context['class'] = CSSBackground.Users.USER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.users.USER
        context['key_map'] = KeyMap.Users.USER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Users.ADD),
                'label': 'Añadir',
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Users.ADD_SUPER),
                'label': 'Añadir Super Usuario',
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Users.ADD_STAFF),
                'label': 'Añadir Usuario al Equipo',
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context