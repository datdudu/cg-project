import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def tronco_de_cone(raio_base_inferior, raio_base_superior, altura, num_lados=20):
    # Definir vértices das bases
    theta = np.linspace(0, 2*np.pi, num_lados)
    base_inferior = np.array([[raio_base_inferior * np.cos(t), raio_base_inferior * np.sin(t), 0] for t in theta])
    base_superior = np.array([[raio_base_superior * np.cos(t), raio_base_superior * np.sin(t), altura] for t in theta])
    
    # Faces laterais
    faces = [[base_inferior[j], base_inferior[(j + 1) % num_lados], base_superior[(j + 1) % num_lados], base_superior[j]] for j in range(num_lados)]
    
    # Faces das bases
    faces.append(base_inferior)
    faces.append(base_superior)
    
    return np.vstack((base_inferior, base_superior)), faces

def plot_tronco_de_cone(raio_base_inferior, raio_base_superior, altura):
    vertices, faces = tronco_de_cone(raio_base_inferior, raio_base_superior, altura)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotar faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors='orange', linewidths=1, edgecolors='r', alpha=.5))
    
    # Ajustar limites dos eixos
    ax.set_xlim([-raio_base_inferior, raio_base_inferior])
    ax.set_ylim([-raio_base_inferior, raio_base_inferior])
    ax.set_zlim([0, altura])
    
    plt.show()

# Teste da função
plot_tronco_de_cone(3, 1.5, 5)
