import os, html

BASE=r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS=os.path.join(BASE,"units")

def e(s): return html.escape(str(s), quote=False)
def c(s): return f"<code>{e(s)}</code>"
def ln(): return '<span class="line"></span>'

def ex_block(n,title,inst,items=None,example=None):
    out=[f'<div class="exercise">',f'<h3>Ejercicio {n}. {e(title)}</h3>',f'<p class="inst">{inst}</p>']
    if example: out.append(f'<div class="example"><strong>Ejemplo:</strong> {example}</div>')
    if items:
        out.append("<ol class='items'>")
        for it in items: out.append(f"<li>{it}</li>")
        out.append("</ol>")
    out.append('</div>')
    return "\n".join(out)

def ans_p(n,ans): return f'<p><strong>Ej. {n}:</strong> {e(ans)}</p>'

specs = {
1:("JS/ESM y tooling Node 20+", "CLI de migración de datos", "Script ESM que lee JSON, valida registros y genera reporte; falla por imports, coerciones y mutaciones.", "Escribe módulo parseInput.js + validateRecord.js + report.js con manejo de errores y salida determinista."),
2:("tipado TypeScript", "SDK interno tipado", "Librería compartida expone funciones con tipos inseguros y uso de any en bordes.", "Define tipos públicos, guards y ApiResult para una función fetchEntity<T>."),
3:("asincronía y concurrencia", "orquestador de tareas", "Jobs paralelos con dependencias parciales, timeouts y reintentos.", "Implementa runJobs(jobs) con límite de concurrencia, timeout y resumen de resultados."),
4:("diseño REST", "API de reservas", "Clientes sufren errores 409/422 inconsistentes y falta de idempotencia en POST.", "Especifica endpoints, códigos, esquema de error y estrategia de idempotencia."),
5:("Git y colaboración", "flujo de release", "Múltiples hotfix/features causan conflictos y regresiones por PRs grandes.", "Define estrategia de ramas, convención de commits, plantilla PR y checklist CI."),
6:("React componentes/estado", "dashboard de citas", "Estados duplicados y keys inestables rompen filtros y edición.", "Diseña árbol de componentes, estado mínimo y flujo de eventos para la pantalla."),
7:("hooks y rendimiento", "stream de eventos", "Suscripciones y timers sin cleanup degradan la app.", "Implementa useEventStream(source, filters) con cleanup, abort y memoización."),
8:("Next.js App Router", "panel admin seguro", "Fugas de secretos y exceso de JS cliente por mal uso de componentes.", "Propón segmentación server/client, loading/error y estrategia de datos/cache."),
9:("accesibilidad y formularios", "onboarding multi-paso", "Errores poco claros y navegación por teclado deficiente.", "Diseña formulario accesible con validación, focus management y feedback."),
10:("integración cliente-API", "sincronización offline-parcial", "Reintentos y respuestas fuera de orden generan inconsistencias en UI.", "Implementa cliente API con abort, retry selectivo y cache/invalidation."),
11:("arquitectura Express", "servicio de catálogo", "Código monolítico dificulta pruebas y evolución.", "Estructura módulo catalog con rutas, controller, service, repo y errores."),
12:("validación y errores Zod", "ingesta de webhooks", "Payloads variables y errores no estandarizados.", "Crea esquemas, validador y mapeo de errores a respuestas consistentes."),
13:("modelado PostgreSQL", "facturación multi-tenant", "Necesidad de integridad, auditoría y consultas por periodo/tenant.", "Diseña tablas facturas, items, pagos con constraints e índices."),
14:("SQL/Prisma", "reporte y ajuste de inventario", "Consultas lentas y condiciones de carrera en stock.", "Escribe consultas/operaciones Prisma con transacción y paginación eficiente."),
15:("arquitectura multi-tenant", "aislamiento de datos", "Repos compartidos filtran mal tenant_id en algunos flujos.", "Define TenantGuard, repositorio base y pruebas de aislamiento."),
16:("auth JWT/2FA", "gestión de sesiones", "Robo de refresh tokens y sesiones huérfanas.", "Diseña rotación, revocación, detección de reuse y flujo 2FA."),
17:("RBAC y hardening", "endpoints administrativos", "Escalada de privilegios y webhooks sin verificar.", "Implementa políticas RBAC, ownership checks y verificación HMAC."),
18:("testing", "suite de regresión", "Bugs recurrentes en bordes y errores de integración.", "Planifica y ejemplifica tests unitarios/integración con fixtures y mocks."),
19:("CI y calidad", "pipeline confiable", "Builds lentos, flaky tests y cobertura poco útil.", "Define pipeline con gates, paralelismo, cache y métricas de calidad."),
20:("Docker y operación", "despliegue reproducible", "Diferencias entre entornos y caídas sin detección temprana.", "Crea Dockerfile/compose, healthchecks, observabilidad y plan de rollback."),
}

