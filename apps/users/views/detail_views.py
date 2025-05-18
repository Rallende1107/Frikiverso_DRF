# Django imports
from django.views.generic import (DetailView)
from django.urls import reverse_lazy
# Local app imports
from apps.users.models import CustomUser
# from .forms import UserForm, StaffUserForm, SuperUserForm, UserUpdateForm
# Local app imports
from core.utils.utils import delete_previous_media
from core.utils.texts import WITHOUT_PERMISSION
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, KeyMap
from core.utils.mixins import PermissionRequiredMessageMixin

############################################################################################################################################    User Create

class UserDetailView(PermissionRequiredMessageMixin, DetailView):
    model = CustomUser
    template_name = Templates.Users.DTL
    context_object_name = 'usuario'
    cancel_url = reverse_lazy(URLS.Users.LST)

    def test_func(self):
        user = self.request.user
        perfil_usuario = self.get_object()
        return user.is_authenticated and (user.is_superuser or user.is_staff or user == perfil_usuario)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()
        edad = objeto.get_edad()

        context['edad'] = edad
        context['img_url'] = img_url
        context['class'] = CSSBackground.Users.USER
        context['title'] = f'perfil de {objeto.username}'
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)

        if self.request.user.is_superuser:
            context['listURL'] = reverse_lazy(URLS.Users.LST)
            context['cancel_url'] =self.cancel_url

        return context