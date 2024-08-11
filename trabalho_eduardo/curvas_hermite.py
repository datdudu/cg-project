import numpy as np
import matplotlib.pyplot as plt
from raster import rasterizacao_reta, produz_fragmento

def curva_hermite(p1, p2, t1, t2, n_points=100):
    """
    Gera uma curva de Hermite parametrizada por t, com n_points pontos.

    :param p1: Ponto inicial (x, y)
    :param p2: Ponto final (x, y)
    :param t1: Tangente no ponto inicial (dx, dy)
    :param t2: Tangente no ponto final (dx, dy)
    :param n_points: Número de pontos para discretizar a curva
    :return: Lista de pontos [(x, y)] ao longo da curva
    """
    t_values = np.linspace(0, 1, n_points)
    curve_points = []

    for t in t_values:
        h1 = 2*t**3 - 3*t**2 + 1
        h2 = -2*t**3 + 3*t**2
        h3 = t**3 - 2*t**2 + t
        h4 = t**3 - t**2
        
        x = h1*p1[0] + h2*p2[0] + h3*t1[0] + h4*t2[0]
        y = h1*p1[1] + h2*p2[1] + h3*t1[1] + h4*t2[1]
        
        curve_points.append((x, y))
    
    return curve_points

def rasterizar_curva_hermite(curve_points):
    """
    Rasteriza uma curva de Hermite conectando os pontos discretizados.

    :param curve_points: Lista de pontos [(x, y)] que formam a curva
    :return: Lista de pontos rasterizados
    """
    rasterized_points = []
    
    for i in range(len(curve_points) - 1):
        x1, y1 = curve_points[i]
        x2, y2 = curve_points[i + 1]
        rasterized_points.extend(rasterizacao_reta(x1, y1, x2, y2))
    
    return rasterized_points

def gerar_imagem_curva_hermite(p1, p2, t1, t2, n_points=100, resolucao=(80, 80)):
    curve_points = curva_hermite(p1, p2, t1, t2, n_points)
    rasterized_points = rasterizar_curva_hermite(curve_points)
    img = np.zeros(resolucao)
    for (x, y) in rasterized_points:
        if 0 <= x < resolucao[0] and 0 <= y < resolucao[1]:
            img[int(y), int(x)] = 1
    return img


# def desenhar_curva_hermite(p1, p2, t1, t2, n_points=100, resolucao=(100, 100)):
#     """
#     Desenha uma curva de Hermite usando matplotlib.

#     :param p1: Ponto inicial (x, y)
#     :param p2: Ponto final (x, y)
#     :param t1: Tangente no ponto inicial (dx, dy)
#     :param t2: Tangente no ponto final (dx, dy)
#     :param n_points: Número de pontos para discretizar a curva
#     :param resolucao: Resolução da imagem (largura, altura)
#     """
#     curve_points = curva_hermite(p1, p2, t1, t2, n_points)
#     rasterized_points = rasterizar_curva_hermite(curve_points)
    
#     img = np.zeros(resolucao)
    
#     for (x, y) in rasterized_points:
#         if 0 <= x < resolucao[0] and 0 <= y < resolucao[1]:
#             img[int(y), int(x)] = 1
    
#     plt.imshow(img, cmap='gray')
#     plt.title('Curva de Hermite Rasterizada')
#     plt.show()

# # Exemplo de uso
# p1 = (20, 30)
# p2 = (80, 70)
# t1 = (10, 40)
# t2 = (-30, -10)

# # Curva 1
# desenhar_curva_hermite((20, 30), (80, 70), (10, 40), (-30, -10))

# # Curva 2
# desenhar_curva_hermite((10, 10), (90, 90), (20, 50), (-20, -50))

# # Curva 3
# desenhar_curva_hermite((15, 60), (70, 20), (0, 50), (-50, 0))

# # Curva 4
# desenhar_curva_hermite((50, 50), (50, 50), (30, -30), (-30, 30))

# # Curva 5
# desenhar_curva_hermite((25, 75), (75, 25), (40, 40), (-40, -40))

# # P1 e P2 iguais
# desenhar_curva_hermite((50, 50), (50, 50), (30, -30), (-30, 30))

# # Curva com 10 pontos
# desenhar_curva_hermite((20, 30), (80, 70), (10, 40), (-30, -10), n_points=10)

# # Curva com 50 pontos
# desenhar_curva_hermite((20, 30), (80, 70), (10, 40), (-30, -10), n_points=50)

# # Curva com 100 pontos
# desenhar_curva_hermite((20, 30), (80, 70), (10, 40), (-30, -10), n_points=100)