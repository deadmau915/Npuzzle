# Implementacion de una Pila

import math

class Stack(object):

	class _Node(object):

		def __init__(self, item, next):
			self._item = item
			self._next = next

	def __init__(self):
		self._first = None
		self._N = 0

	def empty(self):
		return self._first is None

	def size(self):
		return self._N

	def push(self, item):
		self._first = self._Node(item, self._first)
		self._N += 1

	def pop(self):
		if self.empty(): raise Exception('Stack underflow')
		item = self._first._item
		self._first = self._first._next
		self._N -= 1
		return item

	def peek(self):
		if self.empty(): raise Exception('Stack underflow')
		return self._first._item

	def __str__(self):
		return ' '.join([str(item) for item in self])

	def __iter__(self):
		return self.ListIterator(self._first)

	class ListIterator(object):
		"""Iterator Starts at the first item."""

		def __init__(self, first):
			self._current = first # Node<Item>

		def __iter__(self):
			return self

		def next(self):
			"""Return Next item."""
			if self._current is None: raise StopIteration
			item = self._current._item
			self._current = self._current._next
			return item

# Implementacion de una Cola de Prioridad

class MinPQ(object):

	def __init__(self):
		self._pq = [0]
		self._N = 0

	def empty(self):
		return self._N == 0

	def size(self):
		return self._N

	def min(self):
		if self.empty(): raise IndexError('Priority queue underflow')
		return self._pq[1]

	def insert(self, x):
		self._N += 1
		self._pq.append(x)
		self._swim(self._N)
		assert self._isMinHeap()

	def delMin(self):
		self._exch(1, self._N)
		minkey = self._pq.pop()
		self._N -= 1
		self._sink(1)
		assert self._isMinHeap()
		return minkey

	def _swim(self, k):
		while (k > 1 and self._greater(k/2, k)):
			self._exch(k, k/2)
			k /= 2

	def _sink(self, k):
		while (2*k <= self._N):
			j = 2*k
			if j < self._N and self._greater(j, j+1): j += 1
			if not self._greater(k, j): break
			self._exch(k, j)
			k = j

	def _greater(self, i, j):
		return self._pq[i] > self._pq[j]

	def _exch(self, i, j):
		tmp = self._pq[i]
		self._pq[i] = self._pq[j]
		self._pq[j] = tmp

	def _isMinHeap(self, k = 1):
		if k > self._N: return True
		left, right = 2*k, 2*k + 1
		if left  < self._N and self._greater(k, left):  return False
		if right < self._N and self._greater(k, right): return False
		return self._isMinHeap(left) and self._isMinHeap(right)

	def __str__(self):
		return "".join(["N=%-2d pq[%d]=" % (self._N, len(self._pq)),  " ".join(map(str,self._pq))])
  
	def __repr__(self): 
		return __str__(self)

	def __len__(self):
		return len(self._pq)

	def draw(self): # TBD: Finish this
		# 0 1   2 3   4 5 6 7   8 9 ...
		#   S   P R   N H O A   E I ...
		#   1   2 2   3 3 3 3   4 4 ...
		for i,E in enumerate(self.pq):
			if i == 0 or E is None: continue
			level = int(math.log(i,2))
			print ''.join(['-']*(level+1)), E

if __name__ == '__main__':
	pass