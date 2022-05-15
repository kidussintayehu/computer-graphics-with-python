import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
def init():
    pygame.init()
    display = (800,600)
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

# vertices = (
#     (1, -1, -1), a
#     (1, 1, -1),b
#     (-1, 1, -1),c
#     (-1, -1, -1),d
#     (1, -1, 1),e
#     (1, 1, 1),f
#     (-1, -1, 1),g
#     (-1, 1, 1)h
# )


def draw_1():

    # third quadrant
    list = [-0.5,0.6]
    list2 = [0 , 0.6]
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    p0 = np.array(list)
    v = np.array(list2)
    
   
    t = -2
    p = p0+t*v
    glBegin(GL_LINES)
    glVertex(p0)
    glVertex(p)

    glEnd()
    
    
    list3 = [0.5,0.6]
    list4 = [0,0.6]
    
    p1 = np.array(list3)
    v1 = np.array(list4)
    
   
    t1= -2
    p2 = p1+t1*v1
    glBegin(GL_LINES)
    glVertex(p1)
    glVertex(p2)

    
    glEnd()

    list5 = [-0.5,0.6]
    list6 = [0.5,0]
    
    p3 = np.array(list5)
    v3 = np.array(list6)
    
   
    t2= 2
    p4 = p3+t2*v3
    glBegin(GL_LINES)
    glVertex(p3)
    glVertex(p4)

    
    glEnd()
    list7 = [-0.5,-0.6]
    list8 = [0.5,0]
    
    p5 = np.array(list7)
    v4 = np.array(list8)
    
   
    t3= 2
    p6 = p5+t3*v4
    glBegin(GL_LINES)
    glVertex(p5)
    glVertex(p6)

    
    glEnd()
    list9 = [-0.3,0.4]
    list10 = [0,0.4]
    
    p7 = np.array(list9)
    v5 = np.array(list10)
    
   
    t4= -2
    p8 = p7+t4*v5
    glBegin(GL_LINES)
    glVertex(p7)
    glVertex(p8)

    
    glEnd()
    list11 = [0.3,0.4]
    list12 = [0,0.4]
    
    p9 = np.array(list11)
    v6 = np.array(list12)
    
   
    t4= -2
    p10 = p9+t4*v6
    glBegin(GL_LINES)
    glVertex(p9)
    glVertex(p10)

    
    glEnd()
    list13 = [-0.3,0.4]
    list14 = [0.3,0]
    
    p11 = np.array(list13)
    v7 = np.array(list14)
    
   
    t5= 2
    p12 = p11+t5*v7
    glBegin(GL_LINES)
    glVertex(p11)
    glVertex(p12)

    
    glEnd()

    list15 = [-0.3,-0.4]
    list16 = [0.3,0]
    
    p13 = np.array(list15)
    v8 = np.array(list16)
    
   
    t6= 2
    p14 = p13+t6*v8
    glBegin(GL_LINES)
    glVertex(p13)
    glVertex(p14)
    glEnd()
    a = [0.3,0.4]
    b = [0.6,0.6]
    
    p15 = np.array(a)
    v9 = np.array(b)
    
   
    t7= 0.33
    p16 = p15+t7*v9
    glBegin(GL_LINES)
    glVertex(p15)
    glVertex(p16)
    glEnd()
    c = [-0.3,0.4]
    d = [-0.6,0.6]
    
    p17 = np.array(c)
    v10 = np.array(d)
    
   
    t7= 0.33
    p18 = p17+t7*v10
    glBegin(GL_LINES)
    glVertex(p17)
    glVertex(p18)
    glEnd()

    e = [0.3,-0.4]
    f = [0.6,-0.6]
    
    p19 = np.array(e)
    v11 = np.array(f)
    
   
    t7= 0.33
    p20 = p19+t7*v11
    glBegin(GL_LINES)
    glVertex(p19)
    glVertex(p20)
    glEnd()    
    g = [-0.3,-0.4]
    h = [-0.6,-0.6]
    
    p21 = np.array(g)
    v12 = np.array(h)
    
   
    t7= 0.33
    p22 = p21+t7*v12
    glBegin(GL_LINES)
    glVertex(p21)
    glVertex(p22)
    glEnd()  

    glFlush()
    
   

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