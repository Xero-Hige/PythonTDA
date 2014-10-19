WHITE = 0
BLACK = 1

class _Vertex(object):
	"""Clase vertice que modela los vertices de un grafo"""
	
	def __init__(self,id,data):
		"""Crea una instancia de el tipo _Vertex"""
		self.id = id
		self.state = WHITE
		self.neighbors = []
		self.edges = {}
		self.data = data

	def get_neighbors(self):
		return self.edges.keys()
		
	def __cmp__(self,another_vertex):
		"""Comparacion que indica una relacion de orden entre los indices
			de los vertices de un grafo"""
		if (self.id > another_vertex.id):
			return 1
		elif(self.id < another_vertex.id):
			return -1
		return 0
		
class _Edge(object):
	"""Clase arista que modela las uniones entre 2 vertices de un grafo
		opccionalmente en un digrafo el vert1 es el vertice saliente y
		el vert2 es el vertice entrante"""
		
	def __init__(self,initial_vertex,end_vertex,weight=1):
		self.init_point = initial_vertex
		self.end_point = end_vertex
		self.weight = weight

	def __cmp__(self,another):
		"""Una arista es menor a otra cuando su peso es menor"""
		if (self.weight > another.weight):
			return 1
		elif(self.weight < another.weight):
			return -1
		return 0
		
class Graph(object):

	def __init__(self):
		self.vertex = {}
		self.size = 0
	
	def add_vertex(self,id,data=None):
		vertex = _Vertex(id,data)
		self.vertex[id] = vertex
		self.size += 1
	
	def add_edge(self,initial_point,end_point,weight=1):
		"""Pre: initial_point y end_point son vertices que existen en el grafo"""
		
		initial = self.vertex[initial_point]
		end = self.vertex[end_point]

		edge = _Edge (initial,end,weight)

		initial.edges[end_point] = edge
		end.edges[initial_point] = edge
		
	def unmark_all(self):
		for vertex in self.vertex.values():
			vertex.state=WHITE

	def mark_vertex(self,vertex_id):
		self.vertex[vertex_id].state = BLACK

	def unmark_vertex(self,vertex_id):
		self.vertex[vertex_id].state = WHITE

	def is_marked(self,vertex_id):
		return self.vertex[vertex_id].state == BLACK
	
	def vertex_exists(self,vertex_id):
		return self.vertex.has_key(id_Vertex)

	def get_vertex_neighbours(self,vertex_id):
		return self.vertex[vertex_id].get_neighbors()

	def get_unmarked_vertex_neighbours(self,vertex_id):
		neighbours = self.get_vertex_neighbours(vertex_id)
		unmarked_neighbours = []
		for neighbour in neighbours:
			if( not self.is_marked(neighbour) ):
				unmarked_neighbours.append(neighbour)

		return unmarked_neighbours

	def get_marked_vertex_neighbours(self,vertex_id):
		neighbours = self.get_vertex_neighbours(vertex_id)
		unmarked_neighbours = []
		for neighbour in neighbours:
			if( self.is_marked(neighbour) ):
				unmarked_neighbours.append(neighbour)

		return unmarked_neighbours

	def get_vertex_data(self,vertex_id):
		return self.vertex[vertex_id].data

	def get_all_vertex_ids(self):
		return self.vertex.keys();
