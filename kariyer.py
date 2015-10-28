
import requests

from bs4 import BeautifulSoup
import json



url="http://www.kariyer.net/"

rmainpage=requests.get(url)
mainpage=BeautifulSoup(rmainpage.text)

joblist=mainpage.find("section",class_="job-list").findAll("div",class_="box")

listelink=[]
for i in joblist:
    listelink.append(i.findAll("a",class_="all"))

listelink=listelink[3:6]

listelink

linkler=[]
for link in listelink:
    linkler.append(link[0].get("href"))



linkler

url1=linkler[0]
url2=linkler[1]
url3=linkler[2]



url1

r1=requests.get(url1)
item1=BeautifulSoup(r1.text)

partlar=item1.find("table",id="dlSektorler").findAll("td")[1:]


data={'sektor':'','count':''}
datajson=[]
for i in partlar:
    data={'sektor': i.find("div").find("a").text.strip(),'count':i.find("div").find("a").find("span").text.strip()}
    datajson.append(data)

with open('sektorler.json', 'w') as outfile:
    json.dump(datajson, outfile)



r2=requests.get(url2)
item2=BeautifulSoup(r2.text)

item2.title

partlar2=item2.find("table",id="dlIsAlanlari").findAll("td")[1:]

data={'departman':'','count':''}
datajson=[]
for i in partlar2:
    data={'departman': i.find("div").find("a").text.strip(),'count':i.find("div").find("a").find("span").text.strip()}
    datajson.append(data)

with open('departmanlar.json', 'w') as outfile:
    json.dump(datajson, outfile)

r3=requests.get(url3)
item3=BeautifulSoup(r3.text)



partlar3=item3.find("table",id="dlSehirler").findAll("td")[1:]

data={'il':'','count':''}
datajson=[]
for i in partlar3:
    #print i.find("div").find("span").text.strip()
    #print i.find("div").text.strip()
    data={'il': i.find("div").find("a").text.strip(),'count':i.find("div").find("a").find("span").text.strip()}
    datajson.append(data)
    #data={'il':i.find("div").text.strip(),'count':i.find("div").find("span").text.strip()}

with open('iller.json', 'w') as outfile:
    json.dump(datajson, outfile)

r4=requests.get("http://www.kariyer.net/website/isara/index.aspx?&keyword=yaz%C4%B1l%C4%B1m")
item4=BeautifulSoup(r4.text)

listeler=item4.find("div",id="divAramaSonuclari").findAll("div")

linkler=[]
for i in listeler:
    try:
       linkler.append(i.find("div",class_="ilanustorta").find("a",class_="pozlink genLink").get("href"))
    except:
        pass

linkler=list(set(linkler))

listepage2=item4.find("div",id="divAramaSonuclari").findAll("div",sayfano="2")


    





linkler[1]

tur=['yazılım','android','web','database','java','network']



tur



bilgiler=[]
linkler=[]
for i in tur:
    r4=requests.get("http://www.kariyer.net/website/isara/index.aspx?&keyword="+i)
    item4=BeautifulSoup(r4.text)
    listeler=item4.find("div",id="divAramaSonuclari").findAll("div")
    
    for j in listeler:
        try:
           linkler.append(j.find("div",class_="ilanustorta").find("a",class_="pozlink genLink").get("href"))
           linkler.append(i)
           bilgiler.append(linkler)
           print linkler
        except:
            pass
    








len(bilgiler)





bilgiler













for i in bilgiler:
    
    r5=requests.get("http://www.kariyer.net"+i[0])
    item5=BeautifulSoup(r5.text)
    try:
        tur=i[1]
        sirket=item5.find("a",id="emp3763").text
        
    except:
        pass
    print tur
    print sirket
    























































linkler=list(set(linkler))

(linkler)

























linkler




























































































































































