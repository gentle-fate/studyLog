# -*-  coding:UTF-8 -*-
import sys
#func
def ask_ok(prompt,retries = 4,complaint = 'Yes or no,please!'):
	while True:
		ok = input(prompt)
		if ok in('y','ye','yes'):
			return True
		if ok in('n','no','nop','nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise OSError('uncooperative user')
		print complaint
#ask_ok("ok or no?")
i = 5
def f(arg = i):
	global i
	print(arg)
	i += 10
	print i
i = 10
f()
print i
#??????
#pass
def f2(a,L = []):
	L.append(a)
	return L
print(f2(1))
print(f2(2))
print(f2(3))
#!!!!!!!

















