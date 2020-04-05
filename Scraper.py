import requests
from bs4 import BeautifulSoup
import pprint
import json

#pobieranie kodu pojedyńczej strony z opiniami o produkcie
url_prefix = "http://www.ceneo.pl"
url_postfix = "/85910996#tab=reviews"
url = "http://ceneo.pl/85910996#tab=reviews"
respons = requests.get(url)
page_dom = BeautifulSoup(respons.text,'html.parser')

#wydobycie z kodu strony fragmentów odpowiadających opiniom konsumentów
opinions = page_dom.select("li.js_product-review")

all_opinions = []

while url:
    # pobranie pojedyńczej strony z opiniami
    respons = requests.get(url)
    page_dom = BeautifulSoup(respons.text,'html.parser')
    #dla pojedyńczej opinii wydobycie jej składowych
    for opinion in opinions:
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

        features = {
            "opinion_id":opinion_id,
            "author":author,
            "recommendation":recomendation,
            "stars":stars,
            "content":content,
            "cons":cons,
            "pros":pros,
            "useful":useful,
            "useless":useless,
            "opinion_date":opinion_date,
            "purchase_date":purchase_date

        }
        all_opinions.append(features)
    try:
        url = url.prefix+page_dom.select("a.paigination_next").pop()["href"]
    except IndexError:
        url = None
    print(len(all_opinions))
    print(url)

with open('opinions.json','w',encoding="UTF-8") as fp:
    json.dump(all_opinions,fp,indent=4, ensure_ascii=False)

url = url.prefix+page_dom.select("a.paigination_next").pop()
pprint.pprint(features)