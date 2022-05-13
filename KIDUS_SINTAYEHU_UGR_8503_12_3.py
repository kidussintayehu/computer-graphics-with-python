from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np

win = Tk()


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def drawLogAndPower():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    x = np.linspace(-1, 1, 100)
    y = np.log(x)

    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, y):
        glVertex2f(a, b)
    glEnd()
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    z = np.power(x, 2)
    for c, d in zip(x, z):
        glVertex2f(c, d)

    glEnd()
    glFlush()


def drawSineAndCubic():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    x = np.linspace(-1, 10, 100)
    y = np.sin(x)

    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, y):
        glVertex2f(a, b)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    z = np.power(x,3)
    for c, d in zip(x, z):
        glVertex2f(c, d)

    glEnd()
    glFlush()

def drawTanAndArchTan():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    x = np.linspace(-1, 10, 100)
    y = np.sin(x)
    z = np.cos(x)
    w = y / z
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, w):
        glVertex2f(a ,b)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    z = np.arctan(x)
    for c, d in zip(x, z):
        glVertex2f(c, d)

    glEnd()
    glFlush()


def logAndPower():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        drawLogAndPower()
        pygame.display.flip()
        pygame.time.wait(10)


def sineAndCubic():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        drawSineAndCubic()

        pygame.display.flip()
        pygame.time.wait(10)


def tanAndArchTan():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        drawTanAndArchTan()

        pygame.display.flip()
        pygame.time.wait(10)

win.geometry("700x350")

Label(win, text="ComputerGraphics!", font=('Aerial 17 bold italic')).pack(pady=30)

ttk.Button(win, text="log(x) and x^2", command=logAndPower).pack(pady=20)
ttk.Button(win, text="sin(x) and x^3", command=sineAndCubic).pack(pady=20)
ttk.Button(win, text="tan(x) and archtan(x)", command=tanAndArchTan).pack(pady=20)

win.mainloop()
