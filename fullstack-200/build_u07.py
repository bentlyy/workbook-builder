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

u7 = {
"n":7,"title":"React: efectos, hooks y rendimiento",
"context":"Los hooks permiten encapsular lógica con estado y efectos secundarios en componentes funcionales, pero un uso incorrecto genera bugs difíciles de rastrear y problemas de rendimiento. Comprender el ciclo de efectos, las dependencias, la memoización y las reglas de los hooks es fundamental en aplicaciones React 18 y Next.js. Esta unidad practica useEffect, useMemo, useCallback, hooks personalizados y estrategias para evitar renders innecesarios.",
"exercises":[
 {"title":"Completar: useEffect y ciclo de efectos","inst":"Completa con el concepto correcto.","example":"Ejemplo: El array de dependencias de useEffect indica cuándo debe re-ejecutarse el efecto.",
  "items":[
   f"{c('useEffect')} se usa para sincronizar el componente con sistemas {b('md')} (fetch, suscripciones, timers, DOM).",
   f"Un efecto que retorna una función define una {b('md')} que se ejecuta antes de re-ejecutar el efecto o al desmontar.",
   f"Un array de dependencias vacío {c('[]')} indica que el efecto se ejecuta {b('lg')} tras el montaje.",
   f"Omitir dependencias usadas dentro del efecto puede provocar valores {b('md')} (stale closures).",
   f"Agregar objetos/funciones creadas en cada render al array puede causar ejecuciones {b('md')} si no se estabilizan.",
   f"Los efectos se ejecutan después del {b('md')} y pintado, no durante la renderización pura."],
  "ans":["1) externos 2) limpieza/cleanup 3) una vez 4) obsoletos 5) repetidas 6) render"]},
 {"title":"Completar: memoización y hooks personalizados","inst":"Completa los conceptos.",
  "items":[
   f"{c('useMemo')} memoriza un {b('md')} calculado y {c('useCallback')} memoriza una {b('md')}.",
   f"La memoización solo aporta si el costo de cálculo o la estabilidad referencial {b('md')}.",
   f"Un custom hook es una función que comienza con {b('sm')} y puede llamar otros hooks.",
   f"Los hooks deben llamarse siempre en el mismo {b('md')} y en el mismo nivel del componente.",
   f"{c('React.memo')} evita re-render si sus {b('md')} no cambian (comparación superficial).",
   f"Optimizar prematuramente sin medir puede añadir {b('md')} innecesaria."],
  "ans":["1) valor / función 2) lo justifica 3) use 4) orden 5) props 6) complejidad"]},
 {"title":"Corregir errores (si es correcto, escribe \"Correcto\")","inst":"Corrige o marca \"Correcto\".",
  "items":[
   f"Colocar {c('if (cond) useEffect(...)')} dentro del componente. → {ln()}",
   f"Incluir todas las dependencias usadas en el efecto según las reglas de hooks. → {ln()}",
   f"Hacer fetch en efecto y actualizar estado sin cleanup puede causar warnings o fugas. → {ln()}",
   f"Usar {c('useMemo')} para todo 'por si acaso' mejora siempre el rendimiento. → {ln()}",
   f"Crear un hook {c('useFetch')} para reutilizar lógica de carga y estado. → {ln()}",
   f"Mutar objeto dentro de {c('useMemo')} esperando detección sin nueva referencia. → {ln()}"],
  "ans":["a) Error b) Correcto c) Correcto d) Error e) Correcto f) Error"]},
 {"title":"Elegir la opción correcta","inst":"Elige la alternativa adecuada.",
  "items":[
   f"Suscribirse a evento global y limpiarlo: ({c('useEffect con cleanup')} / {c('useState')} / {c('solo render')}).",
   f"Dependencia que cambia en cada render: ({c('objeto literal inline')} / {c('referencia memoizada/primitivo estable')}).",
   f"Valor derivado barato: ({c('useMemo obligatorio')} / {c('cálculo directo suele bastar')}).",
   f"Handler pasado a hijo memoizado: ({c('useCallback')} / {c('useEffect')}).",
   f"Valor mutable que no re-renderiza: ({c('useRef')} / {c('useState siempre')}).",
   f"setState en efecto con dependencias incorrectas puede causar ({c('bucle infinito')} / {c('mejor SEO')})."],
  "ans":["1) useEffect con cleanup 2) referencia memoizada/primitivo 3) cálculo directo 4) useCallback 5) useRef 6) bucle infinito"]},
 {"title":"Elegir/decisión de rendimiento","inst":"Selecciona la mejor decisión.",
  "items":[
   f"Antes de optimizar: ({c('medir/perfilar')} / {c('memoizar todo')}).",
   f"Virtualización útil cuando: ({c('pocos elementos')} / {c('muchos elementos')}).",
   f"Dependencias del efecto: ({c('silenciar linter')} / {c('cumplir reglas/reestructurar')}).",
   f"Extraer custom hook: ({c('cuando hay duplicación clara')} / {c('todo prematuramente')}).",
   f"Prop drilling profundo: ({c('considerar composición/contexto')} / {c('nunca contexto')}).",
   f"Cálculo costoso dependiente de data: ({c('useMemo([data])')} / {c('recalcular siempre')})."],
  "ans":["1) medir 2) muchos elementos 3) cumplir reglas 4) con criterio 5) considerar contexto 6) useMemo"]},
 {"title":"Transformar: corregir efectos y hooks","inst":"Transforma según se indique.",
  "items":[
   f"Añade cleanup: {c('useEffect(()=>{ const id=setInterval(tick,1000); },[])')} → {ln()}{ln()}",
   f"Estabiliza handler: {c('const onSave = () => save(form);')} → {ln()}",
   f"Evitar stale closure en interval (describe): {ln()}{ln()}",
   f"Firma de hook {c('useUsers()')} para carga/error/dato: {ln()}",
   f"Cálculo pesado en render → {c('useMemo')}: {ln()}",
   f"Efecto usa {c('userId')} pero array {c('[]')} → {ln()}"],
  "ans":["1) return ()=>clearInterval(id) 2) useCallback(()=>save(form),[form,save]) 3) setState funcional o ref 4) function useUsers(){return {data,loading,error}} 5) useMemo(()=>expensive(data),[data]) 6) [userId]"]},
 {"title":"Reordenar/relacionar: reglas y flujo","inst":"Ordena o relaciona.",
  "items":[
   f"Ciclo efecto: (a) render (b) cleanup previo (c) ejecutar efecto (d) cleanup al desmontar. → {ln()}",
   f"1)useState 2)useRef 3)useEffect con A)mutable sin re-render B)estado C)sincronización. → {ln()}",
   f"Custom hook: (a) identificar duplicación (b) extraer useX (c) definir API (d) reutilizar. → {ln()}",
   f"1)stale closure 2)bucle 3)fuga con A)deps mal B)setState sin control C)sin cleanup. → {ln()}",
   f"Depurar: (a) medir (b) identificar causa (c) aplicar mejora (d) verificar. → {ln()}",
   f"1)React.memo 2)useCallback 3)useMemo con A)función B)componente C)valor. → {ln()}"],
  "ans":["1) a,b,c,d 2) 1-B,2-A,3-C 3) a,b,c,d 4) 1-A,2-B,3-C 5) a,b,c,d 6) 1-B,2-A,3-C"]},
 {"title":"Escenario: monitor de sensores en tiempo real (IoT)","inst":"Responde al escenario.","example":"Escenario: pantalla de lecturas IoT por WebSocket/polling. Al cambiar dispositivo seleccionado deben limpiarse suscripciones y evitar datos obsoletos.",
  "items":[
   f"¿Dónde y cómo limpiar suscripción? {ln()}",
   f"Dependencia clave del efecto: {ln()}",
   f"Mitigar setState tras desmontar: {ln()}",
   f"Cálculo costoso de payload: ¿qué hook? {ln()}",
   f"Handler pasado a hijos memoizados: ¿cómo estabilizar? {ln()}",
   f"2 acciones antes de optimizar renders: {ln()}"],
  "ans":["1) cleanup en useEffect 2) deviceId 3) flag/abort/cleanup 4) useMemo 5) useCallback 6) perfilar y revisar deps/props"]},
 {"title":"Producción guiada","inst":"Escribe soluciones breves.",
  "items":[
   f"Efecto que escucha {c('resize')} y limpia listener. {ln()}{ln()}{ln()}",
   f"Firma y retorno de {c('useToggle(initial)')}. {ln()}{ln()}",
   f"3 reglas de uso correcto de hooks. {ln()}{ln()}{ln()}"],
  "ans":["1) useEffect con add/removeEventListener 2) [value,toggle] con useState/useCallback 3) nivel superior, solo componentes/hooks, deps correctas"]
  }
]
}

if __name__ == "__main__":
    frag = render_unit_html(u7)
    ans = render_ans(u7)
    open(os.path.join(UNITS_DIR,"u07.html"),"w",encoding="utf-8").write(frag)
    open(os.path.join(UNITS_DIR,"u07_ans.html"),"w",encoding="utf-8").write(ans)
    print(7, len(frag), len(ans), len(frag)+len(ans))
