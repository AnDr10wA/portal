from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name= 'Наименование')
    slug = models.SlugField(max_length=100, unique=True, verbose_name= 'SLUG')
    image = models.ImageField(upload_to='category')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail_url',kwargs={'slug':self.slug})


class Product(models.Model):
    manufacture = models.CharField(max_length=50, verbose_name='Производитель')
    model_product = models.CharField(max_length=50, verbose_name='Модель',unique=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to=f'products/', blank=True, verbose_name='Изображение1')
    image2 = models.ImageField(upload_to=f'products/', blank=True, verbose_name='Изображение2')
    image3 = models.ImageField(upload_to=f'products/', blank=True, verbose_name='Изображение3')

    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.model_product




class Videocard(Product):
    company_choices = [('nvidia','Nvidia'),
                       ('amd', 'AMD'),
                       ('intel', 'Intel')]
    company = models.CharField(max_length=50, choices=company_choices, verbose_name='Производитель графического процессора')
    processor = models.CharField(max_length=50, verbose_name='Графический процессор')
    videomemory = models.IntegerField(verbose_name='Видеопамять', blank=True)
    category = models.ForeignKey(Category, related_name='videocards', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'

    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug, 'category': self.category.slug})



class Motherboard(Product):
    memory_choices = [('ddr4', 'DDR4'),
                      ('ddr4-so','DDR4-SO'),
                      ('ddr3','DDR3'),
                      ('ddr3-so', 'DDR3-SO'),
                      ('ddr2', 'DDR2') ]
    size_choices = [
        ('atx', 'ATX'),
        ('matx', 'mATX'),
        ('eatx', 'eATX')

    ]

    amount_port_pci = models.IntegerField(verbose_name='Количество портов PCIe', blank=True)
    socet = models.CharField(max_length=50, verbose_name='Сокет', blank=True)
    type_memory = models.CharField(max_length=50, choices=memory_choices, verbose_name='Тип оперативной памяти', blank=True)
    size = models.CharField(max_length=50,choices=size_choices, blank=True, verbose_name='Размер')
    chipset = models.CharField(max_length=50, blank=True, verbose_name='Чипсет')
    category = models.ForeignKey(Category, related_name='motherbords', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'

    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug, 'category': self.category.slug})

class Processor(Product):

    socet = models.CharField(max_length=50, verbose_name='Сокет', blank=True)
    frequency = models.IntegerField(verbose_name='Частота работы')
    amount_core = models.IntegerField(verbose_name='Количество ядер')
    category = models.ForeignKey(Category, related_name='processors', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug, 'category': self.category.slug})

class PowerBlock(Product):

    power = models.IntegerField(verbose_name='Мощность')
    amount_PCIe = models.IntegerField(verbose_name='Количество разъемов PCIe', blank=True)
    amount_sata = models.IntegerField(verbose_name='Количество разъемов SATA', blank=True)
    amount_molex = models.IntegerField(verbose_name='Количество разъемов molex',  blank=True)
    category = models.ForeignKey(Category, related_name='powerblocks', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug, 'category': self.category.slug})

class RAMemory(Product):
    frequency = models.IntegerField(verbose_name='Частота памяти')
    volume = models.IntegerField(verbose_name='Объем памяти')
    category = models.ForeignKey(Category, related_name='ram', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

    def get_absolute_url(self):
        return reverse('product_detail_url',kwargs={'slug':self.slug, 'category': self.category.slug})







