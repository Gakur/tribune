from django.conf import settings
from django .conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    # path('welcome',views.welcome, name = 'welcome'),
    path('',views.news_of_day, name='newsToday'),
    path('archives/<slug:past_date>/', views.past_days_news, name = 'pastNews'),
    path('search/',views.search_results, name= 'search_results'),
    path('article/(\d+)', views.article, name = 'article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
