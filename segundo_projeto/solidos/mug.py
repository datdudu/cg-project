import numpy as np
from hermite_curve import hermite
from pipe import create_pipe


def create_mug(height=1, radius=1, num_points_mug=20, handle_radius=0.1,
               num_points_handle=20, num_points_handle_circle=20):

    face_color = "#215b20"
    edge_color = "#52ed0a"

    # Definir os vértices da base e topo da caneca
    p0_bottom = np.array([0, 0, 0])
    p1_bottom = np.array([radius, 0, 0])

    arc_t1_bottom = [0, radius * 2, 0]
    arc_t2_bottom = [0, -radius * 2, 0]

    p0_top = np.array([0, 0, height])
    p1_top = np.array([radius, 0, height])

    arc_t1_top = [0, radius * 2, 0]
    arc_t2_top = [0, -radius * 2, 0]

    # Gerar os vértices da base maior
    base_vertices_bottom = []
    base_vertices_bottom += hermite(p0_bottom, arc_t1_bottom, p1_bottom, arc_t2_bottom, round(num_points_mug / 2))
    base_vertices_bottom += hermite(p0_bottom, arc_t2_bottom, p1_bottom, arc_t1_bottom, round(num_points_mug / 2))

    # Gerar os vértices da base menor (topo)
    base_vertices_top = []
    base_vertices_top += hermite(p0_top, arc_t1_top, p1_top, arc_t2_top, round(num_points_mug / 2))
    base_vertices_top += hermite(p0_top, arc_t2_top, p1_top, arc_t1_top, round(num_points_mug / 2))

    # Conectar os pontos correspondentes das duas bases para formar as laterais do cilindro
    mug_cylinder = []
    for i in range(len(base_vertices_bottom) - 1):
        if i == num_points_mug / 2 - 1:
            continue
        p1 = base_vertices_bottom[i]
        p2 = base_vertices_bottom[i + 1]
        p3 = base_vertices_top[i + 1]
        p4 = base_vertices_top[i]
        mug_cylinder.append([p1, p2, p3, p4])

    # Adicionar as duas bases
    mug_cylinder += [base_vertices_bottom]

    # Criar a alça da xícara usando a curva de Hermite, iniciando na borda
    p0_handler = np.array([radius, 0, height * 0.25])  # Começando na borda do cilindro
    p1_handler = np.array([radius, 0, height * 0.75])  # Terminando na borda no topo

    arc_t1_handler = [radius, 0, 0]  # Controle da curva da alça
    arc_t2_handler = [-radius, 0, 0]

    mug_cylinder += create_pipe(p0_handler, arc_t1_handler, p1_handler,
                                arc_t2_handler, num_points_handle, num_points_handle_circle, handle_radius)[0]

    return mug_cylinder, face_color, edge_color