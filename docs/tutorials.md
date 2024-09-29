# Tutorial

Asumamos que queremos estudiar la evolución temporal de un estado $\mathbf{y}(t)$. Este estado será representado mediante una matriz 2x2 que corresponde a algún operador lineal. La función que genera la dinámica del problema es 
$$
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
$$
donde $\mathbf{O}$ es otro operador lineal, ${\rm{i}}$ es la constante compleja y $[A, B] = AB - BA$ es un operación de conmutación. Note que **la función $f(t, \mathbf{y})$ no depende explícitamente de la variable temporal**.

La dinámica del problema depende intrínsicamente del operador 𝐎. Escojamos el siguiente operador:
``` py
import numpy as np

oOper = np.array([[0, 1], [1, 0]])
```

Dicho operador puede tener distintos significados físicos dependiendo del problema dinámico en cuestión. Puede representar un mapa algebraico, el generador dinámico de un sistema caótico, un Hamiltoniano, etc. 

Lo siguiente es difinir un estado inicial. De igual forma, dicho estado puede representar cantidades físicas de un sistema. Consideremos:

``` py 
yInit = np.array([[1, 0], [0, 0]])
```

def dyn_generator(oper, state):
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    k_1 = h*func(oper, state)
    k_2 = h*func(oper, state+k_1/2)
    k_3 = h*func(oper, state+k_2/2)
    k_4 = h*func(oper, state+k_3)
    return state + 1/6 * (k_1 + 2*k_2 + 2*k_3 + k_4)


Con estas funciones a nuestra disposición, podemos evaluar la dinámica temporal en una grilla temporal unidimensional.
``` py 
times = np.linspace(0.0, 10.0, num=500)

h = times[1] - times[0]
```

Y, finalmente, llamamos de manera iterativa la rutina `rk4()`, calculando el operador del estado del sistema $\mathbf{y}(t)$ a través del tiempo. A travéz del tiempo, vamos a guardar la entrada $(0, 0)$ y $(1, 1)$ de la matriz $\mathbf{y}(t)$. 

Para esto, vamos a inicializar dos arreglos que van a contener los valores con valores iniciales cero. Utilizamos el mismo tamaño del arreglo que contiene la variable independiente temporal: 
``` py
stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)
``` 

for tt in range(times.size):
    # Guarde el valor de las entradas (0,0) y (1,1) en los arreglos que definimos
    # Obtenga estos valores de las entradas de yInit
    # Código aquí ->
    stateQuant00[tt] = yInit[0,0].real
    stateQuant11[tt] = yInit[1,1].real

    # Invoque rk4 operando sobre yInit
    # y devuelva el resultado a un nuevo yN
    # Código aquí ->
    yN = rk4(dyn_generator, oOper, yInit, h)

    # Ahora asignamos yN a yInit
    # De esta manera, en la siguiente iteración, el operador de esta iteración se convierte en el inicial
    # de la siguiente iteración
    yInit = yN


import matplotlib.pyplot as plt

t = times
y_00 = stateQuant00
y_11 = stateQuant11 

fig, axes = plt.subplots()
plt.xlabel('Tiempo')
plt.ylabel('Valor del estado')
axes.plot(t, y_00, 'b')
twin_axes = axes.twiny()
twin_axes.plot(t, y_11, 'r')




