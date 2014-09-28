#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys
import time

from PyWorkflowGen import WorkflowXML
myResult = WorkflowXML()
#reload(sys)
#sys.setdefaultencoding("utf-8")
# read config
try:
    configFile = open('.config', 'r')
    configStr = configFile.read()
    config = json.loads(configStr)
    configFile.close()
except Exception, e:
    myResult.addItem(title=u"未初始化！", subtitle=u"请使用seuinit命令初始化",
                     icon=u"img/seu-error.png")
    print myResult.toPrettyString().encode('utf-8')
    sys.exit()

if config['sbbs']['token'] == '':
    myResult.addItem(title=u"未登录！", subtitle=u"请使用seuset命令登录",
                     icon=u"img/seu-error.png")
    print myResult.toPrettyString().encode('utf-8')
    sys.exit()

s = urllib2.urlopen("http://bbs.seu.edu.cn/api/notifications.json?token=%s" %
                    config['sbbs']['token']).read()
s_unicode = s.decode('utf-8')
information = json.loads(s_unicode)

if information['success'] != True:
    myResult.addItem(title=u"获取信息失败！",
                     subtitle=u"请使用seuset命令重新登录",
                     icon=u"img/sbbs-error.png")
else:
    if information.has_key('mails'):
        myResult.addItem(title=u"站内信",
                         subtitle=u"%d 封未读" % len(information['mails']),
                         icon=u"img/sbbs-mail.png",
                         arg=u"http://bbs.seu.edu.cn/bbsmailbox.php")

        for mail in information['mails']:
            myResult.addItem(title=u" %s" % mail['title'],
                             subtitle=u"  作者: %s" % (mail['sender']),
                             icon=u"img/sbbs-mail.png",
                             arg=u"http://bbs.seu.edu.cn/bbsmailcon.php?dir=.DIR&num=%d" 
                             % mail['id'])
    else:
        myResult.addItem(title=u"没有未读的站内信",
                         icon=u"img/sbbs-mail.png",
                         arg=u"http://bbs.seu.edu.cn/bbsmailbox.php")

    if information.has_key('replies'):
        myResult.addItem(title=u"回复",
                         subtitle=u"%d 未读" % len(information['replies']),
                         icon=u"img/sbbs-reply.png")
        for reply in information['replies']:
            myResult.addItem(title=u" %s" % reply['title'],
                             subtitle=u"  作者: %s" % reply['user'],
                             icon=u"img/sbbs-reply.png",
                             arg=u"http://bbs.seu.edu.cn/bbscon.php?board=%s&id=%s"
                             % (reply['board'], reply['id']))
    else:
        myResult.addItem(title=u"没有未读的回复",
                         itemValid=u"no",
                         icon=u"img/sbbs-reply.png")

    if information.has_key('ats'):
        myResult.addItem(title=u"提到我的",
                         subtitle=u"%d 未读" % len(information['ats']),
                         icon=u"img/sbbs-at.png")
        for at in information['ats']:
            myResult.addItem(title=u" %s" % at['title'],
                             subtitle=u"  作者: %s" % at['user'],
                             icon=u"img/sbbs-at.png",
                             arg=u"http://bbs.seu.edu.cn/bbscon.php?board=%s&id=%s"
                             % (at['board'], at['id']))
    else:
        myResult.addItem(title=u"没有未读的@",
                         itemValid=u"no",
                         icon=u"img/sbbs-at.png")

print myResult.toPrettyString().encode('utf-8')
