# -*- coding:utf-8 -*-
import math
def reverse(data):
	for index in range(len(data)-1, -1, -1):
		yield data[index]
for char in reverse('golf'):
	print char
print sum(i*i for i in range(10))
xv = [10, 20, 30]
yv = [7, 5, 3]
page = ["fds", "fdslfj", "doiefn"]
print sum(x*y for x,y in zip(xv, yv))
table = {x: math.sin(x*math.pi/180) for x in range(0, 91)}
words = set(word for line in page for word in line.split())
#vale = max((student.gpa, student.name) for student in graduates)
data = 'golf'
print list(data[i] for i in range(len(data)-1, -1, -1))




























