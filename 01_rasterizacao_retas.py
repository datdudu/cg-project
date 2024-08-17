import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox

# Função que rasteriza um segmento de reta
def rasterizar_reta(x0, y0, x1, y1, res_x, res_y):
    # Inicializa a imagem (preto)
    imagem = np.zeros((res_y, res_x), dtype=np.uint8)
    
    # Converte as coordenadas normalizadas [-1, 1] para coordenadas de pixel [0, res_x-1] e [0, res_y-1]
    x0 = int((x0 + 1) * (res_x - 1) / 2)
    y0 = int((1 - y0) * (res_y - 1) / 2)  # Invertendo o eixo Y
    x1 = int((x1 + 1) * (res_x - 1) / 2)
    y1 = int((1 - y1) * (res_y - 1) / 2)  # Invertendo o eixo Y

    dx = x1 - x0
    dy = y1 - y0
    
    # Caso 1: |Δx| > |Δy|, percorre x
    if abs(dx) > abs(dy):
        if x0 > x1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dy / dx
        for x in range(x0, x1 + 1):
            y = y0 + m * (x - x0)
            imagem[int(round(y)), x] = 255
    
    # Caso 2: |Δy| > |Δx|, percorre y
    else:
        if y0 > y1:
            x0, x1, y0, y1 = x1, x0, y1, y0
        m = dx / dy
        for y in range(y0, y1 + 1):
            x = x0 + m * (y - y0)
            imagem[y, int(round(x))] = 255

    return imagem

# Função para visualizar a imagem rasterizada
def visualizar_imagem(imagem):
    plt.imshow(imagem, cmap='gray')
    plt.show()

# Classe da interface gráfica
class RasterizacaoApp:
    def __init__(self, master):
        self.master = master
        master.title("Rasterização de Retas")

        # Canvas para desenhar o espaço normalizado [-1,1] x [-1,1]
        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()

        # Botão para adicionar segmentos de reta
        self.button_adicionar = tk.Button(master, text="Adicionar Segmento de Reta", command=self.adicionar_segmento)
        self.button_adicionar.pack()

        # Botão para rasterizar e exibir as imagens
        self.button_rasterizar = tk.Button(master, text="Rasterizar e Exibir", command=self.rasterizar_todos)
        self.button_rasterizar.pack()

        # Resoluções definidas
        self.resolucoes = [(100, 100), (300, 300), (800, 600), (1920, 1080)]
        self.segmentos = []

    def adicionar_segmento(self):
        # Cria uma nova janela de diálogo
        dialog = tk.Toplevel(self.master)
        dialog.title("Inserir Coordenadas")

        tk.Label(dialog, text="Digite as coordenadas x0, y0, x1, y1 nos campos abaixo:").pack(pady=10)

        # Campos de entrada para x0, y0, x1, y1 com rótulos
        tk.Label(dialog, text="x0:").pack()
        entry_x0 = tk.Entry(dialog)
        entry_x0.pack()

        tk.Label(dialog, text="y0:").pack()
        entry_y0 = tk.Entry(dialog)
        entry_y0.pack()

        tk.Label(dialog, text="x1:").pack()
        entry_x1 = tk.Entry(dialog)
        entry_x1.pack()

        tk.Label(dialog, text="y1:").pack()
        entry_y1 = tk.Entry(dialog)
        entry_y1.pack()

        # Função para capturar os valores e realizar a validação
        def confirmar():
            try:
                x0 = float(entry_x0.get())
                y0 = float(entry_y0.get())
                x1 = float(entry_x1.get())
                y1 = float(entry_y1.get())
            except ValueError:
                messagebox.showerror("Erro", "Todos os valores devem ser números.")
                return

            # Verifica se os valores estão dentro do intervalo [-1, 1]
            if not all(-1 <= v <= 1 for v in [x0, y0, x1, y1]):
                messagebox.showerror("Erro", "Valor inserido inválido. Todos os valores devem estar no intervalo [-1, 1].")
                return

            # Adiciona o segmento à lista e fecha o diálogo
            self.segmentos.append((x0, y0, x1, y1))
            self.canvas.create_line(self.normalizar(x0), self.normalizar_invertido(y0), self.normalizar(x1), self.normalizar_invertido(y1), fill="blue")
            dialog.destroy()

        # Botão para confirmar a entrada
        tk.Button(dialog, text="Confirmar", command=confirmar).pack(pady=10)

        # Foco no primeiro campo
        entry_x0.focus_set()

        # Impede que o usuário interaja com a janela principal até que o diálogo seja fechado
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
            for x0, y0, x1, y1 in self.segmentos:
                imagem += rasterizar_reta(x0, y0, x1, y1, res_x, res_y)
            plt.figure(f"Resolução {res_x}x{res_y}")
            visualizar_imagem(imagem)

    def normalizar(self, valor):
        # Normaliza o valor de [-1,1] para [0,300] para o canvas
        return int((valor + 1) * 150)

    def normalizar_invertido(self, valor):
        # Inverte e normaliza o valor de [-1,1] para [0,300] para o canvas
        return int((1 - valor) * 150)

# Executa a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = RasterizacaoApp(root)
    root.mainloop()
