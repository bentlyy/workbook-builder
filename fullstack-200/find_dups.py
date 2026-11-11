import re
from collections import Counter
base=r'C:\Users\garay\OneDrive\Escritorio\ai-skills\workbook-builder\fullstack-200'
p=base+r'\workbook-fullstack-200.html'
html=open(p,encoding='utf-8').read()
texts=re.findall(r'<div class="example">.*?</div>|<p class="context">.*?</p>',html,flags=re.S)
def norm(t): return re.sub(r'\s+',' ',re.sub('<.*?>','',t)).strip()
c=Counter(norm(t) for t in texts)
for t,n in c.items():
    if n>1 and len(t)>30:
        print('---DUP',n)
        print(t)
        print()
