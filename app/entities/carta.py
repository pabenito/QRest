# Import libraries
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from app.entities.models import Seccion, Elemento_carta
from app.database import db

# Create router
router = APIRouter()

# Collections
carta = db["carta"]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Seccion)
def create_carta(seccion: Seccion):
    for elemento in seccion:
        check_precio(elemento)

    seccion = jsonable_encoder(seccion, exclude_unset=True, exclude_defaults=True)
    new_seccion = carta.insert_one(seccion)
    created_seccion = carta.find_one(
        {"_id": new_seccion.inserted_id}
    )

    return created_seccion


@router.get("/", response_model_exclude_unset=True)
def get_carta():
    return list(carta.find({}, {"_id": False}))


@router.get("/{id}", response_model_exclude_unset=True)
def get_by_id(seccion: str):
    return carta.find_one({"nombre": seccion}, {"_id": False})

def check_precio(elemento: Elemento_carta):
    if elemento.precio is None:
        if elemento.variantes is None:
            raise AttributeError("Si el precio no está definido, debe haber variantes con precios")
        else:
            for variantes in elemento.variantes:
                for variante in variantes.variantes:
                    if variante.precio is None:
                        raise AttributeError(f"Si el precio no está definido, todas las variantes deben tener precio.\nLa variante \"{variante.descripcion}\" no lo tiene definido")
                    elif variante.precio <= 0:
                        raise AttributeError(f"El precio debe ser positivo.\nLa variante \"{variante.descripcion}\" tiene de precio: {variante.precio}")
    elif elemento.precio <= 0:
        raise AttributeError(f"El precio debe ser positivo. El precio es: {elemento.precio}")
    else:
        if elemento.variantes is not None:
            for variantes in elemento.variantes:
                for variante in variantes.variantes:
                    if variante.precio is not None:
                        raise AttributeError(f"Si el precio está definido, ninguna variante puede tener precio.\nLa variante \"{variante.descripcion}\" tiene de precio: {elemento.precio}.")

