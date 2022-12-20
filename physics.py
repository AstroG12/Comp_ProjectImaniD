import numpy as np
import matplotlib.pyplot as plt
from gas import *
from celluloid import Camera

np.random.seed(69420)
m_h = 1.67356 * 1e-27
solar_mass = 1.9891 # * 1e30


def Model(N_gas, time=100):
    """
    This is 2D model. For these first few test I'm using random #s
    [-50, 50]
    """

    # Creating BH position(0, 1), velocity(2,3), and mass(4)
    pos_bh = (np.random.random((1, 2)) * 100) - 50
    veloc_bh = np.zeros((1, 2))
    mass_bh = np.array([5 * solar_mass]).reshape(1, 1)
    # The black hole
    bh = np.concatenate((pos_bh, veloc_bh, mass_bh), axis=1)

    # Some problem set-up
    R_s = Bondi_R(bh[0][4])
    rho = 1e6 * m_h / ((10 * R_s) ** 2)
    mass_part = ((10 * R_s) ** 2) * rho / N_gas
    # This creates the particles' intial positions, velocities
    # and masses
    index = np.arange(N_gas, dtype=int).reshape(N_gas, 1)
    pos_part = (np.random.random((N_gas, 2)) * 100 ) - 50
    velocity = (np.random.random((N_gas, 2)) * 5) - 2
    masses = np.full((N_gas, 1), mass_part)
    # The particles
    particles = np.concatenate((pos_part, velocity, masses, index), axis=1)

    # Time passing and adding actual physics starting with gravity
    t_points = np.arange(1, time, 1)

    # Adding physics
    M_acc = 0
    # fig = plt.figure()
    # cam = Camera(fig)
    for t in t_points:
        r = bh[:, 0:2] - particles[:, 0:2]
        # if len(r) == 0:
        #     break
        rho_time_loss = rho
        if (M_acc >= mass_part) & (np.any(r <= R_s)):
            r = np.sqrt((r[:, 0] ** 2) + (r[:, 1] ** 2))
            dex = np.where(r == r.min())[0][0]
            bh[0][4] += mass_part
            particles = np.delete(particles, dex, 0)
            rho_time_loss -= m_h / ((10 * R_s) ** 2)
            M_acc = 0
        M_acc += Bondi_acc(rho_time_loss, bh[0][4]) * t
        plt.scatter(particles[:, 0], particles[:, 1], color="grey")
        plt.scatter(bh[:, 0], bh[:, 1], color="k")
        # cam.snap()
        # plt.scatter(t, bh[0][4])
        # This section updates position and velocity
        a = Force_g(particles, bh, t)
        particles[:, 0:2] += (a * (t ** 2) * 0.5) + \
            particles[:, 0:2]
        particles[:, 2:4] += a * t
    # animate = cam.animate()
        # print(particles[:, 0:2])
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        print(len(particles))
        plt.show()
Model(10)