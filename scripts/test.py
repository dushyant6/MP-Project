from astar import *
import math
import numpy
from draw import draw_bot, draw_endpoint
import matplotlib.pyplot as plt
import time 

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
	for path in path_list:
		diff = max(len_list) - len(path)
		if diff != 0:
			for k in range(diff):
				path.append(path[-1])

	len_list = [len(path) for path in path_list]

	return path_list


def main():
	start_pts = [(5,5), (7,5), (1,6), (15,22), (24,12), (21,20), (19,3), (25,20),(4,12)]
	goal_pts = [(7,11), (3,17), (8,17), (3,10), (12,4), (2,2), (3,13), (4,20),(25,20)]
	ox, oy = [], []
	path_list = []
	
	for i in range(15,21):
		ox.append(i)
		oy.append(12)

	for i in range(15,22):
		ox.append(i)
		oy.append(19)

	for i in range(12,19):
		oy.append(i)
		ox.append(15)

	for i in range(12,19):
		oy.append(i)
		ox.append(21)
		

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

	#-------------------------------------- start of plotting -----------------------------------------------
	vis = False
	if vis:
		for i in range(len(path_all[0])):
			plt.cla()
			plt.plot(ox,oy,'sk')
			for start, goal in zip(start_pts, goal_pts):
				#draw_endpoint(start, 'orange')
				draw_endpoint(goal,'grey')
				
			for path_n in path_all:
				draw_bot(path_n[i][0], path_n[i][1])
			plt.axis('equal')
			plt.xlim([-5,30])
			plt.ylim([-5,30])
			plt.show(block=False)	
			plt.pause(0.8)
	plt.show()		
	#abstract distace of any point from a goal point
	x = (24,24)
	y = AbstractDist(x, goal_pts[-1], ox, oy)
	
	
	
if __name__ == "__main__":
	main()
