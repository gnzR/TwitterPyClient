## Simple Python Twitter Client
## gnzR 09.29.16

#!/usr/bin/env python
# coding: utf8
import sys
import os
import subprocess
from twython import Twython

#Insert your user data here
apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
apiSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

print ('Was hast du vor?')
print ('1 = Text posten')
print ('2 = CPU Temparatur posten')
print ('3 = Uptime posten')
print ('4 = CPU Temp und Uptime posten')

i= int(input())

if i == 1:
	txt1 = str(raw_input('Gib den Text ein: '))
	api.update_status(status=' '+txt1+' ')

if i == 2:
	execfile('temp.py')

if i == 3:
	execfile('uptime.py')

if i == 4:
	execfile('uptime.py')
	execfile('temp.py')

print ('Fertig!')
