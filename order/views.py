from django.shortcuts import render
from .models import OrderItem, Client
from cart.cart import Cart
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("You don't have access to this page.")

    cart = Cart(request)
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        order = Order.objects.create(client=Client.objects
                                     .filter(email=user_email)
                                     .first())

        for item in cart:
            OrderItem.objects.create(order=order,
                                     service=item['service'],
                                     price=item['cost'],
                                     quantity=item['quantity'])
            # item['service'].purchase_count += item['quantity']
            item['service'].save()
        # clear cart
        cart.clear()
        return render(request, 'order/created.html', {'order': order})

    customers_emails = Client.objects.all().values_list('email', flat=True)
    return render(request, 'order/create.html', {
        'cart': cart,
        'emails': customers_emails
    })
