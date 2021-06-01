from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:slug>/', views.store, name='p-store'),
    path('<slug:slug>/<slug:p_slug>/', views.detail, name='detail'),
]
