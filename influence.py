from graph import Graph
from collections import deque

def Brand1(fb_graph):
	C = {}
	for vertex in fb_graph.vertex:
		C[vertex] = 0
	for s in fb_graph.vertex:
		stack = deque()
		P = {}
		o = {}
		d = {}
		sigma = {}
		for w in fb_graph.vertex:
			P[w] = []
			o[w] = 0
			d[w] = -1
			sigma[w] = 0
		o[s] = 1
		d[s] = 0
		queue = deque()
		queue.append(s)
		while len(queue) > 0:
			v = queue.popleft()
			stack.append(v)
			for w in fb_graph.get_vertex_neighbours(v):
				""" w found for the first time? """
				if d[w] < 0:
					queue.append(w)
					d[w] = d[v] + 1
				""" Shortest path to w via v? """
				if d[w] == d[v] + 1:
					o[w] = o[w] + o[v]
					P[w].append(v)
		while len(stack) > 0:
			w = stack.pop()
			for v in P[w]:
				sigma[v] = sigma[v] + o[v]/(float(o[w])) * (1 + sigma[w])
				if w != s:
					C[w] = float(C[w]) + float(sigma[w])
	return C

def decode(fb_graph,influences):
	result = []
	for id,influence in influences.items():
		name = fb_graph.get_vertex_data(id)
		result.append((name,influence))

	return result

def show_influence(fb_graph):
	influences = Brand1(fb_graph)
	influence_list = decode(fb_graph,influences)
	influence_list.sort(key=lambda tup: tup[1],reverse=True)
	for name,influence in influence_list:
		if influence<0.01 and influence>0:
			influence = 0.01	
			#Al mostrar la influencia la redondea solo para para poder separar los casos que son 0 de los que no
		print '{0:<30s} Influencia: {1:>9.2f}'.format(name,influence)
