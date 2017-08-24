import matplotlib.pyplot as plt
import numpy as np
import math

def AngToRad(ang):
    return ang * 2 * math.pi / 360.0


def AngComplement(ang):
    return 90 - ang

deadrise = int(input("Insira o angulo de Deadrise: "))
x = np.arange(0,20,1)
d = np.tan(AngToRad(deadrise))

plt.plot(x, d * x, 'g')
plt.legend(['y ='+str(d)+'x'], loc='upper left')
plt.grid(True)
#plt.show()

#largura = int(input("Insira a largura da meia boca: "))
costado = int(input("Insira o angulo de Costado: "))
costado = AngComplement(costado)
c = np.tan(AngToRad(costado))

plt.plot(x, c * x, 'r')

#plt.axvline(x = largura)

plt.show()
#plt.plot(x , 5 * x + 3)
#plt.show()

