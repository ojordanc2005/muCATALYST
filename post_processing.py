import numpy as np
from scipy import special
from matplotlib import pyplot as plt

# physical constants
c = 3e8
epsilon = 8.8e-12
mu = 1.3e-6
Z_0 = np.sqrt(mu / epsilon)

# cavity parameters
a = .142 # in mm
L = .100 # in mm
#E_0 = 1
beta = 0.9
kappa = 59.6e6 # for copper, in S/m

# ---------- Mode 1 frequency ---------------------------------------
def mode_1_frequency(a):
    return special.jn_zeros(0, 1) * c / (2 * np.pi * a)

mode_1_frequency = mode_1_frequency(a)
print(f'Mode 1 frequency: {mode_1_frequency} [Hz]')

# ---------- Skin depth ---------------------------------------------
def skin_depth_func(frequency, kappa, mu):
    return np.sqrt(1 / (np.pi * frequency * mu * kappa))

skin_depth = skin_depth_func(mode_1_frequency, kappa, mu)
print(f'Skin depth of our cavity: {skin_depth}')

other_skin_depth = skin_depth_func(500000000, kappa, mu)
print(f'Skin depth from notes: {other_skin_depth}')

#f_vals = np.linspace(0, 1e10, 10)
#_depth_vals = skin_depth_func(f_vals, kappa, mu)
#plt.plot(f_vals, s_depth_vals)
#plt.xlabel('frequency')
#plt.ylabel('skin depth')
#plt.show()

# ---------- E_0 ----------------------------------------------------
def max_field(a, L):
    return np.sqrt(1/(epsilon * (a**2) * L * np.pi * (special.jv(1, special.jn_zeros(0,1))**2)))

E_0 = max_field(a, L)
print(f'Initial E field is: {E_0}')

# ---------- Total energy -------------------------------------------
def total_energy(E_0):
    return (epsilon/2) * (E_0**2) * (special.jv(1, special.jn_zeros(0,1))**2) * np.pi * (a**2) * L

U = total_energy(E_0)
print(f'Total energy is: {U}')

# ---------- Surface resistance -------------------------------------
def surface_resistance(kappa, skin_depth):
    return 1 / (kappa * skin_depth)

R_surf = surface_resistance(kappa, skin_depth)
print(f'Surface resistance: {R_surf}')

# ---------- Voltage ------------------------------------------------
def voltage(E_0, L):
    return E_0 * L

V_0 = voltage(E_0, L)
print(f'Voltage: {V_0} [V]')

# ---------- Dissapated power --------------------------------------
def dissapated_power(E_0, R_surf, a, L):
    return (E_0**2 * np.pi * R_surf * a * (special.jv(1, special.jn_zeros(0,1))**2) * (a + L)) / (Z_0**2)

P_d = dissapated_power(E_0, R_surf, a, L)
print(f'Dissapated power: {P_d} [W]')

# ---------- Transitive time ---------------------------------------
def transitive_time_factor(beta):
    return 2 / (np.pi * beta)

T = transitive_time_factor(beta)
print(f'Transitive time factor: {T}')

# ---------- Effective Voltage -------------------------------------
def effective_voltage(T, V_0):
    return V_0 * T

V_eff = effective_voltage(T, V_0)
print(f'Effective voltage: {V_eff} [V]')

# ---------- Q factor ----------------------------------------------
def Q_factor(skin_depth, L, a):
    return (1 / skin_depth) * ((L * a)/(L + a))

Q_0 = Q_factor(skin_depth, L, a)
print(f'Q-factor: {Q_0}')

# ---------- Shunt Impedance --------------------------------------
def eff_shunt_impedance(R_surf, T, a, L):
    return Z_0 / np.pi / R_surf / a / (a + L) / (special.jv(1, special.jn_zeros(0,1))**2) * L * (T**2)

R_eff = eff_shunt_impedance(R_surf, T, a, L)
print(f'Effective shunt-impedance: {R_eff}')

#L_vals = np.linspace(0, 200, 15)
#R_eff_vals = eff_shunt_impedance(R_surf, T, a, L_vals)
#plt.plot(L_vals, R_eff_vals)
#plt.xlabel('L')
#plt.ylabel('R_eff')
#plt.show()

def shunt_impedance(V_0, P_d):
    return V_0**2 / P_d

R_s = shunt_impedance(V_0, P_d)
print(f'Shunt-impedance: {R_s}')

# ---------- R/Q ---------------------------------------------------
def R_over_Q(T, L, a, frequency):
    return 2 * c / frequency / 2 / np.pi * T * L / (a**2)

R_Q = R_over_Q(T, L, a, mode_1_frequency)
print(f'R/Q: {R_Q}')


def dissapated_power_second_sol(frequency, U, Q_0):
    return frequency * np.pi / Q_0

other_P_d = dissapated_power_second_sol(mode_1_frequency, total_energy, Q_0)
print(f'Dissapated power is also: {other_P_d} [W]')

