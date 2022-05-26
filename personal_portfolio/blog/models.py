from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    date = models.DateField(verbose_name='Дата')
    is_published = models.BooleanField(default=False, verbose_name='Статус публикации')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
