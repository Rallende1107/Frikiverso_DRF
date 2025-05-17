from django.urls import path
from .views import TestView

app_name = 'api_music_app'

urlpatterns = [
    path('test/', TestView.as_view(), name='test_music_app'),

]
