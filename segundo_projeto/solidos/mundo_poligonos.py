import matplotlib.pyplot as plt

#from box_without_cover import create_cube
from pipe import  create_pipe
from mug import  create_mug 
from cone import create_cone 
from cone_trunk import create_cone_trunk
from transformations import translation, scale_polygon
from plots import plot_2d, plot_3d
from mundo import define_world2d, define_world3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#define os limites nos eixos x, y e z
define_world3d(ax)

#cubo1, cubo1_faceColor, cubo1_edgeColor = create_cube()
#plot_3d(ax, cubo1, cubo1_faceColor, cubo1_edgeColor)


#Definindo cone e cano no mesmo octante

cone1, cone1_faceColor, cone1_edgeColor = create_cone()
cone1 = scale_polygon(cone1, [2, 2, 2])
cone1 = translation(cone1, [-8, -8, -8])

plot_3d(ax, cone1, cone1_faceColor, cone1_edgeColor)

cano1, cano1_faceColor, cano1_edgeColor = create_pipe([-6, -2, -6], [5, 5, 0], [-2, -1, -2], [5, 5, 0], radius=0.5)

plot_3d(ax, cano1, cano1_faceColor, cano1_edgeColor)

#Definindo tronco de cone e caneca no mesmo octante

caneca1, caneca1_face_color, caneca1_edgeColor = create_mug()
caneca1 = scale_polygon(caneca1, [3, 3, 3])
caneca1 = translation(caneca1, [5, 5, 5])

plot_3d(ax, caneca1, caneca1_face_color, caneca1_edgeColor)

tronco_cone, tronco_cone_face_color, tronco_cone_edge_color = create_cone_trunk()
tronco_cone = scale_polygon(tronco_cone, [2, 2, 2])
tronco_cone = translation(tronco_cone, [2, 2, 2])

plot_3d(ax, tronco_cone, tronco_cone_face_color, tronco_cone_edge_color)

plt.show()

fig2, ax2 = plt.subplots()
define_world2d(ax2, title="Vizualização nos eixos X e Y", xlabel="Eixo x", ylabel="Eixo y")

plot_2d(ax2, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='xy')
plot_2d(ax2, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='xy')
plot_2d(ax2, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='xy')
plot_2d(ax2, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='xy')
#plot_2d(ax2, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='xy')

plt.show()

fig3, ax3 = plt.subplots()
define_world2d(ax3, title="Vizualização nos eixos X e Z", xlabel="Eixo x", ylabel="Eixo Z")

plot_2d(ax3, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='xz')
plot_2d(ax3, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='xz')
plot_2d(ax3, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='xz')
plot_2d(ax3, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='xz')
#plot_2d(ax3, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='xz')

plt.show()

fig4, ax4 = plt.subplots()
define_world2d(ax4, title="Vizualização nos eixos Y e Z", xlabel="Eixo Y", ylabel="Eixo Z")

plot_2d(ax4, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='yz')
plot_2d(ax4, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='yz')
plot_2d(ax4, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='yz')
plot_2d(ax4, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='yz')
#plot_2d(ax4, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='yz')

plt.show()

