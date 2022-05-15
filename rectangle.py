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

def draw_1(list1,list2 ,t):
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    p0 = np.array(list1)
    v = np.array(list2)
    
    t1 = t
    p = p0+t1*v
    glBegin(GL_LINES)
    glVertex(p0)
    glVertex(p)

    glEnd()
    glFlush()
    xyplane()

def main():
    list1 = [-0.3,0.2]
    list2 = [0 , 0.2]
    list7 = [-0.3,-0.2]
    list8 = [0.3,0]
    list5 = [-0.3,0.2]
    list6 = [0.2,0]
    list3 = [0.3,0.2]
    list4 = [0,0.2]
    
    t3= 3
    t1= -2
    t4  = 2
    
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        for i in range(4):
            if i == 0:
                draw_1(list1,list2 ,t1)
            elif i == 1:
                draw_1(list3,list4 ,t1)
            elif i == 2:
                draw_1(list5,list6 , t3)
            elif i == 3:
                draw_1(list7,list8 ,t4)

            
        
        # draw_2(list3,list4)

        # draw_1()
        pygame.display.flip()
        pygame.time.wait(10)

main()