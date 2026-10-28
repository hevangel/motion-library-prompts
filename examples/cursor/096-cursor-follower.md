# 096 · 游標跟隨 — Cursor Follower

拖尾圓點與反相圓圈

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 
- 標籤 Tag: quickTo
- 範例文字 Example text: 「跟著游標」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「游標跟隨（Cursor Follower）」動態效果：游標後方跟著一串由快到慢的拖尾圓點，加上一顆較大的圓圈以反色混合模式蓋在文字上，經過時文字變成反色。（GSAP：多個 gsap.quickTo 設不同 duration，大圓用 mix-blend-mode:difference）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx96">`, preview text 「跟著游標」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「游標跟隨」.

### JavaScript — `FX[96]` from `site/fx.js`

```js
96(s,x){const l=layer(s);l.append(T(x,Math.min(14,60/chars(x).length)));const big=el('div','fbig');const ds=[...Array(5)].map((_,i)=>{const d=el('div','fdot');d.style.opacity=1-i*.17;l.append(d);return d});l.append(big);gsap.set([big,...ds],{xPercent:-50,yPercent:-50});
  const qs=[big,...ds].map((d,i)=>[gsap.quickTo(d,'x',{duration:i?.12+i*.1:.5,ease:'power3'}),gsap.quickTo(d,'y',{duration:i?.12+i*.1:.5,ease:'power3'})]);
  pointer(l,(px,py)=>qs.forEach(([a,b])=>{a(px);b(py)}),null,false)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx96` rules from `site/fx.css`

_No dedicated `.fx96` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #96
