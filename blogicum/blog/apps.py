""" Файл apps.py определяет настройки для приложения blog. """

from django.apps import AppConfig # Импортируем базовый класс AppConfig из Django для настройки приложения



class BlogConfig(AppConfig): # Определяем класс BlogConfig, который наследует от AppConfig

    default_auto_field = 'django.db.models.BigAutoField' # Указываем тип поля по умолчанию для автоматического увеличения (BigAutoField)
    name = 'blog' # Задаем имя приложения
    verbose_name = 'Блог'
