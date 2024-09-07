import numpy as np

def hermite(P0, T0, P1, T1, num_points):
    vertices = []
    for t in np.linspace(0, 1, num_points):
        h1 = 2 * t ** 3 - 3 * t ** 2 + 1  # P0
        h2 = t ** 3 - 2 * t ** 2 + t  # T0
        h3 = -2 * t ** 3 + 3 * t ** 2  # P1
        h4 = t ** 3 - t ** 2  # T1

        x = h1 * P0[0] + h2 * T0[0] + h3 * P1[0] + h4 * T1[0]
        y = h1 * P0[1] + h2 * T0[1] + h3 * P1[1] + h4 * T1[1]
        z = h1 * P0[2] + h2 * T0[2] + h3 * P1[2] + h4 * T1[2]

        vertices.append([x, y, z])

    return vertices