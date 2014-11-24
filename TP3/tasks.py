from collections import namedtouple

File_line = namedtuple('File_line', 't,v,b')
Task = namedtuple('Task', 'id,t_init,t_end,v,b')


def parse_lines(file):
	tasks = []
	id = 0
	for l in file:
		parsed = l.split(",")
		line = File_line.make([int(parsed[0]),int(parsed[1]),int(parsed[2])])
		t_init = line.v - line.t
		
		while t_init >= 0:
			tasks.append(Task.make([id,t_init,t_init+line.t,line.v,line.b]))
			t_init -= 1
		
		id+=1
		

def sort_tasks(tasks):
	tasks.sort(key=lambda x: x.t_end)

def 