import matplotlib.pyplot as plt
import numpy as np


ep = 0.001

xn = 5
n = 0
dif = 50

xa = 1

#Ingresar la funcion
def f(x):
    
    return x**3-x-3 #x^3-3

print(f(xn))

#Derivada de la funcion
def f1(x):
   
    return 3*x**2-1

print(f1(xn))

#Metodo de Newton
def newton(x):
     
     return x - f(x)/f1(x)


# El método de la secante     
def secante(xn, xa):
    # El método de la secante no se puede aplicar si:

    if(f(xn) * f(xa) >= 0):
        print('El método de la secante no se puede aplicar')
        print("------------------------")
        
    
    else: # Cálculo de la secante
        print("Metodo secante\n")
        c = xa - f(xa)*(xn - xa)/(f(xn) - f(xa))
        
        if (f(c) == 0):
            return c
        
        elif(f(xa) * f(c) < 0):
            xn = c
            return xn
        
        else:
            xa = c
            return xa

# Valores del eje X que toma el gráfico.
cordx = np.arange(-15, 15,0.01)
# Graficar ambas funciones.

plt.plot(cordx, [f(i) for i in cordx])
plt.plot(cordx, [f1(i) for i in cordx])
# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")
# Limitar los valores de los ejes.
plt.xlim(-15, 15)
plt.ylim(-15, 15)
# Guardar gráfico como imágen PNG.
plt.savefig("output.png")
# Mostrarlo.
plt.show()


while (dif > ep):
    #Si n es impar usa el metodo de Newton, si es par usa metodo secante
    if(n % 2 == 0):
        print("Metodo de Newton\n")
        xn = newton(xn)
        dif = np.abs(xn - newton(xn))
        
        n += 1
       
    else:
       xn = secante(xa,xn)
       dif = dif/n
      
       n += 1
       

    #Calculo de error 
    error = np.log2(np.absolute(xa-xn)/ep)
    
    #impresion de resultados de cada vuelta
    print("Error: ", error )
    print("xn: ", xn)
    print("dif: ", dif)
    print("n: ", n)
    print("---------------------")

#Resultados finales
print("\n El resultado es: ", xn)
print("\n Error: ", error )

