""" Файл служит для определения конфигурации приложения pages. """

from django.apps import AppConfig

""" Настройки для приложения, обрабатывающего статические и вспомогательные  страницы """
class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
