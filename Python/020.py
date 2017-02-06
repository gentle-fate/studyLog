# -*- coding:utf-8 -*-
from datetime import date
now = date.today()
print now
print now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B")
birthday = date(1996, 10, 5)
age = now - birthday
print age.days
#pass
# zlib,	gzip,	bz2, lzma,	zipfile	 tarfile
import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print t
print len(t)
z = zlib.decompress(t)
print z
zlib.crc32(s)
#pass
from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print Timer('a,b = b,a', 'a=1; b=2').timeit()
#pass
def average(values):
	"""Computer the arithmetic mean of a list of numbers.
	>>>print(average([20,30,70])
	40.0
	"""
	return sum(values)/len(values) 
import doctest
#doctest.testmod()
#????
import unittest
class TestStaticalFunctions(unittest.TestCase):
	def test_average(self):
		self.assertEqual(average([20, 30, 70]), 40.0)
		self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
		with self.assertRaises(ZeroDivisionError):
			average([])
		with self.assertRaises(TypeError):
			average(20, 30, 70)
unittest.main()	
#pass
# xmlrpc.client		xmlrpc.server
# email;	smtplib;	poplib;
# xml.dom	xml.sax		csv
# gettext	locale		codecs
		
		
		
		
		
		

























