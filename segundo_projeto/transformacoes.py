import numpy as np

def transladar(vertices, tx, ty, tz):
    return [[v[0] + tx, v[1] + ty, v[2] + tz] for v in vertices]

def escalar(vertices, sx, sy, sz):
    return [[v[0] * sx, v[1] * sy, v[2] * sz] for v in vertices]

def rotacionar(vertices, angulo, eixo):
    # Implementação de rotação em torno de um eixo arbitrário
    # Exemplo para rotação em torno do eixo Z
    c, s = np.cos(np.radians(angulo)), np.sin(np.radians(angulo))
    if eixo == 'z':
        matriz_rotacao = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
    # Outros eixos...
    return [np.dot(matriz_rotacao, v) for v in vertices]

def perspectiva(vertices, matriz_projecao):
    vertices_proj = []
    for v in vertices:
        v_homog = np.array([v[0], v[1], v[2], 1.0])
        v_proj = np.dot(matriz_projecao, v_homog)
        v_proj /= v_proj[3]
        vertices_proj.append([v_proj[0], v_proj[1]])
    return vertices_proj
