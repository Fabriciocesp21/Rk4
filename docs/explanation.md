# Explicación

##Método Runge-Kutta de orden 4 (RK4)

Una herramienta numérica (aproximación) para la resolución de ecuaciones diferenciales ordinarias con valores iniciales, son los métodos de Runge-Kutta. En este caso, se trabaja el de orden 4.

$$
\begin{align}
    y_{n+1} &= y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right)  \\
    k_1 &= hf(t_n, y_n ) \\
    k_2 &= hf\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)  \\
    k_3 &= hf\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right)  \\
    k_4 &= hf\left(t_n + h, y_n + k_3\right) \\
\end{align}
$$

La primera línea indica la ecuación principal del método. Las siguientes líneas indican la manera de calcular los términos $k_n$. El valor $h$ indica un incremento, un paso del tiempo. Mientras que $y_n$ es el estado del sistema en el tiempo $t_n$. Los términos $k$ indican diferentes pendientes, que necesitan de una pendiente anterior para su cálculo (a excepción de la primera).

El método se realiza de manera iterativa, en el cual, el valor $y_{n+1}$ es calculado por el valor en ese momento de $y_n$ y una pendiente promedio por el avance temporal. El error total de este método es de orden 4 ( $O(h^4)$ ).

