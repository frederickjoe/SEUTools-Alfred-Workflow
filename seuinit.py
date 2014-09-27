# -*- coding: utf-8 -*-

import json

sbbsConfig = {}
config = {}

########## SBBS settings ##########

sbbsConfig["username"] = "your_username"
sbbsConfig["token"] = ""
config["sbbs"] = sbbsConfig

###################################

######### the other settings ######


###################################


configStr = json.dumps(config)
configFile = open(".config", "w")
configFile.write(configStr)
configFile.close()

print ("初始化已完成！")