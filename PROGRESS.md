# Progreso del curso de Python — Admission Course Jala University

Estudiante: Yilmar
Carpeta del curso: C:\Users\USUARIO\Documents\python
Repositorio: https://github.com/Yilmar-sosa/curso-python
Última sesión: 24 sep 2026 — Sesión 3 EN CURSO (suma/promedio cerrados; falta mayor/menor y mini-reto).

> Este curso es independiente del curso de C (Documents\c ↔ curso-c). No mezclar.

## Estado de sesiones
- Sesión 1 — Pensamiento computacional y algoritmos: COMPLETADA ✅
- Sesión 2 — Bases de programación en Python: COMPLETADA ✅ (mini-reto de la calculadora de propina cerrado)
- Sesión 3 — Condicionales, listas y bucles: EN CURSO (listas y for vistos; falta mayor/menor + mini-reto)
- Sesión 4 — Simulacro Módulo I (≥70%): SIN INICIAR
- Sesión 5 — POO básica: SIN INICIAR
- Sesión 6 — Agregación y composición: SIN INICIAR
- Sesión 7 — Estrategias de resolución con POO: SIN INICIAR
- Sesión 8 — Simulacro Módulo II (≥70%): SIN INICIAR
- Sesiones 9–10 — Pair programming de un juego (≥80%): SIN INICIAR

## Conceptos completados
- Sesión 1: algoritmo, descomposición de problemas, pseudocódigo libre (SI...ENTONCES / MIENTRAS...HACER), ciclo problema → datos → salida → pasos → decisiones → código → prueba → corrección.
- Descubrió por sí mismo el algoritmo voraz (greedy) para billetes de cajero. 🏆
- Saltó del pseudocódigo a código Python real (por iniciativa propia): usó variables, listas, `input()/int()`, f-strings, `while`, `if/elif/else`, `break`, `append`. Entiende la idea de `break` (ya lo aplicó bien en opción 1).
- Sesión 2 — ya demostró por diagnóstico (mini-check 9 preguntas + 2 de refuerzo):
  - `print`, comentarios `#`, f-strings con `{}` ✅
  - Variables dinámicas y tipos `int`, `float`, `str` ✅
  - `input()` + conversión `int()` y `str()` ✅
  - Operadores de comparación (`<=`, `==`, `!=`) usados en el cajero ✅
  - Operadores lógicos `and`/`or` ✅ (corrigió idea previa de que `and` imprime ambos)
  - Módulo `%` = residuo ✅ (corrigió idea de porcentaje → hoy domina 15%4=3, 9%3=0)
  - `TypeError` por mezclar texto con número ✅ (entendió que hay que convertir)
- Sesión 2 — PENDIENTE de validar: `/` vs `//` (división normal vs entera). ✅ VALIDADO al inicio de Sesión 3: `7/2=3.5`, `7//2=3`, `7%2=1` (las 3 respuestas correctas).
- Sesión 3 — conceptos completados:
  - Listas: índices 0-based (traducción directa de C) ✅, `len()` ✅.
  - Índices negativos: -1 último, -2 penúltimo... ✅ (explicó la regla solo).
  - Slicing: `[inicio:fin]` con **fin sin incluir** ✅, `[inicio:]`, `[:fin]`, avanzar del slice: si <fin no se incluye; `[-2:]` no retrocede, avanza al final ✅.
  - Regla clave: `lista[i]` = UNA caja vs `lista[i:j]` = tramo; el colon es lo único que abre tramo. El estudiante recaía en leer `[-N]` como `[-N:]` (le agregaba el colon mentalmente); se rompió el patrón con la "regla de emergencia" (un solo número = UNA caja) ✅.
  - Detalle Python: `lista[:-3]` = "todo menos las 3 últimas" (confundió una vez, aclarado).
  - `for i in range(n)` = 0..n-1 (off-by-one corregido: dijo 1,2,3,4 para range(4); realidad 0,1,2,3; se ató a `i < n` de C) ✅.
  - `for valor in lista` (directo) vs `for i in range(len(lista))` (con índice); sabe elegir: posición → índice, valores → directo ✅.
  - GOTCHA aprendido: la variable del bucle sobrevive tras el bucle con el último valor (imprimió 75 por usar `{nota}` tras el loop; halló por qué él mismo) ✅.

