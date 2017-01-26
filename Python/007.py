# -*- coding:UTF-8 -*-
import sys
#keyword parameters
def parrot(voltage,state='a stiff',action='voom',type='Norwegain Blue'):
	print "--This parrot wouldn't",action,
	print 'if you put',voltage,'volts through it.'
	print '--Lovely plumage,the',type
	print '--It\'s',state,'!'
parrot(1000)
parrot(voltage = 1000)
parrot(voltage=100000,action='VOOOOOOM')
parrot(action = 'VOOOOOM',voltage=10000000)
parrot('a million','bereft of life','jump')
parrot('a thousand',state='pushing up the daisies')
# keyword parameters must be put after real paremeters!!!!
# pass
def cheeseshop(kind,*arguments,**keywords):
	print '--Do you have any',kind,'?'
	print "--I'm sorry,we're all out of",kind
	for arg in arguments:
		print arg
	print '-'*20
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw,':',keywords[kw]
		
cheeseshop("Limburger","It's very runny,sir.",
		   "It's really very,VERY runny,sir.",
		   shopkeeper="Michael Palin",
		   client='John Cleese',
		   sketch='Cheese Shop Sketch'
)
# **name must be put after *name
# **name pre a dictionary;*name pre a tuple
























