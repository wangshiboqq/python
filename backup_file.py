#!/usr/bin/python
#FileName:backup_file.py 

import os
import time
import sys 

OK=0
ERR=-1

# 1. backup script usage 
def print_help():
	print "Usage: %s target_directory source_files" %sys.argv[0]
	sys.exit(ERR)
	
if __name__ == '__main__':
	if len(sys.argv) < 3:
		print_help()
# 2. The backup must be stored in a main backup directory.
	#target_dir='/root/backup/'
	
	target_dir=sys.argv[1]
	print 'current target directory',target_dir
	
# 3. The files and directories to be backed up are specified in a list. 
	#source=['/root/data/a','/root/data/b','/root/data/c','/root/data/d']
	
	source=sys.argv[2:] 
	print 'current source list',source

# 4. The files are backed up into a zip file.
# 5. The current day is the name of the subdirectory in the main directory 
	today=target_dir+time.strftime('%Y:%m:%d')
	
# The current time is the name of the zip archive 
	now=time.strftime('%H:%M:%S')
	
# Take a comment from the user to create the name of the zip file 
	comment=raw_input('Enter a comment -->')
	
	if len(comment)==0:
		target=today+os.sep+now+'.zip'
	else:
		target=today+os.sep+now+'_'+comment.replace(' ', '_')+'.zip'
						
# Create the subdirectory if it isn't already there
	if not os.path.exists(today):
		os.mkdir(today)
		print 'Successfully created directory',today 
# 6. We use the tar command (in Unix/Linux) to put the files in a zip archive  

	zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup 
	if os.system(zip_command)==0:
		print 'Successful backup to',target 
		sys.exit(OK) 
	else:
		print 'Bckup FAILED'
