"""Entidad Producto para la Libreria del Centro."""


class Producto:
    def __init__(self, nombre: str, precio_base: float) -> None:
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base
        self.descuento_porcentaje = 0.0