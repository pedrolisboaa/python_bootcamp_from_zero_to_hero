import requests
import bs4

res = requests.get('https://pt.wikipedia.org/wiki/C%C3%A3o')
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# buscando imagens
img_dogs = soup.select('img')

# pegandoo somente o src e adicionando http:
all_img = []
for i in img_dogs:
    if not i['src'][1] == 's':
        all_img.append(f"http:{i['src']}")


# Baixando as imagens
c = 0
for i in all_img:
    image_link = requests.get(all_img[c])
    print(all_img[c])
    f = open(f'{str(c)}.jpg', 'wb')
    f.write(image_link.content)
    f.close()
    c += 1

print('fiiiim')

