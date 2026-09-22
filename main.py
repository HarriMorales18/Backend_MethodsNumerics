from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import (
    BiseccionFalsaPosicionRequest,
    PuntoFijoRequest,
    NewtonRaphsonRequest,
)
from solvers import (
    resolver_biseccion,
    resolver_falsa_posicion,
    resolver_punto_fijo,
    resolver_newton_raphson,
)

app = FastAPI(
    title="Calculadora de Métodos Numéricos API",
    version="1.0.0"
)

# Configuración de CORS para conectar con el frontend en Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensaje": "API de Métodos Numéricos activa y lista."}

@app.post("/api/biseccion")
def endpoint_biseccion(req: BiseccionFalsaPosicionRequest):
    try:
        res = resolver_biseccion(
            req.expresion, req.a, req.b, req.tolerancia, req.max_iter
        )
        return {"ok": True, "data": res}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/falsa-posicion")
def endpoint_falsa_posicion(req: BiseccionFalsaPosicionRequest):
    try:
        res = resolver_falsa_posicion(
            req.expresion, req.a, req.b, req.tolerancia, req.max_iter
        )
        return {"ok": True, "data": res}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/punto-fijo")
def endpoint_punto_fijo(req: PuntoFijoRequest):
    try:
        res = resolver_punto_fijo(
            req.expresion_g, req.x0, req.tolerancia, req.max_iter
        )
        return {"ok": True, "data": res}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/newton-raphson")
def endpoint_newton_raphson(req: NewtonRaphsonRequest):
    try:
        res = resolver_newton_raphson(
            req.expresion, req.x0, req.tolerancia, req.max_iter
        )
        return {"ok": True, "data": res}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))