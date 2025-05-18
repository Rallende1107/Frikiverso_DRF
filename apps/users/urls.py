# Importando path Django
from django.urls import path, include
# Importando vistas
from apps.users.views.auth_views import CustomLoginView, CustomLogoutView, ChangePasswordView
from apps.users.views.create_views import UserCreateView, SuperUserCreateView, StaffUserCreateView
from apps.users.views.update_views import UserUpdateView
from apps.users.views.list_views import UserListView
from apps.users.views.detail_views import UserDetailView
from apps.users.views.password_reset_views import (CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView,)
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

    path('forget_password/', CustomPasswordResetView.as_view(), name='forget_password'),
    path('forget_password/done/', CustomPasswordResetDoneView.as_view(), name='forget_password_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Rutas de API (descomentarlas si es necesario)
    path('api/', include('apps.users.api.urls')),
]