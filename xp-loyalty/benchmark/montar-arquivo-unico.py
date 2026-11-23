"""Gera a versão em arquivo único do benchmark (dados embutidos), para abrir direto no navegador."""
S='/tmp/claude-0/-home-user-memore-mvp-web/cb0f6e45-b126-5c62-bffa-408e7affbee5/scratchpad'
h=open(S+'/bench-site/benchmark-digital.html',encoding='utf-8').read()
d=open(S+'/bench-site/benchmark-dados.json',encoding='utf-8').read().replace('</','<\\/')
a="fetch('benchmark-dados.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })"
assert h.count(a)==1
h=h.replace(a,"Promise.resolve(JSON.parse(document.getElementById('dados').textContent))")
i=h.index('<script>')
h=h[:i]+'<script type="application/json" id="dados">'+d+'</script>\n'+h[i:]
h=h.replace('<style>','<style>\nhtml{color-scheme:light}body{margin:0}img{max-width:100%}',1)
out='<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n</head>\n<body>\n'+h+'\n</body>\n</html>\n'
open('/home/user/memore-mvp-web/xp-loyalty/benchmark/benchmark-digital-offline.html','w',encoding='utf-8').write(out); print('offline',len(out))
