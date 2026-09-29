<p align="right">
  <b>Cambiar idioma / Change language:</b><br>
  <a href="./README.md"><img src="https://img.shields.io/badge/Idioma-Español-blue?style=for-the-badge&logo=spain" alt="Español"></a>
  <a href="./README.en.md"><img src="https://img.shields.io/badge/Language-English-red?style=for-the-badge&logo=unitedstates" alt="English"></a>
</p>

---

# 🧮 Numerical Methods API Core (Backend)

<table>
  <tr>
    <td align="center" width="260px">
      <a href="https://github.com/HarriMorales18">
        <img src="./assets/HarriMorales18.png" width="120px" height="120px" style="border-radius: 50%; object-fit: cover;" alt="HarriMorales18"/><br />
        <b>HarriMorales18</b>
      </a><br />
      <small><b>Harrinson D. Morales Tejedor(CEO and Dev)</b></small><br />
      <small>Angular Developer | Python Developer | Scrum Master</small>
    </td>
    <td align="center" width="260px">
      <a href="https://github.com/jhonarrieta2050">
        <img src="./assets/jhonarrieta2050.png" width="120px" height="120px" style="border-radius: 50%; object-fit: cover;" alt="jhonarrieta2050"/><br />
        <b>jhonarrieta2050</b>
      </a><br />
      <small><b>Jhon D. Arrieta Tovar(Dev)</b></small><br />
      <small>Backend Developer | Java & Spring Boot | Cloud Engineer</small>
    </td>
    <td align="center" width="260px">
      <a href="https://github.com/JuanGarcia0209">
        <img src="./assets/JuanGarcia0209.png" width="120px" height="120px" style="border-radius: 50%; object-fit: cover;" alt="JuanGarcia0209"/><br />
        <b>JuanGarcia0209</b>
      </a><br />
      <small><b>Juan D. Navarro Garcia(Dev)</b></small><br />
      <small>Backend Developer | PHP & Laravel | Data Analyst & Troubleshooting</small>
    </td>
  </tr>
</table>

---

## 📝 1. Descripción del Proyecto

**Numerical Methods API Core** es un motor backend especializado en la resolución analítica e iterativa de ecuaciones no lineales de una variable mediante métodos numéricos. 

La plataforma está construida bajo una arquitectura de API RESTful modular, mantenible y escalable. Recibe expresiones matemáticas en texto plano, realiza evaluación y derivación simbólica en tiempo de ejecución (con SymPy), efectúa validaciones matemáticas estrictas previo al cálculo (como la verificación del Teorema de Bolzano o el análisis del criterio de convergencia) y devuelve las iteraciones organizadas en un formato JSON unificado para ser consumido dinámicamente desde clientes frontend.

---

## 🛠️ 2. Tecnologías Usadas (Backend)

* **Python 3.10+:** Lenguaje de programación principal para la implementación de la lógica matemática y los algoritmos iterativos.
* **FastAPI:** Framework web asíncrono, moderno y de alto rendimiento para la construcción de la API REST.
* **SymPy:** Librería de cálculo simbólico utilizada para el parseo de funciones matemáticas, evaluación numérica precisa y derivación automática en tiempo de ejecución.
* **Pydantic:** Librería para la definición de esquemas DTO (Data Transfer Objects), validación estricta de tipos de datos de entrada/salida y prevención de errores.
* **Uvicorn:** Servidor web ASGI de alta velocidad para la ejecución y despliegue local de la aplicación FastAPI.

---

## 📐 3. Tabla de Métodos Numéricos e Implementación

