#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json
import sys
import time
import os
import datetime
from PyWorkflowGen import WorkflowXML
myResult = WorkflowXML()

try:
    mtime = time.localtime(os.stat(".kbcache").st_mtime)
    modifyTime = datetime.datetime(year=mtime[0], month=mtime[1],
                                   day=mtime[2], hour=mtime[3],
                                   minute=mtime[4], second=mtime[5])
    nowTime = datetime.datetime.now()
    if (nowTime - modifyTime).days >= 1:
        os.system("rm .kbcache")
except Exception, e:
    pass

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

if config.has_key('card') != True:
    myResult.addItem(title=u"未设置一卡通号！", subtitle=u"请使用seuset命令设置",
                     icon=u"img/seu-error.png")
    print myResult.toPrettyString().encode('utf-8')
    sys.exit()

if len(config['card']['number']) != 9:
    myResult.addItem(title=u"一卡通号有误！", subtitle=u"请使用seuset命令重新设置",
                     icon=u"img/seu-error.png")
    print myResult.toPrettyString().encode('utf-8')
    sys.exit()

arg = ''

if len(sys.argv) >= 2:
    arg = sys.argv[1]

if arg == '':
    myResult.addItem(itemValid=u"no",
                     autocomplete=u" 0",
                     title=u"今天有啥课？",
                     subtitle=u"按回车查看"
                     )
    myResult.addItem(itemValid=u"no",
                     autocomplete=u" 1",
                     title=u"明天有啥课？",
                     subtitle=u"按回车查看"
                     )
    myResult.addItem(itemValid=u"no",
                     autocomplete=u" 2",
                     title=u"后天有啥课？",
                     subtitle=u"按回车查看"
                     )

else:

    try:
        kbcacheFile = open('.kbcache', 'r')
        kbStr = kbcacheFile.read()
    except Exception, e:
        kbStr = urllib2.urlopen("http://herald.seu.edu.cn/ws/curriculum/%s" %
                                config['card']['number']).read()
        kbcacheFile = open('.kbcache', 'w')
        kbcacheFile.write(kbStr)

    s_unicode = kbStr.decode('utf-8')
    information = json.loads(s_unicode)
    today = datetime.date.today()
    somedayslater = today + datetime.timedelta(days=int(arg))
    day = somedayslater.weekday()
    todayInfo = information[day]
    for course in todayInfo['courses']:
        myResult.addItem(itemValid=u"no",
                         title=course['name'],
                         subtitle=u"%s   %s" % (
                             course['time'], course['location'])
                         )
    if len(todayInfo['courses']) == 0:
        myResult.addItem(itemValid=u"no",
                         title=u"这天没有课！"
                         )
print myResult.toPrettyString().encode('utf-8')
