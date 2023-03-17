from app.entities.models import *
from app.entities.carta import check_precio
import unittest


class TestSCarta(unittest.TestCase):
    def test___check_precio___when_precio_is_set_and_there_is_not_variantes___then_dont_raise_exception(self):
        elemento = Elemento_carta(nombre="Nestea")
        elemento.precio = 2.5
        check_precio(elemento)

    def test___check_precio___when_precio_is_set_and_there_is_not_variantes___then_raise_exception(self):
        elemento = Elemento_carta(nombre="Agua")

        with self.assertRaises(AttributeError):
            check_precio(elemento)
