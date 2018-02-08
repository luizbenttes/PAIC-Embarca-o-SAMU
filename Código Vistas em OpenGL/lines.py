import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init2D(r,g,b):
    glClearColor(r,g,b,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, 200.0, 0.0, 150.0) 

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    # #draw two points
    # glBegin(GL_POINTS)
    # for i in range(0,10):
    #     glVertex2i(10+5*i,110)
    # glEnd()

    #draw a line
    glBegin(GL_LINES)
    glVertex2i(0,0)   
    glVertex2i(200,150)
    glEnd()

    glFlush()
    
glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow (b'points and lines')
init2D(0.0,0.0,0.0)
glutDisplayFunc(display)
glutMainLoop()