# Django imports
from django.contrib import messages
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

# Local app imports - Modelos y formularios
from apps.users.models import CustomUser
from apps.users.forms import (UserForm, StaffUserForm, SuperUserForm)

# Local app imports - Utilidades y mixins personalizados
from core.utils.constants import (Templates, URLS, CSSBackground, JSConstants, KeyMap)
from core.utils.mixins import PermissionRequiredMessageMixin

# Create your views here.
############################################################################################################################################    User Login
class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = Templates.Users.CREATE
    success_url = reverse_lazy(URLS.Users.LOGIN)
    title = _('Registrate')

    def form_valid(self, form):
        messages.success(self.request, 'Te has Registrado Exitosamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['special'] = False
        context['login_url'] = reverse(URLS.Users.LOGIN)
        return context

############################################################################################################################################    User Staff Create
class StaffUserCreateView(PermissionRequiredMessageMixin, CreateView):
    model = CustomUser
    form_class = StaffUserForm
    template_name = Templates.Users.CREATE
    success_url = reverse_lazy(URLS.Users.LIST)
    title = _('Añadir Usuario Staff')
    permission_redirect_url = reverse_lazy(URLS.Home.COMMON)

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, _('¡Usuario de Staff Registrado Exitosamente!'))
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        context['special'] = True
        return context

############################################################################################################################################    User Staff
class SuperUserCreateView(PermissionRequiredMessageMixin, CreateView):
    model = CustomUser
    form_class = SuperUserForm
    template_name = Templates.Users.CREATE
    success_url = reverse_lazy(URLS.Users.LIST)
    title = _('Añadir Super Usuario')
    permission_redirect_url = reverse_lazy(URLS.Home.COMMON)

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, _('¡Super Usuario Registrado Exitosamente!'))
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        context['special'] = True
        return context