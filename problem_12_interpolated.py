import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# given initial theta, r vals, i'll evaluate the simplified nonlinear system
# given by problem 12 in my intro to accelerators book. 

# with this simplified system, i'll hopefully be able to see behavior characteristic
# of real accelerating structures, as well as chaotic behavior based on different k vals.

k = 0.1
# k = 0.9

n_turns = 24

# initial values
r0 = 0.27
theta0 = 0


def iterate_r(r0, theta0):
    return r0 - ((k/(2 * np.pi)) * np.sin(2 * np.pi * theta0))

def iterate_theta(r, theta0):
    return theta0 + r


# i need a function to interpolate between iterated points
# to give a smooth trajectory
N = 10
def interpolate_points(x0, y0, x, y):
    return np.linspace(x0, x, N), np.linspace(y0, y, N)

def main(r0, theta0, color):

    for n in range(n_turns):

        x0 = r0 * np.cos(theta0)
        y0 = r0 * np.sin(theta0)

        r = iterate_r(r0, theta0)
        theta = iterate_theta(r0, theta0)

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        x_array, y_array = interpolate_points(x0, y0, x, y)

        plt.scatter(x_array, y_array, color=color)

        r0 = r
        theta0 = theta

        x_array = 0
        y_array = 0


main(r0, theta0, '#4e63f8')
plt.show()

