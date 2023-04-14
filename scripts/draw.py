import numpy as np
import matplotlib.pyplot as plt
import math

class C:
    PI = math.pi
    RB = 0.25
    RF = 0.25
    W = 0.5


#def draw_bot(x, y, color = "black"):
def draw_bot(x, y):
    car = np.array([[C.RB, -C.RB, -C.RF, C.RF, C.RB], 
                    [C.W/2, C.W/2, -C.W/2, -C.W/2, C.W/2]])
                   #[C.W/2, -C.W/2, -C.W/2, C.W/2, C.W/2]
    car += np.array([[x], [y]])

    plt.plot(car[0, :], car[1, :])
    #plt.plot(car[0, :], car[1, :], color)


