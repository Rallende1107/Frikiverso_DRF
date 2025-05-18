# Vistas de Django para restablecimiento de contraseña
from django.contrib.auth.views import (PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetView,)

# Sistema de mensajes de Django
from django.contrib import messages

# Utilidades para autenticación y tokens
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

# Utilidades para codificación, URL y traducción
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _

# Decoradores y vistas
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

# Utilidades de correo
from django.core.mail import BadHeaderError, send_mail

# Utilidades de templates, vistas y redirección
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

# Constantes del proyecto
from core.utils.constants import (Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap,)

# Función personalizada para notificar cambio de contraseña
from core.utils.send_emails import notify_password_changed

# Formularios de la app de usuarios
from apps.users.forms import PasswordRecoveryForm

# Create your views here.
############################################################################################################################################    PasswordResetView
class CustomPasswordResetView(PasswordResetView):
    template_name = Templates.PasswordRecover.FORGET_PASSWORD
    success_url = reverse_lazy(URLS.PasswordRecover.FORGET_PASSWORD_DONE)
    cancel_url = reverse_lazy(URLS.Users.LOGIN)
    form_class = PasswordRecoveryForm
    title = _('Recuperar Contraseña')
    email_template_name = Templates.emailBoddy.PASSWORD_RECOVERY
    subject_template_name = Templates.emailSubject.PASSWORD_RECOVERY

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        print('Formulario Valido')
        email = form.cleaned_data['email']
        user = get_user_model().objects.get(email=email)

        # Creamos el token y el UID
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = self.get_reset_url(uidb64, token)

        # Renderizamos el contenido del correo
        context = {
            'user': user,
            'username': user.get_username(),
            'reset_link': reset_link,
        }

        email_content = render_to_string(self.email_template_name, context)
        subject = render_to_string(self.subject_template_name, context).strip()

        try:
            send_mail(subject, email_content, None, [email])
        except BadHeaderError:
            messages.error(self.request, _('Hubo un error al enviar el correo. Por favor, intenta nuevamente.'))
            return self.form_invalid(form)

        return redirect(self.success_url)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_reset_url(self, uidb64, token):
        return self.request.build_absolute_uri(
            reverse(URLS.PasswordRecover.PASSWORD_RESET_CONFIRM, kwargs={'uidb64': uidb64, 'token': token})
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

############################################################################################################################################    PasswordResetDoneView
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = Templates.PasswordRecover.RESET_DONE
    cancel_url = reverse_lazy(URLS.Users.LOGIN)
    title = _('Correo Enviado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

############################################################################################################################################    PasswordResetConfirmView
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = Templates.PasswordRecover.RESET_CONFIRM
    success_url = reverse_lazy(URLS.PasswordRecover.PASSWORD_RESET_COMPLETE)
    title = _('Reestablecer Contraseña')

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def form_valid(self, form):
        print('form_valid')
        response = super().form_valid(form)

        user = self.user

        try:
            notify_password_changed(user)
            messages.success(self.request, _('Tu contraseña ha sido actualizada y te hemos enviado un correo de confirmación.'))
        except BadHeaderError:
            messages.warning(self.request, _('La contraseña se actualizó, pero hubo un error al enviar el correo de confirmación.'))

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        return context

############################################################################################################################################    PasswordResetCompleteView
class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = Templates.PasswordRecover.RESET_COMPLETE
    title = _('Contraseña Restablecida')
    cancel_url = reverse_lazy(URLS.Users.LOGIN)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context