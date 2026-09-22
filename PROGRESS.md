# Progreso del curso de Python — Admission Course Jala University

Estudiante: Yilmar
Carpeta del curso: C:\Users\USUARIO\Documents\python
Repositorio: https://github.com/Yilmar-sosa/curso-python
Última sesión: 21 sep 2026 — Sesión 2 COMPLETADA (calculadora de propina cerrada). Siguiente: Sesión 3.

> Este curso es independiente del curso de C (Documents\c ↔ curso-c). No mezclar.

## Estado de sesiones
- Sesión 1 — Pensamiento computacional y algoritmos: COMPLETADA ✅
- Sesión 2 — Bases de programación en Python: COMPLETADA ✅ (mini-reto de la calculadora de propina cerrado)
- Sesión 3 — Condicionales, listas y bucles: SIN INICIAR
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
- Sesión 2 — PENDIENTE de validar: `/` vs `//` (división normal vs entera). Ya validado: `float()` ✅ (lo usó en la calculadora), `NameError` ✅ (ya lo vivió en el cajero y lo explicó en el diagnóstico), mini-reto ✅ (calculadora de propina, ver abajo).

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

## Simulacros y notas
- (ninguno todavía)

## Temas débiles detectados
- Nada nuevo; el estudiante atrapó comparaciones invertidas y uso de `break` con guía.
- Reto recurrente: olvida que cada camino debe decidir su salida (lo resolvió con guardia `if intentos != 3` y moviendo `opcion` fuera del bucle).
- Aprendió por experiencia el `NameError`: usar una variable que solo existe en un `elif` fuera de ese bloque.
- Detalle opcional de UX: al rechazar retirar > saldo imprime "Entregando billetes []" (no rompe, pero se puede pulir algún día).

## Pendientes (para retomar mañana)
- (Ninguno de la Sesión 2: básicos completados y mini-reto cerrado)
- Validar `/` vs `//` (división normal vs entera) — quedó pendiente del diagnóstico de la Sesión 2; se puede validar al inicio de la Sesión 3 con 2 preguntas.
- Iniciar **Sesión 3 — Condicionales, listas y bucles**: `if/elif/else` (ya los usa), listas (índices 0-based como C, `len()`, `append()`, slicing), `while` (ya lo usa), `for` con `range()` y sobre listas, `break`/`continue`, acumuladores, anidados. Mini-reto: procesar una lista (promedio, mayor/menor) trasladando lo de C.

## Plan próxima sesión
- Sesión 3: validar `/` vs `//` → condicionales (repaso corto, ya los domina del cajero) → listas: índices, `len`, `append`, slicing (traducción directa de arreglos en C) → `for` con `range()` y `for valor in lista` → ejercicios de procesamiento de lista → mini-reto (promedio / mayor / menor).

## Ritual de cierre de sesión
- Actualizar PROGRESS.md → git add -A → commit → push (curso de Python, repo curso-python)