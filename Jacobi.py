import numpy as np

A = np.array([[2,-1,1], [3,3,9],[3,3,5]],float)
b = np.array([[-1],[0],[4]], float) 
x = np.array([[0],[1],[1]],float)

print ("\nMatriz A:\n", A)

print ("\nVector b:\n", b)

print("\nVector x:\n", x)


def jacobi(a,b,x): 

	n = len(x) 
	t = x.copy()
	
	for i in range(n): 
		s = 0
		for j in range(n): 
			if i != j:
				s = s+a[i,j]*t[j]
				x[i] = (b[i]-s)/a[i,i]
	return x


def jacobim(a,b,x,e,m): 
	
	n = len(x)  

	t = x.copy()
	
	for  k  in  range(m): 

		x = jacobi(a,b,x)
		d = np.linalg.norm(np.array(x) - np.array(t), np.inf)
		
		print("Para la iteración "+str(k+1)+": X = "+str(np.transpose(x.round(7))) + "\t Error: "+str(abs(d)))

		if d<e:

			return [x,k] 
		
		else:

			t = x.copy() 

	return [[],m]





maxite = 100
print("\nNuméro de iteraciones = ", maxite, "\n")


# X es la solución y k las iteraciones
[x,k] = jacobim(A,b,x,1.e-14,maxite)

if(k == maxite):
	print("\nEl método diverge o no converge para la cota de error pedido")

else: 
	print("\nEl vector 'x' es:")
	print(x)

	print("\nEl numero de iteraciones es: "+str(k+1))


