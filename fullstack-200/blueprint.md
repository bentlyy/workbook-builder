# Blueprint maestro (Fase 1)

## Arco y mapa de conceptos
- **Nivel 1 (U1–U5) Fundamentos:** JS moderno, TypeScript, asincronía, HTTP/REST, Git y calidad base.
- **Nivel 2 (U6–U10) Frontend:** React 18, estado/efectos, Next.js App Router, UI/Tailwind/accesibilidad, integración cliente.
- **Nivel 3 (U11–U15) Backend y datos:** Node/Express/Nest, validación/errores, PostgreSQL/SQL, Prisma/ORM, arquitectura y multi-tenancy.
- **Nivel 4 (U16–U20) Seguridad, testing y entrega:** authN/authZ (JWT/RBAC/2FA), hardening, testing y cobertura, Docker/CI-CD, observabilidad y operación.

## TOC y presupuesto
| U | Título | Objetivo | Conceptos nuevos | Prerrequisitos | Chars ej | Ej (ítems) | Chars sol |
|---|---|---|---|---|---:|---:|---:|
| 1 | JS moderno y entorno Node 20+/ESM | Escribir JS fiable con módulos y estructuras modernas | let/const, scope, módulos ESM, desestructuración, spread, npm/scripts | base JS | 16240 | 9 (54) | 6960 |
| 2 | TypeScript esencial: tipos y narrowing | Modelar datos y reducir errores en compilación | tipos, uniones, interfaces/type, generics básicos, unknown, narrowing | U1 | 16240 | 9 (54) | 6960 |
| 3 | Asincronía: callbacks, promesas, async/await | Controlar flujos async y errores | event loop, promesas, async/await, Promise.all/settled, try/catch | U1-U2 | 16240 | 9 (54) | 6960 |
| 4 | HTTP, REST y diseño de APIs | Diseñar contratos claros y predecibles | métodos, códigos, recursos, idempotencia, paginación, versionado | U1-U3 | 16240 | 9 (54) | 6960 |
| 5 | Git, colaboración y revisión | Gestionar cambios y calidad colaborativa | ramas, commits, PR, conflictos, code review, convenciones | U1-U4 | 16240 | 9 (54) | 6960 |
| 6 | React 18: componentes, props y estado | Construir UI declarativa y predecible | JSX, props, estado, renderizado, listas/keys, composición | U1-U3 | 16240 | 9 (54) | 6960 |
| 7 | React: efectos, hooks y rendimiento | Manejar efectos y evitar renders/cierres problemáticos | useEffect, dependencias, useMemo/useCallback, custom hooks | U6 | 16240 | 9 (54) | 6960 |
| 8 | Next.js App Router y Server Components | Separar servidor/cliente y controlar datos/caché | rutas, layouts, Server/Client, fetch/caché, loading/error | U6-U7,U4 | 16240 | 9 (54) | 6960 |
| 9 | UI con Tailwind, formularios y accesibilidad | Crear interfaces usables y accesibles | utilidades, responsive, formularios, validación UI, a11y básica | U6-U8 | 16240 | 9 (54) | 6960 |
| 10 | Integración cliente-API y estado remoto | Consumir APIs con resiliencia y UX correcta | fetch/errores, estados loading/error, cache/sync conceptual, retries | U4,U6-U9 | 16240 | 9 (54) | 6960 |
| 11 | Node.js, Express y arquitectura de API | Estructurar servicios mantenibles | middlewares, routing, capas, config/env, manejo async | U3-U5 | 16240 | 9 (54) | 6960 |
| 12 | Validación, errores y contratos (Zod) | Proteger bordes y responder de forma consistente | schemas, parse/safeParse, error handling central, respuestas tipadas | U2,U4,U11 | 16240 | 9 (54) | 6960 |
| 13 | PostgreSQL y modelado relacional | Diseñar datos íntegros y consultables | tablas, PK/FK, constraints, índices, normalización básica | U4 | 16240 | 9 (54) | 6960 |
| 14 | SQL práctico y Prisma ORM | Consultar y mutar datos con seguridad y eficiencia | SELECT/JOIN/WHERE, agregaciones, transacciones, Prisma schema/queries | U13 | 16240 | 9 (54) | 6960 |
| 15 | Arquitectura, modularidad y multi-tenancy | Escalar diseño y aislar tenants | capas/hexagonal (conceptual), boundaries, tenant isolation, configuración | U11-U14 | 16240 | 9 (54) | 6960 |
| 16 | Autenticación y sesiones (JWT, refresh, 2FA) | Implementar identidad y sesión segura | JWT access/refresh, rotación, cookies vs storage, TOTP/2FA | U5,U12 | 16240 | 9 (54) | 6960 |
| 17 | Autorización, RBAC y hardening de API | Controlar permisos y reducir superficie de ataque | RBAC, ownership, Helmet, rate limiting, CORS, HMAC, secretos | U16,U13 | 16240 | 9 (54) | 6960 |
| 18 | Testing: unitario e integración | Verificar comportamiento y prevenir regresiones | Vitest/Jest, Supertest, mocks, AAA, determinismo | U6-U17 (selectivo) | 16240 | 9 (54) | 6960 |
| 19 | Cobertura, calidad y automatización en CI | Convertir pruebas en señal confiable de entrega | cobertura, thresholds, pipelines, lint/typecheck, gates | U18,U5 | 16240 | 9 (54) | 6960 |
| 20 | Docker, CI/CD, despliegue y observabilidad | Empaquetar y operar servicios de forma repetible | Dockerfile/Compose, imágenes, env/secrets, GitHub Actions, logs/métricas/health | U11,U19 | 16240 | 9 (54) | 6960 |
| **Total** | | | | | **324.800** | **180 (1080)** | **139.200** |

## Esqueleto por unidad (obligatorio, 9 ejercicios)
Cada unidad: título + **micro-contexto (3–5 líneas)** + 9 ejercicios + bloque de soluciones.
1. **Completar (6 ítems)** — huecos `________` + pistas `(concepto/pista)`; ejemplo modelo en ítem 1 cuando inicie tema nuevo.
2. **Completar/código corto (6 ítems)** — rellenar API, firma, opción de config o fragmento.
3. **Corregir errores (6 ítems)** — incluye ≥1 ítem **"Correcto"**; bugs plausibles del tema.
4. **Elegir opción c/distractores (6 ítems)** — 2–3 opciones inline `(a / b / c)`, distractores verosímiles.
5. **Elegir/decisión de diseño (6 ítems)** — trade-offs y elección contextual.
6. **Transformar (6 ítems)** — refactor/reescritura (p. ej. JS→TS, callback→async, query insegura→segura, config débil→robusta).
7. **Reordenar/relacionar (6 ítems)** — pasos, flujo, emparejamiento concepto→uso.
8. **Escenario/diálogo (6 ítems)** — caso realista (code review, incidente, diseño) con huecos/respuestas breves.
9. **Producción guiada (6 ítems o 3 amplios)** — escribir handler, esquema, test, query, Dockerfile/CI fragment o plan; soluciones modelo.

**Reglas de andamiaje:** ejemplo resuelto en E1/E3 inicial; dificultad ascendente intra-unidad; huecos de longitud variable; pistas entre paréntesis; escenarios distintos por unidad (ver ledger).
