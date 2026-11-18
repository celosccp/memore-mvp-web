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

# 3 momentos: quatro frentes em órbita da Jornada XP, sem começo nem fim
M=[('Planeje sua vida financeira','Organize contas, gastos e objetivos.'),('Comece a poupar','Guarde um pouco todo mês, no seu ritmo.'),('Otimize seu dia a dia','Faça o dinheiro do mês render mais.'),('Acelere e proteja seus planos','Vá mais longe quando fizer sentido.')]
CX,CY,R=960,540,340; D=round(R*0.7071)
POS=[(-1,-1),(1,-1),(1,1),(-1,1)]
orb=''
for i,((t,d),(sx,sy)) in enumerate(zip(M,POS)):
    x,y=CX+sx*D,CY+sy*D
    lab=f'right:{1920-x+70}px;text-align:right;justify-content:flex-end' if sx<0 else f'left:{x+70}px;text-align:left'
    orb+=(f'<i class="s3-rp" id="s3-rp{i}" style="left:{x-33}px;top:{y-33}px"></i><i class="s3-d" id="s3-d{i}" style="left:{x-33}px;top:{y-33}px"></i>'
          f'<div class="s3-lw" style="{lab};top:{y-110}px"><div class="s3-l" id="s3-l{i}"><b>{t}</b><span>{d}</span></div></div>')
random.seed(11); stars=''; sjs=[]
for k in range(46):
    x,y,z=random.randint(40,1880),random.randint(40,1040),random.choice([3,4,4,6])
    if abs(x-CX)<330 and abs(y-CY)<200: continue
    stars+=f'<i class="s3-st" id="s3-st{k}" style="left:{x}px;top:{y}px;width:{z}px;height:{z}px"></i>'
    sjs.append(f'      tl.fromTo("#s3-st{k}", {{ opacity: 0 }}, {{ opacity: {random.choice([0.35,0.5,0.8])}, duration: {0.6+random.random():.2f}, yoyo: true, repeat: 3, ease: "sine.inOut" }}, {random.random()*1.8:.2f});')
