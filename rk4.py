import numpy as np

def dyn_generator(oper, state):
    """Generador dinámico de dos ndarrays.

    Esta función calcula el generador dinámico al multiplicar las matrices
    `oper` y `state`, y restarle la multiplicación en el orden inverso de las
    mismas. El resultado se multiplica por -1.0j (imaginario).

    Examples:
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        [[0.-0.j 0.+1.j]
         [0.-1.j 0.-0.j]]

    Args:
        oper (ndarray): Primera matriz.
        state (ndarray): Segunda matriz.

    Returns:
        ndarray: Devuelve el generador dinámico resultante de la operación.

    """
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))

print(help(dyn_generator)) 


def rk4(func, oper, state, h):
    """Implementación del método Rung-Kutta de orden 4 (RK4) sin una dependencia explícita de la variable temporal.

    Examples:
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.2)
        [[0.96053333+0.j        , 0.        +0.19466667j],
         [0.        -0.19466667j, 0.03946667+0.j        ]]

    Args:
        func (callable): Función que describe la evolución del sistema.
            Debe aceptar dos argumentos: `oper` y `state`.
        oper (ndarray): Operador lineal (matriz en este caso) y primer argumento
            que se pasa a la función `func`.
        state (ndarray): Estado actual del sistema (matriz en este caso) y
            segundo argumento que se pasa a la función `func`.
        h (float): Tamaño del paso que determina el intervalo de tiempo entre
            los estados calculados.

    Returns:
        ndarray: El nuevo estado del sistema después de aplicar el método RK4.

    """
    k_1 = func(oper, state)
    k_2 = func(oper, state + k_1 / 2)
    k_3 = func(oper, state + k_2 / 2)
    k_4 = func(oper, state + k_3)
    return state + 1 / 6 * h * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

print(help(rk4))
