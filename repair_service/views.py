import requests
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from cart.forms import CartAddProductForm
from info_service.models import News
from repair_service.forms import ServiceForm
from repair_service.models import Service
import logging

logger = logging.getLogger('')
JOKE_API = 'https://official-joke-api.appspot.com/jokes/programming/random'


def home_screen_view(request):
    latest_news = News.objects.latest('created_at')
    logger.info('INFO: Show home page')
    return render(request, 'repair_service/home.html', {'latest_news': latest_news})


def service_list(request):
    logger.info('INFO: Get all services from database')
    services = Service.objects.all()
    logger.info(f"INFO: Send request to API '{JOKE_API}'")
    joke_data = requests.get(JOKE_API).json()[0]
    joke = joke_data['setup'] + joke_data['punchline']
    return render(request, 'repair_service/services.html', {
        'services': services,
        'joke': joke
    })


def edit_service(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied("You don't have access to this function.")

    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        logger.info('INFO: Request for editing service=' + str(service))
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        logger.info('INFO: Get form for editing service=' + str(service))
        form = ServiceForm(instance=service)
    return render(request, 'repair_service/create.html', {'form': form})


def create_service(request):
    if not request.user.is_superuser:
        raise PermissionDenied("You don't have access to this function.")

    if request.method == 'POST':
        logger.info('INFO: Process form for creating service')
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            return redirect('/services/', pk=service.pk)
    else:
        logger.info('INFO: Get form for creating service')
        form = ServiceForm()
    return render(request, 'repair_service/create.html', {'form': form})


def delete_service(request, id):
    logger.info('INFO: Request for deleting service')
    if not request.user.is_superuser:
        raise PermissionDenied("You don't have access to this function.")

    service = Service.objects.get(id=id)
    service.delete()
    return redirect('service_list')


def service_detail(request, id):
    logger.info('INFO: Show service details')
    service = get_object_or_404(Service, id=id)
    cart_service_form = CartAddProductForm()
    return render(request, 'repair_service/detail.html', {
        'service': service,
        'cart_service_form': cart_service_form
    })
