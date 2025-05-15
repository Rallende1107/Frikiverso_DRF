from django.contrib.auth.mixins import AccessMixin
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

class PermissionRequiredMessageMixin(AccessMixin):
    login_message = _('Debes estar logueado para acceder a esta página.')
    permission_message = _('No tienes permisos suficientes para realizar esta acción.')
    permission_redirect_url = None  # Puedes definirlo en cada vista si quieres

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.login_message)
            return redirect(f"{settings.LOGIN_URL}?next={request.get_full_path()}")

        if hasattr(self, 'test_func') and not self.test_func():
            messages.error(request, self.permission_message)
            redirect_url = self.permission_redirect_url or settings.LOGIN_REDIRECT_URL
            return redirect(redirect_url)

        return super().dispatch(request, *args, **kwargs)
