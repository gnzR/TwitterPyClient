#gnzR
#!/usr/bin/env python
# coding: utf8
import sys
import os
from twython import Twython

#Hier musst du deine Daten einfuegen!
apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
apiSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

cmd = 'uptime'
line = os.popen(cmd).readline().strip()
laufzeit = line
api.update_status(status='Uptime Info: '+laufzeit+' ')
