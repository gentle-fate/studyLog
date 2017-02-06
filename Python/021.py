# -*- coding : utf-8 -*-
#import reprlib
#reprlib.repr(set('supercalifragilisticex;=plidocious'))
import pprint
t = [[[['black', 'cyan'],'white', ['green', 'red']],[['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width = 40))
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1251')
conv = locale.localeconv()
x = 1234567.8
print locale.format("%d", x, grouping = True)
#print locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'],x)grouping = True)
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print t.substitute(village='Nottingham', cause='the ditch fund')
d = dict(village='Nottingham')
print t.safe_substitute(d)
# import time, os.path
# import struct
import threading, zipfile
class AsyncZip(threading.Thread):
	def __init__(self, infile, outfile):
		threading.Thread.__init__(self)
		self.infile = infile
		self.outfile = outfile
	def run(self):
		f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
		f.write(self.infile)
		f.close()
		print('Finished background zip of:', self.infile)
# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
print('The main program continues to run in foreground.')
# background.join()
print('Main program waited until background was done.')
#	queue
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')












