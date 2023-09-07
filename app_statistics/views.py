import matplotlib.pyplot as plt
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from repair_service.models import ServiceTag


def main_statistics(request):
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")

    x = [tag.name for tag in ServiceTag.objects.all()]
    y = []

    tags = ServiceTag.objects.prefetch_related().all()
    for tag in tags:
        y.append(tag.service_set.count())

    plt.bar(x, y, color="aquamarine", width=0.1)

    plt.xlabel('Service tag name')
    plt.ylabel('Amount of services that used tag')
    plt.title('Stats')

    plt.savefig('app_statistics/static/app_statistics/img/main_statistics.png', format='png')
    plt.clf()
    return render(request, 'app_statistics/main_statistics.html')
