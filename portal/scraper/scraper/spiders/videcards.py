import scrapy
from scraper.items import ScraperItem


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

        for prod in product:
            pr_item = ScraperItem()
            price = prod.css('span.price-block__commission-current-price::text').get()
            name = prod.css('h1.same-part-kt__header > span::text').get()
            descr = prod.css('div.j-description > p::text').get()
            vproc = prod.css('table.product-params__table > td.product-params__cell').get()

            if price != None:
                price = price.replace('\u00a0', '').replace('\u20bd', '').strip()
            else:
                price = 0
            # print(f'{price}-{name}')
            # pr_item['name'] = name
            # pr_item['price'] = price
            # pr_item['description'] = descr

            yield {

                'link': response.url,
                'name': name,
                'description': descr,
                'price': price,
                'vproc': vproc

            }



