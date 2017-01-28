# -*- coding:utf-8 -*-
# ZeroDivisionError	NameError 	TypeError
while True:
	try:
		#x = int(input('Please enter a number'))
		pass
		break
	except ValueError:
		print '0ops! That was no valid number. Try again'

# instance.args
# __str__()
try:
	raise Exception('spam','eggs')
except Exception as inst:
	print type(inst)
	print inst.args
	print inst
class MyError(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)
try:
	raise MyError(2*2)
except MyError as e:
	print("My exception occured, value:",e.value)
# try...except...else...finally...
#pass
with open('file.txt') as f:
	for line in f:
		print line
























