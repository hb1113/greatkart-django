from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _crat_id
from django.core.paginator import Paginator
from django.db.models import Q

def store(request, slug=None):
    categories = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(is_available=True, category=categories)
        paginator = Paginator(products, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        product_count = products.count()
    context = {
        'products': page_obj,
        'product_count': product_count,
        'page_obj': page_obj,
    }
    return render(request, 'store/store.html', context)


def detail(request, slug, p_slug):
    try:
        p = Product.objects.get(category__slug=slug, slug=p_slug)
        in_cart = CartItem.objects.filter(product=p, cart__cart_id=_crat_id(request)).exists()
    except Exception as e:
        raise e
    context = {
        'product': p,
        'in_cart': in_cart,
    }
    return render(request, 'store/detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)