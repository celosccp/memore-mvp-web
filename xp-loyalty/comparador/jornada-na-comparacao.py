"""Comparação, versão 3: top 10 e a linha da Jornada XP calculada a partir do que está ativo no app."""
p = '/home/user/memore-mvp-web/xp-loyalty/index.html'; s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:90]); s = s.replace(a, b)

rep("function renderCmp(){", """// Valor da Jornada XP como está simulada no app, nas mesmas premissas do comparador:
// CDI de 14,9% ao ano, 22,5% de imposto sobre o rendimento, sala VIP a US$ 50 por acesso com dólar a R$ 5,50; corretagem a R$ 3,50 por ordem (planilha do simulador).
const CMPX = { cdi: 14.9, tax: 22.5, usd: 5.5, loungeUsd: 50, ordem: 3.5, saldoMax: 10000 };
function jornadaEntry(mode){
  const card = activeCard(), on = f => S.active[f] && S.active[f].status === 'active' ? S.active[f].opt : null;
  const ib = investbackNow(), cof = on('cofrinho'), taxa = cof ? +cof.slice(1) : P.cofBase, cz = on('corretagem'), ordens = cz ? +cz.slice(2) : 0, acessos = salaNow(card, true).n;
  const mes = Math.pow(1 + CMPX.cdi / 100, 1 / 12) - 1;
  const yld = Math.round(Math.min(S.auc, CMPX.saldoMax) * mes * Math.max(0, taxa - 100) / 100 * (1 - CMPX.tax / 100));
  const cash = Math.round(ib.valor), serv = mode === 'fin' ? 0 : Math.round(ordens * CMPX.ordem + acessos * CMPX.loungeUsd * CMPX.usd / 12);
  const partes = [ordens ? `${ordens} ordens sem corretagem` : '', acessos ? `${acessos} acessos a salas VIP` : ''].filter(Boolean).join(' e ');
  return { banco: 'XP', nome: `${card === 'infinite' ? 'XP Infinite' : 'XP One'} · como está no app`, cash, kind: 1, yld, cdi: taxa > 100 ? taxa : 0, serv, cost: 0, bruto: cash + yld + serv, v: cash + yld + serv,
    tpv: S.gasto, lab: { cash: 'Investback', yld: 'Cofre XP', serv: partes ? partes.charAt(0).toUpperCase() + partes.slice(1) : 'Serviços' }, vazio: 'Nenhum benefício ativo. Ative no app para ver o valor subir.' };
}
function renderCmp(){""")
rep("const riv = list.filter(r => r.banco !== 'XP' && !off[r.banco]).sort((x, y) => y.v - x.v).slice(0, 5);",
    "const riv = list.filter(r => r.banco !== 'XP' && !off[r.banco]).sort((x, y) => y.v - x.v).slice(0, 10), jx = jornadaEntry(mode);")
rep("const top = Math.max(1, xp ? xp.bruto : 0, ...riv.map(r => r.bruto));", "const top = Math.max(1, jx.bruto, xp ? xp.bruto : 0, ...riv.map(r => r.bruto));")
rep("const pct = v => tpv ? ' ' + (v / tpv * 100).toFixed(1).replace('.', ',').replace(',0', '') + '%' : '';",
    "const pct = (v, base = tpv) => base ? ' ' + (v / base * 100).toFixed(1).replace('.', ',').replace(',0', '') + '%' : '';")
rep("""<em class="k1">${r.kind === 2 ? 'Pontos' : r.kind === 1 ? 'Cashback' : 'Conta'}${r.kind ? pct(r.cash) : ''} · ${brl(r.cash)}</em>""",
    """<em class="k1">${r.lab ? r.lab.cash : r.kind === 2 ? 'Pontos' : r.kind === 1 ? 'Cashback' : 'Conta'}${r.kind ? pct(r.cash, r.tpv) : ''} · ${brl(r.cash)}</em>""")
rep("""<em class="k2">Caixinha${r.cdi ? ' ' + r.cdi + '% CDI' : ''} · ${brl(r.yld)}</em>""", """<em class="k2">${r.lab ? r.lab.yld : 'Caixinha'}${r.cdi ? ' ' + r.cdi + '% CDI' : ''} · ${brl(r.yld)}</em>""")
rep("""<em class="k3">Serviços · ${brl(r.serv)}</em>""", """<em class="k3">${r.lab ? r.lab.serv : 'Serviços'} · ${brl(r.serv)}</em>""")
rep("""${r.bruto <= 0 && r.cost <= 0 ? '<em>Sem valor estimado neste perfil</em>' : ''}""", """${r.bruto <= 0 && r.cost <= 0 ? `<em>${r.vazio || 'Sem valor estimado neste perfil'}</em>` : ''}""")
rep("const melhor = riv[0], dif = melhor && xp ? melhor.v - xp.v : 0, pos = xp ? riv.filter(r => r.v > xp.v).length + 1 : null, aberto = isOpen('cmpf');",
    "const melhor = riv[0], dif = melhor ? melhor.v - jx.v : 0, pos = riv.filter(r => r.v > jx.v).length + 1, ganho = xp ? jx.v - xp.v : jx.v, aberto = isOpen('cmpf');")
rep("""    <div class="gl">XP hoje</div>
    ${xp ? row({ ...xp, nome: xp.nome + ' · regra atual' }, '<i>XP</i>', 'xp')""",
"""    <div class="gl">Jornada XP · simulação no app</div>
    ${row(jx, '<i>XP</i>', 'xp')}
    <div class="gl">XP hoje</div>
    ${xp ? row({ ...xp, nome: xp.nome + ' · regra atual' }, '<i>XP</i>', 'xp ref')""")
rep("""<div class="cr xp"><div class="rk"><i>XP</i></div><div style="min-width:0"><b>Sem cartão elegível</b>""", """<div class="cr xp ref"><div class="rk"><i>XP</i></div><div style="min-width:0"><b>Sem cartão elegível</b>""")
rep("Top ${riv.length || 5} fora da XP", "Top ${riv.length || 10} fora da XP")
a = s.index("    ${melhor ? `<div class=\"gap\">${dif > 0 ?"); b = s.index("\n", a)
s = s[:a] + """    ${melhor ? `<div class="gap">${dif > 0 ? `Com a Jornada XP como está no app, a XP ficaria em <b>${pos}º</b> entre ${riv.length + 1}. A melhor oferta ${ligados.length < bancos.length ? 'entre os bancos escolhidos' : 'de fora'} entrega <b>${brl(dif)}</b> a mais por mês.` : `Com a Jornada XP como está no app, a XP entrega mais que ${ligados.length < bancos.length ? 'os bancos escolhidos' : 'todas as ofertas de fora'}.`}${xp ? ` Em relação à regra de hoje, ${ganho > 0 ? `são <b>${brl(ganho)}</b> a mais` : ganho < 0 ? `são <b>${brl(-ganho)}</b> a menos` : 'o valor é o mesmo'}.` : ''}</div>` : ''}""" + s[b:]
rep("Fonte: Comparativo econômico das propostas de valor,", "A linha da Jornada XP soma o que está ativo no app, nas mesmas premissas: CDI de 14,9% ao ano com 22,5% de imposto, sala VIP a US$ 50 por acesso e corretagem a R$ 3,50 por ordem. Fonte: Comparativo econômico das propostas de valor,")
rep(".cr.xp .rk{color:#FFC709}", ".cr.xp.ref{background:#141416;box-shadow:inset 0 0 0 1px #3A3A40}\n.cr.xp .rk{color:#FFC709}")
open(p, 'w', encoding='utf-8').write(s); print('ok')
