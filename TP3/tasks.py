from collections import namedtouple

File_line = namedtuple('File_line', 't,v,b')
Task = namedtuple('Task', 'id,t,v,b')


def parse_lines(file):
	tasks = []
	id = 0
	for l in file:
		parsed = l.split(",")
		line = File_line.make([int(parsed[0]),int(parsed[1]),int(parsed[2])])
	
		tasks.append(Task.make([id,line.t,line.v,line.b]))
		t_init -= 1
		
		id+=1
		

def sort_tasks(tasks):
	tasks.sort(key=lambda x: (x.v))

def generate_base_matrix(tasks):
	row_length = tasks[-1].v

	matrix = []

	for x in xrange(row_length):
		matrix.append([0]*len(tasks))

	return matrix

def calculate(tasks):
	matrix = generate_base_matrix(tasks)

	for i in xrange(1,len(tasks)):
		for t in xrange(tasks[-1].v):
			t_prim = min(t,tasks[i].v)-tasks[i].t

			if t_prim < 0:
				matrix[i][t]=matrix[i-1][t]
			else:
				matrix[i][t]=max(matrix[i-1][t],tasks[i].b+matrix[i-1][t_prim])

	return matrix

def show_result(tasks,matrix,i,t):
	if i==0:
		return

	if matrix[i][t] == matrix[i-1][t]:
		show_result(tasks,matrix,i-1,t)
	else:
		t_prim = min(t,tasks[i].v)-tasks[i].t
		show_result(tasks,matrix,i-1,t_prim)
		print task[i].id,