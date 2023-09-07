from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

from repair_service.models import Service


class Client(models.Model):
    first_name = models.CharField(max_length=200, help_text='Enter first name')
    last_name = models.CharField(max_length=200, help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, help_text='Enter phone number')

    def clean(self):
        super().clean()

        # Check age validation (18+)
        age = timezone.now().date().year - self.date_of_birth.year
        if age < 18:
            raise ValidationError("Clients must be 18 years or older.")

        # Check phone number format
        import re
        phone_regex = r'^\+375(29|44|33)\d{7}$'
        if not re.match(phone_regex, self.phone_number):
            raise ValidationError("Invalid phone number format. It should be in the format '+375(29|44|33)1234567'.")

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, related_name='order_items', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
