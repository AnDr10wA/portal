from django.db import models
from django.shortcuts import reverse


class News(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    head = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to= 'media/news/')
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='news')
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-title',)



    def get_absolute_url(self):
        return reverse('news_detail_url',kwargs={'slug':self.slug})


    def __str__(self):
        return self.title



class Tag(models.Model):

    title = models.CharField(max_length=70)
    slug  = models.SlugField(max_length=70)



    def __str__(self):
        return self.title
