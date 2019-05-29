from django.urls import path

from .views import home_view, error_view


urlpatterns = [
    path('', home_view, name='home'),
    path('404', error_view, name='error'),
]
