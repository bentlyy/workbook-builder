# -*- coding: utf-8 -*-
import os, html
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

u8 = {
"n":8,"title":"Next.js App Router: rutas, Server/Client Components y datos",
"context":"Next.js con App Router introduce un modelo donde el servidor es el entorno por defecto para componentes, datos y composición de rutas. Entender la diferencia entre Server y Client Components, el sistema de archivos como enrutador, los layouts y las estrategias de carga/caché permite construir aplicaciones rápidas, seguras y con buena experiencia de usuario. Esta unidad practica decisiones de arquitectura en App Router, manejo de estados de carga/error y obtención de datos.",
"exercises":[
 {"title":"Completar: fundamentos de App Router","inst":"Completa con el concepto correcto.","example":"Ejemplo: En App Router, la carpeta <code>app/</code> define el árbol de rutas mediante segmentos de carpeta.",
  "items":[
   f"Un archivo {c('page.tsx')} dentro de un segmento define la {b('md')} de esa ruta.",
   f"Un archivo {c('layout.tsx')} permite compartir UI y estado de layout entre rutas {b('md')}.",
   f"Los componentes son {b('md')} Components por defecto, lo que permite acceder a recursos del servidor sin exponer secretos al cliente.",
   f"Para usar hooks de estado/efecto o APIs del navegador debo marcar el componente con {b('xl')} al inicio del archivo.",
   f"Los archivos {c('loading.tsx')} y {c('error.tsx')} permiten manejar estados de {b('md')} y {b('md')} por segmento.",
   f"Las rutas dinámicas se definen con carpetas como {b('md')} (ejemplo de parámetro id)."],
  "ans":["1) UI/página 2) anidadas/hijas 3) Server 4) \"use client\" 5) carga / error 6) [id]"]},
 {"title":"Completar: datos, caché y composición","inst":"Completa los conceptos.",
  "items":[
   f"En Server Components puedo realizar {c('fetch')} directamente y mantener {b('lg')} en el servidor.",
   f"Para datos que deben ser siempre actuales puedo usar opciones como {c("cache: 'no-store'")} o estrategias de {b('md')}.",
   f"Un Client Component puede recibir datos desde un Server Component a través de {b('md')}.",
   f"La directiva {c('"use client"')} crea un límite: los módulos importados ahí pasan a formar parte del bundle del {b('md')}.",
   f"Para mutaciones y lógica de formulario en App Router pueden usarse {b('lg')} (Server Actions) según el caso.",
   f"Separar componentes de presentación (cliente) de obtención de datos (servidor) mejora {b('md')} y seguridad."],
  "ans":["1) secretos/credenciales 2) revalidación 3) props 4) cliente 5) Server Actions 6) rendimiento"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Usar {c('useState')} en un componente sin {c(chr(34)+'use client'+chr(34))}. → {ln()}",f"Acceder a {c('process.env.SECRET_KEY')} en un Server Component para llamar a un servicio interno. → {ln()}",f"Marcar toda la aplicación como {c(chr(34)+'use client'+chr(34))} por defecto sin necesidad. → {ln()}",f"Colocar {c('loading.tsx')} en un segmento para mostrar UI de carga mientras se resuelve la página. → {ln()}",f"Importar un Server Component dentro de un Client Component directamente como hijo pasado por composición no es posible en todos los patrones; lo correcto es diseñar la composición desde el servidor cuando se requiere. → {ln()}",f"Hacer fetch de datos sensibles con tokens privados en el cliente cuando puede hacerse en el servidor. → {ln()}"],
  "ans":["a) Error b) Correcto c) Error/mala práctica d) Correcto e) Correcto (consideración de diseño) f) Error"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Componente que solo muestra datos ya obtenidos y no usa hooks de navegador: ({c('Server')} / {c('Client')}) por defecto.",f"Componente con {c('onClick')} y estado local: ({c('Server')} / {c('Client')}).",f"Archivo que define UI compartida para /dashboard y subrutas: ({c('page.tsx')} / {c('layout.tsx')}).",f"Ruta para detalle /products/42: carpeta ({c('products/[id]/page.tsx')} / {c('products/id/page.tsx')}).",f"Datos que cambian en cada request: ({c('cache por defecto siempre')} / {c('no-store o revalidación adecuada')}).",f"Para manejar error de render/datos en un segmento: ({c('error.tsx')} / {c('style.css')})."],
  "ans":["1) Server 2) Client 3) layout.tsx 4) products/[id]/page.tsx 5) no-store/revalidación 6) error.tsx"]},
 {"title":"Elegir/decisión de arquitectura","inst":"Selecciona la mejor decisión.",
  "items":[f"Formulario interactivo complejo: ({c('Client Component')} / {c('solo Server sin interactividad')}).",f"Consulta a DB con credenciales: ({c('Server Component/acción/route handler')} / {c('Client Component')}).",f"Minimizar JS enviado al navegador: ({c('mantener lógica en servidor cuando sea posible')} / {c('convertir todo a cliente')}).",f"UI de skeleton mientras carga: ({c('loading.tsx o Suspense')} / {c('bloquear sin feedback')}).",f"Componente de botón reutilizable con onClick: ({c('Client')} / {c('Server')}).",f"Página de marketing mayormente estática: ({c('aprovechar renderizado en servidor/cache')} / {c('forzar todo dinámico sin razón')})."],
  "ans":["1) Client Component 2) Server 3) mantener en servidor 4) loading/Suspense 5) Client 6) aprovechar servidor/cache"]},
 {"title":"Transformar: adaptar a App Router","inst":"Transforma según se indique.",
  "items":[f"Componente con estado necesita interactividad: añade directiva → {ln()}",f"Mover fetch de datos desde {c('useEffect')} en cliente a carga en Server Component (describe cambio): {ln()}{ln()}",f"Estructura de archivos para /settings/profile: {ln()}",f"Página dinámica de orden {c('/orders/[orderId]')}: firma de acceso a params (conceptual): {ln()}",f"Separar botón interactivo de una página server: crear {c('SubmitButton.tsx')} con {ln()}","Reemplazar spinner global por {c('loading.tsx')} en segmento dashboard: indica ubicación → {ln()}"],
  "ans":["1) \"use client\" 2) fetch async en server component y pasar props 3) app/settings/profile/page.tsx (+ layout si aplica) 4) recibir params/orderId según API de Next 5) \"use client\" y onClick 6) app/dashboard/loading.tsx"]},
 {"title":"Reordenar/relacionar: composición y datos","inst":"Ordena o relaciona.",
  "items":[f"Render de ruta: (a) resolver layout(s) (b) ejecutar server components/fetch (c) enviar HTML/RSC (d) hidratar client components). → {ln()}",f"1)layout.tsx 2)page.tsx 3)loading.tsx 4)error.tsx con A)UI ruta B)marco compartido C)fallback carga D)manejo fallo. → {ln()}",f"Decisión Server/Client: (a) ¿necesita estado/efectos/browser? (b) ¿accede a secretos/DB? (c) elegir tipo (d) componer). → {ln()}",f"1)Server Component 2)Client Component 3)Server Action con A)interactividad B)mutación en servidor C)fetch/secretos. → {ln()}",f"Flujo de formulario: (a) validar (b) mutar en servidor (c) revalidar/actualizar UI (d) feedback). → {ln()}",f"1)[slug] 2)route.ts 3)middleware con A)segmento dinámico B)endpoint handler C)lógica previa a request. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-A,3-C,4-D 3) a,b,c,d 4) 1-C,2-A,3-B 5) a,b,c,d 6) 1-A,2-B,3-C"]},
 {"title":"Escenario: portal de administración de inventario","inst":"Responde al escenario.","example":"Escenario: construyes un portal en Next.js App Router para administrar inventario multi-sucursal. Listados y reportes leen datos sensibles; hay filtros interactivos, modales y formularios de edición.",
  "items":[f"¿Qué partes implementarías como Server Components y cuáles como Client? Da 2 ejemplos de cada uno. {ln()}{ln()}",f"¿Dónde realizarías la consulta de inventario con credenciales de DB? {ln()}",f"El listado tarda: ¿qué mecanismos de UX usas en App Router? {ln()}",f"Un filtro por texto debe responder al teclear: ¿implica cliente o servidor? Justifica. {ln()}",f"¿Cómo evitas exponer tokens de servicios internos al navegador? {ln()}",f"Propón estructura de segmentos para /inventory y /inventory/[sku]. {ln()}{ln()}"],
  "ans":["1) Server: página/listado inicial, layout; Client: filtros interactivos, modal edición 2) en servidor (Server Component/route handler/action) 3) loading.tsx/Suspense 4) interacción en cliente (estado UI) aunque datos puedan consultarse en servidor 5) mantener llamadas y secretos en servidor 6) app/inventory/page.tsx y app/inventory/[sku]/page.tsx"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Esqueleto de {c('app/products/page.tsx')} como Server Component que haga fetch (pseudocódigo). {ln()}{ln()}{ln()}{ln()}",f"Esqueleto de {c('SearchBox')} Client Component con input controlado. {ln()}{ln()}{ln()}",f"3 reglas para decidir Server vs Client Component en tu equipo. {ln()}{ln()}{ln()}"],
  "ans":["1) export default async function Page(){const res=await fetch(...);const data=await res.json();return <List data={data}/>} 2) \"use client\"; useState para value/onChange 3) servidor por defecto, cliente solo si hay interactividad/browser APIs, secretos siempre en servidor"]
  }
]
}

# Due to space I'll create u9 and u10 in same file but abbreviated with rich content
u9 = {
"n":9,"title":"UI con Tailwind CSS, formularios y accesibilidad básica",
"context":"Una interfaz efectiva no solo se ve bien: también es legible, consistente, accesible y tolerante a errores de entrada. Tailwind CSS permite construir estilos de forma rápida con utilidades, pero requiere disciplina para mantener consistencia. Esta unidad practica composición de UI, estados de formulario, validación, retroalimentación visual y fundamentos de accesibilidad (a11y) en aplicaciones React/Next.js.",
"exercises":[
 {"title":"Completar: utilidades y layout con Tailwind","inst":"Completa con la clase o concepto correcto.","example":"Ejemplo: <code>flex</code> activa un contenedor flexbox y <code>gap-4</code> define separación entre hijos.",
  "items":[f"Para centrar contenido en un eje con flex uso {c('items-center')} y {c('justify-center')} según {b('md')}.",f"Clases responsive como {c('md:grid-cols-2')} aplican estilos desde el breakpoint {b('sm')}.",f"Para espaciado interno uso {c('p-4')} (padding) y externo {c('m-4')} ({b('md')}).",f"{c('text-sm')}, {c('font-medium')} y {c('text-gray-600')} controlan tipografía y {b('md')}.",f"Evitar duplicación masiva de cadenas largas puede lograrse con componentes o extracción de {b('lg')}.",f"Estados interactivos como hover/focus se expresan con prefijos {c('hover:')} y {b('sm')}:"],
  "ans":["1) eje 2) md 3) margin 4) color/estilo visual 5) clases/componentes reutilizables 6) focus"]},
 {"title":"Completar: formularios y feedback","inst":"Completa los conceptos.",
  "items":[f"Cada input debe tener una etiqueta asociada mediante {c('<label htmlFor>')} e {b('md')} del control.",f"Mensajes de error deben ser {b('md')} y estar vinculados al campo cuando sea posible.",f"Durante envío conviene deshabilitar el botón o mostrar estado {b('md')} para evitar duplicados.",f"Validación en cliente mejora UX pero la validación {b('md')} es obligatoria para seguridad.",f"Campos obligatorios deben indicarse visual y {b('md')} (no solo por color).",f"Usar tipos de input adecuados ({c('email')}, {c('number')}, {c('date')}) ayuda a la {b('md')} y UX móvil."],
  "ans":["1) id 2) claros 3) loading 4) en servidor 5) semánticamente/texto 6) validación nativa"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Usar solo color rojo para indicar error sin texto explicativo. → {ln()}",f"Botón de icono sin {c('aria-label')} ni texto accesible. → {ln()}",f"Asociar correctamente {c('label')} con {c('input')} mediante {c('htmlFor/id')}. → {ln()}",f"Permitir enviar formulario con campos requeridos vacíos sin validación. → {ln()}",f"Usar elementos semánticos como {c('<button>')} para acciones en lugar de {c('<div onClick>')}. → {ln()}",f"Orden de foco ilógico y navegación por teclado rota en un modal. → {ln()}"],
  "ans":["a) Error b) Error c) Correcto d) Error e) Correcto f) Error"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Para acción principal de formulario: ({c('<button type=\"submit\">')} / {c('<div>')} clickable).",f"Indicar campo inválido: ({c('borde rojo + mensaje')} / {c('solo borde rojo')}).",f"Texto alternativo en imagen informativa: ({c('alt descriptivo')} / {c('alt=\"\"')} siempre).",f"Agrupar campos relacionados: ({c('<fieldset>/<legend>')} / {c('divs sin relación')}).",f"Feedback tras guardar: ({c('mensaje de éxito o error visible')} / {c('nada')}).",f"Contraste de texto bajo: ({c('aceptable')} / {c('problema de accesibilidad')})."],
  "ans":["1) button submit 2) borde + mensaje 3) alt descriptivo 4) fieldset/legend 5) mensaje visible 6) problema de accesibilidad"]},
 {"title":"Elegir/decisión de UI","inst":"Selecciona la mejor decisión.",
  "items":[f"Consistencia visual: ({c('design tokens/clases reutilizables')} / {c('estilos ad-hoc por pantalla')}).",f"Formulario largo: ({c('agrupar en secciones/pasos')} / {c('todo en un bloque caótico')}).",f"Errores del servidor en formulario: ({c('mostrar resumen y por campo')} / {c('solo console.log')}).",f"Componente de tabla en móvil: ({c('considerar scroll/responsive')} / {c('romper layout')}).",f"Placeholder como única etiqueta: ({c('suficiente')} / {c('insuficiente; usar label')}).",f"Estados disabled/loading: ({c('visuales y accesibles')} / {c('solo opacidad sin semántica')})."],
  "ans":["1) reutilizables 2) agrupar 3) mostrar en UI 4) responsive 5) insuficiente 6) visuales y accesibles"]},
 {"title":"Transformar: mejorar markup y estilos","inst":"Transforma según se indique.",
  "items":[f"{c('<div onClick={save}>Guardar</div>')} → elemento semántico: {ln()}",f"Input sin label: añade label asociado a {c('email')}: {ln()}{ln()}",f"Clase larga repetida en 5 botones → estrategia de extracción: {ln()}",f"Mensaje de error genérico 'Error' → mensaje útil para email inválido: {ln()}",f"Layout de 1 a 2 columnas en md: clases Tailwind en contenedor grid: {ln()}",f"Agregar indicación de carga a botón submit: {ln()}"],
  "ans":["1) <button type='button' onClick={save}>Guardar</button> 2) <label htmlFor='email'>Email</label><input id='email'/> 3) componente Button o @apply/const clases 4) 'Ingresa un email válido' 5) grid grid-cols-1 md:grid-cols-2 gap-4 6) disabled/aria-busy y texto/spinner"]},
 {"title":"Reordenar/relacionar: formulario accesible","inst":"Ordena o relaciona.",
  "items":[f"Flujo de envío: (a) usuario completa (b) validar (c) enviar (d) mostrar resultado. → {ln()}",f"1)label 2)aria-describedby 3)fieldset con A)agrupa campos B)asocia texto ayuda/error C)nombre del control. → {ln()}",f"Diseño responsive: (a) base móvil (b) breakpoints (c) ajustar layout (d) probar). → {ln()}",f"1)contraste 2)foco visible 3)semántica con A)navegación teclado B)legibilidad C)estructura correcta. → {ln()}",f"Validación: (a) reglas cliente (b) feedback inmediato (c) validar servidor (d) manejar errores). → {ln()}",f"1)placeholder 2)helper text 3)error text con A)pista permanente B)ejemplo C)fallo específico. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-C,2-B,3-A 3) a,b,c,d 4) 1-B,2-A,3-C 5) a,b,c,d 6) 1-B,2-A,3-C"]},
 {"title":"Escenario: formulario de registro de técnicos","inst":"Responde al escenario.","example":"Escenario: formulario para registrar técnicos en un SaaS de talleres. Incluye nombre, email, teléfono, especialidad y aceptación de términos. Usuarios reportan errores confusos y dificultades con teclado.",
  "items":[f"Lista 3 requisitos de accesibilidad para este formulario. {ln()}{ln()}",f"¿Cómo mostrarías errores de validación por campo y generales? {ln()}{ln()}",f"¿Qué harías con el botón mientras se envía? {ln()}",f"Un usuario envía email inválido: escribe mensaje y dónde mostrarlo. {ln()}",f"¿Por qué no basta validar solo en cliente? {ln()}",f"Propón estructura de layout (secciones/columnas) para desktop y móvil. {ln()}{ln()}"],
  "ans":["1) labels, foco visible, mensajes accesibles/semántica 2) inline por campo + resumen superior si aplica 3) disabled + loading + aria-busy 4) mensaje claro junto al input email 5) seguridad/integridad en servidor 6) secciones agrupadas, 1 col móvil, 2 cols md cuando aplique"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Markup básico de un campo email con label, input y espacio para error. {ln()}{ln()}{ln()}{ln()}",f"Clases Tailwind para un contenedor de tarjeta (padding, borde, sombra suave, radio). {ln()}",f"3 prácticas de accesibilidad que aplicarás por defecto en formularios. {ln()}{ln()}{ln()}"],
  "ans":["1) div>label+input+small error 2) ej. p-4 border rounded-lg shadow-sm bg-white 3) labels, errores claros, teclado/semántica, contraste"]
  }
]
}

u10 = {
"n":10,"title":"Integración cliente-API y gestión de estado remoto",
"context":"Consumir APIs desde el frontend implica más que hacer una petición: requiere manejar latencia, errores, estados vacíos, reintentos y coherencia de datos. Una buena integración mejora la experiencia de usuario y reduce inconsistencias. Esta unidad practica patrones de fetching, manejo de estados, sincronización básica y decisiones para comunicar el cliente con servicios REST de forma resiliente.",
"exercises":[
 {"title":"Completar: estados y ciclo de petición","inst":"Completa con el concepto correcto.","example":"Ejemplo: Una petición típica pasa por estados como idle/loading/success/error.",
  "items":[f"Antes de recibir respuesta, la UI debería reflejar estado {b('md')}.",f"Si la respuesta es exitosa pero sin datos, se debe manejar el estado {b('md')}.",f"Ante fallo de red o 5xx, la UI debe mostrar un estado de {b('md')} con opción de {b('md')}.",f"Cancelar o ignorar respuestas obsoletas evita condiciones de {b('md')} al cambiar filtros rápido.",f"Guardar en cache respuestas puede reducir latencia pero requiere estrategia de {b('md')}.",f"Mostrar datos parciales puede ser preferible a bloquear toda la pantalla cuando una fuente {b('md')}."],
  "ans":["1) loading 2) vacío/empty 3) error / reintentar 4) carrera 5) invalidación/revalidación 6) falla"]},
 {"title":"Completar: fetch, errores y contratos","inst":"Completa los conceptos.",
  "items":[f"{c('fetch')} no rechaza por códigos HTTP 4xx/5xx; hay que verificar {b('md')} o el status.",f"Parsear JSON de una respuesta vacía o inválida puede lanzar {b('md')}.",f"Enviar credenciales/cookies requiere configuración adecuada ({b('md')}) según el caso.",f"Los timeouts y abortos pueden implementarse con {b('lg')}.",f"Normalizar errores de API a un formato interno facilita el {b('md')} en la UI.",f"Reintentar automáticamente tiene sentido en fallos {b('md')}, no en errores de validación."],
  "ans":["1) response.ok 2) excepción 3) credentials 4) AbortController 5) manejo consistente 6) transitorios"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Asumir que {c('await fetch(url)')} lanza error en 404. → {ln()}",f"Mostrar spinner infinito sin manejar error ni timeout. → {ln()}",f"Validar y tipar la respuesta antes de usarla en la UI. → {ln()}",f"Disparar múltiples peticiones idénticas en cada render sin control. → {ln()}",f"Mostrar mensaje genérico útil y registrar detalle técnico en logs/monitoring. → {ln()}",f"Actualizar estado con respuesta de una petición antigua después de que el usuario cambió el filtro. → {ln()}"],
  "ans":["a) Error b) Error c) Correcto d) Error e) Correcto f) Error"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Para detectar 500: ({c('try/catch solamente')} / {c('verificar status/ok')} además).",f"Búsqueda con tipeo rápido: ({c('debounce/cancelación')} / {c('petición por tecla sin control')}).",f"Error 400 por input: ({c('reintentar automáticamente')} / {c('corregir input y mostrar feedback')}).",f"Datos compartidos en varias vistas: ({c('cache/estado remoto centralizado')} / {c('duplicar fetches inconsistentes')}).",f"Lista vacía tras filtro: ({c('estado empty con mensaje')} / {c('tabla rota')}).",f"Operación de guardado: ({c('optimistic UI con cuidado')} / {c('sin feedback')} según riesgo)."],
  "ans":["1) verificar status/ok 2) debounce/cancelación 3) corregir input 4) cache/estado remoto 5) estado empty 6) feedback/optimistic con cuidado"]},
 {"title":"Elegir/decisión de resiliencia","inst":"Selecciona la mejor decisión.",
  "items":[f"Timeout de API lenta: ({c('esperar forever')} / {c('límite + mensaje/reintento')}).",f"Reintentos: ({c('solo transitorios con backoff')} / {c('para 400 siempre')}).",f"Exponer detalle interno al usuario final: ({c('evitar')} / {c('mostrar stack trace')}).",f"Sincronización tras mutación: ({c('invalidar/re-fetch')} / {c('esperar que se actualice solo')}).",f"Indicador de carga: ({c('por sección cuando aplique')} / {c('bloqueo total innecesario')}).",f"Paginación remota: ({c('pedir páginas/cursores')} / {c('traer todo siempre')})."],
  "ans":["1) límite 2) solo transitorios 3) evitar 4) invalidar/re-fetch 5) por sección 6) páginas/cursores"]},
 {"title":"Transformar: mejorar integración con API","inst":"Transforma según se indique.",
  "items":[f"Fetch sin chequeo de estado → añade verificación: {ln()}{ln()}",f"UI sin manejo de error → define estados {c('data,loading,error')}: {ln()}",f"Peticiones en cada tecla → estrategia con debounce/abort: {ln()}{ln()}",f"Error técnico crudo al usuario → mensaje amigable + logging: {ln()}{ln()}",f"Actualización tras POST sin refrescar datos → acción: {ln()}",f"Cliente confía en respuesta sin validar → mejora: {ln()}"],
  "ans":["1) if(!res.ok) throw... 2) useState/useReducer con 3 estados 3) debounce y AbortController 4) mensaje claro UI y log técnico 5) revalidar/refetch/invalidate 6) validar esquema/tipos"]},
 {"title":"Reordenar/relacionar: flujo de datos remoto","inst":"Ordena o relaciona.",
  "items":[f"Petición: (a) iniciar loading (b) request (c) éxito/error (d) actualizar UI. → {ln()}",f"1)200 2)401 3)500 con A)éxito B)auth requerida C)fallo servidor. → {ln()}",f"Búsqueda: (a) input usuario (b) debounce (c) fetch (d) render resultados). → {ln()}",f"1)retry 2)cache 3)abort con A)cancelar B)reintentar C)reutilizar. → {ln()}",f"Mutación: (a) enviar (b) manejar respuesta (c) invalidar datos (d) feedback). → {ln()}",f"1)loading 2)empty 3)error con A)sin datos B)fallo C)espera. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-A,2-B,3-C 3) a,b,c,d 4) 1-B,2-C,3-A 5) a,b,c,d 6) 1-C,2-A,3-B"]},
 {"title":"Escenario: buscador de repuestos con filtros","inst":"Responde al escenario.","example":"Escenario: interfaz React/Next que consulta /parts con filtros por categoría, stock y texto. La red es inestable en sucursales y los usuarios cambian filtros rápidamente.",
  "items":[f"¿Qué estados de UI necesitas por consulta? {ln()}",f"Estrategia para evitar respuestas fuera de orden: {ln()}",f"Cómo manejar 500 intermitente vs 400 por filtro inválido: {ln()}{ln()}",f"¿Cuándo usarías cache/revalidación? {ln()}",f"Qué feedback dar al guardar un filtro favorito (mutación): {ln()}",f"2 métricas/observaciones útiles para detectar problemas de integración: {ln()}{ln()}"],
  "ans":["1) loading,success,empty,error 2) abortar o descartar obsoletas 3) reintento/backoff en 500; corregir y mostrar error en 400 4) datos poco cambiantes o reutilizados 5) éxito/error/loading y consistencia 6) tasa de errores, latencia/timeouts"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Función {c('fetchJson')} que lance error si {c('!res.ok')} y retorne JSON. {ln()}{ln()}{ln()}",f"Esquema de estado para hook de búsqueda: {ln()}{ln()}",f"3 buenas prácticas para consumir APIs desde el frontend. {ln()}{ln()}{ln()}"],
  "ans":["1) async function fetchJson(u){const r=await fetch(u); if(!r.ok) throw new Error(r.status); return r.json()} 2) {data,loading,error,query} 3) manejar estados, validar/chequear status, abortar/debounce, reintentos transitorios"]
  }
]
}

for u in [u8,u9,u10]:
    frag = render_unit_html(u); ans = render_ans(u)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}_ans.html"),"w",encoding="utf-8").write(ans)
    print(u['n'], len(frag), len(ans), len(frag)+len(ans))
