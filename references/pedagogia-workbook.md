# Guía pedagógica: patrón de workbook de ejercicios

Extraída del análisis de un workbook de inglés A1→C1 (progresión por niveles, práctica intensiva, solucionario). Usar como checklist para generar workbooks de otros temas.

## 1. Estructura macro
- **Índice por niveles/módulos** con breve promesa de aprendizaje por bloque ("Nivel X: qué permite lograr").
- **Unidades temáticas** secuenciadas de básico a avanzado; cada unidad agrupa 10–20 ejercicios.
- **Solucionario al final** ("Respuestas - …") con claves por ejercicio y, cuando hay producción abierta, respuestas modelo "(posibles respuestas/soluciones)".

## 2. Apertura de unidad (micro-contexto)
- Título numerado: `N. Tema (traducción/alias si aplica)`.
- 1 frase de encuadre: para qué sirve, cuándo se usa o qué habilidad habilita. Sin teoría larga; la práctica lleva el peso.

## 3. Tipos de ejercicio y formato
| Tipo | Instrucción típica | Señales de diseño |
|---|---|---|
| Completar | "Completa las frases/oraciones con…" | Huecos `________` + pista entre paréntesis `(verbo/tiempo/pista)` |
| Transformar | "Reescribe/Convierte…" | Ejemplo modelo; pares afirmativa/negativa/interrogativa o cambio de forma |
| Corregir | "Corrige los errores…" | Mezclar ítems ya correctos → respuesta "Correcta" |
| Elegir opción | "Elige la opción correcta…" | Opciones inline `(a / b)` o lista; distractores plausibles |
| Reordenar | "Ordena/Reordena…" | Palabras o pasos desordenados → línea de respuesta |
| Diálogo/escenario | "Completa el diálogo/texto…" | Huecos en contexto conversacional o narrativo |
| Producción guiada | "Escribe 3 frases…" / "Traduce…" | Consigna clara + espacio amplio; en soluciones, ejemplos modelo |
| Clasificar/relacionar | "Clasifica/Une…" | Categorías o emparejamiento A→1 |

## 4. Diseño de ítems
- **Distractores plausibles**: errores típicos del nivel/tema (confusión de forma, tiempo, concepto cercano), no absurdos.
- **Andamiaje**: primer ítem o bloque puede traer ejemplo resuelto; dificultad crece dentro y entre unidades.
- **Variación de respuesta**: frase corta, palabra, reescritura completa, tabla/lista; evita monotonía.
- **Espacio de respuesta**: línea subrayada/hueco proporcional (corto para palabra, largo para frase/párrafo).

## 5. Tono y presentación
- Instrucciones directas y consistentes ("Completa…", "Corrige…", "Escribe…").
- Numeración jerárquica (Unidad → Ejercicio → ítem a/b/c).
- Vocabulario/meta del dominio introducido en contexto, no en glosario extenso.
- Solucionario separado al final para permitir autoevaluación.

## 6. Adaptación a temas técnicos (p. ej. desarrollo web)
- Mapear "gramática/tiempos" a conceptos/sintaxis/APIs; "diálogos" a flujos cliente-servidor o code review; "traducción" a refactor entre paradigmas (JS→TS, callback→async, REST→validado).
- Mantener corrección de errores con snippets "Correcto"/bug realista, y opciones con implementaciones plausible-incorrectas (seguridad, tipos, async, SQL).
- Incluir escenarios: diseñar endpoint, test, pipeline, esquema; producción: escribir handler, test, query, Dockerfile fragment.
