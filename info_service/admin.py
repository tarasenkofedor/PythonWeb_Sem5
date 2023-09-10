from django.contrib import admin

from info_service.models import News


# Register your models here.
@admin.register(News)
class ServiceAdmin(admin.ModelAdmin):
    pass
