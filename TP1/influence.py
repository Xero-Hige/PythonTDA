from graph import Graph
from collections import deque

def Brand1(fb_graph):
	influence = {}
	for vertex in fb_graph.vertex:
		influence[vertex] = 0
	for s in fb_graph.vertex:
		stack = deque()
		P = {}
		o = {}
		d = {}
		sigma = {}
		for vertex in fb_graph.vertex:
			P[vertex] = []
			o[vertex] = 0
			d[vertex] = -1
			sigma[vertex] = 0
		o[s] = 1
		d[s] = 0
		queue = deque()
		queue.append(s)
		while len(queue) > 0:
			v = queue.popleft()
			stack.append(v)
			for neighbour in fb_graph.get_vertex_neighbours(v):
				#Se encontro por primera vez?
				if d[neighbour] < 0:
					queue.append(neighbour)
					d[neighbour] = d[v] + 1
				#Es el camino mas a neighbour via v?
				if d[neighbour] == d[v] + 1:
					o[neighbour] = o[neighbour] + o[v]
					P[neighbour].append(v)
		while len(stack) > 0:
			w = stack.pop()
			for v in P[w]:
				sigma[v] = sigma[v] + o[v]/(float(o[w])) * (1 + sigma[w])
				if w != s:
					influence[w] = float(influence[w]) + float(sigma[w])
	return influence

def decode(fb_graph,influences):
	"""Genera una lista con tuplas nombre,influencia en base al diccionario
		de influencias pasado como parametro, obteniendo los nombres correspondientes
		a las id del mismo del grafo"""
	result = []
	for id,influence in influences.items():
		name = fb_graph.get_vertex_data(id)
		result.append((name,influence))

	return result

def show_influence(fb_graph):
	"""Calcula y muestra la influencia de cada actor dentro del grafo de facebook
		en forma decreciente en base a su influencia"""
	influences = Brand1(fb_graph)
	influence_list = decode(fb_graph,influences)
	influence_list.sort(key=lambda tup: tup[1],reverse=True)
	for name,influence in influence_list:
		if influence<0.01 and influence>0:
			influence = 0.01	
			#Al mostrar la influencia la redondea solo para para poder separar los casos que son 0 de los que no
		print '{0:<30s} Influencia: {1:>9.2f}'.format(name,influence)
