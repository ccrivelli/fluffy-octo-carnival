import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.coinspot.com.au/buy/xmr')
r.status_code


soup = BeautifulSoup(r.content, "html.parser")

h1_all = soup.find_all('h1')
for element in h1_all:
	if element.string[0:5] == "1 XMR":
		#print(element)
    	#print(element.get('style'))
		print(element.string)
    	