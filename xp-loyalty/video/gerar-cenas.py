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
    #s3-k{font-size:34px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#A3A3A8}
    #s3-h{font-size:112px;margin-top:6px;white-space:nowrap}
    #s3-s{font-size:34px;font-weight:700;color:#FFC709;margin-top:14px;line-height:1.25}
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
        <div id="s3-c"><div id="s3-k">Sua</div><div id="s3-h" class="h">Jornada <span class="y">XP</span></div><div id="s3-s">Mais perto dos seus objetivos<br>a cada avanço.</div></div>
        {orb}
      </div>
    </div>""",
"""      gsap.set(["#s3-out", "#s3-comet", "#s3-cam"], { transformOrigin: "960px 540px" });
      tl.fromTo("#s3-glow", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 1.2, ease: "power2.out" }, 0);
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
    #s4-txt{position:absolute;left:170px;top:150px;width:920px}
    #s4-h{font-size:96px}
    #s4-num{display:flex;align-items:flex-end;gap:26px;margin-top:70px}
    #s4-n{font-size:260px;font-weight:900;letter-spacing:-.05em;line-height:.85;min-width:300px}
    #s4-u{font-size:60px;font-weight:700;padding-bottom:14px}
    #s4-bar{height:22px;border-radius:12px;background:rgba(255,255,255,.12);margin-top:40px;overflow:hidden;width:820px}
    #s4-fill{height:100%;width:100%;background:#7BE3A8;border-radius:12px;transform-origin:0 50%}
    #s4-ph{position:absolute;right:210px;top:70px;height:940px;border-radius:64px;box-shadow:0 50px 120px rgba(0,0,0,.6)}
''','''    <div id="s4-all" class="clip" data-start="0" data-duration="7" data-track-index="0">
      <div id="s4-txt">
        <div id="s4-h" class="h">Cada avanço na<br>sua jornada vira<br><span class="y">fichas.</span></div>
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

# 5 régua: o rolo para no Cofre XP, o nome vira o título do cartão e as fichas voam até o ponto escolhido
REEL=['Investback','Salas VIP','Corretagem zero','Cofre XP']*3
reel=''.join(f'<div>{t}</div>' for t in REEL)
X0,W,NY,SX,SY=322,1276,770,1493,484
nodes=''.join(f'<div class="s5-n" id="s5-n{i}" style="left:{p}%"><i id="s5-d{i}"></i><b>{t}</b><span>{c}</span></div>' for i,(p,t,c) in enumerate([(0,'100%','Incluído'),(33.333,'110%','10 fichas'),(66.666,'115%','15 fichas'),(100,'125%','30 fichas')]))
fly=''.join(f'<i class="s5-f" id="s5-f{k}"></i>' for k in range(15))
fx=''
for n in (1,2):
    x=round(X0+W*n/3)
    fx+=f'<i class="s5-rp" id="s5-rp{n}" style="left:{x-28}px;top:{NY-28}px"></i>'+''.join(f'<i class="s5-k" id="s5-k{n}-{k}" style="left:{x-6}px;top:{NY-6}px"></i>' for k in range(12))
