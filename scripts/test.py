from astar import *
import math
import numpy
from draw import draw_bot
import matplotlib.pyplot as plt
import time 
from multiprocessing import Process

def update_time_dict(time_keys, path):
	new_time_keys = time_a_star(path)
	old_keys = time_keys.copy()
	for key in new_time_keys:
		old_keys.append(key)
	return old_keys


def update_path(time_keys, path):
	k = 0
	
	while k < len(path):
		if (path[k][0], path[k][1], k) in time_keys:
			path.insert(k, (path[k-1][0],path[k-1][1]))
			print(f"key {path[k][0], path[k][1], k} already occupied")
			k = 0
			continue
		k += 1
	return path

def plot_path_update(path_list):
	n = len(path_list)
	len_list = [len(path) for path in path_list]
	print('len list = ',len_list)
	print('max = ',max(len_list))
	for path in path_list:
		diff = max(len_list) - len(path)
		if diff != 0:
			for k in range(diff):
				path.append(path[-1])

	len_list = [len(path) for path in path_list]
	print('len list = ',len_list)
	print('max = ',max(len_list))

	return path_list


def main():
	start_pts = [(5,5), (7,5), (1,6), (15,22)]
	goal_pts = [(7,11), (3,17), (8,17), (3,10)]
	ox, oy = [], []
	path_list = []
	
	for i in range(len(start_pts)):
		#calculate shortest path
		path = astar(start_pts[i], goal_pts[i], ox, oy)
		if (i == 0):
			#create a robot coordinate list with (x,y,t)
			timed_keys = time_a_star(path)
		else:
			#update path to avoid collision with prev robots paths
			path = update_path(timed_keys, path)
			timed_keys = update_time_dict(timed_keys, path)
		#create a path lists for plotting
		path_list.append(path)
		path_all = plot_path_update(path_list)	

	#----------------------------------- start of plotting -----------------------------------------------/	
	for i in range(len(path_all[0])):
		plt.cla()
		plt.plot(ox,oy,'sk')
		for start, goal in zip(start_pts, goal_pts):
			plt.plot(start[0], start[1],'sg')
			plt.plot(goal[0], goal[1],'sr')
			
		for path_n in path_all:
			draw_bot(path_n[i][0], path_n[i][1])
		plt.axis('equal')
		plt.xlim([0,30])
		plt.ylim([0,30])
		plt.show(block=False)	
		plt.pause(0.5)
		

	
if __name__ == "__main__":
	main()
