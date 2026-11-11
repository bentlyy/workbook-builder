# Ledger (actualizado - Fase 2/3)

## Cobertura de conceptos
| Unidad | Foco | Profundidad |
|---|---|---|
| U1 | JS/ESM Node | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U2 | TS tipos/narrowing | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U3 | Async/promesas | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U4 | HTTP/REST | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U5 | Git/PR | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U6 | React base | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U7 | Hooks/rendimiento | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U8 | Next App Router | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U9 | UI/Tailwind/a11y | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U10 | Integración API cliente | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U11 | Express/arquitectura | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U12 | Zod/errores | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U13 | PostgreSQL/modelado | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U14 | SQL/Prisma | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U15 | Arquitectura/multi-tenant | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U16 | Auth JWT/2FA | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U17 | RBAC/hardening | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U18 | Testing | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U19 | CI/calidad | intro → práctica → avanzado → integrador (RCA/diseño/producción) |
| U20 | Docker/observabilidad | intro → práctica → avanzado → integrador (RCA/diseño/producción) |

## Escenarios y dominios usados (únicos por unidad)
| Unidad | Escenario/dominio | Entidades/identificadores clave |
|---|---|---|
| U1 | CLI migración de datos JSON→reporte (Node ESM) | parseInput/validateRecord/report, registros inválidos |
| U2 | SDK interno tipado de productos | Product, ApiResult, fetchEntity<T>, type guards |
| U3 | Orquestador de pagos/notificaciones | orderId, jobs, Promise.allSettled, AbortController |
| U4 | API pública de reservas/catálogo | tenants, bookings, idempotency key, 409/422 |
| U5 | Flujo release/hotfix en facturación | release/main, hotfix, cherry-pick, CI gates |
| U6 | Dashboard/tabla editable de citas o pacientes | keys estables, lifting state, filtros/edición |
| U7 | Monitor/stream de alertas IoT | deviceId, WebSocket/polling, cleanup, useCallback |
| U8 | Portal admin inventario (Next App Router) | inventory/[id], Server/Client, loading/error |
| U9 | Formularios de admisión/registro accesible | label/htmlFor, aria, focus, validación |
| U10 | Buscador con filtros y red inestable | AbortController, debounce, res.ok, estados |
| U11 | API modular de inventario (Express) | parts, routers/controllers/services/repos |
| U12 | Ingesta/alta B2B con validación Zod | users/orders/webhooks, safeParse, error estándar |
| U13 | SaaS agenda clínica multi-tenant (PostgreSQL) | tenants, appointments, UNIQUE/índices |
| U14 | Reportes y ajuste de stock (SQL/Prisma) | ventas, $transaction, paginación, concurrencia |
| U15 | Plataforma SaaS multi-clínica (arquitectura) | TenantContext, repos base, boundaries |
| U16 | Panel admin con JWT/refresh/2FA | rotación, reuse, revocación, TOTP |
| U17 | API admin y webhooks firmados (RBAC/hardening) | requireRole, ownership, HMAC, rate limit |
| U18 | Suite de regresión auth/órdenes (Vitest/Supertest) | AAA, mocks, fixtures, casos de error |
| U19 | CI monorepo API+frontend (calidad) | required checks, cache, umbrales, flaky |
| U20 | Despliegue API Node+PostgreSQL (Docker/ops) | healthcheck, rollback, métricas 5xx, secrets |

## Mix de tipos y volumen (acumulado)
- 19 ejercicios/ud × 20 ud = 380 ejercicios: completar, corregir (con ítems "Correcto"), elegir con distractores, transformar, reordenar/relacionar, escenario/diálogo, producción guiada, profundización, caso integrador, RCA, diseño técnico y producción con verificación.
- Ítems (li) totales: 2280. Huecos/pistas y ejemplos de andamiaje presentes en todas las unidades.

## Repeticiones (QA)
- Contextos/escenarios de unidad: sin duplicados. Se evitó reutilización de dominios y datos entre unidades.
- Formato pedagógico repetido mínimo en etiquetas de ejemplo "Modelo:" (contenido distinto por unidad/ejercicio).

## Estado QA final
- 461.588 chars (~199.0 págs @2320cpp), 20 unidades, 380 ejercicios, 2280 ítems, solucionario 21.1% (claves + guía/rúbrica por unidad), densidad 21.3k–26.2k chars/ud, duplicados de contexto 0.