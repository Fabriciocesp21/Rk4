#!/usr/bin/env python

import numpy as np

oOper = np.array([[0, 1], [1, 0]])

print(oOper)

yInit = np.array([[1, 0], [0, 0]])

print(yInit)

def dyn_generator(oper, state):
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))

def rk4(func, oper, state, h):
    k_1 = h*func(oper, state)
    k_2 = h*func(oper, state+k_1/2)
    k_3 = h*func(oper, state+k_2/2)
    k_4 = h*func(oper, state+k_3)
    return state + 1/6 * (k_1 + 2*k_2 + 2*k_3 + k_4)

times = np.linspace(0.0, 10.0, num=500)

h = times[1] - times[0]
# h = 1/(num-1)

stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

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

# Código aquí ->
t = times
y_00 = stateQuant00
y_11 = stateQuant11 

fig, axes = plt.subplots()
plt.xlabel('Tiempo')
plt.ylabel('Valor del estado')
axes.plot(t, y_00, 'b')
twin_axes = axes.twiny()
twin_axes.plot(t, y_11, 'r')

plt.show()
plt.close()

