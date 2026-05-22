# Evidencias - Parcial 1 Pruebas de Software

**Estudiante:** Jerov159  
**Repositorio:** https://github.com/Jerov159/Parcial-1-PS  
**Fecha de ejecucion:** 22 de mayo de 2026  
**Entorno:** Windows 10 | Python 3.14.4 | pytest 9.0.3

---

## 1. Historial de commits del repositorio

**Comando ejecutado:**
```powershell
git log --oneline
```

**Salida:**
```
952fdef docs: reporte de cobertura de pruebas superior al 80 por ciento
bb09afa docs: respuestas de la seccion teorica del parcial
dbcded0 feat: step definitions pytest-bdd conectadas al modulo Producto
2e816a4 test: escenarios BDD en Gherkin para descuento e IVA
bb19504 feat: GREEN Regla 3 - calculo de precio final con IVA del 19 por ciento
6ceb98e test: RED Regla 3 - tests de precio final con descuento e IVA
c8e5ffd refactor: REFACTOR Regla 2 - constante de descuento maximo
6208fb0 feat: GREEN Regla 2 - metodo aplicar_descuento con validacion
fc82d37 test: RED Regla 2 - tests de descuento porcentual entre 0 y 40
d351ecf refactor: REFACTOR Regla 1 - estructura inicial de clase Producto
f02a73e feat: GREEN Regla 1 - validacion de precio base mayor que cero
c0be7bd test: RED Regla 1 - tests de creacion de producto con precio base
4516a19 docs: tabla de ocho casos de prueba distribuidos por regla
7646f72 docs: analisis de particiones de equivalencia y valores limite
ed9bed7 chore: configuracion inicial del proyecto Python con pytest
```

**Total de commits:** 15

---

## 2. Repositorio remoto configurado

**Comando ejecutado:**
```powershell
git remote -v
```

**Salida:**
```
origin  https://github.com/Jerov159/Parcial-1-PS.git (fetch)
origin  https://github.com/Jerov159/Parcial-1-PS.git (push)
```

---

## 3. Evidencia TDD - Regla 1 (precio base)

**Comando ejecutado:**
```powershell
python -m pytest tests/test_regla1_producto.py -v
```

**Salida:**
```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
collected 3 items

tests/test_regla1_producto.py::TestRegla1CrearProducto::test_crear_producto_con_precio_valido PASSED [ 33%]
tests/test_regla1_producto.py::TestRegla1CrearProducto::test_rechazar_precio_base_cero PASSED [ 66%]
tests/test_regla1_producto.py::TestRegla1CrearProducto::test_rechazar_precio_base_negativo PASSED [100%]

============================== 3 passed in 0.02s ==============================
```

**Casos cubiertos:** CP-01 (positivo), CP-02 (negativo), CP-03 (negativo)

---

## 4. Evidencia TDD - Regla 2 (descuento porcentual)

**Comando ejecutado:**
```powershell
python -m pytest tests/test_regla2_descuento.py -v
```

**Salida:**
```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
collected 5 items

tests/test_regla2_descuento.py::TestRegla2Descuento::test_aplicar_descuento_valido_intermedio PASSED [ 20%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_inferior_cero PASSED [ 40%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_superior_cuarenta PASSED [ 60%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_mayor_a_cuarenta PASSED [ 80%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_negativo PASSED [100%]

============================== 5 passed in 0.02s ==============================
```

**Casos cubiertos:** CP-04 (positivo), CP-05 (borde), CP-06 (borde), CP-07 (negativo)

---

## 5. Evidencia TDD - Regla 3 (precio final con IVA)

**Comando ejecutado:**
```powershell
python -m pytest tests/test_regla3_precio_final.py -v
```

**Salida:**
```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
collected 3 items

tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_calcular_precio_final_con_descuento_e_iva PASSED [ 33%]
tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_sin_descuento_incluye_iva PASSED [ 66%]
tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_nunca_es_negativo PASSED [100%]

============================== 3 passed in 0.02s ==============================
```

**Casos cubiertos:** CP-08 (positivo) y validacion de precio no negativo

---

## 6. Evidencia BDD - Escenarios Gherkin (Reglas 2 y 3)

**Comando ejecutado:**
```powershell
python -m pytest features/test_precio_producto.py -v
```

