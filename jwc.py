#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys
import re
from PyWorkflowGen import WorkflowXML

#reload(sys)
#sys.setdefaultencoding("utf-8")

myResult = WorkflowXML()

s = urllib2.urlopen("http://jwc.seu.edu.cn").read()
s_unicode = s.decode('utf-8')
from bs4 import BeautifulSoup
soup = BeautifulSoup(s)

news = soup.table.find_all(class_='font1')[12]
soup2 = BeautifulSoup(str(news))
for new in soup2.table.find_all('table'):
    soup3 = BeautifulSoup(str(new))
    myResult.addItem(title=unicode(soup3.a.string),
                     subtitle=unicode(soup3.div.string),
                     arg=u"http://jwc.seu.edu.cn%s" % soup3.a.get("href"))
print myResult.toPrettyString().encode('utf-8')
