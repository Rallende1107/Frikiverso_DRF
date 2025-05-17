from django.views.generic import (TemplateView)
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactoForm  # Asegúrate de tener este form
from django.core.mail import send_mail
from django.conf import settings


TEMPLATE_MAIN_INDEX = 'pages/index.html'
TEMPLATE_MAIN_CONTACT = 'pages/contact.html'
TEMPLATE_MAIN_ABOUT = 'pages/about.html'

############################################################################################################################################    IndexView
class IndexView(TemplateView):
    template_name = TEMPLATE_MAIN_INDEX
    title = 'Inicio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

############################################################################################################################################    ContactView
class ContactView(FormView):
    template_name = TEMPLATE_MAIN_CONTACT
    form_class = ContactoForm
    success_url = reverse_lazy('pages_app:contact')  # Cambia esto según tu config
    title = 'Contáctanos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def form_valid(self, form):
        try:
            nombre = form.cleaned_data['nombre']
            fono = form.cleaned_data['fono']
            correo = form.cleaned_data['correo']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Puedes usar una plantilla .txt aquí si lo prefieres
            cuerpo_mensaje = (
                f"Has recibido un nuevo mensaje de contacto:\n\n"
                f"Nombre: {nombre}\n"
                f"Teléfono: {fono}\n"
                f"Correo: {correo}\n"
                f"Asunto: {asunto}\n"
                f"Mensaje:\n{mensaje}"
            )
            send_mail(
                subject=f"[Contacto] {asunto}",
                message=cuerpo_mensaje,
                from_email=None,
                recipient_list=[settings.CONTACT_EMAIL],  # O lista de destinatarios
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error al enviar el correo de contacto: {e}")

        messages.success(self.request, ('Tu mensaje fue enviado correctamente'))

        return super().form_valid(form)
############################################################################################################################################    ContactView
class AboutView(TemplateView):
    template_name = TEMPLATE_MAIN_ABOUT
    title = 'Nosotros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
