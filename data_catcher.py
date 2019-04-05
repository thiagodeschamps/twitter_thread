from bs4 import BeautifulSoup as bs
import requests

def catcher():
    url = 'https://twitter.com/thiagoreisd/status/1111905031425536000'

    r = requests.get(url).text

    cont = bs(r, 'lxml')

    with open('source_code.txt', 'w') as f:
        f.write(cont.prettify())
