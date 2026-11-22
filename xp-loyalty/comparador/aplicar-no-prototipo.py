"""Comparação com outros bancos, versão 2: filtro de bancos e composição visual do valor (cashback, caixinha, serviços, mensalidade)."""
import json
S = '/tmp/claude-0/-home-user-memore-mvp-web/cb0f6e45-b126-5c62-bffa-408e7affbee5/scratchpad'
p = '/home/user/memore-mvp-web/xp-loyalty/index.html'; s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)
data = json.dumps(json.load(open(S + '/sim/grid3.json')), ensure_ascii=False, separators=(',', ':'))

a = s.index("// Comparação com outros bancos: grade gerada pelo simulador")
b = s.index("function renderCmp(){"); b = s.index("\n}", b) + 2
s = s[:a] + """// Comparação com outros bancos: grade gerada pelo simulador "Comparativo econômico das propostas de valor".
// Pontos: patrimônio de R$ 5 mil em R$ 5 mil, gasto de R$ 500 em R$ 500. Por instituição, a melhor modalidade pelo valor total (n)
// e, quando for outra, a melhor só pelo lado financeiro (f). Entrada: [modalidade, dinheiro de volta, tipo (1 cashback, 2 pontos),
// rendimento extra, % do CDI, serviços, mensalidade], em R$ por mês.
const CMP = """ + data + """;
function cmpEntries(mode){
  const ai = Math.min(Math.round(S.auc / CMP.aucStep), CMP.n.length / CMP.nTpv - 1), ti = Math.min(Math.round(S.gasto / CMP.tpvStep), CMP.nTpv - 1), k = ai * CMP.nTpv + ti;
  const over = mode === 'fin' ? Object.fromEntries(CMP.f[k].map(e => [e[0], e.slice(1)])) : {};
  return { tpv: ti * CMP.tpvStep, list: CMP.inst.map((banco, i) => { const e = over[i] || CMP.n[k][i]; if (!e) return null;
    const [pi, cash, kind, yld, cdi, serv0, cost] = e, serv = mode === 'fin' ? 0 : serv0;
    return { banco, nome: CMP.prod[pi], cash, kind, yld, cdi, serv, cost, bruto: cash + yld + serv, v: cash + yld + serv - cost }; }).filter(Boolean) };
}
function renderCmp(){
  const el = document.getElementById('cmp'); if (!el) return;
  const mode = S.cmpMode || 'all', off = S.cmpOff || (S.cmpOff = {}), { tpv, list } = cmpEntries(mode);
  const xp = list.find(r => r.banco === 'XP'), bancos = CMP.inst.filter(b => b !== 'XP'), ligados = bancos.filter(b => !off[b]);
  const riv = list.filter(r => r.banco !== 'XP' && !off[r.banco]).sort((x, y) => y.v - x.v).slice(0, 5);
  const top = Math.max(1, xp ? xp.bruto : 0, ...riv.map(r => r.bruto));
  const pct = v => tpv ? ' ' + (v / tpv * 100).toFixed(1).replace('.', ',').replace(',0', '') + '%' : '';
  const row = (r, rk, cls = '') => `<div class="cr ${cls}"><div class="rk">${rk}</div><div style="min-width:0"><b>${r.banco}</b><span>${r.nome}</span></div><div class="v">${brl(r.v)}<small>/mês</small></div>
      <div class="sb" style="width:${Math.max(4, r.bruto / top * 100)}%">${r.cash > 0 ? `<i class="k1" style="flex:${r.cash}"></i>` : ''}${r.yld > 0 ? `<i class="k2" style="flex:${r.yld}"></i>` : ''}${r.serv > 0 ? `<i class="k3" style="flex:${r.serv}"></i>` : ''}</div>
      <div class="tg">${r.cash > 0 ? `<em class="k1">${r.kind === 2 ? 'Pontos' : r.kind === 1 ? 'Cashback' : 'Conta'}${r.kind ? pct(r.cash) : ''} · ${brl(r.cash)}</em>` : ''}${r.yld > 0 ? `<em class="k2">Caixinha${r.cdi ? ' ' + r.cdi + '% CDI' : ''} · ${brl(r.yld)}</em>` : ''}${r.serv > 0 ? `<em class="k3">Serviços · ${brl(r.serv)}</em>` : ''}${r.cost > 0 ? `<em class="k4">Mensalidade · − ${brl(r.cost)}</em>` : ''}${r.bruto <= 0 && r.cost <= 0 ? '<em>Sem valor estimado neste perfil</em>' : ''}</div></div>`;
  const melhor = riv[0], dif = melhor && xp ? melhor.v - xp.v : 0, pos = xp ? riv.filter(r => r.v > xp.v).length + 1 : null, aberto = isOpen('cmpf');
  el.innerHTML = `<div class="ch"><button class="cx" data-a="cmpopen">Fechar ›</button><h1>Nos outros bancos</h1><p>Quanto este cliente teria por mês com <b>${brl(S.auc)}</b> investidos e <b>${brl(S.gasto)}</b> no cartão.</p></div>
    <div class="cb"><div class="seg"><button class="${mode === 'all' ? 'on' : ''}" data-a="cmp:all">Tudo</button><button class="${mode === 'fin' ? 'on' : ''}" data-a="cmp:fin">Só financeiro</button></div>
    <div class="lg"><span><i class="k1"></i>Cashback ou pontos</span><span><i class="k2"></i>Caixinha (% do CDI)</span>${mode === 'all' ? '<span><i class="k3"></i>Serviços</span>' : ''}</div>
    <div class="gl">XP hoje</div>
    ${xp ? row({ ...xp, nome: xp.nome + ' · regra atual' }, '<i>XP</i>', 'xp') : `<div class="cr xp"><div class="rk"><i>XP</i></div><div style="min-width:0"><b>Sem cartão elegível</b><span>Abaixo do mínimo de investimento</span></div><div class="v">${brl(0)}<small>/mês</small></div></div>`}
    <div class="gl" style="display:flex;justify-content:space-between;align-items:center">Top ${riv.length || 5} fora da XP <button class="fb" data-a="tog:cmpf:0">Bancos ${ligados.length}/${bancos.length} ${aberto ? '−' : '+'}</button></div>
    ${aberto ? `<div class="fbx"><div class="fba"><button data-a="cmpbank:*">Todos</button><button data-a="cmpbank:-">Limpar</button></div>${bancos.map(b => `<button class="chb ${off[b] ? '' : 'on'}" data-a="cmpbank:${b}">${b}</button>`).join('')}</div>` : ''}
    ${riv.length ? riv.map((r, i) => row(r, i + 1)).join('') : '<div class="gap">Nenhum banco selecionado. Abra o filtro e escolha pelo menos um.</div>'}
    ${melhor ? `<div class="gap">${dif > 0 ? `A melhor oferta ${ligados.length < bancos.length ? 'entre os bancos escolhidos' : 'de fora'} entrega <b>${brl(dif)}</b> a mais por mês que a XP hoje. A XP ficaria em <b>${pos}º</b> entre ${riv.length + 1}.` : `Neste perfil, a XP hoje já entrega mais que ${ligados.length < bancos.length ? 'os bancos escolhidos' : 'as cinco melhores de fora'}.`}</div>` : ''}
    <p class="src">${mode === 'all' ? 'Valor líquido por mês: dinheiro de volta, rendimento acima de 100% do CDI e serviços pelo preço equivalente, menos a mensalidade.' : 'Só dinheiro de volta, pontos e rendimento acima de 100% do CDI, menos a mensalidade. Não conta serviços como salas VIP e assinaturas.'} A melhor modalidade de cada instituição. Caixinha: rendimento extra sobre até R$ 10 mil. O percentual ao lado de cashback ou pontos é o retorno efetivo sobre o gasto. Fonte: Comparativo econômico das propostas de valor, pesquisa de ${CMP.date.split('-').reverse().join('/')}. Valores da faixa mais próxima (patrimônio de R$ 5 mil em R$ 5 mil, gasto de R$ 500 em R$ 500).</p></div>`;
}
""" + s[b:]

