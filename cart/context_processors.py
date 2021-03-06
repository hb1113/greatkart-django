from .models import Cart, CartItem
from .views import _crat_id


def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_crat_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for item in cart_items:
                count += item.quantity
        except Cart.DoesNotExist:
            count = 0
    return dict(count=count)
