from django.urls import path

from .views import home_view, shop_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shop', shop_view, name='shop'),
]
