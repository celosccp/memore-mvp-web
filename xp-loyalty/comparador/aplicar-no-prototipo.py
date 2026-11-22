"""Coluna à direita do protótipo: quanto o mesmo cliente teria nos outros bancos (top 5), a partir do comparador."""
import json
S = '/tmp/claude-0/-home-user-memore-mvp-web/cb0f6e45-b126-5c62-bffa-408e7affbee5/scratchpad'
p = '/home/user/memore-mvp-web/xp-loyalty/index.html'; s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)
g = json.load(open(S + '/sim/grid.json'))
data = json.dumps(g, ensure_ascii=False, separators=(',', ':'))

rep("""  </main>
</div>
<button id="panelToggle" data-a="panel">Demo ›</button>""",
"""  </main>
  <aside id="cmp"></aside>
</div>
<button id="panelToggle" data-a="panel">Demo ›</button>""")

rep("</style>", """
/* ===== Comparação com outros bancos (coluna da direita) ===== */
#cmp{display:none;width:clamp(250px,26vw,318px);flex:none;background:#0B0B0C;color:#F4F4F2;border-left:1px solid #232327;flex-direction:column;z-index:30}
@media (min-width:1024px){ #cmp{display:flex} }
#cmp .ch{padding:16px 18px 14px;border-bottom:1px solid #232327;background:radial-gradient(120% 140% at 100% 0%,rgba(255,199,9,.16),transparent 60%)}
#cmp h1{font-size:16px;margin:0 0 3px;letter-spacing:-.01em}
#cmp .ch p{margin:0;font-size:12px;color:#9A9AA2;line-height:1.35}
#cmp .ch p b{color:#F4F4F2;font-weight:650}
#cmp .cb{flex:1;overflow:auto;padding:14px 16px 18px;scrollbar-width:thin;scrollbar-color:#2A2A2F transparent}
#cmp .seg{background:#1A1A1D;border-radius:999px;padding:4px;margin-bottom:14px}
#cmp .seg button{border-radius:999px;color:#9A9AA2;padding:8px 6px;font-size:12.5px}
#cmp .seg button.on{background:#FFC709;color:#000}
.cr{position:relative;display:grid;grid-template-columns:22px 1fr auto;column-gap:8px;align-items:center;padding:10px 10px 12px;border-radius:14px;background:#141416;margin-bottom:7px;overflow:hidden}
.cr .rk{font-size:12px;font-weight:800;color:#8A8A92;text-align:center}
.cr b{display:block;font-size:13.5px;font-weight:650;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cr span{display:block;font-size:11.5px;color:#8A8A92;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cr .v{font-size:14.5px;font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap}
.cr .v small{font-size:10.5px;font-weight:600;color:#8A8A92;margin-left:2px}
.cr .bar{position:absolute;left:0;bottom:0;height:3px;width:100%;background:#F4F4F2;opacity:.5;transform-origin:0 50%;transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.cr.xp{background:rgba(255,199,9,.12);box-shadow:inset 0 0 0 1px rgba(255,199,9,.55);margin-bottom:14px}
.cr.xp .rk{color:#FFC709} .cr.xp .bar{background:#FFC709;opacity:1}
.cr.xp .rk i{font-style:normal;display:inline-grid;place-items:center;width:22px;height:19px;border-radius:5px;background:#fff;color:#111;font-size:9.5px;font-weight:900;letter-spacing:-.04em}
#cmp .gl{font-size:11px;text-transform:uppercase;letter-spacing:.09em;color:#FFC709;font-weight:700;margin:0 0 8px}
#cmp .gap{font-size:12.5px;color:#C9C9CF;background:#141416;border-radius:14px;padding:10px 12px;margin-top:10px;line-height:1.4}
#cmp .gap b{color:#FFC709}
#cmp .src{font-size:11px;color:#77777F;line-height:1.4;margin-top:12px}
</style>""")

