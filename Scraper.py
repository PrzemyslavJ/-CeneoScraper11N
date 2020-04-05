import requests
from bs4 import BeautifulSoup

#pobieranie kodu pojedyńczej strony z opiniami o produkcie
url = "http://ceneo.pl/85910996#tab=reviews"
respons = request.get(url)
page_dom = BeautifulSoup(respons.text,'html.parser')

#wydobycie z kodu strony fragmentów odpowiadających opiniom konsumentów
opinions = page.dom.select("li.js_product-review")

opinion = opinions.pop(0)
#dla pojedyńczej opinii wydobycie jej składowych
opinion_id = opinion(["data-entry-id"])
author = opinion.select("div.reviewer-name-line").pop().text
try:
    recomendation = opinion.select("div.product-review-summary").pop().text
except IndexError:
    recomendation = None
stars = opinion.select("div.product-review-summary").pop().text
content = opinion.select("p.product-review-body").pop().text
try:
    cons = opinion.select().pop().text
except IndexError:
    cons = None
try:
    pros = opinion.select("div.pros-cell>ul").pop().text
except IndexError:
    pros = None
useful = opinion.select(" button.vote-yes > span").pop().text
useless = opinion.select("button.vote-no > span").pop().text
opinion_date = opinion.select("span review-time > time:first-child").pop()["datetime"].text
try:
    purchase_date = opinion.select("pan review-time > time:nth-child(2)").pop()["datetime"].text
except IndexError:
    purchase_date = None

print(opinion_id,author,recommendation,stars,content)