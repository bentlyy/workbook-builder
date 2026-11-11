# Plantillas: Blueprint, Ledger, Progreso y QA

## 1. Auditoría (`audit.md`)
```md
# Auditoría
## Referencia
- Páginas: ___  | Caracteres (texto): ___  | Unidades: ___
- Ejercicios totales: ___  | Ítems/ejercicio (media): ___
- % solucionario: ___  | Mix de tipos: ___

## Meta
- Tema: ___  | Audiencia/stack: ___  | Idioma: ___  | Nivel: ___ → ___
- Páginas objetivo: ___  | chars_por_página (est.): 2200
- chars_objetivo: ___  (= páginas × cpp)
- Reservas: ejercicios ___% | solucionario ___% (25-30)

## Presupuesto derivado
- Unidades: ___  | Ejercicios/unidad: ___  | Ítems/ejercicio: ___
- Chars/unidad: ___  | Ítems totales: ___
```

## 2. Blueprint + esqueleto (`blueprint.md`)
```md
# Blueprint maestro
## Arco y mapa de conceptos
- Nivel 1 (U1-U_): fundamentos [...]
- Nivel 2 ... (progresión → avanzando en complejidad e integración)

## TOC
| U | Título | Objetivo | Conceptos nuevos | Prerrequisitos | Chars | Ejercicios (tipo×n, ítems) |

## Unidad U__ — <Título>
**Contexto (3-5 líneas):** qué habilita / cuándo se usa.
**Presupuesto:** ___ chars | ___ ejercicios | ___ ítems | soluciones ___ chars
**Stubs:**
1. [Completar, 6 ítems] pista: ___
2. [Corregir + Correcto, 6 ítems] foco de error: ___
3. [Elegir c/ distractores, 5 ítems] distractores: ___
4. [Transformar, 5 ítems] de ___ a ___
5. [Reordenar/relacionar, 5 ítems] ___
6. [Escenario/diálogo, 4 ítems] contexto: ___
7. [Producción guiada, 3 ítems] entregable: ___
(repetir tabla/stubs por unidad)
```

## 3. Ledger anti-repetición (`ledger.md`)
Actualizar tras cada lote. Consultar antes de generar.
```md
# Ledger
## Cobertura de conceptos
| Concepto | Unidad(s) | Profundidad (intro/práctica/avanzado) |

## Escenarios y ejemplos usados (PROHIBIDO repetir)
| Unidad | Escenario/dominio | Datos/entidades | Snippets/identificadores clave |

## Mix de tipos (acumulado)
| Unidad | Completar | Corregir | Elegir | Transformar | Reordenar | Escenario | Producción | Total |

## Distractores/errores empleados
- <tema>: error usado → unidad/ejercicio (variar en siguientes)

## Términos introducidos
- U1: ...  U2: ... (evitar re-explicar salvo refuerzo planificado)
```

## 4. Progreso (`progress.md`)
```md
# Progreso vs presupuesto
| Unidad | Chars plan | Chars real | Ejercicios | Ítems | Soluciones chars | Acum. chars | Acum. % meta | Estado |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| U1 | | | | | | | | pendiente/en curso/hecho |

**Ajuste:** si acum.% < esperado, incrementar ítems/escenarios/snippets en próximo lote; si >, compactar sin perder tipos.
```

## 5. Checklist QA (Fase 4)
- [ ] Páginas/chars totales dentro de ±10% de meta (o justificado).
- [ ] Todas las unidades tienen micro-contexto y cumplen presupuesto mínimo.
- [ ] Progresión: prerrequisitos respetados, dificultad creciente.
- [ ] Mix de tipos balanceado por unidad; hay "Correcto" en corrección y distractores plausibles en elección.
- [ ] Huecos/pistas/ejemplos modelo presentes (andamiaje).
- [ ] Solucionario completo (~25–30%), con modelos para producción abierta.
- [ ] Cero repeticiones de escenarios/enunciados/distractores (validado contra ledger).
- [ ] HTML imprime correctamente (`@media print`, saltos de página por unidad/sección).
