// Grade do comparador para o protótipo, com a composição do valor de cada oferta.
// Para cada ponto (patrimônio × gasto no cartão) e cada instituição guarda a melhor modalidade pelo valor total (n)
// e, quando for outra, a melhor só pelo lado financeiro (f). Entrada: [modalidade, dinheiro de volta, tipo (1 cashback, 2 pontos),
// rendimento extra, % do CDI, serviços, mensalidade], em R$ por mês arredondados.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext(); await ctx.route(/^https?:/, r => r.abort());
  const p = await ctx.newPage(); await p.goto('file://' + process.argv[2]); await p.waitForTimeout(2000);
  const out = await p.evaluate(() => {
    const inst = [...new Set(db.products.map(x => x.institution))].filter(i => i !== 'Rico');
    const prod = [], pidx = {}; const pid = q => { const k = q.product.id; if (!(k in pidx)) { pidx[k] = prod.length; prod.push(q.product.name.replace(' (disponibilidade a confirmar)', '')); } return pidx[k]; };
    const entry = q => {
      const it = q.items.filter(i => i.selected !== false && i.amount > 0);
      const y = it.filter(i => i.b.category === 'yield'), yld = y.reduce((a, i) => a + i.amount, 0), top = y.sort((a, c) => c.amount - a.amount)[0];
      const cb = it.filter(i => i.b.category === 'cashback').reduce((a, i) => a + i.amount, 0), pt = it.filter(i => i.b.category === 'points').reduce((a, i) => a + i.amount, 0);
      return [pid(q), Math.round(q.direct - yld), cb >= pt && cb > 0 ? 1 : pt > 0 ? 2 : 0, Math.round(yld), top && top.b.value > 100 ? Math.round(top.b.value) : 0, Math.round(q.services), Math.round(q.cost.value)];
    };
    const AUC = [], TPV = []; for (let a = 0; a <= 100000; a += 5000) AUC.push(a); for (let t = 0; t <= 10000; t += 500) TPV.push(t);
    const N = [], F = [];
    for (const a of AUC) for (const t of TPV) {
      const prof = E.profile({ ...state.profile, auc: a, tpv: t, balance: Math.min(a, 10000), previousTpv: t, averageTpv: t });
      const all = E.rank({ ...db, products: db.products.filter(x => x.institution !== 'Rico') }, prof, false).all.filter(q => q.rankable && q.net != null);
      const n = [], f = [];
      inst.forEach((name, i) => {
        const mine = all.filter(q => q.product.institution === name);
        if (!mine.length) { n.push(0); return; }
        const bn = mine.slice().sort((x, y) => y.net - x.net)[0], bf = mine.slice().sort((x, y) => y.financialNet - x.financialNet)[0];
        n.push(entry(bn)); if (bf.product.id !== bn.product.id) f.push([i, ...entry(bf)]);
      });
      N.push(n); F.push(f);
    }
    return { aucStep: 5000, tpvStep: 500, nTpv: TPV.length, date: db.researchDate, inst, prod, n: N, f: F };
  });
  fs.writeFileSync('sim/grid3.json', JSON.stringify(out));
  console.log('pontos', out.n.length, 'instituições', out.inst.length, 'modalidades', out.prod.length, 'bytes', fs.statSync('sim/grid3.json').size);
  const k = (30000 / 5000) * out.nTpv + 5000 / 500;
  out.n[k].forEach((e, i) => e && console.log(out.inst[i].padEnd(16), out.prod[e[0]].padEnd(38), JSON.stringify(e.slice(1)), 'líquido', e[1] + e[3] + e[5] - e[6]));
  console.log('fin', JSON.stringify(out.f[k].map(e => [out.inst[e[0]], out.prod[e[1]], ...e.slice(2)])));
  await b.close();
})();
