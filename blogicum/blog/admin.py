""" Файл admin.py содержит настройки административного интерфейса для моделей
Post, Category, Location и Comment. Он настраивает отображение, 
редактирование и фильтрацию данных в админке Django. """

from django.contrib import admin

from .models import Category, Comment, Location, Post

LENGTH_STRING = 50 #Максимальная длина строки для отображения
NUMBER_OF_POSTS = 10 #Количество постов на странице


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Кастомизация админки для модели Post.
    Включает настройки отображения, редактирования, поиска и фильтрации постов. """

    list_display = (
        'title',
        'text_short',
        'location',
        'category',
        'pub_date',
        'is_published',
    )
    list_editable = (
        'location',
        'category',
        'pub_date',
        'is_published',
    )
    search_fields = (
        'title',
        'text',
        'location',
    )
    list_per_page = NUMBER_OF_POSTS

    @staticmethod
    @admin.display(description='Текст') #Описание поля в админке
    def text_short(object: Post) -> str:
        """ Возвращает сокращённый текст поста, 
        чтобы избежать длинных текстов в списке админки. """
        return f'{object.text[:LENGTH_STRING]}...'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Кастомизация админки для модели Category.
    Включает настройки отображения, редактирования и фильтрации категорий. """
    
    list_display = (
        'title',
        'description_short',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = (
        'slug',
    )
    list_filter = (
        'title',
        'description',
    )
    list_per_page = NUMBER_OF_POSTS

    @staticmethod
    @admin.display(description='Описание')
    def description_short(object: Category) -> str:
        """ Возвращает сокращённое описание категории, 
        чтобы избежать длинных описаний в списке админки. """    
        return f'{object.description[:LENGTH_STRING]}...'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ Кастомизация админки для модели Location.
    Управление отображением и фильтрацией локаций. """

    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('name',)
    list_per_page = NUMBER_OF_POSTS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Кастомизация админки для модели Comment.
    Управление отображением и фильтрацией комментариев."""

    list_display = (
        'text',
        'post',
        'author',
        'created_at',
    )
    list_filter = ('text',)
    list_per_page = NUMBER_OF_POSTS
