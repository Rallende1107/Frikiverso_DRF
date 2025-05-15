from django.urls import path, include
from .views import HomeView


app_name = 'serie_app'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

    # apis url
    # path('api/', include('apps.renpy.api.urls')),
]
