import numpy as np
from matplotlib import pyplot as plt

# with this i want to create a program to plot the phase space trajectory
# of a single particle in a beam given initial energy and phase using
# the difference equations of motion.

w_rf = 805e6 * 2 * np.pi
c = 3e8 #m/s
beta = 0.9 
v = beta * c #m/s

h = 1 #harmonic number
tau = w_rf / h / 2 / np.pi

#slip factor?? 
