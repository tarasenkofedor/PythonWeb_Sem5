from django.contrib import admin

from info_service.models import News, PromoCode, Vacancy


# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
