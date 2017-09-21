
"""
Criado em (date)

@author: Luiz Bentes
"""

import matplotlib.pyplot as plt


Bxt = int(input("Valor de Bxt: "))
Bxt = Bxt/2
BxLin = int(input("Valor de BxLin: "))
BxLin = BxLin/2
xLin = int(input("Valor de xLin: "))

#precisa-se fazer as retas em paralelo e em duplas
plt.plot([-Bxt,-Bxt],[0, xLin],'g')
plt.plot([Bxt,Bxt],[0, xLin],'g')
plt.grid(True)
plt.show()
