import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.coinspot.com.au/buy/xmr')
r.status_code


soup = BeautifulSoup(r.content, "html.parser")

h1_all = soup.find_all('h1')
for element in h1_all:
    print(element)
    print(element.string)

     