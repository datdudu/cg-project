import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from solidos import *
from transformacoes import *
from camera import *

def desenhar_solid_3d(ax, vertices, arestas, cor):
    for aresta in arestas:
        p1 = vertices[aresta[0]]
        p2 = vertices[aresta[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color=cor)

def desenhar_solid_2d(ax, vertices, arestas, cor):
    for aresta in arestas:
        p1 = vertices[aresta[0]]
        p2 = vertices[aresta[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=cor)

def main():
    # Modelagem dos sólidos
    vertices_caixa, arestas_caixa = criar_caixa(2, 3)
    vertices_cone, arestas_cone = criar_cone(1, 3)
    vertices_tronco_cone, arestas_tronco_cone = criar_tronco_cone(1, 0.5, 3)
    vertices_cano, arestas_cano = criar_cano([0, 0, 0], [5, 5, 5], [1, 1, 1], [1, 1, 1], 1)
    vertices_caneca, arestas_caneca = criar_caneca(1, 3, 0.5)
    
    # Transformações e composição da cena
    vertices_caixa = transladar(escalar(vertices_caixa, 1, 1, 1), 5, 5, 5)
    vertices_cone = transladar(rotacionar(vertices_cone, 45, 'z'), 7, 8, 2)
    # Transformações para os outros sólidos...
    
    # Renderização em 3D antes da transformação para a câmera
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    desenhar_solid_3d(ax, vertices_caixa, arestas_caixa, 'blue')
    desenhar_solid_3d(ax, vertices_cone, arestas_cone, 'red')
    # Adicione os outros sólidos à cena 3D
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    plt.show()
    
    # Definição da câmera
    centro_massa_cone = calcular_centro_massa(vertices_cone)
    centro_massa_cano = calcular_centro_massa(vertices_cano)
    ponto_medio = [(c1 + c2) / 2 for c1, c2 in zip(centro_massa_cone, centro_massa_cano)]
    origem_camera = [10, 10, 10]
    matriz_camera = base_camera(origem_camera, ponto_medio)

    # Transformação para o sistema da câmera
    vertices_cone_camera = transformar_para_camera(vertices_cone, origem_camera, matriz_camera)
    # Transformar os outros sólidos...

    # Projeção em perspectiva e renderização 2D
    matriz_projecao = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ])

    vertices_proj_cone = perspectiva(vertices_cone_camera, matriz_projecao)
    # Projeção para os outros sólidos...

    # Renderizar em 2D
    fig, ax = plt.subplots()
    desenhar_solid_2d(ax, vertices_proj_cone, arestas_cone, 'red')
    # Renderizar os outros sólidos...
    plt.show()

if __name__ == "__main__":
    main()