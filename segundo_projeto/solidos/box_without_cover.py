import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def caixa_sem_tampa(lado, altura):
    # Definir os vértices da caixa
    vertices = np.array([[0, 0, 0], [lado, 0, 0], [lado, lado, 0], [0, lado, 0],
                         [0, 0, altura], [lado, 0, altura], [lado, lado, altura], [0, lado, altura]])
    
    # Definir as faces (base e laterais)
    faces = [[vertices[j] for j in [0, 1, 2, 3]],  # Base inferior
             [vertices[j] for j in [0, 1, 5, 4]],  # Lateral 1
             [vertices[j] for j in [1, 2, 6, 5]],  # Lateral 2
             [vertices[j] for j in [2, 3, 7, 6]],  # Lateral 3
             [vertices[j] for j in [3, 0, 4, 7]]]  # Lateral 4
    
    return vertices, faces

def plot_caixa_sem_tampa(lado, altura):
    vertices, faces = caixa_sem_tampa(lado, altura)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotar faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors='saddlebrown', linewidths=1, edgecolors='r', alpha=.25))
    
    # Ajustar limites dos eixos
    ax.set_xlim([0, lado])
    ax.set_ylim([0, lado])
    ax.set_zlim([0, altura])
    
    plt.show()

# Teste da função
plot_caixa_sem_tampa(3, 2)