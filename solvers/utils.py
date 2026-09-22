import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

def parsear_funcion(expr_str: str, var_name: str = None):
    expr_limpia = expr_str.lower().strip().replace('np.', '').replace('math.', '')
    expr_limpia = (
        expr_limpia.replace('arcsen', 'asin')
        .replace('arccos', 'acos')
        .replace('arctan', 'atan')
        .replace('sen', 'sin')
    )

    locales = {
        'pi': sp.pi,
        'e': sp.E,
        'asin': sp.asin,
        'acos': sp.acos,
        'atan': sp.atan,
        'sin': sp.sin,
        'cos': sp.cos,
        'tan': sp.tan,
        'sqrt': sp.sqrt,
    }

    transformations = standard_transformations + (
        implicit_multiplication_application,
        convert_xor,
    )
    expr = parse_expr(expr_limpia, local_dict=locales, transformations=transformations)
    simbolos = list(expr.free_symbols)

    var = sp.Symbol(var_name) if var_name else (simbolos[0] if len(simbolos) == 1 else None)
    if not var:
        raise ValueError("No se pudo determinar la variable o la expresión no contiene una.")

    f = sp.lambdify(var, expr, modules=['math', 'sympy'])
    return expr, var, f