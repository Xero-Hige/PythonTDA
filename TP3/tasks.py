from collections import namedtuple

File_line = namedtuple('File_line', 't,v,b')
Task = namedtuple('Task', 'id,t,v,b')


def parse_lines(file):
	tasks = []
	id = 0
	for l in file:
		parsed = l.split(",")
		line = File_line._make([int(parsed[0]),int(parsed[1]),int(parsed[2])])
	
		tasks.append(Task._make([id,line.t,line.v,line.b]))
		
		id+=1
	return tasks
		

def sort_tasks(tasks):
	tasks.sort(key=lambda x: (x.v))

def generate_base_matrix(tasks):
	row_length = tasks[-1].v

	matrix = []

	for x in xrange(row_length):
		matrix.append([0]*len(tasks))

	return matrix

def calculate(tasks):
	sort_tasks(tasks)
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
		
def main():
	f = open("tasks.tsk")
	tasks = parse_lines(f)
	task_matrix = calculate(tasks)
	show_result(tasks,task_matrix,len(tasks_matrix[0])-1,len(task_matrix)-1)
	f.close()

main()
