import numpy as np


# Função para rotacionar em torno do eixo X
def rotation_x(polygon, ang):
    # Criar a matriz de rotação em torno do eixo X
    cos_theta = np.cos(ang)
    sin_theta = np.sin(ang)
    R_x = np.array([
        [1, 0, 0, 0],
        [0, cos_theta, -sin_theta, 0],
        [0, sin_theta, cos_theta, 0],
        [0, 0, 0, 1]
    ])

    rotated_polygon = []
    for face in polygon:
        face_rotacionada = []
        for vertice in face:
            vertice_homogeneo = np.append(vertice, 1)
            vertice_rotacionado_homogeneo = np.dot(R_x, vertice_homogeneo)
            vertice_rotacionado = vertice_rotacionado_homogeneo[:3]
            face_rotacionada.append(vertice_rotacionado)
        rotated_polygon.append(face_rotacionada)
    return rotated_polygon

# Função para rotacionar em torno do eixo Y
def rotation_y(polygon, ang):
    # Criar a matriz de rotação em torno do eixo Y
    cos_theta = np.cos(ang)
    sin_theta = np.sin(ang)
    R_y = np.array([
        [cos_theta, 0, sin_theta, 0],
        [0, 1, 0, 0],
        [-sin_theta, 0, cos_theta, 0],
        [0, 0, 0, 1]
    ])

    rotated_polygon = []
    for face in polygon:
        face_rotacionada = []
        for vertice in face:
            vertice_homogeneo = np.append(vertice, 1)
            vertice_rotacionado_homogeneo = np.dot(R_y, vertice_homogeneo)
            vertice_rotacionado = vertice_rotacionado_homogeneo[:3]
            face_rotacionada.append(vertice_rotacionado)
        rotated_polygon.append(face_rotacionada)
    return rotated_polygon

# Função para rotacionar em torno do eixo Z
def rotation_z(polygon, ang):
    # Criar a matriz de rotação em torno do eixo Z
    cos_theta = np.cos(ang)
    sin_theta = np.sin(ang)
    R_z = np.array([
        [cos_theta, -sin_theta, 0, 0],
        [sin_theta, cos_theta, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    rotated_polygon = []
    for face in polygon:
        face_rotacionada = []
        for vertice in face:
            vertice_homogeneo = np.append(vertice, 1)
            vertice_rotacionado_homogeneo = np.dot(R_z, vertice_homogeneo)
            vertice_rotacionado = vertice_rotacionado_homogeneo[:3]
            face_rotacionada.append(vertice_rotacionado)
        rotated_polygon.append(face_rotacionada)
    return rotated_polygon


def scale_polygon(polygon, scale_vector):
    # Criar a matriz de escala 4x4
    S = np.array([
        [scale_vector[0], 0, 0, 0],
        [0, scale_vector[1], 0, 0],
        [0, 0, scale_vector[2], 0],
        [0, 0, 0, 1]
    ])

    scaled_polygon = []
    for face in polygon:
        face_escalada = []
        for vertice in face:
            # Converter o vértice para coordenadas homogêneas [x, y, z, 1]
            vertice_homogeneo = np.append(vertice, 1)
            # Multiplicar pela matriz de escala
            vertice_escalado_homogeneo = np.dot(S, vertice_homogeneo)
            # Voltar para as coordenadas 3D (x, y, z)
            vertice_escalado = vertice_escalado_homogeneo[:3]
            face_escalada.append(vertice_escalado)
        scaled_polygon.append(face_escalada)
    return scaled_polygon

def translation(polygon, translation_vector):
    # Criar a matriz de translação 4x4
    T = np.array([
        [1, 0, 0, translation_vector[0]],
        [0, 1, 0, translation_vector[1]],
        [0, 0, 1, translation_vector[2]],
        [0, 0, 0, 1]
    ])

    translated_polygon = []
    for face in polygon:
        face_transladada = []
        for vertice in face:
            # Converter o vértice para coordenadas homogêneas [x, y, z, 1]
            vertice_homogeneo = np.append(vertice, 1)
            # Multiplicar pela matriz de translação
            vertice_transladado_homogeneo = np.dot(T, vertice_homogeneo)
            # Voltar para as coordenadas 3D (x, y, z)
            vertice_transladado = vertice_transladado_homogeneo[:3]
            face_transladada.append(vertice_transladado)
        translated_polygon.append(face_transladada)
    return translated_polygon