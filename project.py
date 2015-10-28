# -*- coding: utf-8 -*-

import web
import json
import time
import codecs
urls = (
    '/chart1', 'chart1',
    '/chart2', 'chart2',
    '/chart3', 'chart3',
    '/chart4', 'chart4',
    '/', 'index',
    '/chart1_query', 'chart1_query',
    '/chart2_query', 'chart2_query',
    '/chart3_query', 'chart3_query',
    '/chart4_query', 'chart4_query'
)
render = web.template.render("templates", base="base")


class chart1:
    def GET(self):
       return render.chart1()

class chart2:
    def GET(self):
       return render.chart2()
	   
class chart3:
    def GET(self):
       return render.chart3()

class chart4:
    def GET(self):
       return render.chart4()

class chart1_query:
    def GET(self):
      # inp = web.input()
      veri=findtopten()
      return json.dumps(veri)
	   
class chart2_query:
    def GET(self):
      # inp = web.input()
      veri=findbest()
      print json.dumps(veri)
      return json.dumps(veri)

class chart3_query:
    def GET(self):
      # inp = web.input()
      veri=dep()
      print json.dumps(veri)
      return json.dumps(veri)

class chart4_query:
    def GET(self):
      # inp = web.input()
      veri=iller()
      return json.dumps(veri)

with open("sektorler.json") as json_file:
    json_data = json.load(json_file)
def siralama(json_data):
    try:        
        return float(json_data["count"])
    except KeyError:
        return 0	
def findtopten():
	data={'sektor':'','count':''}
	obj=[]
	for i in json_data:
		data={'name':i['sektor'].encode('utf8'),'y':float(i['count'])}
		obj.append(data)
	return obj

def findbest():
	json_data.sort(key=siralama,reverse=True)																		  #
	data={'sektor':'','count':''}
	obj=[]
	for i in json_data[0:10]:
		data={'isim':i['sektor'].encode('utf8'),'y':float(i['count'])}
		obj.append(data)
	return obj
#print findbest()

with open("departmanlar.json") as json_file:
    json_data1 = json.load(json_file)

def dep():
	data={'departman':'','count':''}
	obj=[]
	for i in json_data1:
		data={'name':i['departman'].encode('utf8'),'y':float(i['count'])}
		obj.append(data)
	return obj

with open("iller.json") as json_file:
    json_data2 = json.load(json_file)
def siralama(json_data2):
    try:        
        return float(json_data2["count"])
    except KeyError:
        return 0	
def iller():
	data={'il':'','count':''}
	obj=[]
	for i in json_data2:
		data={'name':i['il'].encode('utf8'),'y':float(i['count'])}
		obj.append(data)
	return obj
	
class index:
    def GET(self):
       return render.index()

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("127.0.0.1", 1239))
