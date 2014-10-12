from facebook_graph import parse_file

FACEBOOK_GRAPH_FILE = "./network.gdf"

class _Recommendation(object):
	""" Representa una recomendacion como un par
	'id' (el usuario recomendado) y 'value' (la 
	cantidad de amigos en comun con ese usuario)"""

	def __init__(self):
		self.recommendation_id = None
		self.recommendation_value = None

	def update(self, candidate_id, candidate_value):
		"""Recibe un id y un valor, y si el valor recibido es
		mayor que el valor de la recomendacion que se tiene 
		hasta el momento, la reemplaza por la nueva"""
		if(self.recommendation_value is None 
			or candidate_value > self.recommendation_value):
			self.recommendation_id = candidate_id
			self.recommendation_value = candidate_value

	def get_id(self):
		return self.recommendation_id

	def get_value(self):
		return self.recommendation_value


def get_recommendation_for(contact_id):
	""" Devuelve una recomendacion de amistad para 
	el contacto indicado, basada en la cantidad
	de amigos en comun con dicho contacto """

	fb_graph = parse_file(FACEBOOK_GRAPH_FILE)
	#BFS capa 1:
	fb_graph.mark_vertex(contact_id)
	friends = fb_graph.get_vertex_neighbours(contact_id)
	map(fb_graph.mark_vertex, friends)
	names = []

	#BFS capa 2;
	candidates_for_recommendation = []
	for friend in friends:
		candidates_for_recommendation.extend(fb_graph.get_unmarked_vertex_neighbours(friend))

	#CODIGO PARA PRUEBAS, BORRAR DESPUES
	'''for asd in candidates_for_recommendation:
		print(asd)
		names.append(fb_graph.get_vertex_data(asd))
	print(names)'''

	recommendation = _Recommendation()
	for candidate in candidates_for_recommendation:
		value = len( fb_graph.get_marked_vertex_neighbours(candidate) )
		recommendation.update(candidate, value)

	return recommendation


#EJEMPLO DE USO
recom = get_recommendation_for("1140884962")
if(recom.get_id() is None):
	print("No se encontraron recomendaciones")
else:
	g = parse_file(FACEBOOK_GRAPH_FILE)
	print "Recomendacion: " + g.get_vertex_data( recom.get_id() )
	print "Amigos en comun: " + str(recom.get_value())