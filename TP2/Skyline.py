from collections import deque

class Line:
	"""Una linea contiene un punto de inicio y una altura (el punto final la da la linea siguiente)"""
	
	def __init__(self, lx, h):
		self.lx = lx
		self.h = h

class Building:
	"""Un edificio tiene un xinicial, un xfinal y una altura"""
	
	def __init__(self, lx, h, rx):
		self.lx = lx
		self.h = h
		self.rx = rx

def Skyline(Ed, min, max):
	"""Ed es una lista de edificios, ordenados por lx creciente
		min y max son el primero y el ultimo que reviso"""
	if (min == max):
		sk = deque()
		sk.append(Line(Ed[min].lx,Ed[min].h))
		sk.append(Line(Ed[min].rx,0))
		return sk
	mid = (max+min)/2
	sk1 = Skyline(Ed, min, mid)
	sk2 = Skyline(Ed, mid + 1, max)
	return Merge(sk1,sk2)

def Merge(sk1, sk2):
	sk = deque()
	H1now = 0
	H2now = 0
	MaxH = 0
	LastH = -1
	Xnow = 0
	while (len(sk1) > 0) and (len(sk2) > 0):
		if (sk1[0].lx < sk2[0].lx):
			Xnow = sk1[0].lx
			H1now = sk1[0].h
			MaxH = H1now
			if (H2now > MaxH):
				MaxH = H2now
			if (LastH != MaxH):
				sk.append(Line(Xnow, MaxH))
				LastH = MaxH
			sk1.popleft()
		else:
			Xnow = sk2[0].lx
			H2now = sk2[0].h
			MaxH = H2now
			if (H1now > MaxH):
				MaxH = H1now
			if (LastH != MaxH):
				sk.append(Line(Xnow, MaxH))
				LastH = MaxH
			sk2.popleft()

	while len(sk1)> 0:
		line = sk1.popleft()
		sk.append(line)
	while len(sk2) > 0:
		line = sk2.popleft()
		sk.append(line)
	
	return sk

def Main():
	b1 = Building(0,4,5)
	b2 = Building(1,7,4)
	b3 = Building(3,6,8)
	b4 = Building(6,10,10)
	b5 = Building(7,8,12)
	b6 = Building(9,11,11)
	Ed = deque()
	Ed.append(b2)
	Ed.append(b4)
	Ed.append(b3)
	Ed.append(b6)
	Ed.append(b5)
	Ed.append(b1)
	sk = Skyline(Ed,0,5)
	print len(sk)
	for l in sk:
		print(l.lx,l.h)

Main()
	