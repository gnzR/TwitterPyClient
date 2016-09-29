#!/usr/bin/env python
# coding: utf8
import sys
import os
from twython import Twython

#Hier musst du deine Daten einfügen!
apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
apiSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
api.update_status(status='My current CPU temperature is '+temp+' C')
