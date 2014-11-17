from collections import deque
import sys

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

def parse_line(line):
        line = line.rstrip("\n")
        values = line[1:len(line)-1].split(",")
        return Building(float(values[0]),float(values[1]),float(values[2]))

def parse_file(file):
        Ed = deque()
        for line in file:
             Ed.append(parse_line(line))

        return Ed

def show_skyline(skyline):
        i = len(skyline)
        for line in skyline:
                print line.lx,",",line.h, 
                i-=1
                if (i != 0):
                        print ",",

def main(argv):
        file_path = ""
        if len(argv) < 2:
                file_path="skyline.dat"

        try:
                file = open(file_path)
        except:
                return -1

        Ed = parse_file(file)

        sk = Skyline(Ed,0,len(Ed)-1)

        show_skyline(sk)

main(sys.argv)	
