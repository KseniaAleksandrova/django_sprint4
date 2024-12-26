""" Файл отвечает за создание форм для модели Post и Comment. 
Он используется для удобного ввода данных в эти модели через веб-страницу. """

from django import forms
from django.utils import timezone

from blog.models import Comment, Post

""" Форма для создания и редактирования поста.
Включает поле для даты публикации, которое автоматически устанавливается на текущее время. """
class PostForm(forms.ModelForm): # Определяем класс PostForm, наследующий от ModelForm

    def __init__(self, *args, **kwargs):
        """ Инициализация формы, установка начального значения для поля 'pub_date' на текущее время. """
        super(PostForm, self).__init__(*args, **kwargs) # Вызываем конструктор родительского класса
        self.fields['pub_date'].initial = timezone.now()

    class Meta:
        model = Post #указываем, что форма связана с моделью Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={ # Настраиваем виджет для поля 'pub_date'
                'type': 'datetime-local',
                'format': '%Y-%m-%dT%H:%M'
            }),
        }

""" Форма для создания комментариев.
Исключает поля 'author', 'post' и 'is_published' из формы, 
так как они заполняются автоматически системой. """
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #указываем, что форма связана с моделью Comment
        exclude = ('author', 'post', 'is_published')
