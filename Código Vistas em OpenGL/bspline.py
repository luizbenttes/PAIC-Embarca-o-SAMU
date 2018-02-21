import numpy as np
def Bj(i,j,derivate,u):
	
	if derivate:
		if i == 3:
			derivate3 = [-3*(np.power((1-u),2)),
						3*(np.power((1-u),2))-6*u*(1-u),
						(6*u*(1-u))-3*np.power(u,2),
						3*(np.power(u,2))]
			return derivate3[j]
		elif i == 2:
			derivate2 = [-2*(1-u),
						2-(4*u),
						2*u,
						0]
			return derivate2[j]
	else:
		if i == 3:
			normal3 = [np.power((1-u),3),
						3*u*(np.power((1-u),2)),
						3*(np.power(u,2))*(1-u),
						(np.power(u,3))]
			return normal3[j]
		elif i == 2:
			normal2 = [np.power((1-u),2),
						2*u(1-u),
						np.power(u,2),
						0]
			return normal2[j]



def dist(a,b):
	'''
	Euclidian distance between 2 points
	input: a is the coordinate of the first point (x,y,z)
		   b is the coordinate of the second point (x,y,z)
	output: the distance in straight line of these points.
	post-condition: no modifications
	'''

	result = (np.sqrt(np.power((a[0]-b[0]),2)+np.power((a[1]-b[1]),2)))
	#+np.power((a[2]-b[2]),2)
	#print(result)
	return result

def uStar(K0,K1,K2,k):
	a = np.power(dist(K0,K1),k)
	b = np.power(dist(K1,K2),k)

	u = a/(a + b)
	return u 
