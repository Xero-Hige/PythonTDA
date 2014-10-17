#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from facebook_graph import parse_file
from popularity_meter import *
from recommender import *
from influence import show_influence

COMMAND_POPULARITY = "POPULARITY"
COMMAND_INFLUENCE = "INFLUENCE"
COMMAND_RECOMENDATIONS = "RECOMENDATIONS"

COMMAND_SET_GRAPH = "SET_FILE"
COMMAND_EXIT = "EXIT"


def modo_automatico(facebook_graph):
	print "------POPULARITY-----"
	show_popularity_index(facebook_graph)
	print "------INFLUENCE------"
	show_influence(facebook_graph)
	print ""
	show_recommendations(facebook_graph)
	return 0

def main (argv):

	if (len(argv) < 2):
		print "Aviso: No se cargo ningun grafo"
		facebook_graph = None
	else:
		facebook_graph = parse_file(argv[1])

	if (len(argv) < 3):
		print "Modo interactivo:"
	elif (argv[2] != "-a"):
		print "Comando no reconocido\nModo interactivo:"
	else:
		print "Modo Automatico:"
		return modo_automatico(facebook_graph)


	command = ""

	while True:
		commands = raw_input().split(" ")
		command = commands[0]

		if (command == COMMAND_EXIT):
			break

		if (command == COMMAND_SET_GRAPH):
			facebook_graph = parse_file(commands[1])

		elif (command == COMMAND_POPULARITY):
			show_popularity_index(facebook_graph)

		elif (command == COMMAND_INFLUENCE):
			show_influence(facebook_graph)

		elif (command == COMMAND_RECOMENDATIONS):
			show_recommendations(facebook_graph)

		else:
			print "Error: Comando no reconocido: \""+command+"\""

	return 0;

main(sys.argv)