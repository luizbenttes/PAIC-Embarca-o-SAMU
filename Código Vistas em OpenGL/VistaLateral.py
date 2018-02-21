import numpy as np
import gauss as gs 
import bspline as bs 

def MatrixChine(Lc, Hc, hc, alpha_C, beta_C, C_0, C_1, C_2, k):
	derivate = False
	a_00 = -(np.tan(beta_C))
	a_12 = -(np.tan(alpha_C))
	u = bs.uStar(C_0,C_1,C_2,k)
	a_20 = bs.Bj(3,1,derivate,u)
	a_22 = bs.Bj(3,2,derivate,u)
	a_31 = bs.Bj(3,1,derivate,u)
	a_33 = bs.Bj(3,2,derivate,u)

	A = [[a_00,1,0,0],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]
	print("A: ",A)

	b_1 = Hc - (np.tan(alpha_C)*Lc)
	b_2 = C_1[0] - (bs.Bj(3,3,derivate,u)*Lc)
	b_3 = C_1[1] - (bs.Bj(3,0,derivate,u)*hc) - (bs.Bj(3,3,derivate,u)*Hc)

	B = [hc,b_1,b_2,b_3]
	print("B: ",B)

	return A, B

def MatrixCenterLine(alphak,Hs,Ls,L0,Lc,Hc,K0,K1,K2,k):
	derivate = False
	a_12 = -(np.tan(alphak))
	u = bs.uStar(K0,K1,K2,k)
	a_20 = bs.Bj(3,1,derivate,u)
	a_22 = bs.Bj(3,2,derivate,u)
	a_31 = bs.Bj(3,1,derivate,u)
	a_33 = bs.Bj(3,2,derivate,u)

	A = [[0,1,0,0],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]
	print("A: ",A)

	b_1 = Hs - (np.tan(alphak)*Ls)
	b_2 = Lc - (bs.Bj(3,0,derivate,u)*L0) - (bs.Bj(3,3,derivate,u)*Ls)
	b_3 = Hc - (bs.Bj(3,3,derivate,u)*Hs)

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
	print ("Resposta: ", gs.GEPP(np.copy(A_center), np.copy(B_center), doPricing = True),"\n")
	R = gs.GEPP(A_center,B_center)

	pontosLinhaCentral = []
	pontosLinhaCentral.append(K0)
	pontosLinhaCentral.append([R[0],R[1]])
	pontosLinhaCentral.append([R[2],R[3]])
	pontosLinhaCentral.append(K2)

	print("Linha Central: ",pontosLinhaCentral)


	A_sheer = np.array(A_sheer)
	B_sheer =  np.array(B_sheer)
	print ("Resposta: ", gs.GEPP(np.copy(A_sheer), np.copy(B_sheer), doPricing = True),"\n")
	R2 = gs.GEPP(A_sheer,B_sheer)

	pontosLinhaSheer = []
	pontosLinhaSheer.append(S_0)
	pontosLinhaSheer.append([R2[0],R2[1]])
	pontosLinhaSheer.append(S_2)


	print("Linha Sheer: ", pontosLinhaSheer)

	A_chine = np.array(A_chine)
	B_chine =  np.array(B_chine)
	print ("Resposta: ", gs.GEPP(np.copy(A_chine), np.copy(B_chine), doPricing = True),"\n")
	R3 = gs.GEPP(A_chine,B_chine)

	pontosLinhaChine = []
	pontosLinhaChine.append(C_0)
	pontosLinhaChine.append([R3[0],R3[1]])
	pontosLinhaChine.append([R3[2],R3[3]])
	pontosLinhaChine.append(C_2)

	print("Linha Chine: ",pontosLinhaChine)


	

