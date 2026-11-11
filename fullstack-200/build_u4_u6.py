# -*- coding: utf-8 -*-
import os, html
BASE = r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS_DIR = os.path.join(BASE, "units")
os.makedirs(UNITS_DIR, exist_ok=True)

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

u4 = {
"n":4,"title":"HTTP, REST y diseño de contratos de API",
"context":"Las APIs REST son el punto de unión entre frontend, backend y terceros, por lo que un contrato claro evita ambigüedades y retrabajos. Dominar métodos HTTP, códigos de estado, modelado de recursos, idempotencia y paginación permite diseñar servicios predecibles y fáciles de consumir. Esta unidad practica decisiones de diseño y corrección de errores comunes en endpoints reales.",
"exercises":[
 {"title":"Completar: métodos y códigos HTTP","inst":"Completa con el término o código correcto.",
  "example":f"Ejemplo: Para obtener un recurso sin modificarlo se usa el método {c('GET')}.",
  "items":[
   f"Para crear un recurso suele usarse {b('sm')} y para reemplazar completamente uno existente {b('sm')}.",
   f"Una actualización parcial se asocia comúnmente a {b('sm')}.",
   f"Creación exitosa: {b('sm')} ; solicitud inválida por validación: {b('sm')} (o 422).",
   f"No autenticado: {b('sm')} ; autenticado sin permisos: {b('sm')}.",
   f"Recurso no existe: {b('sm')} ; conflicto (duplicado): {b('sm')}.",
   f"Un método es {b('md')} si repetir la misma petición produce el mismo efecto."],
  "ans":["1) POST / PUT 2) PATCH 3) 201 / 400 4) 401 / 403 5) 404 / 409 6) idempotente"]},
 {"title":"Completar: recursos, rutas y paginación","inst":"Completa los conceptos de diseño REST.",
  "items":[
   f"Las rutas deben modelar {b('md')} (sustantivos) en lugar de acciones RPC.",
   f"{c('GET /tenants/{id}/orders')} es un ejemplo de recurso {b('md')}.",
   f"Paginación por offset usa {b('sm')} y {b('sm')} y metadatos como {b('lg')}.",
   f"Para colecciones grandes, la paginación por {b('md')} (cursor) suele ser más estable.",
   f"Versionado en ruta ejemplo: {b('md')}.",
   f"Errores consistentes incluyen {c('code')}, {c('message')} y opcionalmente {b('md')}."],
  "ans":["1) recursos 2) anidado 3) page/limit, total/page/pageSize 4) cursor 5) /v1 6) details"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"{c('GET /createUser')} para crear usuarios. → {ln()}",f"Devolver 200 con error cuando el recurso no existe. → {ln()}",f"Usar 409 ante email duplicado con restricción única. → {ln()}",f"Responder 401 cuando el usuario autenticado no tiene rol suficiente. → {ln()}",f"Documentar ISO 8601 y zonas horarias en el contrato. → {ln()}",f"Permitir tenantId arbitrario del cliente sin validar contra sesión. → {ln()}"],
  "ans":["a) Error: POST /users b) Error: 404 c) Correcto d) Error: 403 e) Correcto f) Error: fallo de autorización"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa más adecuada.",
  "items":[f"Detalle de producto 10: ({c('POST /products/10')} / {c('GET /products/10')} / {c('GET /getProduct')}).",f"Evitar cobro duplicado en reintentos: ({c('sin control')} / {c('idempotency key')}).",f"Filtro por estado: ({c('GET /orders?status=paid')} / {c('POST /filterStatus')}).",f"Eliminar: ({c('DELETE')} / {c('REMOVE')}) y éxito sin cuerpo ({c('204')} / {c('500')}).",f"Colección vacía: ({c('404')} / {c('200 con array vacío')} / {c('500')}).",f"Cabecera JSON: ({c('Content-Type: application/json')} / {c('Accept-Language: json')})."],
  "ans":["1) GET /products/10 2) idempotency key 3) GET /orders?status=paid 4) DELETE/204 5) 200 con array vacío 6) Content-Type: application/json"]},
 {"title":"Elegir/decisión de contrato","inst":"Selecciona la mejor decisión.",
  "items":[f"Fechas: ({c('formato libre')} / {c('ISO 8601')}).",f"Errores de validación: ({c('genérico')} / {c('detalles por campo')}).",f"Paginación: ({c('sin límite')} / {c('límite y máximo')}).",f"Cambio incompatible: ({c('romper v1')} / {c('versionar/migrar')}).",f"Nombres JSON: ({c('mezcla inconsistente')} / {c('convención consistente')}).",f"Operación larga: ({c('bloqueo sin estrategia')} / {c('202 + job')} cuando aplique)."],
  "ans":["1) ISO 8601 2) detalles por campo 3) límite y máximo 4) versionar/migrar 5) consistente 6) 202 + job"]},
 {"title":"Transformar: mejorar diseño de endpoint","inst":"Transforma la propuesta.",
  "items":[f"{c('POST /doLogin')} → {ln()}",f"{c('GET /users/delete?id=5')} → {ln()}",f"Error plano → estructura JSON: {ln()}{ln()}",f"10.000 registros sin paginar → {ln()}",f"Reintento no idempotente → protección: {ln()}",f"Ruta ambigua {c('/api/data')} para repuestos → {ln()}"],
  "ans":["1) POST /auth/login o /sessions 2) DELETE /users/5 3) {error:{code,message,details}} 4) page/limit o cursor 5) idempotency key 6) /api/spare-parts"]},
 {"title":"Reordenar/relacionar: request/response y diseño","inst":"Ordena o relaciona.",
  "items":[f"Ciclo: (a) request (b) valida (c) procesa (d) responde. → {ln()}",f"1)GET 2)POST 3)DELETE 4)PUT con A)eliminar B)leer C)crear D)reemplazar. → {ln()}",f"1)400 2)401 3)403 4)404 con A)no encontrado B)sin auth C)sin permiso D)inválido. → {ln()}",f"Diseño: (a) recurso (b) método/códigos (c) esquema (d) documentar. → {ln()}",f"1)idempotencia 2)paginación 3)versionado con A)evolución B)reintentos C)colecciones. → {ln()}",f"Validación: (a) detectar (b) detalles (c) 400/422 (d) no ejecutar negocio. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-C,3-A,4-D 3) 1-D,2-B,3-C,4-A 4) a,b,c,d 5) 1-B,2-C,3-A 6) a,b,d,c"]},
 {"title":"Escenario: API de reservas de talleres mecánicos","inst":"Responde al escenario.",
  "example":"Escenario: API para gestionar reservas de hora en talleres multi-sucursal; hay reintentos por mala señal y clientes web/móvil.",
  "items":[f"Método y ruta para crear reserva en tenant t1: {ln()}",f"Código si horario ocupado: {ln()}",f"Evitar duplicados por reintento: {ln()}",f"Query params para reservas del día con filtros: {ln()}",f"Validaciones de autorización imprescindibles: {ln()}",f"Estructura de error para fecha inválida/sucursal inexistente: {ln()}"],
  "ans":["1) POST /tenants/t1/bookings 2) 409 3) idempotency key 4) date,status,page,limit 5) auth y pertenencia al tenant 6) 400/404 con code,message,details"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Especifica método/ruta/status para listar mecánicos de un taller. {ln()}{ln()}",f"Ejemplo JSON de respuesta paginada con metadatos. {ln()}{ln()}{ln()}",f"3 reglas de diseño de API para tu equipo. {ln()}{ln()}"],
  "ans":["1) GET /workshops/{id}/mechanics 200/403/404 2) {data:[...],meta:{page,limit,total}} 3) recursos claros, códigos coherentes, errores consistentes, versionado"]
  }
]
}

u5 = {
"n":5,"title":"Git, colaboración y revisión de código",
"context":"El control de versiones y la colaboración efectiva sostienen la calidad y la trazabilidad del software en equipos. Dominar ramas, commits claros, pull requests, resolución de conflictos y code review permite integrar cambios con seguridad. Esta unidad enfoca prácticas que reducen regresiones y facilitan auditoría en proyectos con CI/CD.",
"exercises":[
 {"title":"Completar: conceptos básicos de Git","inst":"Completa con el término correcto.","example":"Ejemplo: Un commit registra una instantánea con mensaje descriptivo.",
  "items":[f"Crear y cambiar a rama nueva: {c('git switch -c')} {b('md')}.",f"Área de preparación antes de confirmar: {b('md')}.",f"{c('git diff')} muestra cambios no preparados y {c('git log --oneline')} muestra {b('lg')}.",f"Remoto común {b('sm')} y rama principal {b('sm')}/{c('main')}.",f"Alternativa a pull: {b('md')} y luego integrar.",f"Un tag marca típicamente una {b('md')}."],
  "ans":["1) nombre-rama 2) staging/index 3) historial compacto 4) origin / master 5) git fetch 6) versión/release"]},
 {"title":"Completar: flujo de PR y revisión","inst":"Completa las prácticas.",
  "items":[f"Un PR debe describir {b('md')}, alcance y cómo se {b('md')}.",f"Commits atómicos facilitan {b('md')} y revertir.",f"Code review verifica bugs, diseño y {b('lg')}.",f"Antes de PR ejecutar {b('md')} y pruebas.",f"Resolver conflictos sin perder {b('md')}.",f"Proteger main requiere {b('md')} y checks verdes."],
  "ans":["1) propósito/probó 2) revisión 3) calidad/pruebas/seguridad 4) linters 5) funcionalidad 6) aprobaciones"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Commitear secretos (.env, claves). → {ln()}",f"Mensajes de commit claros y explicativos. → {ln()}",f"Force push a main compartida sin coordinación. → {ln()}",f"Revisar PRs grandes por partes y probar cuando sea posible. → {ln()}",f"Ignorar fallos de CI. → {ln()}",f"Usar .gitignore para artefactos y dependencias. → {ln()}"],
  "ans":["a) Error b) Correcto c) Error d) Correcto e) Error f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Descartar cambios locales no commiteados (cuidado): ({c('git restore')} / {c('git push -f')}).",f"Integración que preserva merge commit: ({c('merge')} / {c('rebase')} siempre).",f"Mejor mensaje: ({c('fix')} / {c('fix(auth): handle expired refresh token')}).",f"Conflicto en PR: ({c('ignorar')} / {c('resolver, probar, actualizar')}).",f"Feature branch desde: ({c('main actualizada')} / {c('rama obsoleta')}).",f"Ver cambios de un commit: ({c('git show')} / {c('git init')})."],
  "ans":["1) git restore 2) merge 3) mensaje descriptivo 4) resolver y probar 5) main actualizada 6) git show"]},
 {"title":"Elegir/decisión de flujo","inst":"Selecciona la mejor práctica.",
  "items":[f"PR: ({c('enorme')} / {c('acotado')}).",f"WIP: ({c('sin contexto')} / {c('draft con contexto')}).",f"Credencial filtrada: ({c('ignorar')} / {c('rotar y limpiar')}).",f"Review de endpoint: ({c('omitir seguridad')} / {c('verificar authz/validación')}).",f"Sincronizar con main: ({c('nunca')} / {c('periódicamente')}).",f"CI roto en main: ({c('mergear igual')} / {c('priorizar arreglo')})."],
  "ans":["1) acotado 2) draft 3) rotar y limpiar 4) verificar 5) periódicamente 6) priorizar"]},
 {"title":"Transformar: mejorar mensajes y flujo","inst":"Transforma.",
  "items":[f"{c('update stuff')} → mensaje convencional (validación email): {ln()}",f"Rama {c('test123')} → nombre para paginación: {ln()}",f"PR vacío → 3 elementos: {ln()}{ln()}",f"Commit gigante mixto → estrategia: {ln()}",f"Comentario agresivo → reformulación: {ln()}",f"Sin CI → pasos mínimos: {ln()}"],
  "ans":["1) fix(validation): reject invalid email format 2) feat/api-pagination 3) objetivo, cambios, cómo probar 4) separar en commits/PRs 5) sugerencia constructiva 6) lint,typecheck,tests,build"]},
 {"title":"Reordenar/relacionar: ciclo de colaboración","inst":"Ordena o relaciona.",
  "items":[f"Feature: (a) rama (b) commits (c) PR (d) review (e) merge. → {ln()}",f"1)fetch 2)merge 3)rebase con A)integra B)actualiza refs C)reaplica. → {ln()}",f"Conflicto: (a) marcadores (b) editar (c) probar (d) add/continuar. → {ln()}",f"1)nit 2)bloqueante 3)sugerencia con A)opcional B)menor C)debe corregirse. → {ln()}",f"Antes merge: (a) CI (b) aprobaciones (c) actualizada (d) sin secretos. → {ln()}",f"1).gitignore 2)CODEOWNERS 3)PR template con A)revisores B)exclusiones C)guía. → {ln()}"],
  "ans":["1) a,b,c,d,e 2) 1-B,2-A,3-C 3) a,b,c,d 4) 1-B,2-C,3-A 5) a,b,c,d 6) 1-B,2-A,3-C"]},
 {"title":"Escenario: hotfix en API de facturación","inst":"Responde al escenario.","example":"Escenario: bug de cálculo de impuestos en producción; hay rama release y main con features. Se requiere hotfix rápido y trazable.",
  "items":[f"¿Desde qué rama crear hotfix y por qué? {ln()}",f"3 elementos del PR: {ln()}",f"Cómo llevar fix a main y release: {ln()}",f"Pruebas mínimas antes de merge: {ln()}",f"Riesgo a documentar: {ln()}",f"Acción post-merge clave: {ln()}"],
  "ans":["1) desde release/main según flujo, rama dedicada 2) causa,cambio,verificación 3) merge/cherry-pick a ambas 4) tests del módulo y regresión 5) impacto en montos 6) monitorear y validar"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Mensaje de commit para índice en orders(tenant_id,created_at): {ln()}{ln()}",f"Checklist 4 puntos para PR backend: {ln()}{ln()}{ln()}",f"Convención de ramas (3 tipos): {ln()}{ln()}"],
  "ans":["1) perf(db): add index on orders(tenant_id, created_at) 2) correctitud,tests,seguridad,errores/migraciones 3) feat/, fix/, chore/"]
  }
]
}

u6 = {
"n":6,"title":"React 18: componentes, props, estado y composición",
"context":"React permite construir interfaces declarativas a partir de componentes reutilizables. Entender props, estado, renderizado y composición es clave para crear UIs predecibles y fáciles de mantener. Esta unidad practica patrones básicos de React 18 aplicables a aplicaciones con Next.js y productos SaaS.",
"exercises":[
 {"title":"Completar: fundamentos de componentes","inst":"Completa con el concepto correcto.","example":"Ejemplo: Los datos de padre a hijo se pasan mediante props.",
  "items":[f"Un componente funcional es una {b('md')} que retorna JSX.",f"Estado local se gestiona con {b('md')}.",f"JSX requiere un único raíz o {b('md')}.",f"Listas con {c('map')} requieren prop {b('sm')} estable.",f"Eventos se nombran en {b('md')} (ej. onClick).",f"La UI es función del {b('md')} y las props."],
  "ans":["1) función 2) useState 3) Fragment 4) key 5) camelCase 6) estado"]},
 {"title":"Completar: props, estado y flujo","inst":"Completa los conceptos.",
  "items":[f"Elevar estado: moverlo al ancestro {b('md')}.",f"Props son de solo lectura; el hijo notifica con {b('lg')}.",f"Estado derivado innecesario causa {b('md')} de sincronización.",f"Inicializar desde props una vez puede ignorar cambios si no se {b('md')}.",f"Renderizado condicional: ternario o {c('&&')} con cuidado en {b('md')}.",f"Inputs controlados vinculan valor al {b('md')}."],
  "ans":["1) común 2) callbacks 3) errores 4) sincroniza/diseña 5) valores falsy 6) estado"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Mutar props dentro del hijo. → {ln()}",f"Usar índice como key en lista que se reordena. → {ln()}",f"{c('setCount(c => c + 1)')} para actualizar desde valor previo. → {ln()}",f"Llamar hooks dentro de condicionales/bucles. → {ln()}",f"Guardar en estado valores calculables sin necesidad. → {ln()}",f"Dividir UI en componentes pequeños y claros. → {ln()}"],
  "ans":["a) Error b) Error/riesgo c) Correcto d) Error e) Error/mala práctica f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Mostrar si isOpen: ({c('{isOpen && <Panel/>}')} / {c('{isOpen = <Panel/>}')}).",f"Update fiable: ({c('setN(n+1)')} / {c('setN(n=>n+1)')}).",f"Input controlado: ({c('value+onChange')} / {c('solo defaultValue')} cuando necesitas estado).",f"Datos a nieto profundo: ({c('prop drilling')} / {c('siempre global inmediato')}) considerar composición/contexto.",f"Fragmento sin nodo extra: ({c('<>...</>')} / {c('<div>')} siempre).",f"Submit: ({c('onSubmit + preventDefault')} / {c('onClick sin semántica')})."],
  "ans":["1) {isOpen && <Panel/>} 2) funcional 3) value+onChange 4) prop drilling 5) Fragment 6) onSubmit"]},
 {"title":"Elegir/decisión de composición","inst":"Selecciona la mejor decisión.",
  "items":[f"Componente grande: ({c('dividir')} / {c('dejar crecer')}).",f"Estado compartido por hermanos: ({c('elevar')} / {c('duplicar')}).",f"Lógica reutilizable: ({c('componente/hook')} / {c('copiar')}).",f"Lista grande con renders costosos: ({c('ignorar')} / {c('optimizar/memo/virtualizar')}).",f"Nombre de componente: ({c('PascalCase')} / {c('camelCase')}).",f"Datos remotos: ({c('loading/error/empty')} / {c('asumir éxito')})."],
  "ans":["1) dividir 2) elevar 3) componente/hook 4) optimizar 5) PascalCase 6) manejar estados"]},
 {"title":"Transformar: mejorar componentes","inst":"Transforma.",
  "items":[f"Mutación de prop {c('props.user.name=\"x\"')} → {ln()}",f"Lista sin key: añade key estable: {ln()}",f"{c('setC(c+1); setC(c+1);')} → versión segura: {ln()}",f"Input controlado para email (value/handler): {ln()}{ln()}",f"Firma simple de {c('PrimaryButton')}: {ln()}",f"{c('count && <Badge/>')} con count 0 → alternativa: {ln()}"],
  "ans":["1) no mutar; usar callback/estado 2) key={i.id} 3) setC(c=>c+1) dos veces 4) value={email} onChange 5) function PrimaryButton({children,onClick}) 6) count>0 && <Badge/>"]},
 {"title":"Reordenar/relacionar: render y datos","inst":"Ordena o relaciona.",
  "items":[f"Actualización: (a) evento (b) setState (c) re-render (d) UI. → {ln()}",f"1)props 2)state 3)key con A)identidad B)entrada C)memoria. → {ln()}",f"Formulario: (a) estado (b) vincular (c) validar (d) enviar. → {ln()}",f"1)lifting 2)composición 3)controlado con A)combinables B)compartir C)input por React. → {ln()}",f"Depurar: (a) reproducir (b) inspeccionar (c) revisar keys (d) corregir. → {ln()}",f"1)key inestable 2)mutación 3)hook condicional con A)reconciliación B)estado incorrecto C)reglas hooks. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-C,3-A 3) a,b,c,d 4) 1-B,2-A,3-C 5) a,b,c,d 6) 1-A,2-B,3-C"]},
 {"title":"Escenario: pantalla de listado de pacientes","inst":"Responde al escenario.","example":"Escenario: pantalla clínica con búsqueda, filtro por estado y paginación; se requiere manejo claro de carga, vacío y componentes mantenibles.",
  "items":[f"Estados mínimos además de datos: {ln()}",f"Dónde ubicar estado de búsqueda/filtro: {ln()}",f"Key para cada fila: {ln()}",f"Mala práctica que causa lag al tipear: {ln()}",f"Cómo mostrar 'sin resultados': {ln()}",f"División en 3 componentes: {ln()}"],
  "ans":["1) loading,error,empty 2) ancestro común 3) id estable 4) trabajo pesado en render 5) estado vacío claro 6) SearchBar, PatientList, Pagination"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Componente {c('Greeting({name})')}: {ln()}{ln()}{ln()}",f"Contador con +1/-1 usando forma funcional: {ln()}{ln()}{ln()}",f"3 reglas para componentes mantenibles: {ln()}{ln()}"],
  "ans":["1) function Greeting({name}){return <p>Hola {name}</p>} 2) useState y setC(v=>v±1) 3) componentes pequeños, keys estables, estado mínimo"]
  }
]
}

for u in [u4,u5,u6]:
    frag = render_unit_html(u); ans = render_ans(u)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}_ans.html"),"w",encoding="utf-8").write(ans)
    print(u['n'], len(frag), len(ans))