| Método | Tipo | Validación / Criterio Previo | Función / Fórmula de Iteración | Explicación del Funcionamiento |
| :--- | :--- | :--- | :--- | :--- |
| **Bisección** | Cerrado | **Teorema de Bolzano:** Verifica que $f(a) \cdot f(b) < 0$ para garantizar la existencia de al menos una raíz en el intervalo $[a, b]$. | $X_r = \frac{a + b}{2}$ | Divide el intervalo a la mitad en cada iteración. Evalúa el signo de $f(a) \cdot f(X_r)$ para descartar el subintervalo que no contiene la raíz y repetir el proceso hasta cumplir la tolerancia. |
| **Falsa Posición** *(Regula Falsi)* | Cerrado | **Teorema de Bolzano:** Requiere un cambio de signo en los extremos del intervalo: $f(a) \cdot f(b) < 0$. | $X_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$ | Conecta los puntos $(a, f(a))$ y $(b, f(b))$ mediante una recta secante e identifica su intersección con el eje X como la nueva aproximación, conservando el subintervalo con cambio de signo. |
| **Punto Fijo** | Abierto | **Criterio de Convergencia:** Evalúa si $\vert g'(x_0) \vert < 1$ para notificar la factibilidad de convergencia del método. | $X_{n+1} = g(X_n)$ | Transforma la ecuación $f(x) = 0$ en la forma equivalente $x = g(x)$. Genera una sucesión iterativa evaluando la función $g(x)$ a partir de un valor inicial $X_0$. |
| **Newton-Raphson** | Abierto | **Derivada Nula:** Verifica analíticamente que $f'(X_n) \neq 0$ en cada paso para evitar divisiones por cero. | $X_{n+1} = X_n - \frac{f(X_n)}{f'(X_n)}$ | Traza rectas tangentes a la curva de la función en cada punto iterativo. La derivada $f'(x)$ se calcula simbólicamente mediante SymPy de forma transparente para el usuario. |
| **Secante** | Abierto | **Diferencia Nula:** Valida que $f(X_n) - f(X_{n-1}) \neq 0$ en cada iteración para prevenir indeterminaciones numéricas. | $X_{n+1} = X_n - \frac{f(X_n)(X_n - X_{n-1})}{f(X_n) - f(X_{n-1})}$ | Aproxima la derivada mediante diferencias finitas a partir de dos puntos iniciales ($X_0, X_1$), evitando la necesidad de calcular explícitamente la derivada de la función. |

---

## 🚀 4. Instalación y Ejecución del Proyecto

### Requisitos Previos
* **Python 3.10** o superior instalado.
* Gestor de paquetes **`pip`**.

### Paso 1: Clonar el repositorio del Backend
```bash
git clone [https://github.com/HarriMorales18/Backend_MethodsNumerics.git](https://github.com/HarriMorales18/Backend_MethodsNumerics.git)
cd Backend_MethodsNumerics
```

### Paso 2: Crear y activar el entorno virtual
* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Paso 3: Instalar las dependencias
```bash
pip install -r requirements.txt
```
*(Si no posees el archivo `requirements.txt`, puedes instalarlas individualmente con: `pip install fastapi uvicorn sympy pydantic`)*

### Paso 4: Correr el Backend
Para iniciar el servidor en modo desarrollo con recarga automática (*hot-reload*):
```bash
uvicorn main:app --reload
```

El servidor estará corriendo localmente en: `http://127.0.0.1:8000`

### Paso 5: Ver y Probar los Endpoints (Documentación Interactiva)
Para consultar, inspeccionar y probar los endpoints interactivamente desde el navegador:
👉 **[http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)**

---

## 📁 5. Estructura del Backend y Explicación de Archivos y Carpetas

```text
Backend_MethodsNumerics/
├── solvers/                      # Paquete interno con la lógica matemática y algoritmos
│   ├── __init__.py               # Fachada y exportación centralizada de las funciones resolutoras
│   ├── biseccion.py              # Algoritmo del Método de la Bisección
│   ├── falsa_posicion.py         # Algoritmo del Método de la Falsa Posición
│   ├── punto_fijo.py             # Algoritmo del Método del Punto Fijo
│   ├── newton_raphson.py         # Algoritmo de Newton-Raphson con derivación SymPy
│   ├── secante.py                # Algoritmo del Método de la Secante
│   └── utils.py                  # Utilidades de parseo e interpretación de expresiones
├── main.py                       # Servidor FastAPI, middleware CORS y definición de rutas
├── schemas.py                    # Modelos de validación Pydantic (DTOs de entrada/salida)
├── requirements.txt              # Archivo con las dependencias y paquetes de Python
└── README.md                     # Documentación principal del proyecto Backend
```

