from facebook_graph import parse_file

class _Recommendation(object):
	""" Representa una recomendacion como un par
	'id' (el usuario recomendado) y 'value' (la 
	cantidad de amigos en comun con ese usuario)"""

	def __init__(self, receiver):
		self.receiver = receiver
		self.id = None
		self.value = None

	def update(self, candidate_id, candidate_value):
		"""Recibe un id y un valor, y si el valor recibido es
		mayor que el valor de la recomendacion que se tiene 
		hasta el momento, la reemplaza por la nueva"""
		if(self.value is None 
			or candidate_value > self.value):
			self.id = candidate_id
			self.value = candidate_value



def get_recommendation_for(contact_id, fb_graph):
	""" Devuelve una recomendacion de amistad para 
	el contacto indicado, basada en la cantidad
	de amigos en comun con dicho contacto """

	#BFS capa 1:
	fb_graph.mark_vertex(contact_id)
	friends = fb_graph.get_vertex_neighbours(contact_id)
	map(fb_graph.mark_vertex, friends)

	#BFS capa 2;
	candidates_for_recommendation = []
	for friend in friends:
		candidates_for_recommendation.extend(fb_graph.get_unmarked_vertex_neighbours(friend))


	recommendation = _Recommendation(contact_id)
	for candidate in candidates_for_recommendation:
		value = len( fb_graph.get_marked_vertex_neighbours(candidate) )
		recommendation.update(candidate, value)
		
	fb_graph.unmark_all()
	return recommendation


def get_recommendations(fb_graph):
	"""Devuelve una lista con una recomendacion por cada contacto
	del archivo"""

	contacts = fb_graph.get_all_vertex_ids()

	recommendations = []
	for contact in contacts:
		recommendations.append( get_recommendation_for(contact, fb_graph) )

	#TODO: borrar
	return sorted(recommendations)


def show_recommendations(fb_graph):
	"""Funcion para presentar los resultados de las
	recomendaciones por pantalla"""

	recommendations = get_recommendations(fb_graph)

	for recommendation in recommendations:
		print '{0:<30s}'.format(fb_graph.get_vertex_data( recommendation.receiver )) + ": ",
		if(recommendation.id is None):
			print "no hay recomendaciones"
		else:
			print '{0:<30s}'.format(fb_graph.get_vertex_data( recommendation.id )),
			if (recommendation.value == 1):
				print "(   1 amigo en comun)"
			else:
				print "(" + "%4s" % str(recommendation.value) + " amigos en comun)"

"""#EJEMPLO DE USO
show_recommendations(parse_file("./network.gdf"))"""