add('s5',12.6,"""
    #s5-all{position:absolute;inset:0}
    #s5-h{position:absolute;left:170px;top:110px;font-size:88px;width:1500px}
    #s5-reel{position:absolute;left:170px;right:170px;top:345px;height:570px;overflow:hidden}
    #s5-col div,#s5-land{height:190px;line-height:190px;font-size:150px;font-weight:900;letter-spacing:-.04em;white-space:nowrap}
    #s5-col div{color:#77777f}
    .s5-fade{position:absolute;left:0;right:0;height:200px}
    #s5-ft{top:0;background:linear-gradient(#0c0b0b,rgba(12,11,11,0))} #s5-fb{bottom:0;background:linear-gradient(rgba(11,11,12,0),#0b0b0c)}
    .s5-bar{position:absolute;left:170px;right:170px;height:4px;border-radius:2px;background:#FFC709;transform-origin:0 50%}
    #s5-b1l{top:533px} #s5-b2l{top:725px}
    #s5-land{position:absolute;left:170px;top:535px;color:#FFC709;transform-origin:0 0}
    #s5-card{position:absolute;left:170px;right:170px;top:400px;height:540px;border-radius:56px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.1);transform-origin:50% 43%;overflow:hidden}
    #s5-sheen{position:absolute;top:0;bottom:0;left:0;width:200px;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.07),rgba(255,255,255,0))}
    #s5-t{position:absolute;left:90px;top:50px;font-size:44px;font-weight:700;white-space:nowrap}
    #s5-t em{font-style:normal;font-weight:400;color:#A3A3A8;margin-left:18px}
    #s5-tn{opacity:0}
    .s5-chip{position:absolute;top:44px;height:64px;line-height:64px;border-radius:999px;padding:0 30px;font-size:32px;font-weight:700;white-space:nowrap}
    #s5-uso{right:440px;background:#FFC709;color:#000}
    #s5-disp{right:90px;width:330px;text-align:center;border:3px solid #7BE3A8;color:#7BE3A8;line-height:58px}
    #s5-big{position:absolute;left:90px;top:128px;height:156px;width:700px;overflow:hidden}
    #s5-big div{position:absolute;left:0;top:0;font-size:150px;font-weight:900;letter-spacing:-.04em;line-height:156px}
    #s5-rg{position:absolute;left:150px;right:150px;top:340px;height:160px}
    #s5-track{position:absolute;left:0;right:0;top:22px;height:12px;border-radius:6px;background:rgba(255,255,255,.14);transform-origin:0 50%}
    #s5-fill{position:absolute;left:0;right:0;top:22px;height:12px;border-radius:6px;background:#FFC709;transform-origin:0 50%;box-shadow:0 0 24px rgba(255,199,9,.7)}
    .s5-n{position:absolute;top:0;width:260px;margin-left:-130px;text-align:center}
    .s5-n i{display:block;width:56px;height:56px;border-radius:50%;margin:0 auto 18px;background:#1e1b17;border:7px solid #6E6E75}
    .s5-n b{display:block;font-size:44px;font-weight:700}
    .s5-n span{display:block;font-size:28px;color:#A3A3A8;margin-top:4px}
    .s5-f{position:absolute;left:"""+str(SX-11)+"""px;top:"""+str(SY-11)+"""px;width:26px;height:26px;border-radius:50%;background:#7BE3A8;box-shadow:0 0 22px rgba(123,227,168,.95);opacity:0}
    .s5-rp{position:absolute;width:56px;height:56px;border-radius:50%;border:5px solid #FFC709;opacity:0}
    .s5-k{position:absolute;width:12px;height:12px;border-radius:50%;background:#FFC709;opacity:0}
""",f"""    <div id="s5-all" class="clip" data-start="0" data-duration="12.6" data-track-index="0">
      <div id="s5-h" class="h">Com fichas, você escolhe<br>o que <span class="y">turbinar.</span></div>
      <div id="s5-reel" data-layout-allow-overflow><div id="s5-col">{reel}</div><div class="s5-fade" id="s5-ft"></div><div class="s5-fade" id="s5-fb"></div></div>
      <div class="s5-bar" id="s5-b1l"></div><div class="s5-bar" id="s5-b2l"></div>
      <div id="s5-card">
        <div id="s5-sheen"></div>
        <div id="s5-t"><span id="s5-tn">Cofre XP</span><em id="s5-te">% do CDI</em></div>
        <div class="s5-chip" id="s5-uso">Em uso <span id="s5-un">0</span></div>
        <div class="s5-chip" id="s5-disp">Disponíveis <span id="s5-dn">15</span></div>
        <div id="s5-big"><div id="s5-b0">100%</div><div id="s5-b1" class="y">110%</div><div id="s5-b2" class="y">115%</div></div>
        <div id="s5-rg"><div id="s5-track"></div><div id="s5-fill"></div>{nodes}</div>
      </div>
      <div id="s5-land">Cofre XP</div>
      {fly}{fx}
    </div>""",
"""      const X0 = 322, W = 1276, NY = 770, SX = 1493, SY = 484, nodeX = n => X0 + W * n / 3;
      const un = document.querySelector("#s5-un"), dn = document.querySelector("#s5-dn");
      const lit = { backgroundColor: "#FFC709", borderColor: "#FFC709", duration: 0.2 }, unlit = { backgroundColor: "#1e1b17", borderColor: "#6E6E75" };
      tl.fromTo("#s5-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.15);

      // 1. rolo: três linhas à vista, só a do meio em foco; gira borrado, desacelera e trava com um tranco
      tl.fromTo("#s5-reel", { opacity: 0 }, { opacity: 1, duration: 0.25 }, 0.55);
      tl.fromTo(".s5-bar", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, 0.55);
      tl.fromTo("#s5-col", { y: 190, filter: "blur(14px)" }, { y: 190 - 190 * 11, filter: "blur(0px)", duration: 1.75, ease: "back.out(0.9)" }, 0.6);
      tl.fromTo("#s5-land", { opacity: 0 }, { opacity: 1, duration: 0.01 }, 2.35);
      tl.fromTo("#s5-land", { scale: 1.12 }, { scale: 1, duration: 0.3, ease: "back.out(3)" }, 2.35);
      tl.fromTo("#s5-col", { opacity: 1 }, { opacity: 0, duration: 0.01, immediateRender: false }, 2.35);
      tl.fromTo("#s5-reel", { opacity: 1 }, { opacity: 0, duration: 0.2, immediateRender: false }, 2.45);

      // 2. o nome escolhido encolhe e vira o título do cartão, que se abre a partir da faixa do rolo
      tl.fromTo(".s5-bar", { opacity: 1 }, { opacity: 0, duration: 0.25, immediateRender: false }, 2.95);
      tl.fromTo("#s5-card", { opacity: 0, scaleY: 0.36 }, { opacity: 1, scaleY: 1, duration: 0.55, ease: "power4.out" }, 2.95);
      tl.fromTo("#s5-land", { x: 0, y: 0, scale: 1, color: "#FFC709" }, { x: 92, y: -83, scale: 0.2933, color: "#F4F4F2", duration: 0.55, ease: "power4.inOut", immediateRender: false }, 2.95);
      tl.fromTo("#s5-tn", { opacity: 0 }, { opacity: 1, duration: 0.01 }, 3.5);
      tl.fromTo("#s5-land", { opacity: 1 }, { opacity: 0, duration: 0.01, immediateRender: false }, 3.5);
      tl.fromTo("#s5-te", { opacity: 0 }, { opacity: 1, duration: 0.3 }, 3.5);
      tl.fromTo("#s5-track", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, 3.3);
      for (let i = 0; i < 4; i++) tl.fromTo("#s5-n" + i, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.35, ease: "back.out(2)" }, 3.4 + i * 0.09);
      tl.fromTo("#s5-b0", { yPercent: 110 }, { yPercent: 0, duration: 0.5, ease: "back.out(1.5)" }, 3.45);
      tl.fromTo(["#s5-uso", "#s5-disp"], { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out", stagger: 0.1 }, 3.6);
      tl.fromTo("#s5-d0", unlit, lit, 3.95);
      tl.fromTo("#s5-fill", { scaleX: 0 }, { scaleX: 0, duration: 0.01 }, 0);
      tl.fromTo("#s5-b1", { yPercent: 110 }, { yPercent: 110, duration: 0.01 }, 0);
      tl.fromTo("#s5-b2", { yPercent: 110 }, { yPercent: 110, duration: 0.01 }, 0);
      tl.fromTo("#s5-sheen", { x: -400, skewX: -20 }, { x: -400, skewX: -20, duration: 0.01 }, 0);

      // 3. alocar: as fichas disponíveis voam até o ponto, a barra avança e o impacto troca o número
      function allocate(n, t, first, count, usoFrom, usoTo, dispFrom, dispTo) {
        for (let i = 0; i < count; i++) {
          const id = "#s5-f" + (first + i), d = t + i * 0.055;
          tl.fromTo(id, { x: 0, opacity: 0, scale: 0.4 }, { x: nodeX(n) - SX, opacity: 1, scale: 1, duration: 0.7, ease: "power1.inOut", immediateRender: false }, d);
          tl.fromTo(id, { y: 0 }, { y: NY - SY, duration: 0.7, ease: "power2.in", immediateRender: false }, d);
          tl.fromTo(id, { opacity: 1 }, { opacity: 0, duration: 0.06, immediateRender: false }, d + 0.7);
        }
        const hit = t + 0.9, c = { u: usoFrom, d: dispFrom };
        tl.fromTo("#s5-disp", { scale: 1 }, { scale: 0.93, duration: 0.12, yoyo: true, repeat: 1, immediateRender: false }, t);
        tl.fromTo(c, { u: usoFrom, d: dispFrom }, { u: usoTo, d: dispTo, duration: 0.9, ease: "none", immediateRender: false, onUpdate: () => { un.textContent = Math.round(c.u); dn.textContent = Math.round(c.d); } }, t + 0.1);
        tl.fromTo("#s5-fill", { scaleX: (n - 1) / 3 }, { scaleX: n / 3, duration: 0.8, ease: "power3.in", immediateRender: false }, t + 0.1);
        tl.fromTo("#s5-d" + n, unlit, lit, hit);
        tl.fromTo("#s5-d" + n, { scale: 1 }, { scale: 1.5, duration: 0.14, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, hit);
        tl.fromTo("#s5-rp" + n, { scale: 1, opacity: 0.9 }, { scale: 4.2, opacity: 0, duration: 0.7, ease: "power2.out", immediateRender: false }, hit);
        for (let k = 0; k < 12; k++) {
          const a = k * Math.PI / 6, r = 90 + (k % 3) * 44;
          tl.fromTo("#s5-k" + n + "-" + k, { x: 0, y: 0, opacity: 1, scale: 1 }, { x: Math.cos(a) * r, y: Math.sin(a) * r, opacity: 0, scale: 0.3, duration: 0.6, ease: "power3.out", immediateRender: false }, hit);
        }
        tl.fromTo("#s5-card", { scale: 1 }, { scale: 1.018, duration: 0.1, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, hit);
        tl.fromTo("#s5-sheen", { x: -400, skewX: -20 }, { x: 1700, skewX: -20, duration: 0.6, ease: "power2.out", immediateRender: false }, hit);
        tl.fromTo("#s5-b" + (n - 1), { yPercent: 0 }, { yPercent: -110, duration: 0.22, ease: "power2.in", immediateRender: false }, hit - 0.05);
        tl.fromTo("#s5-b" + n, { yPercent: 110 }, { yPercent: 0, duration: 0.45, ease: "back.out(1.8)", immediateRender: false }, hit + 0.1);
        tl.fromTo("#s5-uso", { scale: 1 }, { scale: 1.1, duration: 0.14, yoyo: true, repeat: 1, immediateRender: false }, hit);
      }
      allocate(1, 4.9, 0, 10, 0, 10, 15, 5);
      allocate(2, 8.0, 10, 5, 10, 15, 5, 0);""")

