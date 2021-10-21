from django.db import models


class HelpMessage(models.Model):

    firstname = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, blank=True, verbose_name= 'Фамилия')
    email = models.EmailField(max_length=100, verbose_name= 'Элетронная почта')
    message = models.TextField(verbose_name='Описание проблемы')

    def __str__(self):
        return self.email
