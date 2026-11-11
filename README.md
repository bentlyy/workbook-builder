# Workbook Builder

Skill para agentes de IA que diseña **workbooks didácticos extensos** (HTML imprimible a PDF) replicando las estrategias pedagógicas de un documento guía.

En vez de generar el libro completo en un solo pase (lo que produce material incoherente, repetitivo y corto), la skill trabaja **por fases con artefactos de estado y presupuestos numéricos**, logrando libros de **~100–200+ páginas** con progresión, variedad de ejercicios y solucionario, sin repeticiones.

## Por qué existe

Pedirle a un modelo "hazme un cuaderno de 200 páginas" falla por dos motivos: pierde coherencia al crecer y repite escenarios. Esta skill resuelve eso externalizando la memoria y el control en archivos, de modo que el modelo ejecuta y los artefactos guardan el estado.

## Idea central

- **Trabajo subdividido obligatorio**: prohibido un solo pase. Fases con *gates* (no se avanza sin cumplir la anterior).
- **Estrategia híbrida Blueprint + Esqueleto + Ledger por lotes** (E5): mejor coherencia y menor repetición con escalabilidad controlada.
- **Presupuesto numérico**: `caracteres_objetivo = páginas × caracteres/página` (~2.2k chars/pág en A4), reservando ~25–30% para el solucionario.
- **Portabilidad entre modelos**: adapta el tamaño de lote y el rigor según la capacidad del modelo (alta / media / baja). Modelos más capaces → resultados más ricos; el estado externo mantiene la estructura y la escala en cualquier caso.

## Fases

| Fase | Salida | Propósito |
|---|---|---|
| 0 · Auditoría | `audit.md` | Medir la referencia y fijar meta, idioma, audiencia y presupuesto. |
| 1 · Blueprint | `blueprint.md` | TOC, arco de dificultad y stubs por unidad con mix de tipos. |
| 2 · Ledger | `ledger.md` | Registro vivo anti-repetición (conceptos, escenarios, distractores). |
| 3 · Generación | `units/` + `progress.md` | Generar por lotes respetando stubs, andamiaje y huecos. |
| 4 · QA | HTML final | Ensamblar, verificar conteos vs presupuesto y medir desviación. |

## Estructura del repositorio

```
SKILL.md                          Definición de la skill (fases, reglas, portabilidad)
references/
  pedagogia-workbook.md           Patrón pedagógico (progresión, tipos, huecos, andamiaje)
  estrategias-escala.md           Análisis comparativo de estrategias de escala (E1–E5)
  blueprint-y-ledger.md           Plantillas de audit / blueprint / ledger / progress / QA
templates/
  workbook-template.html          Base HTML/CSS imprimible (@media print)
examples/
  unidad-ejemplo.md               Unidad de ejemplo (formato y tono)
  workbook-fullstack.html         Ejemplo corto (referencia de formato, no de tamaño)
fullstack-200/                    Ejemplo COMPLETO a escala (ver abajo)
```

## Ejemplo a escala — `fullstack-200/`

Workbook de desarrollo web full-stack generado con la skill, como demostración del resultado a tamaño real:

- **20 unidades** en 4 niveles (fundamentos → entrega), tema: full-stack (JS/Node, TS, React, Next, Express, PostgreSQL, auth, testing, CI/CD, Docker).
- **380 ejercicios** con tipos variados: completar, corregir (con ítems "Correcto"), elegir con distractores, transformar, reordenar/relacionar, escenario/diálogo, producción, caso integrador, RCA y diseño técnico.
- **~461.000 caracteres (~199 páginas)**, solucionario ~21% con claves y guía/rúbrica por unidad.
- Artefactos reales del proceso: `audit.md`, `blueprint.md`, `ledger.md`, `progress.md`, `units/` y scripts (`qa.py`, `assemble.py`).
- Resultado: [`fullstack-200/workbook-fullstack-200.html`](fullstack-200/workbook-fullstack-200.html) (abrir en el navegador e imprimir a PDF).

## Uso

1. Coloca la carpeta en el directorio de skills de tu cliente de IA:
   - **opencode**: `~/.config/opencode/skills/workbook-builder/`
   - **Claude / otros**: `skills/workbook-builder/`
2. Pide el workbook indicando tema, audiencia y tamaño objetivo, por ejemplo:
   > "Crea un workbook de práctica de ~150 páginas sobre SQL para analistas junior, con solucionario."
3. La skill arranca en Fase 0 (auditoría + presupuesto) y avanza por lotes actualizando `ledger.md` y `progress.md` hasta el QA final.

## Clonar

```bash
git clone https://github.com/bentlyy/workbook-builder.git
```

## Licencia

MIT
