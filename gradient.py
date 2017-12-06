import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FormatStrFormatter

def fun(x,y):
    return ((4-((2.1)*(x**2))+((1/3)*(x**4)))*(x**2))+(x*y)-((4*(1-(y**2)))*(y**2))

def gradx(x,y):
	return 8*x-8.4*(x**3)+2*(x**5)+y

def grady(x,y):
	return x+16*(y**3)-8*y

def hessxx(x):
	return 8-25.2*(x**2)+10*(x**4)

def hessyy(y):
	return 48*(y**2)-8


maxiter = int(input("Máximo de iterações: "))
a = float(input("Valor do alfa: "))
x = float(input("Valor inicial do x: ")) 
y = float(input("Valor inicial do y: "))
tol = float(input("Valor da toleancia: "))

iter = 0 #iterações inicializa com zero.

p = np.array([gradx(x,y),grady(x,y)])
old = np.array([x,y])
d = -p

while iter<maxiter or err<tol:
	new = old + a*d
	err = abs(fun(old[0],old[1])-fun(new[0],new[1]))
	print("Novo x:")
	print(new)
	print("\n")
	print("valor de f(x,y):")
	print(fun(new[0],new[1]))
	old = new
	iter = iter + 1
	print("passo:",iter)
	print("\n")
