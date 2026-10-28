# 097 · 拖曳甩動 — Drag & Toss

卡片可拖曳並帶慣性甩出

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 拖曳手勢
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 
- 標籤 Tag: Draggable・Inertia
- 範例文字 Example text: 「拖拖看」（預覽底色：acc）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「拖曳甩動（Drag & Toss）」動態效果：幾張卡片可以用滑鼠或手指拖曳，放開時依甩動速度帶慣性滑行，碰到邊界會減速回彈，拖曳中的卡片浮到最上層。（GSAP：Draggable.create { bounds, inertia:true, edgeResistance }，需 InertiaPlugin）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx97">`, preview text 「拖拖看」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「拖曳甩動」.

### JavaScript — `FX[97]` from `site/fx.js`

```js
97(s,x,card){const l=layer(s);const cs=[x,'✦','●'].map((v,i)=>{const c=el('div','dcard');c.textContent=v;c.style.left=[10,40,66][i]+'%';c.style.top=[22,52,18][i]+'%';l.append(c);return c});let idle=true,it;
  const ds=Draggable.create(cs,{bounds:l,inertia:true,edgeResistance:.7,zIndexBoost:true,onPress(){idle=false;clearTimeout(it);gsap.killTweensOf(this.target)},onRelease(){it=setTimeout(()=>idle=true,4000)}});card._kill.push(()=>ds.forEach(d=>d.kill()));
  card._timers.push(setInterval(()=>{if(!idle)return;const c=gsap.utils.random(cs);const W=l.offsetWidth,H=l.offsetHeight;gsap.to(c,{x:gsap.utils.random(-W*.15,W*.15),y:gsap.utils.random(-H*.15,H*.15),rotation:gsap.utils.random(-14,14),duration:1,ease:'power3.out'})},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx97` rules from `site/fx.css`

_No dedicated `.fx97` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #97
