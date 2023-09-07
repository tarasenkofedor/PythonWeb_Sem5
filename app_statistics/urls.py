from django.urls import path

from app_statistics import views

urlpatterns = [
    path('', views.main_statistics, name='main-statistics'),
]
