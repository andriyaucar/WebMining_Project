# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests

from bs4 import BeautifulSoup
import json

# <codecell>

r4=requests.get("http://www.kariyer.net/website/isara/index.aspx?&keyword=yaz%C4%B1l%C4%B1m")
item4=BeautifulSoup(r4.text)

list1=item4.find("div",id="divAramaSonuclari").findAll("div")

link=[]
for i in list1:
    try:
       link.append(i.find("div",class_="ilanustorta").find("a",class_="pozlink genLink").get("href"))
    except:
        pass

link=list(set(link))

# <codecell>

url1=link[0]
url2=link[1]
url3=link[2]
url4=link[3]
url5=link[4]
url6=link[5]
url7=link[6]
url8=link[7]
url9=link[8]
url10=link[9]
url11=link[10]

# <codecell>

an=[]
for i in link:
    r1=requests.get("http://www.kariyer.net/"+i)
    item1=BeautifulSoup(r1.text)
    an.append(item1)
    

# <codecell>


#listeler=item1.find("div",id="dvheader").find("div",id="dvHeaderTable").find("table",id="tblIlanDetay").find("div",id="divIlanDetay").find("div",id="divIlanDetay")

# <codecell>

#a=listeler.find("div",class_="CandidateInfo").find("div",class_="candidateContent")

# <codecell>

data={'Experience':''}
datajson=[]
for i in an:
    try:
      data={'Experience': i.find("div",id="divIlanDetay").find("div",class_="CandidateInfo").find("div",class_="candidateContent").find("div",class_="leftBlock").text}
    except:
        pass
    datajson.append(data)
    
with open('experience.json', 'w') as outfile:
    json.dump(datajson, outfile)

# <codecell>

data1={'Job':''}
datajson1=[]
for i in an:
    try:
      data1={'Job': i.find("div",class_="headerCenter").find("div",class_="fontbig").text}
    except:
        pass
    datajson1.append(data1)

# <codecell>

data2={'Company':''}
datajson2=[]
for i in an:
    try:
      data2={'Company': i.find("div",class_="headerCenter").find("div",class_="fontbig").find("a",class_="link").text}
    except:
        pass
    datajson2.append(data2)

