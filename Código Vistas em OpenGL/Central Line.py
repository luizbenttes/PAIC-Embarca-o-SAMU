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

def MatrixChine(Lc, Hc, hc, alpha_C, beta_C, C_0, C_1, C_2, k):
	derivate = False
	a_00 = -(np.tan(beta_C))
	a_12 = -(np.tan(alpha_C))
	u = uStar(C_0,C_1,C_2,k)
	a_20 = Bj(3,1,derivate,u)
	a_22 = Bj(3,2,derivate,u)
	a_31 = Bj(3,1,derivate,u)
	a_33 = Bj(3,2,derivate,u)

	A = [[a_00,1,0,0],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]
	print("A: ",A)

	b_1 = Hc - (np.tan(alpha_C)*Lc)
	b_2 = C_1[0] - (Bj(3,3,derivate,u)*Lc)
	b_3 = C_1[1] - (Bj(3,0,derivate,u)*hc) - (Bj(3,3,derivate,u)*Hc)

	B = [hc,b_1,b_2,b_3]
	print("B: ",B)

	return A, B

def MatrixCenterLine(alphak,Hs,Ls,L0,Lc,Hc,K0,K1,K2,k):
	derivate = False
	a_12 = -(np.tan(alphak))
	u = uStar(K0,K1,K2,k)
	a_20 = Bj(3,1,derivate,u)
	a_22 = Bj(3,2,derivate,u)
	a_31 = Bj(3,1,derivate,u)
	a_33 = Bj(3,2,derivate,u)

	A = [[0,1,0,0],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]
	print("A: ",A)

	b_1 = Hs - (np.tan(alphak)*Ls)
	b_2 = Lc - (Bj(3,0,derivate,u)*L0) - (Bj(3,3,derivate,u)*Ls)
	b_3 = Hc - (Bj(3,3,derivate,u)*Hs)

	B = [0,b_1,b_2,b_3]
	print("B: ",B)

	return A, B

def MatrixSheer(Ls,Hs, hs, alpha_S, beta_S):
	A = [[(np.tan(beta_S)), -1],[-(np.tan(alpha_S)), 1]]
	B = [[-hs],[Hs -(np.tan(alpha_S))*Ls]]

	return A, B

def MatrixConstructor():
	Ls = 124.0
	L0 = 66.5
	Lc = 114.4
	Hs = 16.3
	Hc = 11.2
	hs = 12.8
	hc = 3.3
	Xc1 = 55.4
	Yc1 = 4.6

	alpha_S = np.deg2rad(1)
	beta_S = np.deg2rad(2)
	beta_C = np.deg2rad(0)
	alpha_C = np.deg2rad(8)
	alphak = np.deg2rad(29)

	K0 = [L0,0]
	K1 = [Lc,Hc]
	K2 = [Ls,Hs]
	C_2 = [Lc,Hc] 

	S_0 = [0,hs]
	S_2 = [Ls,Hs]

	C_0 = [0,hc]
	C_1 = [Xc1,Yc1]


	A_center,B_center = MatrixCenterLine(alphak,Hs,Ls,L0,Lc,Hc,K0,K1,K2,k=1)
	A_sheer, B_sheer =  MatrixSheer(Ls, Hs, hs, alpha_S, beta_S)
	A_chine, B_chine =  MatrixChine(Lc, Hc, hc, alpha_C, beta_C, C_0, C_1, C_2, k=1)

	return A_center, B_center, K0, K2, A_sheer, B_sheer, S_0, S_2, A_chine, B_chine, C_0, C_2


if __name__ == "__main__":
	A_center, B_center, K0, K2, A_sheer, B_sheer, S_0, S_2, A_chine, B_chine, C_0, C_2 = MatrixConstructor()
	A_center = np.array(A_center)
	B_center =  np.array(B_center)
	print ("Resposta: ", GEPP(np.copy(A_center), np.copy(B_center), doPricing = True),"\n")
	R = GEPP(A_center,B_center)

	pontosLinhaCentral = []
	pontosLinhaCentral.append(K0)
	pontosLinhaCentral.append([R[0],R[1]])
	pontosLinhaCentral.append([R[2],R[3]])
	pontosLinhaCentral.append(K2)

	print("Linha Central: ",pontosLinhaCentral)


	A_sheer = np.array(A_sheer)
	B_sheer =  np.array(B_sheer)
	print ("Resposta: ", GEPP(np.copy(A_sheer), np.copy(B_sheer), doPricing = True),"\n")
	R2 = GEPP(A_sheer,B_sheer)

	pontosLinhaSheer = []
	pontosLinhaSheer.append(S_0)
	pontosLinhaSheer.append([R2[0],R2[1]])
	pontosLinhaSheer.append(S_2)


	print("Linha Sheer: ", pontosLinhaSheer)

	A_chine = np.array(A_chine)
	B_chine =  np.array(B_chine)
	print ("Resposta: ", GEPP(np.copy(A_chine), np.copy(B_chine), doPricing = True),"\n")
	R3 = GEPP(A_chine,B_chine)

	pontosLinhaChine = []
	pontosLinhaChine.append(C_0)
	pontosLinhaChine.append([R3[0],R3[1]])
	pontosLinhaChine.append([R3[2],R3[3]])
	pontosLinhaChine.append(C_2)

	print("Linha Chine: ",pontosLinhaChine)


	

