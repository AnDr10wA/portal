import scrapy
from scraper.scraper.items import ScraperItem
from cotalog.models import Category, Videocard

class ComputesSpider(scrapy.Spider):
    name = 'videocards'
    allowed_domains = ['www.wildberries.ru']
    start_urls = [
        'https://www.wildberries.ru/catalog/elektronika/noutbuki-i-kompyutery/komplektuyushchie-dlya-pk?sort=popular&page=1&xsubject=3274',
    ]

    def parse(self, response, **kwargs):
        for product in response.css('div.j-card-item'):
            link_to_product = product.css('a.j-open-full-product-card::attr(href)').get()
            yield response.follow(link_to_product, callback=self.parse_product)
        next_page = response.css('a.pagination-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    def parse_product(self, response):
        product = response.css('div.main__container')
        table = response.xpath('//table[@class="product-params__table"]/tbody/tr')
        price_block = response.xpath('//div[@class="price-block "]')
        slug_block = response.xpath('//div[@class="same-part-kt__common-info"]')
        image_block = response.xpath('//div[@class="slide__content img-plug current"]')


        for prod in product:
            pr_item = ScraperItem()
            price = price_block.xpath('div[@class="price-block__content"]/p[@class="price-block__price-wrap"]/span[@class="price-block__final-price"]/text()').get()
            name = prod.css('h1.same-part-kt__header > span::text').get()
            # descr = prod.css('div.j-description > p::text').get()
            slug = slug_block.xpath('p[@class="same-part-kt__article"]/span[@id="productNmId"]/text()').get()
            image = image_block.xpath('picture/source/@srcset').get()[2:]

            for row in table:

                if row.xpath('th/span[ @class="product-params__cell-decor"]/span/text()').get() == 'Видеопроцессор':
                    vproc = row.xpath('td/text()').get()
                elif row.xpath('th/span[ @class="product-params__cell-decor"]/span/text()').get() == 'Модель':
                    model = row.xpath('td/text()').get()
                elif row.xpath('th/span[ @class="product-params__cell-decor"]/span/text()').get() == 'Производитель видеопроцессора':
                    company = row.xpath('td/text()').get()
                elif row.xpath('th/span[ @class="product-params__cell-decor"]/span/text()').get() == 'Объем памяти видеоадаптера':
                    videomemory = row.xpath('td/text()').get()
                    videomemory = videomemory.replace('Гб', '').replace('Мб', '').replace('Gb', '').strip()




            if price != None:
                price = price.replace('\u00a0', '').replace('\u20bd', '').strip()
            else:
                price = 0
            # print(f'{price}-{name}')
            pr_item['manufacture'] = name
            pr_item['price'] = price
            pr_item['model_product'] = model
            pr_item['processor'] = vproc
            pr_item['videomemory'] = videomemory
            pr_item['category'] = Category.objects.get(name = 'videocard')
            pr_item['image'] = image
            pr_item['slug'] = slug
            pr_item['company'] = company

            yield pr_item


            #
            # {
            #
            #
            #     'name': name,
            #     'model': model,
            #     'price': price,
            #     'vproc': vproc,
            #     'slug': slug,
            #     'company':company,
            #     'videomemory': videomemory,
            #     'image': image
            #
            # }



