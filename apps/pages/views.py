from django.views.generic import (TemplateView)

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
class ContactView(TemplateView):
    template_name = TEMPLATE_MAIN_CONTACT
    title = 'Contactanos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

############################################################################################################################################    ContactView
class AboutView(TemplateView):
    template_name = TEMPLATE_MAIN_ABOUT
    title = 'Nosotros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
