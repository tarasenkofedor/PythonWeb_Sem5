from decimal import Decimal
from django.conf import settings

from repair_service.models import Service


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        service_ids = self.cart.keys()
        services = Service.objects.filter(id__in=service_ids)
        for service in services:
            self.cart[str(service.id)]['service'] = service

        for item in self.cart.values():
            item['cost'] = Decimal(item['cost'])
            item['total_cost'] = item['cost'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, service, quantity=1, update_quantity=False):
        service_id = str(service.id)
        if service_id not in self.cart:
            self.cart[service_id] = {
                'quantity': 0,
                'cost': str(service.price)
            }
        if update_quantity:
            self.cart[service_id]['quantity'] = quantity
        else:
            self.cart[service_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, service):
        service_id = str(service.id)
        if service_id in self.cart:
            del self.cart[service_id]
            self.save()

    def get_total_price(self):
        print(self.cart.values())
        return sum(Decimal(item['cost']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
