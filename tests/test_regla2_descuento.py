import pytest

from libreria.producto import Producto


@pytest.fixture
def producto_base():
    return Producto("Libro", 10000)


class TestRegla2Descuento:
    def test_aplicar_descuento_valido_intermedio(self, producto_base):
        producto_base.aplicar_descuento(20)

        assert producto_base.descuento_porcentaje == 20

    def test_aceptar_descuento_limite_inferior_cero(self, producto_base):
        producto_base.aplicar_descuento(0)

        assert producto_base.descuento_porcentaje == 0

    def test_aceptar_descuento_limite_superior_cuarenta(self, producto_base):
        producto_base.aplicar_descuento(40)

        assert producto_base.descuento_porcentaje == 40

    def test_rechazar_descuento_mayor_a_cuarenta(self, producto_base):
        with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
            producto_base.aplicar_descuento(41)

    def test_rechazar_descuento_negativo(self, producto_base):
        with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
            producto_base.aplicar_descuento(-1)

