# -*- coding:utf-8 -*-
class MyClass:
	'''A simple example class'''
	i = 123456
	def f(self):
		return 'hello world'
	def __init__(self):
		self.data = []
		
class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart
x = MyClass()
y = Complex(3.0, -4.5)
print y.r,y.i
class Dog:
	kind = 'canine'
	def __init__(self, name):
		self.name = name
d = Dog("fido")
e = Dog('buddy')
print d.kind,d.name
print e.kind,e.name
print d.__class__
#name mangling （命名编码）
class Mapping:
	def __init__(self, interable):
		self.items_list = []
		self.__update(iterable)
	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)
	__update = update
class MappingSubclass(Mapping):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)

#exec()		eval()		getattr()	
#setattr()		delattr()
# m.__self__		m.__func__
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

























