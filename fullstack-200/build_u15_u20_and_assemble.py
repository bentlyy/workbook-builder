# -*- coding: utf-8 -*-
import os, html, glob

BASE = r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS_DIR = os.path.join(BASE, "units")

def e(s): return html.escape(str(s), quote=False)
def c(s): return f"<code>{e(s)}</code>"
def b(cls="md"): return f'<span class="blank {cls}"></span>'
def ln(): return '<span class="line"></span>'

def render_unit_html(u):
    out=[f'<section class="unit" id="u{u["n"]}">',f'<h2>Unidad {u["n"]}. {e(u["title"])}</h2>',f'<p class="context">{e(u["context"])}</p>']
    for i,ex in enumerate(u["exercises"],1):
        out.append('<div class="exercise">')
        out.append(f'<h3>Ejercicio {i}. {e(ex["title"])}</h3>')
        out.append(f'<p class="inst">{e(ex["inst"])}</p>')
        if ex.get("example"): out.append(f'<div class="example"><strong>Ejemplo:</strong> {ex["example"]}</div>')
        if ex.get("pre"): out.append(f'<pre>{e(ex["pre"])}</pre>')
        if ex.get("items"):
            out.append("<ol class='items'>")
            for it in ex["items"]: out.append(f"<li>{it}</li>")
            out.append("</ol>")
        if ex.get("lines"):
            for _ in range(ex["lines"]): out.append('<span class="line"></span>')
        out.append('</div>')
    out.append('</section>')
    return "\n".join(out)

def render_ans(u):
    out=[f'<p class="u">Unidad {u["n"]}. {e(u["title"])}</p>']
    for i,ex in enumerate(u["exercises"],1):
        ans = ex.get("ans",[]); ans = " ".join(str(a) for a in ans) if isinstance(ans,list) else str(ans)
        out.append(f'<p><strong>Ej. {i}:</strong> {e(ans)}</p>')
    return "\n".join(out)

units = []

