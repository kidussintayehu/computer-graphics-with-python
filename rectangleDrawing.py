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
    list = [-0.3,0.2]
    list2 = [0 , 0.2]
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    p0 = np.array(list)
    v = np.array(list2)
    
   
    t = -2
    p = p0+t*v
    glBegin(GL_LINES)
    glVertex(p0)
    glVertex(p)

    glEnd()
    
    
    list3 = [0.3,0.2]
    list4 = [0,0.2]
    
    p1 = np.array(list3)
    v1 = np.array(list4)
    
   
    t1= -2
    p2 = p1+t1*v1
    glBegin(GL_LINES)
    glVertex(p1)
    glVertex(p2)

    
    glEnd()

    list5 = [-0.3,0.2]
    list6 = [0.2,0]
    
    p3 = np.array(list5)
    v3 = np.array(list6)
    
   
    t2= 3
    p4 = p3+t2*v3
    glBegin(GL_LINES)
    glVertex(p3)
    glVertex(p4)

    
    glEnd()
    list7 = [-0.3,-0.2]
    list8 = [0.3,0]
    
    p5 = np.array(list7)
    v4 = np.array(list8)
    
   
    t3= 2
    p6 = p5+t3*v4
    glBegin(GL_LINES)
    glVertex(p5)
    glVertex(p6)

    
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

        pygame.display.flip()
        pygame.time.wait(10)

main()