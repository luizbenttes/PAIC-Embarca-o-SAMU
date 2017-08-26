import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def fun (a,b,x,y):
    return a * x - y + b

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
funcoesCasco = [-1,2,20,0]
for i in range(2):
  x = y = np.arange(-3.0, 3.0, 0.5)
  X, Y = np.meshgrid(x, y)
  zs = np.array([fun(funcoesCasco[i],funcoesCasco[i+1],x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
  Z = zs.reshape(X.shape)
  ax.scatter(X, Y, Z)

# ax.scatter(X, Y, Z2)
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

plt.show()