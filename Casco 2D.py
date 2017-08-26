import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from numpy import ones,vstack
from numpy.linalg import lstsq
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
# Nome da função: criarHull
# pontos: parâmetro nparray que consiste em todos os pontos
        que representam as quinas da embarcação
# altura: altura da embarcação
# largura: largura da embarcação 
# Descrição: com os pontos que constituem as quinas é possível
            criar uma limitacao que representa uma baliza da
            embarcação
'''
def criarHull(pontos,altura,largura):
    hull = ConvexHull(pontos)

    plt.plot(pontos[:, 0], pontos[:, 1], 'ro')
    for simplex in hull.simplices:
        plt.plot(pontos[simplex, 0], pontos[simplex, 1], 'k-')
    plt.axis([-1, altura * 2, -1, largura * 2], 'b')
    plt.show()


#plotagem da função relacionada ao angulo de deadrise
deadrise = int(input("Insira o angulo de Deadrise: "))
x = np.arange(-10.,100.,1.)
d = np.tan(angParaRad(deadrise))
#plt.plot(x, d * x, 'g')

#plotagem da função relacionada ao angulo de costado
largura = int(input("Insira a largura da meia boca: "))
altura  = int(input("Insira a altura da meia boca: "))
costado = int(input("Insira o angulo de Costado: "))

angBase = angComplemento(costado)
costado = angParaRad(costado)

coefA = np.tan(angParaRad(angBase))
pontoCostadoX = deslocamento(largura, altura, np.tan(costado))
m, c = encontraFuncao([(pontoCostadoX,0),(largura,altura)])

#encontro do ponto chine (interceção da funcão de deadrise e costado)
u, v = intercessao(d, m, c)
pontos = np.array([[0, altura],[0,0], [largura, altura], [u, v]])
print(pontos)
#marcação dos pontos que representam as "quinas" da embarcação
criarHull(pontos,altura,largura)

#plt.plot([0, 0,largura, u],[altura, 0, altura, v],'ro')

#configurações básicas da figura
# plt.grid(True)
# plt.axis([-1,altura*2,-1,largura*2], 'b')
# plt.show()


