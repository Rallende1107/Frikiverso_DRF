from django.urls import path
from .views import TestView
from .views import FormatListView, FormatDetailView, LanguageListView, LanguageCreateView

app_name = 'api_common_app'

urlpatterns = [
    path('test/', TestView.as_view(), name='test_api_common'),
    path('formats/', FormatListView.as_view(), name='format_list'),
    path('formats/<slug>', FormatDetailView.as_view(), name='format_detail'),
    path('language/', LanguageListView.as_view(), name='language_detail'),
    path('language/add', LanguageCreateView.as_view(), name='language_create'),

]
