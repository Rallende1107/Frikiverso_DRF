from django.urls import path, include
from .views import HomeView


app_name = 'movie_app'
urlpatterns = [

    path('home/', HomeView.as_view(), name='home'),
    # apis url
    path('api/', include('apps.movie.api.urls')),
]
