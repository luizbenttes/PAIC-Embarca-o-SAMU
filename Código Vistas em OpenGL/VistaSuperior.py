import numpy as np
import gauss as gs 
import bspline as bs 

def MatrixChine(Lc, Bc, alphaC, C0, Cx, C2,k):
	derivate = True
	u = bs.uStar(C0,Cx,C2,k)
	a_01 = bs.Bj(3,1,derivate,u)
	a_03 = bs.Bj(3,2,derivate,u)

	a_12 = -(np.tan(alphaC))
	derivate = False
	a_20 = bs.Bj(3,1,derivate,u)
	a_22 = bs.Bj(3,2,derivate,u)
	a_31 = bs.Bj(3,1,derivate,u)
	a_33 = bs.Bj(3,2,derivate,u)

	A = [[0,a_01,0,a_03],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]
	print("A: ",A)

	derivate = True
	b_0 = -(bs.Bj(3,0,derivate,u)*Bc)
	b_1 = - (np.tan(alphaC)*Lc)
	derivate = False
	b_2 = Cx[0] - (bs.Bj(3,3,derivate,u)*Lc)
	b_3 = Cx[1] - (bs.Bj(3,1,derivate,u)*Bc)

	B = [b_0,b_1,b_2,b_3]
	print("B: ",B)

	return A, B


def MatrixSheer(Ls, Bs, alphaS, S0, Sx, S2,k):
	derivate = True
	u = bs.uStar(S0,Sx,S2,k)
	a_01 = bs.Bj(3,1,derivate,u)
	a_03 = bs.Bj(3,2,derivate,u)

	a_12 = -(np.tan(alphaS))
	derivate = False
	a_20 = bs.Bj(3,1,derivate,u)
	a_22 = bs.Bj(3,2,derivate,u)
	a_31 = bs.Bj(3,1,derivate,u)
	a_33 = bs.Bj(3,2,derivate,u)

	A = [[0,a_01,0,a_03],
		[0,0,a_12,1],
		[a_20,0,a_22,0],
		[0,a_31,0,a_33]]
	print("A: ",A)

	derivate = True
	b_0 = -(bs.Bj(3,0,derivate,u)*Bs)
	b_1 = - (np.tan(alphaS)*Ls)
	derivate = False
	b_2 = Sx[0] - (bs.Bj(3,3,derivate,u)*Ls)
	b_3 = Sx[1] - (bs.Bj(3,1,derivate,u)*Bs)

	B = [b_0,b_1,b_2,b_3]
	print("B: ",B)

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
	Bs = 11.1
	Lx = 62.8
	Bx = 13.7
	Bc = 10.2 

	alpha_S = np.deg2rad(1)
	alphaS = np.deg2rad(129)
	beta_S = np.deg2rad(2)
	beta_C = np.deg2rad(0)
	alpha_C = np.deg2rad(8)
	alphaC = np.deg2rad(180 - 24)
	betaC = 0
	alphak = np.deg2rad(29)

	K0 = [L0,0]
	K1 = [Lc,Hc]
	K2 = [Ls,Hs]
	C_2 = [Lc,Hc] 

	S_0 = [0,hs]
	S_2 = [Ls,Hs]
	S0 = [0,Bs]
	Sx = [Lx,Bx]
	Cx = [80, 80]
	S2 = [Ls,0]

	C0 = [0,Bc]
	C2 = [Lc,0]


	#A_center,B_center = MatrixCenterLine(alphak,Hs,Ls,L0,Lc,Hc,K0,K1,K2,k=0.5)
	A_sheer, B_sheer =  MatrixSheer(Ls, Bs, alphaS, S0, Sx, S2, k=1)
	A_chine, B_chine =  MatrixChine(Lc, Bc, alphaC, C0, Sx, C2, k=1)
	#A_chine, B_chine =  MatrixChine(Lc, Hc, hc, alpha_C, beta_C, C_0, C_1, C_2, k=1)

	return A_sheer, B_sheer, S0, S2, A_chine, B_chine, C0, C2


if __name__ == "__main__":
	A_sheer, B_sheer, S0, S2, A_chine, B_chine, C0, C2 = MatrixConstructor()

	A_sheer = np.array(A_sheer)
	B_sheer =  np.array(B_sheer)
	print ("Resposta: ", gs.GEPP(np.copy(A_sheer), np.copy(B_sheer), doPricing = True),"\n")
	R2 = gs.GEPP(A_sheer,B_sheer)

	pontosLinhaSheer = []
	pontosLinhaSheer.append(S0)
	pontosLinhaSheer.append([R2[0],R2[1]])
	pontosLinhaSheer.append([R2[2],R2[3]])
	pontosLinhaSheer.append(S2)


	print("Linha Sheer: ", pontosLinhaSheer)


	A_chine = np.array(A_chine)
	B_chine =  np.array(B_chine)
	print ("Resposta: ", gs.GEPP(np.copy(A_chine), np.copy(B_chine), doPricing = True),"\n")
	R2 = gs.GEPP(A_chine,B_chine)

	pontosLinhaChine = []
	pontosLinhaChine.append(C0)
	pontosLinhaChine.append([R2[0],R2[1]])
	pontosLinhaChine.append([R2[2],R2[3]])
	pontosLinhaChine.append(C2)


	print("Linha Chine: ", pontosLinhaChine)


	

