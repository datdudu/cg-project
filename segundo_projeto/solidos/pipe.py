import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def hermite_curve(P1, P2, T1, T2, t):
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = -2*t**3 + 3*t**2
    h3 = t**3 - 2*t**2 + t
    h4 = t**3 - t**2
    return h1*P1 + h2*P2 + h3*T1 + h4*T2

def cano(raio, P1, P2, T1, T2, num_pontos=20, num_lados=20):
    t_values = np.linspace(0, 1, num_pontos)
    centers = np.array([hermite_curve(P1, P2, T1, T2, t) for t in t_values])
    
    theta = np.linspace(0, 2*np.pi, num_lados)
    circulos = []
    for center in centers:
        circle = np.array([[center[0] + raio*np.cos(t), center[1] + raio*np.sin(t), center[2]] for t in theta])
        circulos.append(circle)
    
    vertices = np.vstack(circulos)
    
    # Conectando os círculos para formar o cano
    faces = []
    for i in range(num_pontos - 1):
        for j in range(num_lados):
            next_j = (j + 1) % num_lados
            faces.append([circulos[i][j], circulos[i][next_j], circulos[i+1][next_j], circulos[i+1][j]])
    
    return vertices, faces

def plot_cano(raio, P1, P2, T1, T2):
    vertices, faces = cano(raio, P1, P2, T1, T2)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plotar faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors='blue', linewidths=1, edgecolors='r', alpha=.5))
    
    plt.show()

# Teste da função
P1 = np.array([0, 0, 0])
P2 = np.array([5, 5, 5])
T1 = np.array([1, 2, 1])
T2 = np.array([1, -1, 2])
plot_cano(1, P1, P2, T1, T2)