add('s3',8,"""
    #s3-all{position:absolute;inset:0}
    #s3-cam{position:absolute;inset:0}
    #s3-glow{position:absolute;left:560px;top:140px;width:800px;height:800px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,199,9,.34),rgba(255,199,9,.08) 55%,rgba(255,199,9,0) 100%)}
    .s3-st{position:absolute;border-radius:50%;background:#FFE27A;opacity:0}
    .s3-sv{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
    #s3-c{position:absolute;left:660px;top:380px;width:600px;height:320px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
    #s3-k{font-size:30px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#A3A3A8}
    #s3-h{font-size:112px;margin-top:6px;white-space:nowrap}
    #s3-s{font-size:36px;font-weight:700;color:#FFC709;margin-top:14px}
    .s3-d{position:absolute;width:66px;height:66px;border-radius:50%;background:#FFC709;box-shadow:0 0 0 12px #0f0d0a,0 0 46px 10px rgba(255,199,9,.55)}
    .s3-rp{position:absolute;width:66px;height:66px;border-radius:50%;border:4px solid #FFC709;opacity:0}
    .s3-lw{position:absolute;width:540px;height:220px;display:flex;align-items:center}
    .s3-l b{display:block;font-size:50px;font-weight:900;letter-spacing:-.03em;line-height:1.06}
    .s3-l span{display:block;font-size:30px;color:#A3A3A8;margin-top:8px;line-height:1.25}
""",f"""    <div id="s3-all" class="clip" data-start="0" data-duration="8" data-track-index="0">
      <div id="s3-cam">
        <div id="s3-glow"></div>
        {stars}
        <svg class="s3-sv" id="s3-out" viewBox="0 0 1920 1080" fill="none"><circle cx="{CX}" cy="{CY}" r="455" stroke="rgba(255,255,255,.16)" stroke-width="3" stroke-dasharray="3 26" stroke-linecap="round"/></svg>
        <svg class="s3-sv" viewBox="0 0 1920 1080" fill="none"><circle cx="{CX}" cy="{CY}" r="{R}" stroke="rgba(255,255,255,.12)" stroke-width="6"/><circle id="s3-arc" cx="{CX}" cy="{CY}" r="{R}" stroke="#FFC709" stroke-width="6" stroke-linecap="round" pathLength="1" stroke-dasharray="1" transform="rotate(-90 {CX} {CY})"/></svg>
        <svg class="s3-sv" id="s3-comet" viewBox="0 0 1920 1080" fill="none">
          <circle cx="{CX}" cy="{CY}" r="{R}" stroke="#fff" stroke-opacity=".16" stroke-width="16" stroke-linecap="round" pathLength="100" stroke-dasharray="16 84" transform="rotate(-148 {CX} {CY})"/>
          <circle cx="{CX}" cy="{CY}" r="{R}" stroke="#fff" stroke-opacity=".4" stroke-width="12" stroke-linecap="round" pathLength="100" stroke-dasharray="8 92" transform="rotate(-119 {CX} {CY})"/>
          <circle cx="{CX}" cy="{CY-R}" r="34" fill="#fff" fill-opacity=".22"/><circle cx="{CX}" cy="{CY-R}" r="15" fill="#fff"/>
        </svg>
        <div id="s3-c"><div id="s3-k">Sua</div><div id="s3-h" class="h">Jornada <span class="y">XP</span></div><div id="s3-s">Evolua no seu ritmo.</div></div>
        {orb}
      </div>
    </div>""",
"""      gsap.set(["#s3-out", "#s3-comet", "#s3-cam"], { transformOrigin: "960px 540px" });
      tl.fromTo("#s3-cam", { scale: 0.9 }, { scale: 1.03, duration: 8, ease: "none" }, 0);
      tl.fromTo("#s3-glow", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 1.2, ease: "power2.out" }, 0);
      tl.fromTo("#s3-glow", { scale: 1 }, { scale: 1.14, duration: 1.6, yoyo: true, repeat: 3, ease: "sine.inOut", immediateRender: false }, 1.2);
      tl.fromTo("#s3-k", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }, 0.15);
      tl.fromTo("#s3-h", { opacity: 0, scale: 0.6, filter: "blur(18px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.7, ease: "back.out(1.6)" }, 0.25);
      tl.fromTo("#s3-s", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0.8);
      tl.fromTo("#s3-arc", { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 1.3, ease: "power3.inOut" }, 0.4);
      tl.fromTo("#s3-out", { opacity: 0, rotation: -20 }, { opacity: 1, rotation: 0, duration: 1.2, ease: "power2.out" }, 0.5);
      tl.fromTo("#s3-out", { rotation: 0 }, { rotation: 40, duration: 6.3, ease: "none", immediateRender: false }, 1.7);
      // cometa: dá voltas no anel, sem parar em ninguém
      tl.fromTo("#s3-comet", { opacity: 0 }, { opacity: 1, duration: 0.4 }, 1.5);
      tl.fromTo("#s3-comet", { rotation: 0 }, { rotation: 620, duration: 6.4, ease: "none" }, 1.5);
      // as frentes acendem fora de ordem: nenhuma é a primeira
      [2, 0, 3, 1].forEach((k, n) => {
        const t = 1.0 + n * 0.28;
        tl.fromTo("#s3-d" + k, { scale: 0 }, { scale: 1, duration: 0.5, ease: "back.out(2.6)" }, t);
        tl.fromTo("#s3-rp" + k, { scale: 1, opacity: 0.8 }, { scale: 3.4, opacity: 0, duration: 0.9, ease: "power2.out", immediateRender: false }, t + 0.05);
        tl.fromTo("#s3-l" + k, { opacity: 0, x: (k === 0 || k === 3) ? 50 : -50 }, { opacity: 1, x: 0, duration: 0.6, ease: "power3.out" }, t + 0.1);
      });
      [1, 3, 0, 2].forEach((k, n) => {
        const t = 3.3 + n * 0.95;
        tl.fromTo("#s3-d" + k, { scale: 1 }, { scale: 1.32, duration: 0.3, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, t);
        tl.fromTo("#s3-rp" + k, { scale: 1, opacity: 0.7 }, { scale: 3, opacity: 0, duration: 0.8, ease: "power2.out", immediateRender: false }, t);
      });
""" + chr(10).join(sjs))

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
