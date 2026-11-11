# QA script (F4)
import os, re, json, collections
BASE=r"C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200"
WB=os.path.join(BASE,"workbook-fullstack-200.html")
UNITS=os.path.join(BASE,"units")

def read(p): return open(p,encoding='utf-8').read()

def main():
    html=read(WB)
    m=re.search(r'<section class="answers">',html)
    ex_chars=len(html[:m.start()]) if m else len(html)
    sol_chars=len(html[m.start():]) if m else 0
    units=html.count('class="unit"')
    exercises=html.count('<h3>Ejercicio ')
    items=html.count('<li>')
    # per unit
    rows=[]
    for i in range(1,21):
        h=read(os.path.join(UNITS,f'u{i:02d}.html'))
        a=read(os.path.join(UNITS,f'u{i:02d}_ans.html'))
        exs=h.count('<h3>Ejercicio ')
        lis=h.count('<li>')
        rows.append((i,len(h),len(a),len(h)+len(a),exs,lis))
    total=sum(r[3] for r in rows)
    # naive duplication: repeated long lines/sentences in scenarios/examples
    texts=re.findall(r'<div class="example">.*?</div>|<p class="context">.*?</p>',html,flags=re.S)
    norm=[re.sub(r'\s+',' ',re.sub('<.*?>','',t)).strip() for t in texts]
    dups=[t for t,c in collections.Counter(norm).items() if c>1 and len(t)>40]
    report={
      'wb_chars':len(html),'ex_chars':ex_chars,'sol_chars':sol_chars,
      'sol_pct':round(sol_chars/len(html)*100,2) if html else 0,
      'pages_est_2320':round(len(html)/2320,1),
      'units':units,'exercises':exercises,'li_items':items,
      'avg_unit_chars':round(total/units) if units else 0,
      'min_unit':min(r[3] for r in rows),'max_unit':max(r[3] for r in rows),
      'dup_context_examples':len(dups)
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))
    for r in rows:
        print(f"U{r[0]:02d} ex={r[1]} sol={r[2]} tot={r[3]} ejercicios={r[4]} li={r[5]}")

if __name__=='__main__':
    main()
