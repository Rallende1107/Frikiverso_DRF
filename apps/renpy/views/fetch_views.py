# Django imports
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from django.views.generic.edit import FormView
# from apps.renpy.forms import (F95GameFetchStatus,)
from apps.renpy.forms import (LoadGamesForm)

# Project-level imports - Mixins and utilities
from core.utils.constants import (CSSBackground, ImageCards, JSConstants, KeyMap, Templates, URLS,)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################
class GamesLoadView(PermissionRequiredMessageMixin, FormView):
    template_name = Templates.Renpy.Game.LOAD
    form_class = LoadGamesForm
    success_url = reverse_lazy(URLS.Renpy.Game.LIST)
    permission_redirect_url = URLS.Home.RENPY
    title = _('Cargar Juegos desde F95')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        inicio = form.cleaned_data['inicio']
        fin = form.cleaned_data['fin']
        print(f'inicio {inicio}')
        print(f'fin {fin}')

        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Renpy.GAME
        context['title'] = self.title
        context['cargar'] = True
        context['cancel_url'] = self.success_url
        return context