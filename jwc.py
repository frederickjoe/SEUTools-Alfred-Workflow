#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2, json
import sys,re
reload(sys)
sys.setdefaultencoding("utf-8")
s=urllib2.urlopen("http://jwc.seu.edu.cn").read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(s)
i=1
print "<?xml version='1.0'?><items>"
news=soup.table.find_all(class_='font1')[12]
soup2 = BeautifulSoup(str(news))
for new in soup2.table.find_all('table'):
    soup3 = BeautifulSoup(str(new))
    print "<item><title>%s</title><subtitle>%s</subtitle><arg>%s</arg></item>" % (soup3.a.string, soup3.div.string,"http://jwc.seu.edu.cn%s" % soup3.a.get("href"))
print "</items>"
