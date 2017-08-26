import matplotlib.pyplot as plt
import numpy as np
from numpy import ones,vstack
from numpy.linalg import lstsq
import math

'''
# Nome da funcão: angParaRad
# ang: angulo em graus
# Descricao: dado um angulo em graus é retornado 
            seu equivalente em radianos
'''
def angParaRad(ang):
    return ang * math.pi / 180.0


'''
# Nome da funcão: angComplemento
# ang: angulo em graus
# Descricao: retornar o complemento do angulo, dada
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
# Descricao: utilizando teorema de pitagoras,
            é encontrado o valor de deslocamento
            da reta após a insercao do angulo de costado
'''
def deslocamento(largura, altura, ang):
    return largura - (ang * altura)


'''
# Nome da funcão: encontraFuncao
# pontos: tupla contendo duas coordenadas no plano cartesiano
# Descricao: retornar a funcao y = mx + c 
            dado 2 pontos distintos retornando os coeficientes
            M e C
'''
def encontraFuncao(pontos):
    x_coords, y_coords = zip(*pontos)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    x = np.arange(-10., 100., 1.)
    plt.plot(x, m * x + c)
    return m, c


def findIntersection(fun1,fun2,x0):
    return fsolve(lambda x : fun1(x) - fun2(x),x0)

#plotagem da função relacionada ao angulo de deadrise
deadrise = int(input("Insira o angulo de Deadrise: "))
x = np.arange(-10.,100.,1.)
d = np.tan(angParaRad(deadrise))
plt.plot(x, d * x, 'g')

#plotagem da função relacionada ao angulo de costado
largura = int(input("Insira a largura da meia boca: "))
altura  = int(input("Insira a altura da meia boca: "))
costado = int(input("Insira o angulo de Costado: "))

angBase = angComplemento(costado)
costado = angParaRad(costado)

coefA = np.tan(angParaRad(angBase))
pontoCostadoX = deslocamento(largura, altura, np.tan(costado))
m, c = encontraFuncao([(pontoCostadoX,0),(largura,altura)])

#marcação do ponto chine (interceção da funcão de deadrise e costado)
y = d * x
g = m * x + c

# idx = np.argwhere(np.diff(np.sign((d * x)-(m * x + c))) != 0).reshape(-1) + 0
# plt.plot(x[idx], (d * x)[idx], 'ro')

#marcação dos pontos que representam as "quinas" da embarcação
plt.plot([0, 0,largura],[altura, 0,altura],'ro')

#configurações básicas da figura
plt.grid(True)
plt.axis([-1,altura*2,-1,largura*2], 'b')
plt.show()


