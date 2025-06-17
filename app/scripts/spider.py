import scrapy
from scrapy.http import TextResponse
import requests
import re

class NewsSpider(scrapy.Spider):
    name = 'Noticias'

    def parse(self, response):
        for p in response.css('div.glb-grid'):
            item = {
                'title': p.css('h1.content-head__title::text').get(),
                'subtitle': p.css('h2.content-head__subtitle::text').get(),
                'text': p.css('p.content-text__container::text').getall(),
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

    noticia = str(item['title']) + str(item['subtitle']) + str(item['text'])
    noticia = str(noticia)

    # remove pontuação, colchetes, listas, etc...
    noticia_limpa = re.sub(r"[\[\],\.\:\;\!\?\“\”\"\'\(\)]", " ", noticia)

    noticia_limpa = re.sub(r'\s+', ' ', noticia_limpa)

    noticia = noticia_limpa

    # with open('noticia_extraida_limpa.txt', 'w', encoding='utf-8') as f:
    #     f.write(noticia.strip())

    return noticia

extrairTexto('https://g1.globo.com/mundo/noticia/2025/06/12/perda-de-sustentacao-problema-nos-motores-calculo-de-peso-as-hipoteses-para-a-queda-do-aviao-da-air-india.ghtml')