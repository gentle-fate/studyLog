# -*- coding : utf-8 -*-
#set
# : union; intersection; difference; sysymmetric deifference
s = set()
basket = {'apple','orange','pear','orange','banana'}
print basket
print('orange' in basket)
# Demonstrate set operations on unique letters from two words
a = set("dfjslfjgvdab")
print a
b = {x for x in "fdsjlafngvaf" if x not in 'abc'}
print b
#dictionary
#associative memories; associative arrays;
d = {"dfd":"dfd",'dfs':"gjbfl",8:"jgofdf"}
print list(d.keys())
print sorted(d.keys())
dic = dict([('space',1321),('dfjsd',435),('dbvje',688)])
print dic
#pass
k = {'gal':'the pure','rovin':'the brave'}
for k,v in k.items():
	print k,v
for i,v in enumerate(['tic','tac','toe']):
	print i,v
#
questions = ['name','quest','favorite color']	
answers = ['lamcelot','the holy grail','blue']
for q, a in zip(questions,answers):
	print('What is your {0}? It is {1}.'.format(q,a))
for i in reversed(range(1,10,2)):
	print i
for f in sorted(set(basket)):
	print f
#
basket = list(basket)
for w in basket[:]:
	if len(w) > 6:
		basket.insert(0,w)
print basket
#
string1,string2,string3 = '','tron','ham'
not_null = string1 or string2 or string3
print not_null





















