import sympy as sp
from .utils import parsear_funcion

def resolver_newton_raphson(expr_str: str, x0: float, tol: float, max_iter: int = 100):
    expr, var, f = parsear_funcion(expr_str)
    expr_df = sp.diff(expr, var)
    df = sp.lambdify(var, expr_df, modules=['math', 'sympy'])

    iteraciones = []
    x_actual = x0

    for i in range(1, max_iter + 1):
        fx = float(f(x_actual))
        dfx = float(df(x_actual))

        if dfx == 0:
            raise ValueError(f"La derivada f'({x_actual}) es cero.")

        x_siguiente = x_actual - (fx / dfx)
        error = abs(x_siguiente - x_actual)

        iteraciones.append({
            "iteracion": i,
            "x": round(x_actual, 6),
            "fx": round(fx, 6),
            "dfx": round(dfx, 6),
            "x_siguiente": round(x_siguiente, 6),
            "error": round(error, 6)
        })

        if error < tol or abs(fx) < tol:
            break

        x_actual = x_siguiente

    return {
        "variable": str(var),
        "expresion": str(expr),
        "derivada": str(expr_df),
        "iteraciones": iteraciones
    }