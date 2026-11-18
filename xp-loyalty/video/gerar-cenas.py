import os, random, json
V='/home/user/memore-mvp-web/xp-loyalty/video'
os.makedirs(V+'/compositions',exist_ok=True)
BASE='''
    #root{position:absolute;inset:0;font-family:Inter,sans-serif;color:#F4F4F2;overflow:hidden}
    .bg{position:absolute;inset:0;background:radial-gradient(70% 60% at 18% 0%,#5a421a 0%,#2a1e0e 38%,#0b0b0c 78%)}
    .h{font-weight:900;letter-spacing:-.035em;line-height:1.04}
    .y{color:#FFC709}
    .mut{color:#A3A3A8}
'''
def scene(sid,dur,css,html,js):
    open(f'{V}/compositions/{sid}.html','w',encoding='utf-8').write(f'''<template>
  <style>{BASE}{css}</style>
  <div id="root" data-composition-id="{sid}" data-width="1920" data-height="1080">
    <div class="bg"></div>
{html}
  </div>
  <script>
    (function(){{
      const tl = gsap.timeline({{ paused: true }});
{js}
      tl.fromTo("#{sid}-all", {{ opacity: 1 }}, {{ opacity: 0, duration: 0.45, ease: "power2.in" }}, {dur-0.55});
      window.__timelines["{sid}"] = tl;
    }})();
  </script>
</template>
''')
SC=[]
def add(sid,dur,css,html,js): SC.append((sid,dur)); scene(sid,dur,css,html,js)

# 1 abertura
waves=''.join(f'<path id="s1-w{i}" d="M-40 {160+i*46} C 420 {20+i*46}, 980 {420+i*40}, 1980 {80+i*52}" pathLength="1" stroke-dasharray="1" />' for i in range(14))
add('s1',5,'''
    #s1-all{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:44px}
    #s1-art{position:absolute;inset:0;width:100%;height:100%}
    #s1-logo{width:190px;height:158px;border-radius:30px;background:#fff;color:#111;font-weight:900;font-size:84px;letter-spacing:-.05em;display:flex;align-items:center;justify-content:center}
    #s1-name{font-size:120px}
''',f'''    <svg id="s1-art" viewBox="0 0 1920 1080" fill="none" stroke="#FFC709" stroke-opacity=".3" stroke-width="2">{waves}</svg>
    <div id="s1-all" class="clip" data-start="0" data-duration="5" data-track-index="0">
      <div id="s1-logo">XP</div>
      <div id="s1-name" class="h" data-var-text="programa">Jornada XP</div>
    </div>''',
'''      for (let i = 0; i < 14; i++) tl.fromTo("#s1-w" + i, { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 2.2, ease: "power2.out" }, 0.05 * i);
      tl.fromTo("#s1-logo", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.7, ease: "back.out(1.7)" }, 0.5);
      tl.fromTo("#s1-name", { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 1.1);
      tl.fromTo("#s1-art", { opacity: 1 }, { opacity: 0, duration: 0.45 }, 4.45);''')

# 2 mote
words="Sua vida financeira,|uma conquista|de cada vez.".split('|')
add('s2',7,'''
    #s2-all{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 170px}
    .s2-l{font-size:150px;overflow:hidden;padding-bottom:14px}
    .s2-l span{display:inline-block}
''','    <div id="s2-all" class="clip" data-start="0" data-duration="7" data-track-index="0">\n'+''.join(f'      <div class="s2-l h"><span id="s2-w{i}" class="{"y" if i==1 else ""}">{w}</span></div>\n' for i,w in enumerate(words))+'    </div>',
'''      for (let i = 0; i < 3; i++) tl.fromTo("#s2-w" + i, { yPercent: 110 }, { yPercent: 0, duration: 0.9, ease: "power4.out" }, 0.3 + i * 0.75);''')

