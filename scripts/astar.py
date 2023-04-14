import math
import numpy as np
import heapq

def time_a_star(path):
	time_dict = dict()
	for time, node in enumerate(path):
		#print(f'instance = {ii}, node = {node}')
		time_dict[node[0], node[1], time] = 1
	timed_keys = list(time_dict.keys())
	return timed_keys


def astar(start, goal, ox, oy):
	Open_list = []
	Closed_list = []
	g = dict()
	Parent = dict()
	g[start] = 0
	g[goal] = math.inf
	Parent[start] = start
	heapq.heappush(Open_list, (f_value(start, g[start], goal), start))	
	
	while Open_list:
		_, s = heapq.heappop(Open_list)
		Closed_list.append(s)
		if s == goal:
			break
		for s_n in find_neighbors(s):
			new_cost = g[start] + cost(start, s_n)
			if s_n not in g:
				g[s_n] = math.inf
			
			if new_cost < g[s_n]:
				g[s_n] = new_cost
					
				Parent[s_n] = s
				heapq.heappush(Open_list, (f_value(s_n, g[s_n], goal), s_n))
	path = extract_path(Parent, start, goal)
	return path

def extract_path(Parent, start, goal):
	path = [goal]
	s= goal
	while True:
		s= Parent[s]
		path.append(s)
		if s == start:
			break
	path = path[::-1]
	return list(path)

def cost(p1,p2):
	return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def h_cost(p1, p2):
	return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def f_value(s, g, goal):
	return g + h_cost(s, goal)

def find_neighbors(node):
	neighbors = []
	xyreso = 1
	motion_set = [[-xyreso,0],[0,-xyreso], [0,xyreso], [xyreso,0]]

	for ii, m in enumerate(motion_set):
		nx = node[0] + m[0]
		ny = node[1] + m[1]
		#setting graph limits so as to accomodate the car in horizontal consition at the extreme righ-left or top-bottoms
		if nx > 0 and nx  <250 and ny > 0 and ny < 250:
			neighbors.append((nx,ny))
	#print('neighors = ', neighbors)
	return neighbors




