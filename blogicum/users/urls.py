""" Настраивает маршруты для приложения users.
    Добавляет маршрут для регистрации пользователей. """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserCreateView.as_view(), name='registration'),
]