rep("    case 'cmpopen': document.body.classList.toggle('cmpopen'); break;",
    "    case 'cmpopen': document.body.classList.toggle('cmpopen'); break;\n    case 'cmpbank': { const o = S.cmpOff || (S.cmpOff = {}); if (x === '*') S.cmpOff = {}; else if (x === '-') CMP.inst.forEach(b => o[b] = true); else o[x] = !o[x]; } break;")
rep("#cmp .gap{", """.cr .sb{grid-column:1/-1;display:flex;gap:2px;height:7px;margin-top:9px;border-radius:4px;overflow:hidden;transition:width .5s cubic-bezier(.2,.8,.2,1)}
.cr .sb i{display:block;min-width:3px;border-radius:2px}
.k1{--k:#FFC709} .k2{--k:#7BE3A8} .k3{--k:#8FA8FF} .k4{--k:#FF8A7A}
.sb i,.lg i{background:var(--k)}
.cr .tg{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:4px 5px;margin-top:7px}
.cr .tg em{font-style:normal;font-size:10.5px;font-weight:650;line-height:1;padding:4px 7px;border-radius:999px;color:var(--k,#8A8A92);background:color-mix(in srgb,var(--k,#8A8A92) 14%,transparent);white-space:nowrap}
.cr{padding-bottom:10px}
.cr .bar{display:none}
#cmp .lg{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:11px;color:#9A9AA2;margin:-4px 0 14px}
#cmp .lg span{display:inline-flex;align-items:center;gap:5px} #cmp .lg i{width:8px;height:8px;border-radius:50%}
#cmp .fb{font-size:11px;font-weight:700;letter-spacing:0;text-transform:none;color:#F4F4F2;background:#1A1A1D;border:1px solid #3A3A40;border-radius:999px;padding:4px 10px}
#cmp .fbx{display:flex;flex-wrap:wrap;gap:5px;background:#141416;border-radius:14px;padding:10px;margin-bottom:8px}
#cmp .fba{width:100%;display:flex;gap:6px;margin-bottom:3px}
#cmp .fba button{font-size:11px;font-weight:650;color:#C9C9CF;border:1px solid #3A3A40;border-radius:999px;padding:3px 10px}
#cmp .chb{font-size:11.5px;font-weight:650;padding:5px 9px;border-radius:999px;background:#1F1F23;color:#77777F}
#cmp .chb.on{background:rgba(255,199,9,.16);color:#FFC709;box-shadow:inset 0 0 0 1px rgba(255,199,9,.5)}
#cmp .gap{""")
open(p, 'w', encoding='utf-8').write(s)
print('ok', len(s))
