""" Файл определяет маршруты для приложения pages. 
    Он связывает URL-адреса с представлениями, которые отображают статические страницы. """

from django.urls import path

from . import views

app_name = 'pages' #пространство имен для URL

urlpatterns = [ #список маршрутов
    path('about/', views.AboutView.as_view(), name='about'),
    path('rules/', views.RulesView.as_view(), name='rules'),
]
