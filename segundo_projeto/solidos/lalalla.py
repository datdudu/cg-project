import numpy as np
import matplotlib.pyplot as plt
from mug import create_mug
from cone import cone
from cone_trunk import tronco_de_cone
from pipe import pipe
from box_without_cover import caixa_madeira_sem_tampa
from mug import create_mug
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Função para verificar e ajustar a escala dos vértices e arestas
def ajustar_escala(vertices, arestas):
    max_valor = np.max(np.abs(vertices))
    if max_valor > 10:
        escala = 10 / max_valor
        vertices *= escala
        # Também escalamos as arestas
        arestas = [[tuple(np.array(ponto) * escala) for ponto in aresta] for aresta in arestas]
    return vertices, arestas

# Função para aplicar transformações nos vértices e arestas
def aplicar_transformacao(vertices, arestas, escala=None, rotacao=None, translacao=None):
    if escala is not None:
        vertices = vertices * escala
    if rotacao is not None:
        vertices = vertices.dot(rotacao)
    if translacao is not None:
        vertices = vertices + translacao

    arestas_transformadas = []
    for aresta in arestas:
        aresta_transformada = [(np.array(ponto) * escala if escala is not None else ponto) for ponto in aresta]
        aresta_transformada = [(np.dot(ponto, rotacao) if rotacao is not None else ponto) for ponto in aresta_transformada]
        aresta_transformada = [(ponto + translacao if translacao is not None else ponto) for ponto in aresta_transformada]
        arestas_transformadas.append(aresta_transformada)

    return vertices, arestas_transformadas

# Criando os sólidos
vertices_caixa, faces_caixa = caixa_madeira_sem_tampa(10, 8)
vertices_cone, faces_cone = cone(50, 25)
vertices_tronco_cone, faces_tronco_cone = tronco_de_cone(5, 3, 10)
P1 = np.array([0, 0, 0])
P2 = np.array([10, 0, 5])
T1 = np.array([0, 10, 0])
T2 = np.array([0, -10, 0])
vertices_cano, faces_cano = pipe(1, [P1, P2, T1, T2])
vertices_caneca, faces_caneca = create_mug(100, 200, 50)

# Ajustando a escala dos vértices e arestas para garantir que nenhum componente seja maior que 10
vertices_caixa, faces_caixa = ajustar_escala(vertices_caixa, faces_caixa)
vertices_cone, faces_cone = ajustar_escala(vertices_cone, faces_cone)
vertices_tronco_cone, faces_tronco_cone = ajustar_escala(vertices_tronco_cone, faces_tronco_cone)
vertices_cano, faces_cano = ajustar_escala(vertices_cano, faces_cano)
vertices_caneca, faces_caneca = ajustar_escala(vertices_caneca, faces_caneca)

# Ajustando transformações para evitar sobreposição
escala_cone_cano = 0.3
translacao_cone = np.array([7, 6, 2])
translacao_cano = np.array([3, 4, 4])
vertices_cone, faces_cone = aplicar_transformacao(vertices_cone, faces_cone, escala=escala_cone_cano, translacao=translacao_cone)
vertices_cano, faces_cano = aplicar_transformacao(vertices_cano, faces_cano, escala=escala_cone_cano, translacao=translacao_cano)

escala_tronco_caneca = 0.3
translacao_tronco = np.array([-8, -8, -8])
translacao_caneca = np.array([-6, -8, -4])
vertices_tronco_cone, faces_tronco_cone = aplicar_transformacao(vertices_tronco_cone, faces_tronco_cone, escala=escala_tronco_caneca, translacao=translacao_tronco)
vertices_caneca, faces_caneca = aplicar_transformacao(vertices_caneca, faces_caneca, escala=escala_tronco_caneca, translacao=translacao_caneca)

# Função para desenhar os planos de separação dos octantes
def desenhar_planos(ax):
    # Plano XY
    x = np.linspace(-10, 10, 2)
    y = np.linspace(-10, 10, 2)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros(X.shape)
    ax.plot_surface(X, Y, Z, color='gray', alpha=0.3)

    # Plano YZ
    y = np.linspace(-10, 10, 2)
    z = np.linspace(-10, 10, 2)
    Y, Z = np.meshgrid(y, z)
    X = np.zeros(Y.shape)
    ax.plot_surface(X, Y, Z, color='gray', alpha=0.3)

    # Plano ZX
    z = np.linspace(-10, 10, 2)
    x = np.linspace(-10, 10, 2)
    Z, X = np.meshgrid(z, x)
    Y = np.zeros(Z.shape)
    ax.plot_surface(X, Y, Z, color='gray', alpha=0.3)

# Visualizando todos os sólidos na mesma cena
def visualizar_cena():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Adicionar planos de separação dos octantes
    desenhar_planos(ax)

    # Função auxiliar para adicionar um sólido
    def adicionar_solido(vertices, faces, cor='green'):
        for face in faces:
            if len(face) == 2:
                ax.plot3D(*zip(*face), color=cor)
            else:
                poly3d = [[tuple(vertex) for vertex in face]]
                ax.add_collection3d(Poly3DCollection(poly3d, color=cor, linewidths=1, edgecolors=cor, alpha=.25))

    # Adicionar sólidos à cena
    adicionar_solido(vertices_cone, faces_cone, cor='blue')
    adicionar_solido(vertices_cano, faces_cano, cor='red')
    adicionar_solido(vertices_tronco_cone, faces_tronco_cone, cor='orange')
    adicionar_solido(vertices_caneca, faces_caneca, cor='purple')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    plt.show()
