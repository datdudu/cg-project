import numpy as np
from hermite_curve import hermite


def create_cone_trunk(height=1, bottom_radius=1, top_radius=0.5, num_points=20):

    face_color = "red"
    edge_color = "cyan"

    p0_bottom = np.array([0, 0, 0])
    p1_bottom = np.array([bottom_radius, 0, 0])

    arc_t1_bottom = [0, bottom_radius * 2, 0]
    arc_t2_bottom = [0, -bottom_radius * 2, 0]

    space_around = (bottom_radius - top_radius) / 2

    p0_top = np.array([space_around, 0, height])
    p1_top = np.array([space_around + top_radius, 0, height])

    arc_t1_top = [0, top_radius * 2, 0]
    arc_t2_top = [0, -top_radius * 2, 0]

    # Gerar os vértices da base maior
    base_vertices_bottom = []
    base_vertices_bottom += hermite(p0_bottom, arc_t1_bottom, p1_bottom, arc_t2_bottom, round(num_points / 2))
    base_vertices_bottom += hermite(p0_bottom, arc_t2_bottom, p1_bottom, arc_t1_bottom, round(num_points / 2))

    # Gerar os vértices da base menor (topo)
    base_vertices_top = []
    base_vertices_top += hermite(p0_top, arc_t1_top, p1_top, arc_t2_top, round(num_points / 2))
    base_vertices_top += hermite(p0_top, arc_t2_top, p1_top, arc_t1_top, round(num_points / 2))

    # Conectar os pontos correspondentes das duas bases para formar as laterais do tronco
    cone_trunk = []
    for i in range(len(base_vertices_bottom)):
        if i == num_points / 2 - 1:
            continue
        p1 = base_vertices_bottom[i]
        p2 = base_vertices_bottom[(i + 1) % len(base_vertices_bottom)]
        p3 = base_vertices_top[(i + 1) % len(base_vertices_top)]
        p4 = base_vertices_top[i]
        cone_trunk.append([p1, p2, p3, p4])

    # Adicionar as duas bases
    cone_trunk += [base_vertices_bottom]
    cone_trunk += [base_vertices_top]

    return cone_trunk, face_color, edge_color