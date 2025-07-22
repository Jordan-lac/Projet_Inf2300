import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import ctypes

# Les textures
def load_texture(path):
    surface = pygame.image.load(path).convert_alpha()
    data = pygame.image.tostring(surface, "RGBA", True)
    width, height = surface.get_size()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glGenerateMipmap(GL_TEXTURE_2D)

    return texture

# Les shaders
def load_shader(vs_path, fs_path):
    with open(vs_path) as f:
        vs = f.read()
    with open(fs_path) as f:
        fs = f.read()
    return compileProgram(
        compileShader(vs, GL_VERTEX_SHADER),
        compileShader(fs, GL_FRAGMENT_SHADER)
    )

# Ajoutons la balle 
def create_quad():
    vertices = np.array([
        # pos      # tex
        -0.05,  0.05, 0.0, 0.0, 1.0,
        -0.05, -0.05, 0.0, 0.0, 0.0,
         0.05, -0.05, 0.0, 1.0, 0.0,

        -0.05,  0.05, 0.0, 0.0, 1.0,
         0.05, -0.05, 0.0, 1.0, 0.0,
         0.05,  0.05, 0.0, 1.0, 1.0,
    ], dtype=np.float32)
    return vertices

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

    shader = load_shader("shaders/lili_vert.glsl", "shaders/lili_frag.glsl")
    glUseProgram(shader)
    
    texture = load_texture("assets/balle.png")

    vertices = create_quad()
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    pygame.mixer.music.load("assets/musique_3.mp3")
    pygame.mixer.music.set_volume(0.4)  
    pygame.mixer.music.play(-1)
    
    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # pos
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, False, 5 * vertices.itemsize, ctypes.c_void_p(0))
    # tex
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, False, 5 * vertices.itemsize, ctypes.c_void_p(12))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Position initiale de la balle
    pos = [0.0, 0.0]
    vel = [0.01, 0.012]

    clock = pygame.time.Clock()

    running = True
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Changement de sa position
        for i in [0, 1]:
            pos[i] += vel[i]
            if abs(pos[i]) + 0.05 > 1.0:
                vel[i] *= -1

        glClearColor(1.0, 1.0, 1.0, 1.0)  # fond blanc
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader)

        # Envoi de la position
        pos_loc = glGetUniformLocation(shader, "offset")
        glUniform2f(pos_loc, pos[0], pos[1])

        # Envoi du temps pour le changement de couleur
        time_loc = glGetUniformLocation(shader, "time")
        current_time = pygame.time.get_ticks() / 1000.0  # en secondes
        glUniform1f(time_loc, current_time)

        # Activation et binding de la texture
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texture)
        tex_loc = glGetUniformLocation(shader, "texture1")
        glUniform1i(tex_loc, 0)

        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, 6)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
