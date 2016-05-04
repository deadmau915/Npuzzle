# animate.py

from graphics import *
from board import Board
from stack import Stack
import time

class Animate(object):
	
	class _picture(object):
		
		def __init__(self, rectngl, txt):
			self.rectngl = rectngl
			self.txt = txt
			self.txt.setStyle('bold italic')
			self.txt.setTextColor('#000000')
			self.rectngl.setFill('#2A5DC5')
					
		def getCentralPoint(self):
			return self.txt.getAnchor()
			
		def getNmbr(self):
			return self.txt.getText()
			
		def exhibit(self, win):
			if self.txt.getText() != 0:
				self.rectngl.draw(win)
				self.txt.draw(win)
				
		def mvZero(self, point):
			dx = point.getX()-self.getCentralPoint().getX()
			dy = point.getY()-self.getCentralPoint().getY()
			self.rectngl.move(dx, dy)
			self.txt.move(dx, dy)
				
		def mv(self, point):
			dx = point.getX()-self.getCentralPoint().getX()
			dy = point.getY()-self.getCentralPoint().getY()
			
			seconds = 0.01
			if dx == 0:
				if dy >= 0:
					for i in range(int(abs(dy))):
						self.rectngl.move(0, 1)
						self.txt.move(0, 1)
						time.sleep(seconds)
				else:
					for i in range(int(abs(dy))):
						self.rectngl.move(0, -1)
						self.txt.move(0, -1)
						time.sleep(seconds)
			else:
				if dx >= 0:
					for i in range(int(abs(dx))):
						self.rectngl.move(1, 0)
						self.txt.move(1, 0)
						time.sleep(seconds)
				else:
					for i in range(int(abs(dx))):
						self.rectngl.move(-1, 0)
						self.txt.move(-1, 0)
						time.sleep(seconds)

	def __init__(self, brd):
		self.brd = brd
		self.lst = []
		
		for f in range(self.brd.size()):
			for c in range(self.brd.size()):
				
				point1 = Point((f+1)*100,(c+1)*100)
				point2 = Point(point1.getX()+100,point1.getY()+100)
				R = Rectangle(point1,point2)
				
				nmbr = self.brd.tileAt(c,f)
				anchorpnt = R.getCenter()
				T = Text(anchorpnt, nmbr)
				
				self.lst.append(self._picture(R,T))
				
	def getLst(self):
		return self.lst
		
	def fndEmptyCell(self):
		for f in range(self.brd.size()):
			for c in range(self.brd.size()):
				if self.brd.tileAt(f,c)==0:
					return [f, c]
		return [-1, -1]
	
	def animation(self, board):
		
		lstLen = len(self.lst)
		site = self.fndEmptyCell()
		numtoMove = board.tileAt(site[0], site[1])
		self.brd = board
		
		for i in range(lstLen):
			if self.lst[i].getNmbr() == 0:
				Pfinal = self.lst[i].getCentralPoint()
			elif self.lst[i].getNmbr() == numtoMove:
				Pinitial = self.lst[i].getCentralPoint()
				
		for i in range(lstLen):
			if self.lst[i].getNmbr() == 0:
				self.lst[i].mvZero(Pinitial)
			elif self.lst[i].getNmbr() == numtoMove:
				self.lst[i].mv(Pfinal)
