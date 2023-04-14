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

	

def path_list_for_plotting(path_list):
	for path in path_list:
		for i in range(len(path)):
			path_x.append(path[i][0])
			path_y.append(path[i][1])



def main():
	#---------------start of first path finding---------------------------
	start = (5,5)
	goal = (7,11)
	sx, sy, gx, gy = [], [], [], []
	path_list = []
	sx.append(start[0]); sy.append(start[1])
	gx.append(goal[0]); gy.append(goal[1])
	ox, oy = [], []
	path = astar(start, goal, ox, oy)
	timed_keys = time_a_star(path)

	#---------------start of second path finding---------------------------
	start = (7,5)
	goal = (3,17)
	sx.append(start[0]); sy.append(start[1])
	gx.append(goal[0]); gy.append(goal[1])
	path2 = astar(start, goal, ox, oy)
	
	path2 = update_path(timed_keys, path2)
	
	new_keys = update_time_dict(timed_keys, path2)
	timed_keys2 = time_a_star(path2)
	
	print(f'length of path1 = {len(timed_keys)}, length of keys 2 = {len(timed_keys2)}, length of new keys = {len(new_keys)}')
	
	#---------------start of third path finding---------------------------
	start = (1,6)
	goal = (8,17)
	sx.append(start[0]); sy.append(start[1])
	gx.append(goal[0]); gy.append(goal[1])
	path3 = astar(start, goal, ox, oy)

	path3 = update_path(new_keys, path3)

	timed_keys3 = time_a_star(path3)
	print(f' max path length = {len(path), len(path2), len(path3)}')
	path_list = [path, path2, path3]
	path_all = plot_path_update(path_list)
	print(f'length of path all = {len(path_all)}x{len(path_all[0])}x{len(path_all[0][1])}')
	x_path_list, y_path_list = [], []
	for seg in path_all:
		for xy in seg:
			x_path_list.append(xy[0])
			y_path_list.append(xy[1])

	#----------------------------------- start of plotting -----------------------------------------------/	
	for i in range(len(path2)):
		plt.cla()
		plt.plot(ox,oy,'sk')
		plt.plot(sx,sy,'sg')
		plt.plot(gx,gy,'sr',linewidth = 0.1)

		for path_n in path_all:
			draw_bot(path_n[i][0], path_n[i][1])
		plt.axis('equal')
		plt.xlim([-10,30])
		plt.ylim([-10,30])
		plt.show(block=False)	
		plt.pause(0.5)
		

	
if __name__ == "__main__":
	main()
