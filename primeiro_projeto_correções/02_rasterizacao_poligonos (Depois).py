# RASTERIZAÇÃO DE POLÍGONOS
# Código desenvolvido na disciplina de Computação Gráfica, do curso de Engenharia da Computação do IFCE Fortaleza
# Autores: José Edilson Ceará Gomes Filho e Carlos Eduardo Carvalho Cardoso
# Data: 10/08/2024

# INSTRUÇÕES
# 1 - Coloque os seguintes arquivos em uma única pasta:
#       01_rasterizacao_retas.py
#       02_rasterizacao_poligonos.py
#       03_rasterizacao_curvas_hermite.py
#       interface.py
# 2 - Execute o interface.py
# 3 - Escolha uma das opções de rasterização que aparecerá no menu

###################################################################################################################

# Importando as bibliotecas
# RASTERIZAÇÃO DE POLÍGONOS
# Código desenvolvido na disciplina de Computação Gráfica, do curso de Engenharia da Computação do IFCE Fortaleza
# Autores: José Edilson Ceará Gomes Filho e Carlos Eduardo Carvalho Cardoso
# Data: 20/08/2024

# INSTRUÇÕES
# 1 - Coloque os seguintes arquivos em uma única pasta:
#       01_rasterizacao_retas.py
#       02_rasterizacao_poligonos.py
#       03_rasterizacao_curvas_hermite.py
#       interface.py
# 2 - Execute o interface.py
# 3 - Escolha uma das opções de rasterização que aparecerá no menu

###################################################################################################################

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Função que rasteriza um segmento de reta
def rasterizar_reta(x0, y0, x1, y1, res_x, res_y):
    imagem = np.zeros((res_y, res_x), dtype=np.uint8)
    
    x0 = int((x0 + 1) * (res_x - 1) / 2)
    y0 = int((1 - y0) * (res_y - 1) / 2)
    x1 = int((x1 + 1) * (res_x - 1) / 2)
    y1 = int((1 - y1) * (res_y - 1) / 2)

    dx = x1 - x0
    dy = y1 - y0
    
    if abs(dx) > abs(dy):
        if x0 > x1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dy / dx
        for x in range(x0, x1 + 1):
            y = y0 + m * (x - x0)
            imagem[int(round(y)), x] = 255
    else:
        if y0 > y1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dx / dy
        for y in range(y0, y1 + 1):
            x = x0 + m * (y - y0)
            imagem[y, int(round(x))] = 255

    return imagem

# Função que rasteriza um polígono e preenche usando o algoritmo de varredura com par-ímpar
def rasterizar_poligono(imagem, vertices, res_x, res_y):
    num_vertices = len(vertices)
    edges = []

    # Converte as coordenadas dos vértices para coordenadas de pixel
    for i in range(num_vertices):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % num_vertices]
        x0 = int((x0 + 1) * (res_x - 1) / 2)
        y0 = int((1 - y0) * (res_y - 1) / 2)
        x1 = int((x1 + 1) * (res_x - 1) / 2)
        y1 = int((1 - y1) * (res_y - 1) / 2)
        edges.append((x0, y0, x1, y1))

    # Scanline algorithm with odd-even filling
    for y in range(res_y):
        intersections = []
        for x0, y0, x1, y1 in edges:
            if y0 < y1:
                ymin, ymax = y0, y1
                xmin, xmax = x0, x1
            else:
                ymin, ymax = y1, y0
                xmin, xmax = x1, x0

            if ymin <= y < ymax:
                if xmax != xmin:
                    x_intersection = xmin + (y - ymin) * (xmax - xmin) / (ymax - ymin)
                    intersections.append(x_intersection)
                else:
                    intersections.append(xmin)

        intersections.sort()

        # Fill between pairs of intersections
        for i in range(0, len(intersections), 2):
            x_start = int(intersections[i])
            x_end = int(intersections[i + 1])
            imagem[y, x_start:x_end] = 255

    return imagem

# Função para criar polígonos básicos
def criar_poligonos():
    triangulo1 = [(-0.95, -0.95), (-0.8, -0.5), (-0.65, -0.95)]
    triangulo2 = [(-0.5, -0.95), (-0.25, 0), (0, -0.95)]
    quadrado1 = [(-0.95, 0.95), (-0.65, 0.95), (-0.65, 0.65), (-0.95, 0.65)]
    quadrado2 = [(-0.95, 0.5), (-0.95, 0.0), (-0.45, 0.0), (-0.45, 0.5)]
    hexagono1 = [(0.5, 0.87), (0.9, 0.4), (0.9, -0.4), (0.5, -0.87), (0.1, -0.4), (0.1, 0.4)]
    hexagono2 = [(0.5, 0.43), (0.75, 0.2), (0.75, -0.2), (0.5, -0.43), (0.25, -0.2), (0.25, 0.2)]
    
    return [triangulo1, triangulo2, quadrado1, quadrado2, hexagono1, hexagono2]

# Função principal para rasterizar e visualizar todos os polígonos no mesmo canvas
def rasterizar_poligonos():
    poligonos = criar_poligonos()
    resolucoes = [(100, 100), (300, 300), (800, 600), (1920, 1080)]

    fig, axs = plt.subplots(2, 2, figsize=(13, 9))
    axs = axs.flatten()

    for i, (res_x, res_y) in enumerate(resolucoes):
        imagem = np.zeros((res_y, res_x), dtype=np.uint8)
        for vertices in poligonos:
            imagem = rasterizar_poligono(imagem, vertices, res_x, res_y)
        axs[i].imshow(imagem, cmap='gray')
        axs[i].set_title(f"Polígonos - Resolução {res_x}x{res_y}")
        axs[i].axis('off')

    plt.subplots_adjust(hspace=3)
    plt.tight_layout()
    plt.show()

# Executa a rasterização dos polígonos
if __name__ == "__main__":
    rasterizar_poligonos()
