"""Entidad Producto para la Libreria del Centro."""


class Producto:
    DESCUENTO_MAXIMO = 40.0

    def __init__(self, nombre: str, precio_base: float) -> None:
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base
        self.descuento_porcentaje = 0.0

    def aplicar_descuento(self, porcentaje: float) -> None:
        if porcentaje < 0 or porcentaje > self.DESCUENTO_MAXIMO:
            raise ValueError("El descuento debe estar entre 0% y 40%")

        self.descuento_porcentaje = porcentaje

    def calcular_precio_final(self) -> float:
        precio_con_descuento = self.precio_base * (1 - self.descuento_porcentaje / 100)
        return precio_con_descuento * 1.19