import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

def hull3D(pts,altura,largura):
    #pts = np.array([[0.,10.],[0.,0.],[10.,10.],[8.18105591, 1.44254089],[-10.,10.],[ -8.18105591,1.44254089]])

    hull = ConvexHull(pts)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for i in range(12):
    # Plot defining corner points
        ax.plot(pts.T[0], pts.T[1],i+2, "ko")

        for s in hull.simplices:
            s = np.append(s, s[0])  # Here we cycle back to the first coordinate
            ax.plot(pts[s, 0], pts[s, 1],i+2, "r-")

    plt.axis([-altura*2, altura * 2, -largura*2, largura * 2], 'b')
    plt.show()

pts = np.array([[0.,10.],[0.,0.],[10.,10.],[8.18105591, 1.44254089],[-10.,10.],[ -8.18105591,1.44254089]])
altura = 10
largura = 10
hull3D(pts,altura,largura)