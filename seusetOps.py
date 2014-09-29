# -*- coding: utf-8 -*-

#this implements the settings, incl. writing config, login etc.


import json
import urllib
import urllib2
import sys
import os
from xml.sax.saxutils import escape

#reload(sys)
#sys.setdefaultencoding("utf-8")
try:
    configFile = open('.config', 'r')
    configStr = configFile.read().decode('utf-8')
    config = json.loads(configStr)
    configFile.close()
except Exception, e:
    failMsg = u"未初始化！请使用seuinit初始化"
    print failMsg.encode('utf-8')
    sys.exit()

arg = ''

if len(sys.argv) >= 2:
    arg = sys.argv[1]

if arg == '':
    # do nothing
    pass

elif arg.startswith("bu:"):
    username = arg[4:]
    config['sbbs']['username'] = username

elif arg.startswith("bp:"):
    password = arg[4:]
    #config['sbbs']['password'] = password

# the other settings #
elif arg.startswith("card:"):
    cardNumber = arg[6:]
#


# get the token for sbbs
if arg.startswith("bp:"):
    s = urllib2.urlopen(
        "http://bbs.seu.edu.cn/api/token.json?user=%s&pass=%s" %
        (config['sbbs']['username'].encode('utf-8'), password)).read().decode("utf-8")
    information = json.loads(s)
    if information['success'] == True:
        sucMsg = u"%s登录SBBS成功！" % information['name']
        print sucMsg.encode('utf-8')
        config['sbbs']['token'] = information['token']

    else:
        failMsg = u"登录SBBS失败！"
        print failMsg.encode('utf-8')
        config['sbbs']['token'] = ''

if arg.startswith("card:"):
    card = {'number': cardNumber}
    config['card'] = card
    os.system("rm .kbcache")
    sucMsg = u"设置一卡通号成功！"
    print sucMsg.encode('utf-8')

configStr = json.dumps(config)
configFile = open('.config', 'w')
configFile.write(configStr)
configFile.close()
