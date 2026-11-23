"""Monta a página interativa do benchmark a partir da grade do comparador e dos logos embutidos nele."""
import json, re, sys
S = '/tmp/claude-0/-home-user-memore-mvp-web/cb0f6e45-b126-5c62-bffa-408e7affbee5/scratchpad'
SRC = '/root/.claude/uploads/cb0f6e45-b126-5c62-bffa-408e7affbee5/67fa081b-Simulador_Proposta_Valor_XP.html'
g = json.load(open(S + '/sim/grid3.json'))
AUC = [5000, 10000, 15000, 30000, 50000, 75000, 100000]; TPV = [1000, 2500, 5000, 10000]
pts = {}
for a in AUC:
    for t in TPV:
        k = (a // g['aucStep']) * g['nTpv'] + t // g['tpvStep']
        over = {e[0]: e[1:] for e in g['f'][k]}
        pts[f'{a}|{t}'] = [([n] + ([over[i]] if i in over else [])) if n else 0 for i, n in enumerate(g['n'][k])]
src = open(SRC, encoding='utf-8', errors='replace').read()
brands = json.loads(re.search(r'<script id="embedded-brands" type="application/json">(.*?)</script>', src, re.S).group(1))
logos = {b: brands[b]['data'] for b in g['inst'] if b in brands and isinstance(brands[b], dict) and str(brands[b].get('data', '')).startswith('data:image/')}
D = {'auc': AUC, 'tpv': TPV, 'inst': g['inst'], 'prod': g['prod'], 'pts': pts, 'date': g['date'], 'logos': logos}
html = open(S + '/bench-template.html', encoding='utf-8').read().replace('/*__DATA__*/null', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
open(S + '/benchmark-digital.html', 'w', encoding='utf-8').write(html)
print('ok', len(html), 'logos', len(logos), 'de', len(g['inst']))
