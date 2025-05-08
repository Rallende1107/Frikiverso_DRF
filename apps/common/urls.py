from django.urls import path, include
from .views import IndexView


app_name = 'common_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # apis url
    # path('api/', include('apps.common.api.urls')),
]
