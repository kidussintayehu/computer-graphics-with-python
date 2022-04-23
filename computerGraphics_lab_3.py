import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    x = np.linspace(-1, 1, 100)
    y = np.log(x)
    # z =np.power(x,2)
    
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, y):
# give (a, b) to OpenGL to draw
        glVertex2f(a, b)
    
    # glBegin(GL_LINE_STRIP)
    # f = np.linspace(1, -1, 100)
    # glPointSize(0)
    glEnd()

    # glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(-1.0, 1.0, 0.0)
    # glPointSize(10)

    glBegin(GL_LINE_STRIP)
    z =np.power(x,2)
    # x = np.linspace(-1, 1, 100)

    for c, d in zip(x, z):
        glVertex2f(c, d)
    # draw_1()
    # glVertex2f(0.0, 0.0)
    # glVertex2f(0.5, 0.0)
    # glVertex2f(-0.5, 0.0)
    # glVertex2f(0.0, 0.5)

    glEnd()

    glFlush()
def draw_1():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    x = np.linspace(-1, 1, 100)
    y =np.power(x,2)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, y):
        glVertex2f(a, b)
    glEnd()
    glFlush()
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        draw()

        # draw_1()
        pygame.display.flip()
        pygame.time.wait(10)


main()