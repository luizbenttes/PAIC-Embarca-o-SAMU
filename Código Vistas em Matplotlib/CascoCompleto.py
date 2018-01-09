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
def intercessao(d, m, c):
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

    plt.plot(pontos[:, 0], pontos[:, 1], 'ro')
    for simplex in hull.simplices:
        plt.plot(pontos[simplex, 0], pontos[simplex, 1], 'k-')
    plt.axis([-altura*2, altura * 2, -largura*2, largura * 2], 'b')
    plt.show()

def plot3D(deadrise,costado,altura,largura):
    pts, altura, largura = principal(deadrise,costado,altura,largura)
    hull = ConvexHull(pts)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    for i in range(12):
        ax.plot(pts.T[0], pts.T[1],i+2, "ko")

        for s in hull.simplices:
            s = np.append(s, s[0])  # Here we cycle back to the first coordinate
            ax.plot(pts[s, 0], pts[s, 1],i+2, "r-")

    plt.axis([-altura*2, altura * 2, -largura*2, largura * 2], 'b')
    plt.show()

def coordenadadasQuinas(altura,largura, u, v):
    return np.array([[0, altura],[0,0], [largura, altura], [u, v],[-largura,altura],[-u, v]])

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
    u, v = intercessao(d, m, c)

    #marcação dos pontos que representam as "quinas" da embarcação
    pontos = coordenadadasQuinas(altura, largura, u, v)

    return pontos,altura,largura





