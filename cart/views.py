from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from repair_service.models import Service
from .cart import Cart
from .forms import CartAddProductForm
from django.core.exceptions import PermissionDenied


@require_POST
def cart_add(request, service_id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    service = get_object_or_404(Service, id=service_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(service=service,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, service_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    service = get_object_or_404(Service, id=service_id)
    cart.remove(service)
    return redirect('cart:cart_detail')


def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    for item in cart:
        initial = {
            'quantity': item['quantity'],
            'update': True
        }
        item['update_quantity_form'] = CartAddProductForm(initial=initial)
    return render(request, 'cart/detail.html', {'cart': cart})
