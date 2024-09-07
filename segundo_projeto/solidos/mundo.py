import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def define_world3d(ax):
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    # Adicionando linhas divisórias para os octantes
    ax.plot([10, -10], [0, 0], [0, 0], color='k', linewidth=2)
    ax.plot([0, 0], [10, -10], [0, 0], color='k', linewidth=2)
    ax.plot([0, 0], [0, 0], [10, -10], color='k', linewidth=2)

    ax.set_title("Vizualização 3D")
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')

def define_world2d(ax, title, xlabel, ylabel):
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Adicionando linhas divisórias para os octantes
    ax.plot([10, -10], [0, 0], [0, 0], color='k', linewidth=1)
    ax.plot([0, 0], [10, -10], [0, 0], color='k', linewidth=1)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)