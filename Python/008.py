# -*- coding : UTF-8 -*-
def write_multiple_items(file,separator,*args):
	file.write(separator.join(args))

def concat(sep='/',*args):
	return sep.join(args)
concat("earth","mars","venus")
#concat("earth","mars","venus",sep='.')
#pass
list(range(3,6))
args = [3,6]
list(range(*args))
#
def parrot(voltage,state = 'a stiff',action='voom'):
	print "--This parrot would't",action,
	print "if you put",voltage,"volts through it.",
	print "E's",state,"!"
d = {"voltage":"four million","state":"bleedin' demised","action":"VOOM"}
parrot(d)
#lambda
def make_incrementor(n):
	return lambda x:x+n
f = make_incrementor(42)
print(f(0))
print(f(1))
#???!!!!
def my_function():
	'''Do nothing,but document it.
	
	No,really, it does\'t do anything.
	'''
	pass
print(my_function.__doc__)
#
#def f2(ham:42,eggs:int='spam') -> "Nothing to see here":
def f2(ham,eggs='spam'):
	print("Annotations:",f2.__annnotations__)
	print("Arguments:",ham,eggs)
f2("wonderful")




































