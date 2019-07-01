from django.urls import path

from .views import shop_view, add_to_basket, ProductDetailView

urlpatterns = [
    path('', shop_view, name='shop'),
    path('add_to_basket/', add_to_basket, name='add_to_basket'),
    path('shop/product/<slug:slug>/', ProductDetailView.as_view(), name='product'),

]
