import sys
from collections import namedtuple

File_line = namedtuple('File_line', 't,v,b')
Task = namedtuple('Task', 'id,duration,deadline,benefit')

def parse_lines(file):
	tasks = []
	id = 1
	for l in file:
		parsed = l.split(",")
		try:
			line = File_line._make([int(parsed[0]),int(parsed[1]),int(parsed[2])])
		except ValueError:
			continue

		tasks.append(Task._make([id,line.t,line.v,line.b]))
		
		id+=1
	return tasks
		

def sort_tasks(tasks):
	"""Ordena una lista de tareas in place segun el tiempo de 
		vencimiento en orden creciente"""
	tasks.sort(key=lambda x: (x.deadline))

def generate_base_matrix(tasks):
	"""Genera una matriz de numero de tareas + 1 filas y vencimiento maximo columnas"""
	columns = tasks[-1].deadline + 1

	matrix = []

	for x in xrange(len(tasks)):
		matrix.append([0]*columns)

	return matrix

def calculate(tasks):
	matrix = generate_base_matrix(tasks)

	for i in xrange(1,len(tasks)):
		for t in xrange(tasks[-1].deadline+1):
			t_prim = min(t,tasks[i].deadline)-tasks[i].duration

			if t_prim < 0:	#La tarea no se puede agregar
				matrix[i][t]=matrix[i-1][t]
			else:			#Compruebo si agregar la tarea mejora o no los resultados anteriores
				matrix[i][t]=max(matrix[i-1][t],tasks[i].benefit+matrix[i-1][t_prim])

	return matrix

def show_result(tasks,matrix,i,t):
	if i==0:
		return

	if matrix[i][t] == matrix[i-1][t]:
		show_result(tasks,matrix,i-1,t)
	else:
		t_prim = min(t,tasks[i].deadline)-tasks[i].duration
		show_result(tasks,matrix,i-1,t_prim)
		print tasks[i].id,
		
def main(argv):
	if len(argv) < 2:
		print "Falta archivo de entrada"
		return

	try:
		f = open(argv[1])
	except IOError:
		print "Error al abrir el archivo:",argv[1]
		return

	tasks = parse_lines(f)
	
	if (tasks == []):
		print "El archivo no posee ninguna tarea valida"
		return

	sort_tasks(tasks)			#Ordeno segun vencimiento creciente

	tasks = [None] + tasks 		#Agrego una tarea none solo para que coincidan los
								#indices de las tareas con el numero de tarea (no es el id)

	task_matrix = calculate(tasks)

	number_of_tasks = len(tasks)-1 	#La tarea que es none no se considera
	time = len(task_matrix[0])-1 	#Solo los indices validos (coindide con 0 a Vmax)

	show_result(tasks,task_matrix,number_of_tasks,time)
	f.close()

main(sys.argv)
