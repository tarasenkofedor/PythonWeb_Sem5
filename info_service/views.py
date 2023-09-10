from django.shortcuts import render


# Create your views here.


def about_company(request):
    return render(request, 'info_service/about.html')


def news(request):
    return render(request, 'info_service/news.html')
