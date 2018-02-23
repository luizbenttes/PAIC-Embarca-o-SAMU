from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

TOTAL = 4 #número de pontos
prec = 8000 #total de pontos intermediários
LARGURA = 600
ALTURA = 600

tam = 100
quant = 4 #quantidade de curvas a serem mostradas''

# pontos = [[[66.5, 0.0, 0.0], [91.701537401368, 0.0, 0.0], [105.71495612196605, 6.1644346721947407, 0.0], [124.0, 16.3, 0.0]],
# 			[[0, 12.8, 0.0], [76.468254918831391, 15.470330303456716, 0.0], [124.0, 16.3, 0.0]],
# 			[[0, 3.3,0.0], [47.897336317074284, 3.2999999999999998,0.0], [66.275645365241274, 4.4365630301171066,0.0], [114.4, 11.2,0.0]]]

pontos = [[[0, 11.1, 0.0], [19.707890300631821, 10.842545907638371, 0.0], [106.19223310320206, 21.9907607050948, 0.0], [124.0, 0, 0.0]],
			[[0, -11.1, 0.0], [19.707890300631821, -10.842545907638371, 0.0], [106.19223310320206, -21.9907607050948, 0.0], [124.0, 0, 0.0]],
			[[0, 10.2, 0.0], [48.175123682594453, 6.5822834252897744, 0.0], [70.031790183162144, 19.753999726244025, 0.0], [114.4, 0, 0.0]],
			[[0, -10.2, 0.0], [50.730828282414706, -6.5822834252897744, 0.0], [67.862493010446258, -19.753999726244025, 0.0], [114.4, 0.0, 0.0]]]

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def Init():
	delta = 1/prec

	glClearColor(0.0,0.0,0.0,0.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	

	for i in range(quant): #quantidade de curvas para a figura
		glMap1f(GL_MAP1_VERTEX_3,0.0,1.0,pontos[i])
		glEnable(GL_MAP1_VERTEX_3)

		glColor3f(1.5,1.0,0.3)
		thickness=0.1
		glLineWidth(thickness)
		glBegin(GL_LINE_STRIP)
		for j in frange(0.0,1.0,delta):
			glEvalCoord1f(round(j,2))
		glEnd()

		glRasterPos2f(125, 0)
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, 33)
		glBegin(GL_LINES)
		glVertex2f(0,0)   
		glVertex2f(124.0, 0)
		glEnd()


		# PONTOS
	
		glColor3f(0.0,1.0,0.0)
		glPointSize(5)

		glBegin(GL_POINTS)
		
		aux = len((pontos[i]))

		for j in range(0,aux):
			glVertex3fv(pontos[i][j])
		glEnd();

		# glColor3f(0.0,1.0,1.0)
		# glPointSize(5)



		glBegin(GL_POINTS)
		glVertex3fv([114.4,11.2,0.0])
		glEnd()
		glEnable(GL_DEPTH_TEST)

	
	glutSwapBuffers()
	glFlush()

# def Display():
# 	delta = 1/prec

# 	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# 	glColor3f(1.0,0.0,0.0)

# 	glBegin(GL_LINE_STRIP)
# 	for i in frange(0.0,1.0,delta):
# 		glEvalCoord1f(round(i,2))
# 	glEnd()

# 	glColor3f(0.0,1.0,0.0)
# 	glPointSize(5)

# 	#pontos de controle da curva
# 	glBegin(GL_POINTS)
# 	for i in range(0,TOTAL):
# 		glVertex3fv(pontos[i])
# 	glEnd();

# 	glutSwapBuffers()
# 	glFlush()

def escolha(botao, estado, x, y):
	global quant
	if (botao == GLUT_LEFT_BUTTON) and (estado == GLUT_DOWN):
		if quant < 1:
			quant = quant + 1
	elif (botao == GLUT_RIGHT_BUTTON) and (estado == GLUT_DOWN):
		if quant > 0:
			quant = quant - 1

def reshape(w, h):
	# glViewport(0, 0, w, h)
	# glMatrixMode(GL_PROJECTION)
	# glLoadIdentity()
	# if w <= h:
	#     glOrtho(-tam, tam, -tam*h/w,tam*h/w, -tam, tam)
	# else:
	#     glOrtho(-tam*w/h,tam*w/h, -tam, tam, -tam, tam)
	# glMatrixMode(GL_MODELVIEW)
	# glLoadIdentity()
	glMatrixMode (GL_PROJECTION)
	gluOrtho2D (-5.5, 130, -60.0, 60.0) 


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(LARGURA, ALTURA)
glutInitWindowPosition(250,70)
glutCreateWindow(b'Curvas de Bezier')

glutDisplayFunc(Init)
glutReshapeFunc(reshape)
glutMouseFunc(escolha)


glutMainLoop()