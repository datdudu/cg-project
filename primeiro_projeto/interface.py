import tkinter as tk
from tkinter import simpledialog, messagebox
import importlib.util
import sys
import matplotlib.pyplot as plt
import numpy as np

# Carrega módulos externos
def load_module(file_path):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = module
    spec.loader.exec_module(module)
    return module


# RASTERIZAÇÃO DE RETAS
# Função para solicitar parâmetros ao usuário
def obter_parametros_retas():
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

        # Fecha o diálogo e retorna os valores
        dialog.destroy()
        dialog.result = (x0, y0, x1, y1)

    # Cria uma nova janela de diálogo
    dialog = tk.Toplevel()
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

    # Botão para confirmar a entrada
    tk.Button(dialog, text="Confirmar", command=confirmar).pack(pady=10)

    # Foco no primeiro campo
    entry_x0.focus_set()

    # Impede que o usuário interaja com a janela principal até que o diálogo seja fechado
    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

    return dialog.result if hasattr(dialog, 'result') else (None, None, None, None)

# Função para rasterizar e exibir em todas as resoluções
def rasterizar_retas():
    try:
        x0, y0, x1, y1 = obter_parametros_retas()
        if None in [x0, y0, x1, y1]:
            return

        resolucoes = [(100, 100), (300, 300), (800, 600), (1920, 1080)]
        rasterizacao_reta = load_module("01_rasterizacao_retas.py")

        # Cria uma nova figura com subplots para exibir todas as resoluções
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        axs = axs.flatten()

        for i, (res_x, res_y) in enumerate(resolucoes):
            imagem = rasterizacao_reta.rasterizar_reta(x0, y0, x1, y1, res_x, res_y)
            axs[i].imshow(imagem, cmap='gray')
            axs[i].set_title(f"Resolução {res_x}x{res_y}")
            axs[i].axis('off')  # Remove os eixos para uma visualização mais limpa

        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao rasterizar retas: {e}")


# RASTERIZAÇÃO DE POLÍGONOS
def rasterizar_poligonos():
    try:
        rasterizacao_poligono = load_module("02_rasterizacao_poligonos.py")
        rasterizacao_poligono.rasterizar_poligonos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao rasterizar polígonos: {e}")


# RASTERIZAÇÃO DE CURVAS
def rasterizar_curvas():
    try:
        rasterizacao_curva_hermite = load_module("03_rasterizacao_curvas_hermite.py")
        rasterizacao_curva_hermite.rasterizar_curvas_hermite()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao rasterizar curvas de Hermite: {e}")

# Cria a interface gráfica
class RasterizacaoApp:
    def __init__(self, master):
        self.master = master
        master.title("Rasterização")

        # Define o estilo da interface
        master.configure(bg='light blue')

        # Título da interface
        title_label = tk.Label(master, text="Aplicação de Rasterização", font=('Arial', 16, 'bold'), bg='light blue')
        title_label.pack(pady=10)

        # Botão para rasterizar retas
        self.button_retas = tk.Button(master, text="Rasterizar Retas", command=rasterizar_retas, font=('Arial', 10, 'bold'), bg='light green', fg='black', height=2, width=30)
        self.button_retas.pack(pady=10)

        # Botão para rasterizar polígonos
        self.button_poligonos = tk.Button(master, text="Rasterizar Polígonos", command=rasterizar_poligonos, font=('Arial', 10, 'bold'), bg='light coral', fg='black', height=2, width=30)
        self.button_poligonos.pack(pady=10)

        # Botão para rasterizar curvas de Hermite
        self.button_curvas = tk.Button(master, text="Rasterizar Curvas de Hermite", command=rasterizar_curvas, font=('Arial', 10, 'bold'), bg='light goldenrod', fg='black', height=2, width=30)
        self.button_curvas.pack(pady=10)

# Executa a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = RasterizacaoApp(root)
    root.mainloop()
