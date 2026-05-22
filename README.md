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
## Casos de prueba

| ID | Regla | Descripcion | Precondicion | Datos de entrada | Pasos | Resultado esperado | Tipo |
|----|-------|-------------|--------------|------------------|-------|-------------------|------|
| CP-01 | 1 | Crear producto con precio valido | Ninguna | nombre="Novela", precio_base=25000 | Instanciar Producto | Objeto creado con precio 25000 | Positivo |
| CP-02 | 1 | Rechazar precio base cero | Ninguna | precio_base=0 | Instanciar Producto | ValueError con mensaje claro | Negativo |
| CP-03 | 1 | Rechazar precio base negativo | Ninguna | precio_base=-500 | Instanciar Producto | ValueError con mensaje claro | Negativo |
| CP-04 | 2 | Aplicar descuento valido intermedio | Producto con precio 10000 | descuento=20 | Llamar aplicar_descuento(20) | Descuento registrado en 20% | Positivo |
| CP-05 | 2 | Aceptar descuento en limite inferior | Producto creado | descuento=0 | Llamar aplicar_descuento(0) | Descuento aceptado | Borde |
| CP-06 | 2 | Aceptar descuento en limite superior | Producto creado | descuento=40 | Llamar aplicar_descuento(40) | Descuento aceptado | Borde |
| CP-07 | 2 | Rechazar descuento mayor al 40% | Producto creado | descuento=41 | Llamar aplicar_descuento(41) | ValueError con mensaje claro | Negativo |
| CP-08 | 3 | Calcular precio final con descuento e IVA | Producto precio 10000, descuento 10% | descuento=10 | Llamar calcular_precio_final() | 10000 * 0.90 * 1.19 = 10710.0 | Positivo |
## Reporte de cobertura

Ejecutar:

```bash
python -m pytest --cov=libreria --cov-report=term-missing
```

Resultado obtenido:

```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
collected 18 items

tests/test_regla1_producto.py ...... PASSED
tests/test_regla2_descuento.py ...... PASSED
tests/test_regla3_precio_final.py ... PASSED
features/test_precio_producto.py ....... PASSED

=============================== tests coverage ================================
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src\libreria\__init__.py       2      0   100%
src\libreria\producto.py      17      0   100%
--------------------------------------------------------
TOTAL                         19      0   100%
======================= 18 passed in 0.11s =======================
```