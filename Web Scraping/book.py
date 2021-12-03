# GOAL: Get tittle of every book with a 2 star rating

import requests
import bs4

# https://books.toscrape.com/catalogue/page-1.html

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'html.parser')

product = soup.select('.product_pod')

example = product[0]
example.select('.star-rating.Three')

print(example.select('a')[1])
print(example.select('a')[1]['title'])

two_star_titles = []

for i in range(1, 51):
    scrape_url = base_url.format(i)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    books = soup.select('.product_pod')

    for book in books:
        # if 'star-rating Two' in str(book):
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
