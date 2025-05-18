from django.views.generic import (TemplateView)
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactoForm  # Asegúrate de tener este form
from core.utils.send_emails import send_contact_email
from core.utils.constants import Templates, URLS
from django.utils.translation import gettext_lazy as _

############################################################################################################################################    IndexView
class IndexView(TemplateView):
    template_name = Templates.Main.INDEX
    title = _('Inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

############################################################################################################################################    ContactView
class ContactView(FormView):
    template_name = Templates.Main.CONTACT
    form_class = ContactoForm
    success_url = reverse_lazy(URLS.Main.CONTAC)  # Cambia esto según tu config
    title = _('Contáctanos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title.upper()
        return context

    def form_valid(self, form):
        try:
            send_contact_email(
                nombre=form.cleaned_data['nombre'],
                fono=form.cleaned_data['fono'],
                correo=form.cleaned_data['correo'],
                asunto=form.cleaned_data['asunto'],
                mensaje=form.cleaned_data['mensaje'],
            )
            messages.success(self.request, _('Tu mensaje fue enviado correctamente'))
        except Exception as e:
            messages.error(self.request, _('Ocurrió un error al enviar tu mensaje. Intenta nuevamente.'))

        return super().form_valid(form)


############################################################################################################################################    ContactView
class AboutView(TemplateView):
    template_name = Templates.Main.ABOUT
    title = _('Nosotros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

class TermsView(TemplateView):
    template_name = Templates.Main.TERMS
    title = _('Términos y condiciones')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class PrivacyView(TemplateView):
    template_name = Templates.Main.PRIVACY
    title = _('Política de Privacidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