# 3 momentos: quatro frentes, sem ordem obrigatória
M=[('Planeje sua vida financeira','Organize contas, gastos e objetivos.'),('Comece a poupar','Guarde um pouco todo mês, no seu ritmo.'),('Otimize seu dia a dia','Faça o dinheiro do mês render mais.'),('Acelere e proteja seus planos','Vá mais longe quando fizer sentido.')]
cards=''.join(f'<div class="s3-c" id="s3-c{i}"><i id="s3-g{i}"></i><b>{t}</b><span>{d}</span></div>' for i,(t,d) in enumerate(M))
add('s3',8,"""
    #s3-all{position:absolute;inset:0;padding:96px 150px}
    #s3-h{font-size:96px}
    #s3-s{font-size:42px;color:#A3A3A8;margin-top:20px}
    #s3-grid{position:absolute;left:150px;right:150px;top:420px;bottom:96px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:28px}
    .s3-c{position:relative;border-radius:40px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.08);padding:38px 46px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}
    .s3-c i{position:absolute;inset:0;border-radius:38px;border:5px solid #FFC709;background:rgba(255,199,9,.1);opacity:0}
    .s3-c b{position:relative;font-size:66px;font-weight:900;letter-spacing:-.03em;line-height:1.05}
    .s3-c span{position:relative;font-size:38px;color:#A3A3A8;margin-top:12px}
""",f"""    <div id="s3-all" class="clip" data-start="0" data-duration="8" data-track-index="0">
      <div id="s3-h" class="h">Rumo à sua <span class="y">autonomia financeira.</span></div>
      <div id="s3-s">Quatro frentes. Comece por onde fizer sentido para você.</div>
      <div id="s3-grid">{cards}</div>
    </div>""",
"""      tl.fromTo("#s3-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.15);
      tl.fromTo("#s3-s", { opacity: 0 }, { opacity: 1, duration: 0.5 }, 0.7);
      const from = [{ x: -120, y: -60 }, { x: 120, y: -60 }, { x: -120, y: 60 }, { x: 120, y: 60 }];
      for (let i = 0; i < 4; i++) tl.fromTo("#s3-c" + i, { opacity: 0, x: from[i].x, y: from[i].y, scale: 0.9 }, { opacity: 1, x: 0, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)" }, 1.0 + i * 0.12);
      // o destaque passeia fora de ordem: qualquer frente pode ser a primeira
      [2, 0, 3, 1].forEach((k, n) => {
        tl.fromTo("#s3-g" + k, { opacity: 0 }, { opacity: 1, duration: 0.25, ease: "power2.out" }, 2.3 + n * 1.15);
        tl.fromTo("#s3-c" + k, { scale: 1 }, { scale: 1.04, duration: 0.25, ease: "power2.out", immediateRender: false }, 2.3 + n * 1.15);
        tl.fromTo("#s3-g" + k, { opacity: 1 }, { opacity: 0, duration: 0.35, immediateRender: false }, 3.15 + n * 1.15);
        tl.fromTo("#s3-c" + k, { scale: 1.04 }, { scale: 1, duration: 0.35, immediateRender: false }, 3.15 + n * 1.15);
      });""")

# 4 fichas
add('s4',7,'''
    #s4-all{position:absolute;inset:0}
    #s4-txt{position:absolute;left:170px;top:210px;width:920px}
    #s4-h{font-size:104px}
    #s4-num{display:flex;align-items:flex-end;gap:26px;margin-top:90px}
    #s4-n{font-size:260px;font-weight:900;letter-spacing:-.05em;line-height:.85;min-width:300px}
    #s4-u{font-size:60px;font-weight:700;padding-bottom:14px}
    #s4-bar{height:22px;border-radius:12px;background:rgba(255,255,255,.12);margin-top:40px;overflow:hidden;width:820px}
    #s4-fill{height:100%;width:100%;background:#7BE3A8;border-radius:12px;transform-origin:0 50%}
    #s4-ph{position:absolute;right:210px;top:70px;height:940px;border-radius:64px;box-shadow:0 50px 120px rgba(0,0,0,.6)}
''','''    <div id="s4-all" class="clip" data-start="0" data-duration="7" data-track-index="0">
      <div id="s4-txt">
        <div id="s4-h" class="h">Cada conquista<br>vira <span class="y">fichas.</span></div>
        <div id="s4-num"><div id="s4-n">0</div><div id="s4-u">fichas</div></div>
        <div id="s4-bar"><div id="s4-fill"></div></div>
      </div>
      <img id="s4-ph" src="assets/usar.png" alt="">
    </div>''',
'''      const c = { v: 0 }, n = document.querySelector("#s4-n");
      tl.fromTo("#s4-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.2);
      tl.fromTo("#s4-ph", { opacity: 0, y: 160 }, { opacity: 1, y: 0, duration: 1.1, ease: "power3.out" }, 0.5);
      tl.fromTo("#s4-num", { opacity: 0 }, { opacity: 1, duration: 0.4 }, 1.2);
      tl.fromTo(c, { v: 0 }, { v: 15, duration: 2.4, ease: "power2.out", onUpdate: () => { n.textContent = Math.round(c.v); } }, 1.4);
      tl.fromTo("#s4-fill", { scaleX: 0 }, { scaleX: 0.3, duration: 2.4, ease: "power2.out" }, 1.4);''')

