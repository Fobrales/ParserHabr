from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
	search = 'парсер'
	html = urlopen("https://habr.com/ru/search/?q=" + search.encode('utf-8').decode('ascii') + "&target_type=posts&order=relevance")
	bs = BeautifulSoup(html, "html.parser")
except HTTPError as e:
	print("The server returned an HTTP error")
except URLError as e:
	print("The server could not be found!")
else:
	nameList = bs.findAll('a', {'class': 'tm-article-snippet__title-link'})

for name in nameList:
	print(name.get_text())