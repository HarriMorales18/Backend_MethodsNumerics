<p align="right">
  <b>Change language / Cambiar idioma:</b><br>
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
      <small><b>Harrinson D. Morales Tejedor (CEO and Dev)</b></small><br />
      <small>Angular Developer | Python Developer | Scrum Master</small>
    </td>
    <td align="center" width="260px">
      <a href="https://github.com/jhonarrieta2050">
        <img src="./assets/jhonarrieta2050.png" width="120px" height="120px" style="border-radius: 50%; object-fit: cover;" alt="jhonarrieta2050"/><br />
        <b>jhonarrieta2050</b>
      </a><br />
      <small><b>Jhon D. Arrieta Tovar (Dev)</b></small><br />
      <small>Backend Developer | Java & Spring Boot | Cloud Engineer</small>
    </td>
    <td align="center" width="260px">
      <a href="https://github.com/JuanGarcia0209">
        <img src="./assets/JuanGarcia0209.png" width="120px" height="120px" style="border-radius: 50%; object-fit: cover;" alt="JuanGarcia0209"/><br />
        <b>JuanGarcia0209</b>
      </a><br />
      <small><b>Juan D. Navarro Garcia (Dev)</b></small><br />
      <small>Backend Developer | PHP & Laravel | Data Analyst & Troubleshooting</small>
    </td>
  </tr>
</table>

---

## 📝 1. Project Description

**Numerical Methods API Core** is a specialized backend engine for the analytical and iterative solving of non-linear single-variable equations using numerical methods.

The platform is built on a modular, maintainable, and scalable RESTful API architecture. It receives mathematical expressions in plain text, performs runtime symbolic evaluation and differentiation (using SymPy), executes strict mathematical validations prior to computation (such as Bolzano's Theorem verification or convergence criterion analysis), and returns structured iterations in a unified JSON format for dynamic consumption by frontend clients.

---

## 🛠️ 2. Technologies Used (Backend)

* **Python 3.10+:** Main programming language used to implement core mathematical logic and iterative algorithms.
* **FastAPI:** Modern, high-performance, asynchronous web framework for building REST APIs.
* **SymPy:** Symbolic mathematics library used for parsing mathematical expressions, precise numerical evaluation, and automatic runtime differentiation.
* **Pydantic:** Data validation library used for defining DTOs (Data Transfer Objects), strict input/output type checking, and error prevention.
* **Uvicorn:** High-speed ASGI web server for running and deploying the FastAPI application.

---

## 📐 3. Numerical Methods & Implementation Table

| Method | Type | Validation / Prior Criterion | Iteration Function / Formula | Operational Explanation |
| :--- | :--- | :--- | :--- | :--- |
| **Bisection** | Closed | **Bolzano's Theorem:** Verifies $f(a) \cdot f(b) < 0$ to guarantee at least one root exists in $[a, b]$. | $X_r = \frac{a + b}{2}$ | Divides the interval in half at each iteration. Evaluates the sign of $f(a) \cdot f(X_r)$ to discard the subinterval without a root and repeats until tolerance is met. |
| **False Position** *(Regula Falsi)* | Closed | **Bolzano's Theorem:** Requires a sign change at interval endpoints: $f(a) \cdot f(b) < 0$. | $X_r = b - \frac{f(b)(a - b)}{f(a) - f(b)}$ | Connects $(a, f(a))$ and $(b, f(b))$ with a secant line and finds its X-intercept as the new approximation, preserving the subinterval with the sign change. |
| **Fixed Point** | Open | **Convergence Criterion:** Evaluates whether $\vert g'(x_0) \vert < 1$ to inform convergence feasibility. | $X_{n+1} = g(X_n)$ | Transforms $f(x) = 0$ into $x = g(x)$. Generates an iterative sequence by evaluating $g(x)$ starting from an initial value $X_0$. |
| **Newton-Raphson** | Open | **Zero Derivative:** Analytically checks $f'(X_n) \neq 0$ at each step to prevent division by zero. | $X_{n+1} = X_n - \frac{f(X_n)}{f'(X_n)}$ | Draws tangent lines to the curve at each iteration. The derivative $f'(x)$ is calculated symbolically via SymPy transparently to the user. |
| **Secant** | Open | **Zero Difference:** Validates $f(X_n) - f(X_{n-1}) \neq 0$ per iteration to prevent numerical indeterminacy. | $X_{n+1} = X_n - \frac{f(X_n)(X_n - X_{n-1})}{f(X_n) - f(X_{n-1})}$ | Approximates the derivative using finite differences from two initial points ($X_0, X_1$), eliminating the need for explicit derivative calculation. |

---

## 🚀 4. Installation and Setup

### Prerequisites
* **Python 3.10** or higher installed.
* Package manager **`pip`**.

### Step 1: Clone the Backend Repository
```bash
git clone [https://github.com/HarriMorales18/Backend_MethodsNumerics.git](https://github.com/HarriMorales18/Backend_MethodsNumerics.git)
cd Backend_MethodsNumerics
```

