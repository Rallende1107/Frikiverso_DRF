# Django imports
from django.contrib import messages
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView)
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Local app imports - Constantes y mixins personalizados
from core.utils.constants import (Templates, URLS, CSSBackground, JSConstants, KeyMap)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    User Login
class CustomLoginView(LoginView):
    template_name = Templates.Users.LOGIN
    title = _('Iniciar Sesión')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] =self.title
        context['register_url'] = reverse(URLS.Users.CREATE)
        context['recover_url'] = reverse(URLS.PasswordRecover.FORGET_PASSWORD)
        return context

    def form_valid(self, form):
        # Añadir mensaje de éxito al iniciar sesión
        messages.success(self.request, _('Has iniciado sesión correctamente.'))
        return super().form_valid(form)

    def form_invalid(self, form):
        # Añadir mensaje de éxito al iniciar sesión
        messages.error(self.request, _('Credenciales inválidas. Por favor, inténtalo de nuevo.'))
        return self.render_to_response(self.get_context_data(form=form))

############################################################################################################################################    User Logout
class CustomLogoutView(PermissionRequiredMessageMixin, LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            response = super().dispatch(request, *args, **kwargs)
            messages.info(request, _('Has cerrado sesión correctamente.'))
            return response
        else:
            # Manejar otro tipo de solicitud aquí si es necesario
            return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.is_authenticated

############################################################################################################################################    User Change Password
class ChangePasswordView(PermissionRequiredMessageMixin, PasswordChangeView):
    template_name = Templates.Users.CHANGE_PASS
    title = _('Cambiar Contraseña')
    success_url = reverse_lazy(URLS.Main.INDEX)
    permission_redirect_url = reverse_lazy(URLS.Users.LOGIN)

    def form_valid(self, form):
        messages.success(self.request, _('Contraseña Actualizada'))
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_cancel_url(self):
        user = self.request.user
        return reverse_lazy(URLS.Users.DETAIL, kwargs={'pk': user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Users.USER
        context['cancel_url'] = self.get_cancel_url()
        return context
