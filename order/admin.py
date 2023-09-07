from django.contrib import admin
from .models import Order, OrderItem, Client


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['service']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'created']
    list_filter = ['created']
    inlines = [OrderItemInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'date_of_birth', 'first_name']
    list_filter = ['phone_number', 'date_of_birth', 'first_name']


admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
