import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np

import numpy as np

def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])

    return mat

# print(rotationMatrix(30))
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


    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)


    mat = rotationMatrix(60)

    # start new rectangle in forth quadrant
    list3 = [0.3,0.2]
    list4 = [0,0.2]
    
    p1 = np.array(list3)
    v1 = np.array(list4)
    
   
    t1= -2
    p2 = p1+t1*v1

    p1 = np.dot(p1 , mat)
    p2 = np.dot(p2 , mat)
    glBegin(GL_LINES)
    glVertex(p1)
    glVertex(p2)

    
    glEnd()
    # connect from fourth to first
    list5 = [-0.3,0.2]
    list6 = [0.2,0]
    
    p3 = np.array(list5)
    v3 = np.array(list6)
    
   
    t2= 3
    p4 = p3+t2*v3

    p3 = np.dot(p3 , mat)
    p4 = np.dot(p4 , mat)
    glBegin(GL_LINES)
    glVertex(p3)
    glVertex(p4)

    
    glEnd()
    # connect from third to second
    list7 = [-0.3,-0.2]
    list8 = [0.3,0]
    
    p5 = np.array(list7)
    v4 = np.array(list8)
    
   
    t3= 2
    p6 = p5+t3*v4

    p5 = np.dot(p5 , mat)
    p6 = np.dot(p6 , mat)
    glBegin(GL_LINES)
    glVertex(p5)
    glVertex(p6)

    
    glEnd()
    list9 = [-0.3,0.2]
    list10 = [0,0.2]
    
    p7 = np.array(list9)
    v8 = np.array(list10)
    
   
    t1= -2
    p8 = p7+t1*v8

    p7 = np.dot(p7 , mat)
    p8 = np.dot(p8 , mat)
    glBegin(GL_LINES)
    glVertex(p7)
    glVertex(p8)

    
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