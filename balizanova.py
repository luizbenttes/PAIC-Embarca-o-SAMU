import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from numpy import ones,vstack
from numpy.linalg import lstsq
from mpl_toolkits.mplot3d import Axes3D
import math

'''
# Nome da funcão: angParaRad
# ang: angulo em graus
# Descrição: dado um angulo em graus é retornado 
            seu equivalente em radianos
'''
def angParaRad(ang):
    return ang * math.pi / 180.0

def AngToRad(ang):
    return ang * 2 * math.pi / 360.0

'''
# Nome da funcão: angComplemento
# ang: angulo em graus
# Descrição: retornar o complemento do angulo, dada
            a regra que a soma dos angulos
            internos do triangulo é 180
'''
def angComplemento(ang):
    return 90 - ang


'''
# Nome da funcão: Deslocamento
# largura: comprimento eixo X
# altura: largura eixo Y
# ang: angulo de costado
# Descrição: utilizando teorema de pitagoras,
            é encontrado o valor de deslocamento
            da reta após a insercao do angulo de costado
'''
def deslocamento(largura, altura, ang):
    return largura - (ang * altura)


'''
# Nome da funcão: encontraFuncao
# pontos: tupla contendo duas coordenadas no plano cartesiano
# Descrição: retornar a funcao y = mx + c 
            dado 2 pontos distintos retornando os coeficientes
            M e C
'''
def encontraFuncao(pontos):
    x_coords, y_coords = zip(*pontos)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    x = np.arange(-10., 100., 1.)
    #plt.plot(x, m * x + c)
    return m, c


'''
# Nome da funcão: intercessão
# d: coeficiente de X [equacao 1]
# m: coeficiente de X [equacao 2]
# c: coeficiente independete [equacao 2]
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

def intercessao1(d, m, c):
    deltaD = (d * -1) - (m * -1)

    deltaDx = (0 * -1) - (-1 * -c)
    x = deltaDx / deltaD

    deltaDy = (d * -c) - (m * 0)
    y = deltaDy / deltaD
    return x,y
'''
# Nome da função: plot2D
# pontos: parâmetro nparray que consiste em todos os pontos
        que representam as quinas da embarcação
# altura: altura da embarcação
# largura: largura da embarcação 
# Descrição: com os pontos que constituem as quinas é possível
            criar uma limitacao que representa uma baliza da
            embarcação
'''
def plot2D(deadrise,costado,altura,largura):
    pontos, altura, largura = principal(deadrise,costado,altura,largura)
    hull = ConvexHull(pontos)
    print(pontos)
    plt.plot(pontos[:, 0], pontos[:, 1], 'ro')
    for simplex in hull.simplices:
        plt.plot(pontos[simplex, 0], pontos[simplex, 1], 'k-')
    plt.axis([-altura*2, altura * 2, -largura*2, largura * 2], 'b')
    plt.show()

def coordenadadasQuinas(altura,largura, u, v,pontoChineX,pontoChineY):
    return np.array([[0, altura],[0,0], [largura, altura], [u, v],[-largura,altura],[-u, v], [pontoChineY,pontoChineX],
                     [-pontoChineY,pontoChineX]])

def funcaoPontoAngulo(ponto,a):
    b = ponto[1] - (ponto[0]*a)
    print("y = ",a,"x +",b)
    return b

def encontraY(pontos,x):
    if (x >= 0) and (x <=pontos[2]):
        (m,c) = pontos[0]
    else:
        (m, c) = pontos[1]
    #print(m, c)
    #print(m*x + c)
    return x, m*x + c

def linhaDeChine(dBow,comprimento,aChine,xBaseChine,dT):
    xBase = 20
    alfaBow = 45


    pontoComprimento = [comprimento, dBow]
    aBase = math.tan(AngToRad(alfaBow))
    bBase = funcaoPontoAngulo(pontoComprimento, aBase)
    raiz = -bBase / aBase


    pontosFuncao = [(0, dT), (xBaseChine, dT)]
    m, c = encontraFuncao(pontosFuncao)
    #
    linhaChine = []
    linhaChine.append((m, c))
    pontoChine = [xBaseChine, dT]
    bChine = funcaoPontoAngulo(pontoChine, aChine)
    # plt.plot(x, aChine * x + bChine,'b')

    # #intercessao linha base e linha base chine
    x, y = intercessao(aBase, bBase, aChine, bChine)
    # plt.plot([xBaseChine, x], [dT, y], 'b')

    pontosFuncao = [(xBaseChine, dT), (x, y)]
    m, c = encontraFuncao(pontosFuncao)
    linhaChine.append((m, c))
    linhaChine.append(dT)
    print(linhaChine)

    teste = 0
    x, y = encontraY(linhaChine,teste)
    return x, y
    # plt.grid(False)
    # plt.axis([-1, comprimento + 2, -dBow * 3.5, dBow * 3.5], 'b')
    # plt.show()


def principal(deadrise,costado,altura,largura):

    #plotagem da função relacionada ao angulo de deadrise
    x = np.arange(-10.,100.,1.)
    d = np.tan(angParaRad(deadrise))

    #plotagem da função relacionada ao angulo de costado
    angBase = angComplemento(costado)
    costado = angParaRad(costado)
    pontoCostadoX = deslocamento(largura, altura, np.tan(costado))
    m, c = encontraFuncao([(pontoCostadoX,0),(largura,altura)])

    #encontro do ponto chine (interceção da funcão de deadrise e costado)
    u, v = intercessao1(d, m, c)

    #marcação dos pontos que representam as "quinas" da embarcação
    #pontos = coordenadadasQuinas(altura, largura, u, v)

    # xBaseChine = 10
    # dT = 3
    # alfaChine = 20
    # aChine = math.tan(AngToRad(alfaChine))
    # comprimento = 40
    # pontoChineX,pontoChineY = linhaDeChine(altura, comprimento, aChine, xBaseChine, dT)

    pontos = coordenadadasQuinas(altura, largura, u, v, pontoChineX, pontoChineY)

    return pontos,altura,largura

deadrise  = int(input("Deadrise: "))
costado  = int(input("Costado: "))
altura  = int(input("Altura: "))
largura  = int(input("Largura: "))


alfaChine = int(input("Alfa Chine: "))
valorX = int(input("Valor de X: "))


plot2D(deadrise,costado,altura,largura)