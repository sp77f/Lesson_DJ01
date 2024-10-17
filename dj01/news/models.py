from django.db import models
class News(models.Model):
    title = models.CharField('Название новости',max_length=150)
    short_description = models.CharField('Краткое описание',max_length=300)
    content = models.TextField('Новость',blank=True)
    created_at = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор',max_length=150)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    def __str__(self):
        return self.title

