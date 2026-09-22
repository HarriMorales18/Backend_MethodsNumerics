from .utils import parsear_funcion

def resolver_falsa_posicion(expr_str: str, a: float, b: float, tol: float, max_iter: int = 100):
    expr, var, f = parsear_funcion(expr_str)
    fa, fb = float(f(a)), float(f(b))

    if fa * fb >= 0:
        raise ValueError("La función no cambia de signo en [a, b] (f(a)*f(b) >= 0).")

    iteraciones = []
    c_anterior = None

    for i in range(1, max_iter + 1):
        c = a - (fa * (b - a)) / (fb - fa)
        fc = float(f(c))
        error = abs(c - c_anterior) if c_anterior is not None else None

        iteraciones.append({
            "iteracion": i,
            "a": round(a, 6),
            "b": round(b, 6),
            "c": round(c, 6),
            "fc": round(fc, 6),
            "error": round(error, 6) if error is not None else None
        })

        if abs(fc) < tol or (c_anterior is not None and error < tol):
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c_anterior = c

    return {"variable": str(var), "expresion": str(expr), "iteraciones": iteraciones}