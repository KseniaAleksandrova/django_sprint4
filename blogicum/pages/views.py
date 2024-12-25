""" Файл содержит представления для обработки запросов и возврата страниц. """

from django.shortcuts import render
from django.views.generic import TemplateView


""" AboutView и RulesView нужны для отображения страниц "О проекте" и "Правила". """
class AboutView(TemplateView):
    template_name = 'pages/about.html' #отображает статическую страницу "О проекте"


class RulesView(TemplateView):
    template_name = 'pages/rules.html' #отображает статическую страницу "Правила"

""" Обработчики ошибок нужны для возврата пользовательских страниц при возникновении ошибок. """
def page_not_found(request, *args, **kwargs):
    return render(request, 'pages/404.html', status=404) #отображает пользовательскую страницу ошибки 404


def csrf_failure(request, *args, **kwargs):
    return render(request, 'pages/403csrf.html', status=403) #отображает страницу ошибки 403


def internal_error(request, *args, **kwargs):
    return render(request, 'pages/500.html', status=500) #отображает страницу ошибки 500
