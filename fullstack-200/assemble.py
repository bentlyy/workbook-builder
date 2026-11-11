import os, re, html
BASE=r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
UNITS=os.path.join(BASE,"units")

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
def e(s): return html.escape(s)

unit_htmls=[]; ans_htmls=[]
for i in range(1,21):
    unit_htmls.append(open(os.path.join(UNITS,f'u{i:02d}.html'),encoding='utf-8').read())
    ans_htmls.append(open(os.path.join(UNITS,f'u{i:02d}_ans.html'),encoding='utf-8').read())

all_units=''.join(unit_htmls)
ex_count=all_units.count('<h3>Ejercicio ')
li_count=all_units.count('<li>')

cover = f'''<section class="cover">
<h1>Workbook Full Stack</h1>
<p class="subtitle">Práctica guiada de desarrollo web moderno — De fundamentos a arquitectura, calidad y entrega (Edición extendida)</p>
<p class="note">Orientado a: TypeScript, JavaScript, Node.js 20+, React 18+, Next.js (App Router), APIs REST, PostgreSQL/Prisma, testing (Vitest/Jest/Supertest), seguridad (JWT/Refresh/TOTP/RBAC/hardening), Docker y CI/CD. Progresión por niveles, micro-contexto por unidad, ejercicios graduados (completar, corregir, elegir, transformar, reordenar, escenarios y producción) y solucionario final. Imprime o guarda como PDF desde el navegador.</p>
<table class="meta"><tr><th>Unidades</th><th>Ejercicios</th><th>Ítems (li)</th><th>Metodología</th></tr>
<tr><td>20</td><td>{ex_count}</td><td>{li_count}</td><td>Andamiaje, distractores plausibles, escenarios extendidos, soluciones modelo</td></tr></table>
</section>
<section class="toc"><h2>Índice</h2><ul>
''' + "\n".join(f"<li><a href='#u{n}'>Unidad {n}. {e(t)}</a></li>" for n,t in toc_titles) + "</ul></section>\n"

answers_sec = '<section class="answers"><h2>Solucionario</h2><p class="note">Respuestas de referencia. En ejercicios de producción/escenario se incluyen soluciones modelo y criterios; pueden existir variantes válidas si mantienen corrección, claridad y seguridad.</p><div class="key">' + "\n".join(ans_htmls) + '</div></section>'

html_out = HEAD + cover + "\n".join(unit_htmls) + "\n" + answers_sec + "\n</div></body></html>\n"
out_path = os.path.join(BASE, "workbook-fullstack-200.html")
open(out_path,"w",encoding="utf-8").write(html_out)
print("ASSEMBLED", len(html_out), "ex",ex_count,"li",li_count)
