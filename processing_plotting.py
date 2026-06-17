import numpy as np
from matplotlib import pyplot as plt

from processing_functions import *

# for a given length, V_0 and E_0 changes, f is the same, T is the same, R_surf...
# for the chosen length above vv

mode_1_frequency = mode_1_frequency(a)
print(f'Mode 1 frequency: {mode_1_frequency} [Hz]')

skin_depth = skin_depth_func(mode_1_frequency, kappa, mu)
print(f'Skin depth of our cavity: {skin_depth}')

E_0 = max_field(a, L)
print(f'Initial E field is: {E_0} [V/m]')
#^ this is for sure incorrect!

U = total_energy(E_0)
print(f'Total energy is: {U} [J]')

R_surf = surface_resistance(kappa, skin_depth)
print(f'Surface resistance: {R_surf} [Ohms]')

V_0 = voltage(E_0, L)
print(f'Voltage: {V_0} [V]')

T = transitive_time_factor(mode_1_frequency, L, beta)
print(f'Transitive time factor: {T}')

#lets see if this helps
#T = 0.97
#print(f'Transitive time factor: {T}')

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

P_d_also = also_dissapated_power(mode_1_frequency, U, Q_0)
print(f'Also dissapated power: {P_d_also}')

R_eff = eff_shunt_impedance(R_surf, T, a, L)
print(f'Effective shunt-impedance (big formula, likely): {R_eff}')

R_eff_also = eff_R_s_also(V_0, T, P_d)
print(f'Effective shunt-impedance (small formula): {R_eff_also}')

print(f'Shunt impedance per unit length: {R_eff_also / 100}')

#print('^^^Shunt impedance per length in CST is 4.8e4. R/Q is 1.13e-5')
#print('Total loss is 2e5')


print(f'R/Q (likely): {R_eff / Q_0_second}')
#print(f'R/Q (off by T?): {R_eff_also / Q_0_second * epsilon * c}')

R_Q = R_over_Q(T, L, a, mode_1_frequency)
print(f'R/Q (reference, big formula): {R_Q}')

maybe_R_Q = maybe_R_over_Q(V_0, T, mode_1_frequency, U)
print(f'R/Q (perchance): {maybe_R_Q}')


# ------------------------------------------------------------------
# ------------------------ PLOTTING --------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

# here, i'll plot Q_0, shunt impedance per unit length, R/Q, and P_d

#plotcolor = 'mediumpurple'
#plotcolor = 'slateblue'
plotcolor = '#4e63f8'
L_vals = np.linspace(0.030, 0.150, 25)

#fig, ax = plt.subplots(1,1)
#y_param = 'Q-factor'
#ax.plot(L_vals * 1000, Q_factor(skin_depth, L_vals, a), color=plotcolor)
#ax.set_title(y_param + ' versus length')
#ax.set_ylabel(y_param)
#ax.set_xlabel('Length [mm]')
#fig.savefig('figures/' + y_param + '.png')

fig, ax = plt.subplots(1,1)
y_param = 'Shunt impedance'
ax.plot(L_vals * 1000, eff_shunt_impedance(R_surf, T, a, L_vals), color=plotcolor)
ax.set_title(y_param + ' versus length')
ax.set_ylabel(y_param)
ax.set_xlabel('Length [mm]')
fig.savefig('figures/' + y_param + '.png')

fig, ax = plt.subplots(1,1)
y_param = 'Shunt impedance per unit length'
ax.plot(L_vals * 1000, eff_shunt_impedance(R_surf, T, a, L_vals)/L_vals/1000, color=plotcolor)
ax.set_title(y_param + ' versus length')
ax.set_ylabel(y_param)
ax.set_xlabel('Length [mm]')
fig.savefig('figures/' + y_param + '.png')

fig, ax = plt.subplots(1,1)
y_param = 'R over Q'
ax.plot(L_vals * 1000, R_over_Q(T, L_vals, a, mode_1_frequency), color=plotcolor)
ax.set_title(y_param + ' versus length')
ax.set_ylabel(y_param)
ax.set_xlabel('Length [mm]')
fig.savefig('figures/' + y_param + '.png')

fig, ax = plt.subplots(1,1)
y_param = 'Dissapated power'
ax.plot(L_vals * 1000, dissapated_power(E_0, R_surf, a, L_vals * 1000), color=plotcolor)
ax.set_title(y_param + ' versus length')
ax.set_ylabel(y_param)
ax.set_xlabel('Length [mm]')
fig.savefig('figures/' + y_param + '.png')

# not against length
freq_vals = np.linspace(1, 1e10, 30)
fig, ax = plt.subplots(1,1)
y_param = 'Skin depth'
ax.plot(freq_vals, skin_depth_func(freq_vals, kappa, mu), color=plotcolor)
ax.set_title(y_param + ' versus frequency')
ax.set_ylabel(y_param)
ax.set_xlabel('frequency')
fig.savefig('figures/' + y_param + '.png')