# 5 regua
nodes=''.join(f'<div class="s5-n" style="left:{p}%"><i id="s5-d{i}"></i><b>{t}</b><span id="s5-s{i}">{s}</span></div>' for i,(p,t,s) in enumerate([(0,'100%','Incluído'),(33.333,'110%','10 fichas'),(66.666,'115%','15 fichas'),(100,'125%','30 fichas')]))
REEL=['Investback','Salas VIP','Corretagem zero','Cofre XP']*3
reel=''.join(f'<div>{t}</div>' for t in REEL)
add('s5',12.6,'''
    #s5-all{position:absolute;inset:0;padding:110px 170px}
    #s5-h{font-size:88px;max-width:1500px}
    #s5-reel{position:absolute;left:170px;right:170px;top:520px;height:230px;overflow:hidden;border-top:3px solid rgba(255,255,255,.14);border-bottom:3px solid rgba(255,255,255,.14)}
    #s5-col div{height:230px;line-height:230px;font-size:170px;font-weight:900;letter-spacing:-.04em;white-space:nowrap}
    #s5-col div:last-child{color:#FFC709}
    #s5-card{position:absolute;left:170px;right:170px;top:400px;height:540px;border-radius:56px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.08);padding:56px 90px}
    #s5-t{font-size:44px;font-weight:700;display:flex;justify-content:space-between;align-items:center}
    #s5-t em{font-style:normal;font-weight:400;color:#A3A3A8;margin-left:18px}
    #s5-chips{position:relative;width:420px;height:64px}
    .s5-chip{position:absolute;right:0;top:0;white-space:nowrap;font-size:34px;font-weight:700;background:#FFC709;color:#000;border-radius:999px;padding:10px 30px}
    #s5-big{position:relative;height:150px;margin-top:20px}
    #s5-big div{position:absolute;left:0;top:0;font-size:150px;font-weight:900;letter-spacing:-.04em;line-height:1}
    #s5-rg{position:relative;margin:70px 60px 0;height:150px}
    #s5-track{position:absolute;left:0;right:0;top:22px;height:12px;border-radius:6px;background:rgba(255,255,255,.14)}
    #s5-fill{position:absolute;left:0;right:0;top:22px;height:12px;border-radius:6px;background:#FFC709;transform-origin:0 50%}
    .s5-n{position:absolute;top:0;width:260px;margin-left:-130px;text-align:center}
    .s5-n i{display:block;width:56px;height:56px;border-radius:50%;margin:0 auto 18px;background:#1e1b17;border:7px solid #6E6E75}
    .s5-n b{display:block;font-size:44px;font-weight:700}
    .s5-n span{display:block;font-size:28px;color:#A3A3A8;margin-top:4px}
''',f'''    <div id="s5-all" class="clip" data-start="0" data-duration="11" data-track-index="0">
      <div id="s5-h" class="h">Com fichas, você escolhe<br>o que <span class="y">turbinar.</span></div>
      <div id="s5-reel" data-layout-allow-overflow><div id="s5-col">{reel}</div></div>
      <div id="s5-card">
        <div id="s5-t"><div>Cofre XP<em>% do CDI</em></div><div id="s5-chips"><span id="s5-c0" class="s5-chip">Incluído</span><span id="s5-c1" class="s5-chip">10 fichas em uso</span><span id="s5-c2" class="s5-chip">15 fichas em uso</span></div></div>
        <div id="s5-big"><div id="s5-b0">100%</div><div id="s5-b1" class="y">110%</div><div id="s5-b2" class="y">115%</div></div>
        <div id="s5-rg"><div id="s5-track"></div><div id="s5-fill"></div>{nodes}</div>
      </div>
    </div>''',
'''      const on = { backgroundColor: "#FFC709", borderColor: "#FFC709", duration: 0.3 }, off0 = { backgroundColor: "#1e1b17", borderColor: "#6E6E75" };
      tl.fromTo("#s5-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.2);
      // rolo de benefícios: gira rápido, desacelera e para no Cofre XP
      tl.fromTo("#s5-reel", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 0.6);
      tl.fromTo("#s5-col", { y: 0 }, { y: -230 * 11, duration: 1.7, ease: "power3.out" }, 0.6);
      tl.fromTo("#s5-reel", { opacity: 1, y: 0 }, { opacity: 0, y: -60, duration: 0.3, ease: "power2.in", immediateRender: false }, 2.75);
      tl.fromTo("#s5-card", { opacity: 0, y: 80 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 3.0);
      tl.fromTo("#s5-d0", off0, on, 3.3);
      tl.fromTo("#s5-fill", { scaleX: 0 }, { scaleX: 0.3333, duration: 1.3, ease: "power3.inOut" }, 4.9);
      tl.fromTo("#s5-d1", off0, on, 5.9);
      tl.fromTo("#s5-d1", { scale: 1 }, { scale: 1.35, duration: 0.25, yoyo: true, repeat: 1, ease: "power2.out" }, 5.9);
      tl.fromTo("#s5-fill", { scaleX: 0.3333 }, { scaleX: 0.6667, duration: 1.3, ease: "power3.inOut", immediateRender: false }, 8.3);
      tl.fromTo("#s5-d2", off0, on, 9.3);
      tl.fromTo("#s5-d2", { scale: 1 }, { scale: 1.35, duration: 0.25, yoyo: true, repeat: 1, ease: "power2.out" }, 9.3);
      tl.fromTo("#s5-b1", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 5.9);
      tl.fromTo("#s5-b0", { opacity: 1 }, { opacity: 0, duration: 0.3 }, 5.8);
      tl.fromTo("#s5-b2", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, 9.3);
      tl.fromTo("#s5-b1", { opacity: 1 }, { opacity: 0, duration: 0.3, immediateRender: false }, 9.2);
      tl.fromTo("#s5-c0", { opacity: 1 }, { opacity: 0, duration: 0.25 }, 5.8);
      tl.fromTo("#s5-c1", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 5.9);
      tl.fromTo("#s5-c1", { opacity: 1 }, { opacity: 0, duration: 0.25, immediateRender: false }, 9.2);
      tl.fromTo("#s5-c2", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 9.3);''')

