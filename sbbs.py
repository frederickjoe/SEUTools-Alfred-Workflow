#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2, json
import sys
from xml.sax.saxutils import escape
reload(sys)
sys.setdefaultencoding("utf-8")
s=urllib2.urlopen("http://bbs.seu.edu.cn/api/hot/topten.js").read().encode("utf-8")
information=json.loads(s)
print "<?xml version='1.0'?><items>"
for topic in information["topics"]:
    print "<item>",
    print "<title>%s</title>" % escape(topic["title"]),
    subt =  "版面:%s  作者:%s  回复:%d  点击:%d" % (topic["board"],topic["author"],topic["replies"],topic["read"])
    print "<subtitle>%s</subtitle>" % subt,
    print "<icon>img/sbbs.png</icon>",
    print "<arg>http://bbs.seu.edu.cn/bbscon.php?board=%s&amp;id=%s</arg>" %(topic["board"],topic["id"]),
    print "</item>",
print "</items>"

