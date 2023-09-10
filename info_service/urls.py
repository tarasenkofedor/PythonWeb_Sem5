from django.urls import path
from . import views

app_name = 'info_service'

urlpatterns = [
    path('about', views.about_company, name='about_company'),
    path('news', views.news, name='about_company'),
]
