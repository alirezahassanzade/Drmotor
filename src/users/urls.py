from django.urls import path

from .views import profile_view, login_view, register_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
