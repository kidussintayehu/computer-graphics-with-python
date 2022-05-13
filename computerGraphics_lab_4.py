import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


# this function is to draw the x y coordinate
def xyplane():
    glColor3f(1.0, 0.0, 1.0)
    glPointSize(2)
    glBegin(GL_LINES)
    glVertex2f(-20.0, 0.0)
    glVertex2f(20, 0.0)
    glVertex2f(0, 8.0)
    glVertex2f(0, -8.0)
    glEnd()
    glFlush()


# this function is used to create the tkinter GUI
def tk():
    root = Tk()
    root.geometry('400x200')
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ch1 = IntVar()
    ch2 = IntVar()
    ch3 = IntVar()
    ch4 = IntVar()
    ch5 = IntVar()
    ch6 = IntVar()
    fontStyle = tkFont.Font(size=15)
    ttk.Label(frm, text="choose any function to draw", font=fontStyle).grid(column=2, row=1)
    ttk.Checkbutton(frm, text="sin", variable=ch1).grid(column=2, row=4)
    ttk.Checkbutton(frm, text="cos", variable=ch2).grid(column=2, row=5)
    ttk.Checkbutton(frm, text="x cubed", variable=ch3).grid(column=2, row=6)
    ttk.Checkbutton(frm, text="x squared - 7", variable=ch4).grid(column=2, row=7)
    ttk.Checkbutton(frm, text="1/(-x)", variable=ch5).grid(column=2, row=8)
    ttk.Checkbutton(frm, text="square root", variable=ch6).grid(column=2, row=9)

    def button():
        if ch1.get() == 1:
            list.append(sin)
        if ch2.get() == 1:
            list.append(cos)
        if ch3.get() == 1:
            list.append(cube)
        if ch4.get() == 1:
            list.append(xsquard_7)
        if ch5.get() == 1:
            list.append(_minusx)
        if ch6.get() == 1:
            list.append(squareroot)
        if len(list) == 0:
            ttk.Label(frm, text="choose at least 1 function").grid(column=2, row=11)
        if len(list) >= 1:
            display()

    ttk.Button(frm, text="Display Graph", command=lambda: button()).grid(column=1, row=10)

    root.mainloop()


def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-30.0, 30.0, -10.0, 10.0)


def xsquard_7():
    glColor3f(1.0, 1.0, 1.0, )
    x = np.arange(-2, 2, 0.01)
    y = np.power(x, 2) - 7
    glPointSize(2)
    glBegin(GL_LINE_STRIP)

    for a, b in zip(x, y):
        glVertex2f(a, b)
    glEnd()
    glFlush()
    xyplane()


def _minusx():
    glColor3f(0.7, 0.6, 0.2,)
    x = np.arange(-20,20 , 0.01)
    y = 1/(-x)
    glPointSize(2)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, y):
        if(-8<=b<=8):
            glVertex2f(a, b)

    glEnd()
    glFlush()
    xyplane()


def cube():
    glColor4f(0.0, 1.0, 0.0, 0.7)
    x = np.arange(-2, 2, 0.01)
    y = np.power(x, 3)
    glPointSize(2)
    glBegin(GL_LINE_STRIP)

    for a, b in zip(x, y):
        glVertex2f(a, b)
    glEnd()
    glFlush()
    xyplane()


def cos():
    glColor3f(0.2, 0.7, 0.8)
    z = np.arange(-10, 10, 0.01)
    l = np.cos(z)
    glPointSize(2)

    for a, b in zip(z, l):
        glBegin(GL_POINTS)
        glVertex2f(a, b)
        glEnd()
    xyplane()


def sin():
    glColor3f(1.0, 0.2, 0.3)

    glPointSize(2)
    x = np.arange(-10, 10, 0.001)
    y = np.sin(x)
    for a, b in zip(x, y):
        glBegin(GL_POINTS)
        glVertex2f(a, b)
        glEnd()

    xyplane()


def squareroot():
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(2)
    x = np.arange(0, 25, 0.01)
    y = np.sqrt(x)
    for a, b in zip(x, y):
        glBegin(GL_POINTS)
        glVertex2f(a, b)
        glEnd()
    xyplane()


# i created a list to store  the name of the functions
list = []


def display():
    init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT)
        for i in list:
            i()

        pygame.display.flip()
        pygame.time.wait(10)


def main():
    tk()


# if name == 'main':
main()