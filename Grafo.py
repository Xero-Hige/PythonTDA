from heap import Heap
from conjuntos_dis import Conjuntos_dis

class _Vertice(object):
	"""Clase vertice que modela los vertices de un grafo"""
	
	def __init__(self,identificador):
		"""Crea una instancia de el tipo _Vertice"""
		self.id=identificador
		self.estado="BLANCO"
		self.vecinos=[]
		self.aristas={}
		
	def __cmp__(self,otro):
		"""Comparacion que indica una relacion de orden entre los indices
			de los vertices de un grafo"""
		if (self.id > otro.id):
			return 1
		elif(self.id < otro.id):
			return -1
		return 0
		
class _Arista(object):
	"""Clase arista que modela las uniones entre 2 vertices de un grafo
		opccionalmente en un digrafo el vert1 es el vertice saliente y
		el vert2 es el vertice entrante"""
		
	def __init__(self,vertice_sa,vertice_en,peso=False):
		self.vert1=vertice_sa
		self.vert2=vertice_en
		self.peso=peso

	def __ep__(self,otra):
		return self == otra
		
	def __cmp__(self,otra):
		"""Una arista es menor a otra cuando su peso es menor"""
		if (arista.peso > otra.peso):
			return 1
		elif(arista.peso < otra.peso):
			return -1
		return 0
		
	def __str__(self):
		return "("+str(self.vert1.id)+"--"+str(self.vert2.id)+") ("+str(self.peso)+")"
			
class Grafo(object):
	def __init__(self):
		self.l_vertices={}
		self.tamanio=0
	
	def agregar_vertice(self,id):
		ver=_Vertice(id)
		self.l_vertices[id]=ver
	
	def agregar_arista(self,ver_A,ver_B,peso=False):
		"""Pre: ver_A y ver_B son vertices que existen en el grafo"""
		arista=_Arista(ver_A,ver_B,peso)
		if (ver_A.aristas.has_key(ver_B.id)):
			aristas=ver_A.aristas.get(ver_B.id) #Guardo la arista en la lista de aristas de A a B
			aristas.append(arista)
			aristas=ver_B.aristas.get(ver_A.id) #Guardo la arista en la lista de aristas de B a A
			aristas.append(arista)
		else:
			ver_A.aristas[ver_B.id]=[arista]
			ver_B.aristas[ver_A.id]=[arista]
			
	def arbol_tendido_minimo_K(self):
		arbol_tendido=grafo()
		heap_aristas=heap()
		bosque=Conjuntos_dis()
		for vertice in self.l_vertices:
			arbol_tendido.agregar_vertice(vertice.id)
			bosque.agregar(vertice.id)
			for arista in vertice.aristas:
				heap_aristas.encolar(arista)
		while (not heap.esta_vacio()):
			arista=heap_aristas.borramin()
			conjunto_A=bosque.pertenece_a(str(arista.vert1.id))
			conjunto_B=bosque.pertenece_a(str(arista.vert2.id))
			if (conjunto_A!=conjunto_B):
				bosque.unir_conjuntos(conjunto_A,conjunto_B)
				arbol_tendido.agregar_arista(arista.vert1,arista.vert2,arista.peso)
		return arbol_tendido
		
	def grafo_inicializar(self):
		for vertices in self.l_vertices:
			vertices.estado="BLANCO"
	
	def obtener_vertice(self,identificador):
		try:
			return self.l_vertices[identificador]
		except:
			print "No existe el vertice"
			raise ValueError
	
	def existe(self,id_vertice):
		return self.l_vertices.has_key(id_vertice)
		
	def mostrar_grafo(self):
		"""Funcion que imprime todas las aristas presentes en el grafo"""
		for v in self.l_vertices: #v es el id de cada vertice
			vertice=self.l_vertices[v] #se recupera el objeto vertice asociado al id
			for vecino in vertice.aristas: #para los vecinos en la lista de aristas
				aristas_vecino=vertice.aristas[vecino] #se obtiene la lista de aristas que lo conectan con el vecino
				for arista in aristas_vecino:
					print arista
	
class Digrafo(Grafo):
	
	def agregar_arista(self,ver_saliente,ver_entrante,peso=False):
		"""Pre: ver_saliente y ver_entrante son vertices que existen en el grafo"""
		arista=_Arista(ver_saliente,ver_entrante,peso)
		if (ver_saliente.aristas.has_key(ver_entrante.id)):
			aristas=ver_saliente.aristas[ver_entrante.id]
			aristas.append(arista)
		else:
			ver_saliente.aristas[ver_entrante.id]=[arista]
			
class Digrafo_s(Digrafo):
	
	def agregar_arista(self,ver_saliente,ver_entrante,peso=False):
		"""Pre: ver_saliente y ver_entrante son vertices que existen en el grafo
		   Post: se guardo la referencia a la arista. Si la arista existe se sobrescribe"""
		arista=_Arista(ver_saliente,ver_entrante,peso)
		ver_saliente.aristas[ver_entrante.id]=[arista]
		return True

g=Grafo()
g.agregar_vertice(2)
