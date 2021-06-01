from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, slug=None):
    categories = None

    if slug != None:
        categories = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(is_available=True, category=categories)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def detail(request, slug, p_slug):
    try:
        p = Product.objects.get(category__slug=slug, slug=p_slug)
    except Exception as e:
        raise e
    context = {
        'product': p,
    }
    return render(request, 'store/detail.html', context)
