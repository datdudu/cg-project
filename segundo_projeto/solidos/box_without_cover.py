import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def scale_matrix(scale_x, scale_y, scale_z):
    """ Cria uma matriz de escala 3D. """
    return np.array([
        [scale_x, 0, 0, 0],
        [0, scale_y, 0, 0],
        [0, 0, scale_z, 0],
        [0, 0, 0, 1]
    ])

def apply_transformation(vertices, matrix):
    """ Aplica a matriz de transformação aos vértices. """
    vertices_homogeneous = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    transformed_vertices = vertices_homogeneous @ matrix.T
    return transformed_vertices[:, :-1]

def plot_solid_filled(ax, vertices, faces, cor='brown'):
    """ Desenha os objetos 3D com faces pintadas. """
    poly3d = [[vertices[vertice] for vertice in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=cor, linewidths=2, edgecolors='k', alpha=0.7))

def caixa_madeira_sem_tampa(lado_externo, altura_externa, espessura_parede = 0.5):
    lado_interno = lado_externo - 2 * espessura_parede
    altura_interna = altura_externa - espessura_parede
    
    # Vértices da caixa externa (fechada embaixo e aberta em cima)
    vertices_externa = np.array([
        [0, 0, 0], 
        [lado_externo, 0, 0], 
        [lado_externo, lado_externo, 0], 
        [0, lado_externo, 0],  # Base
        [0, 0, altura_externa], 
        [lado_externo, 0, altura_externa], 
        [lado_externo, lado_externo, altura_externa], [0, lado_externo, altura_externa]  # Vértices superiores
    ])
    
    # Aplicar matriz de escala para criar a caixa interna
    scale_mat = scale_matrix((lado_interno / lado_externo), (lado_interno / lado_externo), (altura_externa / altura_externa))
    vertices_interna = apply_transformation(vertices_externa, scale_mat)
    
    # Ajustar a posição da caixa interna
    vertices_interna += np.array([espessura_parede, espessura_parede, 0])

    # Faces da caixa externa (sem a face superior)
    faces_externa = [
        [0, 1, 2, 3],  # Base
        [0, 1, 5, 4],  # Parede lateral
        [1, 2, 6, 5],  # Parede lateral
        [2, 3, 7, 6],  # Parede lateral
        [3, 0, 4, 7]   # Parede lateral
    ]
    
    # Faces da caixa interna (sem a face superior)
    faces_interna = [
        [0, 1, 2, 3],  # Base interna
        [0, 1, 5, 4],  # Parede lateral interna
        [1, 2, 6, 5],  # Parede lateral interna
        [2, 3, 7, 6],  # Parede lateral interna
        [3, 0, 4, 7]   # Parede lateral interna
    ]
    
    return np.array(vertices_externa), np.array(faces_externa), vertices_interna, np.array(faces_interna)

def desenhar_caixa():
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Caixa de madeira sem tampa
    lado_externo = 4
    altura_externa = 5
    espessura_parede = 0.2
    vertices_externa, faces_externa, vertices_interna, faces_interna = caixa_madeira_sem_tampa(lado_externo, altura_externa, espessura_parede)
    
    # Cores diferentes para cada face da caixa externa
    cores_externa = ['red', 'green', 'blue', 'orange', 'purple']
    
    # Desenha as faces da caixa externa com cores diferentes
    for i, face in enumerate(faces_externa):
        plot_solid_filled(ax, vertices_externa, [face], cor=cores_externa[i % len(cores_externa)])
    
    # Desenha a caixa interna em branco
    plot_solid_filled(ax, vertices_interna, faces_interna, cor='white')
    
    # Adicionar e pintar as faces laterais entre as caixas
    for i in range(4):
        # Faces laterais externas
        face_lateral_externa = [vertices_externa[i], vertices_externa[(i+1)%4], vertices_externa[(i+1)%4 + 4], vertices_externa[i + 4]]
        # Faces laterais internas
        face_lateral_interna = [vertices_interna[i], vertices_interna[(i+1)%4], vertices_interna[(i+1)%4 + 4], vertices_interna[i + 4]]
        # Faces laterais entre a caixa interna e externa
        face_lateral_entre = [vertices_externa[i], vertices_externa[(i+1)%4], vertices_interna[(i+1)%4], vertices_interna[i]]
        ax.add_collection3d(Poly3DCollection([face_lateral_entre], facecolors='black', linewidths=2, edgecolors='k', alpha=0.5))

    # Adicionando e pintando as faces superior e inferior
    face_superior_entre = [vertices_externa[4], vertices_externa[5], vertices_interna[5], vertices_interna[4]]
    face_inferior = [vertices_externa[0], vertices_externa[1], vertices_externa[2], vertices_externa[3]]
    ax.add_collection3d(Poly3DCollection([face_superior_entre], facecolors='black', linewidths=2, edgecolors='k', alpha=0.5))
    ax.add_collection3d(Poly3DCollection([face_inferior], facecolors='black', linewidths=2, edgecolors='k', alpha=0.5))
    
    # Configurações da plotagem
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([0, lado_externo])
    ax.set_ylim([0, lado_externo])
    ax.set_zlim([0, altura_externa])
    
    plt.show()

# Função para desenhar a cena com a caixa
desenhar_caixa()