# Importando path Django
from django.urls import path, include
# Importando vistas
from .views import (
    UserCreateView, UserUpdateView, UserDetailView, UserListView,
    CustomLoginView, CustomLogoutView,
    SuperUserCreateView, StaffUserCreateView,
    ChangePasswordView,
)
# Definició nombre App
app_name = 'users_app'

# Definición de rutas (URLs)
urlpatterns = [
    # Autenticación
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    # Gestión de usuarios
    path('list/', UserListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    # Creación de usuarios especiales
    path('create/superuser/', SuperUserCreateView.as_view(), name='superuser_create'),
    path('create/staffuser/', StaffUserCreateView.as_view(), name='staffuser_create'),
    # Cambio de contraseña
    path('change/password/', ChangePasswordView.as_view(), name='password_change'),

    # Rutas de API (descomentarlas si es necesario)
    # path('api/', include('apps.renpy.api.urls')),
]
