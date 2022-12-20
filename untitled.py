import numpy as np
from gas import *
import matplotlib.pyplot as plt
from celluloid import Camera

np.random.seed(69420)
# a = np.array(([1,2,3], [4,5,6]))
# b = np.array(([1,2,3]))
# c = np.random.random((15,4))
# print(c[0:len(c), 0:2])
# print(a / b)
# np.random.seed(69420)
# pos_part = (np.random.random((4, 2)) * 100) - 50
# velocit = (np.random.random((4, 2)) * 10) - 5
# masses = (np.random.random((4, 1)) * 50) + 50
# # The hi
# hi = np.concatenate((pos_part, velocit, masses), axis=1)

# # Creating BH position(0, 1), velocity(2), and mass(3)
# pos_bh = (np.random.random((1, 2)) * 100) - 50
# veloc_bh = (np.random.random((1, 2)) * 10) - 5
# mass_bh = (np.random.random((1, 1)) * 1000) + 500
# # The black hole
# bh = np.concatenate((pos_bh, veloc_bh, mass_bh), axis=1)

# x = np.random.random((1, 5))
# y = np.random.random((1, 5))
# fig = plt.figure()
# cam = Camera(fig)
# for t in range(100):
#     plt.scatter(x, y, color="grey")
#     cam.snap()
#     x += np.random.random((1, 5))
#     y += np.random.random((1, 5))
# animate = cam.animate()
# plt.show()

t_points = np.arange(1, 100, 1)
print(t_points)
