#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys
from PyWorkflowGen import WorkflowXML

reload(sys)
sys.setdefaultencoding("utf-8")

myResult = WorkflowXML()

s = urllib2.urlopen(
    "http://bbs.seu.edu.cn/api/hot/topten.js").read().encode("utf-8")
information = json.loads(s)

for topic in information["topics"]:

    subt = "版面:%s  作者:%s  回复:%d  点击:%d" % (
        topic["board"], topic["author"], topic["replies"], topic["read"])

    myResult.addItem(title=topic["title"],
                     subtitle=subt,
                     icon="img/sbbs.png",
                     arg="http://bbs.seu.edu.cn/bbscon.php?board=%s&id=%s"
                     % (topic["board"], topic["id"]))
print myResult.toPrettyString()
