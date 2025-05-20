# Django imports
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

# Local app imports - Modelos
from apps.users.models import CustomUser

# Local app imports - Utilidades y mixins personalizados
from core.utils.constants import (Templates, URLS, CSSBackground, JSConstants, KeyMap)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    User List
class UserListView(PermissionRequiredMessageMixin, ListView):
    model = CustomUser
    template_name = Templates.Users.LIST
    context_object_name = 'usuarios'
    title = _('Lista de Usuarios')
    permission_redirect_url = reverse_lazy(URLS.Home.COMMON)

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.is_staff)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = self.get_queryset()

        # Añadir la combinación "Edad (Fecha de Nacimiento)" para cada usuario
        for user in context['usuarios']:

            # Concatenar nombres si están disponibles
            if user.first_name and user.last_name:
                user.full_name = f"{user.first_name} {user.last_name}"
            else:
                user.full_name = user.first_name or user.last_name or _('Sin Información')

            if user.birth_date:
                # Usar el método `get_edad` para obtener la edad
                age = user.get_edad()
                # Asignar el formato "Edad (Fecha de Nacimiento)"
                user.display_age_birthdate = f"{age} años ({user.birth_date})"
            else:
                user.display_age_birthdate = _('Sin Información')

        context['title'] = self.title
        context['class'] = CSSBackground.Users.USER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.users.USER
        context['key_map'] = KeyMap.Users.USER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': _('Inicio'),
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Users.CREATE),
                'label': _('Añadir'),
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Users.CREATE_SUPER),
                'label': _('Añadir Super Usuario'),
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Users.CREATE_STAFF),
                'label': _('Añadir Usuario al Equipo'),
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context