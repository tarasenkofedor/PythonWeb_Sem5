from repair_service.models import (
    ServiceTag,
    Service,
)
from django.contrib import admin


@admin.register(ServiceTag)
class ServiceTagAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_filter = ('name', 'price', 'about')
    search_fields = ('name', 'about')
