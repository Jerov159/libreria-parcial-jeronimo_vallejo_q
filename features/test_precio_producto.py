from pytest_bdd import given, parsers, scenarios, then, when

from libreria.producto import Producto

scenarios("precio_producto.feature")


@given(
    parsers.parse('un producto llamado "{nombre}" con precio base de {precio:d} pesos'),
    target_fixture="producto_contexto",
)
def crear_producto_contexto(nombre, precio):
    return {"producto": Producto(nombre, precio), "error": None}


@when(parsers.parse("aplico un descuento del {descuento:d} por ciento"))
def aplicar_descuento(producto_contexto, descuento):
    producto_contexto["producto"].aplicar_descuento(descuento)


@when(parsers.parse("intento aplicar un descuento del {descuento:d} por ciento"))
def intentar_aplicar_descuento(producto_contexto, descuento):
    producto_contexto["error"] = None
    try:
        producto_contexto["producto"].aplicar_descuento(descuento)
    except ValueError as exc:
        producto_contexto["error"] = exc


@then(parsers.parse("el descuento queda registrado en {descuento:d} por ciento"))
def verificar_descuento_registrado(producto_contexto, descuento):
    assert producto_contexto["producto"].descuento_porcentaje == descuento


@then("el sistema rechaza el descuento con un mensaje claro")
def verificar_rechazo_descuento(producto_contexto):
    assert producto_contexto["error"] is not None
    assert "El descuento debe estar entre 0% y 40%" in str(producto_contexto["error"])


@then(parsers.parse("el precio final debe ser {precio_final:d} pesos"))
def verificar_precio_final(producto_contexto, precio_final):
    assert producto_contexto["producto"].calcular_precio_final() == precio_final