**Salida:**
```
============================= test session starts =============================
platform win32 -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
collected 7 items

features/test_precio_producto.py::test_aplicar_un_descuento_valido_al_producto PASSED [ 14%]
features/test_precio_producto.py::test_aceptar_descuento_en_el_limite_inferior PASSED [ 28%]
features/test_precio_producto.py::test_aceptar_descuento_en_el_limite_superior PASSED [ 42%]
features/test_precio_producto.py::test_rechazar_descuento_mayor_al_permitido PASSED [ 57%]
features/test_precio_producto.py::test_calcular_precio_final_con_descuento_e_iva_del_19_por_ciento[0-11900] PASSED [ 71%]
features/test_precio_producto.py::test_calcular_precio_final_con_descuento_e_iva_del_19_por_ciento[10-10710] PASSED [ 85%]
features/test_precio_producto.py::test_calcular_precio_final_con_descuento_e_iva_del_19_por_ciento[40-7140] PASSED [100%]

============================== 7 passed in 0.08s ==============================
```

**Escenarios BDD:** 5 escenarios (4 Scenario + 1 Scenario Outline con 3 Examples)

---

## 7. Suite completa TDD + BDD

**Comando ejecutado:**
```powershell
python -m pytest -v
```

**Salida:**
```
collected 18 items

tests/test_regla1_producto.py ...                                        [ 16%]
tests/test_regla2_descuento.py .....                                     [ 44%]
tests/test_regla3_precio_final.py ...                                    [ 61%]
features/test_precio_producto.py .......                                 [100%]

======================= 18 passed in 0.08s =======================
```

---

## 8. Reporte de cobertura de codigo

**Comando ejecutado:**
```powershell
python -m pytest --cov=libreria --cov-report=term-missing
```

**Salida:**
```
collected 18 items

tests/test_regla1_producto.py ... PASSED
tests/test_regla2_descuento.py ..... PASSED
tests/test_regla3_precio_final.py ... PASSED
features/test_precio_producto.py ....... PASSED

=============================== tests coverage ================================
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src\libreria\__init__.py       0      0   100%
src\libreria\producto.py      15      0   100%
--------------------------------------------------------
TOTAL                         15      0   100%
======================= 18 passed in 0.13s =======================
```

**Resultado:** Cobertura del 100% (requerido: minimo 80%)

---

## 9. Evidencia ciclo TDD por regla en commits

### Regla 1
**Comando:** `git log --oneline --grep="Regla 1"`
```
d351ecf refactor: REFACTOR Regla 1 - estructura inicial de clase Producto
f02a73e feat: GREEN Regla 1 - validacion de precio base mayor que cero
c0be7bd test: RED Regla 1 - tests de creacion de producto con precio base
```

### Regla 2
**Comando:** `git log --oneline --grep="Regla 2"`
```
c8e5ffd refactor: REFACTOR Regla 2 - constante de descuento maximo
6208fb0 feat: GREEN Regla 2 - metodo aplicar_descuento con validacion
fc82d37 test: RED Regla 2 - tests de descuento porcentual entre 0 y 40
```

### Regla 3
**Comando:** `git log --oneline --grep="Regla 3"`
```
bb19504 feat: GREEN Regla 3 - calculo de precio final con IVA del 19 por ciento
6ceb98e test: RED Regla 3 - tests de precio final con descuento e IVA
```

---

## 10. Resumen de cumplimiento

| Criterio | Resultado |
|----------|-----------|
| Tests unitarios TDD | 11 passed |
| Tests BDD Gherkin | 7 passed |
| Total tests | 18 passed |
| Cobertura de codigo | 100% |
| Commits en historial | 15 |
| Repositorio publico | https://github.com/Jerov159/Parcial-1-PS |
| Archivo TEORIA.md | Presente |
| Archivo README.md con analisis | Presente |
| Archivo .feature BDD | Presente |

---

## 11. Archivos de entrega verificados

```
README.md
TEORIA.md
EVIDENCIAS.md
requirements.txt
pytest.ini
src/libreria/producto.py
tests/test_regla1_producto.py
tests/test_regla2_descuento.py
tests/test_regla3_precio_final.py
features/precio_producto.feature
features/test_precio_producto.py
```
