""" Файл содержит абстрактные базовые модели IsPublished и CreatedAt. """

from django.db import models


class IsPublished(models.Model):
    """Модель статуса публикации.
    Абстрактная модель, добавляющая логическое поле is_published.
    Используется для управления видимостью объектов в интерфейсе. """

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True


class CreatedAt(models.Model):
    """Модель времени создания.
    Абстрактная модель, добавляющая поле created_at, используется для отслеживания времени добавления записей. """

    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
