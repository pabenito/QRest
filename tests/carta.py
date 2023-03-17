from models import *

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
