import scrapy
from scrapy.http import TextResponse
import requests

class NewsSpider(scrapy.Spider):
    name = 'Noticias'

    def parse(self, response):
        for p in response.css('div.glb-grid'):
            item = {
                'title': p.css('h1.content-head__title').get(),
                'subtitle': p.css('h2.content-head__subtitle').get(),
                'text': p.css('p.content-text__container').getall(),
            }

            yield item

def extrairTexto(link = ' '):
    url = str(link)
    response_html = requests.get(url).text
    response = TextResponse(url=url, body=response_html, encoding='utf-8')
    spider = NewsSpider()
    for item in spider.parse(response):
        item['title'] = item['title']
        item['subtitle'] = item['subtitle']
        item['text'] = item['text']

    noticia = item['title'] + item['subtitle'] + item['text']
    noticia = str(noticia)
    print(noticia)

