# 🧮 Numerical Methods API Core (Backend)

API RESTful desarrollada con **FastAPI** y **SymPy** para la resolución de ecuaciones no lineales mediante métodos numéricos iterativos. Este motor backend implementa derivación simbólica automática, validación estricta de datos mediante **Pydantic** y una arquitectura modular basada en patrones de diseño limpios.

---

## 🌟 Características Principales

* **Cálculo Simbólico Automatizado:** Integración con `SymPy` para obtener analíticamente las derivadas en tiempo de ejecución (sin necesidad de requerir la derivada manualmente en métodos como Newton-Raphson o Punto Fijo).
* **Respuestas Estandarizadas:** Formato JSON unificado `{"ok": true, "data": {...}}` con normalización de claves (`xi`, `xr`, `f_xr`, `error`) para simplificar el renderizado dinámico en tablas frontend.
* **Control de Convergencia y Excepciones:** Validación matemática previa (verificación del Teorema de Bolzano en métodos cerrados, detección de derivada nula $f'(x) = 0$ y análisis del criterio de convergencia $\vert{}g'(x_0)\vert{} < 1$).
* **Arquitectura Modular Extensible:** Separación rigurosa entre esquemas de transporte (DTOs), enrutamiento HTTP y módulos matemáticos independientes.

---

## 📐 Métodos Numéricos Implementados

| Método | Tipo | Fórmula de Iteración | Criterio de Parada / Particularidad |
| :--- | :--- | :--- | :--- |
| **Bisección** | Cerrado | $X_r = \frac{a + b}{2}$ | Error absoluto $\Vert{}X_r^{(k)} - X_r^{(k-1)}\Vert{} < \text{tol}$ y cambio de signo $f(a) \cdot f(X_r) < 0$. |
| **Falsa Posición** | Cerrado | $X_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$ | Interpolación lineal con actualización de intervalo según signo. |
| **Punto Fijo** | Abierto | $X_{n+1} = g(X_n)$ | Revisa si $\Vert{}g'(x_0)\Vert{} < 1$ para notificar factibilidad de convergencia. |
| **Newton-Raphson** | Abierto | $X_{n+1} = X_n - \frac{f(X_n)}{f'(X_n)}$ | Generación simbólica de $f'(x)$ vía SymPy y prevención de división por cero. |

---

## 📁 Estructura del Proyecto

```text
backend/
├── solvers/                      # Paquete interno con los algoritmos matemáticos
│   ├── __init__.py               # Fachada y exportación centralizada de resolvedores
│   ├── biseccion.py              # Cálculo por división sucesiva del intervalo
│   ├── falsa_posicion.py         # Cálculo por interpolación lineal en intervalos
│   ├── punto_fijo.py             # Iteración funcional x = g(x) y chequeo de derivada
│   └── newton_raphson.py         # Aproximación por rectas tangentes con SymPy
├── main.py                       # Servidor FastAPI, middleware CORS y definición de rutas
├── schemas.py                    # Modelos de validación Pydantic de entrada/salida
└── requirements.txt              # Dependencias del entorno Python