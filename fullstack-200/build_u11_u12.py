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

u11 = {
"n":11,"title":"Node.js, Express y arquitectura de API",
"context":"El backend concentra reglas de negocio, acceso a datos y políticas de seguridad, por lo que su estructura impacta en la mantenibilidad. Node.js con Express permite construir APIs rápidamente, pero requiere disciplina en capas, middlewares, configuración y manejo asíncrono. Esta unidad practica organización de proyectos, routing, middlewares, variables de entorno y patrones para servicios claros y escalables.",
"exercises":[
 {"title":"Completar: fundamentos de Express y middlewares","inst":"Completa con el concepto correcto.","example":"Ejemplo: Un middleware recibe req, res y next.",
  "items":[f"Para escuchar puerto uso {c('app.listen')} con el valor leído de {b('lg')}.",f"{c('express.json()')} parsea el cuerpo {b('md')} entrante.",f"Un middleware que no responde debe llamar a {b('sm')} para continuar.",f"El orden de middlewares es {b('md')} y afecta el resultado.",f"Un router modular se monta con {c('app.use')} para agrupar {b('md')}.",f"Manejador de errores en Express tiene firma {b('xl')}."],
  "ans":["1) process.env/PORT 2) JSON 3) next() 4) secuencial 5) rutas 6) (err,req,res,next)"]},
 {"title":"Completar: configuración y estructura","inst":"Completa los conceptos.",
  "items":[f"Configuración sensible se lee de {b('lg')} y se valida al inicio.",f"Separar rutas/controladores/servicios/repositorios mejora {b('md')}.",f"Lógica de negocio pertenece a la capa de {b('md')}.",f"Validación de entrada se realiza en el {b('md')} de la API.",f"Abstraer dependencias facilita {b('md')} automatizado.",f"Endpoint de salud permite verificar el estado del {b('md')}."],
  "ans":["1) variables de entorno 2) mantenibilidad 3) servicios 4) borde 5) testing 6) servicio"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Poner lógica compleja y SQL directo en el handler sin capas. → {ln()}",f"Olvidar {c('next()')} en middleware que no responde puede colgar la petición. → {ln()}",f"Usar try/catch o wrapper async para pasar errores a {c('next(err)')}. → {ln()}",f"Exponer stack traces al cliente en producción. → {ln()}",f"Centralizar manejo de errores en middleware final. → {ln()}",f"Hardcodear secretos en el repositorio. → {ln()}"],
  "ans":["a) Mala práctica b) Correcto c) Correcto d) Error e) Correcto f) Error"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Ruta para usuario 5: ({c('app.get(\"/users/:id\")')} / {c('app.fetch')} ).",f"Middleware global: ({c('app.use(mw)')} / {c('app.only')} ).",f"Responder JSON: ({c('res.json(obj)')} / {c('res.file')} ).",f"Crear recurso: ({c('res.status(201).json')} / {c('404')} ).",f"Entorno: ({c('process.env.NODE_ENV')} / {c('hardcode')} ).",f"Ruta inexistente: ({c('middleware 404')} / {c('ignorar')} )."],
  "ans":["1) app.get 2) app.use 3) res.json 4) 201 5) process.env 6) middleware 404"]},
 {"title":"Elegir/decisión de arquitectura","inst":"Selecciona la mejor decisión.",
  "items":[f"Muchos endpoints: ({c('routers por dominio')} / {c('archivo único')} ).",f"Acceso a datos: ({c('repositorio')} / {c('queries en handlers')} ).",f"Errores: ({c('tipados/consistentes')} / {c('strings aleatorios')} ).",f"Env: ({c('validar al inicio')} / {c('fallar tarde')} ).",f"Logging: ({c('estructurado con contexto')} / {c('sin contexto')} ).",f"CORS: ({c('orígenes permitidos')} / {c('* con credenciales sin control')} )."],
  "ans":["1) routers por dominio 2) repositorio 3) tipados 4) validar al inicio 5) estructurado 6) orígenes permitidos"]},
 {"title":"Transformar: refactorizar handler","inst":"Transforma según se indique.","pre":"app.get('/orders', async (req,res)=>{\n  const data = await db.query('SELECT * FROM orders');\n  res.send(data);\n});",
  "items":[f"Extrae a {c('orderService.list()')}: {ln()}{ln()}",f"Añade manejo de error async: {ln()}{ln()}",f"Responde con status y json: {ln()}",f"Añade paginación (params): {ln()}",f"Indica dónde validar input: {ln()}",f"Separa en router dedicado (concepto): {ln()}"],
  "ans":["1) controller llama service 2) try/catch next(err) 3) res.status(200).json(data) 4) page,limit 5) middleware/validador 6) Router + app.use"]},
 {"title":"Reordenar/relacionar: pipeline de request","inst":"Ordena o relaciona.",
  "items":[f"Pipeline: (a) request (b) middlewares (c) handler (d) respuesta/error. → {ln()}",f"1)req 2)res 3)next con A)continuar B)entrada C)salida. → {ln()}",f"Estructura: (a) routes (b) controllers (c) services (d) repos. → {ln()}",f"1)auth 2)validador 3)handler con A)orquesta B)identidad C)input. → {ln()}",f"Arranque: (a) env (b) DB (c) rutas (d) listen. → {ln()}",f"1)404 2)500 3)400 con A)inválido B)no ruta C)interno. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-C,3-A 3) a,b,c,d 4) 1-B,2-C,3-A 5) a,b,c,d 6) 1-B,2-C,3-A"]},
 {"title":"Escenario: API de inventario de taller","inst":"Responde al escenario.","example":"Escenario: API Express para repuestos, proveedores y stock; crecerá en módulos y equipo.",
  "items":[f"Estructura de carpetas por capas (4): {ln()}{ln()}",f"¿Dónde validar body de creación? {ln()}",f"Cómo propagar errores async al handler: {ln()}",f"3 variables de entorno al iniciar: {ln()}",f"Endpoint de health check: {ln()}",f"Riesgo de un solo archivo grande: {ln()}"],
  "ans":["1) routes,controllers,services,repositories 2) middleware 3) try/catch next o wrapper 4) PORT,DATABASE_URL,NODE_ENV 5) GET /health 200 6) acoplamiento y baja mantenibilidad"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Middleware de logging (método, url): {ln()}{ln()}",f"Error handler central (firma y 500 seguro): {ln()}{ln()}{ln()}",f"3 buenas prácticas para Express mantenible: {ln()}{ln()}"],
  "ans":["1) log y next() 2) (err,req,res,next)=>res.status(500).json({error:{code:'INTERNAL'}}) 3) capas, validación, manejo errores, config env"]
  }
]
}

u12 = {
"n":12,"title":"Validación de datos, manejo de errores y contratos (Zod)",
"context":"Los bordes de la API son la principal defensa contra datos inválidos o maliciosos. Validar entradas, tipar contratos y unificar respuestas de error mejora confiabilidad y experiencia del consumidor. Esta unidad practica validación con esquemas (Zod), parseo seguro, errores de dominio y patrones de respuesta consistentes en servicios Node.js/TypeScript.",
"exercises":[
 {"title":"Completar: validación y esquemas","inst":"Completa con el concepto correcto.","example":"Ejemplo: Validar en servidor es obligatorio aunque el cliente valide.",
  "items":[f"Validación en {b('md')} es obligatoria; en cliente mejora {b('md')}.",f"Un esquema Zod define forma y {b('md')} esperados.",f"{c('parse')} lanza; {c('safeParse')} retorna {b('md')}.",f"Errores de validación se responden con {b('sm')} y detalles.",f"Coerción debe usarse con {b('md')} explícito.",f"Validar params, query y body evita supuestos {b('md')}."],
  "ans":["1) servidor/UX 2) tipos 3) success/error 4) 400/422 5) cuidado 6) incorrectos"]},
 {"title":"Completar: errores y respuestas","inst":"Completa los conceptos.",
  "items":[f"Error consistente incluye {c('code')}, {c('message')} y {b('md')}.",f"Diferenciar errores operacionales de bugs guía la {b('lg')}.",f"No exponer stacks en producción protege {b('md')}.",f"Errores de negocio usan códigos de {b('md')} claros.",f"Middleware central evita duplicar {b('md')} de error.",f"Contratos tipados reducen fallos de {b('md')}."],
  "ans":["1) details 2) respuesta/logging 3) seguridad 4) dominio 5) manejo 6) integración"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[f"Confiar en validación solo del frontend. → {ln()}",f"Usar {c('safeParse')} para controlar errores. → {ln()}",f"Responder 200 cuando la validación falla. → {ln()}",f"Registrar contexto y devolver mensaje seguro. → {ln()}",f"Exponer stack trace al cliente en producción. → {ln()}",f"Validar formato y rangos en el esquema. → {ln()}"],
  "ans":["a) Error b) Correcto c) Error d) Correcto e) Error f) Correcto"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[f"Email válido: ({c('z.string().email()')} / {c('z.any()')} ).",f"Edad int >=18: ({c('z.number().int().min(18)')} / {c('z.string()')} ).",f"Opcional: ({c('.optional()')} / {c('.never()')} ).",f"Entrada desconocida: ({c('z.unknown()')} / {c('z.any()')} ).",f"Enum rol: ({c('z.enum([\"admin\",\"user\"])')} / {c('z.number()')} ).",f"Objeto: ({c('z.object({...})')} / {c('z.array()')} )."],
  "ans":["1) z.string().email() 2) int().min(18) 3) optional 4) unknown 5) enum 6) object"]},
 {"title":"Elegir/decisión de manejo de errores","inst":"Selecciona la mejor decisión.",
  "items":[f"Validación fallida: ({c('400/422')} / {c('500')} ).",f"No encontrado: ({c('404')} / {c('400')} ).",f"Duplicado único: ({c('409')} / {c('200')} ).",f"Bug inesperado: ({c('log + 500 seguro')} / {c('stack al cliente')} ).",f"Mensajes: ({c('claros')} / {c('crípticos')} ).",f"Formato de error: ({c('consistente')} / {c('variable')} )."],
  "ans":["1) 400/422 2) 404 3) 409 4) log+500 seguro 5) claros 6) consistente"]},
 {"title":"Transformar: añadir validación y errores","inst":"Transforma según se indique.",
  "items":[f"{c('const {email}=req.body')} sin validar → con Zod safeParse: {ln()}{ln()}",f"Error string → {c('{code,message,details}')}: {ln()}",f"Catch que oculta error → manejo correcto: {ln()}",f"page string → número con default: {ln()}",f"DTO any → tipo inferido de esquema: {ln()}",f"Respuesta inconsistente → formato estándar: {ln()}"],
  "ans":["1) schema.safeParse(req.body) 2) objeto error estructurado 3) log y next/respuesta 4) z.coerce.number().default(1) 5) z.infer<typeof schema> 6) contrato común"]},
 {"title":"Reordenar/relacionar: flujo de validación","inst":"Ordena o relaciona.",
  "items":[f"Entrada: (a) recibir (b) validar (c) lógica (d) responder. → {ln()}",f"1)parse 2)safeParse 3)refine con A)custom B)lanza C)resultado. → {ln()}",f"Error: (a) detectar (b) mapear status (c) formatear (d) log. → {ln()}",f"1)body 2)query 3)params con A)ruta B)payload C)filtros. → {ln()}",f"Capas: (a) schema (b) controller (c) service (d) repo. → {ln()}",f"1)400 2)404 3)409 con A)conflicto B)no encontrado C)inválido. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-C,3-A 3) a,b,c,d 4) 1-B,2-C,3-A 5) a,b,c,d 6) 1-C,2-B,3-A"]},
 {"title":"Escenario: alta de órdenes en e-commerce B2B","inst":"Responde al escenario.","example":"Escenario: POST /orders recibe items, cantidades, dirección y tenant. Fallos: cantidades negativas, SKU inexistente, tenant no autorizado, payload mal formado.",
  "items":[f"3 validaciones de esquema: {ln()}{ln()}",f"Diferencia validación vs no encontrado (status): {ln()}",f"SKU inexistente: status/code posible: {ln()}",f"Dónde verificar tenant del token vs recurso: {ln()}",f"Formato de error con detalles por campo: {ln()}{ln()}",f"Qué loguear en fallo 500: {ln()}"],
  "ans":["1) items no vacío, qty>0, dirección requerida 2) 400/422 vs 404 3) 404 o 422 negocio 4) capa authz/servicio 5) details por campo 6) requestId, ruta, contexto sin secretos"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[f"Esquema Zod CreateUser (email,password>=8,role enum): {ln()}{ln()}{ln()}",f"Helper validate(schema,data) con safeParse: {ln()}{ln()}",f"3 reglas de respuestas de error: {ln()}{ln()}"],
  "ans":["1) z.object({email:z.string().email(),password:z.string().min(8),role:z.enum(['admin','user'])}) 2) retorna ok/data o ok false/errors 3) consistentes, seguras, códigos claros"]
  }
]
}

for u in [u11,u12]:
    frag = render_unit_html(u); ans = render_ans(u)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}_ans.html"),"w",encoding="utf-8").write(ans)
    print(u['n'], len(frag), len(ans))
