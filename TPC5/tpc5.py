from bs4 import BeautifulSoup
import requests
import re
import json
import string

url = "https://www.atlasdasaude.pt/doencasAaZ/"
url2= "https://www.atlasdasaude.pt"


def extrair_paginas(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    div_doencas = soup.find_all("div", class_="views-row")

    res= {}
    for div in div_doencas:
        designacao = div.div.h3.a.text 
        samllDescricao= div.find("div", class_="views-field-body").div.text 

        linkFullDescricao= div.div.h3.a["href"]

        html2= requests.get(url2 + linkFullDescricao).text
        soup2= BeautifulSoup(html2, "html.parser")

        fullDescricao= soup2.find("div", class_="field-name-body").text

        res[designacao]={"smallDescricao":samllDescricao.strip(), "fullDescricao":fullDescricao.strip()}

    return res


res ={}
for letra in string.ascii_lowercase:
    res = res | extrair_paginas(url +letra)


f_out= open("doencasCompleto.json", "w", encoding="UTF-8")
json.dump(res, f_out, indent=4, ensure_ascii= False)
f_out.close()
