// Grade para o benchmark interativo: por ponto e por instituição, as modalidades que vencem em alguma combinação
// dos componentes (cashback/pontos, caixinha, salas VIP, outros serviços, com ou sem mensalidade).
// Entrada: [modalidade, dinheiro de volta, tipo, rendimento extra, % do CDI, salas VIP, outros serviços, mensalidade,
// itens ([nome, categoria, R$ por mês, taxa]), regra da mensalidade], em R$ por mês. Nomes e regras vão em dicionários.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext(); await ctx.route(/^https?:/, r => r.abort());
  const p = await ctx.newPage(); await p.goto('file://' + process.argv[2]); await p.waitForTimeout(2000);
  const out = await p.evaluate(() => {
    // Regra da XP usada no benchmark: XP One com Investback de 0,8% a partir de R$ 2.500 de gasto e de 1% a partir de R$ 5.000.
    { const cash = db.products.find(q => q.id === 'xp_one').benefits.find(x => x.id === 'xp_one_cash');
      cash.tiers[0] = { when: { field: 'tpv', op: 'gte', value: 2500 }, value: 0.8 };
      cash.tiers[1] = { when: { field: 'tpv', op: 'gte', value: 5000 }, value: 1 };
      cash.tiers[2].when.all[0].value = 2500; }
    const inst = [...new Set(db.products.map(x => x.institution))].filter(i => i !== 'Rico');
    const prod = [], pidx = {}; const pid = q => { const k = q.product.id; if (!(k in pidx)) { pidx[k] = prod.length; prod.push(q.product.name.replace(' (disponibilidade a confirmar)', '')); } return pidx[k]; };
    const itn = [], itx = {}, cds = [], cdx = {}, CAT = { cashback: 0, points: 1, yield: 2, banking: 3, lounge: 4 };
    const dict = (arr, map, k) => { if (!(k in map)) { map[k] = arr.length; arr.push(k); } return map[k]; };
    const entry = q => {
      const it = q.items.filter(i => i.selected !== false && i.amount > 0);
      const sum = c => it.filter(i => i.b.category === c).reduce((a, i) => a + i.amount, 0);
      const yld = sum('yield'), lounge = sum('lounge'), top = it.filter(i => i.b.category === 'yield').sort((a, c) => c.amount - a.amount)[0];
      const cb = sum('cashback'), pt = sum('points');
      return [pid(q), Math.round(q.direct - yld), cb >= pt && cb > 0 ? 1 : pt > 0 ? 2 : 0, Math.round(yld), top && top.b.value > 100 ? Math.round(top.b.value) : 0, Math.round(lounge), Math.round(q.services - lounge), Math.round(q.cost.value),
        it.map(i => [dict(itn, itx, i.b.name), i.b.category in CAT ? CAT[i.b.category] : 5, Math.round(i.amount * 100) / 100, typeof i.b.value === 'number' ? i.b.value : 0, Math.round(i.points || 0)]),
        dict(cds, cdx, q.cost.detail || '')];
    };
    const AUC = [5000, 10000, 15000, 30000, 50000, 75000, 100000], TPV = [500, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7500, 10000];
    const pts = {}, prof0 = E.profile({ ...state.profile, mileValue: 30 });
    for (const a of AUC) for (const t of TPV) {
      const prof = E.profile({ ...state.profile, mileValue: 30, auc: a, tpv: t, balance: Math.min(a, 10000), previousTpv: t, averageTpv: t });
      // ficam de fora os pacotes de pontos comprados (paga-se mais do que os pontos valem): não são benefício do cartão
      const comprado = x => x.benefits.some(bn => /pontos (mensais contratados|bônus mensais)/i.test(bn.name));
      const all = E.rank({ ...db, products: db.products.filter(x => x.institution !== 'Rico' && !comprado(x)) }, prof, false).all.filter(q => q.rankable && q.net != null);
      pts[a + '|' + t] = inst.map(name => {
        const mine = all.filter(q => q.product.institution === name).map(entry); if (!mine.length) return 0;
        const keep = new Set();
        for (let m = 0; m < 32; m++) { const v = e => (m & 1 ? e[1] : 0) + (m & 2 ? e[3] : 0) + (m & 4 ? e[5] : 0) + (m & 8 ? e[6] : 0) - (m & 16 ? e[7] : 0);
          let best = 0; mine.forEach((e, i) => { if (v(e) > v(mine[best])) best = i; }); keep.add(best); }
        return [...keep].map(i => mine[i]);
      });
    }
    return { auc: AUC, tpv: TPV, inst, prod, itn, cds, pts, date: db.researchDate, cdi: prof0.cdi, tax: prof0.tax, usd: prof0.usd, loungeUsd: prof0.loungeUsd, mile: prof0.mileValue };
  });
  fs.writeFileSync('sim/grid5.json', JSON.stringify(out));
  const n = Object.values(out.pts).flat().filter(Boolean).map(x => x.length);
  console.log('pontos', Object.keys(out.pts).length, 'bytes', fs.statSync('sim/grid5.json').size, 'candidatos por instituição: média', (n.reduce((a, c) => a + c, 0) / n.length).toFixed(2), 'máx', Math.max(...n));
  for (const k of ['10000|1000', '10000|5000', '50000|7500']) console.log(k, out.pts[k][out.inst.indexOf('C6 Bank')].map(x => out.prod[x[0]] + ' ' + JSON.stringify(x.slice(1, 8)) + ' ' + JSON.stringify(x[8].map(i => [out.itn[i[0]], i[2], i[4]]))).join('  ||  '));
  console.log('milheiro', out.mile, 'modalidades', out.prod.length);
  await b.close();
})();
