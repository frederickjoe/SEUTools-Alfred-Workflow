# -*- coding: utf-8 -*-

import json
import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from PyWorkflowGen import WorkflowXML
myResult = WorkflowXML()

if os.path.isfile('.config') != True:
    myResult.addItem(title="未初始化！",
                     subtitle="请使用seuinit进行初始化",
                     icon="img/seu-error.png")
    print myResult.toPrettyString()
    sys.exit()

arg = ''

if len(sys.argv) >= 2:
    arg = sys.argv[1]

if arg == '':

    myResult.addItem(itemValid="no",
                     autocomplete="bu: ",
                     title="设置SBBS用户名",
                     subtitle="按Tab键继续",
                     icon="img/sbbs-settings.png")
    myResult.addItem(itemValid="no",
                     autocomplete="bp: ",
                     title="设置SBBS密码",
                     subtitle="按Tab键继续",
                     icon="img/sbbs-settings.png")

    # add some new item as new settings ######

    #

elif arg.startswith("bu:"):  # set up sbbs username
    username = arg[4:]

    myResult.addItem(title="设置SBBS用户名:%s" % username,
                     subtitle="按回车确认",
                     arg=arg,
                     icon="img/sbbs-settings.png")


elif arg.startswith("bp:"):  # set up sbbs password
    password = arg[4:]

    myResult.addItem(title="设置SBBS密码:%s" % ('●' * len(password)),
                     subtitle="按回车确认",
                     arg=arg,
                     icon="img/sbbs-settings.png")

# the other settings ##########

#


print myResult.toPrettyString()
