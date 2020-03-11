'''Import package urlopen dan BeautifulSoup'''
import requests
import json
import os
import datetime
from bs4 import BeautifulSoup

'''Inisialisasi'''
berita = {}
all = []

'''Request ke website'''
page = requests.get("https://www.republika.co.id/")

'''Extract konten menjadi objek BeautifulSoup'''
obj = BeautifulSoup(page.text, 'html.parser')

'''Mulai mengambil data dari web'''
for headline in obj.find_all('div', class_='teaser_conten1'):
    berita["kategori"] = json.dumps(headline.find('h1').text)
    berita["judul"] = json.dumps(headline.find('h2').text)
    date = datetime.datetime.now()
    berita["date"] = date.strftime("%A")+", "+date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")
    berita["time"] = json.dumps(headline.find('div', class_='date').text)
    #tmp = str(berita)
    #tmp = tmp.replace("\'", "\"")
    #print(berita)
    all.append(dict(berita))
    lucu = all
    print(berita)
    with open('beritaterkini.json', 'w') as file:
    	json.dump(lucu, file, indent=4)