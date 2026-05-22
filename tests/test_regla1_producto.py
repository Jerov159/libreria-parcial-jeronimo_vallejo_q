import pytest

from libreria.producto import Producto


class TestRegla1CrearProducto:
    def test_crear_producto_con_precio_valido(self):
        producto = Producto("Novela", 25000)

        assert producto.nombre == "Novela"
        assert producto.precio_base == 25000

    def test_rechazar_precio_base_cero(self):
        with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
            Producto("Revista", 0)

    def test_rechazar_precio_base_negativo(self):
        with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
            Producto("Cuaderno", -500)

