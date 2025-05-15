# Django imports
from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, ListView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
# Local app imports
from .models import CustomUser
from .forms import UserForm, StaffUserForm, SuperUserForm, UserUpdateForm
# Local app imports
from core.utils.utils import delete_previous_media
from core.utils.texts import WITHOUT_PERMISSION
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, KeyMap

############################################################################################################################################    User Create
class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = Templates.Users.ADD
    success_url = reverse_lazy(URLS.Main.LOGIN)
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
        context['login_url'] = reverse(URLS.Main.LOGIN)
        return context

############################################################################################################################################    User Update
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = Templates.Users.UPT
    form_class = UserUpdateForm
    title = 'Editar Perfil'

    def test_func(self):
        user = self.request.user
        perfil_usuario = self.get_object()
        return user.is_authenticated and (user.is_superuser or user.is_staff or user == perfil_usuario)

    def handle_no_permission(self):
        messages.error(self.request, WITHOUT_PERMISSION)
        return redirect(URLS.Main.INDEX)

    def get_success_url(self):
        # Obtener el pk del usuario actualizado
        pk = self.object.pk
        return reverse_lazy(URLS.Users.DTL, kwargs={'pk': pk})

    def get_username(self):
        return self.object.username

    def form_valid(self, form):
        # Obtener el objeto actual
        objeto = self.get_object()
        media_url = objeto.get_img_url() if objeto else None

        # Actualizar el objeto
        self.object = form.save()

        # Si hay una nueva foto, elimina la anterior
        if 'avatar' in self.request.FILES and media_url:
            try:
                delete_previous_media(media_url)
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la imagen anterior: {e}')

        # Mensaje de éxito
        messages.success(self.request, f'Información actualizada exitosamente!')

        # Redirigir a la vista detallada del usuario
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()
        success_url= self.get_success_url()
        context['username'] = self.get_username()
        context['img_url'] = img_url
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        return context

############################################################################################################################################    User List
class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = Templates.Users.LST
    context_object_name = 'usuarios'
    title = 'Lista de Usuarios'

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.is_staff)

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción.')
        return redirect(URLS.Home.COMMON)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = self.get_queryset()

        # Añadir la combinación "Edad (Fecha de Nacimiento)" para cada usuario
        for user in context['usuarios']:

            # Concatenar nombres si están disponibles
            if user.first_name and user.last_name:
                user.full_name = f"{user.first_name} {user.last_name}"
            else:
                user.full_name = user.first_name or user.last_name or "Sin Información"

            if user.birth_date:
                # Usar el método `get_edad` para obtener la edad
                age = user.get_edad()
                # Asignar el formato "Edad (Fecha de Nacimiento)"
                user.display_age_birthdate = f"{age} años ({user.birth_date})"
            else:
                user.display_age_birthdate = "Sin Información"

        context['title'] = self.title
        context['class'] = CSSBackground.Users.USER
        context['js_action'] = JSConstants.ACTIONS
        context['js_script'] = JSConstants.users.USER
        context['key_map'] = KeyMap.Users.USER
        context['buttons'] = [
            {
                'url': reverse_lazy(URLS.Home.COMMON),
                'label': 'Inicio',
                'icon': 'bi bi-house',
                'show': True
            },
            {
                'url': reverse_lazy(URLS.Users.ADD),
                'label': 'Añadir',
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Users.ADD_SUPER),
                'label': 'Añadir Super Usuario',
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
            {
                'url': reverse_lazy(URLS.Users.ADD_STAFF),
                'label': 'Añadir Usuario al Equipo',
                'icon': 'bi bi-person-add',
                'show': self.request.user.is_superuser or self.request.user.is_staff
            },
        ]
        return context

############################################################################################################################################    User Detail
class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = Templates.Users.DTL
    context_object_name = 'usuario'
    title = 'Perfil '
    cancel_url = reverse_lazy(URLS.Users.LST)

    def test_func(self):
        user = self.request.user
        perfil_usuario = self.get_object()
        return user.is_authenticated and (user.is_superuser or user.is_staff or user == perfil_usuario)

    def handle_no_permission(self):
        messages.error(self.request, 'No tienes los permisos para realizar esta acción!')
        return redirect(URLS.Main.INDEX)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objeto = self.get_object()
        img_url = objeto.get_img_url()
        edad = objeto.get_edad()
        context['edad'] = edad
        context['img_url'] = img_url
        context['class'] = CSSBackground.Users.USER
        context['title'] = self.title
        context['listURL'] = reverse_lazy(URLS.Users.LST)
        context['homeURL'] = reverse_lazy(URLS.Home.COMMON)
        return context

############################################################################################################################################    User Login
class CustomLoginView(LoginView):
    template_name = Templates.Users.LOGIN
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = CSSBackground.Users.USER
        context['title'] = ('Iniciar Sesión')
        context['REGISTER'] = ('Iniciar Sesión')
        context['register_url'] = reverse(URLS.Users.ADD)
        return context

    def form_valid(self, form):
        # Añadir mensaje de éxito al iniciar sesión
        messages.success(self.request, 'Has iniciado sesión correctamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Añadir mensaje de éxito al iniciar sesión
        messages.error(self.request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
        return self.render_to_response(self.get_context_data(form=form))

############################################################################################################################################    User Logout
class CustomLogoutView(LoginRequiredMixin, UserPassesTestMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            response = super().dispatch(request, *args, **kwargs)
            messages.info(request, 'Has cerrado sesión correctamente.')
            return response
        else:
            # Manejar otro tipo de solicitud aquí si es necesario
            return super().dispatch(request, *args, **kwargs)
    def test_func(self):
        return self.request.user.is_authenticated

############################################################################################################################################    User Change Password
class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    template_name = Templates.Users.CHANGE_PASS
    title = 'Cambiar Contraseña'
    success_url = reverse_lazy (URLS.Main.INDEX)
    dispatch_url = reverse_lazy (URLS.Main.LOGIN)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.dispatch_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña Actualizada')
        user = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)
        return super().form_invalid(form)

    def get_cancel_url(self):
        user = self.request.user
        return reverse_lazy(URLS.Users.DTL, kwargs={'pk': user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['class'] = CSSBackground.Users.USER
        context['cancel_url'] = self.get_cancel_url()
        context['dispatch_url'] = self.dispatch_url
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
