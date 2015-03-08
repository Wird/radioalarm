#!/usr/bin/env python
drbaseurl = 'http://dr.dk'
import urllib2
import json
from bs4 import BeautifulSoup

html_doc = urllib2.urlopen(drbaseurl+"/p3/p3-nyheder").read()
soup = BeautifulSoup(html_doc)
drp3nyhedersensteurl = soup.find('div', class_="section mute-heading boxed episode-information").find('a').get('href')
html_doc2 = urllib2.urlopen(drbaseurl+drp3nyhedersensteurl).read()
soup2 = BeautifulSoup(html_doc2)
drp3nyhedersenstexmlurl = soup2.find('div', class_="dr-widget-audio-player").get('data-resource')
json_doc = urllib2.urlopen(drp3nyhedersenstexmlurl).read()
data = json.loads(json_doc)
print data['Data'][0]['Assets'][0]['Links'][1]['Uri']
