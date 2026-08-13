import numpy as np
from matplotlib import pyplot as plt

# given initial theta, r vals, i'll evaluate the simplified nonlinear system
# given by problem 12 in my intro to accelerators book. 

# with this simplified system, i'll hopefully be able to see behavior characteristic
# of real accelerating structures, as well as chaotic behavior based on different k vals.

k = 0.1
# k = 0.9

n_turns = 100

# initial values
r0 = 0.27
theta0 = 0

def iterate_r(r0, theta0):
    return r0 - ((k/(2 * np.pi)) * np.sin(2 * np.pi * theta0))

def iterate_theta(r, theta0):
    return theta0 + r


def plot(r, theta, color):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.scatter(x, y, color=color)

#'''
for n in range(n_turns):
    r = iterate_r(r0, theta0)
    theta = iterate_theta(r, theta0)

    #plot(r, theta, color='blue')
    plot(r, theta, color='#4e63f8')

    # plot or something before changing these variables
    r0 = r
    theta0 = theta

'''
# with different initial conditions
r0 = 0.4
theta0 = 0.2
n_turns = 100

for n in range(n_turns):
    r = iterate_r(r0, theta0)
    theta = iterate_theta(r, theta0)

    plot(r, theta, color='grey')
    # plot or something before changing these variables
    r0 = r
    theta0 = theta
'''

'''
# with chaotic initial conditions
r0 = 0.27
theta0 = 0
k = 0.9
n_turns = 800

for n in range(n_turns):
    r = iterate_r(r0, theta0)
    theta = iterate_theta(r, theta0)

    plot(r, theta, color='#4e63f8')
    # plot or something before changing these variables
    r0 = r
    theta0 = theta

# i like this one

plt.title(f'Nonlinear RF Bucket, n_turns = {n_turns}')
plt.ylabel('E')
plt.xlabel('$\phi$')
plt.savefig('nonlinear_bucket.png')
'''

plt.title(f'Stationary Bucket, n_turns = {n_turns}')
plt.ylabel('E')
plt.xlabel('$\phi$')
plt.savefig('stationary_bucket.png')
plt.show()