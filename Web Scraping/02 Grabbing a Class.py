import requests
import bs4

result = requests.get('https://pt.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(result.text, 'html.parser')


for item in soup.select('.toctext'):
    print(item.text)

