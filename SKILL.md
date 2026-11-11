---
name: workbook-builder
description: Diseña workbooks didácticos extensos (HTML imprimible a PDF) replicando estrategias pedagógicas de un documento guía. Usar cuando el usuario pida crear un cuaderno/workbook de práctica, material formativo estilo libro, o escalar un workbook a gran tamaño (~100-200+ páginas) con progresión, variedad de ejercicios y solucionario sin repeticiones.
---

# Workbook Builder (escala y coherencia)

Genera workbooks temáticos que igualan un documento guía en: progresión y contexto, tipos de ejercicios, alternativas buenas/malas, huecos y andamiaje, y tamaño (p. ej. ~200 páginas) manteniendo coherencia y sin repeticiones.

## Regla principal: trabajo subdividido obligatorio
**Prohibido** generar el libro completo en un solo pase. Sigue siempre las fases y artefactos de estado. Estrategia por defecto: **Híbrida Blueprint+Esqueleto+Ledger por lotes** (ver `references/estrategias-escala.md`, E5).

## Principio de portabilidad entre modelos
La calidad final sí tiende a mejorar con modelos más capaces (mejor seguimiento de instrucciones, coherencia, redacción, casos más ricos y menos repeticiones), **pero la skill reduce la dependencia del modelo** externalizando memoria y control en artefactos (`audit`, `blueprint`, `ledger`, `progress`) y scripts (`qa.py`/ensamble). El modelo ejecuta; los archivos guardan el estado.

## Adaptación según capacidad del modelo
Seleccionar en Fase 0 (`audit.md`, campo `capacidad_modelo: alta|media|baja`) y ajustar lote/rigor:

| Capacidad | Lote (F3) | Rigor | Uso de recursos |
|---|---|---|---|
| Alta | 1 unidad por iteración | Puede enriquecer escenarios y redacción manteniendo stubs/presupuesto | QA por lote o cada 2 unidades; aprovecha para casos integradores/RCA más profundos |
| Media | 1 unidad por iteración | Seguir stubs, plantillas y mix al pie de la letra; no improvisar estructura | `qa.py` cada lote; actualizar `ledger/progress` sin excepción |
| Baja | 3–4 ejercicios (sub-bloque) por iteración | Plantillas rígidas, frases simples, un tipo de tarea a la vez; copiar formato de ejemplos | `qa.py` y actualización de estado en cada sub-bloque; ensamblar solo con script |

Reglas: si hay desvío de presupuesto, duplicados o pérdida de coherencia, **reducir tamaño de lote** y volver a stubs/plantillas. Nunca sacrificar gates por velocidad.

## Fases (gates)

### Fase 0 — Auditoría de referencia y meta
- Medir referencia (si existe): páginas, caracteres, #unidades, ejercicios/unidad, ítems/ejercicio, proporción de solucionario.
- Fijar meta: páginas objetivo (p. ej. 200), idioma, audiencia/stack, nivel inicial→objetivo.
- Calcular presupuesto: `chars_obj = paginas_obj × chars_por_pagina` (impresión A4, CSS base: ~2.2k chars/pág). Reservar ~25–30% para solucionario.
- Salida: `audit.md` (métricas ref + meta + presupuesto). No avanzar sin esto.

### Fase 1 — Blueprint maestro + esqueleto
- Crear TOC completo (18–22 unidades para ~200p), arco de dificultad y mapa de conceptos por unidad.
- Por unidad: objetivo, micro-contexto (3–5 líneas), lista de ejercicios con tipo + nº de ítems (stubs) y presupuesto (chars/ítems).
- Definir mix obligatorio de tipos por unidad (completar, corregir con ítems "Correcto", elegir con distractores, transformar, reordenar/relacionar, diálogo/escenario, producción).
- Salida: `blueprint.md` + esqueleto HTML/MD con todos los stubs. Ver plantilla en `references/blueprint-y-ledger.md`.

### Fase 2 — Ledger (estado vivo anti-repetición)
- Inicializar registro: conceptos cubiertos, escenarios/ejemplos usados, términos introducidos, distribución de tipos, errores/distractores ya empleados.
- Regla: antes de generar un lote, consultar ledger; prohibido reutilizar escenarios, enunciados o distractores ya usados (variar dominio, datos y superficie).
- Salida: `ledger.md` (actualizar en cada lote).

### Fase 3 — Generación por lotes
- Generar por iteración según capacidad (ver tabla): **1 unidad** (alta/media) o **sub-bloque de 3–4 ejercicios** (baja), respetando stubs y presupuesto.
- Cada lote debe incluir: micro-contexto, andamiaje (ejemplo modelo en los primeros ítems/bloques), huecos proporcionales, distractores plausibles y al menos un ítem "Correcto" en corrección.
- Tras cada lote: actualizar `ledger.md` y `progress.md` (chars/ejercicios/ítems acumulados vs presupuesto), ejecutar/verificar conteos (`qa.py` o métricas) y ajustar densidad del siguiente lote para converger a la meta.
- No avanzar más de 1–2 unidades (o 2 sub-bloques en baja) sin actualizar estado. Ante repetición o deriva, reducir lote y reanclar en blueprint/ledger.

### Fase 4 — Ensamble y QA
- Concatenar unidades en HTML único (CSS print-ready) + solucionario final (~25–30%).
- Verificar: conteos vs presupuesto (páginas/chars/ejercicios), progresión y contexto por unidad, balance de tipos, calidad de alternativas (plausibles, no absurdas), huecos/pistas, y **cero repeticiones** (cruce con ledger).
- Entregar métricas finales y desviación % respecto a meta.

## Presupuesto orientativo (~200 páginas)
- 18–22 unidades × (contexto + 8–10 ejercicios × 5–8 ítems + soluciones) ≈ 180–220p, ~400–480k chars.
- Mix por unidad: completar(2), corregir+“Correcto”(1–2), elegir con distractores(1–2), transformar(1), reordenar/relacionar(1), escenario/producción(1–2).
- Densidad: escenarios/diálogos, snippets de código, tablas y enunciados ricos (no solo una línea) para alcanzar volumen con valor.

## Recursos
- `references/pedagogia-workbook.md`: patrón pedagógico (progresión, tipos, huecos, andamiaje, distractores, soluciones).
- `references/estrategias-escala.md`: análisis comparativo y experimento de estrategias (E1–E5); justificación de la híbrida.
- `references/blueprint-y-ledger.md`: plantillas de auditoría, blueprint, ledger, progress y checklist QA.
- `templates/workbook-template.html`: base HTML/CSS imprimible (`@media print`).
- `examples/workbook-fullstack.html`: ejemplo corto (no a escala); usar como referencia de tono/formato, no de tamaño.
