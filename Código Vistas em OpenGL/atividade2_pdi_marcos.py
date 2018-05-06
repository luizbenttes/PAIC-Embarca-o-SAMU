from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

TOTAL = 4 	#numero de pontos
prec = 1000 	#total de pontos interediarios
LARGURA = 600
ALTURA = 600

tam = 140
quant = 4 	#quantidade de curvas a serem mostradas

pontos = [[[0, 11.1,0.0], [19.70789030063182, 10.842545907638371,0.0], [106.19223310320206, 21.9907607050948,0.0], [124.0, 0,0.0]],
			[[0, -11.1, 0.0],[19.707890300631821, -10.842545907638371, 0.0], [106.19223310320206, -21.9907607050948, 0.0], [124.0, 0, 0.0]],
			[[0, 10.2,0.0], [57.2, 11.198429713894045,0.0], [85.80000000000001, 12.139979743594694, 0.0], [114.4, 0, 0.0]],
			[[0, -10.2,0.0], [57.2, -11.198429713894045,0.0], [85.80000000000001, -12.139979743594694, 0.0], [114.4, 0, 0.0]]]

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step
		#print(step) 
def Bezier(A,B,C,D,t):
	s = 1 - t
    AB = A*s + B*t
    BC = B*s + C*t
    CD = C*s + D*t
    ABC = AB*s + CD*t
    BCD = BC*s + CD*t
    return ABC*s + BCD*t

def Walking(controlPoints):
	for i in range(len(controlPoints)):
			j = 0
			A = controlPoints[i][j]
			B = controlPoints[i][j++]
			C = controlPoints[i][j++]
			D = controlPoints[i][j++]
			Bezier(A, B, C, D, 0)
			
def Init():
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
		for j in frange(0.0,1,delta):
			glEvalCoord1f(round(j,2))
		glEnd()

		glPointSize(8)
		glBegin(GL_POINTS)
		glVertex3fv([123.628349,0,0])
		glEnd()

		glBegin(GL_LINES)
		glVertex2f(0,11.1)
		glVertex2f(0,-11.1)
		glEnd()

		# PONTOS
			
		# glPointSize(8)
		# glBegin(GL_POINTS)		
		# aux = len((pontos[i]))

		# for j in range(0,aux):
		# 	if (j == 0) or (j == len(pontos[i])-1):
		# 		glColor3f(0.0,1.0,0.0)
		# 		glVertex3fv(pontos[i][j])
		# 	else:
		# 		glColor3f(1.0,0.0,0.6)
		# 		glVertex3fv(pontos[i][j])
		# glEnd()

		# glColor3f(0.0,1.0,1.0)
		# glPointSize(5)



		# glBegin(GL_POINTS)
		# glVertex3fv([114.4,11.2,0.0])
		# glEnd()
		glEnable(GL_DEPTH_TEST)

	
	glutSwapBuffers()
	glFlush()

def escolha(botao, estado, x, y):
	global quant
	if (botao == GLUT_LEFT_BUTTON) and (estado == GLUT_DOWN):
		if quant < 1:
			quant = quant + 1
	elif (botao == GLUT_RIGHT_BUTTON) and (estado == GLUT_DOWN):
		if quant > 0:
			quant = quant - 1

def reshape(w, h):
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D (-5.5, 130, -60.0, 60.0)
	# glLoadIdentity()
	# if w <= h:
	# 	gluOrtho2D (-2, tam, -tam*h/w,tam*h/w)
	# else:
	# 	gluOrtho2D (-tam/h,tam*w/h, -tam, tam)
	# glMatrixMode(GL_MODELVIEW)
	# glLoadIdentity()
	# glMatrixMode (GL_PROJECTION)
	 
	#glRotatef(1, 3, 1, 1)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(LARGURA, ALTURA)
glutInitWindowPosition(250,70)
glutCreateWindow(b'Linha Chine')

glutDisplayFunc(Init)
glutReshapeFunc(reshape)
glutMouseFunc(escolha)


glutMainLoop()