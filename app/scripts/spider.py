import scrapy
from scrapy.http import TextResponse
import requests
import re


def organizarTexto(link = ' '):
    try:
        #requisição da página
        url = str(link)
        response_html = requests.get(url).text
        response = TextResponse(url=url, body=response_html, encoding='utf-8')

        if not response.css('div.glb-grid'):
               return '❗Não foi possível extrair o texto desse link, porfavor copie todos os titulos, subtitulos e textos da notícia e copie na caixa acima'
            
        for p in response.css('div.glb-grid'):
                item = {
                    'title': p.css('h1::text').get(),
                    'subtitle': p.css('h2::text').get(),
                    'text': p.css('p::text').getall(),
                }

        noticia = str(str(item['title']) + str(item['subtitle']) + str(item['text']))

        # remove pontuação, colchetes, listas, etc...
        noticia = re.sub(r"[\[\],\.\:\;\!\?\“\”\"\'\(\)]", " ", noticia)

        noticia = re.sub(r'\s+', ' ', noticia)

        return noticia.strip()
    except Exception as e:
        print(f"[ERRO ao extrair texto da URL]: {e}")
        return '❗Ocorreu um erro ao tentar acessar o link. Verifique se ele está correto.'

# organizarTexto('https://g1.globo.com/mundo/noticia/2025/06/12/perda-de-sustentacao-problema-nos-motores-calculo-de-peso-as-hipoteses-para-a-queda-do-aviao-da-air-india.ghtml')