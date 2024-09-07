from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def projection_2d(points, axis='xy'):
    #Projeta os pontos 3D para 2D conforme o eixo escolhido.
    projected_points = []
    for point in points:
        x, y, z = point[:3]
        if axis == 'xy':
            projected_points.append([x, y])  # Descartar z
        elif axis == 'xz':
            projected_points.append([x, z])  # Descartar y
        elif axis == 'yz':
            projected_points.append([y, z])  # Descartar x
    return projected_points


def plot_2d(ax, faces, face_color='r', edge_color='black', axis='xy'):
    """ Preenche as faces projetadas em 2D com a cor especificada. """
    for face in faces:
        # Projeta os vértices da face para o plano 2D
        projected_face = projection_2d(face, axis=axis)

        # Verifica se a face tem pelo menos 3 pontos para preencher
        if len(projected_face) < 3:
            continue

        # Separa os valores de x e y
        x_vals = [p[0] for p in projected_face]
        y_vals = [p[1] for p in projected_face]

        # Preenche a face no 2D com a cor especificada
        ax.fill(x_vals, y_vals, color=face_color, edgecolor=edge_color, alpha=0.6)


def plot_3d(ax, faces, f_color='r', e_color="cyan", alpha=.5):
    ax.add_collection3d(Poly3DCollection(faces, facecolors=f_color, linewidths=1, edgecolors=e_color, alpha=alpha))