import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init2D(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (-20.0, 200.0, -60.0, 150.0) 

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)

    # #draw two points
    glBegin(GL_POINTS)
    glVertex2f(124.0, 16.3)
    glVertex2f(0,0)
    glVertex2f(66.5, 0)
    glVertex2f(114.4,11.2)
    glEnd()
    # for i in range(0,10):
    #     glVertex2i(10+5*i,110)
    # glColor3f(1.0, 10.0, 0.0)
    # glVertex2i(80,110)
    # glEnd()


    #draw a line
    glBegin(GL_LINES)
    glVertex2f(0,0)   
    glVertex2f(66.5, 0)
    glEnd()



    glFlush()
    
glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (600, 600)
glutInitWindowPosition (100, 100)
glutCreateWindow (b'points and lines')
init2D(0.0,0.0,0.0)
glutDisplayFunc(display)
glutMainLoop()