import numpy as np
import matplotlib.pyplot as plt

# Função que rasteriza um segmento de reta
def rasterizar_reta(x0, y0, x1, y1, res_x, res_y):
    imagem = np.zeros((res_y, res_x), dtype=np.uint8)
    
    # Converte coordenadas normalizadas [-1, 1] para coordenadas de pixel [0, res_x-1] e [0, res_y-1], com (0,0) centralizado
    x0 = int((x0 + 1) * (res_x - 1) / 2)
    y0 = int((1 - y0) * (res_y - 1) / 2)
    x1 = int((x1 + 1) * (res_x - 1) / 2)
    y1 = int((1 - y1) * (res_y - 1) / 2)

    dx = x1 - x0
    dy = y1 - y0
    
    # Caso de reta vertical
    if dx == 0:
        if y0 > y1:
            y0, y1 = y1, y0
        for y in range(y0, y1 + 1):
            imagem[y, x0] = 255
    
    # Caso de reta horizontal
    elif dy == 0:
        if x0 > x1:
            x0, x1 = x1, x0
        for x in range(x0, x1 + 1):
            imagem[y0, x] = 255
    
    # Caso 1: |Δx| > |Δy|, percorre x
    elif abs(dx) > abs(dy):
        if x0 > x1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dy / dx
        for x in range(x0, x1 + 1):
            y = y0 + m * (x - x0)
            if 0 <= x < res_x and 0 <= int(round(y)) < res_y:
                imagem[int(round(y)), x] = 255
    
    # Caso 2: |Δy| > |Δx|, percorre y
    else:
        if y0 > y1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dx / dy
        for y in range(y0, y1 + 1):
            x = x0 + m * (y - y0)
            if 0 <= int(round(x)) < res_x and 0 <= y < res_y:
                imagem[y, int(round(x))] = 255

    return imagem

# Função para calcular um ponto na curva de Hermite
def hermite_curve(p0, p1, t0, t1, t):
    h00 = 2*t**3 - 3*t**2 + 1
    h10 = t**3 - 2*t**2 + t
    h01 = -2*t**3 + 3*t**2
    h11 = t**3 - t**2
    return h00*p0 + h10*t0 + h01*p1 + h11*t1

# Função para rasterizar uma curva de Hermite
def rasterizar_curva_hermite(p0, p1, t0, t1, res_x, res_y, num_segmentos):
    imagem = np.zeros((res_y, res_x), dtype=np.uint8)
    t_values = np.linspace(0, 1, num_segmentos + 1)
    
    for i in range(num_segmentos):
        t_a = t_values[i]
        t_b = t_values[i + 1]
        ponto_a = hermite_curve(p0, p1, t0, t1, t_a)
        ponto_b = hermite_curve(p0, p1, t0, t1, t_b)
        imagem += rasterizar_reta(ponto_a[0], ponto_a[1], ponto_b[0], ponto_b[1], res_x, res_y)
    
    return imagem

# Função para criar diferentes curvas de Hermite
def criar_curvas_hermite():
    curvas = [
        [(-0.5, 0.5), (-0.5, -0.5), (2.0, -1.0), (-2.0, 1.0)], # Curva 1
        [(0.0, 0.0), (0.5, 0.5), (2.0, -2.0), (-2.0, 2.0)],  # Curva 2
        [(0.5, -0.5), (-0.5, 0.5), (0.0, 1.0), (1.0, 0.0)], # Curva 3
        [(-0.7, -0.7), (0.7, 0.7), (0.0, 1.0), (1.0, 0.0)], # Curva 4
        [(0.0, 0.0), (0.5, 0.5), (1.0, 0.0), (0.0, 1.0)]  # Curva 5
    ]
    return curvas

# Função para visualizar a imagem rasterizada
def visualizar_imagem(imagem, ax):
    ax.imshow(imagem, cmap='gray', origin='lower')
    ax.axis('off')

# Função principal para rasterizar e visualizar todas as curvas
def rasterizar_curvas_hermite():
    curvas = criar_curvas_hermite()
    resolucao = (500, 500)
    
    # Quantidades diferentes de segmentos para comparar
    num_segmentos_variantes = [5, 10, 25]

    for i, curva in enumerate(curvas):
        p0, p1, t0, t1 = curva
        imagens = []
        for num_segmentos in num_segmentos_variantes:
            imagem = rasterizar_curva_hermite(np.array(p0), np.array(p1), np.array(t0), np.array(t1), resolucao[0], resolucao[1], num_segmentos)
            imagens.append(imagem)
        
        # Cria uma nova figura com subplots para exibir todas as resoluções para a curva atual
        fig, axs = plt.subplots(1, 3, figsize=(15, 8))
        for ax, num_segmentos, img in zip(axs, num_segmentos_variantes, imagens):
            visualizar_imagem(img, ax)
            ax.set_title(f"{num_segmentos} segmentos")
        
        plt.suptitle(f"Curva Hermite {i+1}")
        plt.subplots_adjust(wspace=0.1)  # Ajusta o espaçamento horizontal entre os subplots
        plt.show()

# Executa a rasterização das curvas de Hermite
if __name__ == "__main__":
    rasterizar_curvas_hermite()
