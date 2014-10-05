def swap(lista,posA,posB):
	(lista[posA],lista[posB])=(lista[posB],lista[posA])
	
class Heap(object):
	def __init__(self):
		self.lista=[]
		self.cantidad=0
	
	def esta_vacio(self):
		return self.cantidad==0
	
	def encolar (self,objeto):
		try:
			self.lista.append(objeto)
			posicion = len(self.lista)-1
			padre = (posicion-1)/2
			while (posicion > 0 and self.lista[posicion] < self.lista[padre]):
				swap(self.lista,padre,posicion)
				posicion = padre
				padre = (posicion-1)/2
			self.cantidad+=1
		except:
			print "No son elementos comparables"
			raise TypeError
			
	def borramin (self):
		try:
			min = self.lista[0]
		except:
			print "El heap esta vacio"
			raise ValueError
		self.cantidad-=1
		ultimo=self.lista.pop( self.cantidad )
		if (self.cantidad <= 0):
			return min
		self.lista[0]=ultimo
		
		posicion=0
		hijoI = (posicion*2)+1
		hijoD = (posicion*2)+2
		while (True): #cicla hasta que se llega al punto de control
			if (hijoI >= self.cantidad): #si no hay hijo izquierdo no tiene hijos
				break;
			elif (hijoD >= self.cantidad): #si no hay hijo derecho hay que controlar el izquierdo
										   #en cualquier caso no hay mas hijos
				if (self.lista[hijoI] < self.lista[posicion]):
					swap(self.lista,posicion,hijoI)
				break
			else:
				if (self.lista[posicion] > self.lista [hijoD] and self.lista[hijoD] < self.lista [hijoI]):
					swap(self.lista,posicion,hijoD)
					posicion=hijoD
				elif (self.lista[posicion] > self.lista [hijoI]):
					swap(self.lista,posicion,hijoI)
					posicion=hijoI
				else:
					break
			hijoI = (posicion*2)+1
			hijoD = (posicion*2)+2
		return min