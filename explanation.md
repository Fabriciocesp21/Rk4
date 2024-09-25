##Método Runge-Kutta de orden 4 (RK4)


\begin{equation}
    y_{n+1} = y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right)  \\
    k_1 = hf(t_n, y_n ) \\
    k_2 = hf\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)  \\
    k_3 = hf\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right)  \\
    k_4 = hf\left(t_n + h, y_n + k_3\right) \\
\end{equation}
