from django.urls import path

from .views import SigninView, SignupView, SignoutView

urlpatterns = [
    # path('profile/', profile_view, name='profile'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signout/', SignoutView.as_view(), name='signout'),
]
