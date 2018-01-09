import matplotlib.pyplot as plt
from numpy import ones, vstack
from numpy.linalg import lstsq
import numpy as np
import math
import VistaSuperior
'''
# Nome da funcão: intercessão
# a1: coeficiente de X [equacao 1]
# b1: coeficiente independente [equacao 1]
# a2: coeficiente de X [equacao 2]
# b2: coeficiente independete [equacao 2]
# Descrição: em posse dos coefientes de cada equacao é 
            possivel encontrar as coordenadas onde
            as duas retas se encontram
'''
def intercessao(a1, b1, a2, b2):
    deltaD = (a1 * -1) - (a2 * -1)

    deltaDx = (-b1 * -1) - (-1 * -b2)
    x = deltaDx / deltaD

    deltaDy = (a1 * -b2) - (a2 * -b1)
    y = deltaDy / deltaD

    return x,y

def encontraFuncao(pontos):
    x_coords, y_coords = zip(*pontos)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    x = np.arange(-10., 100., 1.)
    #print("y = ", m, "x +", c)
    #plt.plot(x, m * x + c)
    return m, c

def AngToRad(ang):
    return ang * 2 * math.pi / 360.0

def funcaoPontoAngulo(ponto,a):
    b = ponto[1] - (ponto[0]*a)
    print("y = ",a,"x +",b)
    return b

def encontraY(pontos,x):
    if (x > 0) and (x <=pontos[2]):
        (m,c) = pontos[0]
    else:
        (m, c) = pontos[1]
    #print(m, c)
    #print(m*x + c)
    return x, m*x + c

# xBase = int(input("Insira o tamanho da base: "))
# xBaseChine = int(input("Insira o tamanho da base Chine: "))
# dT= int(input("Insira o tamanho Dt: "))
# dBow = int(input("Insira o tamanho DBow: "))
# comprimento = int(input("Insira Comprimento embarcaçao: "))
# alfaBow = int(input("Insira angulo de Alfa Bow: "))

xBase = 20
xBaseChine = 10
dT= 3
dBow = 12
comprimento = 30
alfaBow = 45

alfaChine = int(input("Insira angulo de Alfa Chine: "))
x = np.arange(-10., 100., 1.)
aChine = math.tan(AngToRad(alfaChine))

#linha que representa a linha do DECK
plt.plot([0,comprimento],[dBow,dBow],'g')
plt.plot([0,0],[0,dBow],'g')
#linhas que repesentam a base


pontoComprimento = [comprimento,dBow]
aBase = math.tan(AngToRad(alfaBow))
bBase = funcaoPontoAngulo(pontoComprimento,aBase)
#plt.plot(x, aBase * x + bBase, 'r')
raiz = -bBase/aBase
plt.plot([0,raiz],[0,0],'r')
plt.plot([raiz,comprimento],[0,dBow],'r')
#linhas que repesentam a base CHINE
plt.plot([0,xBaseChine],[dT,dT],'b')

pontosFuncao = [(0,dT),(xBaseChine,dT)]
m,c = encontraFuncao(pontosFuncao)
#
pontoChine = [xBaseChine,dT]
bChine = funcaoPontoAngulo(pontoChine,aChine)
#plt.plot(x, aChine * x + bChine,'b')




# #intercessao linha base e linha base chine
x,y = intercessao(aBase, bBase, aChine, bChine)
plt.plot([xBaseChine,x],[dT,y], 'b')
pontosFuncao = [(xBaseChine,dT),(x,y)]


plt.grid(False)
plt.axis([-1, comprimento+2, -dBow*3.5, dBow*3.5], 'b')
plt.show()
#VistaSuperior.VistaSuperior(x)