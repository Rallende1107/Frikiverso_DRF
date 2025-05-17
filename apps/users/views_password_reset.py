from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model

import logging

logger = logging.getLogger(__name__)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset/password_reset_form.html'
    email_template_name = 'emails/password_recovery_body.txt'
    subject_template_name = 'emails/password_recovery_subject.txt'
    success_url = reverse_lazy('users_app:password_reset_done')
    correo_no_existe = 'users/password_reset/password_reset_email_not_found.html'

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Por seguridad, simplemente redirigimos al mismo "éxito" aunque el email no esté
            # return redirect(self.success_url)
            # O si realmente quieres mostrar un mensaje de error:
            return render(self.request, self.correo_no_existe)

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
            return render(self.request, 'users/password_reset/password_reset_error.html')

        return redirect(self.success_url)

    def get_reset_url(self, uidb64, token):
        return self.request.build_absolute_uri(
            reverse('users_app:password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        )



class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset/password_reset_done.html'

    def dispatch(self, request, *args, **kwargs):
        logger.info("Usuario accedió a password_reset_done: %s", request.user)
        return super().dispatch(request, *args, **kwargs)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('users_app:password_reset_complete')

    def form_valid(self, form):
        logger.info("Contraseña cambiada para UID: %s", self.kwargs.get("uidb64"))
        return super().form_valid(form)


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset/password_reset_complete.html'

    def dispatch(self, request, *args, **kwargs):
        logger.info("Password reset completado para %s", request.user)
        return super().dispatch(request, *args, **kwargs)

def enviar_correo_personalizado(user, context, subject_template, body_template):
    subject = render_to_string(subject_template, context).strip()
    body = render_to_string(body_template, context)

    send_mail(
        subject=subject,
        message=body,
        from_email=None,  # Usa DEFAULT_FROM_EMAIL
        recipient_list=[user.email],
        fail_silently=False,
    )


def notify_password_reset(user, nueva_contrasena):
    context = {
        'user': user,
        'nueva_contrasena': nueva_contrasena,
    }
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template='emails/reset_password_subject.txt',
        body_template='emails/reset_password_body.txt',
    )

def notify_blocked_user(user):
    context = {'user': user}
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template='emails/user_blocked_subject.txt',
        body_template='emails/user_blocked_body.txt',
    )


def notify_activated_user(user):
    context = {'user': user}
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template='emails/user_activated_subject.txt',
        body_template='emails/user_activated_body.txt',
    )


def notify_deleted_user(user):
    context = {'user': user}
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template='emails/deleted_user_subject.txt',
        body_template='emails/deleted_user_body.txt',
    )
