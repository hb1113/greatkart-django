from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add-cart'),
    path('decrease-cart/<int:product_id>/', views.decrease_cart, name='decrease-cart'),
    path('remove-cart/<int:product_id>/', views.remove_cart, name='remove-cart'),
]