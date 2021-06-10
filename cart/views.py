from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from store.models import Product
from .models import Cart, CartItem


def _crat_id(request):
    cart = request.session.session_key
    if not cart:
        request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_crat_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_crat_id(request)
        )
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()
    return redirect('cart')


def decrease_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_crat_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_crat_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()

    return redirect('cart')


def cart(request, total=0, quantity=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=_crat_id(request))
        cart_item = CartItem.objects.filter(cart=cart)
        for item in cart_item:
            total += (item.product.price * item.quantity)
            quantity += item.quantity
    except:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_item': cart_item,
    }

    return render(request, 'store/cart.html', context)
