# -*- coding:UTF-8 -*-
#list introduction
list = [1,2,3]
x = "x"
list.append(x)
print list
# equal: list[len(list):] = [x]
L = [4,5,6]
list.extend(L)
print list
# equal: list[len(list):] = L
i = 5
list.insert(i,x)
list.remove(2)
print list
#
list.pop()
list.pop(4)
print list
#pass

#list.clear()

# equal: del list[:]
list = range(1,20)
print list
print(list.count(3))
list.sort()
list.reverse()
print list
#a = list.copy()
i = 100
j = i
j += 100
a = list
a[3:] = []
print list
print i
print j
list = range(1,20)
list.reverse()
print list
print(list.index(5))



















