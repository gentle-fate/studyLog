# -*- coding : UTF-8 -*-
stack = [2,3,4,5]
stack.append(6)
stack.append(7)
print stack
stack.pop()
print stack
stack.pop(2)
print stack
#pass
from collections import deque
queue = deque(["eric","john","michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
print queue
print(queue.popleft())
#
squares = []
for x in range(10):
	squares.append(x**2)
print squares
#squares = list(map(lambda x : x**2,range(10))
#print squares
squares = [x**2 for x in range(10)]
print squares
print [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
#pass
matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
]
print matrix
print [[row[i] for row in matrix] for i in range(4)]




















