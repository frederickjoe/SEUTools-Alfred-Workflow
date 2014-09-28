# -*- coding: utf-8 -*-

#this implements the settings, incl. writing config, login etc.


import json
import urllib
import urllib2
import sys
from xml.sax.saxutils import escape

reload(sys)
sys.setdefaultencoding("utf-8")
try:
    configFile = open('.config', 'r')
    configStr = configFile.read()
    config = json.loads(configStr)
    configFile.close()
except Exception, e:
    print "未初始化！请使用seuinit初始化"
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

#


# get the token for sbbs
if arg.startswith("bp:"):
    s = urllib2.urlopen(
        "http://bbs.seu.edu.cn/api/token.json?user=%s&pass=%s" %
        (config['sbbs']['username'], password)).read().encode("utf-8")
    information = json.loads(s)
    if information['success'] == True:
        print "%s登录SBBS成功！" % information['name']
        config['sbbs']['token'] = information['token']

    else:
        print "登录SBBS失败！"
        config['sbbs']['token'] = ''

configStr = json.dumps(config)
configFile = open('.config', 'w')
configFile.write(configStr)
configFile.close()
