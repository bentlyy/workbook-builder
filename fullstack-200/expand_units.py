# -*- coding: utf-8 -*-
import os, html, re

BASE=r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS=os.path.join(BASE,"units")

def e(s): return html.escape(str(s), quote=False)
def c(s): return f"<code>{e(s)}</code>"
def b(cls="md"): return f'<span class="blank {cls}"></span>'
def ln(): return '<span class="line"></span>'

def ex_block(n,title,inst,items=None,pre=None,example=None,lines=0):
    out=[f'<div class="exercise">',f'<h3>Ejercicio {n}. {e(title)}</h3>',f'<p class="inst">{inst}</p>']
    if example: out.append(f'<div class="example"><strong>Ejemplo:</strong> {example}</div>')
    if pre: out.append(f'<pre>{e(pre)}</pre>')
    if items:
        out.append("<ol class='items'>")
        for it in items: out.append(f"<li>{it}</li>")
        out.append("</ol>")
    for _ in range(lines): out.append('<span class="line"></span>')
    out.append('</div>')
    return "\n".join(out)

def ans_p(n,ans):
    return f'<p><strong>Ej. {n}:</strong> {e(ans)}</p>'

EXP = {}

EXP[1] = {"extras":[
 (10,"Completar avanzado: patrones modernos y runtime",
  "Completa con el concepto o API correcta. Piensa en comportamiento real en Node 20+ y navegadores modernos.",
  [f"{c('structuredClone(obj)')} crea una copia {b('md')} de estructuras soportadas, a diferencia del spread superficial.",
   f"Para ejecutar scripts definidos en {c('package.json')} uso {c('npm run ')}{b('md')}.",
   f"El operador nullish coalescing {c('??')} solo aplica cuando el valor es {b('sm')} o {b('sm')}, no para {c('0')} o {c(chr(34)+chr(34))}.",
   f"Un {c('Map')} preserva el orden de inserción y permite claves de cualquier {b('md')}, a diferencia de objetos planos.",
   f"Para trabajar con rutas de archivos de forma portable en Node uso el módulo {b('md')} ({c('path')}).",
   f"{c('Promise.resolve(x)')} envuelve un valor en una promesa {b('md')} con ese valor."],
  "1) profunda 2) nombre-script 3) null / undefined 4) tipo 5) path 6) resuelta"),
 (11,"Corregir avanzado (marca \"Correcto\" si aplica)",
  "Analiza cada fragmento o afirmación en contexto de un servicio Node ESM.",
  [f"{c('if (port == 0) port = 3000')} para validar puerto configurable. → {ln()}",
   f"{c('import cfg from \"./data.json\"')} con import attributes según soporte/configuración. → {ln()}",
   f"Usar {c('Number.isNaN(x)')} es más preciso que {c('isNaN(x)')} para detectar NaN real. → {ln()}",
   f"{c('Object.freeze')} hace inmutable en profundidad cualquier objeto anidado. → {ln()}",
   f"Definir {c('\"engines\": {\"node\": \">=20\"}')} ayuda a alinear entornos. → {ln()}",
   f"Capturar y registrar errores en el nivel superior de un CLI evita fallos silenciosos. → {ln()}"],
  "a) Error: 0 es válido; usar ?? o chequeo explícito b) Correcto (según config) c) Correcto d) Error: solo superficial e) Correcto f) Correcto"),
 (12,"Elegir avanzado: decisiones en módulos y utilidades",
  "Selecciona la opción más robusta.",
  [f"Convertir lista a conjunto único: ({c('new Set(arr)')} / {c('arr.map')} / {c('arr.join')}).",
   f"Combinar config por defecto y env: ({c('merge controlado y validado')} / {c('reemplazar sin validar')} / {c('ignorar env')}).",
   f"Leer JSON de entrada externa: ({c('validar esquema tras parsear')} / {c('asumir forma')} / {c('eval')}).",
   f"Exportar constantes compartidas: ({c('export const nombrado')} / {c('globales implícitas')} / {c('mutar exports')}).",
   f"Detectar entorno: ({c('process.env.NODE_ENV')} / {c('hardcode')} / {c('variable mágica')}).",
   f"Logs estructurados: ({c('JSON con campos')} / {c('string sin formato')} / {c('solo emoji')})."],
  "1) new Set 2) merge controlado 3) validar esquema 4) export const 5) process.env.NODE_ENV 6) JSON estructurado"),
 (13,"Transformar avanzado: refactor a utilidades claras",
  "Aplica la transformación pedida.",
  [f"Evita mutación: {c('user.role = \"admin\"; return user;')} → {ln()}",
   f"Optional chaining/nullish: {c('const city = user && user.address && user.address.city ? user.address.city : \"N/A\";')} → {ln()}",
   f"De CJS a ESM: {c('const fs = require(\"fs\"); module.exports = {read};')} → {ln()}{ln()}",
   f"Agrupa imports: {c('import {a} from \"./x.js\"; import {b} from \"./x.js\";')} → {ln()}",
   f"Acumular con reduce (sumar totales): {ln()}",
   f"Firma segura para {c('average(nums)')} con validación: {ln()}"],
  "1) return {...user, role:'admin'} 2) user?.address?.city ?? 'N/A' 3) import fs from 'fs'; export {read} 4) import {a,b} from './x.js' 5) nums.reduce((s,n)=>s+n,0) 6) validar arreglo no vacío y números finitos"),
 (14,"Escenario extendido: pipeline de importación de catálogo (Node ESM)",
  "Responde con decisiones técnicas detalladas.",
  [f"Diseño de módulos: propone 3 archivos y responsabilidad de cada uno. {ln()}{ln()}",
   f"Define objeto resumen {c('{processed, valid, invalid, errors[]}')} con un ejemplo. {ln()}{ln()}",
   f"Regla robusta para precio '0', vacío y no numérico (usa ??/validación). {ln()}{ln()}",
   f"Muestra cómo acumular válidos sin mutar el array original. {ln()}",
   f"Lista 3 variables de entorno necesarias y su propósito. {ln()}{ln()}",
   f"¿Qué harías si el archivo de entrada no existe o es ilegible? (comportamiento y exit code). {ln()}{ln()}"],
  f"Escenario: script ESM importa CSV→JSON para e-commerce (50k filas), normaliza campos y reporta errores por fila. Falló antes por mezcla CJS/ESM, comparación laxa y mutaciones. Debe correr en CI y Linux con Node 20 y producir salida determinista. Requiere trazabilidad por fila y manejo seguro de valores como 0.",
  "1) p.ej. parseCsv.js, validateItem.js, index.js 2) ejemplo con conteos y errors[{row,reason}] 3) 0 válido; vacío->default o inválido según regla; no numérico->invalidar 4) [...acc,item] o copia 5) INPUT_PATH,OUTPUT_PATH,NODE_ENV 6) log claro y process.exit(1)"),
 (15,"Producción extendida: mini-módulo de utilidades",
  "Desarrolla soluciones concretas.",
  [f"Implementa {c('toNonNegativeInt(value, fallback)')} (acepta number/string, rechaza NaN/negativos, usa fallback). {ln()}{ln()}{ln()}{ln()}",
   f"Snippet para leer {c('process.env.PORT')} con default 3000 sin romper '0'. {ln()}{ln()}",
   f"Define contrato (TS/JSDoc) para resultado de importación {c('{success,data,errors}')}. {ln()}{ln()}{ln()}",
   f"Escribe 5 casos de prueba manuales (entrada→salida esperada). {ln()}{ln()}{ln()}",
   f"Lista 4 buenas prácticas de módulos ESM en equipos. {ln()}{ln()}",
   f"Si index.js supera 300 líneas, ¿qué 3 extracciones harías? {ln()}{ln()}"],
  "1) convertir, validar entero >=0, sino fallback 2) const port = process.env.PORT ?? '3000' 3) discriminated result o campos tipados 4) '10',0,-1,'abc',null 5) extensiones, exports claros, sin side-effects, env validado 6) parseo, validación, reporte/io")
]}

