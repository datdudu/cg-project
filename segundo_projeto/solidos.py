import numpy as np

def criar_caixa(lado, altura):
    # Vértices e arestas para a caixa sem tampa
    vertices = [
        [0, 0, 0], [lado, 0, 0], [lado, lado, 0], [0, lado, 0], # Base
        [0, 0, altura], [lado, 0, altura], [lado, lado, altura], [0, lado, altura]  # Topo
    ]
    arestas = [(0, 1), (1, 2), (2, 3), (3, 0),  # Base
               (0, 4), (1, 5), (2, 6), (3, 7),  # Laterais
               (4, 5), (5, 6), (6, 7), (7, 4)]  # Topo
    return vertices, arestas

def criar_cone(raio, altura):
    # Criação do cone com a base no plano XY e ápice no eixo Z
    num_lados = 20  # Definição de 20 segmentos para a base
    vertices = [[raio * np.cos(2 * np.pi * i / num_lados), raio * np.sin(2 * np.pi * i / num_lados), 0] for i in range(num_lados)]
    vertices.append([0, 0, altura])  # Ápice
    arestas = [(i, (i + 1) % num_lados) for i in range(num_lados)]  # Arestas da base
    arestas += [(i, num_lados) for i in range(num_lados)]  # Arestas laterais
    return vertices, arestas

def criar_tronco_cone(raio_inf, raio_sup, altura):
    num_lados = 20
    vertices_inf = [[raio_inf * np.cos(2 * np.pi * i / num_lados), raio_inf * np.sin(2 * np.pi * i / num_lados), 0] for i in range(num_lados)]
    vertices_sup = [[raio_sup * np.cos(2 * np.pi * i / num_lados), raio_sup * np.sin(2 * np.pi * i / num_lados), altura] for i in range(num_lados)]
    vertices = vertices_inf + vertices_sup
    arestas = [(i, (i + 1) % num_lados) for i in range(num_lados)]  # Base inferior
    arestas += [(i + num_lados, (i + 1) % num_lados + num_lados) for i in range(num_lados)]  # Base superior
    arestas += [(i, i + num_lados) for i in range(num_lados)]  # Arestas laterais
    return vertices, arestas

def criar_cano(p1, p2, t1, t2, raio):
    num_lados = 20
    # Implementação da curva de Hermite para definir o caminho do cano
    # Simplificação para a criação dos pontos da curva
    # Apenas exemplo, não a implementação completa da curva Hermite
    vertices = [[raio * np.cos(2 * np.pi * i / num_lados), raio * np.sin(2 * np.pi * i / num_lados), 0] for i in range(num_lados)]
    arestas = [(i, (i + 1) % num_lados) for i in range(num_lados)]
    # Continuação da implementação...
    return vertices, arestas

def criar_caneca(raio, altura, raio_alca):
    num_lados = 20
    # Criação da base da caneca
    vertices_base = [[raio * np.cos(2 * np.pi * i / num_lados), raio * np.sin(2 * np.pi * i / num_lados), 0] for i in range(num_lados)]
    vertices_topo = [[raio * np.cos(2 * np.pi * i / num_lados), raio * np.sin(2 * np.pi * i / num_lados), altura] for i in range(num_lados)]
    vertices = vertices_base + vertices_topo
    arestas = [(i, (i + 1) % num_lados) for i in range(num_lados)]  # Base
    arestas += [(i + num_lados, (i + 1) % num_lados + num_lados) for i in range(num_lados)]  # Topo
    arestas += [(i, i + num_lados) for i in range(num_lados)]  # Laterais
    # Alça da caneca - simplificação
    # Continuação da implementação...
    return vertices, arestas
