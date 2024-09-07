# RASTERIZAÇÃO DE RETAS
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
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Função que rasteriza um segmento de reta
def rasterizar_reta(x0, y0, x1, y1, res_x, res_y):

    # Inicializa a imagem (preto)
    imagem = np.zeros((res_y, res_x), dtype=np.uint8)
    
    # Converte as coordenadas normalizadas [-1, 1] para coordenadas de pixel [0, res_x-1] e [0, res_y-1]
    x0 = int((x0 + 1) * (res_x - 1) / 2)
    y0 = int((1 - y0) * (res_y - 1) / 2)  # Invertendo o eixo Y para centralizar o ponto 0,0
    x1 = int((x1 + 1) * (res_x - 1) / 2)
    y1 = int((1 - y1) * (res_y - 1) / 2)  # Invertendo o eixo Y para centralizar o ponto 0,0
    dx = x1 - x0
    dy = y1 - y0

    # Caso especial: segmento de ponto único
    if dx == 0 and dy == 0:  
        # Garante que o ponto único (x0, y0) está dentro dos limites da imagem
        if 0 <= x0 < res_x and 0 <= y0 < res_y: 
            imagem[y0, x0] = 255
        return imagem
    
    # Caso 1: |Δx| > |Δy|, percorre x
    # Para cada pixel em x, o código calcula a posição correspondente em y e desenha o pixel correspondente.
    if abs(dx) > abs(dy):  
        if x0 > x1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dy / dx if dx != 0 else 0   # Calculo da inclinação (M)
        for x in range(x0, x1 + 1):
            y = y0 + m * (x - x0)
            imagem[int(round(y)), x] = 255

    # Caso 2: |Δy| > |Δx|, percorre y
    # # Para cada pixel em y, o código calcula a posição correspondente em x e desenha o pixel correspondente.
    else:  
        if y0 > y1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dx / dy if dy != 0 else 0   # Calculo da inclinação (M)
        for y in range(y0, y1 + 1):
            x = x0 + m * (y - y0)
            imagem[y, int(round(x))] = 255
    return imagem

# Classe da interface gráfica
class RasterizacaoApp:
    def __init__(self, master):
        self.master = master
        master.title("Rasterização de Retas")

        # Canvas para desenhar o espaço normalizado [-1,1] x [-1,1]
        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()

        # Botões para interações
        self.button_adicionar = tk.Button(master, text="Adicionar Segmento de Reta", command=self.adicionar_segmento)
        self.button_adicionar.pack()

        self.button_rasterizar = tk.Button(master, text="Rasterizar e Exibir", command=self.rasterizar_todos)
        self.button_rasterizar.pack()

        # Resoluções definidas e lista de segmentos
        self.resolucoes = [(100, 100), (300, 300), (800, 600), (1920, 1080)]
        self.segmentos = []

    def adicionar_segmento(self):
        # Abre um diálogo para inserir coordenadas
        dialog = tk.Toplevel(self.master)
        dialog.title("Inserir Coordenadas")

        tk.Label(dialog, text="Digite as coordenadas x0, y0, x1, y1 nos campos abaixo:").pack(pady=10)
        entries = [(tk.Entry(dialog), tk.Label(dialog, text=f"{coord}:")) for coord in ["x0", "y0", "x1", "y1"]]
        
        for entry, label in entries:
            label.pack()
            entry.pack()

        def confirmar():
            try:
                coords = [float(entry.get()) for entry, _ in entries]
                if not all(-1 <= v <= 1 for v in coords):
                    raise ValueError("Valores fora do intervalo [-1, 1]")
            except ValueError:
                messagebox.showerror("Erro", "Todos os valores devem ser números no intervalo [-1, 1].")
                return

            # Adiciona o segmento e desenha no canvas
            self.segmentos.append(tuple(coords))
            self.canvas.create_line(*[self.normalizar_invertido(c) if i % 2 else self.normalizar(c) for i, c in enumerate(coords)], fill="blue")
            dialog.destroy()

        tk.Button(dialog, text="Confirmar", command=confirmar).pack(pady=10)
        entries[0][0].focus_set()  # Foco no primeiro campo
        dialog.transient(self.master)
        dialog.grab_set()
        self.master.wait_window(dialog)

    def rasterizar_todos(self):
        if not self.segmentos:
            messagebox.showerror("Erro", "Nenhum segmento foi adicionado.")
            return

        # Rasteriza e exibe em diferentes resoluções
        for res_x, res_y in self.resolucoes:
            imagem = np.zeros((res_y, res_x), dtype=np.uint8)
            for segmento in self.segmentos:
                imagem += rasterizar_reta(*segmento, res_x, res_y)
            plt.figure(f"Resolução {res_x}x{res_y}")
            self.visualizar_imagem(imagem)

    def normalizar(self, valor):
        return int((valor + 1) * 150)  # Normaliza o valor de [-1,1] para [0,300]

    def normalizar_invertido(self, valor):
        return int((1 - valor) * 150)  # Inverte e normaliza o valor de [-1,1] para [0,300]

    @staticmethod
    def visualizar_imagem(imagem):
        plt.imshow(imagem, cmap='gray')
        plt.show()

# Executa a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = RasterizacaoApp(root)
    root.mainloop()
