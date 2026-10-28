# 252 · 反色混合游標 — Blend Difference Cursor

一顆圓形游標，經過文字時放大，重疊的地方顏色反轉

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 反色 反轉 混合模式 difference 游標 圓形 Blend Mode Invert Cursor Hero 游標 滑鼠
- 標籤 Tag: mix-blend-mode
- 範例文字 Example text: 「INVERT」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「反色混合游標（Blend Difference Cursor）」動態效果：游標替換成一顆實心圓，以平滑的延遲跟隨滑鼠；圓形使用「差異」混合模式，與底下的文字重疊時，文字和背景的顏色互相反轉；當游標移到大標題上時，圓形平滑放大約三倍，讓反轉範圍覆蓋更多文字，離開標題後縮回。（CSS：圓形元素 mix-blend-mode:difference、pointer-events:none；JS 每幀以 lerp 追上滑鼠座標，並偵測是否在標題範圍內以插值改變 scale；容器 cursor:none 隱藏原生游標）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx252">`, preview text 「INVERT」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「反色混合游標」.

### JavaScript — `FX[252]` from `site/fx.js`

```js
252(s,x,card){const l=el('div','abs gl cr-bl');l.append(T(x,Math.min(15,64/chars(x).length)));const c=el('i','cr-bc');l.append(c);s.append(l);let cx=0,cy=0,tx=0,ty=0,big=false,sc=.35;
  vpointer(l,card,(px,py)=>{tx=px;ty=py;const t=l.querySelector('.t').getBoundingClientRect(),r=l.getBoundingClientRect();big=px>t.left-r.left&&px<t.right-r.left&&py>t.top-r.top&&py<t.bottom-r.top});
  const loop=()=>{cx+=(tx-cx)*.2;cy+=(ty-cy)*.2;sc+=((big?1:.3)-sc)*.12;c.style.transform=`translate(${cx}px,${cy}px) translate(-50%,-50%) scale(${sc})`};const prev=ticks.get(card);ticks.set(card,t=>{prev&&prev(t);loop()})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx252` rules from `site/fx.css`

_No dedicated `.fx252` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #252
