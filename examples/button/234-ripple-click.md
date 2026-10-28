# 234 · 按鈕漣漪回饋 — Ripple Click

從手指點下的位置擴散出一圈漣漪，Material Design 經典回饋

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 漣漪 水波 點擊 回饋 Material Design Ripple Click Feedback Ink 按鈕
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「送出表單」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「按鈕漣漪回饋（Ripple Click）」動態效果：點擊按鈕時，從手指（游標）按下的那個點擴散出一個圓形漣漪，漣漪半透明、由小放大到能蓋住整顆按鈕的大小並同時淡出，約 0.7 秒；連續點擊可同時出現多個漣漪。（JS：pointerdown 時計算點擊位置與到最遠角落的距離 × 2 當直徑，插入一個圓形 span，CSS keyframes scale 0→1、opacity 漸消，animationend 時移除；按鈕 overflow:hidden）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx234">`, preview text 「送出表單」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「按鈕漣漪回饋」.

### JavaScript — `FX[234]` from `site/fx.js`

```js
234(s,x,card){const b=bxBtn('bx-rp',x);s.append(b);const rip=(px,py)=>{const r=el('i');const W=b.offsetWidth,H=b.offsetHeight,d=Math.hypot(Math.max(px,W-px),Math.max(py,H-py))*2;r.style.cssText=`left:${px}px;top:${py}px;width:${d}px;height:${d}px`;b.append(r);r.addEventListener('animationend',()=>r.remove())};
  b.addEventListener('pointerdown',e=>{const r=b.getBoundingClientRect();rip(e.clientX-r.left,e.clientY-r.top)});bxDemo(b,card,()=>rip(rnd(.15,.85)*b.offsetWidth,rnd(.2,.8)*b.offsetHeight),1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx234` rules from `site/fx.css`

_No dedicated `.fx234` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #234
