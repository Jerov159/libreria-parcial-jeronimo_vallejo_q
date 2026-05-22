# Libreria del Centro - Parcial 1 Pruebas de Software

Modulo en Python para calcular el precio final de productos de la Libreria del Centro.

## Requisitos

- Python 3.10+
- pytest, pytest-cov, pytest-bdd

```bash
pip install -r requirements.txt
```

## Ejecutar pruebas

```bash
python -m pytest
python -m pytest --cov=libreria --cov-report=term-missing
```
## Analisis de pruebas

### Regla 1 - Precio base del producto

| Particion | Clase | Valor representativo | Resultado esperado |
|-----------|-------|----------------------|--------------------|
| PE1 | Validos: precio > 0 | 15000 | Producto creado correctamente |
| PE2 | Invalidos: precio = 0 | 0 | Rechazo con mensaje claro |
| PE3 | Invalidos: precio < 0 | -100 | Rechazo con mensaje claro |

### Regla 2 - Descuento porcentual

| Particion | Clase | Valor representativo | Resultado esperado |
|-----------|-------|----------------------|--------------------|
| PE1 | Validos: 0% <= descuento <= 40% | 20 | Descuento aplicado |
| PE2 | Validos: descuento = 0% (borde inferior) | 0 | Descuento aplicado |
| PE3 | Validos: descuento = 40% (borde superior) | 40 | Descuento aplicado |
| PE4 | Invalidos: descuento < 0% | -1 | Rechazo con mensaje claro |
| PE5 | Invalidos: descuento > 40% | 41 | Rechazo con mensaje claro |

#### Analisis de valores limite (Regla 2)

| Valor limite | Tipo | Resultado esperado |
|--------------|------|--------------------|
| -0.01 | Justo bajo minimo | Rechazo |
| 0 | Minimo valido | Aceptado |
| 0.01 | Justo sobre minimo | Aceptado |
| 39.99 | Justo bajo maximo | Aceptado |
| 40 | Maximo valido | Aceptado |
| 40.01 | Justo sobre maximo | Rechazo |

### Regla 3 - Precio final con IVA

**Pregunta al administrador:** Si el descuento deja el subtotal en cero, el IVA del 19% debe calcularse sobre cero o existe un precio minimo de venta?

**Justificacion:** Define si el precio final puede ser exactamente cero o si hay una regla comercial adicional que afecta los casos de prueba en el borde.