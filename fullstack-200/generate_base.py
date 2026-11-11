# -*- coding: utf-8 -*-
import os, html

BASE = r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"

HEAD = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Workbook Full Stack — Práctica guiada (200 páginas)</title>
<style>
  :root{--ink:#1a1a1a;--muted:#555;--accent:#0f766e;--accent2:#155e75;--line:#cbd5e1;--bg:#fff;--soft:#f8fafc;}
  *{box-sizing:border-box} body{font-family:Georgia,"Times New Roman",serif;color:var(--ink);background:var(--bg);margin:0;line-height:1.55}
  .page{max-width:820px;margin:0 auto;padding:36px 44px}
  h1,h2,h3,h4{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#0b3b36}
  h1{font-size:2.2rem;margin:0 0 .25rem} .subtitle{color:var(--muted);margin:0 0 1.1rem;font-size:1.05rem}
  h2{font-size:1.38rem;border-bottom:2px solid var(--accent);padding-bottom:.25rem;margin:1.8rem 0 .5rem}
  h3{font-size:1.06rem;margin:1.1rem 0 .3rem;color:var(--accent2)}
  .context{font-style:italic;color:var(--muted);margin:.2rem 0 .85rem}
  .exercise{margin:.85rem 0 1.05rem} .inst{font-family:system-ui,sans-serif;font-weight:600;margin:.35rem 0 .28rem}
  ol.items{margin:.15rem 0 .15rem 1.3rem;padding:0} ol.items li{margin:.34rem 0}
  .subitems{list-style:lower-alpha;margin:.2rem 0 .2rem 1.2rem}
  .blank{display:inline-block;min-width:9ch;border-bottom:1px solid #334155;height:1.1em;vertical-align:baseline}
  .blank.sm{min-width:5ch}.blank.md{min-width:16ch}.blank.lg{min-width:30ch}
  .line{display:block;border-bottom:1px solid #94a3b8;height:1.45em;margin:.16rem 0}
  .example{background:var(--soft);border-left:3px solid var(--accent);padding:.5rem .7rem;margin:.45rem 0;font-size:.94rem}
  code{font-family:ui-monospace,Consolas,"Cascadia Mono",monospace;background:#f1f5f9;padding:.04rem .28rem;border-radius:3px;font-size:.9em}
  pre{background:#0f172a;color:#e2e8f0;padding:.65rem .85rem;border-radius:6px;overflow:auto;font-size:.83rem;line-height:1.42;white-space:pre-wrap}
  .note{font-size:.91rem;color:var(--muted)}
  .toc ul{columns:2;gap:2rem;margin:.4rem 0} .toc li{margin:.2rem 0;font-family:system-ui,sans-serif;font-size:.94rem}
  .answers{page-break-before:always} .answers h3{margin-top:1rem}
  .key{font-family:system-ui,sans-serif;font-size:.92rem} .key p{margin:.22rem 0}
  table.meta{border-collapse:collapse;width:100%;font-family:system-ui,sans-serif;font-size:.9rem;margin:.5rem 0}
  table.meta th,table.meta td{border:1px solid #e2e8f0;padding:.3rem .45rem;text-align:left}
  @media print{
    .page{max-width:none;padding:0 7mm} body{font-size:10.7pt}
    h2{page-break-after:avoid} .exercise,.example,pre{page-break-inside:avoid}
    .unit{page-break-before:always} .unit:first-of-type,.cover{page-break-before:auto}
    a{color:inherit;text-decoration:none}
  }
  @page{margin:14mm}
</style>
</head>
<body>
<div class="page">
'''
FOOT = "\n</div>\n</body>\n</html>\n"

def e(s):
    return html.escape(str(s), quote=False)

def blank(cls=""): 
    c = "blank" + (" " + cls if cls else "")
    return f'<span class="{c}"></span>'

def line(): return '<span class="line"></span>'

if __name__ == "__main__":
    print("ok")
