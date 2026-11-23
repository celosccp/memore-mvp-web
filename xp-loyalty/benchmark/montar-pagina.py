"""Monta a página interativa do benchmark a partir da grade do comparador (sim/grid4.json) e dos logos embutidos nele."""
import json, re
S = '/tmp/claude-0/-home-user-memore-mvp-web/cb0f6e45-b126-5c62-bffa-408e7affbee5/scratchpad'
SRC = '/root/.claude/uploads/cb0f6e45-b126-5c62-bffa-408e7affbee5/67fa081b-Simulador_Proposta_Valor_XP.html'
D = json.load(open(S + '/sim/grid4.json'))
src = open(SRC, encoding='utf-8', errors='replace').read()
brands = json.loads(re.search(r'<script id="embedded-brands" type="application/json">(.*?)</script>', src, re.S).group(1))
D['logos'] = {b: brands[b]['data'] for b in D['inst'] if b in brands and isinstance(brands[b], dict) and str(brands[b].get('data', '')).startswith('data:image/')}
html = open(S + '/bench-template.html', encoding='utf-8').read().replace('/*__DATA__*/null', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
open(S + '/benchmark-digital.html', 'w', encoding='utf-8').write(html)
print('ok', len(html), 'logos', len(D['logos']), 'de', len(D['inst']))
