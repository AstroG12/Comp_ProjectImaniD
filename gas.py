import numpy as np
from astropy.constants import G, c


c_s = 343  # m / s


def Force_g(particles, bh, t):
    """
    particles is an N x 4 (0-x, 1-y, 2-vx, 3-vy, 4-m)
    bh is N x 1
    This is specifically for my project.
    This finds the force between particles and bh
    """
    r = bh[:, 0:2] - particles[0:len(particles), 0:2]
    mod = (r[:, 0]**2 + r[:, 1]**2) ** 1.5
    Fx = - G.value * r[:, 0] * particles[:, 4] * bh[:, 4] / mod
    Fy = - G.value * r[:, 1] * particles[:, 4] * bh[:, 4] / mod
    ax = Fx / particles[:, 4]
    ay = Fy / particles[:, 4]
    a = np.concatenate((ax.reshape(len(particles), 1),
                        ay.reshape(len(particles), 1)), axis=1)
    return(a)


def E_orbit(particles, bh):
    """
    This will be used to calculate the Energy of a particles
    orbit...
    """
    r_com = bh[:, 0:2] - particles[0:len(particles), 0:2]
    r = (r_com[:, 0]**2 + r_com[:, 1]**2) ** 0.5
    E = - G.value * bh[:, 4] * particles[:, 4] / r
    return(E)


def Bondi_acc(rho, M):
    """
    This is the code for Bondi accretion
    """
    M_dot = np.pi * rho * (G.value ** 2) * (M ** 2) / c_s
    return(M_dot)


def Schwarz_radius(M):
    """
    Calculates schwarzschild radius
    """
    r_s = 2 * G.value * M / (c.value ** 2)
    return(r_s)


def Bondi_R(M):
    """
    Finds bondi radius for given mass
    """
    R = 2 * G.value * M / (5 ** 2)
    return(R)
