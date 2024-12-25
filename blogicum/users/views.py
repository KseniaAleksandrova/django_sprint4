""" Определяет логику регистрации пользователя через представление. """

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


""" Представление для регистрации нового пользователя. """
class UserCreateView(CreateView):
    model = get_user_model()
    template_name = 'registration/registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:index')