### Explicación detallada de cada archivo y carpeta:

* **`main.py`:** Es el punto de entrada de la API. Inicializa la aplicación FastAPI, configura el middleware de CORS para autorizar peticiones provenientes del frontend (`http://localhost:4200`), define la ruta raíz (`/`) y expone los endpoints HTTP POST (`/api/biseccion`, `/api/falsa-posicion`, `/api/punto-fijo`, `/api/newton-raphson`, `/api/secante`).
* **`schemas.py`:** Contiene los contratos de datos (Data Transfer Objects - DTOs) creados con Pydantic (`BiseccionFalsaPosicionRequest`, `PuntoFijoRequest`, `NewtonRaphsonRequest`, `SecanteRequest`). Se encarga de la validación automática de los tipos de datos recibidos en las peticiones JSON.
* **`solvers/`:** Carpeta que agrupa de forma modular todos los algoritmos numéricos, aislando la lógica matemática del servidor web.
  * **`solvers/__init__.py`:** Expone e importa de forma centralizada todas las funciones resolutoras para que `main.py` las consuma directamente.
  * **`solvers/biseccion.py`:** Implementa el algoritmo de bisección e incluye la validación del Teorema de Bolzano.
  * **`solvers/falsa_posicion.py`:** Aplica la fórmula de interpolación lineal y genera la tabla de iteraciones.
  * **`solvers/punto_fijo.py`:** Ejecuta la secuencia $x_{n+1} = g(x_n)$ y calcula la derivada $g'(x_0)$ con SymPy para alertar sobre la convergencia.
  * **`solvers/newton_raphson.py`:** Calcula simbólicamente la primera derivada de la función con SymPy y genera las iteraciones por recta tangente.
  * **`solvers/secante.py`:** Aplica el algoritmo de la secante a partir de dos puntos iniciales y aproximación por diferencias finitas.
  * **`solvers/utils.py`:** Provee utilidades para convertir expresiones matemáticas ingresadas en texto (ej. `x^2`, `exp(-x)`) en funciones ejecutables por SymPy.
* **`requirements.txt`:** Especifica las librerías necesarias (`fastapi`, `uvicorn`, `sympy`, `pydantic`) para el correcto funcionamiento del backend.

---

## 🌟 6. Características Principales

* **Cálculo Simbólico Automatizado:** Procesa expresiones matemáticas complejas en notación estándar, incluyendo funciones exponenciales (`exp(x)`), logarítmicas (`log(x)`), trigonométricas (`sin(x)`, `cos(x)`) y polinómicas.
* **Derivación Simbólica en Tiempo de Ejecución:** Calcula automáticamente la derivada de $f(x)$ para Newton-Raphson y $g(x)$ para Punto Fijo usando SymPy, sin requerir que el usuario la ingrese manualmente.
* **Validación Matemática Rigurosa:** Detecta y notifica errores conceptuales antes o durante la ejecución (incumplimiento del Teorema de Bolzano, derivada nula $f'(x) = 0$, divisiones por cero o exceso de iteraciones máximo).
* **Respuestas Estandarizadas JSON:** Devuelve un formato estructurado único `{"ok": true, "data": {...}}` con nombres de propiedades uniformes que simplifican el renderizado dinámico en tablas frontend.
* **Integración CORS Preconfigurada:** Permitida la comunicación directa con clientes web alojados en entornos locales como Angular (`http://localhost:4200`).

---

## 🔗 7. Link del Repositorio Frontend

El cliente frontend desarrollado en Angular para interactuar con este backend está disponible en:
👉 [https://github.com/HarriMorales18/Frontend_MethodsNumerics.git](https://github.com/HarriMorales18/Frontend_MethodsNumerics.git)
