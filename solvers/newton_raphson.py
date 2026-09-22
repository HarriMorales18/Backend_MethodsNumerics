from typing import Dict, Any
import sympy as sp

def resolver_newton_raphson(expresion: str, x0: float, tolerancia: float, max_iter: int = 100) -> Dict[str, Any]:
    x = sp.Symbol('x')
    f_expr = sp.sympify(expresion)
    df_expr = sp.diff(f_expr, x)  # Derivada analítica automática

    f = sp.lambdify(x, f_expr, 'math')
    df = sp.lambdify(x, df_expr, 'math')

    iteraciones = []
    xi = float(x0)

    for i in range(1, max_iter + 1):
        df_val = df(xi)
        if df_val == 0:
            raise ValueError(f"La derivada f'(x) se anuló en x = {xi}. El método se detiene.")

        f_val = f(xi)
        xi_sig = xi - (f_val / df_val)
        error = abs(xi_sig - xi)

        iteraciones.append({
            "iteracion": i,
            "xi": round(xi, 6),
            "f_xi": round(f_val, 6),
            "df_xi": round(df_val, 6),
            "xi_siguiente": round(xi_sig, 6),
            "error": round(error, 6)
        })

        if error < tolerancia:
            break

        xi = xi_sig

    return {
        "derivada": str(df_expr),
        "iteraciones": iteraciones
    }