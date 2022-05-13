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
def xyplane():
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2)
    glBegin(GL_LINES)
    glVertex2f(-20.0, 0.0)
    glVertex2f(20, 0.0)
    glVertex2f(0, 8.0)
    glVertex2f(0, -8.0)
    glEnd()
    glFlush()

def draw_1():
    list = [0.1,0.2]
    list2 = [0.5 , 0.4]
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    # x = np.linspace(-1, 1, 100)
    # y =np.power(x,2)
    # glPointSize(10)
    # glBegin(GL_LINE_STRIP)
    # for a, b in zip(x, y):
    #     glVertex2f(a, b)
    v1 = np.array(list)
    v2 = np.array(list2)
    t = 2
    p = v1+t*v2
    glBegin(GL_LINES)
    glVertex(v1)
    glVertex(p)

    
    glEnd()
    glFlush()

    xyplane()

def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        draw_1()

        # draw_1()
        pygame.display.flip()
        pygame.time.wait(10)
main()