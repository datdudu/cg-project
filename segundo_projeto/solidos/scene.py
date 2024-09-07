import numpy as np
import matplotlib.pyplot as plt
from mug import create_mug
from cone import cone
from cone_trunk import tronco_de_cone
from pipe import pipe
from box_without_cover import caixa_madeira_sem_tampa
from mug import create_mug

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Funções de transformação e plotagem (definidas conforme os sólidos anteriores)

def transladar(vertices, dx, dy, dz):
    """Aplica uma translação nos vértices."""
    matriz_translacao = np.array([dx, dy, dz])
    return vertices + matriz_translacao

def escalar(vertices, sx, sy, sz):
    """Aplica uma escala nos vértices."""
    matriz_escala = np.array([sx, sy, sz])
    return vertices * matriz_escala

def rotacionar(vertices, eixo, angulo):
    """Aplica uma rotação nos vértices em torno de um eixo."""
    rad = np.deg2rad(angulo)
    if eixo == 'x':
        matriz_rotacao = np.array([[1, 0, 0], [0, np.cos(rad), -np.sin(rad)], [0, np.sin(rad), np.cos(rad)]])
    elif eixo == 'y':
        matriz_rotacao = np.array([[np.cos(rad), 0, np.sin(rad)], [0, 1, 0], [-np.sin(rad), 0, np.cos(rad)]])
    elif eixo == 'z':
        matriz_rotacao = np.array([[np.cos(rad), -np.sin(rad), 0], [np.sin(rad), np.cos(rad), 0], [0, 0, 1]])
    return np.dot(vertices, matriz_rotacao)

# Reuso das funções de geração dos sólidos
# Caneca, Cone, Tronco de Cone, Cano, Caixa sem Tampa

# Para fins de composição:
def plotar_cena():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # --- Transforma e plota a Caneca ---
    caneca = create_mug()
    caneca = [transladar(np.array(face), 6, 6, 0) for face in caneca]  # Transladando para o 1º octante
    for face in caneca:
        ax.add_collection3d(Poly3DCollection([face], facecolors='r', linewidths=1, edgecolors='cyan', alpha=.5))

    # --- Transforma e plota o Cone ---
    _, faces_cone = cone(2, 4)
    faces_cone = [transladar(np.array(face), -6, 6, 0) for face in faces_cone]  # Transladando para o 2º octante
    for face in faces_cone:
        ax.add_collection3d(Poly3DCollection([face], facecolors='gold', linewidths=1, edgecolors='r', alpha=.5))

    # --- Transforma e plota o Tronco de Cone ---
    _, faces_tronco_cone = tronco_de_cone(3, 1.5, 4)
    faces_tronco_cone = [transladar(np.array(face), 6, -6, 0) for face in faces_tronco_cone]  # Transladando para o 3º octante
    for face in faces_tronco_cone:
        ax.add_collection3d(Poly3DCollection([face], facecolors='orange', linewidths=1, edgecolors='r', alpha=.5))

    # --- Transforma e plota o Cano ---
    _, faces_cano = pipe(0.5, np.array([0, 0, 0]), np.array([3, 3, 3]), np.array([1, 2, 1]), np.array([1, -1, 2]))
    faces_cano = [transladar(np.array(face), -6, -6, 0) for face in faces_cano]  # Transladando para o 4º octante
    for face in faces_cano:
        ax.add_collection3d(Poly3DCollection([face], facecolors='blue', linewidths=1, edgecolors='r', alpha=.5))

    # --- Transforma e plota a Caixa ---
    vertices_externa, faces_externa, vertices_interna, faces_interna = caixa_madeira_sem_tampa(4, 5, 0.2)
    vertices_externa = transladar(vertices_externa, 0, 0, 5)
    for face in faces_externa:
        ax.add_collection3d(Poly3DCollection([vertices_externa[face]], facecolors='brown', linewidths=1, edgecolors='black', alpha=.7))

    # Definir o sistema de coordenadas
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([0, 10])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Executa a função para plotar a cena
plotar_cena()
