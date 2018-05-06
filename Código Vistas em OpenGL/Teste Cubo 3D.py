import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

TOTAL = 4   #numero de pontos
prec = 80   #total de pontos intermediarios
LARGURA = 600
ALTURA = 600

tam = 70
quant = 4   #quantidade de curvas a serem mostradas

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Boat():
    pontos = [[[0, 11.1,0.0], [19.70789030063182, 10.842545907638371,0.0], [106.19223310320206, 21.9907607050948,0.0], [124.0, 0,0.0]],
            [[0, -11.1, 0.0],[19.707890300631821, -10.842545907638371, 0.0], [106.19223310320206, -21.9907607050948, 0.0], [124.0, 0, 0.0]],
            [[0, 10.2,0.0], [57.2, 11.198429713894045,0.0], [85.80000000000001, 12.139979743594694, 0.0], [114.4, 0, 0.0]],
            [[0, -10.2,0.0], [57.2, -11.198429713894045,0.0], [85.80000000000001, -12.139979743594694, 0.0], [114.4, 0, 0.0]]]

    delta = 1/prec

    glClearColor(0,0,0,0)
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for i in range(quant): #quantidade de curvas para a figura
        glMap1f(GL_MAP1_VERTEX_3,0.0,1.0,pontos[i])
        glEnable(GL_MAP1_VERTEX_3)

        glColor3f(1,0,0)
        thickness=2
        glLineWidth(thickness)
        glBegin(GL_LINE_STRIP)
        for j in frange(0.0,1.0,delta):
            glEvalCoord1f(round(j,2))
            print(round(j,2))
        glEnd()
        
        glBegin(GL_LINES)
        glVertex2f(0,11.1)   
        glVertex2f(0,-11.1)
        glEnd()    


        # glPointSize(8)
        # glBegin(GL_POINTS)      
        # aux = len((pontos[i]))

        # for j in range(0,aux):
        #     if (j == 0) or (j == len(pontos[i])-1):
        #         glColor3f(0.0,1.0,0.0)
        #         glVertex3fv(pontos[i][j])
        #     else:
        #         glColor3f(1.0,0.0,0.6)
        #         glVertex3fv(pontos[i][j])
        # glEnd()

        glEnable(GL_DEPTH_TEST)

    
    #glutSwapBuffers()
    glFlush()

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(90, (display[0]/display[1]), 10, 50.0)

    glTranslatef(0.0,0.0, -60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Cube()
        Boat()
        pygame.display.flip()
        pygame.time.wait(10)


main()