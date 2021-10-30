from django.test import TestCase
from cotalog.models import Processor
class CotalogDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        image = SimpleUploadedFile(name='test.jpg', content=b'\x00')
        category = Category.objects.create(name='processor', slug='processor', image=image)
        test_product = Processor.objects.create(manufacture = 'Intel', model_product = 'Core i9',
                                                slug = 'intel-i9', image = image,
                                                price = 1700.00, socet = '1200',
                                                frequency = '4400', amount_core = 10,
                                                category = 'processor')


