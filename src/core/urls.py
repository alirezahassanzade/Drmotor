from django.urls import path

from .views import home_view, shop_view, panel_view, error_view, emergency_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shop', shop_view, name='shop'),
    path('panel', panel_view, name='panel'),
    path('404', error_view, name='error'),
    path('emergency', emergency_view, name='emergency')
]
