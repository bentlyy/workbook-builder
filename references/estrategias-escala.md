# Estrategias de escala para workbooks largos (~200 páginas)

## Objetivo
Igualar documento guía en: (1) progresión y contexto, (2) tipos de ejercicios, (3) alternativas buenas/malas, (4) huecos y andamiaje, (5) tamaño/cantidad (~200 páginas) manteniendo coherencia y sin repeticiones.

## Línea base (medida)
| Artefacto | Páginas | Chars aprox. | Estructura |
|---|---:|---:|---|
| Referencia (EN workbook PDF) | 201 | ~466k (texto extraído) | Niveles A1→C1, ~80 bloques de ejercicios, soluciones extensas |
| Full-stack v1 (HTML) | ~12-15 (estimado impresión) | 26k | 7 unidades, 29 ejercicios, 4-5 ítems c/u |

**Densidad objetivo (impresión A4, márgenes 15-16mm, CSS actual):** ~1.8k–2.4k caracteres útiles/página HTML → para 200 páginas se requieren **~360k–480k caracteres** de contenido (incl. enunciados, huecos, bloques de código, solucionario).

## Dependencia del modelo y mitigaciones
- **Mejor modelo → mejor resultado esperado:** mayor adherencia a instrucciones largas, coherencia entre lotes, variedad de escenarios, calidad de distractores/redacción y menor tasa de repetición/deriva.
- **Mitigaciones de la skill (para que funcione con modelos diversos):** descomposición obligatoria, artefactos de estado (blueprint/ledger/progress) como memoria externa, stubs y presupuesto numérico, plantillas, scripts deterministas (ensamble/qa) y reducción de tamaño de lote en capacidad baja.
- **Implicación práctica:** la E5 + estado externo mantiene la estructura y escala alcanzable; la riqueza pedagógica y finura editorial escalan con la capacidad del modelo.

## Estrategias evaluadas

### E1. Monolítica (un solo pase)
- **Método:** generar todo el HTML en una respuesta.
- **Proyección a 200p:** inviable en salida única; obliga a resumir → ~20-40p reales.
- **Coherencia:** baja (deriva tonal/temática). **Repetición:** alta.
- **Puntaje escala:** 10/100. **Veredicto:** descartar.

### E2. Secuencial sin estado
- **Método:** generar unidad 1, luego 2, etc., sin memoria estructurada más allá del chat.
- **Proyección:** puede sumar páginas, pero sin presupuesto por unidad el total oscila (80-220p).
- **Coherencia:** media-baja; conceptos se repiten o se olvidan; dificultad irregular.
- **Puntaje escala:** 45/100. **Veredicto:** insuficiente para 200p fiables.

### E3. Blueprint + ledger + generación por lotes (RECOMENDADA)
- **Método:**
  1. **Auditoría:** medir referencia (páginas, chars, #unidades, ejercicios/unidad, ítems/ejercicio, proporción soluciones).
  2. **Blueprint maestro:** TOC completo, objetivos y micro-contexto por unidad, mapa de conceptos, presupuesto (páginas/chars/ejercicios/ítems) y curva de dificultad.
  3. **Ledger de estado:** registro vivo de conceptos cubiertos, escenarios usados, vocabulario/términos introducidos, tipos de ejercicio por unidad y ejemplos empleados (para prohibir repetición).
  4. **Producción por lotes:** generar 1 unidad (o sub-bloque) por iteración usando blueprint + ledger; cada salida actualiza ledger.
  5. **Ensamble + QA:** concatenar fragmentos, verificar conteos vs presupuesto, deduplicar, chequear progresión y balance de tipos.
- **Proyección (cálculo):** 20 unidades × (1 pág. portada/contexto + 6 págs. ejercicios × 18 ítems + 3 págs. soluciones) ≈ 200 páginas. En chars: 20 × (2k + 12k + 6k) ≈ 400k.
- **Coherencia:** alta (blueprint fija arco; ledger evita repetición). **Control de tamaño:** alto (presupuesto explícito).
- **Puntaje escala:** 92/100. **Veredicto:** adoptar como obligatoria.

### E4. Esqueleto global + expansión (doble pasada)
- **Método:** (A) generar esqueleto de todas las unidades con títulos, contextos y stubs de cada ejercicio (instrucción + nº de ítems) para fijar cobertura y volumen; (B) expandir lote a lote rellenando ítems y soluciones.
- **Proyección:** excelente control de longitud (stubs definen conteo exacto); 200p alcanzable si stubs dimensionan ítems/líneas.
- **Coherencia:** muy alta en cobertura; riesgo de texto plano en expansión si no hay ledger de estilo/escenarios.
- **Puntaje escala:** 88/100. **Veredicto:** combinar con E3 (esqueleto como parte del blueprint).

### E5. Híbrida E3+E4 (óptima)
- **Método:** Blueprint+esqueleto (TOC, contextos, stubs con conteos) → expansión por lotes con ledger → ensamble y auditoría de métricas.
- **Proyección:** 95-105% del objetivo de páginas cuando se respeta presupuesto por unidad y se reserva ~30% para solucionario (como referencia).
- **Coherencia:** muy alta. **Repetición:** mínima (ledger de escenarios/conceptos).
- **Puntaje escala:** 96/100. **Veredicto:** estrategia por defecto de la skill.

## Experimento (estimación comparativa)
Supuesto: 200 páginas objetivo, 2200 chars/pág, 30% solucionario.

| Estrategia | Unidades planificadas | Ejercicios | Ítems | Chars estimados | Pág. estimadas | Coherencia (1-5) | Repetición (1-5, menor mejor) | % objetivo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| E1 Monolítica | 7 | 30 | 120 | 30k | 14 | 2 | 4 | 7% |
| E2 Secuencial sin estado | 12-25 (variable) | 120 | 500 | 180k | 82 | 3 | 4 | 41% |
| E3 Blueprint+ledger | 20 | 170 | 850 | 420k | 191 | 5 | 1 | 96% |
| E4 Esqueleto+expansión | 20 | 170 | 850 | 430k | 195 | 4 | 2 | 98% |
| E5 Híbrida E3+E4 | 20 | 180 | 900 | 445k | 202 | 5 | 1 | 101% |

**Conclusión:** E5 es la que más se acerca al 100% de largo (≈101%) manteniendo coherencia y concordancia. La skill debe imponerla.

## Presupuesto de referencia (para igualar ~200 páginas)
- **Unidades/niveles:** 18–22 (progresión básico→avanzado).
- **Por unidad:** micro-contexto (3-5 líneas) + 8–10 ejercicios + 5–8 ítems por ejercicio + bloques de código/diálogos donde aplique.
- **Mix por unidad:** completar (2), corregir con “Correcto” (1-2), elegir opción con distractores (1-2), transformar (1), reordenar/relacionar (1), escenario/producción (1-2).
- **Solucionario:** ~25-30% del total; claves + modelos para producción abierta.
- **Control:** tras cada lote, contar chars/ejercicios y comparar contra presupuesto acumulado; ajustar densidad del siguiente lote (más ítems, enunciados más ricos, escenarios más largos) para converger a meta.