def build(u,topic,case,scenario,prod):
    ex16=(16,"Caso práctico integrador",
      "Resuelve el caso aplicando conceptos de la unidad y unidades previas cuando corresponda.",
      [f"Contexto: identifica actores, entradas, salidas y restricciones. {ln()}{ln()}{ln()}",
       f"Problemas detectados (mínimo 3) y causa probable. {ln()}{ln()}{ln()}",
       f"Decisiones de diseño/implementación y justificación. {ln()}{ln()}{ln()}",
       f"Plan de implementación por pasos (ordenado). {ln()}{ln()}{ln()}",
       f"Validación: cómo comprobarías que el caso quedó resuelto. {ln()}{ln()}"],
      f"Caso: {scenario}",
      f"Solución modelo: delimitar alcance, listar 3+ problemas con causa, proponer diseño alineado a {topic}, ejecutar pasos incrementales y validar con pruebas/observación; considerar seguridad, errores y mantenibilidad.")
    ex17=(17,"Depuración y análisis de causa raíz",
      "Analiza el incidente y propone diagnóstico y corrección.",
      [f"Síntoma observado y evidencia a recoger (logs, métricas, trazas, inputs). {ln()}{ln()}{ln()}",
       f"Hipótesis de causa raíz (al menos 2) y cómo descartarlas. {ln()}{ln()}{ln()}",
       f"Corrección inmediata (mitigación) y corrección definitiva. {ln()}{ln()}{ln()}",
       f"Riesgo de regresión y pruebas a añadir. {ln()}{ln()}",
       f"Acción preventiva para evitar recurrencia. {ln()}{ln()}"],
      f"Incidente: durante {case} se observan fallos intermitentes bajo carga y datos inconsistentes en algunos casos límite.",
      "Modelo: recolectar evidencia, formular hipótesis, aislar con reproducción, mitigar (rollback/flag/limit), corregir causa raíz, agregar tests y monitoreo/alertas.")
    ex18=(18,"Diseño y documentación técnica",
      "Produce artefactos técnicos claros para el equipo.",
      [f"Define contrato/interfaz (entradas, salidas, errores) relacionado con la solución. {ln()}{ln()}{ln()}{ln()}",
       f"Diagrama o descripción estructurada de componentes/flujo (texto). {ln()}{ln()}{ln()}",
       f"Consideraciones de seguridad, rendimiento y compatibilidad. {ln()}{ln()}{ln()}",
       f"Criterios de aceptación y definición de terminado (DoD). {ln()}{ln()}",
       f"Notas de operación/despliegue y rollback. {ln()}{ln()}"],
      f"Documenta la solución propuesta para {case} de forma que otro desarrollador pueda implementarla y operarla.",
      "Modelo: contrato explícito, flujo por componentes, requisitos no funcionales, criterios medibles y runbook breve.")
    ex19=(19,"Producción avanzada y verificación",
      "Entrega una implementación/plan detallado y su verificación.",
      [f"{prod} {ln()}{ln()}{ln()}{ln()}{ln()}{ln()}",
       f"Casos de verificación: feliz, error, borde, seguridad y regresión. {ln()}{ln()}{ln()}{ln()}",
       f"Datos/fixtures de ejemplo y resultado esperado. {ln()}{ln()}{ln()}",
       f"Observabilidad: logs/métricas/alertas relevantes. {ln()}{ln()}",
       f"Riesgos, mitigaciones y próximos pasos. {ln()}{ln()}"],
      "Incluye detalles suficientes (nombres, estados, códigos, estructuras) para que la solución sea ejecutable y evaluable.",
      "Modelo: implementación coherente, 5 verificaciones, fixtures claros, señales operativas y mejora incremental.")
    return [ex16,ex17,ex18,ex19]

def append(u, extras):
    hp=os.path.join(UNITS,f'u{u:02d}.html'); ap=os.path.join(UNITS,f'u{u:02d}_ans.html')
    h=open(hp,encoding='utf-8').read(); a=open(ap,encoding='utf-8').read()
    blocks=[]; ans=[]
    for ex in extras:
        blocks.append(ex_block(ex[0],ex[1],ex[2],ex[3],example=ex[5]))
        ans.append(ans_p(ex[0],ex[5]))
    notes = f"\n<p><strong>Notas ampliadas U{u}:</strong> criterios de evaluación — corrección técnica, manejo de errores/bordes, seguridad, claridad de contratos, pruebas y observabilidad. Acepta variantes equivalentes bien justificadas.</p>\n"
    h=h.replace('</section>', "\n".join(blocks)+"\n</section>")
    a=a + "\n" + "\n".join(ans) + notes
    open(hp,'w',encoding='utf-8').write(h); open(ap,'w',encoding='utf-8').write(a)

if __name__ == '__main__':
    for u in range(1,21):
        append(u, build(u,*specs[u]))
        print('pass2',u)
    print('done')
