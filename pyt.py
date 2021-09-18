from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.parse import quote
import json

count = 3;
#задать количество страниц.
data = [];
#массив для хранения данных

for i in range(count):
	page = i+1
	try:
		search = 'парсер'
		html = urlopen("https://habr.com/ru/search/page" + str(page) + "/?q=" + quote(search) + "&target_type=posts&order=relevance")
		bs = BeautifulSoup(html, "html.parser")
	except HTTPError as e:
		print("The server returned an HTTP error")
	except URLError as e:
		print("The server could not be found!")
	else:
		articleList = bs.findAll('div', {'class': ['tm-article-snippet']})	
	for art in articleList:
		header = art.find('a', {'class': 'tm-article-snippet__title-link'})
		anno = art.find('div', {'class': 'article-formatted-body'})
		annoText = anno.get_text()
		url = header['href']
		author = art.find('a', {'class': 'tm-user-info__username'})
		authorName = author.get_text().replace("\n", "").strip();
		title = header.get_text()
		data.append({
			'title': title,
			'author': authorName,
			'url': "https://habr.com" + url,
			'anno': annoText
		})
	print("Parsing " + str(page) + " page...");

with open('data.json', 'w') as outfile:
	try:
		json.dump(data, outfile, ensure_ascii=False)
	except:
		print("Parsing error on page " + str(page))