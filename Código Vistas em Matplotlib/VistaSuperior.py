
"""
Criado em

@author: Luiz Bentes
"""

import matplotlib.pyplot as plt

def VistaSuperior(ComprimentoChine, ComprimentoBarco):
    Bxt = int(input("Valor de Bxt: "))
    Bxt = Bxt/2
    BxLin = int(input("Valor de BxLin: "))
    BxLin = BxLin/2
    xLin = int(input("Valor de xLin: "))

    #precisa-se fazer as retas em paralelo e em duplas
    #deck
    plt.plot([-Bxt,-Bxt],[0, xLin],'g')
    plt.plot([Bxt,Bxt],[0, xLin],'g')
    plt.plot([0,-Bxt],[ComprimentoBarco,xLin],'g')
    plt.plot([0, Bxt], [ComprimentoBarco, xLin], 'g')
    #linha do chine
    plt.plot([-BxLin, -BxLin], [0, xLin], 'b')
    plt.plot([BxLin, BxLin], [0, xLin], 'b')
    #encontro linha chine e base
    #plt.plot([0,0],[0,ComprimentoChine],'p')
    plt.plot([-BxLin,0],[xLin,ComprimentoChine],'b')
    plt.plot([BxLin, 0], [xLin, ComprimentoChine], 'b')
    #base
    plt.plot([0,0],[0,ComprimentoBarco],'r')

    plt.plot()
    plt.grid(False)
    plt.axis([-Bxt*3, Bxt*3,0, ComprimentoBarco*1.2], 'b')
    plt.show()

VistaSuperior(27,30)