import numpy as np
from matplotlib import pyplot as plt
import random

# this is a work in progress...

# based off of the properties of the material, we can define an appropriate range
# for the plot. with lead

X_0 = 0.56 # radiation length in cm
Z = 82 # atomic number

# i'll take the initial electron position to be at (0,0)
# it is traveling also with no angle, and travels X_0 before radiating.

fig = plt.figure()
ax = plt.axes()
ax.set_facecolor('black')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


# initial electron
x = [0, 0]
y = [0, X_0]

ax.plot(x, y, color="white")

# here's the first split. i'll just have them in equal and opposite directions.
# in 'split photon' or 'split electron', i'll generalize to take an incident energy, angle and position
# and then draw the path that the daughter particles take. 
def splitElectron(x, y, incident_angle):
    # the photon/electron combination can be either direction
    outgoing_angle = (np.pi / 2 - incident_angle) / 2

    # print([-1,1][random.randrange(2)])
    direction = [-1,1][random.randrange(2)]

    # i'm choosing for now to hard code the distances that the photon or electron will travel.
    # for now also i'll hard code that they're the same distance, X_0

    #x, y for the photon is then X_0 * cos(outgoing_angle), X_0 * sin(outgoing_angle)
    ax.plot([x, x + -direction * X_0 * np.cos(outgoing_angle)], [y, y + X_0 * np.sin(outgoing_angle)], color="slateblue")
    ax.plot([x, x + direction * X_0 * np.cos(outgoing_angle)], [y, y + X_0 * np.sin(outgoing_angle)], color="blanchedalmond")

splitElectron(0, X_0, 0)



plt.show()

