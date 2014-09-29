# -*- coding: utf-8 -*-

# this defines the settings frontend

import json
import os
import sys
from PyWorkflowGen import WorkflowXML

#reload(sys)
#sys.setdefaultencoding("utf-8")

myResult = WorkflowXML()

if os.path.isfile('.config') != True:
    myResult.addItem(title=u"未初始化！",
                     subtitle=u"请使用seuinit进行初始化",
                     icon=u"img/seu-error.png")
    print myResult.toPrettyString().encode('utf-8')
    sys.exit()

arg = ''
if len(sys.argv) >= 2:
    arg = sys.argv[1]

arg = unicode(arg)
if arg == '':

    myResult.addItem(itemValid=u"no",
                     autocomplete=u"bu: ",
                     title=u"设置SBBS用户名",
                     subtitle=u"按Tab或回车键继续",
                     icon=u"img/sbbs-settings.png")
    myResult.addItem(itemValid=u"no",
                     autocomplete=u"bp: ",
                     title=u"设置SBBS密码",
                     subtitle=u"按Tab或回车键继续",
                     icon=u"img/sbbs-settings.png")
    myResult.addItem(itemValid=u"no",
                     autocomplete=u"card: ",
                     title=u"设置一卡通号",
                     subtitle=u"按Tab或回车键继续",
                     icon=u"img/settings.png")

    # add some new item as new settings #

    #

elif arg.startswith("bu:"):  # set up sbbs username
    username = arg[4:]
    myResult.addItem(title=u"设置SBBS用户名:%s" % username,
                     subtitle=u"按回车确认",
                     arg=arg,
                     icon=u"img/sbbs-settings.png")


elif arg.startswith("bp:"):  # set up sbbs password
    password = arg[4:]
    myResult.addItem(title=u"设置SBBS密码:%s" % (u'●' * len(password)),
                     subtitle=u"按回车确认",
                     arg=arg,
                     icon=u"img/sbbs-settings.png")

# the other settings #
elif arg.startswith("card:"):  # set up allinonecard number
    cardNumber = arg[6:]
    myResult.addItem(title=u"设置一卡通号码:%s" % cardNumber,
                     subtitle=u"按回车确认",
                     arg=arg,
                     icon=u"img/settings.png")
#


print myResult.toPrettyString().encode('utf-8')
