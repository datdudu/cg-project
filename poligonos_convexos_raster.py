# poligono_convexo.py

import numpy as np
import matplotlib.pyplot as plt
from raster import rasterizacao_reta, produz_fragmento

def rasterizacao_poligono(vertices, resolucao=(100, 100)):
    """
    Rasteriza um polígono convexo usando o algoritmo de scan-line.
    
    :param vertices: Lista de vértices [(x1, y1), (x2, y2), ..., (xn, yn)] definindo o polígono.
    :param resolucao: Resolução da imagem (largura, altura).
    :return: Uma imagem binária com o polígono preenchido.
    """
    img = np.zeros(resolucao)
    n = len(vertices)
    
    # Para cada par de vértices, rasterize a linha que os conecta
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # O próximo vértice (circular)
        pontos_linha = rasterizacao_reta(x1, y1, x2, y2)
        
        # Preenche a imagem com os pontos da linha rasterizada
        for (x, y) in pontos_linha:
            if 0 <= x < resolucao[0] and 0 <= y < resolucao[1]:
                img[y, x] = 1

    # Para cada scan-line (linha da imagem), preencha os espaços internos do polígono
    for y in range(resolucao[1]):
        # Encontre os pontos de interseção com as arestas do polígono
        intersecoes = []
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            if min(y1, y2) <= y <= max(y1, y2) and y1 != y2:  # O y da scan-line cruza a aresta
                intersecao_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersecoes.append(intersecao_x)
        
        # Ordenar as interseções para preencher entre pares
        intersecoes.sort()
        for i in range(0, len(intersecoes), 2):
            x_start = int(round(intersecoes[i]))
            x_end = int(round(intersecoes[i + 1]))
            img[y, x_start:x_end] = 1
    
    return img

def gerar_imagem_poligono(vertices, resolucao=(80, 80)):
    return rasterizacao_poligono(vertices, resolucao)

# # Função de desenho de polígono
# def desenhar_poligono(vertices, resolucao):
#     img = rasterizacao_poligono(vertices, resolucao)
#     plt.imshow(img, cmap='gray')
#     plt.title(f'Polígono Convexo Rasterizado')
#     plt.show()

# # Resoluções diferentes
# resolucoes = [(100, 100), (200, 200), (300, 300), (400, 400)]

# # Triângulo equilátero 1
# vertices_triangle1 = [(50, 20), (80, 80), (20, 80)]

# # Triângulo equilátero 2
# vertices_triangle2 = [(30, 40), (70, 40), (50, 80)]

# # Desenho dos triângulos para diferentes resoluções
# for resolucao in resolucoes:
#     desenhar_poligono(vertices_triangle1, resolucao)
#     desenhar_poligono(vertices_triangle2, resolucao)


# # Quadrado 1
# vertices_square1 = [(20, 20), (80, 20), (80, 80), (20, 80)]

# # Quadrado 2
# vertices_square2 = [(40, 40), (60, 40), (60, 60), (40, 60)]

# # Desenho dos quadrados para diferentes resoluções
# for resolucao in resolucoes:
#     desenhar_poligono(vertices_square1, resolucao)
#     desenhar_poligono(vertices_square2, resolucao)

# # Hexágono 1
# vertices_hexagon1 = [(50, 10), (90, 30), (90, 70), (50, 90), (10, 70), (10, 30)]

# # Hexágono 2
# vertices_hexagon2 = [(30, 20), (70, 20), (90, 40), (70, 60), (30, 60), (10, 40)]

# # Desenho dos hexágonos para diferentes resoluções
# for resolucao in resolucoes:
#     desenhar_poligono(vertices_hexagon1, resolucao)
#     desenhar_poligono(vertices_hexagon2, resolucao)
