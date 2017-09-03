import matplotlib.pyplot as plt
from numpy import ones, vstack
from numpy.linalg import lstsq
import numpy as np
import math

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
    #plt.plot(x, m * x + c)
    return m, c

def AngToRad(ang):
    return ang * 2 * math.pi / 360.0

def funcaoPontoAngulo(ponto,a):
    b = ponto[1] - (ponto[0]*a)
    x = np.arange(-30., 100., 1.)
    print("y = ",a,"x +",b)
    return b
    # plt.plot(x, a * x + b)
    # plt.axis([-10, 10, -10, 10], 'g')
    # plt.show()

# xBase = int(input("Insira o tamanho da base: "))
# xBaseChine = int(input("Insira o tamanho da base Chine: "))
# dT= int(input("Insira o tamanho Dt: "))
# dBow = int(input("Insira o tamanho DBow: "))
# comprimento = int(input("Insira Comprimento embarcaçao: "))
# alfaBow = int(input("Insira angulo de Alfa Bow: "))

xBase = 10
xBaseChine = 5
dT= 3
dBow = 12
comprimento = 30
alfaBow = 30

alfaChine = int(input("Insira angulo de Alfa Chine: "))
x = np.arange(-10., 100., 1.)
aChine = math.tan(AngToRad(alfaChine))

plt.plot([0,xBase],[0,0],'r')
pontoBase = [xBase,0]
aBase = math.tan(AngToRad(alfaBow))
bBase = funcaoPontoAngulo(pontoBase,aBase)
plt.plot(x, aBase * x + bBase, 'r')
plt.plot([0,xBaseChine],[dT,dT],'b')

plt.plot([0,comprimento],[dBow,dBow],'g')
plt.legend(['xBase','xBaseChine','LinhaDeck'], loc='upper left')
# m,c = encontraFuncao([(xBase,0),(comprimento,dBow)])
#
# plt.plot(x, m * x + c)


pontoChine = [xBaseChine,dT]
bChine = funcaoPontoAngulo(pontoChine,aChine)
plt.plot(x, aChine * x + bChine,'b')
plt.grid(True)
plt.axis([-1, 30, -1, 30], 'b')
plt.show()

