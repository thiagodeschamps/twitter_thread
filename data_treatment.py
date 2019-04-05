from bs4 import BeautifulSoup as bs

def treatment():
    with open('source_code.txt', 'r') as f:
        data = f.read()

    cont = bs(data, 'lxml')

    dias = []

    first_content = cont.find('p', class_ = 'TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text')

    dias.append(first_content)

    contents = cont.findAll('p', class_ = 'TweetTextSize js-tweet-text tweet-text')

    dias.extend(contents)

    index = dias[0].text.find("F")

    lista = []

    lista.append(dias[0].text[21:])

    for i in dias[1:]:
       lista.append(i.text[31:])

    start = lista[1].find(':')
    end = lista[1].find('\n')

    '''
    - Flexões
    - Abdominais
    - Mergulhos
    - Agachamentos
    - Prancha
    '''
    flex = []
    abdo = []
    merg = []
    agac = []
    prancha = []

    for i in lista:
        flex.append(int(i[start+1:end].strip()))

    start = lista[1].find(':', start+1)
    end = lista[1].find('\n', end+1)

    for i in lista:
        abdo.append(int(i[start+1:end].strip()))

    start = lista[1].find(':', start+1)
    end = lista[1].find('\n', end+1)

    for i in lista:
        merg.append(int(i[start+1:end].strip()))

    start = lista[1].find(':', start+1)
    end = lista[1].find('\n', end+1)

    for i in lista:
        agac.append(int(i[start+1:end+1].strip()))

    start = lista[1].find(':', start+1)
    end = lista[1].find('\n', end+1)

    for i in lista:
        res = str(i[start+2:].strip())
        prancha.append(int(res[:-1]))

    return flex, abdo, merg, agac, prancha
