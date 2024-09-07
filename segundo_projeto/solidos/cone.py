import numpy as np
from hermite_curve import hermite


def create_cone(height=1, radius=1, num_points=20):
    p0 = np.array([0, 0, 0])
    p1 = np.array([radius, 0, 0])
    arc_t1 = [0, radius * 2, 0]
    arc_t2 = [0, -radius * 2, 0]

    base_vertices = []

    base_vertices += hermite(p0, arc_t1, p1, arc_t2, round(num_points / 2))
    base_vertices += hermite(p0, arc_t2, p1, arc_t1, round(num_points / 2))

    # define o meio da base do cone e depois a altura
    vertex = [(p0[0] + p1[0]) / 2, p0[1], height]

    # Conectar cada ponto da base ao vértice para formar as laterais do cone
    cone = []
    for i in range(len(base_vertices)):
        # Obter o ponto atual e o próximo ponto (para criar uma face lateral)
        p1 = base_vertices[i]
        p2 = base_vertices[(i + 1) % len(base_vertices)]  # O próximo ponto, ou o primeiro se for o último ponto
        # Criar um triângulo que conecta p1, p2 e o vértice
        cone.append([p1, p2, vertex])

    cone += [base_vertices]
    face_color = "#190681"
    edge_color = "#ff5800"

    return cone, face_color, edge_color