# Evidencias - Parcial 1 Pruebas de Software

**Estudiante:** Jerov159  
**Repositorio:** https://github.com/Jerov159/libreria-parcial-jeronimo_vallejo_q  
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
fabdca2 docs: evidencias de ejecucion de pruebas TDD y BDD desde terminal
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

## 3. Ciclo TDD Regla 1 - Precio base

### 3.1 RED - Tests fallan (commit c0be7bd, sin clase Producto)

**Comando ejecutado:**
```powershell
git checkout c0be7bd
python -m pytest tests/test_regla1_producto.py -v --tb=short
git checkout main
```

**Salida (FALLA):**
```
collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting tests/test_regla1_producto.py ________________
ImportError while importing test module '...\tests\test_regla1_producto.py'.
tests\test_regla1_producto.py:3: in <module>
    from libreria.producto import Producto
E   ImportError: cannot import name 'Producto' from 'libreria.producto'
    (...\src\libreria\producto.py). Did you mean: 'producto'?

=========================== short test summary info ===========================
ERROR tests/test_regla1_producto.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.28s ===============================
```

**Resultado RED:** 1 error - la clase `Producto` aun no existe en codigo de produccion.

---

### 3.2 GREEN - Tests pasan (commit f02a73e, implementacion minima)

**Comando ejecutado:**
```powershell
git checkout f02a73e
python -m pytest tests/test_regla1_producto.py -v
git checkout main
```

**Salida (EXITO):**
```
collected 3 items

tests/test_regla1_producto.py::TestRegla1CrearProducto::test_crear_producto_con_precio_valido PASSED [ 33%]
tests/test_regla1_producto.py::TestRegla1CrearProducto::test_rechazar_precio_base_cero PASSED [ 66%]
tests/test_regla1_producto.py::TestRegla1CrearProducto::test_rechazar_precio_base_negativo PASSED [100%]

============================== 3 passed in 0.02s ==============================
```

**Resultado GREEN:** 3 passed - Regla 1 implementada correctamente.

**Casos cubiertos:** CP-01 (positivo), CP-02 (negativo), CP-03 (negativo)

---

## 4. Ciclo TDD Regla 2 - Descuento porcentual

### 4.1 RED - Tests fallan (commit fc82d37, sin metodo aplicar_descuento)

**Comando ejecutado:**
```powershell
git checkout fc82d37
python -m pytest tests/test_regla2_descuento.py -v --tb=short
git checkout main
```

**Salida (FALLA):**
```
collected 5 items

tests/test_regla2_descuento.py::TestRegla2Descuento::test_aplicar_descuento_valido_intermedio FAILED [ 20%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_inferior_cero FAILED [ 40%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_superior_cuarenta FAILED [ 60%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_mayor_a_cuarenta FAILED [ 80%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_negativo FAILED [100%]

================================== FAILURES ===================================
________ TestRegla2Descuento.test_aplicar_descuento_valido_intermedio _________
tests\test_regla2_descuento.py:13: in test_aplicar_descuento_valido_intermedio
    producto_base.aplicar_descuento(20)
E   AttributeError: 'Producto' object has no attribute 'aplicar_descuento'

=========================== short test summary info ===========================
FAILED tests/test_regla2_descuento.py::TestRegla2Descuento::test_aplicar_descuento_valido_intermedio
FAILED tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_inferior_cero
FAILED tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_superior_cuarenta
FAILED tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_mayor_a_cuarenta
FAILED tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_negativo
============================== 5 failed in 0.13s ==============================
```

**Resultado RED:** 5 failed - el metodo `aplicar_descuento` aun no existe.

---

### 4.2 GREEN - Tests pasan (commit 6208fb0, implementacion minima)

**Comando ejecutado:**
```powershell
git checkout 6208fb0
python -m pytest tests/test_regla2_descuento.py -v
git checkout main
```

**Salida (EXITO):**
```
collected 5 items

tests/test_regla2_descuento.py::TestRegla2Descuento::test_aplicar_descuento_valido_intermedio PASSED [ 20%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_inferior_cero PASSED [ 40%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_aceptar_descuento_limite_superior_cuarenta PASSED [ 60%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_mayor_a_cuarenta PASSED [ 80%]
tests/test_regla2_descuento.py::TestRegla2Descuento::test_rechazar_descuento_negativo PASSED [100%]

============================== 5 passed in 0.02s ==============================
```

**Resultado GREEN:** 5 passed - Regla 2 implementada correctamente.

**Casos cubiertos:** CP-04 (positivo), CP-05 (borde), CP-06 (borde), CP-07 (negativo)

---

## 5. Ciclo TDD Regla 3 - Precio final con IVA

### 5.1 RED - Tests fallan (commit 6ceb98e, sin metodo calcular_precio_final)

**Comando ejecutado:**
```powershell
git checkout 6ceb98e
python -m pytest tests/test_regla3_precio_final.py -v --tb=short
git checkout main
```

**Salida (FALLA):**
```
collected 3 items

tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_calcular_precio_final_con_descuento_e_iva FAILED [ 33%]
tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_sin_descuento_incluye_iva FAILED [ 66%]
tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_nunca_es_negativo FAILED [100%]

================================== FAILURES ===================================
____ TestRegla3PrecioFinal.test_calcular_precio_final_con_descuento_e_iva _____
tests\test_regla3_precio_final.py:11: in test_calcular_precio_final_con_descuento_e_iva
    precio_final = producto.calcular_precio_final()
E   AttributeError: 'Producto' object has no attribute 'calcular_precio_final'

=========================== short test summary info ===========================
FAILED tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_calcular_precio_final_con_descuento_e_iva
FAILED tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_sin_descuento_incluye_iva
FAILED tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_nunca_es_negativo
============================== 3 failed in 0.11s ==============================
```

