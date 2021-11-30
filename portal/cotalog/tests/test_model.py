from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from cotalog.models import Videocard, Category

class VideocartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        image = SimpleUploadedFile(name = 'test.jpg', content = b'\x00')
        category = Category.objects.create(name='test', slug='test', image = image)
        product = Videocard.objects.create(manufacture ='Nvidia 1660ti',
                                           model_product = 'GameRock',
                                           slug = 'nvidia-1660-ti',
                                           image = image,
                                           price = 1999.99, category=category,
                                           company = 'Nvidia',
                                           processor = '1660ti',videomemory = '16')


    def test_product_manufacture(self):
        product = Videocard.objects.first()
        self.assertEqual(product.manufacture, 'Nvidia 1660ti')

    def test_product_slug(self):

        product = Videocard.objects.first()
        self.assertEqual(product.slug, 'nvidia-1660-ti')

    def test_product_company(self):

        product = Videocard.objects.first()
        self.assertEqual(product.company, 'Nvidia')

    def test_product_processor(self):

        product = Videocard.objects.first()
        self.assertEqual(product.processor, '1660ti')


    def test_product_manufacture(self):
        product = Videocard.objects.first()
        max_length = product._meta.get_field('manufacture').max_length
        self.assertEqual(max_length, 50)
