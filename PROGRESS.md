# Progreso del curso de Python — Admission Course Jala University

Estudiante: Yilmar
Carpeta del curso: C:\Users\USUARIO\Documents\python
Repositorio: https://github.com/Yilmar-sosa/curso-python
Última sesión: 20 sep 2026 — Sesión 1 (en curso; estudiante pidió descanso, retomamos mañana)

> Este curso es independiente del curso de C (Documents\c ↔ curso-c). No mezclar.

## Estado de sesiones
- Sesión 1 — Pensamiento computacional y algoritmos: EN CURSO
- Sesión 2 — Bases de programación en Python: SIN INICIAR
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
- Cierre total del mini-reto Sesión 1: PENDIENTE (faltan bugs del cajero, abajo).

## Simulacros y notas
- (ninguno todavía)

## Temas débiles detectados
- Nada nuevo; el estudiante atrapó comparaciones invertidas y uso de `break` con guía.
- Reto de próxima: no dejar el `break` solo en una rama (olvida que cada camino debe decidir su salida).

## Pendientes (para retomar mañana)
En `sesion01/cajero.py`:
1. Opción 2 (retirar): falta `break` después de `print("Entregando billetes...")` → al terminar vuelve a pedir la clave (confirmado por ejecución).
2. Bloqueo temprano: `if intentos == 2` bloquea después de 2 fallos; deben ser 3 intentos → esa condición debe ser `== 3` (o revisar el mensaje "Tiene N restantes" para que cuadre con 3 intentos).
3. El saldo nunca se descuenta: tras retirar 480, saldo sigue mostrando 1000. Falta restar el monto (y decidir si se actualiza `saldoactual`).
4. (Opcional) Probar la opción "cualquier otro número para salir" del menú — hoy no se probó.

## Plan próxima sesión
- Retomar: cerrar los 3 pendientes del cajero con preguntas guiadas → ejecutar y aprobar el mini-reto de Sesión 1 → iniciar Sesión 2 (bases de Python: print, input, variables, tipos, f-strings — ya los tocó de forma natural).

## Ritual de cierre de sesión
- Actualizar PROGRESS.md → git add -A → commit → push (curso de Python, repo curso-python)