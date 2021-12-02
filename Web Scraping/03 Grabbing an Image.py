import requests
import bs4

response = requests.get('https://pt.wikipedia.org/wiki/Xadrez')
soup = bs4.BeautifulSoup(response.text, 'html.parser')

#print(soup.select('.thumbimage'))

xadrez = soup.select('.thumbimage')[0]
print(xadrez['src'])

image_link = requests.get('http:' + xadrez['src'])
# print(image_link.content)

f = open('ima_xadrex.jpg', 'wb')
f.write(image_link.content)
f.close()