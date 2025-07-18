import numpy as np

def forward_difference(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h=1e-6):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == "__main__":
    def test_function(x):
        return x**2
    x = 2.0
    forward = forward_difference(test_function, x)
    backward = backward_difference(test_function, x)
    central = central_difference(test_function, x)
    print(f"Derivada em x={x} para f(x)=x²:")
    print(f"Diferença para frente: {forward}")
    print(f"Diferença para trás: {backward}")
    print(f"Diferença central: {central}")
    print(f"Valor analítico (2x): {2*x}")