## Ejercicios resueltos
- Pseudocódigo del café (completo, aprobado).
- Texto 2 (algoritmo numerado del cajero, pasos 1–22): hecho, aprobado con corrección de comparación invertida (paso 13 pasó a "mayor a 0").
- `sesion01/cajero.py`: AHORA ES CÓDIGO PYTHON REAL, no comentarios.
  - ✅ Algoritmo voraz de billetes funciona (480 → [100,100,100,100,50,20,10]).
  - ✅ Contador de intentos funciona (mensaje con intentos restantes).
  - ✅ Validación de saldo insuficiente funciona (retirar > saldo → rechaza).
  - ✅ Comparación `<=` corregida (retirar todo el saldo es válido).
  - ✅ `break` en opción 1 (consultar saldo) → termina bien.
  - ❌ Faltan correcciones (ver pendientes).

## Mini-retos superados
- Texto 1 (café): superado.
- Texto 2 (cajero, pasos numerados 1–N): superado con corrección.
- Mini-reto Sesión 1 (cajero en Python): CERRADO ✅ — todos los bugs resueltos:
  1. Retirar ya no vuelve a pedir la clave (opción del menú movida fuera del bucle con `break`).
  2. Cuenta se bloquea con 3 intentos (`intentos == 3`) y termina limpio (guardia `if intentos != 3`).
  3. Saldo se descuenta correctamente (`saldoactual -= billetes[i]`) → 1000 → 520.
  4. `NameError` de `monto_a_retirar` corregido (su uso quedó protegido en el flujo correcto).
  - Verificado con 6 escenarios ejecutados: consultar, retirar, bloqueo, 2 malas + 1 buena, salir, retirar > saldo.
- Mini-reto Sesión 2 (calculadora de propina, `sesion02/propina.py`): CERRADO ✅ — código escrito por el estudiante SIN copiar (reconoció y corrigió al tutor por adelantarse a dar el código).
  - Usa `float()` para la cuenta y `int()` para el porcentaje ✅
  - `propina = cuenta * porcentaje / 100` ✅ (explicó: división entre 100 = el 1% del valor)
  - `cuenta_total = cuenta + propina` ✅ (lo agregó tras pista: faltaba el total)
  - Muestra los 3 valores con f-strings y símbolo de moneda ✅ (agregó la propina en pesos tras recordatorio de requisitos)
  - Verificado con ejecución: entrada 40/10 → Cuenta $40.0, Propina $4.0, Total $44.0
- Sesión 3 — `sesion03/suma_notas.py`: CERRADO ✅ (suma + promedio).
  - Suma con acumulador `suma = 0; for nota in notas: suma = suma + nota` → 380 ✅.
  - Promedio `suma / len(notas)` → 76.0 ✅.
  - Adoptó convenciones de nombres (listas → `notas`, valor del bucle → `nota`).
  - Corrigió bug: `print(f"... {nota}")` tras el bucle imprimía el último valor (75) — aprendió el gotcha de la variable sobreviviente ✅.

## Simulacros y notas
- (ninguno todavía)

## Temas débiles detectados
- Sesión 1: comparaciones invertidas y uso de `break` (resueltos con guía). Reto recurrente: olvida que cada camino debe decidir su salida (resuelto con guardia `if intentos != 3`).
- Sesión 2: vivió y explicó el `NameError` (variable que solo existe en un `elif` usada fuera de ese bloque).
- Sesión 3 (vigilar en próximos ejercicios):
  - Off-by-one con `range(n)` (pensaba 1..n en vez de 0..n-1) — corregido atándolo a `i < n` de C.
  - Recaída antigua: leía `lista[-N]` como `lista[-N:]` (agregaba colon mental) — roto con la "regla de emergencia"; vigilar.
  - Gotcha de la variable del bucle que sobrevive — lo entendió y lo explicó él mismo.

## Pendientes (para retomar)
- **Sesión 3 — continuar:**
  - Algoritmo de mayor/menor SIN `max()`/`min()` (patrón del campeón): el estudiante iba a describir los pasos del algoritmo en papel. NO ha codificado nada de esto todavía.
  - Mini-reto de la Sesión 3: procesar una lista completa (promedio + mayor + menor) — lo armaremos sobre `suma_notas.py` o archivo nuevo en `sesion03/`.

## Plan próxima sesión
- Retomar Sesión 3: mayor/menor sin `max()`/`min()` (describir algoritmo en papel → traducir a Python → probar con la lista de notas) → mini-reto: procesar una lista completa (promedio, mayor, menor) → cerrar Sesión 3 → si sobra tiempo, repaso rápido de condicionales/`break`/`continue`.

## Ritual de cierre de sesión
- Actualizar PROGRESS.md → git add -A → commit → push (curso de Python, repo curso-python)