from django.urls import path, include
from .views import (IndexView, ContactView, AboutView)

app_name = 'pages_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('About/', AboutView.as_view(), name='about'),
]
