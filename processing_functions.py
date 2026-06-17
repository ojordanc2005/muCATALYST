import numpy as np
from scipy import special

# physical constants
c = 3e8
epsilon = 8.8e-12
mu = 1.3e-6
Z_0 = np.sqrt(mu / epsilon)

# cavity parameters
a = 0.14265 # in mm
L = 0.100 # in mm
beta = 0.9
kappa = 58.0e6 # for copper, in S/m

# ---------- Time-independent E - field ------------------------------
# ---------- E - field -----------------------------------------------
def E_field(E_0, a, r, f, t):
    return E_0 * special.jv(0, ((special.jn_zeros(0, 1) / a * r))) * np.cos(t * 2 * np.pi * f)

# ---------- Time-independent H - field ------------------------------
# ---------- H - field -----------------------------------------------


# ---------- Mode 1 frequency ---------------------------------------
def mode_1_frequency(a):
    return special.jn_zeros(0, 1) * c / (2 * np.pi * a)


# ---------- Skin depth ---------------------------------------------
def skin_depth_func(frequency, kappa, mu):
    return np.sqrt(1 / (np.pi * frequency * mu * kappa))


# ---------- E_0 ----------------------------------------------------
def max_field(a, L):
    return np.sqrt(2 * 1/(epsilon * (a**2) * L * np.pi * (special.jv(1, special.jn_zeros(0,1)))**2))
    #return np.sqrt(2 * 0.997/(epsilon * (a**2) * L * np.pi * (special.jv(1, special.jn_zeros(0,1)))**2))


# ---------- Total energy -------------------------------------------
def total_energy(E_0):
    return (epsilon/2) * (E_0**2) * (special.jv(1, special.jn_zeros(0,1))**2) * np.pi * (a**2) * L


# ---------- Surface resistance -------------------------------------
def surface_resistance(kappa, skin_depth):
    return 1 / (kappa * skin_depth)


# ---------- Voltage ------------------------------------------------
def voltage(E_0, L):
    return E_0 * L


# ---------- Transitive time ---------------------------------------
def transitive_time_factor(frequency, L, beta):
    x = np.pi * L / beta / (c / frequency)
    return np.sin(x) / x

# ---------- Effective Voltage -------------------------------------
def effective_voltage(T, V_0):
    return V_0 * T


# ---------- Dissapated power --------------------------------------
def dissapated_power(E_0, R_surf, a, L):
    return (E_0**2 * np.pi * R_surf * a * (special.jv(1, special.jn_zeros(0,1))**2) * (a + L)) / (Z_0**2)


def also_dissapated_power(frequency, energy, Q_0):
    return frequency * 2 * np.pi * energy / Q_0


# ---------- Q factor ----------------------------------------------
def Q_factor(skin_depth, L, a):
    return (1 / skin_depth) * ((L * a)/(L + a))


def Q_factor_also(L, a, R_surf, frequency):
    return (Z_0**2 * np.pi * frequency * L * a * epsilon) / (R_surf * (L + a))


def Q_factor_also_also(skin_depth, L, a):
    return (1 / skin_depth) * ((L * a) / (L + a))


# ---------- Shunt Impedance --------------------------------------
#big formula
def eff_shunt_impedance(R_surf, T, a, L):
    #return Z_0 / np.pi / R_surf / a / (a + L) / (special.jv(1, special.jn_zeros(0,1))**2) * L * (T**2)
    return ((Z_0**2) * (T**2) * (L))/(np.pi * R_surf * (special.jv(1, special.jn_zeros(0,1))**2) * a * (a + L))


def eff_R_s_also(voltage, T, P_d):
    return ((voltage * T)**2) / P_d


# ---------- R/Q ---------------------------------------------------
def R_over_Q(T, L, a, frequency):
    #return 2 * c / frequency / 2 / np.pi * T * L / (a**2)
    return (2 * c * T * L)/(frequency * 2 * np.pi * np.pi * (a**2) * (special.jv(1, special.jn_zeros(0,1))**2))

def maybe_R_over_Q(V_0, T, f, U):
    return ((V_0 * T)**2) / (f * 2 * np.pi * U)