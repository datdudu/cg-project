import numpy as np

def calcular_centro_massa(vertices):
    x = sum(v[0] for v in vertices) / len(vertices)
    y = sum(v[1] for v in vertices) / len(vertices)
    z = sum(v[2] for v in vertices) / len(vertices)
    return [x, y, z]

def base_camera(origem_camera, ponto_medio):
    z_c = np.array(origem_camera) - np.array(ponto_medio)
    z_c = z_c / np.linalg.norm(z_c)

    y_mundo = np.array([0, 1, 0])
    x_c = np.cross(y_mundo, z_c)
    x_c = x_c / np.linalg.norm(x_c)

    y_c = np.cross(z_c, x_c)
    return np.array([x_c, y_c, z_c])

def transformar_para_camera(vertices, origem_camera, matriz_camera):
    return [np.dot(matriz_camera, np.array(v) - np.array(origem_camera)) for v in vertices]
