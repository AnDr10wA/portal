from scrapy_djangoitem import DjangoItem
from cotalog.models import Videocard

import scrapy


class ScraperItem(DjangoItem):
    django_model = Videocard