# 6 trocar
add('s6',7,'''
    #s6-all{position:absolute;inset:0}
    #s6-h{position:absolute;left:170px;top:300px;width:900px;font-size:104px}
    #s6-s{position:absolute;left:170px;top:680px;font-size:44px;color:#A3A3A8;width:820px;line-height:1.3}
    #s6-ph{position:absolute;right:210px;top:70px;height:940px;border-radius:64px;box-shadow:0 50px 120px rgba(0,0,0,.6)}
''','''    <div id="s6-all" class="clip" data-start="0" data-duration="7" data-track-index="0">
      <div id="s6-h" class="h">Troque quando quiser.<br><span class="y">As fichas voltam.</span></div>
      <div id="s6-s">Investback, Salas VIP, Cofre XP e Corretagem zero, cada um na sua régua.</div>
      <img id="s6-ph" src="assets/usar-ativo.png" alt="">
    </div>''',
'''      tl.fromTo("#s6-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.2);
      tl.fromTo("#s6-ph", { opacity: 0, y: 160, scale: 1 }, { opacity: 1, y: 0, scale: 1, duration: 1.0, ease: "power3.out" }, 0.4);
      tl.fromTo("#s6-s", { opacity: 0 }, { opacity: 1, duration: 0.6 }, 1.6);
      tl.fromTo("#s6-ph", { scale: 1 }, { scale: 1.06, duration: 4.6, ease: "none", immediateRender: false }, 1.6);''')

