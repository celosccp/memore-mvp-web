// Grade para o benchmark interativo: por ponto e por instituição, as modalidades que vencem em alguma combinação
// dos componentes (cashback/pontos, caixinha, salas VIP, outros serviços, com ou sem mensalidade).
// Entrada: [modalidade, dinheiro de volta, tipo, rendimento extra, % do CDI, salas VIP, outros serviços, mensalidade,
// itens ([nome, categoria, R$ por mês, taxa, pontos]), regra da mensalidade, situação da mensalidade], em R$ por mês.
// Situação: 0 sem mensalidade, 1 isento neste perfil, 2 pago e sem regra de isenção, 3 tem regra de isenção e o perfil não atinge.
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
    // Por enquanto a XP entra só com o Investback: os pontos (XP → Livelo) ficam fora da conta em todos os cartões da XP.
    db.products.filter(q => q.institution === 'XP').forEach(q => { q.benefits = q.benefits.filter(x => x.category !== 'points'); });
    const inst = [...new Set(db.products.map(x => x.institution))].filter(i => i !== 'Rico');
    const prod = [], pidx = {}; const pid = q => { const k = q.product.id; if (!(k in pidx)) { pidx[k] = prod.length; prod.push(q.product.name.replace(' (disponibilidade a confirmar)', '')); } return pidx[k]; };
    const itn = [], itx = {}, cds = [], cdx = {}, CAT = { cashback: 0, points: 1, yield: 2, banking: 3, lounge: 4 };
    const dict = (arr, map, k) => { if (!(k in map)) { map[k] = arr.length; arr.push(k); } return map[k]; };
    const temRegra = x => { const f = x.fee || {}; return (f.waivers || []).length > 0 || f.discountPer10kAuc > 0 || f.discountPer1kTpv > 0 || (f.addons || []).length > 0 || (f.variants || []).length > 0; };
    const situ = q => { const pago = Math.round(q.cost.value) > 0, base = (q.product.fee.monthly || 0) > 0 || (q.product.fee.addons || []).length > 0; return !pago ? (base ? 1 : 0) : temRegra(q.product) ? 3 : 2; };
    const entry = q => {
      const it = q.items.filter(i => i.selected !== false && i.amount > 0);
      const sum = c => it.filter(i => i.b.category === c).reduce((a, i) => a + i.amount, 0);
      const yld = sum('yield'), lounge = sum('lounge'), top = it.filter(i => i.b.category === 'yield').sort((a, c) => c.amount - a.amount)[0];
      const cb = sum('cashback'), pt = sum('points');
      return [pid(q), Math.round(q.direct - yld), cb >= pt && cb > 0 ? 1 : pt > 0 ? 2 : 0, Math.round(yld), top && top.b.value > 100 ? Math.round(top.b.value) : 0, Math.round(lounge), Math.round(q.services - lounge), Math.round(q.cost.value),
        // item: [nome, categoria, R$ por mês, taxa, pontos no mês, pontua por dólar (1) ou por real (0), alternativa não somada (1)]
        [...it.map(i => [i, 0]), ...q.items.filter(i => i.selected === false && i.excludedValue > 0).map(i => [i, 1])].map(([i, alt]) => {
          const cat = i.b.category in CAT ? CAT[i.b.category] : 5, pts = alt && cat === 1 ? Math.round((parseFloat(String(i.formula || '').replace(/\./g, '').replace(',', '.')) || 0)) : Math.round(i.points || 0);
          return [dict(itn, itx, i.b.name), cat, Math.round((alt ? i.excludedValue : i.amount) * 100) / 100, cat <= 1 && typeof i.rate === 'number' ? i.rate : typeof i.b.value === 'number' ? i.b.value : 0, pts, i.b.per === 'USD' ? 1 : 0, alt]; }),
        dict(cds, cdx, q.cost.detail || ''), situ(q)];
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
        for (const uni of [mine.map((e, i) => i), mine.map((e, i) => i).filter(i => mine[i][10] !== 3)]) {   // todos os cartões, e só os disponíveis sem pagar por regra não atingida
          if (!uni.length) continue;
          for (let m = 0; m < 32; m++) { const v = e => (m & 1 ? e[1] : 0) + (m & 2 ? e[3] : 0) + (m & 4 ? e[5] : 0) + (m & 8 ? e[6] : 0) - (m & 16 ? e[7] : 0);
            let best = uni[0]; uni.forEach(i => { if (v(mine[i]) > v(mine[best])) best = i; }); keep.add(best); } }
        return [...keep].map(i => mine[i]);
      });
    }
    return { auc: AUC, tpv: TPV, inst, prod, itn, cds, pts, date: db.researchDate, cdi: prof0.cdi, tax: prof0.tax, usd: prof0.usd, loungeUsd: prof0.loungeUsd, mile: prof0.mileValue };
  });
  fs.writeFileSync('sim/grid5.json', JSON.stringify(out));
  const n = Object.values(out.pts).flat().filter(Boolean).map(x => x.length);
  console.log('pontos', Object.keys(out.pts).length, 'bytes', fs.statSync('sim/grid5.json').size, 'candidatos por instituição: média', (n.reduce((a, c) => a + c, 0) / n.length).toFixed(2), 'máx', Math.max(...n));
  for (const k of ['30000|5000', '10000|5000']) console.log(k, 'XP', out.pts[k][out.inst.indexOf('XP')].map(x => out.prod[x[0]] + ' ' + JSON.stringify(x[8].map(i => [out.itn[i[0]], ...i.slice(1)]))).join(' || '));
  console.log('milheiro', out.mile, 'modalidades', out.prod.length);
  await b.close();
})();
