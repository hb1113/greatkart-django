from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:slug>/', views.store, name='p-store'),
    path('category/<slug:slug>/<slug:p_slug>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
