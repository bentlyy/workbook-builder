# -*- coding: utf-8 -*-
import os, html

BASE = r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS_DIR = os.path.join(BASE, "units")

def e(s): return html.escape(str(s), quote=False)
def c(s): return f"<code>{e(s)}</code>"
def b(cls="md"): return f'<span class="blank {cls}"></span>'
def ln(): return '<span class="line"></span>'

u1 = {
"n":1,
"title":"JavaScript moderno y entorno Node.js 20+ (ESM)",
"context":"Un dominio sólido de la sintaxis moderna de JavaScript y del sistema de módulos ESM permite escribir código predecible, mantenible y compatible con el ecosistema actual de Node.js. Esta unidad sienta las bases para tipado, asincronía y tooling que usarás en todo el stack. Practicarás declaraciones, alcance, desestructuración, módulos y scripts con foco en errores frecuentes en proyectos reales.",
"exercises":[
  {"title":"Completar: declaraciones, alcance y valores","inst":"Completa cada frase con el término o expresión correcta. Usa las pistas entre paréntesis cuando aparezcan.",
   "example":f"Ejemplo: Una variable que no debe reasignarse se declara con {c('const')}.",
   "items":[
     f"Una variable con alcance de bloque que puede reasignarse se declara con {b('sm')} (palabra clave).",
     f"Declarar con {c('var')} otorga alcance de {b('md')} y permite hoisting con inicialización a {c('undefined')}, lo que puede provocar errores sutiles.",
     f"En modo estricto y buenas prácticas, para valores que no cambian de referencia prefiero {b('sm')} para evitar {b('lg')} accidentales.",
     f"El valor primitivo que representa ausencia intencional suele ser {b('sm')}, mientras que una variable declarada sin asignar vale {b('sm')}.",
     f"Al comparar igualdad estricta sin coerción uso el operador {b('sm')} en lugar de {b('sm')}.",
     f"El método {c('Array.prototype.map')} devuelve un {b('md')} nuevo sin mutar el original, a diferencia de {b('md')} que modifica el array en sitio."],
   "ans":["1) let 2) función / undefined 3) const / reasignaciones 4) null / undefined 5) === / == 6) array / push, sort o splice (métodos mutables)"]
  },
  {"title":"Completar: módulos ESM y Node.js 20+","inst":"Completa los fragmentos o conceptos relacionados con ESM, package.json y ejecución en Node 20+.",
   "items":[
     f"Para habilitar ESM por defecto en un paquete puedo definir {c(chr(34)+'type'+chr(34)+': '+chr(34)+'module'+chr(34))} en {b('md')}.",
     f"Para exportar una función como exportación nombrada escribo {c('export function parseConfig() {}')} y la importo con {b('xl')}.",
     f"Una exportación por defecto se importa sin llaves: {c('import ___ from '+chr(34)+'./logger.js'+chr(34))} (nombre local).",
     f"En ESM, la ruta relativa a un archivo local debe incluir normalmente la {b('md')} (p. ej. .js) según la resolución del proyecto.",
     f"Para leer variables de entorno en Node uso {b('lg')} y evito hardcodear secretos en el código fuente.",
     f"El archivo {b('md')} permite excluir {c('node_modules')} y artefactos del control de versiones y de empaquetados."],
   "ans":["1) package.json 2) import { parseConfig } from './mod.js' 3) logger (o nombre elegido) 4) extensión 5) process.env 6) .gitignore (y .dockerignore en contenedores)"]
  },
  {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Revisa cada afirmación o fragmento. Corrige el error o indica \"Correcto\".",
   "items":[
     f"{c('const PORT = 3000; PORT = 4000;')} en producción para cambiar el puerto. → {ln()}",
     f"{c('import data from '+chr(34)+'./data'+chr(34))} en un proyecto ESM estricto puede fallar si no se incluye la extensión requerida por el resolver. → {ln()}",
     f"Uso {c('===')} para evitar coerciones inesperadas en comparaciones. → {ln()}",
     f"Ejecutar lógica asíncrona en el nivel superior (top-level await) es compatible con ESM en Node moderno cuando el módulo lo soporta. → {ln()}",
     f"Mezclar {c('require')} y {c('import')} sin configuración interoperable puede generar errores en tiempo de ejecución o build. → {ln()}",
     f"Copiar un objeto anidado con spread ({c('{...obj}')}) garantiza un clon profundo de todas las referencias internas. → {ln()}"],
   "ans":["a) Error: const no permite reasignación. b) Correcto/observación: añadir extensión según configuración. c) Correcto. d) Correcto. e) Correcto (riesgo; unificar módulos). f) Error: spread es superficial; usar structuredClone u otra estrategia."]
  },
  {"title":"Elegir la opción correcta (distractores plausibles)","inst":"Elige la alternativa más adecuada en cada caso.",
   "items":[
     f"Para transformar cada elemento y obtener un nuevo array uso ({c('forEach')} / {c('map')} / {c('filter')}).",
     f"Para obtener solo los elementos que cumplen una condición uso ({c('map')} / {c('filter')} / {c('reduce')}).",
     f"{c('JSON.parse')} de una cadena inválida ({c('lanza excepción')} / {c('devuelve null')} / {c('devuelve undefined')}).",
     f"En desestructuración, {c('const {a: alias} = obj')} asigna el valor de {c('a')} a ({c('a')} / {c('alias')} / {c('obj')}).",
     f"El encadenamiento opcional {c('user?.profile?.email')} evita error cuando ({c('user o profile es null/undefined')} / {c('email es string vacío')} / {c('profile existe siempre')}).",
     f"Para combinar objetos sin mutar el primero es preferible ({c('Object.assign(a,b) mutando a')} / {c('{...a, ...b}')} / {c('a = b')})."],
   "ans":["1) map 2) filter 3) lanza excepción 4) alias 5) user o profile es null/undefined 6) {...a, ...b} (o copia explícita)"]
  },
  {"title":"Elegir/decisión de diseño","inst":"Selecciona la decisión más segura o mantenible.",
   "items":[
     f"Configuración sensible: ({c('commitear .env')} / {c('usar .env.example y secretos fuera del repo')}).",
     f"Script reproducible: ({c('documentar en README y scripts')} / {c('comandos recordados')}).",
     f"Exportar utilidades: ({c('exports nombrados claros')} / {c('default con objeto gigante sin tipos')}).",
     f"Al parsear input externo: ({c('asumir estructura')} / {c('validar y manejar errores')}).",
     f"Funciones de utilidad: ({c('efectos secundarios ocultos')} / {c('entradas/salidas explícitas')}).",
     f"Versión de Node en equipo/CI: ({c('fijar versión (engines/.nvmrc)')} / {c('cada uno usa la suya')})."],
   "ans":["1) .env.example y secretos fuera 2) documentar en README y scripts 3) exports nombrados claros 4) validar y manejar errores 5) entradas/salidas explícitas 6) fijar versión"]
  },
  {"title":"Transformar: modernizar y clarificar","inst":"Reescribe o indica la transformación solicitada.",
   "example":"Ejemplo: <code>var x = 1; x = 2;</code> → <code>let x = 1; x = 2;</code>.",
   "items":[
     f"Convierte a desestructuración: {c('const name = user.name; const role = user.role;')} → {ln()}",
     f"Usa template literal: {c(chr(39)+'Hola '+chr(39)+' + name + '+chr(39)+'!'+chr(39))} → {ln()}",
     f"Arrow en callback: {c('items.map(function(i){ return i.id; })')} → {ln()}",
     f"Evita mutación al agregar: {c('arr.push(item)')} (nuevo array) → {ln()}",
     f"A ESM nombrado: {c('module.exports = { sum }')} → {ln()}",
     f"Parámetro por defecto: {c('function f(port){ port = port || 3000; }')} (ojo con 0) → {ln()}"],
   "ans":["1) const {name, role} = user; 2) `Hola ${name}!` 3) items.map(i => i.id) 4) [...arr, item] 5) export { sum } 6) function f(port = 3000){} (o ?? para 0)"]
  },
  {"title":"Reordenar/relacionar: flujo de módulo y ejecución","inst":"Ordena o relaciona los pasos/ideas.",
   "items":[
     f"Flujo para agregar dependencia: (a) ejecutar script (b) {c('npm install pkg')} (c) importar/usar (d) confirmar {c('package.json/lockfile')}. → {ln()}",
     f"Relaciona: 1) {c('export default')} 2) {c('export const x')} 3) {c('import * as m')} con A) namespace B) único por módulo C) nombrada. → {ln()}",
     f"Crear script: (a) definir en {c('scripts')} (b) implementar lógica (c) ejecutar {c('npm run')}. → {ln()}",
     f"Error-causa: 1) ReferenceError 2) SyntaxError 3) TypeError con A) tipo/propiedad inválida B) identificador no definido C) sintaxis mal formada. → {ln()}",
     f"Diagnóstico: (a) leer stack (b) reproducir (c) aislar (d) corregir y verificar. → {ln()}",
     f"Archivo-propósito: 1) {c('.nvmrc')} 2) {c('package-lock.json')} 3) {c('.gitignore')} con A) versión Node B) deps reproducibles C) exclusiones VCS. → {ln()}"],
   "ans":["1) b,d,c,a 2) 1-B,2-C,3-A 3) b,a,c 4) 1-B,2-C,3-A 5) b,a,c,d 6) 1-A,2-B,3-C"]
  },
  {"title":"Escenario: revisión de módulo de utilidades (CLI de reportes)","inst":"Responde con precisión técnica según el escenario.",
   "example":"Escenario: un CLI en Node 20+ genera reportes diarios. Tras migrar a ESM, algunos entornos fallan y hay resultados inconsistentes por comparaciones y mutaciones.",
   "items":[
     f"Tiene {c(chr(34)+'type'+chr(34)+': '+chr(34)+'commonjs'+chr(34))} pero usa {c('import')}. ¿Ajuste coherente? {ln()}",
     f"Compara con {c('==')} y rompe el caso {c('0')}. ¿Qué operador/práctica evitan esto? {ln()}",
     f"Usa {c('arr.sort()')} sobre array compartido y otro módulo ve orden cambiado. ¿Corrección? {ln()}",
     f"Lee {c('API_KEY')} desde código fuente. Indica dos mejoras. {ln()}",
     f"Import relativo omite extensión y falla en CI. ¿Qué haces? {ln()}",
     f"Propones fijar versión de Node: menciona dos mecanismos. {ln()}"],
   "ans":["1) Unificar a ESM o CJS consistentemente. 2) === y validaciones explícitas. 3) Copiar antes: [...arr].sort() o toSorted(). 4) Variables de entorno/secret manager y .env.example. 5) Agregar extensión y alinear config. 6) engines y .nvmrc/.node-version."]
  },
  {"title":"Producción guiada","inst":"Escribe soluciones breves y concretas.",
   "items":[
     f"Función ESM {c('sum(a,b)')} exportada nombrada que valide números finitos y lance {c('TypeError')} si no. {ln()}{ln()}{ln()}",
     f"Ejemplo de {c('package.json')} mínimo para proyecto ESM con script {c('start')}. {ln()}{ln()}{ln()}",
     f"Redacta 3 reglas de estilo JS/TS para evitar bugs de esta unidad. {ln()}{ln()}{ln()}"],
   "ans":["1) export function sum(a,b){ if(!Number.isFinite(a)||!Number.isFinite(b)) throw new TypeError('Invalid'); return a+b; } 2) {\"name\":\"x\",\"type\":\"module\",\"scripts\":{\"start\":\"node src/index.js\"},\"engines\":{\"node\":\">=20\"}} 3) Ej: usar ===, evitar mutaciones, no hardcodear secretos, unificar ESM."]
  }
]
}

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

if __name__ == "__main__":
    frag = render_unit_html(u1)
    ans = render_ans(u1)
    os.makedirs(UNITS_DIR, exist_ok=True)
    open(os.path.join(UNITS_DIR,"u01.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,"u01_ans.html"),"w",encoding="utf-8").write(ans)
    print(len(frag), len(ans))
