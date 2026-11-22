// Grade do comparador para o protótipo: patrimônio × gasto no cartão, em dois critérios (tudo / só financeiro).
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext(); await ctx.route(/^https?:/, r => r.abort());
  const p = await ctx.newPage(); await p.goto('file://' + process.argv[2]); await p.waitForTimeout(2000);
  const out = await p.evaluate(() => {
    const names = [], idx = {}; const id = (inst, name) => { const k = inst + '|' + name; if (!(k in idx)) { idx[k] = names.length; names.push([inst, name.replace(' (disponibilidade a confirmar)', '')]); } return idx[k]; };
    const AUC = [], TPV = []; for (let a = 0; a <= 100000; a += 2500) AUC.push(a); for (let t = 0; t <= 10000; t += 500) TPV.push(t);
    const modes = { all: q => q.net, fin: q => q.financialNet }, rows = { all: [], fin: [] };
    for (const a of AUC) for (const t of TPV) {
      const prof = E.profile({ ...state.profile, auc: a, tpv: t, balance: Math.min(a, 10000), previousTpv: t, averageTpv: t });
      const all = E.rank(analysisDB(), prof, false).all.filter(q => q.rankable);
      for (const m in modes) {
        const v = modes[m], s = all.filter(q => v(q) != null).sort((x, y) => v(y) - v(x));
        const xp = s.find(q => q.product.institution === 'XP');
        const seen = new Set(), riv = [];
        for (const q of s) { const i = q.product.institution; if (['XP', 'Rico', 'XP simulada'].includes(i) || seen.has(i)) continue; seen.add(i); riv.push(q); if (riv.length === 5) break; }
        const row = [xp ? id('XP', xp.product.name) : -1, xp ? Math.round(v(xp)) : 0];
        for (const q of riv) row.push(id(q.product.institution, q.product.name), Math.round(v(q)));
        rows[m].push(row);
      }
    }
    return { aucStep: 2500, tpvStep: 500, nTpv: TPV.length, date: (typeof db !== 'undefined' && db.researchDate) || '', names, all: rows.all, fin: rows.fin };
  });
  fs.writeFileSync('sim/grid.json', JSON.stringify(out));
  console.log('pontos', out.all.length, 'nomes', out.names.length, 'bytes', fs.statSync('sim/grid.json').size, 'data', out.date);
  const show = (m, a, t) => console.log(m, a, t, JSON.stringify(out[m][(a / 2500) * out.nTpv + t / 500].map((v, i) => i % 2 ? v : (out.names[v] || ['-', '-']).join(' · '))));
  for (const [a, t] of [[30000, 5000], [25000, 7500], [2500, 500], [100000, 10000], [0, 0]]) { show('all', a, t); show('fin', a, t); }
  await b.close();
})();
