import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def hermite(p0, t0, p1, t1, num_segmentos):
    vertices = []
    for t in np.linspace(0, 1, num_segmentos):
        h1 = 2 * t ** 3 - 3 * t ** 2 + 1  # P0
        h2 = t ** 3 - 2 * t ** 2 + t  # T0
        h3 = -2 * t ** 3 + 3 * t ** 2  # P1
        h4 = t ** 3 - t ** 2  # T1

        x = h1 * p0[0] + h2 * t0[0] + h3 * p1[0] + h4 * t1[0]
        y = h1 * p0[1] + h2 * t0[1] + h3 * p1[1] + h4 * t1[1]
        z = h1 * p0[2] + h2 * t0[2] + h3 * p1[2] + h4 * t1[2]

        vertices.append([x, y, z])

    return vertices

def generate_circle(center, tangent, radius):
    # Gerar um círculo no plano perpendicular à tangente
    theta = np.linspace(0, 2 * np.pi, 10)
    v = np.cross(tangent, [0, 0, 1])
    if np.linalg.norm(v) == 0:
        v = np.cross(tangent, [0, 1, 0])
    v /= np.linalg.norm(v)
    u = np.cross(tangent, v)
    u /= np.linalg.norm(u)
    circle = np.array([center + radius * (np.cos(t) * u + np.sin(t) * v) for t in theta])
    return circle

def create_mug(height=1, radius=1, num_points=20, handle_radius=0.1):
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
    base_vertices_bottom += hermite(p0_bottom, arc_t1_bottom, p1_bottom, arc_t2_bottom, round(num_points / 2))
    base_vertices_bottom += hermite(p0_bottom, arc_t2_bottom, p1_bottom, arc_t1_bottom, round(num_points / 2))

    # Gerar os vértices da base menor (topo)
    base_vertices_top = []
    base_vertices_top += hermite(p0_top, arc_t1_top, p1_top, arc_t2_top, round(num_points / 2))
    base_vertices_top += hermite(p0_top, arc_t2_top, p1_top, arc_t1_top, round(num_points / 2))

    # Conectar os pontos correspondentes das duas bases para formar as laterais do cilindro
    mug_cylinder = []
    for i in range(len(base_vertices_bottom) - 1):
        if i == num_points // 2 - 1:
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

    arc_t1_handler = [radius * 1.5, 0, 0]  # Controle da curva da alça
    arc_t2_handler = [-radius * 1.5, 0, 0]

    # Gerar pontos da curva de Hermite da alça
    p = hermite(p0_handler, arc_t1_handler, p1_handler, arc_t2_handler, round(num_points))

    # Gerar círculos ao longo da curva da alça
    handle_circles = []
    previous_circle = None
    for i in range(len(p)):
        if i < len(p) - 1:
            tangent = np.array(p[i + 1]) - np.array(p[i])
        else:
            tangent = np.array(p[i]) - np.array(p[i - 1])
        tangent /= np.linalg.norm(tangent)

        # Gerar o círculo usando o ponto atual e a tangente
        circle = generate_circle(np.array(p[i]), tangent, radius=handle_radius)

        # Conectar o círculo anterior ao atual, se houver
        if previous_circle is not None:
            for j in range(len(circle) - 1):
                mug_cylinder.append([previous_circle[j], previous_circle[j + 1], circle[j + 1], circle[j]])
        previous_circle = circle

    return mug_cylinder


def plot_mug(ax, faces):
    ax.add_collection3d(Poly3DCollection(faces, facecolors='r', linewidths=1, edgecolors='cyan', alpha=.5))

def define_world(ax):
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
define_world(ax)

cot1 = create_mug()
plot_mug(ax, cot1)

plt.show()