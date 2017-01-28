# -*- coding : utf-8 -*-
s = "fd shjk vch jl k"
print s.format()
# repr() str()
print(str(34+89))
s1 = "hello,world!"
print str(s1)
print str(1.0/6)
#pass
for x in range(1,11):
	print repr(x).rjust(2),repr(x*x).rjust(3),
	print repr(x*x*x).rjust(4)
for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

# x.ljust(n)[:n]
# str.zfill()
print('{0} and {1}'.format('spam','eggs'))
print('this {food} is {adj}'.format(food = 'spam',adj = 'absolutely horrible'))
import math
print('this value of PI is approximately {!r}'.format(math.pi))
#pass
table = {'s':4127,'jack':4098,'dca':8934}
print('jack:{0[jack]:d} s:{0[s]:d}'.format(table))
#file stream
f = open('file.txt','r+')
# mode : 'r','w','a','r+','r','b'
print f.readline()
print f.read()
print f.read()
f = open('file.txt','r+')
for line in f:
	print line,
f = open('file.txt','a')
f.write('QianJing')
f = open('file.txt','r+')
print(f.readlines())
print f.tell()
# f.seek(offset,from_what)
# from_what is in [0,1,2]
f.close()
# JSON (JavaScript Object Notation)
json.dumps([1,'simple','list'])
#json.dump(x,f)
#x = json.load(f)
#pass
#pinke module









