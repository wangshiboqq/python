#!/usr/bin/python
#FileName:backup_ver1.py 

import os
import time

source=['/root/data/a','/root/data/b','/root/data/c','/root/data/d']

target_dir='/root/backup/'

today=target_dir+time.strftime('%Y%m%d')

now=time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today

target=today+os.sep+now+'.zip'


zip_command="zip -qr '%s' %s" %(target,' '.join(source))

if os.system(zip_command)==0:
     print 'Successful backup to',target 
else:
     print 'Bckup FAILED'