# 6 trocar: um benefício sai, as fichas voltam para o saldo e vão para outro
LX,RX,CYc,WX,WY=510,1410,740,960,452
out=''.join(f'<i class="s6-f" id="s6-o{k}" style="left:{LX-13}px;top:{CYc-13}px"></i>' for k in range(10))
inn=''.join(f'<i class="s6-f" id="s6-i{k}" style="left:{WX-13}px;top:{WY-13}px"></i>' for k in range(10))
def card(cid,x,name,unit,v0,v1,c0,c1):
    return f"""<div class="s6-c" id="s6-{cid}" style="left:{x}px"><i class="s6-g" id="s6-{cid}g"></i>
        <div class="s6-n">{name}<em>{unit}</em></div>
        <div class="s6-v"><div id="s6-{cid}v0">{v0}</div><div id="s6-{cid}v1">{v1}</div></div>
        <div class="s6-ch"><span id="s6-{cid}c0">{c0}</span><span id="s6-{cid}c1">{c1}</span></div></div>"""
add('s6',8.4,"""
    #s6-all{position:absolute;inset:0}
    #s6-h{position:absolute;left:170px;top:100px;font-size:88px;width:1500px}
    #s6-w{position:absolute;left:740px;top:400px;width:440px;height:104px;border-radius:999px;border:4px solid #7BE3A8;color:#7BE3A8;font-size:42px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:16px;background:#0f1512}
    #s6-wn{font-size:60px;font-weight:900;color:#F4F4F2;min-width:76px;text-align:center}
    .s6-c{position:absolute;top:570px;width:680px;height:350px;border-radius:48px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.1);padding:40px 50px;overflow:hidden}
    .s6-g{position:absolute;inset:0;border-radius:46px;border:5px solid #FFC709;background:rgba(255,199,9,.1)}
    .s6-n{position:relative;font-size:42px;font-weight:700}
    .s6-n em{font-style:normal;font-weight:400;color:#A3A3A8;margin-left:16px}
    .s6-v{position:relative;height:140px;margin-top:10px;overflow:hidden}
    .s6-v div{position:absolute;left:0;top:0;font-size:128px;font-weight:900;letter-spacing:-.04em;line-height:140px;white-space:nowrap}
    .s6-ch{position:relative;height:60px;margin-top:22px}
    .s6-ch span{position:absolute;left:0;top:0;height:60px;line-height:60px;border-radius:999px;padding:0 28px;font-size:30px;font-weight:700;white-space:nowrap}
    .s6-f{position:absolute;width:26px;height:26px;border-radius:50%;background:#7BE3A8;box-shadow:0 0 22px rgba(123,227,168,.95);opacity:0}
    #s6-rp{position:absolute;left:"""+str(RX-60)+"""px;top:"""+str(CYc-60)+"""px;width:120px;height:120px;border-radius:50%;border:6px solid #FFC709;opacity:0}
    .on{background:#FFC709;color:#000} .off{border:3px solid #6E6E75;color:#A3A3A8;line-height:54px!important}
""",f"""    <div id="s6-all" class="clip" data-start="0" data-duration="8.4" data-track-index="0">
      <div id="s6-h" class="h">Troque quando quiser.<br><span class="y">As fichas voltam.</span></div>
      {card('a',170,'Cofre XP','% do CDI','<span class="y">110%</span>','100%','10 fichas em uso','Incluído').replace('id="s6-ac0"','id="s6-ac0" class="on"').replace('id="s6-ac1"','id="s6-ac1" class="off"')}
      {card('b',1070,'Investback','no cartão','<span class="mut">Sem</span>','<span class="y">1,0%</span>','10 fichas','10 fichas em uso').replace('id="s6-bc0"','id="s6-bc0" class="off"').replace('id="s6-bc1"','id="s6-bc1" class="on"')}
      <div id="s6-w">Disponíveis <span id="s6-wn">5</span></div>
      <i id="s6-rp"></i>
      {out}{inn}
    </div>""",
"""      const LX = 510, RX = 1410, CY = 740, WX = 960, WY = 452, wn = document.querySelector("#s6-wn");
      tl.fromTo("#s6-h", { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.15);
      tl.fromTo("#s6-a", { opacity: 0, y: 70 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.5);
      tl.fromTo("#s6-b", { opacity: 0, y: 70 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.62);
      tl.fromTo("#s6-w", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2)" }, 0.85);
      // estados iniciais do que entra depois
      tl.fromTo(["#s6-av1", "#s6-bv1"], { yPercent: 110 }, { yPercent: 110, duration: 0.01 }, 0);
      tl.fromTo(["#s6-ac1", "#s6-bc1", "#s6-bg"], { opacity: 0 }, { opacity: 0, duration: 0.01 }, 0);

      function fly(prefix, dx, dy, t) {
        for (let k = 0; k < 10; k++) {
          const id = prefix + k, d = t + k * 0.05, sx = ((k % 5) - 2) * 26, sy = (k < 5 ? -1 : 1) * 16;
          tl.fromTo(id, { x: sx, opacity: 0, scale: 0.4 }, { x: dx, opacity: 1, scale: 1, duration: 0.7, ease: "power2.inOut", immediateRender: false }, d);
          tl.fromTo(id, { y: sy }, { y: dy, duration: 0.7, ease: dy < 0 ? "power2.out" : "power2.in", immediateRender: false }, d);
          tl.fromTo(id, { opacity: 1 }, { opacity: 0, duration: 0.06, immediateRender: false }, d + 0.7);
        }
      }
      function count(from, to, t) { const c = { v: from };
        tl.fromTo(c, { v: from }, { v: to, duration: 0.75, ease: "none", immediateRender: false, onUpdate: () => { wn.textContent = Math.round(c.v); } }, t);
        tl.fromTo("#s6-w", { scale: 1 }, { scale: 1.08, duration: 0.16, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, t + 0.6); }

      // 1. sai do Cofre XP: o cartão apaga, volta a 100% e as fichas sobem para o saldo
      const t1 = 2.2;
      tl.fromTo("#s6-a", { scale: 1 }, { scale: 0.97, duration: 0.12, yoyo: true, repeat: 1, immediateRender: false }, t1);
      tl.fromTo("#s6-ag", { opacity: 1 }, { opacity: 0, duration: 0.35 }, t1);
      tl.fromTo("#s6-av0", { yPercent: 0 }, { yPercent: -110, duration: 0.25, ease: "power2.in" }, t1);
      tl.fromTo("#s6-av1", { yPercent: 110 }, { yPercent: 0, duration: 0.45, ease: "back.out(1.6)", immediateRender: false }, t1 + 0.15);
      tl.fromTo("#s6-ac0", { opacity: 1 }, { opacity: 0, duration: 0.2 }, t1);
      tl.fromTo("#s6-ac1", { opacity: 0 }, { opacity: 1, duration: 0.25, immediateRender: false }, t1 + 0.15);
      fly("#s6-o", WX - LX, WY - CY, t1 + 0.05);
      count(5, 15, t1 + 0.6);

      // 2. entra no Investback: as fichas descem do saldo, o cartão acende e o número troca
      const t2 = 4.6, hit = t2 + 0.95;
      fly("#s6-i", RX - WX, CY - WY, t2);
      count(15, 5, t2);
      tl.fromTo("#s6-bg", { opacity: 0 }, { opacity: 1, duration: 0.2, immediateRender: false }, hit);
      tl.fromTo("#s6-b", { scale: 1 }, { scale: 1.03, duration: 0.12, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, hit);
      tl.fromTo("#s6-rp", { scale: 1, opacity: 0.9 }, { scale: 5, opacity: 0, duration: 0.7, ease: "power2.out", immediateRender: false }, hit);
      tl.fromTo("#s6-bv0", { yPercent: 0 }, { yPercent: -110, duration: 0.22, ease: "power2.in" }, hit - 0.05);
      tl.fromTo("#s6-bv1", { yPercent: 110 }, { yPercent: 0, duration: 0.45, ease: "back.out(1.8)", immediateRender: false }, hit + 0.1);
      tl.fromTo("#s6-bc0", { opacity: 1 }, { opacity: 0, duration: 0.2 }, hit);
      tl.fromTo("#s6-bc1", { opacity: 0 }, { opacity: 1, duration: 0.25, immediateRender: false }, hit + 0.1);""")

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
