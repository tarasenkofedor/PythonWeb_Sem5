from django.urls import path

from .views import (
    home_screen_view,
    create_service,
    delete_service,
    service_detail,
    service_list,
    edit_service,
)

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('services/', service_list, name='service_list'),
    path('services/<int:id>/', service_detail, name='service_detail'),
    path('services/edit/<int:id>/', edit_service, name='edit_service'),
    path('services/create', create_service, name='create_service'),
    path('services/delete/<int:id>/', delete_service, name='delete_service')
]
