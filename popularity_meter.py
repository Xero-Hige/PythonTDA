#!/usr/bin/env python
# -*- coding: utf-8 -*-

from facebook_graph import parse_file

class _Popularity_indicator(object):
	"""Estructura que relaciona un contacto del grafo
	con su cantidad de amigos"""

	def __init__(self, contact, number_of_friends):
		self.id = contact
		self.popularity = number_of_friends

	def __repr__(self):
		return repr( (self.id, self.popularity) )


def get_popularity_index(fb_graph):
	"""Devuelve una lista de _Popularity_indicator,
	en orden descendente por nivel de popularidad"""

	contacts = fb_graph.get_all_vertex_ids()
	popularity_index = []
	for contact in contacts:
		name = fb_graph.get_vertex_data(contact)
		number_of_friends = len(fb_graph.get_vertex_neighbours(contact))
		popularity_index.append( _Popularity_indicator(name, number_of_friends) )

	return sorted(popularity_index, key=lambda pindex: pindex.popularity, reverse=True )


def show_popularity_index(fb_graph):
	"""Función para presentar el índice de 
	popularidad por pantalla"""

	popularity_index = get_popularity_index (fb_graph)

	for popularity_indicator in popularity_index:
		print popularity_indicator.id + ":",
		print popularity_indicator.popularity,
		if popularity_indicator.popularity == 1:
			print "amigo"
		else:
			print "amigos"
			

"""#EJEMPLO DE USO
fb_graph = parse_file("./network.gdf")
show_popularity_index( get_popularity_index(fb_graph) )"""