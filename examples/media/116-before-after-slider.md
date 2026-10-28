# 116 · 前後對比滑桿 — Before / After Slider

拖曳中間的把手，左右比較兩張圖的差異

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 拖曳手勢、懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 圖片 比較 對比 前後 滑桿 拖曳 Before After Compare Slider Image Comparison
- 標籤 Tag: clip-path・Drag
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「前後對比滑桿（Before / After Slider）」動態效果：兩張同尺寸的圖片重疊，中間有一條直線和圓形把手（帶左右箭頭），左上角標示 BEFORE、右上角標示 AFTER；拖曳把手時分界線跟著左右移動，左邊顯示原圖、右邊顯示修改後的圖，方便比較差異；未操作時可以緩慢左右擺動提示可拖曳。（做法：上層圖片用 clip-path:inset(0 0 0 var(--p))，pointerdown/pointermove 算出游標在框內的比例寫入 --p；把手用 setPointerCapture 確保拖出框外也能繼續拖；手機上設 touch-action:pan-y）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx116">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「前後對比滑桿」.

### JavaScript — `FX[116]` from `site/fx.js`

```js
116(s,x,card){const w=el('div','ba');w.innerHTML=`<div class="b1">${scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8')}</div><div class="b2">${scene('#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0')}</div><div class="hd"><i></i></div><span class="lb l">BEFORE</span><span class="lb r">AFTER</span>`;s.append(w);
  let drag=false,idle=0;const set=v=>w.style.setProperty('--p',v*100+'%');set(.5);const move=e=>{const r=w.getBoundingClientRect();set(Math.min(1,Math.max(0,(e.clientX-r.left)/r.width)))};
  w.addEventListener('pointerdown',e=>{drag=true;idle=Infinity;w.setPointerCapture(e.pointerId);move(e)});w.addEventListener('pointermove',e=>{if(drag)move(e)});w.addEventListener('pointerup',()=>{drag=false;idle=performance.now()+3000});
  ticks.set(card,t=>{if(!drag&&performance.now()>idle)set(.5+.38*Math.sin(t*1.2))})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx116` rules from `site/fx.css`

_No dedicated `.fx116` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #116
