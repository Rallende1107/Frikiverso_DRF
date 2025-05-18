# Django imports
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

# Local app imports - Modelos y formularios
from apps.users.forms import UserUpdateForm
from apps.users.models import CustomUser

# Local app imports - Utilidades y mixins personalizados
from core.utils.constants import (Templates, URLS, CSSBackground, JSConstants, KeyMap)
from core.utils.mixins import PermissionRequiredMessageMixin
from core.utils.utils import delete_previous_media

# Create your views here.
############################################################################################################################################    User Update
class UserUpdateView(PermissionRequiredMessageMixin, UpdateView):
    model = CustomUser
    template_name = Templates.Users.UPT
    form_class = UserUpdateForm
    title = _('Editar Perfil')
    permission_redirect_url = reverse_lazy(URLS.Main.INDEX)

    def test_func(self):
        user = self.request.user
        perfil_usuario = self.get_object()
        return user.is_authenticated and (user.is_superuser or user.is_staff or user == perfil_usuario)

    def get_success_url(self):
        # Obtener el pk del usuario actualizado
        pk = self.object.pk
        return reverse_lazy(URLS.Users.DTL, kwargs={'pk': pk})

    def get_username(self):
        return self.object.username

    def form_valid(self, form):
        # Obtener el objeto actual
        objeto = self.get_object()
        media_url = objeto.get_img_url() if objeto else None

        # Actualizar el objeto
        self.object = form.save()

        # Si hay una nueva foto, elimina la anterior
        if 'avatar' in self.request.FILES and media_url:
            try:
                delete_previous_media(media_url)
            except Exception as e:
                messages.error(self.request, _('Error al eliminar la imagen anterior: %(error)s') % {'error': e})

        # Mensaje de éxito
        messages.success(self.request, _('¡Información actualizada exitosamente!'))

        # Redirigir a la vista detallada del usuario
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()
        success_url= self.get_success_url()
        context['username'] = self.get_username()
        context['img_url'] = img_url
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        return context