### Step 2: Create and Activate Virtual Environment
* **On Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **On Linux / macOS:**
  ```bash
  bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is missing, install manually using: `pip install fastapi uvicorn sympy pydantic`)*

### Step 4: Start the Backend
To start the development server with automatic reload (*hot-reload*):
```bash
uvicorn main:app --reload
```

The server will run locally at: `http://127.0.0.1:8000`

### Step 5: View and Test Endpoints (Interactive Documentation)
To view, inspect, and test API endpoints interactively in your browser:
👉 **[http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)**

---

## 📁 5. Backend Structure & File/Folder Directory

```text
Backend_MethodsNumerics/
├── assets/                       # Folder containing project images and assets
│   ├── HarriMorales18.png        # Profile avatar for HarriMorales18
│   ├── jhonarrieta2050.png       # Profile avatar for jhonarrieta2050
│   └── JuanGarcia0209.png        # Profile avatar for JuanGarcia0209
├── solvers/                      # Internal package containing mathematical logic and algorithms
│   ├── __init__.py               # Centralized export facade for solver functions
│   ├── biseccion.py              # Bisection Method algorithm
│   ├── falsa_posicion.py         # False Position Method algorithm
│   ├── punto_fijo.py             # Fixed Point Method algorithm
│   ├── newton_raphson.py         # Newton-Raphson algorithm with SymPy differentiation
│   ├── secante.py                # Secant Method algorithm
│   └── utils.py                  # Expression parsing and string interpretation utilities
├── main.py                       # FastAPI entry point, CORS middleware, and route definitions
├── schemas.py                    # Pydantic validation schemas (Input/Output DTOs)
├── requirements.txt              # List of Python dependencies and packages
├── README.md                     # Spanish documentation
└── README.en.md                  # English documentation
```

### Detailed File and Folder Descriptions:

* **`assets/`:** Stores local images used across documentation, including circular avatar pictures for contributors.
* **`main.py`:** API entry point. Initializes FastAPI, configures CORS middleware to authorize frontend requests (`http://localhost:4200`), defines the root path (`/`), and exposes HTTP POST endpoints (`/api/biseccion`, `/api/falsa-posicion`, `/api/punto-fijo`, `/api/newton-raphson`, `/api/secante`).
* **`schemas.py`:** Contains Data Transfer Objects (DTOs) constructed with Pydantic (`BiseccionFalsaPosicionRequest`, `PuntoFijoRequest`, `NewtonRaphsonRequest`, `SecanteRequest`). Handles input type validation for incoming JSON payloads.
* **`solvers/`:** Modular folder encapsulating numerical algorithms and isolating mathematical logic from the web server.
  * **`solvers/__init__.py`:** Imports and exports solver functions in a centralized manner for consumption in `main.py`.
  * **`solvers/biseccion.py`:** Implements the bisection calculation along with Bolzano's Theorem validation.
  * **`solvers/falsa_posicion.py`:** Applies linear interpolation formula and outputs iteration tables.
  * **`solvers/punto_fijo.py`:** Runs $x_{n+1} = g(x_n)$ iterations and evaluates $g'(x_0)$ via SymPy to check convergence.
  * **`solvers/newton_raphson.py`:** Derives $f(x)$ symbolically with SymPy and executes tangent-line iteration steps.
  * **`solvers/secante.py`:** Applies secant iteration based on two starting points and finite differences.
  * **`solvers/utils.py`:** Converts string-based math expressions (e.g., `x^2`, `exp(-x)`) into executable SymPy functions safely.
* **`requirements.txt`:** Lists third-party dependencies (`fastapi`, `uvicorn`, `sympy`, `pydantic`) required to run the application.

---

## 🌟 6. Key Features

* **Automated Symbolic Computation:** Supports complex standard expressions including exponential (`exp(x)`), logarithmic (`log(x)`), trigonometric (`sin(x)`, `cos(x)`), and polynomial functions.
* **Runtime Symbolic Differentiation:** Automatically computes analytical derivatives of $f(x)$ for Newton-Raphson and $g(x)$ for Fixed Point via SymPy without manual input.
* **Rigorous Mathematical Error Handling:** Captures conceptual errors before or during execution (Bolzano's failure, zero derivative $f'(x) = 0$, division by zero, or max iteration limits).
* **Standardized JSON Responses:** Returns a single unified response model `{"ok": true, "data": {...}}` with consistent keys for seamless frontend table rendering.
* **Pre-configured CORS Integration:** Ready for cross-origin communication with local frontend clients like Angular (`http://localhost:4200`).

---

## 🔗 7. Frontend Repository Link

The Angular frontend client that connects to this backend API is available at:
👉 [https://github.com/HarriMorales18/Frontend_MethodsNumerics.git](https://github.com/HarriMorales18/Frontend_MethodsNumerics.git)