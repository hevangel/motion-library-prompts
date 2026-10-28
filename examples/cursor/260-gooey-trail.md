# 260 · 黏液拖尾 — Gooey Trail

一串圓球跟著游標，彼此像黏液一樣融合拉絲

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 黏液 融合 拖尾 液態 Gooey Blob Trail Cursor SVG Filter Liquid 游標 滑鼠
- 標籤 Tag: SVG goo filter
- 範例文字 Example text: 「Gooey」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「黏液拖尾（Gooey Trail）」動態效果：游標後方跟著一串大小遞減的圓球，第一顆緊跟滑鼠、後面每顆跟著前一顆，形成一條尾巴；圓球之間透過模糊加對比的濾鏡融合在一起，看起來像一團黏液被拉長、拉出細絲，停下來時又縮回一團。前景文字使用混合模式，被黏液蓋到的部分反轉。（SVG filter：feGaussianBlur stdDeviation 約 6 + feColorMatrix 將 alpha 放大（例如 0 0 0 22 −9）形成 goo 效果，套在包住所有圓球的容器上；JS 每幀讓每顆圓球 lerp 追前一顆）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx260">`, preview text 「Gooey」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「黏液拖尾」.

### JavaScript — `FX[260]` from `site/fx.js`

```js
260(s,x,card){const id='cg'+Math.random().toString(36).slice(2);const l=el('div','abs cr-go');l.innerHTML=`<svg width="0" height="0" style="position:absolute"><filter id="${id}"><feGaussianBlur in="SourceGraphic" stdDeviation="6"/><feColorMatrix values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 22 -9"/></filter></svg><div class="cr-gb" style="filter:url(#${id})"></div>`;const gb=l.querySelector('.cr-gb');
  const N=8,B=[...Array(N)].map((_,i)=>{const b=el('i');b.style.setProperty('--s',1-i/N*.7);gb.append(b);return{e:b,x:0,y:0}});const t=T(x,Math.min(12,52/chars(x).length));t.classList.add('cr-gt');l.append(t);s.append(l);let tx=0,ty=0;
  vpointer(l,card,(px,py)=>{tx=px;ty=py});const prev=ticks.get(card);ticks.set(card,tm=>{prev&&prev(tm);let ax=tx,ay=ty;B.forEach((b,i)=>{b.x+=(ax-b.x)*(i?.45:.3);b.y+=(ay-b.y)*(i?.45:.3);b.e.style.transform=`translate(${b.x}px,${b.y}px) translate(-50%,-50%) scale(var(--s))`;ax=b.x;ay=b.y})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx260` rules from `site/fx.css`

_No dedicated `.fx260` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #260
