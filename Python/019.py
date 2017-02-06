# -*- coding : utf-8 -*-
import os
print os.getcwd() # return the current working directoty
# os.chdir('/server/accesslogs')
# os.system('mkdir today')
#print dir(os)
#print help(os)
#
import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')
import glob
print glob.glob('*.py')
import sys
print sys.argv
# sys.exit()
sys.stderr.write("Warning, log file not found starting a new one\n")
import re
print re.findall(r'\bf[a-z]', 'which foot or hand fell fastest')
print re.sub(r'(\b[a-z]+) \1', r'1', 'cat in the hat')
import math
print math.cos(math.pi/4.0)
print math.log(1024, 2)
import random
print random.random()
#pass
#from urllib.request import urlopen
#for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/time.pl'):
#	line = line.decode('utf-8')
#	if 'EST' in line or 'EDT' in line:
#		print line

#import smtplib
#server = smtplib.SMTP('localhost')
#server.sendmail('soothsayer@example.org', 'jcaesar@example.org', '''
#	To: jcaesar@example.org
#	Fro,: soothsayer@example.org
	
#	Beware the Ides of Marth.
#	'''
#)
#server.quit()

































