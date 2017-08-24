import matplotlib.pyplot as plt
import numpy as np
import math

def AngToRad(ang):
    return ang * 2 * math.pi / 360.0
    
deadrise = int(input("Insira o angulo de Deadrise: "))
x = np.arange(10)
t = math.tan(AngToRad(deadrise))

plt.plot(x, t * x)
plt.legend(['y ='+str(t)+'x'], loc='upper left')
plt.grid(True)
#plt.show()

largura = input("Insira a largura da meia boca")
#costado = int(input("Insira o angulo de Costado: "))
#plt.plot(x , 5 * x + 3)
#plt.show()

