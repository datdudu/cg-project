import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np

# Importa as funções dos algoritmos
from raster import gerar_imagem_reta
from poligonos_convexos_raster import gerar_imagem_poligono
from curvas_hermite import gerar_imagem_curva_hermite

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Rasterização de Algoritmos")
        self.geometry("1000x600")

        # Frame esquerdo para seleção de algoritmos e parâmetros
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Opções de algoritmos
        self.algorithms = ["Rasterização de Retas", "Rasterização de Polígonos", "Curvas de Hermite"]
        self.selected_algorithm = tk.StringVar(value=self.algorithms[0])
        for algo in self.algorithms:
            tk.Radiobutton(self.left_frame, text=algo, variable=self.selected_algorithm, value=algo, command=self.update_params).pack(anchor=tk.W)

        # Parâmetros
        self.params_frame = tk.Frame(self.left_frame)
        self.params_frame.pack(pady=10)

        # Inicializa os parâmetros
        self.update_params()

        # Botão de execução
        tk.Button(self.left_frame, text="Executar", command=self.execute_algorithm).pack(pady=10)

        # Frame direito para exibição da imagem
        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.image_label = tk.Label(self.right_frame)
        self.image_label.pack()

    def update_params(self):
        for widget in self.params_frame.winfo_children():
            widget.destroy()

        algorithm = self.selected_algorithm.get()
        
        if algorithm == "Rasterização de Retas":
            self.x1_entry = self.create_param_entry("x1", 0)
            self.y1_entry = self.create_param_entry("y1", 0)
            self.x2_entry = self.create_param_entry("x2", 80)
            self.y2_entry = self.create_param_entry("y2", 80)
        
        elif algorithm == "Rasterização de Polígonos":
            self.vertices_entry = tk.Entry(self.params_frame, width=50)
            self.vertices_entry.insert(0, "[(20, 20), (80, 20), (80, 80), (20, 80)]")
            self.vertices_entry.pack(pady=5)
        
        elif algorithm == "Curvas de Hermite":
            self.p1_entry = self.create_param_entry("P1 (x, y)", "20,30")
            self.p2_entry = self.create_param_entry("P2 (x, y)", "80,70")
            self.t1_entry = self.create_param_entry("T1 (dx, dy)", "10,40")
            self.t2_entry = self.create_param_entry("T2 (dx, dy)", "-30,-10")
            self.n_points_entry = self.create_param_entry("N Points", 100)
        
        self.resolucao_entry = self.create_param_entry("Resolução (width, height)", "80,80")

    def create_param_entry(self, label_text, default_value):
        frame = tk.Frame(self.params_frame)
        frame.pack(pady=5)
        tk.Label(frame, text=label_text).pack(side=tk.LEFT)
        entry = tk.Entry(frame)
        entry.insert(0, default_value)
        entry.pack(side=tk.RIGHT)
        return entry

    def execute_algorithm(self):
        algorithm = self.selected_algorithm.get()
        resolucao = tuple(map(int, self.resolucao_entry.get().split(',')))
        image = None

        try:
            if algorithm == "Rasterização de Retas":
                x1 = int(self.x1_entry.get())
                y1 = int(self.y1_entry.get())
                x2 = int(self.x2_entry.get())
                y2 = int(self.y2_entry.get())
                image_array = gerar_imagem_reta(x1, y1, x2, y2, resolucao)
            
            elif algorithm == "Rasterização de Polígonos":
                vertices_str = self.vertices_entry.get()
                vertices = eval(vertices_str)
                image_array = gerar_imagem_poligono(vertices, resolucao)
            
            elif algorithm == "Curvas de Hermite":
                p1 = tuple(map(int, self.p1_entry.get().split(',')))
                p2 = tuple(map(int, self.p2_entry.get().split(',')))
                t1 = tuple(map(int, self.t1_entry.get().split(',')))
                t2 = tuple(map(int, self.t2_entry.get().split(',')))
                n_points = int(self.n_points_entry.get())
                image_array = gerar_imagem_curva_hermite(p1, p2, t1, t2, n_points, resolucao)

            if image_array is not None:
                self.display_image(image_array)
            else:
                messagebox.showerror("Erro", "Não foi possível gerar a imagem.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def display_image(self, image_array):
        image = Image.fromarray((image_array * 255).astype(np.uint8))
        photo = ImageTk.PhotoImage(image=image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    app = Application()
    app.mainloop()
