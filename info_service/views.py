from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import date
from info_service.models import News, PromoCode, Vacancy


# Create your views here.


def about_company(request):
    return render(request, 'info_service/about.html')


def news_list(request):
    news = News.objects.order_by('-created_at')  # sort by creation time in descending order
    return render(request, 'info_service/news.html', {'news_list': news})


def news_by_id(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'info_service/news_detail.html', {'news': news})


def faq_list(request):
    return render(request, 'info_service/faq.html')


def privacy_policy(request):
    return render(request, 'info_service/privacy_policy.html')


def our_workers(request):
    return render(request, 'info_service/workers.html')


def sales(request):
    current_date = date.today()
    active_codes = PromoCode.objects.filter(
        expiration_date__gte=current_date,
        activated=False
    )
    inactive_codes = PromoCode.objects.filter(
        Q(expiration_date__lt=current_date) | Q(activated=True)
    )

    return render(request, 'info_service/sales.html', {
        'active_codes': active_codes,
        'inactive_codes': inactive_codes
    })


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'info_service/vacancies.html', {'vacancies': vacancies})
