import pytest

from libreria.producto import Producto


class TestRegla3PrecioFinal:
    def test_calcular_precio_final_con_descuento_e_iva(self):
        producto = Producto("Novela", 10000)
        producto.aplicar_descuento(10)

        precio_final = producto.calcular_precio_final()

        assert precio_final == pytest.approx(10710.0)

    def test_precio_final_sin_descuento_incluye_iva(self):
        producto = Producto("Diccionario", 10000)

        precio_final = producto.calcular_precio_final()

        assert precio_final == pytest.approx(11900.0)

    def test_precio_final_nunca_es_negativo(self):
        producto = Producto("Folleto", 1)
        producto.aplicar_descuento(40)

        precio_final = producto.calcular_precio_final()

        assert precio_final >= 0

