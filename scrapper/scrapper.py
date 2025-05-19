import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://nilc-fakenews.herokuapp.com/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')