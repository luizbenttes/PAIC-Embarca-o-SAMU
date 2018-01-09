import matplotlib.pyplot as plt
from numpy import ones, vstack
from numpy.linalg import lstsq
import numpy as np
import math

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
    plt.plot(x, a * x + b)
    plt.axis([-10, 10, -10, 10], 'g')
    plt.show()

alfaBow = 12
t = math.tan(AngToRad(alfaBow))

ponto = [5,3]
funcaoPontoAngulo(ponto,t)
#m,c = encontraFuncao([(xBase,0),(comprimento,dBow)])
# x = np.arange(-10., 100., 1.)
# plt.plot(x, m * x + c)
#

# plt.show()