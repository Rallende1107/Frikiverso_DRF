# Django imports
from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, ListView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
# Local app imports
from apps.users.models import CustomUser
from apps.users.forms import UserForm, StaffUserForm, SuperUserForm
# Local app imports
from core.utils.utils import delete_previous_media
from core.utils.texts import WITHOUT_PERMISSION
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, KeyMap

class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = Templates.Users.ADD
    success_url = reverse_lazy(URLS.Users.LOGIN)
    title = 'Registrate'

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
class StaffUserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = StaffUserForm
    template_name = Templates.Users.ADD
    success_url = reverse_lazy(URLS.Users.LST)
    title = 'Añadir Usuario Staff'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción!')
        return redirect(URLS.Users.LST)

    def form_valid(self, form):
        messages.success(self.request, 'Usuario de Staff Registrado Exitosamente!')
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
class SuperUserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = SuperUserForm
    template_name = Templates.Users.ADD
    success_url = reverse_lazy(URLS.Users.LST)
    title = 'Añadir Super Usuario'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción!')
        return redirect(URLS.Users.LST)

    def form_valid(self, form):
        messages.success(self.request, 'Super Usuario Registrado Exitosamente!')
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