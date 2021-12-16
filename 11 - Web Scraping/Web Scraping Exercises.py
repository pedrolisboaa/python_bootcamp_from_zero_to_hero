import requests
import bs4

res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# print(soup)

# Nome dos autores
atores = soup.select('.author')
nome_atores = set()
for a in atores:
    nome_atores.add(a.text)
print(nome_atores)

# Lista de citações
citacoes = soup.select('.text')
todas_citacoes = []
for c in citacoes:
    todas_citacoes.append(c.text)

print(todas_citacoes)


# Pegandos as tags
tag = soup.select('.tag-item')
tag_list = []
for t in tag:
    tag_list.append(t.text)

print(tag_list)


url = 'https://quotes.toscrape.com/page/{}/'
all_atores = []
for i in range(1, 11):
    scrape_url = url.format(i)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    ator = soup.select('.author')

    for a in ator:
        all_atores.append(a.text)

print(all_atores)