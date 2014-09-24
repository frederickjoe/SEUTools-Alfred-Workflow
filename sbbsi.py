#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2, json
import sys, time
from xml.sax.saxutils import escape
reload(sys)
sys.setdefaultencoding("utf-8")

#read config
configFile = open('.config','r')
configStr = configFile.read()
config = json.loads(configStr)
configFile.close()

if config['sbbs']['token']=='':
    print """
    <?xml version='1.0'?><items>
    <item><title>未登录！</title><subtitle>请使用seuset命令登录</subtitle><icon>img/sbbs-error.png</icon></item>
    </items>
    """
    sys.exit()

print "<?xml version='1.0'?><items>"


s=urllib2.urlopen("http://bbs.seu.edu.cn/api/notifications.json?token=%s" % config['sbbs']['token']).read().encode("utf-8")
information=json.loads(s)

if information['success'] != True:
    print "<item><title>获取信息失败！</title><subtitle>请使用seuset命令重新登录</subtitle><icon>img/sbbs-error.png</icon></item>"

else:
    if information.has_key("mails"):
        print "<item><title>站内信</title><subtitle>%d 封未读</subtitle><icon>img/sbbs-mail.png</icon><arg>http://bbs.seu.edu.cn/bbsmailbox.php</arg></item>" % len(information["mails"]),
        for mail in information["mails"]:
            print "<item>",
            print "<title>  %s</title>" % escape(mail["title"]),
            subt =  "  作者: %s" % (mail["sender"])
            print "<subtitle>%s</subtitle>" % subt,
            print "<icon>img/sbbs-mail.png</icon>",
            print "<arg>http://bbs.seu.edu.cn/bbsmailcon.php?dir=.DIR&amp;num=%d</arg>" %(mail["id"]),
            print "</item>",
    else:
        print "<item><title>没有未读站内信</title><subtitle></subtitle><icon>img/sbbs-mail.png</icon><arg>http://bbs.seu.edu.cn/bbsmailbox.php</arg></item>",
    if information.has_key("replies"):
        print "<item><title>回复</title><subtitle>%d 未读</subtitle><icon>img/sbbs-reply.png</icon><arg></arg></item>" % len(information["replies"]),
        for reply in information["replies"]:
            print "<item>",
            print "<title>  %s</title>" % escape(reply["title"]),
            subt =  "  作者: %s" % (reply["user"])
            print "<subtitle>%s</subtitle>" % subt,
            print "<icon>img/sbbs-reply.png</icon>",
            print "<arg>http://bbs.seu.edu.cn/bbscon.php?board=%s&amp;id=%s</arg>" %(reply["board"],reply["id"]),
            print "</item>",
    else:
        print "<item><title>没有未读回复</title><subtitle></subtitle><icon>img/sbbs-reply.png</icon></item>",

    if information.has_key("replies"):
        print "<item><title>提到我的</title><subtitle>%d 未读</subtitle><icon>img/sbbs-at.png</icon><arg></arg></item>" % len(information["ats"]),
        for at in information["ats"]:
            print "<item>",
            print "<title>  %s</title>" % escape(at["title"]),
            subt =  "  作者: %s" % (at["user"])
            print "<subtitle>%s</subtitle>" % subt,
            print "<icon>img/sbbs-at.png</icon>",
            print "<arg>http://bbs.seu.edu.cn/bbscon.php?board=%s&amp;id=%s</arg>" %(at["board"],at["id"]),
            print "</item>",
    else:
        print "<item><title>没有未读@</title><subtitle></subtitle><icon>img/sbbs-at.png</icon></item>",
print "</items>"

