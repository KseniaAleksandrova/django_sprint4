""" Файл регистрирует приложение users в проекте. 
Он используется для настройки и определения базовых параметров приложения(имя приложения, настройки автоматических первичных ключей). """

from django.apps import AppConfig

""" Настройка приложения users. """
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
