from django.template.loader import render_to_string
from django.core.mail import send_mail
from core.utils.constants import Templates
from django.conf import settings




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
        subject_template=Templates.EmailSubject.RESET_PASSWORD,
        body_template=Templates.EmailBoddy.RESET_PASSWORD
    )

def notify_blocked_user(user):
    context = {'user': user}
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template=Templates.EmailSubject.USER_BLOCKED,
        body_template=Templates.EmailBoddy.USER_BLOCKED
    )


def notify_activated_user(user):
    context = {'user': user}
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template=Templates.EmailSubject.USER_ACTIVATED,
        body_template=Templates.EmailBoddy.USER_ACTIVATED
    )


def notify_deleted_user(user):
    context = {'user': user}
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template=Templates.EmailSubject.DELETED_USER,
        body_template=Templates.EmailBoddy.DELETED_USER,
    )


def notify_password_changed(user):
    print('notify_password_changed')
    context = {
        'user': user,
        'username': user.get_username(),
    }
    enviar_correo_personalizado(
        user=user,
        context=context,
        subject_template=Templates.EmailSubject.PASSWORD_CHANGED,
        body_template=Templates.EmailBoddy.PASSWORD_CHANGED,
    )


def send_contact_email(nombre, fono, correo, asunto, mensaje):
    context = {
        'nombre': nombre,
        'fono': fono,
        'correo': correo,
        'asunto': asunto,
        'mensaje': mensaje,
    }

    subject = render_to_string(Templates.EmailSubject.CONTACT, context).strip()
    body = render_to_string(Templates.EmailBoddy.CONTACT, context)


    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_EMAIL],
        fail_silently=False,
        # headers={'Reply-To': correo},
    )
