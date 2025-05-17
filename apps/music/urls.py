from django.urls import path, include
from .views import HomeView


app_name = 'music_app'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

    # apis url
    path('api/', include('apps.music.api.urls')),
]
