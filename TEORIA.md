# Examen Parcial - Seccion Teorica
# Pruebas de Software - Semestre V

---

## SM-1

**Respuesta: C**

El enfoque descrito es el desarrollo tradicional con pruebas al final, donde QA entra cuando el modulo ya esta terminado. Las otras opciones son incorrectas porque shift-left busca adelantar las pruebas, shift-right se enfoca en produccion y monitoreo posterior al despliegue, e integracion continua es una practica de automatizacion y no un modelo donde QA diseÃ±a todo al cierre del desarrollo.

---

## SM-2

**Respuesta: B**

Se viola la primera regla de Uncle Bob: no escribir codigo de produccion sin un test previo que falle. Las demas opciones no aplican porque refactor ocurre despues de GREEN, la regla Green habla de codigo minimo pero no autoriza escribir todo antes de los tests, y TDD no permite implementar primero de forma general.

---

## Pregunta Abierta 01

En TDD, el paso GREEN existe para hacer pasar el test con la solucion mas simple posible, sin preocuparse aun por el diseno final. Eso mantiene el ciclo corto y demuestra que el test realmente guia el desarrollo. Si en GREEN se escribe codigo limpio y completo, se mezclan responsabilidades: se disena antes de tener evidencia de que los tests cubren el comportamiento necesario y se pierde la retroalimentacion rapida. Ademas, se corre el riesgo de sobreingenieria y de que los tests queden adaptados al codigo ya escrito en lugar de expresar requisitos. El refactor perderia sentido porque gran parte del diseno ya se hizo antes de tiempo.

---

## Pregunta Abierta 02

TDD resuelve el problema de construir software correcto desde la perspectiva del desarrollador: cada funcionalidad nace de un test que define el comportamiento esperado a nivel tecnico. BDD resuelve el problema de alinear negocio, QA y desarrollo usando lenguaje comprensible para todos, normalmente con escenarios Given-When-Then. TDD esta dirigido principalmente al equipo tecnico; BDD esta dirigido a roles no tecnicos y a validar que el sistema cumple necesidades reales del usuario. Se complementan porque TDD asegura calidad interna y diseno guiado por pruebas, mientras BDD asegura que se construye lo correcto desde la vision del negocio.

---

## Pregunta Abierta 03

La cobertura mide que lineas o ramas del codigo fueron ejecutadas por los tests, no si esas ejecuciones verificaron comportamientos correctos. Un test puede recorrer codigo sin asserts utiles o con expectativas incorrectas y aun asi subir el porcentaje. Por ejemplo, una funcion aplicar_descuento(20) puede tener un test que solo llama la funcion y no valida el resultado; la cobertura seria alta, pero un bug que guarde 0.2 en lugar de 20 pasaria desapercibido. Por eso cobertura alta reduce riesgo, pero no garantiza ausencia de defectos.

---

## Pregunta Abierta 04

Probar solo 20% asume erroneamente que el comportamiento es uniforme en todo el rango, pero la Regla 2 tiene limites y condiciones distintas en los bordes. Debo probar 0 y 40 como limites validos, valores justo fuera como -0.01 y 40.01, y al menos un valor intermedio como 20. Tambien conviene un negativo claro como -1 y uno invalido superior como 41, porque cada frontera puede fallar por validaciones diferentes.

---

## Pregunta Abierta 05

TDD y BDD alimentan CI/CD con pruebas automatizadas confiables que se ejecutan en cada cambio. En un pipeline, esas suites son la base para detectar regresiones antes del despliegue. Si el equipo no tiene tests automatizados solidos, CI/CD se convierte en un proceso que solo compila o despliega, pero no protege calidad: los defectos llegarian tarde a integracion o produccion, aumentando costo y riesgo. Las practicas agiles de prueba son prerequisito para que la integracion continua tenga valor real.

