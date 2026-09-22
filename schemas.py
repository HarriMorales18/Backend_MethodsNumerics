from pydantic import BaseModel, Field
from typing import Optional

# Validación para Métodos de Intervalo Creado (Bisección y Falsa Posición)
class BiseccionFalsaPosicionRequest(BaseModel):
    expresion: str = Field(..., description="Función f(x)", example="x^3 - x - 2")
    a: float = Field(..., description="Límite inferior del intervalo", example=1.0)
    b: float = Field(..., description="Límite superior del intervalo", example=2.0)
    tolerancia: float = Field(..., description="Tolerancia del error", example=0.01)
    max_iter: Optional[int] = Field(default=100, description="Límite máximo de iteraciones", example=100)

# Validación para Método del Punto Fijo
class PuntoFijoRequest(BaseModel):
    expresion_g: str = Field(..., description="Función despejada g(x)", example="(x + 2)**(1/3)")
    x0: float = Field(..., description="Punto inicial de aproximación", example=1.5)
    tolerancia: float = Field(..., description="Tolerancia del error", example=0.01)
    max_iter: Optional[int] = Field(default=100, description="Límite máximo de iteraciones", example=100)

# Validación para Método de Newton-Raphson
class NewtonRaphsonRequest(BaseModel):
    expresion: str = Field(..., description="Función f(x)", example="x^3 - x - 2")
    x0: float = Field(..., description="Punto inicial de aproximación", example=1.5)
    tolerancia: float = Field(..., description="Tolerancia del error", example=0.01)
    max_iter: Optional[int] = Field(default=100, description="Límite máximo de iteraciones", example=100)