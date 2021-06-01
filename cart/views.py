from django.shortcuts import render
from django.urls import reverse


def cart(request):
    return render(request, 'store/cart.html')
