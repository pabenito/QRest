from pydantic import BaseModel, HttpUrl

from pydantic.dataclasses import dataclass


class ComplexModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True  # In order to allow ObjectId


# Entidades

## Carta

class Variante(ComplexModel):
    descripcion: str
    imagen: HttpUrl | None
    precio: float | None


class Variantes(ComplexModel):
    nombre: str
    variantes: list[Variante]


class Extra(BaseModel):
    descripcion: str
    precio: float | None


class Etiqueta(ComplexModel):
    nombre: str
    icono: HttpUrl | None


class Elemento_carta(ComplexModel):
    nombre: str
    imagen: HttpUrl | None
    descripcion: str | None
    precio: float | None
    responsable: str | None
    visible: bool = True
    ingredientes: list[str] | None
    alergenos: list[str] | None
    variantes: list[Variantes] | None
    extras: list[Extra] | None
    etiquetas: list[Etiqueta] | None


class Seccion(ComplexModel):
    nombre: str
    visible: bool = True
    elementos: list[Elemento_carta] | None
