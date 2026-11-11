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
    out=[]
    out.append(f'<section class="unit" id="u{u["n"]}">')
    out.append(f'<h2>Unidad {u["n"]}. {e(u["title"])}</h2>')
    out.append(f'<p class="context">{e(u["context"])}</p>')
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
        ans = ex.get("ans",[])
        if isinstance(ans,list): ans = " ".join(str(a) for a in ans)
        out.append(f'<p><strong>Ej. {i}:</strong> {e(ans)}</p>')
    return "\n".join(out)

u2 = {
"n":2,
"title":"TypeScript esencial: tipos, uniones y narrowing",
"context":"TypeScript añade un sistema de tipos estático sobre JavaScript que ayuda a detectar errores antes de ejecutar el código y a documentar contratos entre módulos. Comprender tipos primitivos, uniones, interfaces, genéricos básicos y narrowing te permite modelar datos reales de APIs y UI con mayor seguridad. Esta unidad practica anotaciones, inferencia, refinamiento de tipos y decisiones de modelado habituales en proyectos Node.js y React.",
"exercises":[
 {"title":"Completar: tipos básicos e inferencia","inst":"Completa con el tipo o concepto correcto.",
  "example":f"Ejemplo: Una variable que puede ser cadena o número se modela con una unión como {c('string | number')}.",
  "items":[
   f"El tipo que desactiva la verificación efectiva y debe evitarse es {b('sm')}, mientras que {b('sm')} obliga a comprobar el valor antes de usarlo.",
   f"Para un arreglo de números anoto {c('number[]')} o {b('lg')}.",
   f"Una tupla de {c('[id, activo]')} con id string y activo boolean se escribe {b('xl')}.",
   f"TypeScript puede deducir el tipo sin anotarlo explícito; esto se llama {b('md')}.",
   f"El tipo de retorno que indica que una función nunca devuelve normalmente (lanza o bucle infinito) es {b('sm')}.",
   f"Para permitir ausencia de valor en una propiedad uso {c('prop?: T')} u unión con {b('sm')}."],
  "ans":["1) any / unknown 2) Array<number> 3) [string, boolean] 4) inferencia 5) never 6) undefined (o null según diseño)"]},
 {"title":"Completar: interfaces, types y genéricos","inst":"Completa los fragmentos o términos.",
  "items":[
   f"Para describir la forma de un objeto reutilizable puedo usar {b('md')} o {b('md')}.",
   f"Un alias para unión de literales: {c('type Role = ')}{b('xl')}.",
   f"Una función genérica que devuelve el mismo tipo que recibe: {c('function identity<T>(arg: T): ')}{b('sm')}{c(' { return arg; }')}",
   f"Para hacer todas las propiedades opcionales uso el utility type {b('md')} y para solo lectura {b('md')}.",
   f"El acceso a un tipo por índice de propiedad se escribe como {b('md')} (indexed access).",
   f"Una discriminated union suele tener una propiedad común literal, por ejemplo {c('kind')} o {b('md')}."],
  "ans":["1) interface / type 2) 'admin' | 'user' | 'guest' 3) T 4) Partial / Readonly 5) T[K] 6) type/status"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Revisa y corrige o indica \"Correcto\".",
  "items":[
   f"{c('let x: string = 10;')} compila sin problemas. → {ln()}",
   f"Usar {c('unknown')} para datos externos y luego estrechar con guards es más seguro que {c('any')}. → {ln()}",
   f"{c('type A = {a: string}; type B = {b: number}; type C = A & B;')} crea un tipo con ambas propiedades. → {ln()}",
   f"Una interfaz puede extender otra con {c('extends')}. → {ln()}",
   f"Asumir que {c('document.getElementById')} nunca devuelve {c('null')} es siempre seguro. → {ln()}",
   f"Los genéricos permiten reutilizar lógica manteniendo tipos sin duplicar funciones. → {ln()}"],
  "ans":["a) Error: tipo incompatible. b) Correcto. c) Correcto. d) Correcto. e) Error: puede ser null. f) Correcto."]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa más adecuada.",
  "items":[
   f"Para un valor que puede ser {c('User')} o {c('null')} uso ({c('User & null')} / {c('User | null')} / {c('User?')}).",
   f"Para estrechar un {c('unknown')} comprobando propiedad uso ({c('typeof')} / {c('in')} / {c('as')} sin validar).",
   f"Declarar retorno {c('never')} significa que la función ({c('retorna undefined')} / {c('no retorna normalmente')}).",
   f"{c('as const')} en un literal ayuda a ({c('ensanchar tipos')} / {c('preservar literales')}).",
   f"Para una colección clave-valor tipada uso ({c('Record<string, User>')} / {c('Array<User>')} / {c('User | string')}).",
   f"Al consumir JSON de una API, lo más seguro es ({c('response as MyType')} / {c('validar con esquema y tipar el resultado')})."],
  "ans":["1) User | null 2) in (o guards según caso) 3) no retorna normalmente 4) preservar literales 5) Record<string, User> 6) validar con esquema y tipar"]},
 {"title":"Elegir/decisión de modelado","inst":"Selecciona la mejor opción de diseño.",
  "items":[
   f"Estado de carga UI: ({c('boolean')} solo / {c("'idle'|'loading'|'success'|'error'")}).",
   f"ID de entidad: ({c('number')} siempre / {c('alias/tipo según dominio')}).",
   f"Campos opcionales en edición: ({c('Partial<Form>')} / {c('Required<Form>')}).",
   f"Resultado de operación: ({c('throw siempre')} / {c('unión éxito/error o Result')} según caso).",
   f"Propiedades inmutables: ({c('Readonly<T>')} / {c('any')}).",
   f"Tipos compartidos front/back: ({c('duplicar')} / {c('compartir/generar')})."],
  "ans":["1) unión discriminada 2) alias según dominio 3) Partial 4) unión/Result según caso 5) Readonly 6) compartir/generar"]},
 {"title":"Transformar: de JS a TS y refinar tipos","inst":"Realiza la transformación indicada.",
  "items":[
   f"Añade tipos: {c('function greet(name) { return \"Hi \" + name; }')} → {ln()}",
   f"Modela respuesta: {c('{ id: 1, active: true }')} como type/interface → {ln()}",
   f"Narrowing: dado {c('x: string | number')}, condición para tratar string → {ln()}",
   f"Evita {c('any')} en {c('function parse(input: any)')} → {ln()}",
   f"A genérico: {c('function first(arr: string[]) { return arr[0]; }')} → {ln()}",
   f"Tipo indexado: de {c('type User = { profile: { email: string } };')} extrae tipo de {c('profile')} → {ln()}"],
  "ans":["1) function greet(name: string): string {...} 2) interface Resp{id:number;active:boolean} 3) if(typeof x==='string'){...} 4) input: unknown y validar 5) function first<T>(arr:T[]):T|undefined 6) User['profile']"]},
 {"title":"Reordenar/relacionar: narrowing y utilidades","inst":"Ordena o relaciona.",
  "items":[
   f"Refinamiento seguro de {c('unknown')}: (a) usar valor (b) comprobar tipo/forma (c) recibir dato → {ln()}",
   f"Utility: 1) {c('Pick')} 2) {c('Omit')} 3) {c('Partial')} con A) quita claves B) selecciona claves C) vuelve opcionales. → {ln()}",
   f"Unión discriminada: (a) definir variantes (b) campo discriminante (c) switch exhaustivo. → {ln()}",
   f"Guard: 1) {c('typeof')} 2) {c('in')} 3) predicado {c('x is T')} con A) custom B) primitivo C) propiedad. → {ln()}",
   f"Migración JS→TS: (a) strict gradual (b) renombrar a .ts (c) tipar bordes/APIs (d) corregir errores. → {ln()}",
   f"Problema: 1) tipo amplio 2) aserción insegura 3) any implícito con A) {c('as T')} sin validar B) falta anotación/config C) pérdida de precisión. → {ln()}"],
  "ans":["1) c,b,a 2) 1-B,2-A,3-C 3) b,a,c 4) 1-B,2-C,3-A 5) b,a,c,d 6) 1-C,2-A,3-B"]},
 {"title":"Escenario: tipado de respuestas en panel de órdenes","inst":"Responde según el caso.",
  "example":"Escenario: frontend en React consume /orders; el backend a veces añade campos o cambia la forma de error y el equipo usó <code>as Order[]</code>, causando fallos en runtime.",
  "items":[
   f"¿Por qué {c('as Order[]')} es riesgoso aquí? {ln()}",
   f"Propón estrategia de validación y tipado en el borde. {ln()}",
   f"Define (texto) tipo para estado fetch: loading/success/error. {ln()}",
   f"¿Cómo modelar {c('deliveredAt')} opcional? {ln()}",
   f"Campo {c('status')} con valores limitados; ¿qué tipo usarías? {ln()}",
   f"Beneficio de {c('strict')} en tsconfig para este caso. {ln()}"],
  "ans":["1) No valida en runtime. 2) Esquema (Zod) + inferencia. 3) Unión discriminada. 4) opcional o string|null. 5) Unión de literales. 6) Detecta null/any implícitos."]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[
   f"Define {c('ApiResult<T>')} = éxito {c('{ok:true; data:T}')} o error {c('{ok:false; error:string}')}. {ln()}{ln()}",
   f"Escribe {c('isNonEmptyString(x: unknown): x is string')}. {ln()}{ln()}",
   f"Modela {c('User')} con id, email y rol {c("'admin'|'member'")}. {ln()}{ln()}"],
  "ans":["1) type ApiResult<T>={ok:true;data:T}|{ok:false;error:string} 2) return typeof x==='string' && x.length>0 3) interface User{id:string;email:string;role:'admin'|'member'}"]
  }
]
}

u3 = {
"n":3,
"title":"Asincronía: event loop, promesas y async/await",
"context":"Las operaciones de I/O y red en Node.js y el navegador son no bloqueantes, por lo que entender el event loop y los patrones asíncronos es esencial para evitar condiciones de carrera, bloqueos y errores silenciosos. Esta unidad recorre callbacks, promesas, async/await, composición paralela/secuencial y manejo de fallos. El objetivo es escribir flujos claros, predecibles y fáciles de probar.",
"exercises":[
 {"title":"Completar: fundamentos de asincronía","inst":"Completa con el término correcto.",
  "example":f"Ejemplo: Una {c('Promise')} puede estar pendiente, cumplida o rechazada.",
  "items":[
   f"El {b('md')} permite manejar I/O sin bloquear el hilo principal de JS.",
   f"Una promesa cumplida pasa a {b('sm')} y una rechazada a {b('sm')} o {c('catch')}.",
   f"{c('async')} hace que una función retorne implícitamente una {b('md')}.",
   f"{c('await')} se usa dentro de funciones {b('sm')} (o top-level ESM cuando aplica).",
   f"Para ejecutar tareas independientes en paralelo y fallar rápido uso {b('lg')}.",
   f"Para obtener todos los resultados aunque algunos fallen uso {b('lg')}."],
  "ans":["1) event loop 2) then / catch 3) Promise 4) async 5) Promise.all 6) Promise.allSettled"]},
 {"title":"Completar: errores y control de flujo","inst":"Completa conceptos o fragmentos.",
  "items":[
   f"En async/await manejo errores con {b('sm')} / {b('sm')}.",
   f"Un {c('await')} sin {c('try/catch')} propaga el rechazo al {b('lg')}.",
   f"Para lanzar error uso {c('throw new ')}{b('md')}{c('(...)')}.",
   f"Si {c('b')} depende del resultado de {c('a')}, la ejecución debe ser {b('md')}.",
   f"Para tolerar fallos transitorios uso reintentos con {b('lg')}.",
   f"Un callback invocado dos veces puede causar efectos {b('md')}."],
  "ans":["1) try / catch 2) llamador (promesa) 3) Error 4) secuencial 5) backoff 6) duplicados/no deterministas"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o indica \"Correcto\".",
  "items":[
   f"{c('await Promise.all([a(), b()])')} ejecuta {c('a')} y {c('b')} en paralelo si se invocan al crear el array. → {ln()}",
   f"Olvidar {c('await')} dentro de {c('try/catch')} puede impedir capturar el rechazo ahí. → {ln()}",
   f"Mezclar {c('.then')} y {c('await')} es imposible. → {ln()}",
   f"{c('forEach')} con async no espera como {c('for...of')} con {c('await')}. → {ln()}",
   f"Siempre conviene paralelizar todo sin considerar dependencias ni límites. → {ln()}",
   f"Tragar errores en silencio es riesgoso; es mejor registrar/manejar o propagar. → {ln()}"],
  "ans":["a) Correcto. b) Correcto. c) Error: posible, pero mejor consistencia. d) Correcto. e) Error. f) Correcto."]},
 {"title":"Elegir la opción correcta","inst":"Selecciona la alternativa correcta.",
  "items":[
   f"\"Primero en resolverse ignorando rechazos previos\" corresponde a ({c('Promise.all')} / {c('Promise.race')} / {c('Promise.any')}).",
   f"Para procesar en serie con await en bucle uso ({c('forEach async')} / {c('for...of')}).",
   f"Una función {c('async')} sin retorno explícito resuelve a ({c('null')} / {c('undefined')}).",
   f"Tras {c('Promise.all')} proceso resultados con ({c('map')} / {c('forEach sin retorno')} principalmente).",
   f"Una petición de red debe ({c('esperar indefinidamente')} / {c('tener timeout/abort')}).",
   f"{c('catch(e){}')} vacío es ({c('seguro')} / {c('riesgoso')})."],
  "ans":["1) Promise.any 2) for...of 3) undefined 4) map 5) timeout/abort 6) riesgoso"]},
 {"title":"Elegir/decisión de flujo","inst":"Elige la mejor estrategia.",
  "items":[
   f"Dos llamadas independientes: ({c('secuencial')} / {c('paralelo')}).",
   f"Segunda depende del id de la primera: ({c('paralelo')} / {c('secuencial')}).",
   f"Una sección puede fallar sin tumbar todo: ({c('Promise.all')} / {c('allSettled o manejo parcial')}).",
   f"Fallo transitorio: ({c('reintento infinito inmediato')} / {c('backoff con límite')}).",
   f"Operación larga: ({c('bloquear')} / {c('estado de carga/cancelación')}).",
   f"Logs de error: ({c('con contexto')} / {c('genéricos')})."],
  "ans":["1) paralelo 2) secuencial 3) allSettled/manejo parcial 4) backoff con límite 5) estado de carga 6) con contexto"]},
 {"title":"Transformar: callbacks a async/await","inst":"Transforma según se indique.",
  "pre":"function load(id, cb){\n  getUser(id, (e,u)=>{\n    if(e) return cb(e);\n    getPrefs(u.id, (e2,p)=> e2?cb(e2):cb(null,{u,p}));\n  });\n}",
  "items":[
   f"Reescribe {c('load')} como {c('async')} que retorne {c('{u,p}')}. {ln()}{ln()}{ln()}",
   f"Si fueran independientes, patrón recomendado: {ln()}",
   f"Esquema {c('try/catch')} con await: {ln()}{ln()}",
   f"Estrategia para no ocultar {c('u')} si falla {c('p')}: {ln()}",
   f"Implementa {c('delay(ms)')}: {ln()}{ln()}",
   f"API para cancelar fetch: {ln()}"],
  "ans":["1) async function load(id){const u=await getUser(id);const p=await getPrefs(u.id);return{u,p};} 2) Promise.all 3) try{await ...}catch(e){...} 4) catch parcial/allSettled 5) ms=>new Promise(r=>setTimeout(r,ms)) 6) AbortController"]},
 {"title":"Reordenar/relacionar: estados y patrones","inst":"Ordena o relaciona.",
  "items":[
   f"Promesa exitosa: (1) pendiente (2) cumplida (3) rechazada. Orden: {ln()}",
   f"1){c('Promise.all')} 2){c('Promise.race')} 3){c('Promise.allSettled')} con A) todos B) primero en asentarse C) falla rápida. → {ln()}",
   f"Manejo robusto: (a) intentar (b) capturar/log (c) reintento/fallback (d) informar. → {ln()}",
   f"Síntoma: 1) UI congelada 2) unhandled rejection 3) race condition con A) falta await/catch B) bloqueo C) orden no determinista. → {ln()}",
   f"Secuencia dependiente: (a) validar (b) await paso 1 (c) await paso 2 (d) retornar. → {ln()}",
   f"1) AbortController 2) timeout 3) retry+backoff con A) cancelar B) limitar espera C) fallos transitorios. → {ln()}"],
  "ans":["1) 1→2 2) 1-C,2-B,3-A 3) a,b,c,d 4) 1-B,2-A,3-C 5) a,b,c,d 6) 1-A,2-B,3-C"]},
 {"title":"Escenario: carga de dashboard de citas médicas","inst":"Responde al escenario.",
  "example":"Escenario: el dashboard carga citas, médicos y salas en paralelo. La API de salas a veces falla; se requiere mostrar datos parciales y errores claros sin bloquear toda la pantalla.",
  "items":[
   f"Método de Promise para éxito parcial: {ln()}",
   f"Cómo representar estado por panel: {ln()}",
   f"Corrección a {c('forEach(async...)')} esperando en serie: {ln()}",
   f"Acción ante timeout de salas: {ln()}",
   f"Riesgo de tragar errores en {c('catch')}: {ln()}",
   f"Estrategia ante cambios rápidos de fecha (race): {ln()}"],
  "ans":["1) Promise.allSettled 2) estados independientes loading/success/error 3) for..of con await o Promise.all 4) abort/timeout + error parcial + reintento 5) oculta fallos 6) abortar o ignorar respuestas obsoletas"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[
   f"Implementa {c('delay(ms)')}. {ln()}{ln()}",
   f"Función async que envuelva {c('fetchJson(url)')} con try/catch y retorne objeto {c('{ok,...}')}. {ln()}{ln()}{ln()}",
   f"3 pasos para ejecutar tres tareas independientes y continuar solo si todas tienen éxito. {ln()}{ln()}"],
  "ans":["1) const delay=ms=>new Promise(r=>setTimeout(r,ms)) 2) try{return{ok:true,data:await fetchJson(url)}}catch(e){return{ok:false,error:String(e)}} 3) iniciar promesas, await Promise.all, try/catch"]
  }
]
}

for u in [u2,u3]:
    frag = render_unit_html(u)
    ans = render_ans(u)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,f"u{u['n']:02d}_ans.html"),"w",encoding="utf-8").write(ans)
    print(u['n'], len(frag), len(ans), len(frag)+len(ans))
