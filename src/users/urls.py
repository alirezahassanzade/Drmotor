from django.urls import path

from .views import SigninView, SignupView

urlpatterns = [
    # path('profile/', profile_view, name='profile'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
]
