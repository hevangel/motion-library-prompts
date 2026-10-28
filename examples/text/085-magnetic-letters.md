# 085 · 磁力文字 — Magnetic Letters

游標靠近時字被推開

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、Logo・品牌
- 風格／關鍵字 Style: 
- 標籤 Tag: quickTo
- 範例文字 Example text: 「靠近我看看」（預覽底色：cream）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「磁力文字（Magnetic Letters）」動態效果：游標靠近文字時，附近的字被往外推開並改用強調色，距離越近推得越遠，游標離開後平滑回到原位。（GSAP：SplitText chars，每個字用 gsap.quickTo 控制 x/y，依游標距離計算推力）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx85">`, preview text 「靠近我看看」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「磁力文字」.

### JavaScript — `FX[85]` from `site/fx.js`

```js
85(s,x){const l=layer(s);const t=T(x);l.append(t);const sp=SplitText.create(t,{type:'chars'});
  const qs=sp.chars.map(c=>({c,x:gsap.quickTo(c,'x',{duration:.5,ease:'power3.out'}),y:gsap.quickTo(c,'y',{duration:.5,ease:'power3.out'})}));
  pointer(l,(px,py)=>{const r=l.getBoundingClientRect();const R=r.width*.22;qs.forEach(q=>{const b=q.c.getBoundingClientRect();const cx=b.left+b.width/2-r.left-gsap.getProperty(q.c,'x'),cy=b.top+b.height/2-r.top-gsap.getProperty(q.c,'y');const dx=cx-px,dy=cy-py,d=Math.hypot(dx,dy)||1,f=Math.max(0,1-d/R);q.x(dx/d*f*R*.7);q.y(dy/d*f*R*.7);q.c.style.color=f>.15?'var(--a)':''})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx85` rules from `site/fx.css`

_No dedicated `.fx85` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #85
