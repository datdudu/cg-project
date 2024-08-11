# rasterizacao.py

import numpy as np
import matplotlib.pyplot as plt

def produz_fragmento(x, y):
    """
    Função para produzir o fragmento correspondente a um par (x, y) de valores contínuos.
    Converte as coordenadas contínuas (x, y) para os pixels mais próximos (xm, ym).
    """
    xm = int(round(x))
    ym = int(round(y))
    return xm, ym

def rasterizacao_reta(x1, y1, x2, y2):
    """
    Algoritmo de rasterização de retas usando a equação da reta.
    """
    # Cálculo das diferenças
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    # Determinação do coeficiente angular
    m = delta_y / delta_x if delta_x != 0 else float('inf')
    b = y1 - m * x1
    
    # Lista para armazenar os pontos da reta
    pontos = []
    
    # Se |∆x| > |∆y|, percorre a reta em função de x
    if abs(delta_x) > abs(delta_y):
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        
        x = x1
        y = y1
        
        while x <= x2:
            pontos.append(produz_fragmento(x, y))
            x += 1
            y = m * x + b
    
    # Caso contrário, percorre a reta em função de y
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        
        y = y1
        x = x1
        
        while y <= y2:
            pontos.append(produz_fragmento(x, y))
            y += 1
            x = (y - b) / m if m != float('inf') else x
    
    return pontos

def gerar_imagem_reta(x1, y1, x2, y2, resolucao=(80, 80)):
    pontos = rasterizacao_reta(x1, y1, x2, y2)
    img = np.zeros(resolucao)
    
    for (x, y) in pontos:
        if 0 <= x < resolucao[0] and 0 <= y < resolucao[1]:
            img[y, x] = 1
    
    return img

# def desenhar_reta(x1, y1, x2, y2, resolucao=(100, 100)):
#     """
#     Função para desenhar a reta rasterizada utilizando matplotlib.
#     """
#     pontos = rasterizacao_reta(x1, y1, x2, y2)
    
#     # Criação da imagem
#     img = np.zeros(resolucao)
    
#     for (x, y) in pontos:
#         if 0 <= x < resolucao[0] and 0 <= y < resolucao[1]:
#             img[y, x] = 1
    
#     plt.imshow(img, cmap='gray')
#     plt.title(f'Reta de ({x1},{y1}) a ({x2},{y2})')
#     plt.show()

# # Exemplo de uso
# desenhar_reta(10, 10, 90, 80, resolucao=(100, 100))