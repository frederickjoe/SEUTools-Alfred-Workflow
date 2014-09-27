#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys
import time

from PyWorkflowGen import WorkflowXML
myResult = WorkflowXML()
reload(sys)
sys.setdefaultencoding("utf-8")
# read config
try:
    configFile = open('.config', 'r')
    configStr = configFile.read()
    config = json.loads(configStr)
    configFile.close()
except Exception, e:
    myResult.addItem(title="未初始化！", subtitle="请使用seuinit命令初始化",
                     icon="img/seu-error.png")
    print myResult.toPrettyString()
    sys.exit()

if config['sbbs']['token'] == '':
    myResult.addItem(title="未登录！", subtitle="请使用seuset命令登录",
                     icon="img/seu-error.png")
    print myResult.toPrettyString()
    sys.exit()

s = urllib2.urlopen("http://bbs.seu.edu.cn/api/notifications.json?token=%s" %
                    config['sbbs']['token']).read().encode("utf-8")
information = json.loads(s)

if information['success'] != True:
    myResult.addItem(title="获取信息失败！",
                     subtitle="请使用seuset命令重新登录",
                     icon="img/sbbs-error.png")
else:
    if information.has_key("mails"):
        myResult.addItem(title="站内信",
                         subtitle="%d 封未读" % len(information["mails"]),
                         icon="img/sbbs-mail.png",
                         arg="http://bbs.seu.edu.cn/bbsmailbox.php")

        for mail in information["mails"]:
            myResult.addItem(title=" %s" % mail["title"],
                             subtitle="  作者: %s" % (mail["sender"]),
                             icon="img/sbbs-mail.png",
                             arg="http://bbs.seu.edu.cn/bbsmailcon.php?dir=.DIR&num=%d" 
                             % mail["id"])
    else:
        myResult.addItem(title="没有未读的站内信",
                         icon="img/sbbs-mail.png",
                         arg="http://bbs.seu.edu.cn/bbsmailbox.php")

    if information.has_key("replies"):
        myResult.addItem(title="回复",
                         subtitle="%d 未读" % len(information["replies"]),
                         icon="img/sbbs-reply.png")
        for reply in information["replies"]:
            myResult.addItem(title=" %s" % reply["title"],
                             subtitle="  作者: %s" % reply["user"],
                             icon="img/sbbs-reply.png",
                             arg="http://bbs.seu.edu.cn/bbscon.php?board=%s&id=%s"
                             % (reply["board"], reply["id"]))
    else:
        myResult.addItem(title="没有未读的回复",
                         itemValid="no",
                         icon="img/sbbs-reply.png")

    if information.has_key("ats"):
        myResult.addItem(title="提到我的",
                         subtitle="%d 未读" % len(information["ats"]),
                         icon="img/sbbs-at.png")
        for at in information["ats"]:
            myResult.addItem(title=" %s" % at["title"],
                             subtitle="  作者: %s" % at["user"],
                             icon="img/sbbs-at.png",
                             arg="http://bbs.seu.edu.cn/bbscon.php?board=%s&id=%s"
                             % (at["board"], at["id"]))
    else:
        myResult.addItem(title="没有未读的@",
                         itemValid="no",
                         icon="img/sbbs-at.png")

print myResult.toPrettyString()
