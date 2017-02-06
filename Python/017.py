# -*- coding:utf-8 -*-
# raise Class
# raise Instance
class A(Exception):
	pass
class B(A):
	pass
class C(B):
	pass
for cls in [A,B,C]:
	try:
		raise cls()
	except C:
		print 'C'
	except B:
		print 'B'
	except A:
		print 'A'
s = 'abc'
it = iter(s)
print it
print(next(it))
print(next(it))
print(next(it))
#print(next(it))
class Reverse:
	'''Iterator for looping over a sequence backwards.'''
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def __next__(self):
		if self.index == 0:
			raise StopIeration
		self.index = self.index -1
		return self.data[self.index]
rev = Reverse("spam")
print iter(rev)
#for char in rev:
#	print(char)
#???????
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


























