import numpy as np

def riemann_sum_left(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b - dx, n)
    return np.sum(f(x)) * dx

def riemann_sum_right(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a + dx, b, n)
    return np.sum(f(x)) * dx

def riemann_sum_midpoint(f, a, b, n):
    dx = (b - a) / n
    x = np.linspace(a + dx/2, b - dx/2, n)
    return np.sum(f(x)) * dx

if __name__ == "__main__":
    def test_function(x):
        return x**2
    a, b = 0, 2
    n = 1000
    left = riemann_sum_left(test_function, a, b, n)
    right = riemann_sum_right(test_function, a, b, n)
    midpoint = riemann_sum_midpoint(test_function, a, b, n)
    print(f"Soma de Riemann para f(x)=x² de {a} a {b} com {n} subintervalos:")
    print(f"Soma à esquerda: {left}")
    print(f"Soma à direita: {right}")
    print(f"Soma pelo ponto médio: {midpoint}")
    print(f"Valor analítico (x³/3): {(b**3 - a**3)/3}")