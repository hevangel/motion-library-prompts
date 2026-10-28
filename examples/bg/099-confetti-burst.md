# 099 · 彩紙爆發 — Confetti Burst

受重力影響的彩紙噴發

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 
- 標籤 Tag: Physics2D
- 範例文字 Example text: 「恭喜」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「彩紙爆發（Confetti Burst）」動態效果：文字彈性放大的同時，從下方噴出一大把紙片，紙片受重力拋物線落下、旋轉並在尾段淡出，每 2 秒一次。（GSAP：Physics2DPlugin velocity / angle / gravity，random 隨機化）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx99">`, preview text 「恭喜」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「彩紙爆發」.

### JavaScript — `FX[99]` from `site/fx.js`

```js
99(s,x,card){const t=T(x,Math.min(16,64/chars(x).length));s.append(t);const R=gsap.utils.random;const burst=()=>{const W=s.offsetWidth,H=s.offsetHeight;if(!W)return;gsap.fromTo(t,{scale:.6},{scale:1,duration:.8,ease:'elastic.out(1,.4)'});
  for(let i=0;i<36;i++){const p=el('i','cf');p.style.background=GC[i%5];s.append(p);gsap.set(p,{x:W/2,y:H*.62,rotation:R(0,360)});gsap.to(p,{physics2D:{velocity:R(H*.9,H*1.8),angle:R(215,325),gravity:H*1.9},rotation:'+='+R(-540,540),duration:2,ease:'none',onComplete:()=>p.remove()});gsap.to(p,{opacity:0,duration:.5,delay:1.5})}};
  burst();card._timers.push(setInterval(burst,2300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx99` rules from `site/fx.css`

_No dedicated `.fx99` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #99
