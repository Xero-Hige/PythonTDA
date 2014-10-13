from graph import Graph

PARSER_ID_POSITION = 0
PARSER_NAME_POSITION = 1


def parse_file(file_name):
	try:
		data_file = open(file_name,'r')
	except IOError:
		raise IOError, "Fallo al abrir el archivo gdf"

	network = Graph()

	line = data_file.readline()
	line = data_file.readline().rstrip()
	parsed_line = line.split(",")

	while (parsed_line[PARSER_ID_POSITION].isdigit()):
		id = parsed_line[PARSER_ID_POSITION]
		name = parsed_line[PARSER_NAME_POSITION]

		network.add_vertex(id,name)

		line = data_file.readline().rstrip()
		parsed_line = line.split(",")

	line = data_file.readline().rstrip()
	parsed_line = line.split(",")

	while (line != ""):
		id_1 = parsed_line[0]
		id_2 = parsed_line[1]

		network.add_edge(id_1,id_2)

		line = data_file.readline().rstrip()
		parsed_line = line.split(",")

	data_file.close()

	return network