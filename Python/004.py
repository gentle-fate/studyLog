# -*- coding:UTF-8 -*-
word = ['cat','window','defenestrate']
for w in word:
	print w,len(w)

#from _future_ import print_function
print "Hello,",
print('world')
import sys
sys.stdout.write('Hello,')
sys.stdout.write('world!')
print
print word
sys.stdout.write("word")
print
sys.stdout.write(w)
#sys.stdout.write(word)
print
for w in word[:]:
	if len(w)>6:
		word.insert(0,w)
print word
#range() function
for i in range(6):
	print i,
print
for i in range(3,8):
	print i,
print
for i in range(0,20,2):
	print i,
print
for i in range(len(word)):
	print i,word[i]
#enumerate()
print(range(10))
#???? = why the answer online is range(0,10)
list(range(10))
#???? = why the answer online is [0,1,2,3,4,5]
#pass
list(range(1,10))

for n in range(2,10):
	for x in range(2,n):
		if  n%x == 0:
			print n,'equals',x,'*',n//x
			break
	else:
		print n,'is a prime number'
#!!! = for...else...,when not break,execute else...
class MyEmptyClass:
	pass

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

















































