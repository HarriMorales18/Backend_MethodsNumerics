from .utils import parsear_funcion

def resolver_biseccion(expr_str: str, a: float, b: float, tol: float, max_iter: int = 100):
    expr, var, f = parsear_funcion(expr_str)
    fa, fb = float(f(a)), float(f(b))

    if fa * fb >= 0:
        raise ValueError("El criterio de Bolzano no se cumple: f(a) * f(b) >= 0.")

    iteraciones = []
    p_ant = None

    for i in range(1, max_iter + 1):
        pn = (a + b) / 2.0
        fpn = float(f(pn))
        error = abs(pn - p_ant) if p_ant is not None else None

        iteraciones.append({
            "iteracion": i,
            "a": round(a, 6),
            "b": round(b, 6),
            "c": round(pn, 6),
            "fc": round(fpn, 6),
            "error": round(error, 6) if error is not None else None
        })

        if abs(fpn) < tol or (error is not None and error < tol):
            break

        if fa * fpn < 0:
            b = pn
        else:
            a = pn
            fa = fpn

        p_ant = pn

    return {"variable": str(var), "expresion": str(expr), "iteraciones": iteraciones}