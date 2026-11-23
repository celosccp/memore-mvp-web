"""Monta a página interativa do benchmark: dados (sim/grid5.json) num arquivo ao lado e logos embutidos na página."""
import json, re
S = '/tmp/claude-0/-home-user-memore-mvp-web/cb0f6e45-b126-5c62-bffa-408e7affbee5/scratchpad'
SRC = '/root/.claude/uploads/cb0f6e45-b126-5c62-bffa-408e7affbee5/67fa081b-Simulador_Proposta_Valor_XP.html'
D = json.load(open(S + '/sim/grid5.json'))
src = open(SRC, encoding='utf-8', errors='replace').read()
brands = json.loads(re.search(r'<script id="embedded-brands" type="application/json">(.*?)</script>', src, re.S).group(1))
logos = {b: brands[b]['data'] for b in D['inst'] if b in brands and isinstance(brands[b], dict) and str(brands[b].get('data', '')).startswith('data:image/')}
html = open(S + '/bench-template.html', encoding='utf-8').read().replace('/*__LOGOS__*/{}', json.dumps(logos, ensure_ascii=False, separators=(',', ':')))
import os; os.makedirs(S + '/bench-site', exist_ok=True)
open(S + '/bench-site/benchmark-digital.html', 'w', encoding='utf-8').write(html)
json.dump(D, open(S + '/bench-site/benchmark-dados.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ok pagina', len(html), 'dados', os.path.getsize(S + '/bench-site/benchmark-dados.json'), 'logos', len(logos))
