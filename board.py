# board.py

from copy  import deepcopy

class Board(object):

	def __init__(self, blocks):
		self.blocks = deepcopy(blocks)

	def tileAt(self, i, j):
		return self.blocks[i][j]

	def size(self):
		return len(self.blocks)

	def hamming(self):
		hamming = 0
		for i in range(self.size()):
			for j in range(self.size()):
				if self.blocks[i][j] == 0: continue
				if self.blocks[i][j] != (self.size() * i + j + 1):
					hamming += 1
		return hamming

	def manhattan(self):
		manhattan = 0
		for i in range(self.size()):
			for j in range(self.size()):
				if self.blocks[i][j] == 0: continue
				row = (self.blocks[i][j] - 1) / self.size()
				col = (self.blocks[i][j] - 1) % self.size()
				manhattan += abs(row - i) + abs(col - j)
		return manhattan

	def goal(self):
		return self.manhattan() == 0

	def isSolvable(self):
		if hasattr(self, 'solvable'): return self.solvable
		b = [x for row in self.blocks for x in row]; N = len(b)
		s = 0
		for i in range(N - 1):
			if b[i] == 0: continue
			for j in range(i + 1, N):
				if b[j] == 0: continue
				if b[i] > b[j]: s += 1
		if self.size() % 2 != 0:
			self.solvable = s % 2 == 0
		else:
			row = 0
			col = 0
			while self.blocks[row][col] != 0:
				col += 1
				if col == self.size():
					col  = 0
					row += 1
			s += row
			self.solvable = s % 2 != 0
		return self.solvable

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __ne__(self, other):
		return not self.__eq__(other)

	def neighbors(self):
		row, col = 0, 0
		while self.blocks[row][col] != 0:
			col += 1
			if col == self.size():
				row += 1
				col  = 0

		neighbors = list()
		if self.valid(row-1,col):
			b = Board(deepcopy(self.blocks))
			b.exch(row-1,col,row,col)
			neighbors.append(b)
		if self.valid(row,col+1):
			b = Board(deepcopy(self.blocks))
			b.exch(row,col+1,row,col)
			neighbors.append(b)
		if self.valid(row+1,col):
			b = Board(deepcopy(self.blocks))
			b.exch(row+1,col,row,col)
			neighbors.append(b)
		if self.valid(row,col-1):
			b = Board(deepcopy(self.blocks))
			b.exch(row,col-1,row,col)
			neighbors.append(b)
		return neighbors

	def valid(self, row, col):
		if row < 0 or row > self.size() - 1: return False
		if col < 0 or col > self.size() - 1: return False
		return True

	def exch(self, frow, fcol, trow, tcol):
		tmp = self.blocks[frow][fcol]
		self.blocks[frow][fcol] = self.blocks[trow][tcol]
		self.blocks[trow][tcol] = tmp

	def twin(self):
		twin = deepcopy(self.blocks)
		for i in range(2):
			if twin[i][0] != 0 and twin[i][1] != 0:
				twin[i][0], twin[i][1] = twin[i][1], twin[i][0]
				break
		return Board(twin)

	def __str__(self):
		out = '%2r\n' % self.size()
		for i in range(self.size()):
			for j in range(self.size()):				
				out += ' %2r' % self.blocks[i][j] if self.blocks[i][j] != 0 else '   ' 
			out += '\n'
		return out

if __name__ == '__main__':

	# 8  1  3        1  2  3     1  2  3  4  5  6  7  8    1  2  3  4  5  6  7  8
    # 4     2        4  5  6     ----------------------    ----------------------
    # 7  6  5        7  8        1  1  0  0  1  1  0  1    1  2  0  0  2  2  0  3

    # initial          goal         Hamming = 5 + 0          Manhattan = 10 + 0

	#x = [[7,0,2],[8,5,3],[6,4,1]]
	#x = [[1,2,3],[4,5,6],[8,7,0]]
	#x = [[1,2,3],[4,0,6],[8,5,7]]
	#x = [[0,1,3],[4,2,5],[7,8,6]]
	#x = [[8,1,3],[4,0,2],[7,6,5]]
	#x = [[6,0,5],[8,7,4],[3,2,1]]
	x = [[1,2,3,4],[6,10,7,8],[5,0,11,12],[9,13,14,15]]
	b = Board(x)

	print b
	print "Hamming = %r" % b.hamming()
	print "Manhattan = %r" % b.manhattan()

	print "solvable = %r\n" % b.isSolvable()

	for x in b.neighbors():
		print x
		print "Hamming = %r" % x.hamming()
		print "Manhattan = %r" % x.manhattan()
