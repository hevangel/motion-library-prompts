# 095 · 磁吸按鈕 — Magnetic Button

按鈕被游標吸過去並彈回

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 
- 標籤 Tag: quickTo・Elastic
- 範例文字 Example text: 「按我」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「磁吸按鈕（Magnetic Button）」動態效果：游標靠近按鈕時，按鈕被吸向游標方向，按鈕內文字移動得更少形成層次，同時切換成強調色；離開時帶彈性回到原位。（GSAP：gsap.quickTo 控制 x/y，ease elastic.out(1,0.4)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx95">`, preview text 「按我」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「磁吸按鈕」.

### JavaScript — `FX[95]` from `site/fx.js`

```js
95(s,x){const l=layer(s);const b=el('button','mbtn');const sp=el('span');sp.textContent=x;b.append(sp);l.append(b);const q=(e,k)=>gsap.quickTo(e,k,{duration:.7,ease:'elastic.out(1,.4)'});const bx=q(b,'x'),by=q(b,'y'),tx=q(sp,'x'),ty=q(sp,'y');
  pointer(l,(px,py)=>{const W=l.offsetWidth,H=l.offsetHeight,dx=px-W/2,dy=py-H/2,on=Math.hypot(dx,dy)<W*.26;bx(on?dx*.4:0);by(on?dy*.4:0);tx(on?dx*.2:0);ty(on?dy*.2:0);b.classList.toggle('on',on)},[[.15,.25],[.42,.45],[.56,.56],[.5,.5],[.85,.3],[.62,.62],[.2,.8]])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx95` rules from `site/fx.css`

_No dedicated `.fx95` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #95