**Resultado RED:** 3 failed - el metodo `calcular_precio_final` aun no existe.

---

### 5.2 GREEN - Tests pasan (commit bb19504, implementacion minima)

**Comando ejecutado:**
```powershell
git checkout bb19504
python -m pytest tests/test_regla3_precio_final.py -v
git checkout main
```

**Salida (EXITO):**
```
collected 3 items

tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_calcular_precio_final_con_descuento_e_iva PASSED [ 33%]
tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_sin_descuento_incluye_iva PASSED [ 66%]
tests/test_regla3_precio_final.py::TestRegla3PrecioFinal::test_precio_final_nunca_es_negativo PASSED [100%]

============================== 3 passed in 0.02s ==============================
```

**Resultado GREEN:** 3 passed - Regla 3 implementada correctamente.

**Casos cubiertos:** CP-08 (positivo) y validacion de precio no negativo

---

## 6. Ciclo BDD - Escenarios Gherkin (Reglas 2 y 3)

### 6.1 RED - Sin step definitions (commit 2e816a4, solo archivo .feature)

**Comando ejecutado:**
```powershell
git checkout 2e816a4
python -m pytest features/ -v
git checkout main
```

**Salida (FALLA - sin tests ejecutables):**
```
collected 0 items

============================ no tests ran in 0.01s ============================
```

**Resultado RED:** Los escenarios Gherkin existen en `precio_producto.feature` pero no hay step definitions conectadas al codigo.

---

### 6.2 GREEN - Step definitions implementadas (estado final en main)

**Comando ejecutado:**
```powershell
python -m pytest features/test_precio_producto.py -v
```

**Salida (EXITO):**
```
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

**Resultado GREEN:** 7 passed - escenarios BDD conectados y funcionando.

**Escenarios BDD:** 5 escenarios (4 Scenario + 1 Scenario Outline con 3 Examples)

---

## 7. Suite completa TDD + BDD (estado final)

**Comando ejecutado:**
```powershell
python -m pytest -v
```

**Salida (EXITO):**
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

## 9. Resumen ciclo RED-GREEN por regla

| Regla | Commit RED | Resultado RED | Commit GREEN | Resultado GREEN |
|-------|-----------|---------------|--------------|-----------------|
| 1 - Precio base | c0be7bd | 1 error (ImportError) | f02a73e | 3 passed |
| 2 - Descuento | fc82d37 | 5 failed | 6208fb0 | 5 passed |
| 3 - Precio final | 6ceb98e | 3 failed | bb19504 | 3 passed |
| BDD Gherkin | 2e816a4 | 0 tests (sin steps) | dbcded0 | 7 passed |

---

## 10. Evidencia ciclo TDD en commits

### Regla 1
```powershell
git log --oneline --grep="Regla 1"
```
```
d351ecf refactor: REFACTOR Regla 1 - estructura inicial de clase Producto
f02a73e feat: GREEN Regla 1 - validacion de precio base mayor que cero
c0be7bd test: RED Regla 1 - tests de creacion de producto con precio base
```

### Regla 2
```powershell
git log --oneline --grep="Regla 2"
```
```
c8e5ffd refactor: REFACTOR Regla 2 - constante de descuento maximo
6208fb0 feat: GREEN Regla 2 - metodo aplicar_descuento con validacion
fc82d37 test: RED Regla 2 - tests de descuento porcentual entre 0 y 40
```

### Regla 3
```powershell
git log --oneline --grep="Regla 3"
```
```
bb19504 feat: GREEN Regla 3 - calculo de precio final con IVA del 19 por ciento
6ceb98e test: RED Regla 3 - tests de precio final con descuento e IVA
```

---

## 11. Resumen de cumplimiento

| Criterio | Resultado |
|----------|-----------|
| Ciclo RED demostrado (tests fallan) | Si - Reglas 1, 2, 3 y BDD |
| Ciclo GREEN demostrado (tests pasan) | Si - Reglas 1, 2, 3 y BDD |
| Tests unitarios TDD | 11 passed |
| Tests BDD Gherkin | 7 passed |
| Total tests | 18 passed |
| Cobertura de codigo | 100% |
| Repositorio publico | https://github.com/Jerov159/libreria-parcial-jeronimo_vallejo_q |

---

## 12. Comandos para reproducir evidencias RED y GREEN

Ejecutar desde la carpeta del proyecto:

```powershell
cd "c:\Users\ASUS\.vscode\Pruebas\Parcial 1"

# --- RED Regla 1 ---
git checkout c0be7bd
python -m pytest tests/test_regla1_producto.py -v --tb=short

# --- GREEN Regla 1 ---
git checkout f02a73e
python -m pytest tests/test_regla1_producto.py -v

# --- RED Regla 2 ---
git checkout fc82d37
python -m pytest tests/test_regla2_descuento.py -v --tb=short

# --- GREEN Regla 2 ---
git checkout 6208fb0
python -m pytest tests/test_regla2_descuento.py -v

# --- RED Regla 3 ---
git checkout 6ceb98e
python -m pytest tests/test_regla3_precio_final.py -v --tb=short

# --- GREEN Regla 3 ---
git checkout bb19504
python -m pytest tests/test_regla3_precio_final.py -v

# --- RED BDD (sin step definitions) ---
git checkout 2e816a4
python -m pytest features/ -v

# --- GREEN BDD + suite final ---
git checkout main
python -m pytest features/test_precio_producto.py -v
python -m pytest -v
python -m pytest --cov=libreria --cov-report=term-missing
```

**Captura sugerida:** `Win + Shift + S` en cada salida con FAILED o ERROR visible.