rep("const beh = id => BEH.find(b => b.id === id);",
"""const beh = id => BEH.find(b => b.id === id);
// Comparação com outros bancos: grade gerada pelo simulador "Comparativo econômico das propostas de valor"
// (patrimônio de R$ 2.500 em R$ 2.500, gasto de R$ 500 em R$ 500; valores líquidos em R$/mês). all = tudo, fin = só financeiro.
const CMP = """ + data + """;
function cmpRow(mode = S.cmpMode || 'all'){
  const ai = Math.min(Math.round(S.auc / CMP.aucStep), (CMP[mode].length / CMP.nTpv) - 1), ti = Math.min(Math.round(S.gasto / CMP.tpvStep), CMP.nTpv - 1);
  const r = CMP[mode][ai * CMP.nTpv + ti], out = { xp: r[0] < 0 ? null : { nome: CMP.names[r[0]][1], v: r[1] }, riv: [] };
  for (let i = 2; i < r.length; i += 2) out.riv.push({ banco: CMP.names[r[i]][0], nome: CMP.names[r[i]][1], v: r[i + 1] });
  return out;
}
function renderCmp(){
  const el = document.getElementById('cmp'); if (!el) return;
  const mode = S.cmpMode || 'all', c = cmpRow(mode), top = Math.max(1, c.xp ? c.xp.v : 0, ...c.riv.map(r => r.v));
  const val = v => `<div class="v">${brl(v)}<small>/mês</small></div>`, bar = v => `<i class="bar" style="transform:scaleX(${Math.max(0, v) / top})"></i>`;
  const melhor = c.riv[0], dif = melhor && c.xp ? melhor.v - c.xp.v : 0, pos = c.xp ? c.riv.filter(r => r.v > c.xp.v).length + 1 : null;
  el.innerHTML = `<div class="ch"><h1>Nos outros bancos</h1><p>Quanto este cliente teria por mês com <b>${brl(S.auc)}</b> investidos e <b>${brl(S.gasto)}</b> no cartão.</p></div>
    <div class="cb"><div class="seg"><button class="${mode === 'all' ? 'on' : ''}" data-a="cmp:all">Tudo</button><button class="${mode === 'fin' ? 'on' : ''}" data-a="cmp:fin">Só financeiro</button></div>
    <div class="gl">XP hoje</div>
    ${c.xp ? `<div class="cr xp"><div class="rk"><i>XP</i></div><div style="min-width:0"><b>${c.xp.nome}</b><span>Regra atual, sem a Jornada XP</span></div>${val(c.xp.v)}${bar(c.xp.v)}</div>`
           : `<div class="cr xp"><div class="rk"><i>XP</i></div><div style="min-width:0"><b>Sem cartão elegível</b><span>Abaixo do mínimo de investimento</span></div>${val(0)}</div>`}
    <div class="gl">Top 5 fora da XP</div>
    ${c.riv.map((r, i) => `<div class="cr"><div class="rk">${i + 1}</div><div style="min-width:0"><b>${r.banco}</b><span>${r.nome}</span></div>${val(r.v)}${bar(r.v)}</div>`).join('')}
    ${melhor ? `<div class="gap">${dif > 0 ? `A melhor oferta de fora entrega <b>${brl(dif)}</b> a mais por mês que a XP hoje. Entre estas seis, a XP ficaria em <b>${pos}º</b>.` : `Neste perfil, a XP hoje já entrega mais que as cinco melhores de fora.`}</div>` : ''}
    <p class="src">${mode === 'all' ? 'Valor líquido: dinheiro de volta, rendimento extra e serviços incluídos pelo preço equivalente, menos mensalidades.' : 'Só dinheiro de volta, pontos e rendimento extra, menos mensalidades. Não conta serviços como salas VIP e assinaturas.'} Um cartão por instituição. Saldo em caixinha de até R$ 10 mil. Fonte: Comparativo econômico das propostas de valor, pesquisa de ${CMP.date.split('-').reverse().join('/')}. Valores aproximados à faixa mais próxima.</p></div>`;
}""")

rep("reconcile(); renderPhone(); renderPanel();\n", "reconcile(); renderPhone(); renderPanel(); renderCmp();\n")
rep("""    document.getElementById(k === 'auc' ? 'oAuc' : 'oGasto').textContent = brl(S[k]);
    reconcile(); renderPhone();""", """    document.getElementById(k === 'auc' ? 'oAuc' : 'oGasto').textContent = brl(S[k]);
    reconcile(); renderPhone(); renderCmp();""")
rep("    case 'earn': applyEarn(x); break;", "    case 'earn': applyEarn(x); break;\n    case 'cmp': S.cmpMode = x; break;")
open(p, 'w', encoding='utf-8').write(s)
print('ok', len(s))
