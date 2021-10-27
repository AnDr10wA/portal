from django.db import models
from django.shortcuts import reverse
class CategoryForum(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug')
    body = models.TextField(blank=True, verbose_name='Текст')
    create_date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_category_forum_url',kwargs={'slug':self.slug})


class TopicForum(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема")
    slug = models.SlugField(max_length=100, verbose_name='Slug')
    body = models.TextField(blank=True, verbose_name='Текст')
    create_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(CategoryForum, related_name='topics', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('topic_detail_url',kwargs={'slug':self.slug})

class MessageForum(models.Model):
    author = models.CharField(max_length=100, default='Guest')
    text = models.CharField(max_length=255)
    topic = models.ForeignKey(TopicForum, related_name='messages', on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text