import sympy as sp
from .utils import parsear_funcion

def resolver_punto_fijo(g_str: str, x0: float, tol: float, max_iter: int = 100):
    # 1. Parsear la función g(x) y calcular su derivada g'(x) simbólicamente
    expr_g, var, g = parsear_funcion(g_str)
    expr_dg = sp.diff(expr_g, var)
    dg = sp.lambdify(var, expr_dg, modules=['math', 'sympy'])

    # 2. Evaluar el criterio de convergencia |g'(x0)| < 1
    val_dg_x0 = None
    cumple_criterio = None
    try:
        val_dg_x0 = float(dg(x0))
        cumple_criterio = abs(val_dg_x0) < 1.0
    except Exception:
        pass

    iteraciones = []
    x_actual = x0

    for i in range(1, max_iter + 1):
        try:
            x_siguiente = float(g(x_actual))
        except (OverflowError, ValueError):
            raise ValueError(
                f"El método divergió en la iteración {i}. La función g(x) seleccionada no es adecuada."
            )

        error = abs(x_siguiente - x_actual)

        iteraciones.append({
            "iteracion": i,
            "p0": round(x_actual, 6),
            "p1": round(x_siguiente, 6),
            "error": round(error, 6)
        })

        if error < tol:
            break

        x_actual = x_siguiente

    return {
        "variable": str(var),
        "expresion_g": str(expr_g),
        "derivada_g": str(expr_dg),
        "evaluacion_g_prima_x0": round(val_dg_x0, 6) if val_dg_x0 is not None else None,
        "cumple_criterio_convergencia": cumple_criterio,
        "iteraciones": iteraciones
    }