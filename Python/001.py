# -*- coding: UTF-8 -*-
# python as calculator
print 2+2,50-5*6,50/4,50//4,20%3
print 4**3
print "I am a string..."
print "\"yes!\",he said"
print '"yes!",he said'
s = 'First line.\nSecond line.'
print s
print (r"use a \n to get into the next line")
print('''\
	Uasge: thingy [OPTITONS]
	-h				Display this usage message
	-H Hostname	 	Hostname to connect to 
	  ''')
print('''\
	abcdefg\
	hijklmn\
	opqrstu
	uvwxyz\

		''')
print( 3 * "abc ")
for i in range(0,10):
    print s[i]

for i in range(1,10):
	print s[-i]
s += "\nThird line.\nForth line."
print s[5:10]
print s[:6]+s[6:]
print s[:]
f = "abcdefg"
print f[:6]
print f[:7]
print f[2:-2]
print f[-5:5]
print f[5:0]
#f[0] = 'h'
print 'h'+f[1:]
print len(f)
print s.format()
























