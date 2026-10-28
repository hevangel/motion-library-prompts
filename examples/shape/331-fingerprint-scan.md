# 331 · 指紋掃描解鎖 — Fingerprint Scan

指紋紋路一圈圈畫出，掃描光條上下掃過，成功後外框發光並打勾

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場、切換
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 指紋 掃描 解鎖 生物辨識 驗證 登入 Fingerprint Scan Biometric Unlock Auth 圖形 SVG
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「驗證成功」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「指紋掃描解鎖（Fingerprint Scan）」動態效果：手機指紋解鎖畫面：圓角方形感應區中，指紋的弧線紋路由內而外一圈圈依序畫出；接著一條發光的掃描光條由上往下、再由下往上掃過，下方文字顯示「掃描中…」；掃描完成後指紋紋路變淡，一個粗勾勾快速畫出，感應區外框發出光暈，文字變成「驗證成功」。（GSAP timeline：指紋弧線用 DrawSVG stagger 畫出；掃描條 top 0% → 100% yoyo；完成時加 class 讓外框 box-shadow 發光，勾勾 DrawSVG 0% → 100%）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx331">`, preview text 「驗證成功」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「指紋掃描解鎖」.

### JavaScript — `FX[331]` from `site/fx.js`

```js
331(s,x){const arcs=[];for(let i=0;i<7;i++){const rx=6+i*4.2,ry=8+i*5,gap=i%2?.7:.35;arcs.push(`M${(-rx*Math.sin(gap)).toFixed(1)},${(ry*Math.cos(gap)).toFixed(1)} A${rx},${ry} 0 1 1 ${(rx*Math.sin(gap*.6)).toFixed(1)},${(ry*Math.cos(gap*.6)).toFixed(1)}`)}
  s.insertAdjacentHTML('beforeend',`<div class="sv-fp"><div class="sv-fb"><svg viewBox="-40 -42 80 80">${arcs.map(d=>`<path class="ar" d="${d}"/>`).join('')}<path class="ok" d="M-14,0 L-4,10 L16,-12"/></svg><i class="sv-scan"></i></div><b>請輕觸感應區</b></div>`);
  const w=s.querySelector('.sv-fp'),ar=w.querySelectorAll('.ar'),ok=w.querySelector('.ok'),sc=w.querySelector('.sv-scan'),lb=w.querySelector('b');
  gsap.timeline({repeat:-1,repeatDelay:1}).call(()=>{lb.textContent='請輕觸感應區';w.classList.remove('done')}).set(ok,{drawSVG:'0%'}).set(ar,{opacity:1}).fromTo(ar,{drawSVG:'0%'},{drawSVG:'100%',duration:.7,stagger:.07,ease:'power1.inOut'}).call(()=>lb.textContent='掃描中…').fromTo(sc,{top:'0%',opacity:1},{top:'100%',duration:.8,ease:'power1.inOut',yoyo:true,repeat:1}).to(sc,{opacity:0,duration:.1}).call(()=>{w.classList.add('done');lb.textContent=x}).to(ar,{opacity:.15,duration:.3}).to(ok,{drawSVG:'100%',duration:.4,ease:'power2.out'},'<.1').to({},{duration:1.6})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx331` rules from `site/fx.css`

_No dedicated `.fx331` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #331
