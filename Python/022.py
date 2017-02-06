# -*- coding:utf-8 -*-
import weakref, gc
class A:
	def __init__(self, value):
		self.value = value
	def __repr__(self):
		return str(self.value)
a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print d['primary']
del a
print gc.collect()
# pass
from array import array
a = array('H', [4000, 10, 700, 2222])
print sum(a)
print a[1:3]
from collections import deque
d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print 'Handling',d.popleft()
import bisect
from heapq import heapify, heappop, heappush
from decimal import *
print round(Decimal('0.70') * Decimal('1.05'), 2)
print round(.70 * 1.05, 2)
print 1.00 % 0.10
print Decimal('1.00') % Decimal('.10')
getcontext().prec = 36
print Decimal(1) / Decimal(7)
print sum([Decimal('0.1')]*10) == Decimal('1.0')
print sum([0.1]*10) == 1.0
print 0.1*10 == 1.0
# ????!!!!!!!

































