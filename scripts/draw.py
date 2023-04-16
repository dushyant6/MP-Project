import numpy as np
import matplotlib.pyplot as plt
import math

class C:
    PI = math.pi
    RB = 0.25
    RF = 0.25
    W = 0.5


def draw_bot(x, y):
    car = np.array([[C.RB, -C.RB, -C.RF, C.RF, C.RB, -C.RB, -C.RB, C.RB], 
                    [C.W/2, C.W/2, -C.W/2, -C.W/2, C.W/2, -C.W/2, C.W/2, -C.W/2]])
                   #[C.W/2, -C.W/2, -C.W/2, C.W/2, C.W/2]
    car += np.array([[x], [y]])
    plt.plot(car[0, :], car[1, :])


def draw_endpoint(point, color= 'black'):
	end = np.array([[C.RB+0.1, -C.RB-0.1, -C.RF-0.1, C.RF+0.1, C.RB+0.1], 
		    [C.W/2+0.1, C.W/2+0.1, -C.W/2-0.1, -C.W/2-0.1, C.W/2+0.1]])
	end += np.array([[point[0]], [point[1]]])
	plt.plot(end[0, :], end[1, :], color)

