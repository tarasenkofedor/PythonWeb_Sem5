from django.urls import path
from . import views

app_name = 'info_service'

urlpatterns = [
    path('about', views.about_company, name='about_company'),
    path('news', views.news_list, name='news_list'),
    path('news/<int:id>/', views.news_by_id, name='news_detail'),
    path('faq', views.faq_list, name='faq'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('workers', views.our_workers, name='workers'),
    path('sales', views.sales, name='sales'),
    path('vacancies', views.vacancy_list, name='vacancies'),
    path('feedback', views.feedbacks_page, name='feedbacks_page'),
    path('feedback/create/', views.create_feedback, name='create_feedback')
]
