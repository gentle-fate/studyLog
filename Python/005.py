# -*- coding:UTF-8 -*-
import sys
#define function
def fib(n):
	'''print a Fibonacci series up to n.'''#docstring
	a,b = 0,1
	while a<n:
		print a,
		a,b = b,a+b
		n -= 1
	print
m =2000
fib(m)
#global
#partcal namespace
print m
# m doesn't change!!!
# all ....values....
# ??? = rename jizhi
f = fib
f(200)
print f
print(f(200))
# in fact,this func return None!!,but it will not be output
#pass
def fib2(n): #return Fibonacci series up to n
	'''Return a list containing the Fibonacci series up to n.'''
	result = []
	a,b = 0,1
	while a<n:
		result.append(a)
		a,b = b,a+b
	return result
ff = fib2(2000)
print ff





























