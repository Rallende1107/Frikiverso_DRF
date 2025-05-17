from django.urls import path
from .views import TestView

app_name = 'api_movie_app'

urlpatterns = [
    path('test/', TestView.as_view(), name='test_movie_app'),

]
