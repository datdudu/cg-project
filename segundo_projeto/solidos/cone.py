import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def cone(raio, altura, num_lados=20):
    # Definir vértices da base
    theta = np.linspace(0, 2*np.pi, num_lados)
    base = np.array([[raio * np.cos(t), raio * np.sin(t), 0] for t in theta])
    
    # Vértice superior
    topo = np.array([0, 0, altura])
    
    # Base do cone
    faces = [[base[j], base[(j + 1) % num_lados], topo] for j in range(num_lados)]
    
    return np.vstack((base, topo)), faces

def plot_cone(raio, altura):
    vertices, faces = cone(raio, altura)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotar faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors='gold', linewidths=1, edgecolors='r', alpha=.5))
    
    # Ajustar limites dos eixos
    ax.set_xlim([-raio, raio])
    ax.set_ylim([-raio, raio])
    ax.set_zlim([0, altura])
    
    plt.show()

# Teste da função
plot_cone(3, 5)
