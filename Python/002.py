# -*- coding:UTF-8 -*-
sq = [1,4,9,16,25,36]
print sq
print sq[0]
print sq[-2]
print sq[:3]
sq += [49,64,81,100]
print sq
print len(sq)
sq[0] = 0
print sq
sq[:3] = [1,2,3]
print sq
sq.append(121)
print sq
sd = sq
print sd
sd[1:] = []
print sd
print sq
ss = ['a','b','c','d']
sd = ss +[]
sd[1:] = []
print sd
print ss
sq.append(ss)
print sq
#
a,b = 0,1
while b<10:
	print b
	a,b = b,a+b
	
i = 2
if i:
	print 'i != 0'
j = []
if j:
	print 'j is not empty'
else:
	print 'j is empty'
	
i = 256*256
str = 'The value of i is'
print('The value of i is',i)
end = ','
while b<1000:
	print b,end
	a,b = b,a+b











