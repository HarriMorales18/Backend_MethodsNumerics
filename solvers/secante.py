import sympy as sp
from .utils import parsear_funcion

def resolver_secante(expresion_str: str, x0: float, x1: float, tol: float, max_iter: int = 100):
    # 1. Parsear la función f(x)
    expr_f, var, f = parsear_funcion(expresion_str)

    iteraciones = []
    x_prev = x0
    x_actual = x1

    for i in range(1, max_iter + 1):
        try:
            f_prev = float(f(x_prev))
            f_actual = float(f(x_actual))
        except (OverflowError, ValueError):
            raise ValueError(
                f"El método divergió en la iteración {i}. La función seleccionada no es adecuada."
            )

        denominador = f_actual - f_prev
        if denominador == 0:
            raise ValueError(
                f"División por cero detectada en la iteración {i} (f(x1) - f(x0) = 0). El método no puede continuar."
            )

        # 2. Aplicar fórmula del método de la secante:
        x_siguiente = x_actual - (f_actual * (x_actual - x_prev)) / denominador
        error = abs(x_siguiente - x_actual)

        iteraciones.append({
            "iteracion": i,
            "x0": round(x_prev, 6),
            "x1": round(x_actual, 6),
            "x_siguiente": round(x_siguiente, 6),
            "f_x0": round(f_prev, 6),
            "f_x1": round(f_actual, 6),
            "error": round(error, 6)
        })

        if error < tol:
            break

        # Actualizar puntos para el siguiente ciclo
        x_prev = x_actual
        x_actual = x_siguiente

    return {
        "variable": str(var),
        "expresion": str(expr_f),
        "raiz": round(x_actual, 6),
        "iteraciones": iteraciones
    }