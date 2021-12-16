import requests
import bs4

result = requests.get('https://pt.wikipedia.org/wiki/Jonas_Salk')
soup = bs4.BeautifulSoup(result.text, 'lxml')

print(soup.select('p')[0].getText())

for p in soup.select('p'):
    print(p.getText())