# 7 infinite
add('s7',7,'''
    #s7-all{position:absolute;inset:0}
    #s7-h{position:absolute;left:170px;top:300px;width:900px;font-size:104px}
    #s7-chips{position:absolute;left:170px;top:700px;height:80px;width:900px}
    .s7-c{position:absolute;left:0;top:0;white-space:nowrap;font-size:40px;font-weight:700;border-radius:999px;padding:14px 36px}
    #s7-c0{border:3px solid #6E6E75;color:#A3A3A8}
    #s7-c1{background:#7BE3A8;color:#062b17}
    .s7-ph{position:absolute;right:210px;top:70px;height:940px;border-radius:64px}
    #s7-p0{box-shadow:0 50px 120px rgba(0,0,0,.6)}
''','''    <div id="s7-all" class="clip" data-start="0" data-duration="7" data-track-index="0">
      <div id="s7-h" class="h">E o próximo cartão<br>já está <span class="y">à vista.</span></div>
      <div id="s7-chips"><div id="s7-c0" class="s7-c">Cartão XP Infinite · Bloqueado</div><div id="s7-c1" class="s7-c">Cartão XP Infinite · Desbloqueado</div></div>
      <img id="s7-p0" class="s7-ph" src="assets/inf-lock.png" alt="">
      <img id="s7-p1" class="s7-ph" src="assets/inf-on.png" alt="">
    </div>''',
'''      tl.fromTo("#s7-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.2);
      tl.fromTo("#s7-p0", { opacity: 0, y: 160 }, { opacity: 1, y: 0, duration: 1.0, ease: "power3.out" }, 0.4);
      tl.fromTo("#s7-c0", { opacity: 0 }, { opacity: 1, duration: 0.5 }, 1.3);
      tl.fromTo("#s7-p1", { opacity: 0 }, { opacity: 1, duration: 0.7, ease: "power2.inOut" }, 3.4);
      tl.fromTo("#s7-c0", { opacity: 1 }, { opacity: 0, duration: 0.3, immediateRender: false }, 3.4);
      tl.fromTo("#s7-c1", { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" }, 3.6);''')

# 8 fecho
random.seed(7); dots=[]; djs=[]
import math
for i in range(46):
    a=random.random()*2*math.pi; r=260+random.random()*620; z=14+random.randint(0,3)*8
    dots.append(f'<i id="s8-p{i}" style="width:{z}px;height:{z}px;background:{"#7BE3A8" if i%3==0 else "#FFC709"}"></i>')
    djs.append(f'      tl.fromTo("#s8-p{i}", {{ x: 0, y: 0, opacity: 1, scale: 1 }}, {{ x: {round(math.cos(a)*r)}, y: {round(math.sin(a)*r*0.75)}, opacity: 0, scale: 0.4, duration: {1.3+random.random()*0.6:.2f}, ease: "power3.out" }}, {0.9+random.random()*0.15:.2f});')
add('s8',6,'''
    #s8-all{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:36px}
    #s8-fx{position:absolute;left:960px;top:470px}
    #s8-fx i{position:absolute;border-radius:50%;opacity:0}
    #s8-logo{width:150px;height:126px;border-radius:24px;background:#fff;color:#111;font-weight:900;font-size:66px;letter-spacing:-.05em;display:flex;align-items:center;justify-content:center}
    #s8-name{font-size:150px}
    #s8-cta{font-size:60px;font-weight:700;color:#FFC709}
''',f'''    <div id="s8-fx">{''.join(dots)}</div>
    <div id="s8-all" class="clip" data-start="0" data-duration="6" data-track-index="0">
      <div id="s8-logo">XP</div>
      <div id="s8-name" class="h" data-var-text="programa">Jornada XP</div>
      <div id="s8-cta">Comece a sua.</div>
    </div>''',
'''      tl.fromTo("#s8-logo", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.6, ease: "back.out(1.8)" }, 0.3);
      tl.fromTo("#s8-name", { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.8, ease: "power3.out" }, 0.7);
''' + '\n'.join(djs) + '''
      tl.fromTo("#s8-cta", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6, ease: "power2.out" }, 2.0);''')

t=0; hosts=''
for sid,d in SC:
    hosts+=f'      <div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{t}" data-duration="{d}" data-track-index="0" data-track-kind="graphics" data-width="1920" data-height="1080"></div>\n'; t+=d
vars_=json.dumps([{"id":"programa","type":"string","label":"Nome do programa","default":"Jornada XP"}],ensure_ascii=False)
open(V+'/index.html','w',encoding='utf-8').write(f'''<!doctype html>
<html lang="pt-BR" data-composition-variables='{vars_}'>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="assets/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #0b0b0c; }}
      #root {{ width: 100%; height: 100%; position: relative; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{t}" data-width="1920" data-height="1080">
{hosts}    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
''')
print('duracao',t)