units.append({
"n":15,"title":"Arquitectura de servicios, modularidad y multi-tenancy",
"context":"A medida que un producto crece, la arquitectura define cuánto cuesta cambiar, escalar y operar el sistema. Separar responsabilidades, establecer límites entre módulos y diseñar correctamente el aislamiento multi-tenant evita acoplamiento y fugas de datos. Esta unidad practica capas, modularidad, boundaries, estrategias de multi-tenancy y decisiones de diseño orientadas a mantenibilidad y escalabilidad en SaaS.",
"exercises":[
 {"title":"Completar: capas y modularidad","inst":"Completa con el concepto correcto.","example":"Ejemplo: Separar dominio de infraestructura facilita probar reglas de negocio sin depender de la base de datos.",
  "items":[f"Una arquitectura en capas típica separa presentación/API, aplicación/servicios y acceso a {b('md')}.",f"El principio de responsabilidad única (SRP) indica que un módulo debe tener una razón clara para {b('md')}.",f"Un boundary bien definido expone una interfaz y oculta {b('md')} internos.",f"El acoplamiento alto dificulta el {b('md')} y aumenta el impacto de los cambios.",f"La inyección de dependencias permite sustituir implementaciones para {b('md')} y flexibilidad.",f"Un módulo cohesivo agrupa funcionalidades {b('md')} entre sí."],
  "ans":["1) datos/infraestructura 2) cambiar 3) detalles 4) mantenimiento 5) testing 6) relacionadas"]},
 {"title":"Completar: multi-tenancy y aislamiento","inst":"Completa los conceptos.",
  "items":[f"En multi-tenancy, un tenant representa un {b('md')} (cliente/organización) aislado lógicamente.",f"Una estrategia común es columna {c('tenant_id')} en tablas compartidas con filtros {b('md')}.",f"Otras estrategias incluyen esquema por tenant o base de datos por tenant, con distintos trade-offs de {b('lg')}.",f"El tenant activo debe derivarse del contexto de autenticación, no de input {b('md')} del cliente.",f"Pruebas de aislamiento deben verificar que un tenant no acceda a datos de {b('md')}.",f"Logs y métricas deben incluir {c('tenant_id')} para trazabilidad sin exponer datos {b('md')}."],
  "ans":["1) cliente 2) obligatorios 3) costo/complejidad/aislamiento 4) confiable 5) otro tenant 6) sensibles"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Permitir que el cliente envíe cualquier tenant_id y usarlo directamente en queries. → {ln()}",f"Aplicar filtros por tenant en repositorio/capa de datos de forma consistente. → {ln()}",f"Compartir caché entre tenants sin segmentar claves por tenant. → {ln()}",f"Definir interfaces entre módulos para reducir acoplamiento. → {ln()}",f"Duplicar reglas de negocio en controladores, jobs y scripts. → {ln()}",f"Documentar límites y contratos entre módulos. → {ln()}"],
  "ans":["a) Error grave b) Correcto c) Error/riesgo de fuga d) Correcto e) Mala práctica f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Aislamiento lógico simple en DB compartida: ({c('tenant_id en tablas')} / {c('sin tenant_id')}).",f"Regla de negocio usada en varios endpoints: ({c('servicio de dominio')} / {c('copiar en cada handler')}).",f"Dependencia de infraestructura: ({c('inyectar/abstraer')} / {c('instanciar globalmente en todo')}).",f"Cache multi-tenant: ({c('clave incluye tenant')} / {c('clave global')}).",f"Migraciones en modelo multi-tenant compartido: ({c('coordinadas/versionadas')} / {c('manuales por cliente sin control')}).",f"Límite de módulo: ({c('API/contrato claro')} / {c('acceso directo a internals')})."],
  "ans":["1) tenant_id 2) servicio de dominio 3) inyectar/abstraer 4) incluye tenant 5) versionadas 6) contrato claro"]},
 {"title":"Elegir/decisión de arquitectura","inst":"Selecciona la mejor decisión.",
  "items":[f"Nuevo requisito cruza varios módulos: ({c('definir contrato y owner')} / {c('parches ad-hoc')}).",f"Query sin filtro tenant en repo compartido: ({c('bloquear/corregir')} / {c('aceptar por rapidez')}).",f"Módulo con muchas responsabilidades: ({c('refactorizar por cohesión')} / {c('seguir creciendo')}).",f"Configuración por tenant: ({c('almacenar y resolver por contexto')} / {c('hardcodear')}).",f"Observabilidad: ({c('métricas por tenant agregadas con cuidado')} / {c('sin dimensiones')}).",f"Escalado: ({c('identificar cuellos de botella y límites')} / {c('adivinar')})."],
  "ans":["1) contrato y owner 2) bloquear/corregir 3) refactorizar 4) por contexto 5) con cuidado 6) identificar cuellos"]},
 {"title":"Transformar: mejorar diseño y aislamiento","inst":"Transforma según se indique.",
  "items":[f"Handler con SQL y reglas mezcladas → separación en capas (indica 3 capas): {ln()}",f"Query {c('SELECT * FROM orders WHERE id=$1')} en app multi-tenant → añade aislamiento: {ln()}",f"Clave de cache {c('orders:list')} → versión multi-tenant: {ln()}",f"Servicio que instancia {c('new PrismaClient()')} en cada método → mejora: {ln()}",f"Regla de precio duplicada en 3 lugares → refactor: {ln()}",f"DTO que expone campos de otro tenant → corrección: {ln()}"],
  "ans":["1) controller, service, repository 2) AND tenant_id=$2 (del contexto) 3) orders:list:{tenantId} 4) singleton/inyección 5) centralizar en servicio de dominio 6) filtrar/proyectar campos permitidos"]},
 {"title":"Reordenar/relacionar: diseño modular","inst":"Ordena o relaciona.",
  "items":[f"Diseño: (a) identificar dominios (b) definir boundaries (c) contratos (d) implementar y validar). → {ln()}",f"1)controller 2)service 3)repository con A)datos B)negocio C)HTTP. → {ln()}",f"1)tenant_id 2)schema por tenant 3)DB por tenant con A)aislamiento alto B)columna compartida C)aislamiento medio. → {ln()}",f"Mitigar fuga: (a) obtener tenant de auth (b) propagar contexto (c) filtrar en acceso datos (d) test de aislamiento). → {ln()}",f"1)cohesión 2)acoplamiento 3)contrato con A)interfaz estable B)relación interna C)dependencia entre módulos. → {ln()}",f"Refactor: (a) detectar duplicación (b) extraer servicio (c) actualizar consumidores (d) probar). → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-C,2-B,3-A 3) 1-B,2-C,3-A 4) a,b,c,d 5) 1-B,2-C,3-A 6) a,b,c,d"]},
 {"title":"Escenario: plataforma SaaS para múltiples talleres","inst":"Responde al escenario.","example":"Escenario: una API sirve a múltiples talleres (tenants) con órdenes, clientes y facturación. Se requiere aislamiento estricto, reportes por taller y posibilidad de escalar a cientos de tenants.",
  "items":[f"¿De dónde debe obtenerse el tenant en cada request? {ln()}",f"Indica 2 puntos donde aplicar filtro de tenant: {ln()}{ln()}",f"Riesgo de cache global sin segmentación: {ln()}",f"Estrategia de multi-tenancy elegida y por qué (breve): {ln()}{ln()}",f"Cómo probarías que taller A no ve datos de taller B: {ln()}{ln()}",f"3 señales de que la arquitectura necesita refactor: {ln()}{ln()}"],
  "ans":["1) del token/sesión autenticada 2) repositorio/queries y autorización 3) fuga de datos entre tenants 4) p.ej. columna tenant_id por simplicidad/costo inicial 5) tests de integración con dos tenants 6) duplicación, acoplamiento, cambios riesgosos"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Interfaz de repositorio {c('OrderRepository')} con método listado por tenant (firma). {ln()}{ln()}",f"Middleware/función conceptual para inyectar tenantContext desde auth: {ln()}{ln()}",f"3 reglas de multi-tenancy segura. {ln()}{ln()}{ln()}"],
  "ans":["1) listByTenant(tenantId, params): Promise<...> 2) extraer tenant de token y adjuntar a req/context 3) tenant desde auth, filtrar siempre, tests de aislamiento"]
  }
]})

units.append({
"n":16,"title":"Autenticación y sesiones: JWT, refresh tokens y 2FA/TOTP",
"context":"La autenticación establece la identidad del usuario y es la base de la seguridad en aplicaciones web. Implementarla correctamente implica gestionar credenciales, tokens, sesiones y segundo factor sin exponer información sensible. Esta unidad practica flujos con JWT, access/refresh tokens, almacenamiento seguro, rotación y fundamentos de 2FA/TOTP aplicados a APIs y clientes modernos.",
"exercises":[
 {"title":"Completar: fundamentos de autenticación y tokens","inst":"Completa con el concepto correcto.","example":"Ejemplo: La autenticación responde 'quién eres'; la autorización responde 'qué puedes hacer'.",
  "items":[f"La autenticación verifica la {b('md')} del usuario; la autorización verifica sus {b('md')}.",f"Un access token suele tener vida {b('sm')} para reducir riesgo ante exposición.",f"Un refresh token permite obtener nuevos access tokens sin reingresar {b('md')}.",f"Los JWT deben ser {b('md')} (verificar firma) antes de confiar en sus claims.",f"Guardar secretos de firma en {b('lg')} y rotarlos cuando sea necesario es buena práctica.",f"La expiración se controla con claims como {b('sm')} (exp) y se valida en cada petición."],
  "ans":["1) identidad / permisos 2) corta 3) credenciales 4) verificados 5) variables de entorno/secret manager 6) exp"]},
 {"title":"Completar: sesiones, almacenamiento y 2FA","inst":"Completa los conceptos.",
  "items":[f"Almacenar tokens en {c('localStorage')} expone a robo vía {b('md')} si hay XSS.",f"Cookies {c('HttpOnly')} ayudan a mitigar acceso desde {b('md')}.",f"La rotación de refresh tokens invalida el token anterior para reducir impacto de {b('md')}.",f"2FA/TOTP añade un factor basado en tiempo usando un {b('md')} compartido.",f"Tras habilitar 2FA, códigos de recuperación deben almacenarse de forma {b('md')}.",f"Un logout efectivo debe invalidar/rotar {b('md')} según la estrategia de sesión."],
  "ans":["1) XSS 2) JavaScript 3) robo/replay 4) secreto 5) segura 6) refresh tokens/sesión"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Confiar en el payload del JWT sin verificar la firma. → {ln()}",f"Usar el mismo secreto JWT en dev y producción. → {ln()}",f"Emitir access tokens de larga duración sin mecanismo de revocación/rotación. → {ln()}",f"Implementar rate limiting y protección contra fuerza bruta en login. → {ln()}",f"Registrar contraseñas o tokens en logs. → {ln()}",f"Validar issuer/audience/exp cuando corresponda. → {ln()}"],
  "ans":["a) Error b) Error c) Riesgo/mala práctica d) Correcto e) Error f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Hash de contraseñas: ({c('bcrypt/argon2')} / {c('MD5')} / {c('texto plano')}).",f"Access token comprometido: impacto menor si ({c('vida corta')} / {c('vida de 30 días')}).",f"Enviar token al API: cabecera ({c('Authorization: Bearer <token>')} / {c('X-Password')}).",f"Refresh token reuse detectado: ({c('revocar sesión/cadena')} / {c('ignorar')}).",f"2FA código: depende de ({c('tiempo y secreto')} / {c('solo username')}).",f"Comparación de secretos/HMAC: usar ({c('comparación segura/constante cuando aplique')} / {c('== en todo contexto sensible sin cuidado')})."],
  "ans":["1) bcrypt/argon2 2) vida corta 3) Authorization Bearer 4) revocar cadena 5) tiempo y secreto 6) comparación segura"]},
 {"title":"Elegir/decisión de sesión","inst":"Selecciona la mejor decisión.",
  "items":[f"Almacenamiento de sesión en SPA: ({c('evaluar HttpOnly cookies + CSRF')} / {c('localStorage sin mitigaciones')}).",f"Rotación de refresh: ({c('habilitar y detectar reuse')} / {c('nunca rotar')}).",f"Mensajes de login fallido: ({c('genéricos')} / {c('revelar si el email existe')}).",f"Bloqueo tras intentos fallidos: ({c('aplicar límites/backoff')} / {c('permitir infinitos')}).",f"Recuperación de cuenta: ({c('tokens de un uso y expiración')} / {c('enlaces permanentes')}).",f"Cierre de sesión global: ({c('invalidar refresh/sesiones')} / {c('solo borrar UI')})."],
  "ans":["1) evaluar cookies HttpOnly 2) habilitar 3) genéricos 4) aplicar límites 5) tokens un uso 6) invalidar sesiones"]},
 {"title":"Transformar: fortalecer flujo de autenticación","inst":"Transforma según se indique.",
  "items":[f"Login devuelve token sin expiración → añade claims/estrategia: {ln()}",f"Password comparada en texto plano → hashing/verificación correcta: {ln()}",f"Refresh token sin rotación → describe flujo con rotación: {ln()}{ln()}",f"Middleware que no verifica firma → corrección: {ln()}",f"Respuesta login 'usuario no existe' → respuesta segura: {ln()}",f"Habilitar 2FA: pasos básicos (alta/verificación/uso): {ln()}{ln()}{ln()}"],
  "ans":["1) incluir exp y tiempos cortos 2) bcrypt.hash/compare 3) emitir nuevo refresh e invalidar anterior, detectar reuse 4) verificar firma y claims 5) 'credenciales inválidas' 6) generar secreto, verificar TOTP, requerir en login"]},
 {"title":"Reordenar/relacionar: flujos de auth","inst":"Ordena o relaciona.",
  "items":[f"Login: (a) validar credenciales (b) emitir tokens (c) responder (d) cliente usa access token). → {ln()}",f"1)access 2)refresh 3)TOTP con A)segundo factor B)acceso corto C)renovar sesión. → {ln()}",f"Refresh con rotación: (a) enviar refresh (b) validar/no reuse (c) emitir nuevo par (d) invalidar anterior). → {ln()}",f"1)401 2)403 3)2FA requerido con A)falta factor B)sin auth C)sin permiso. → {ln()}",f"2FA setup: (a) generar secreto (b) mostrar QR (c) verificar código (d) activar). → {ln()}",f"1)XSS 2)CSRF 3)brute force con A)tokens en acciones B)robo en cliente C)intentos masivos. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-C,3-A 3) a,b,c,d 4) 1-B,2-C,3-A 5) a,b,c,d 6) 1-B,2-A,3-C"]},
 {"title":"Escenario: acceso a panel administrativo","inst":"Responde al escenario.","example":"Escenario: un panel administrativo para clínicas requiere login seguro, sesiones persistentes moderadas y 2FA para roles sensibles. Se detectaron intentos de fuerza bruta y tokens robados en un incidente previo.",
  "items":[f"Política de expiración para access y refresh tokens: {ln()}",f"¿Dónde almacenarías tokens en el cliente y por qué? {ln()}{ln()}",f"Controles ante fuerza bruta en login (3): {ln()}{ln()}",f"Flujo al detectar reuse de refresh token: {ln()}",f"¿Qué roles exigirían 2FA y cuándo solicitarlo? {ln()}{ln()}",f"3 eventos de seguridad a auditar: {ln()}{ln()}"],
  "ans":["1) access corto (min) y refresh más largo con rotación 2) preferir cookies HttpOnly+protecciones según contexto 3) rate limit, backoff/captcha, bloqueo progresivo 4) revocar cadena y forzar re-login 5) admin/supervisión en login y acciones sensibles 6) logins, fallos, refresh reuse, cambios 2FA"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Pseudocódigo de verificación JWT en middleware (firma y exp). {ln()}{ln()}{ln()}",f"Estructura de respuesta de login con access/refresh y flag 2FA. {ln()}{ln()}",f"3 reglas de autenticación segura para producción. {ln()}{ln()}{ln()}"],
  "ans":["1) extraer bearer, verify(token,secret), validar exp/claims 2) {accessToken,refreshToken,requires2fa} 3) hash robusto, tokens cortos+rotación, rate limiting, no loguear secretos"]
  }
]})

units.append({
"n":17,"title":"Autorización, RBAC y hardening de API",
"context":"Una vez autenticado el usuario, el sistema debe garantizar que solo acceda a recursos y acciones permitidas. La autorización deficiente es una fuente crítica de incidentes, especialmente en sistemas multi-tenant. Esta unidad practica RBAC, control de propiedad de recursos, y hardening de APIs con cabeceras, CORS, rate limiting, validación y manejo seguro de errores y secretos.",
"exercises":[
 {"title":"Completar: autorización y RBAC","inst":"Completa con el concepto correcto.","example":"Ejemplo: RBAC asigna permisos agrupados por roles a los usuarios.",
  "items":[f"Autorización basada en roles se denomina {b('sm')} y en atributos {b('sm')} (ABAC).",f"El principio de mínimo {b('md')} implica otorgar solo los permisos necesarios.",f"Verificar propiedad del recurso evita que un usuario acceda a objetos de {b('md')}.",f"Las decisiones de autorización deben basarse en identidad confiable del {b('md')} (token/sesión), no en el body.",f"Un permiso sensible debe validarse en el {b('md')} (backend), incluso si la UI lo oculta.",f"Auditar denegaciones de acceso ayuda a detectar intentos {b('md')}."],
  "ans":["1) RBAC / ABAC 2) privilegio 3) otros 4) contexto 5) servidor 6) maliciosos/anómalos"]},
 {"title":"Completar: hardening y controles defensivos","inst":"Completa los conceptos.",
  "items":[f"{c('Helmet')} ayuda a configurar cabeceras HTTP de {b('md')}.",f"Rate limiting mitiga abuso y ataques de {b('md')} en endpoints sensibles.",f"CORS debe permitir orígenes {b('md')} y configurarse con cuidado con credenciales.",f"La validación de entrada previene inyección y datos {b('md')}.",f"Secretos deben rotarse y almacenarse fuera del {b('md')}.",f"Mensajes de error en producción deben evitar filtrar {b('md')} internos."],
  "ans":["1) seguridad 2) fuerza bruta/DoS 3) específicos 4) malformados 5) código fuente 6) detalles"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Ocultar botones en UI es suficiente para proteger acciones administrativas. → {ln()}",f"Verificar rol y pertenencia al tenant en cada endpoint sensible. → {ln()}",f"Usar {c('CORS: *')} con credenciales en producción sin restricciones. → {ln()}",f"Aplicar rate limit a login y recuperación de contraseña. → {ln()}",f"Confiar en {c('isAdmin=true')} enviado por el cliente. → {ln()}",f"Usar HMAC para verificar integridad/autenticidad de webhooks cuando corresponde. → {ln()}"],
  "ans":["a) Error b) Correcto c) Error d) Correcto e) Error f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Usuario autenticado intenta borrar recurso ajeno: ({c('403')} / {c('200')}).",f"Endpoint público de salud: ({c('sin datos sensibles')} / {c('exponer secretos')}).",f"Cabecera para mitigar clickjacking (configurable): ({c('X-Frame-Options/ CSP frame-ancestors')} / {c('X-Powered-By on')}).",f"Política CORS: ({c('lista blanca')} / {c('reflejar cualquier origen con credenciales')}).",f"Validación: ({c('esquemas en borde')} / {c('confiar en cliente')}).",f"Webhook firmado: ({c('verificar firma')} / {c('aceptar sin validar')})."],
  "ans":["1) 403 2) sin datos sensibles 3) CSP/frame-ancestors 4) lista blanca 5) esquemas en borde 6) verificar firma"]},
 {"title":"Elegir/decisión de hardening","inst":"Selecciona la mejor decisión.",
  "items":[f"Permisos por defecto: ({c('deny by default')} / {c('allow all')}).",f"Errores de autorización: ({c('mensajes sin filtrar detalles')} / {c('revelar estructura interna')}).",f"Dependencias: ({c('actualizar y auditar')} / {c('ignorar vulnerabilidades')}).",f"Subida de archivos: ({c('validar tipo/tamaño y escanear si aplica')} / {c('aceptar todo')}).",f"Secretos en CI: ({c('secret store')} / {c('en texto plano en repo')}).",f"Logs: ({c('sin PII/secretos innecesarios')} / {c('todo en claro')})."],
  "ans":["1) deny by default 2) sin filtrar 3) auditar 4) validar 5) secret store 6) sin sensibles"]},
 {"title":"Transformar: asegurar endpoint","inst":"Transforma según se indique.",
  "items":[f"Endpoint admin sin chequeo de rol → añade guardia (concepto): {ln()}",f"Consulta por id sin tenant → añade condición de ownership/tenant: {ln()}",f"CORS abierto {c('*')} con credenciales → configuración segura: {ln()}",f"Respuesta de error con stack → respuesta segura: {ln()}",f"Webhook sin HMAC → verificación: {ln()}{ln()}",f"Rate limit inexistente en login → política: {ln()}"],
  "ans":["1) middleware requireRole('admin') 2) WHERE id AND tenant_id 3) orígenes específicos, credenciales controladas 4) mensaje genérico + log interno 5) validar firma HMAC y timestamp 6) límite por IP/usuario y backoff"]},
 {"title":"Reordenar/relacionar: controles de seguridad","inst":"Ordena o relaciona.",
  "items":[f"Request protegido: (a) autenticar (b) autorizar (c) validar (d) ejecutar). → {ln()}",f"1)RBAC 2)ownership 3)rate limit con A)permisos por rol B)control de abuso C)recurso propio. → {ln()}",f"1)401 2)403 3)429 con A)demasiadas peticiones B)no autenticado C)prohibido. → {ln()}",f"Hardening: (a) Helmet (b) CORS (c) validación (d) logging seguro). → {ln()}",f"Webhook: (a) leer raw body (b) verificar firma (c) validar payload (d) procesar). → {ln()}",f"1)confidencialidad 2)integridad 3)disponibilidad con A)HMAC B)rate limit C)cifrado/control acceso. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-A,2-C,3-B 3) 1-B,2-C,3-A 4) a,b,c,d 5) a,b,c,d 6) 1-C,2-A,3-B"]},
 {"title":"Escenario: API administrativa multi-tenant","inst":"Responde al escenario.","example":"Escenario: endpoints administrativos permiten exportar datos, cambiar roles y recibir webhooks de pagos. El sistema es multi-tenant y está expuesto a internet.",
  "items":[f"Controles para endpoint de cambio de rol (3): {ln()}{ln()}",f"Cómo evitar exportación de datos de otro tenant: {ln()}",f"Política de rate limiting para login y webhooks: {ln()}{ln()}",f"Verificación de webhook de pagos (pasos): {ln()}{ln()}",f"3 cabeceras/controles de hardening a aplicar: {ln()}{ln()}",f"Qué auditarías ante intentos de acceso indebido: {ln()}{ln()}"],
  "ans":["1) authn, RBAC admin, verificación tenant/alcance 2) tenant desde contexto y filtros obligatorios 3) límites por IP/ruta y tolerancia controlada 4) validar firma HMAC, timestamp, idempotencia 5) Helmet/CSP, CORS estricto, límites tamaño 6) actor, recurso, resultado, IP/tiempo"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Middleware {c('requireRole(role)')} (pseudocódigo). {ln()}{ln()}{ln()}",f"Función de verificación de firma HMAC (pasos). {ln()}{ln()}",f"3 reglas de autorización y hardening por defecto. {ln()}{ln()}{ln()}"],
  "ans":["1) comprobar req.user.roles incluye role sino 403 2) calcular HMAC del payload y comparar en tiempo seguro 3) deny by default, validar siempre, tenant desde contexto"]
  }
]})

units.append({
"n":18,"title":"Testing: unitario, integración y calidad automatizada",
"context":"Las pruebas automatizadas permiten verificar comportamiento, prevenir regresiones y refactorizar con confianza. Un buen balance entre tests unitarios e integración, junto con aislamiento y determinismo, es clave en aplicaciones full stack. Esta unidad practica diseño de casos con Vitest/Jest y Supertest, uso de mocks, patrón AAA, pruebas de API y criterios para tests mantenibles y útiles.",
"exercises":[
 {"title":"Completar: fundamentos de testing","inst":"Completa con el concepto correcto.","example":"Ejemplo: Un test unitario verifica una unidad pequeña de lógica de forma aislada.",
  "items":[f"El patrón AAA significa {b('sm')}, {b('sm')} y {b('sm')}.",f"Un test {b('md')} verifica colaboración entre componentes (ej. API + DB mockeada/real de prueba).",f"Los tests deben ser {b('md')} (mismo resultado en cada ejecución) y aislados.",f"Un mock reemplaza una dependencia para controlar su {b('md')}.",f"Un test que valida un bug corregido ayuda a evitar {b('md')}.",f"Nombrar tests por comportamiento esperado mejora la {b('md')} del reporte."],
  "ans":["1) Arrange, Act, Assert 2) de integración 3) deterministas 4) comportamiento 5) regresiones 6) legibilidad"]},
 {"title":"Completar: herramientas y alcance","inst":"Completa los conceptos.",
  "items":[f"Vitest/Jest proporcionan runner, aserciones y utilidades de {b('md')}.",f"Supertest permite probar endpoints HTTP llamando a la app sin levantar un {b('lg')}.",f"Las pruebas de integración de API suelen preparar datos (setup) y limpiar estado en {b('md')}.",f"Cubrir caminos felices y de error aumenta la {b('md')} del sistema.",f"Los tests lentos o frágiles reducen la confianza y el uso del {b('md')}.",f"Separar tests unitarios e integración ayuda a tiempos y {b('md')} de fallos."],
  "ans":["1) mocking 2) servidor externo manual 3) teardown 4) robustez 5) suite/pipeline 6) diagnóstico"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Tests que dependen del orden de ejecución y comparten estado mutable. → {ln()}",f"Usar datos de prueba aislados y limpiar entre casos cuando es necesario. → {ln()}",f"Mockear todo, incluso la lógica bajo prueba. → {ln()}",f"Probar solo el camino feliz. → {ln()}",f"Un test flaky se debe investigar y estabilizar. → {ln()}",f"Aserciones específicas y significativas son preferibles a snapshots indiscriminados. → {ln()}"],
  "ans":["a) Error b) Correcto c) Error d) Mala práctica e) Correcto f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Verificar suma de función pura: ({c('unitario')} / {c('e2e')} obligatorio).",f"Verificar POST /login responde 401 con credenciales inválidas: ({c('integración con Supertest')} / {c('solo lint')}).",f"Dependencia de reloj/fecha: ({c('mockear tiempo')} / {c('depender de hora real')}).",f"Base de datos en integración: ({c('entorno de prueba controlado')} / {c('producción')}).",f"Fallo esperado en validación: ({c('assert status y cuerpo')} / {c('no assert')}).",f"Nombre de test: ({c('describe comportamiento')} / {c('test1')})."],
  "ans":["1) unitario 2) integración 3) mockear tiempo 4) entorno de prueba 5) assert status/cuerpo 6) describe comportamiento"]},
 {"title":"Elegir/decisión de estrategia de pruebas","inst":"Selecciona la mejor decisión.",
  "items":[f"Bug reportado en producción: ({c('escribir test que lo reproduzca')} / {c('arreglar sin test')}).",f"Lógica crítica de cálculo: ({c('alta cobertura de casos borde')} / {c('un caso trivial')}).",f"Servicios externos inestables en CI: ({c('mock/stub controlado')} / {c('llamar siempre real')}).",f"Suite tarda demasiado: ({c('optimizar y paralelizar con cuidado')} / {c('eliminar tests al azar')}).",f"Tests de API: ({c('verificar códigos, esquema y efectos')} / {c('solo que no lance excepción')}).",f"Refactor grande: ({c('apoyarse en tests existentes y añadir')} / {c('sin red de seguridad')})."],
  "ans":["1) reproducir con test 2) casos borde 3) mock/stub 4) optimizar 5) verificar completo 6) apoyarse en tests"]},
 {"title":"Transformar: mejorar casos de prueba","inst":"Transforma según se indique.",
  "items":[f"Test sin aserción → añade assert significativo: {ln()}",f"Nombre {c('works')} → nombre descriptivo para login inválido: {ln()}",f"Dependencia de fecha real → uso de fake timers (concepto): {ln()}",f"Repetición de setup en 10 tests → estrategia: {ln()}",f"Test de endpoint sin verificar cuerpo → añade verificación: {ln()}",f"Mock que altera implementación real del módulo bajo prueba → corrección: {ln()}"],
  "ans":["1) expect(resultado).toBe(...) 2) 'returns 401 when password is invalid' 3) vi.useFakeTimers()/jest.useFakeTimers 4) beforeEach/helpers/factories 5) expect status y body 6) mockear solo dependencia externa"]},
 {"title":"Reordenar/relacionar: ciclo de testing","inst":"Ordena o relaciona.",
  "items":[f"AAA: (a) Arrange (b) Act (c) Assert. → {ln()}",f"1)unit 2)integration 3)e2e con A)flujo completo B)unidad aislada C)módulos integrados. → {ln()}",f"TDD bugfix: (a) test falla (b) corregir (c) test pasa (d) refactor). → {ln()}",f"1)mock 2)stub 3)spy con A)observa llamadas B)respuesta controlada C)doble general. → {ln()}",f"API test: (a) preparar datos (b) request (c) assert respuesta (d) assert estado/cleanup). → {ln()}",f"1)flaky 2)lento 3)frágil con A)depende de detalles internos B)no determinista C)alto tiempo. → {ln()}"],
  "ans":["1) a,b,c 2) 1-B,2-C,3-A 3) a,b,c,d 4) 1-C,2-B,3-A 5) a,b,c,d 6) 1-B,2-C,3-A"]},
 {"title":"Escenario: pruebas para módulo de autenticación","inst":"Responde al escenario.","example":"Escenario: el módulo de auth expone login, refresh y logout. Debe manejar credenciales inválidas, tokens expirados y rotación de refresh tokens. El equipo usa Vitest y Supertest.",
  "items":[f"2 casos unitarios para lógica de tokens/hash: {ln()}{ln()}",f"2 casos de integración para POST /login: {ln()}{ln()}",f"Cómo probarías refresh token reuse: {ln()}{ln()}",f"Qué mockearías y qué no en estas pruebas: {ln()}{ln()}",f"Dato sensible que nunca debe aparecer en fixtures/logs: {ln()}",f"Criterio para considerar estable la suite de auth: {ln()}"],
  "ans":["1) hash/compare y expiración/claims 2) 200 con credenciales válidas, 401 inválidas 3) usar token rotado dos veces y esperar revocación/401 4) mockear externos; no la lógica bajo prueba 5) contraseñas/tokens reales 6) determinista, rápida y cubre casos críticos"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Esqueleto de test (Vitest/Jest) para función {c('isAdult(age)')}. {ln()}{ln()}{ln()}{ln()}",f"Esqueleto de prueba Supertest para {c('GET /health')} → 200. {ln()}{ln()}{ln()}",f"3 reglas para tests mantenibles. {ln()}{ln()}{ln()}"],
  "ans":["1) describe/it con expect true/false 2) request(app).get('/health').expect(200) 3) deterministas, claros, aislados"]
  }
]})

units.append({
"n":19,"title":"Cobertura, calidad de código y automatización en CI",
"context":"La calidad sostenible requiere automatizar verificaciones en cada cambio. Cobertura de pruebas, análisis estático, tipado y pipelines de integración continua permiten detectar problemas temprano y mantener estándares. Esta unidad practica interpretación de cobertura, umbrales, configuración conceptual de CI, gates de calidad y estrategias para que la automatización aporte señal real y no falsas seguridades.",
"exercises":[
 {"title":"Completar: cobertura y métricas de calidad","inst":"Completa con el concepto correcto.","example":"Ejemplo: La cobertura de ramas mide si se evaluaron ambos caminos de una condición.",
  "items":[f"La cobertura de {b('md')} mide líneas ejecutadas y la de {b('md')} mide decisiones condicionales.",f"Un porcentaje alto de cobertura no garantiza ausencia de {b('md')} ni buena calidad de aserciones.",f"Los umbrales (thresholds) en CI definen el mínimo aceptable de {b('md')}.",f"La deuda técnica crece cuando se posponen correcciones de {b('md')} y diseño.",f"El análisis estático (lint) detecta problemas sin {b('md')} el código.",f"El chequeo de tipos en TypeScript ({c('tsc --noEmit')}) ayuda a prevenir errores de {b('md')}."],
  "ans":["1) líneas / ramas 2) bugs 3) cobertura/calidad 4) calidad 5) ejecutar 6) tipos"]},
 {"title":"Completar: pipelines y gates","inst":"Completa los conceptos.",
  "items":[f"Un pipeline de CI se dispara típicamente en {b('md')} o pull requests.",f"Pasos comunes: instalar, lint, typecheck, {b('md')} y build.",f"Un gate de calidad impide merge si los checks {b('md')}.",f"Los jobs pueden ejecutarse en paralelo para reducir {b('md')}.",f"Cachear dependencias acelera ejecuciones repetidas del {b('md')}.",f"Reportes de cobertura y resultados deben ser {b('md')} para el equipo."],
  "ans":["1) push 2) test 3) fallan 4) tiempo 5) pipeline 6) visibles"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Subir cobertura ignorando tests de casos de error importantes. → {ln()}",f"Ejecutar lint, typecheck y tests en CI para cada PR. → {ln()}",f"Deshabilitar el pipeline porque 'retrasa'. → {ln()}",f"Fijar versiones de acciones/dependencias críticas para reproducibilidad. → {ln()}",f"Permitir merge con tests fallidos. → {ln()}",f"Usar reportes para identificar módulos sin cobertura relevante. → {ln()}"],
  "ans":["a) Mala práctica b) Correcto c) Error d) Correcto e) Error f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Cobertura de ramas baja indica: ({c('condiciones no probadas')} / {c('código perfecto')}).",f"Paso que detecta errores de formato/reglas: ({c('lint')} / {c('deploy')}).",f"Paso que valida tipos TS: ({c('tsc --noEmit')} / {c('npm start')}).",f"Pipeline verde: ({c('pasaron checks definidos')} / {c('cero bugs garantizados')}).",f"Flaky tests en CI: ({c('estabilizar')} / {c('reintentar infinito sin arreglar')}).",f"Artefacto de cobertura: ({c('reporte HTML/lcov')} / {c('imagen PNG del código')})."],
  "ans":["1) condiciones no probadas 2) lint 3) tsc --noEmit 4) pasaron checks 5) estabilizar 6) reporte HTML/lcov"]},
 {"title":"Elegir/decisión de calidad","inst":"Selecciona la mejor decisión.",
  "items":[f"Umbral de cobertura: ({c('realista y progresivo')} / {c('100% inmediato sin plan')}).",f"Código legacy sin tests: ({c('agregar tests en cambios críticos')} / {c('ignorar siempre')}).",f"Exclusiones de cobertura: ({c('justificadas y mínimas')} / {c('excluir todo')}).",f"Monorepo: ({c('pipelines por paquete/afectados')} / {c('correr todo siempre sin optimizar')}) según escala.",f"Secretos en CI: ({c('secrets del proveedor')} / {c('en YAML commiteado')}).",f"Notificaciones: ({c('fallos accionables')} / {c('ruido constante')})."],
  "ans":["1) realista 2) en cambios críticos 3) justificadas 4) por afectados según escala 5) secrets 6) accionables"]},
 {"title":"Transformar: mejorar pipeline y calidad","inst":"Transforma según se indique.",
  "items":[f"Pipeline sin tests → añade pasos mínimos: {ln()}{ln()}",f"Proyecto sin typecheck → comando a agregar: {ln()}",f"Cobertura global 40% sin foco → estrategia de mejora: {ln()}{ln()}",f"Job lento instala deps siempre → optimización: {ln()}",f"PR mergeado con lint roto → gate necesario: {ln()}",f"Reporte ignorado → acción para hacerlo útil: {ln()}"],
  "ans":["1) lint,typecheck,test,build 2) tsc --noEmit 3) priorizar módulos críticos y umbrales progresivos 4) cache de dependencias 5) required checks 6) publicar y revisar en PR"]},
 {"title":"Reordenar/relacionar: CI y calidad","inst":"Ordena o relaciona.",
  "items":[f"CI típico: (a) checkout (b) install (c) lint/typecheck/test (d) build/report). → {ln()}",f"1)lint 2)typecheck 3)test 4)build con A)compila B)reglas estáticas C)tipos D)comportamiento. → {ln()}",f"Mejora de cobertura: (a) medir (b) identificar brechas (c) añadir tests útiles (d) ajustar umbral). → {ln()}",f"1)gate 2)cache 3)matrix con A)acelera B)múltiples entornos C)bloquea merge. → {ln()}",f"Ante fallo: (a) ver logs (b) reproducir local (c) corregir (d) re-ejecutar). → {ln()}",f"1)líneas 2)ramas 3)funciones con A)condiciones B)ejecutadas C)invocadas. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-C,3-D,4-A 3) a,b,c,d 4) 1-C,2-A,3-B 5) a,b,c,d 6) 1-B,2-A,3-C"]},
 {"title":"Escenario: pipeline para monorepo de servicios","inst":"Responde al escenario.","example":"Escenario: equipo mantiene API, frontend y paquetes compartidos. Los PR tardan mucho y a veces se cuelan regresiones por tests insuficientes en módulos críticos de pagos.",
  "items":[f"Pasos obligatorios del pipeline para cada PR: {ln()}{ln()}",f"Estrategia para reducir tiempo en monorepo: {ln()}{ln()}",f"Cómo aumentar calidad en módulo de pagos sin perseguir 100% global: {ln()}{ln()}",f"Qué harías con tests flaky que bloquean el pipeline: {ln()}",f"Métricas/reportes que publicarías: {ln()}{ln()}",f"Política de merge ante checks rojos: {ln()}"],
  "ans":["1) lint,typecheck,test,build 2) jobs por paquete afectado/cache 3) umbrales y tests dirigidos en pagos 4) cuarentena temporal con ticket y corrección prioritaria 5) resultados tests, cobertura, tiempos 6) no mergear hasta verde"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"YAML conceptual (pasos) de workflow CI para Node/TS (lista). {ln()}{ln()}{ln()}{ln()}",f"Comandos npm típicos para calidad: {ln()}",f"3 indicadores de que tu CI aporta valor real. {ln()}{ln()}{ln()}"],
  "ans":["1) checkout, setup-node, install, lint, typecheck, test, build 2) npm run lint && npm run typecheck && npm test 3) detecta regresiones, rápido/estable, bloquea merges malos"]
  }
]})

units.append({
"n":20,"title":"Docker, CI/CD, despliegue y observabilidad",
"context":"Entregar software de forma confiable requiere empaquetar aplicaciones, automatizar despliegues y observar su comportamiento en ejecución. Docker, pipelines CI/CD y prácticas de observabilidad reducen diferencias entre entornos y mejoran el tiempo de respuesta ante incidentes. Esta unidad practica contenedores, configuración por entorno, flujos de despliegue y fundamentos de logs, métricas y health checks.",
"exercises":[
 {"title":"Completar: Docker y empaquetado","inst":"Completa con el concepto correcto.","example":"Ejemplo: Una imagen Docker es una plantilla inmutable; un contenedor es una instancia en ejecución.",
  "items":[f"Un {c('Dockerfile')} define los pasos para construir una {b('md')}.",f"{c('docker-compose')} facilita definir y ejecutar múltiples {b('md')} localmente.",f"{c('.dockerignore')} excluye archivos del {b('md')} de build para reducir tamaño y riesgo.",f"Las variables de entorno permiten configurar la app por {b('md')} sin cambiar la imagen.",f"Usar imágenes base actualizadas y mínimas reduce superficie de {b('md')}.",f"Etiquetar imágenes (tags) facilita {b('md')} y rollback."],
  "ans":["1) imagen 2) servicios/contenedores 3) contexto 4) entorno 5) ataque 6) trazabilidad/versionado"]},
 {"title":"Completar: CI/CD y observabilidad","inst":"Completa los conceptos.",
  "items":[f"CI valida cambios automáticamente; CD automatiza la {b('md')} o entrega a entornos.",f"Un despliegue seguro requiere artefactos reproducibles y configuración por {b('md')}.",f"Health checks (liveness/readiness) permiten detectar instancias {b('md')}.",f"Logs estructurados facilitan búsqueda y {b('md')} de incidentes.",f"Métricas (latencia, errores, throughput) ayudan a entender el {b('md')} del sistema.",f"Alertas deben ser accionables para evitar fatiga por {b('md')}."],
  "ans":["1) entrega/despliegue 2) entorno 3) no saludables 4) diagnóstico 5) comportamiento 6) ruido"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Incluir secretos en el Dockerfile o en la imagen. → {ln()}",f"Usar la misma configuración y credenciales en dev y prod. → {ln()}",f"Definir health check para que el orquestador detecte fallos. → {ln()}",f"Desplegar sin pipeline ni pruebas automatizadas. → {ln()}",f"Registrar información sensible (tokens, contraseñas) en logs. → {ln()}",f"Versionar y almacenar artefactos/imágenes para rollback. → {ln()}"],
  "ans":["a) Error b) Error c) Correcto d) Riesgo alto e) Error f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Exponer puerto de app en contenedor: ({c('EXPOSE/puerto mapeado')} / {c('ninguno y esperar que funcione')}).",f"Dependencia DB en compose: ({c('service y env vars')} / {c('hardcode localhost de host siempre')}).",f"Estrategia de despliegue gradual: ({c('rolling/blue-green/canary')} / {c('reemplazo sin monitoreo')}).",f"Fallo en health check: ({c('reiniciar/sacar de balanceo')} / {c('ignorar')}).",f"Logs: ({c('estructurados con nivel/contexto')} / {c('texto caótico sin contexto')}).",f"Configuración: ({c('env/secrets por entorno')} / {c('quemada en imagen')})."],
  "ans":["1) puerto mapeado 2) service y env 3) rolling/canary 4) sacar/reiniciar 5) estructurados 6) env/secrets"]},
 {"title":"Elegir/decisión operativa","inst":"Selecciona la mejor decisión.",
  "items":[f"Incidente en producción: ({c('revisar logs/métricas y mitigar')} / {c('adivinar')}).",f"Rollback: ({c('planificado y probado')} / {c('imposible')}).",f"Escalado: ({c('basado en métricas')} / {c('aleatorio')}).",f"Tiempo de build: ({c('optimizar capas/cache')} / {c('ignorar')}).",f"Acceso a servidores: ({c('mínimo privilegio')} / {c('acceso total para todos')}).",f"Alertas: ({c('SLO/umbrales claros')} / {c('todo alerta crítica')})."],
  "ans":["1) observar y mitigar 2) planificado 3) en métricas 4) optimizar 5) mínimo privilegio 6) umbrales claros"]},
 {"title":"Transformar: mejorar empaquetado y entrega","inst":"Transforma según se indique.",
  "pre":"FROM node:latest\nCOPY . .\nRUN npm install\nCMD node src/index.js",
  "items":[f"Mejora Dockerfile: versión fija, directorio de trabajo y copia selectiva: {ln()}{ln()}",f"Añade .dockerignore (3 entradas): {ln()}",f"Expón puerto y usa CMD/ENTRYPOINT claro: {ln()}",f"Externaliza config a env vars (3 ejemplos): {ln()}",f"Añade paso de CI antes de build/push de imagen: {ln()}",f"Define health endpoint a usar por orquestador: {ln()}"],
  "ans":["1) FROM node:20-alpine, WORKDIR, COPY package*, RUN npm ci, COPY src 2) node_modules,.git,.env 3) EXPOSE 3000 y CMD 4) PORT,DATABASE_URL,JWT_SECRET 5) tests/lint/build 6) GET /health"]},
 {"title":"Reordenar/relacionar: entrega y operación","inst":"Ordena o relaciona.",
  "items":[f"Flujo CI/CD: (a) commit/PR (b) CI checks (c) build imagen (d) deploy). → {ln()}",f"1)liveness 2)readiness 3)metrics con A)tráfico listo B)vive C)rendimiento. → {ln()}",f"Incidente: (a) detectar alerta (b) diagnosticar (c) mitigar/rollback (d) postmortem). → {ln()}",f"1)imagen 2)contenedor 3)registry con A)instancia B)almacén C)plantilla. → {ln()}",f"Build eficiente: (a) deps cacheables (b) copiar código (c) build (d) imagen final). → {ln()}",f"1)logs 2)métricas 3)trazas con A)números B)eventos C)recorrido request. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-A,3-C 3) a,b,c,d 4) 1-C,2-A,3-B 5) a,b,c,d 6) 1-B,2-A,3-C"]},
 {"title":"Escenario: despliegue de API de inventario","inst":"Responde al escenario.","example":"Escenario: debes contenerizar y desplegar una API Node.js con PostgreSQL. El equipo usa GitHub Actions, necesita entornos staging/prod y quiere detectar rápido caídas y errores 5xx.",
  "items":[f"Servicios mínimos en docker-compose para desarrollo (2-3): {ln()}",f"Variables sensibles que no deben ir en imagen: {ln()}",f"Pasos del pipeline hasta publicar imagen: {ln()}{ln()}",f"Health check y señal para marcar instancia no lista: {ln()}",f"3 métricas/logs clave para monitorear: {ln()}{ln()}",f"Estrategia de rollback ante despliegue fallido: {ln()}"],
  "ans":["1) api y db (y opcional admin) 2) DB URL, secretos JWT, keys 3) lint/test/build, docker build/push 4) /health y readiness según dependencias 5) tasa 5xx, latencia, errores de DB 6) redeploy de imagen/tag previa"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Dockerfile básico para app Node 20 (multi-etapa simple o pasos clave). {ln()}{ln()}{ln()}{ln()}{ln()}",f"Fragmento docker-compose con api y postgres (campos esenciales). {ln()}{ln()}{ln()}{ln()}",f"3 prácticas de operación confiable en producción. {ln()}{ln()}{ln()}"],
  "ans":["1) FROM node:20-alpine, WORKDIR, COPY package*, npm ci --omit=dev, COPY, EXPOSE, CMD 2) services api y postgres con env/ports/depends_on 3) health checks, observabilidad, rollback y secretos seguros"]
  }
]})

# Render and save U15-U20
for u in units:
    frag = render_unit_html(u)
    ans = render_ans(u)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}_ans.html"),"w",encoding="utf-8").write(ans)
    print(u['n'], len(frag), len(ans))

# Assemble final workbook
HEAD = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Workbook Full Stack — Práctica guiada (Edición extendida)</title>
<style>
:root{--ink:#1a1a1a;--muted:#555;--accent:#0f766e;--accent2:#155e75;--line:#cbd5e1;--bg:#fff;--soft:#f8fafc}
*{box-sizing:border-box}body{font-family:Georgia,"Times New Roman",serif;color:var(--ink);background:var(--bg);margin:0;line-height:1.55}
.page{max-width:820px;margin:0 auto;padding:36px 44px}
h1,h2,h3{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#0b3b36}
h1{font-size:2.2rem;margin:0 0 .25rem}.subtitle{color:var(--muted);margin:0 0 1.1rem}
h2{font-size:1.38rem;border-bottom:2px solid var(--accent);padding-bottom:.25rem;margin:1.8rem 0 .5rem}
h3{font-size:1.06rem;margin:1.05rem 0 .28rem;color:var(--accent2)}
.context{font-style:italic;color:var(--muted);margin:.2rem 0 .8rem}
.exercise{margin:.8rem 0 1rem}.inst{font-family:system-ui,sans-serif;font-weight:600;margin:.3rem 0 .25rem}
ol.items{margin:.15rem 0 .15rem 1.3rem;padding:0}ol.items li{margin:.32rem 0}
.blank{display:inline-block;min-width:9ch;border-bottom:1px solid #334155;height:1.1em;vertical-align:baseline}
.blank.sm{min-width:5ch}.blank.md{min-width:16ch}.blank.lg{min-width:30ch}.blank.xl{min-width:42ch}
.line{display:block;border-bottom:1px solid #94a3b8;height:1.45em;margin:.16rem 0}
.example{background:var(--soft);border-left:3px solid var(--accent);padding:.5rem .7rem;margin:.45rem 0;font-size:.94rem}
code{font-family:ui-monospace,Consolas,monospace;background:#f1f5f9;padding:.04rem .28rem;border-radius:3px;font-size:.9em}
pre{background:#0f172a;color:#e2e8f0;padding:.65rem .85rem;border-radius:6px;overflow:auto;font-size:.83rem;line-height:1.42;white-space:pre-wrap;margin:.4rem 0}
.note{font-size:.91rem;color:var(--muted)}
.toc ul{columns:2;gap:2rem;margin:.4rem 0}.toc li{margin:.18rem 0;font-family:system-ui,sans-serif;font-size:.93rem}
.answers{page-break-before:always}.key{font-family:system-ui,sans-serif;font-size:.92rem}.key p{margin:.2rem 0}.key .u{margin-top:.8rem;font-weight:700;color:#0b3b36}
table.meta{border-collapse:collapse;width:100%;font-family:system-ui,sans-serif;font-size:.9rem;margin:.5rem 0}
table.meta th,table.meta td{border:1px solid #e2e8f0;padding:.3rem .45rem;text-align:left}
@media print{.page{max-width:none;padding:0 7mm}body{font-size:10.7pt}h2{page-break-after:avoid}.exercise,.example,pre{page-break-inside:avoid}.unit{page-break-before:always}.unit:first-of-type,.cover{page-break-before:auto}}
@page{margin:14mm}
</style>
</head><body><div class="page">
'''

toc_titles = [
 (1,"JS moderno y entorno Node.js 20+ (ESM)"),(2,"TypeScript esencial: tipos, uniones y narrowing"),
 (3,"Asincronía: event loop, promesas y async/await"),(4,"HTTP, REST y diseño de contratos de API"),
 (5,"Git, colaboración y revisión de código"),(6,"React 18: componentes, props, estado y composición"),
 (7,"React: efectos, hooks y rendimiento"),(8,"Next.js App Router: rutas, Server/Client Components y datos"),
 (9,"UI con Tailwind CSS, formularios y accesibilidad básica"),(10,"Integración cliente-API y gestión de estado remoto"),
 (11,"Node.js, Express y arquitectura de API"),(12,"Validación de datos, manejo de errores y contratos (Zod)"),
 (13,"PostgreSQL y modelado relacional"),(14,"SQL práctico y Prisma ORM"),
 (15,"Arquitectura de servicios, modularidad y multi-tenancy"),(16,"Autenticación y sesiones: JWT, refresh tokens y 2FA/TOTP"),
 (17,"Autorización, RBAC y hardening de API"),(18,"Testing: unitario, integración y calidad automatizada"),
 (19,"Cobertura, calidad de código y automatización en CI"),(20,"Docker, CI/CD, despliegue y observabilidad")
]

cover = f'''<section class="cover">
<h1>Workbook Full Stack</h1>
<p class="subtitle">Práctica guiada de desarrollo web moderno — De fundamentos a arquitectura, calidad y entrega (Edición extendida)</p>
<p class="note">Orientado a: TypeScript, JavaScript, Node.js 20+, React 18+, Next.js (App Router), APIs REST, PostgreSQL/Prisma, testing (Vitest/Jest/Supertest), seguridad (JWT/Refresh/TOTP/RBAC/hardening), Docker y CI/CD. Diseñado con progresión por niveles, micro-contexto por unidad, ejercicios graduados (completar, corregir, elegir, transformar, reordenar, escenarios y producción) y solucionario final. Imprime o guarda como PDF desde el navegador.</p>
<table class="meta"><tr><th>Unidades</th><th>Ejercicios</th><th>Ítems (aprox.)</th><th>Metodología</th></tr>
<tr><td>20</td><td>180</td><td>1080</td><td>Progresión guiada, andamiaje, distractores plausibles, soluciones modelo</td></tr></table>
</section>
<section class="toc"><h2>Índice</h2><ul>
''' + "\n".join(f"<li><a href='#u{n}'>Unidad {n}. {e(t)}</a></li>" for n,t in toc_titles) + "</ul></section>\n"

# collect all unit html and answers in order
unit_htmls = []
ans_htmls = []
for i in range(1,21):
    up = os.path.join(UNITS_DIR,f"u{i:02d}.html")
    ap = os.path.join(UNITS_DIR,f"u{i:02d}_ans.html")
    if os.path.exists(up): unit_htmls.append(open(up,encoding="utf-8").read())
    if os.path.exists(ap): ans_htmls.append(open(ap,encoding="utf-8").read())

answers_sec = '<section class="answers"><h2>Solucionario</h2><p class="note">Respuestas de referencia. En ejercicios de producción/escenario se incluyen soluciones modelo; pueden existir variantes válidas si mantienen corrección, claridad y seguridad.</p><div class="key">' + "\n".join(ans_htmls) + '</div></section>'

html_out = HEAD + cover + "\n".join(unit_htmls) + "\n" + answers_sec + "\n</div></body></html>\n"
out_path = os.path.join(BASE, "workbook-fullstack-200.html")
open(out_path,"w",encoding="utf-8").write(html_out)
print("ASSEMBLED", len(html_out), out_path)