def generic(u,title,topics,scenario_domain,scenario_detail,prod):
    return [
 (10,f"Completar avanzado: {title}",
  "Completa con el término, API o práctica correcta (profundización).",
  [f"Un concepto clave para robustez en {e(title)} es {b('lg')}, porque reduce fallos en producción.",
   f"Antes de desplegar cambios relacionados se debe {b('lg')} (verificación recomendada).",
   f"Usar {c(topics[0])} correctamente permite {b('lg')} cuando el contexto lo requiere.",
   f"Una mala práctica frecuente es {c(topics[1])}; en su lugar conviene {b('lg')}.",
   f"Para casos límite como {e(topics[2])} la estrategia adecuada es {b('lg')}.",
   f"Una señal de implementación madura incluye {b('lg')} (observabilidad, pruebas o métricas)."],
  f"1) concepto central del tema 2) probar/validar 3) aplicar {topics[0]} 4) alternativa segura a {topics[1]} 5) manejo explícito de {topics[2]} 6) evidencia: tests/logs/métricas"),
 (11,"Corregir avanzado (marca \"Correcto\" si aplica)",
  "Analiza decisiones típicas e identifica errores sutiles.",
  [f"Omitir validación o controles en el borde del sistema. → {ln()}",
   f"Registrar contexto suficiente (sin secretos) para diagnosticar fallos. → {ln()}",
   f"Aplicar una solución sin considerar impacto en seguridad o datos. → {ln()}",
   f"Automatizar pruebas y checks relevantes para el cambio. → {ln()}",
   f"Usar configuraciones iguales en todos los entornos sin control. → {ln()}",
   f"Documentar contratos, supuestos y pasos de operación. → {ln()}"],
  "a) Error b) Correcto c) Error d) Correcto e) Error/riesgo f) Correcto"),
 (12,"Elegir avanzado: decisiones y trade-offs",
  "Selecciona la opción más adecuada.",
  [f"Requisito ambiguo: ({c('definir contrato y validar')} / {c('asumir')} / {c('implementar sin acordar')}).",
   f"Fallo transitorio de dependencia: ({c('retry con backoff y límite')} / {c('reintento infinito')} / {c('ignorar error')}).",
   f"Cambio incompatible: ({c('versionar/migrar')} / {c('romper silenciosamente')} / {c('no avisar')}).",
   f"Acceso a datos sensibles: ({c('mínimo privilegio y controles')} / {c('acceso amplio')} / {c('exponer en logs')}).",
   f"Degradación de rendimiento: ({c('medir y optimizar cuello')} / {c('optimizar a ciegas')} / {c('ignorar')}).",
   f"Entregas frecuentes: ({c('CI con gates')} / {c('deploy manual sin pruebas')} / {c('saltar revisión')})."],
  "1) definir contrato 2) retry con backoff 3) versionar/migrar 4) mínimo privilegio 5) medir y optimizar 6) CI con gates"),
 (13,"Transformar avanzado: de frágil a robusto",
  "Transforma a una alternativa más segura y mantenible.",
  [f"Implementación sin validación → añade validación/guards explícitos. {ln()}{ln()}",
   f"Valor/config hardcodeado → uso de configuración por entorno. {ln()}",
   f"Flujo sin manejo de errores → manejo consistente y respuesta adecuada. {ln()}{ln()}",
   f"Operación sin trazabilidad → logging/métricas con contexto. {ln()}",
   f"Componente acoplado → separación de responsabilidades (indica extracción). {ln()}{ln()}",
   f"Caso límite {e(topics[2])} no cubierto → tratamiento correcto. {ln()}"],
  "1) validar inputs/estados 2) variables de entorno/config 3) try/catch y errores tipados/consistentes 4) observabilidad 5) extraer módulo/capa 6) manejar límite explícitamente"),
 (14,f"Escenario extendido: {scenario_domain}",
  "Responde con decisiones técnicas, mitigaciones y verificación.",
  [f"Objetivo y alcance del cambio (qué incluye/excluye). {ln()}{ln()}",
   f"Riesgos principales (seguridad, datos, disponibilidad) y mitigación. {ln()}{ln()}{ln()}",
   f"Decisiones de diseño/contrato y por qué. {ln()}{ln()}",
   f"Estrategia de pruebas (unitarias, integración, casos borde). {ln()}{ln()}{ln()}",
   f"Métricas/logs/alertas para operar y detectar fallos. {ln()}{ln()}",
   f"Plan de despliegue y rollback. {ln()}{ln()}"],
  f"Escenario: {scenario_detail} Debes proponer una solución alineada a buenas prácticas de {e(title)} considerando mantenibilidad, seguridad y operación en producción.",
  "1) alcance claro 2) riesgos con mitigaciones 3) diseño y contratos coherentes 4) pruebas multinivel y bordes 5) observabilidad accionable 6) rollout gradual y rollback"),
 (15,"Producción extendida: entrega práctica",
  "Desarrolla una solución concreta y verificable.",
  [f"{prod} {ln()}{ln()}{ln()}{ln()}{ln()}",
   f"Define 4 casos de verificación (feliz, error, borde, seguridad/regresión). {ln()}{ln()}{ln()}",
   f"Criterios de aceptación medibles (3). {ln()}{ln()}",
   f"Riesgos residuales y mitigación. {ln()}{ln()}",
   f"Notas de documentación/operación necesarias. {ln()}{ln()}",
   f"Dos mejoras incrementales futuras. {ln()}{ln()}"],
  "1) implementación/esquema correcto y claro 2) casos cubren éxito, fallo, límite y seguridad 3) criterios medibles 4) riesgos y mitigaciones 5) docs/operación 6) mejoras incrementales")
    ]

