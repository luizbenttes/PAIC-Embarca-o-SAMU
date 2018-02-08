import numpy as np

def GEPP(A, b, doPricing = True):
	'''
	Gaussian elimination with partial pivoting.
	
	input: A is an n x n numpy matrix
		   b is an n x 1 numpy array
	output: x is the solution of Ax=b 
			with the entries permuted in 
			accordance with the pivoting 
			done by the algorithm
	post-condition: A and b have been modified.
	'''
	n = len(A)
	if b.size != n:
		raise ValueError("Invalid argument: incompatible sizes between"+
						 "A & b.", b.size, n)
	# k represents the current pivot row. Since GE traverses the matrix in the 
	# upper right triangle, we also use k for indicating the k-th diagonal 
	# column index.
	
	# Elimination
	for k in range(n-1):
		if doPricing:
			# Pivot
			maxindex = abs(A[k:,k]).argmax() + k
			if A[maxindex, k] == 0:
				raise ValueError("Matrix is singular.")
			# Swap
			if maxindex != k:
				A[[k,maxindex]] = A[[maxindex, k]]
				b[[k,maxindex]] = b[[maxindex, k]]
		else:
			if A[k, k] == 0:
				raise ValueError("Pivot element is zero. Try setting doPricing to True.")
		#Eliminate
		for row in range(k+1, n):
			multiplier = A[row,k]/A[k,k]
			A[row, k:] = A[row, k:] - multiplier*A[k, k:]
			b[row] = b[row] - multiplier*b[k]
	# Back Substitution
	x = np.zeros(n)
	for k in range(n-1, -1, -1):
		x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
	return x

def Bj(i,j,derivate,u):
	
	if derivate:
		if i == 3:
			derivate3 = [-3*((1-u)**2),
						3*((1-u)**2)-6*u*(1-u),
						(6*u*(1-u))-3*u**2,
						3*(u**2)]
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
						3*(np.power(u,2)),
						3*(np.power(u,2))]
			print("entrou")
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
	return result

def uStar(K0,K1,K2,k):
	u = np.power(dist(K0,K1),k)/(np.power(dist(K0,K1),k) + np.power(dist(K1,K2),k))
	return u 


def MatrixCenterLine(alphak,Hs,Ls,L0,Lc,Hc,K0,K1,K2,k=1):
	derivate = False
	a_12 = -(np.tan(np.deg2rad(alphak)))
	u = uStar(K0,K1,K2,k)
	a_20 = Bj(3,1,derivate,u)
	a_22 = Bj(3,2,derivate,u)
	a_31 = Bj(3,1,derivate,u)
	a_33 = Bj(3,2,derivate,u)

	A = [[0,1,0,0],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]

	b_1 = Hs - (np.tan(np.deg2rad(alphak))*Ls)
	b_2 = Lc - (Bj(3,0,derivate,u)*L0) - (Bj(3,3,derivate,u)*Ls)
	b_3 = Hc - (Bj(3,3,derivate,u)*Hs)

	B = [0,b_1,b_2,b_3]

	return A,B

def MatrixConstructor():
	Ls = 124.0
	L0 = 66.5
	Lc = 114.4
	Hs = 16.3
	Hc = 11.2
	alphak = 29

	K0 = [L0,0]
	K1 = [Lc,Hc]
	K2 = [124.0,16.3]

	return MatrixCenterLine(alphak,Hs,Ls,L0,Lc,Hc,K0,K1,K2,k=1)


if __name__ == "__main__":
	A, b = MatrixConstructor()
	A = np.array(A)
	b =  np.array(b)
	print (GEPP(np.copy(A), np.copy(b), doPricing = True))
	print (GEPP(A,b)) 
	

