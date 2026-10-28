# 263 · 滑過放大檢視 — Hover Zoom & Pan

滑過圖片時放大兩倍，放大的位置跟著游標移動，看商品細節

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 放大 檢視 細節 商品圖 電商 跟隨游標 平移 Zoom Pan Hover Product Detail Ecommerce 圖片 媒體
- 標籤 Tag: transform-origin
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「滑過放大檢視（Hover Zoom & Pan）」動態效果：商品大圖：滑鼠移進圖片時，圖片在原本的框內平滑放大到約 2.2 倍，而且放大的中心點跟著游標位置移動——游標移到左上就看左上的細節，移到右下就看右下；滑鼠離開時縮回原尺寸。右下角有「滑過看細節」的小提示，放大時淡出。（JS + CSS：mousemove 時把 transform-origin 設為游標在圖片中的百分比位置，容器 :hover 時 scale(2.2)，transition 0.5 秒；容器 overflow:hidden、cursor:zoom-in）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx263">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滑過放大檢視」.

### JavaScript — `FX[263]` from `site/fx.js`

```js
263(s,x,card){const f=el('div','md-zp');f.innerHTML=mdImg(1)+'<span class="md-zh">滑過看細節</span>';s.append(f);const im=f.querySelector('.md-im');let on=false;
  f.addEventListener('pointerenter',()=>on=true);f.addEventListener('pointerleave',()=>{on=false;f.classList.remove('on')});
  vpointer(f,card,(px,py)=>{const W=f.offsetWidth,H=f.offsetHeight;f.classList.add('on');im.style.transformOrigin=`${px/W*100}% ${py/H*100}%`},(t,W,H)=>{const k=Math.sin(t*.5);if(k<-.6)f.classList.remove('on');return[W*(.5+.4*Math.sin(t*1.1)),H*(.5+.35*Math.cos(t*.8))]})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx263` rules from `site/fx.css`

_No dedicated `.fx263` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #263