specs = {
2:("TypeScript y contratos",["unknown","any","null/undefined"],"catálogo de productos tipado compartido","Frontend y backend comparten modelos de producto/precio; hubo fallos por aserciones inseguras y opcionales mal manejados.","Define tipos/interfaces y type guard para Product (id,name,price:number,currency,stock?:number) más un ApiResult<Product>."),
3:("asincronía resiliente",["Promise.allSettled","await sin catch","timeout/abort"],"orquestación de pago y notificación","Cobros y notificaciones fallan intermitentemente; se requieren reintentos controlados, timeouts y resultados consistentes.","Implementa async processCheckout(input) con timeout, manejo de error y retorno {ok,data|error} (pseudocódigo TS)."),
4:("contratos REST",["idempotency key","GET /doAction","paginación cursor"],"API pública de catálogo para partners","Partners exigen contratos estables, paginación, rate limits y errores consistentes con versionado.","Diseña contrato de GET /v1/products y POST /v1/orders (params, body, respuestas, códigos y errores)."),
5:("colaboración con Git",["conventional commits","force push a main","conflictos de merge"],"hotfix urgente en release","Bug crítico en producción mientras avanzan features; se requiere trazabilidad, revisión y sincronización de ramas.","Redacta plan de hotfix: rama, commits, PR, pruebas, merge/cherry-pick y checklist post-deploy."),
6:("componentes React",["key estable","índice como key","estado derivado"],"tabla editable de pacientes","Reordenar y editar filas causa renders incorrectos y pérdida de foco por keys/estado mal modelado.","Diseña componentes y estado para tabla con búsqueda, edición inline y paginación (estructura y handlers)."),
7:("hooks y rendimiento",["useEffect cleanup","dependencias omitidas","suscripción WebSocket"],"dashboard de alertas IoT en tiempo real","Cambios rápidos de dispositivo generan fugas, datos obsoletos y renders excesivos.","Implementa useDeviceAlerts(deviceId) con suscripción, cleanup, abort/guard y API de retorno."),
8:("Next.js App Router",["Server Components","'use client' global","revalidación de datos"],"portal admin con datos sensibles","Se necesita proteger secretos, optimizar carga y mantener interactividad en filtros y formularios.","Propón árbol app/ para /admin/inventory y define server/client, fetch y estados loading/error."),
9:("UI accesible con Tailwind",["label htmlFor","placeholder como única etiqueta","aria-describedby"],"formulario de admisión de técnicos","Usuarios reportan errores confusos, envíos duplicados y problemas de navegación por teclado.","Crea formulario accesible (campos, labels, errores, loading) con markup y comportamiento."),
10:("integración cliente-API",["AbortController","ignorar res.ok","reintento en 400"],"buscador con filtros y red inestable","Respuestas fuera de orden y fallos intermitentes degradan la experiencia en sucursales.","Implementa capa fetchJson y hook de búsqueda con cancelación, estados y manejo de errores."),
11:("arquitectura Express",["middleware de errores","lógica en rutas","inyección de dependencias"],"API modular de inventario","Crecimiento de endpoints genera duplicación y dificultad para testear.","Define estructura de módulos (parts) y esqueleto controller/service/repository con manejo de errores."),
12:("validación con Zod",["safeParse","z.any()","error 422 consistente"],"alta de usuarios y órdenes B2B","Payloads mal formados y errores inconsistentes rompen integraciones.","Crea esquemas Zod (CreateUser, CreateOrder) y formateador estándar de errores."),
13:("modelado PostgreSQL",["UNIQUE(tenant_id,email)","float para dinero","índice (tenant_id,created_at)"],"SaaS de agenda multi-taller","Se requiere aislamiento por tenant, integridad de citas y consultas eficientes por fecha.","Diseña DDL simplificado para tenants, customers, professionals, appointments con constraints e índices."),
14:("SQL y Prisma",["$transaction","SELECT *","paginación cursor"],"confirmación de orden y stock","Concurrencia provoca stock negativo y reportes lentos.","Escribe flujo Prisma transaccional para confirmar orden y consulta paginada de órdenes por tenant."),
15:("arquitectura multi-tenant",["tenant desde auth","tenant desde body","boundary de módulo"],"plataforma SaaS multi-clínica","Riesgo de fuga de datos entre tenants y reglas duplicadas en módulos.","Define TenantContext, repositorio con filtro obligatorio y reglas de autorización cruzada."),
16:("autenticación JWT/2FA",["rotación de refresh","access token largo","verificación TOTP"],"panel administrativo sensible","Intentos de fuerza bruta y robo de tokens exigen sesiones seguras y 2FA.","Diseña flujo login/refresh/logout con rotación, detección de reuse y 2FA TOTP."),
17:("RBAC y hardening",["requireRole y ownership","CORS * con credenciales","verificación HMAC"],"API admin y webhooks","Acciones críticas y webhooks requieren permisos, aislamiento y verificación de integridad.","Implementa guardas de autorización y verificación de webhook firmado con idempotencia."),
18:("testing confiable",["patrón AAA","tests flaky","mocks de dependencias"],"módulo auth y órdenes","Regresiones en login/refresh y creación de órdenes por falta de casos de error.","Diseña casos unitarios e integración (Supertest) para auth y POST /orders con errores."),
19:("calidad y CI",["required checks","100% cobertura sin valor","tests por módulo crítico"],"monorepo con API y frontend","Pipelines lentos y cobertura engañosa permiten fallos en pagos.","Propón workflow CI con etapas, cache, reportes y umbrales focalizados en módulos críticos."),
20:("Docker y operación",["healthcheck","secretos en imagen","estrategia de rollback"],"despliegue API Node + PostgreSQL","Se necesitan releases reproducibles, observabilidad y recuperación ante fallos.","Crea Dockerfile, docker-compose y plan de despliegue/monitoreo/rollback.")
}

for u in range(2,21):
    EXP[u]={"extras": generic(u,*specs[u])}

def append_to_unit(uid, extras):
    hp=os.path.join(UNITS,f'u{uid:02d}.html')
    ap=os.path.join(UNITS,f'u{uid:02d}_ans.html')
    h=open(hp,encoding='utf-8').read()
    a=open(ap,encoding='utf-8').read()
    blocks=[]; ansps=[]
    for ex in extras:
        n,title,inst,items,ans = ex[0],ex[1],ex[2],ex[3],ex[4]
        blocks.append(ex_block(n,title,inst,items))
        ansps.append(ans_p(n,ans))
    h=h.replace('</section>', "\n".join(blocks)+"\n</section>")
    a=a + "\n" + "\n".join(ansps)
    open(hp,'w',encoding='utf-8').write(h)
    open(ap,'w',encoding='utf-8').write(a)

if __name__=='__main__':
    for uid in range(1,21):
        append_to_unit(uid, EXP[uid]['extras'])
        print('expanded',uid)
    print('done')
