// Gravação do protótipo para a cena do app: um fluxo só, em ritmo calmo.
// Usar → escolhe 110% no Cofre XP → confirma → volta com o benefício ativo → aba Juntar → desce a lista.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 468, height: 960 }, deviceScaleFactor: 1, recordVideo: { dir: 'rec2', size: { width: 468, height: 960 } } });
  const p = await ctx.newPage();
  const tv = Date.now();
  await p.goto('file:///home/user/memore-mvp-web/xp-loyalty/index.html');
  await p.addStyleTag({ content: '#panelToggle,.btn.demo{display:none!important} #tapdot{position:fixed;width:48px;height:48px;margin:-24px 0 0 -24px;border-radius:50%;background:rgba(255,255,255,.35);border:2px solid rgba(255,255,255,.85);pointer-events:none;z-index:99;opacity:0;transition:opacity .22s,transform .22s;transform:scale(1.5)} #tapdot.on{opacity:1;transform:scale(1)}' });
  await p.evaluate(() => { const d = document.createElement('div'); d.id = 'tapdot'; document.body.appendChild(d); act('theme:dark'); act('enter'); });
  const marks = {};
  const now = () => (Date.now() - tv) / 1000;
  const tap = async (name, sel, wait) => {
    const el = p.locator(sel).first(); const bx = await el.boundingBox();
    const x = bx.x + bx.width / 2, y = bx.y + bx.height / 2;
    await p.evaluate(([x, y]) => { const d = document.getElementById('tapdot'); d.style.left = x + 'px'; d.style.top = y + 'px'; d.classList.add('on'); }, [x, y]);
    await p.waitForTimeout(420);
    await p.mouse.click(x, y); marks[name] = now();
    await p.evaluate(() => document.getElementById('tapdot').classList.remove('on'));
    await p.waitForTimeout(wait);
  };
  await p.waitForTimeout(900); marks.start = now();
  await p.waitForTimeout(1300);
  await tap('ponto', '[data-a="sheet:confirm:cofrinho:c110"]', 1500);
  await tap('ativar', '.sheet .btn', 2600);
  await tap('voltar', '.sheet .btn', 1500);
  await tap('juntar', '[data-a="go:juntar"]', 1300);
  marks.rola = now();
  await p.evaluate(() => { const s = document.querySelector('.scr'); const t0 = performance.now(); const go = t => { const k = Math.min(1, (t - t0) / 1600); s.scrollTop = 330 * (k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2); if (k < 1) requestAnimationFrame(go); }; requestAnimationFrame(go); });
  await p.waitForTimeout(2600); marks.end = now();
  console.log(JSON.stringify(marks));
  await ctx.close(); await b.close();
})();
