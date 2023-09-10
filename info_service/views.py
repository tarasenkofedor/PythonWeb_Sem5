from django.shortcuts import render, get_object_or_404

from info_service.models import News


# Create your views here.


def about_company(request):
    return render(request, 'info_service/about.html')


def news_list(request):
    news = News.objects.order_by('-created_at')  # sort by creation time in descending order
    return render(request, 'info_service/news.html', {'news_list': news})


def news_by_id(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'info_service/news_detail.html', {'news': news})
