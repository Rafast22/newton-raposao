import numpy as np 
import sympy as sp


def calculate_newton_raposao(fx):
    x = sp.Symbol('x')
    dfdx = sp.diff(fx, x)
    return sp.lambdify(x, dfdx)

def newton_raphson(x_symbol, f_symbol, dfdx_symbol, x0, tol=1e-6):
    """
    Implementa o método de Newton-Raphson para encontrar a raiz de uma função.

    Args:
        f: A função para a qual se deseja encontrar a raiz.
        df: A derivada da função f.
        x0: A estimativa inicial da raiz.
        tol: A tolerância para a convergência.
        max_iter: O número máximo de iterações.

    Returns:
        A raiz aproximada da função.
    """
    f = sp.lambdify(x_symbol, f_symbol)
    dfdx = sp.lambdify(x_symbol, dfdx_symbol)
    x = x0
    while True:
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = dfdx(x)
        if dfx == 0:
            print("Derivada nula. Método não converge.")
            return None
        x = x - fx / dfx

