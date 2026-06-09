import numpy as np
from matplotlib import pyplot as plt

from processing_functions import *

# physical constants
c = 3e8
epsilon = 8.8e-12
mu = 1.3e-6
Z_0 = np.sqrt(mu / epsilon)

# cavity parameters
a = 0.14232 # in mm
L = 0.11334 # in mm
beta = 0.9
kappa = 58.0e6 # for copper, in S/m


# for a given length, V_0 and E_0 changes, f is the same, T is the same, R_surf...
# for the chosen length above vv

mode_1_frequency = mode_1_frequency(a)
print(f'Mode 1 frequency: {mode_1_frequency} [Hz]')

skin_depth = skin_depth_func(mode_1_frequency, kappa, mu)
print(f'Skin depth of our cavity: {skin_depth}')

E_0 = max_field(a, L)
print(f'Initial E field is: {E_0} [V/m]')

U = total_energy(E_0)
print(f'Total energy is: {U} [J]')

R_surf = surface_resistance(kappa, skin_depth)
print(f'Surface resistance: {R_surf} [Ohms]')

V_0 = voltage(E_0, L)
print(f'Voltage: {V_0} [V]')

T = transitive_time_factor(beta)
print(f'Transitive time factor: {T}')

V_eff = effective_voltage(T, V_0)
print(f'Effective voltage: {V_eff} [V]')

P_d = dissapated_power(E_0, R_surf, a, L)
print(f'Dissapated power: {P_d} [W]')

Q_0 = Q_factor(skin_depth, L, a)
print(f'Q-factor: {Q_0}')

Q_0_second = Q_factor_also(L, a, R_surf, mode_1_frequency)
print(f'Q-factor is also: {Q_0_second}')

Q_0_third = Q_factor_also_also(skin_depth, L, a)
print(f'Q-factor is also also: {Q_0_third}')

R_eff = eff_shunt_impedance(R_surf, T, a, L)
print(f'Effective shunt-impedance (big formula, likely): {R_eff}')

R_eff_also = eff_R_s_also(V_0, T, P_d)
print(f'Effective shunt-impedance (small formula): {R_eff_also}')

print(f'R/Q (likely): {R_eff / Q_0_second}')
print(f'R/Q (off by T?): {R_eff_also / Q_0_second * epsilon * c}')

R_Q = R_over_Q(T, L, a, mode_1_frequency)
print(f'R/Q (reference, big formula): {R_Q}')


# ------------------------------------------------------------------
# ------------------------ PLOTTING --------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

# here, i'll plot Q_0, shunt impedance per unit length, R/Q, and P_d

plotcolor = 'purple'
L_vals = np.linspace(0, L, 15)

fig, axs = plt.subplots(2, 2)
y_param = '$Q_0$'
axs[0, 0].plot(L_vals, Q_factor(skin_depth, L_vals, a), color=plotcolor)
axs[0, 0].set_title('Axis [0, 0]')
axs[0, 0].set_ylabel(y_param)

y_param = '$Shunt Impedance per unit Length$'
axs[0, 1].plot(L_vals, eff_shunt_impedance(R_surf, T, a, L_vals)/L_vals, color=plotcolor)
axs[0, 1].set_title('Axis [0, 1]')
axs[0, 1].set_ylabel(y_param)

y_param = '$R/Q$'
axs[1, 0].plot(L_vals, R_over_Q(T, L_vals, a, mode_1_frequency), color=plotcolor)
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 0].set_ylabel(y_param)

y_param = '$Q_0$'
axs[1, 1].plot(L_vals, eff_shunt_impedance(R_surf, T, a, L_vals), color=plotcolor)
axs[1, 1].set_title('Axis [1, 1]')
axs[1, 1].set_ylabel(y_param)

for ax in axs.flat:
    ax.set(xlabel='Length (m)')

# Hide x labels and tick labels for top plots and y ticks for right plots.
#for ax in axs.flat:
#    ax.label_outer()

fig.savefig('figures/processing_plotting.png')
