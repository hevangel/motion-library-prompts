# 166 · Dock 放大選單 — Dock Magnify

游標掃過一排圖示時，靠近的圖示放大並推開鄰居

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: Dock 放大 圖示 選單 macOS 工具列 magnify icons toolbar hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS + JS
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「Dock 放大選單（Dock Magnify）」動態效果：像 macOS Dock 的一排圓角圖示：游標在圖示列附近左右移動時，最靠近游標的圖示放大到約 1.9 倍，左右鄰近的圖示依距離遞減地跟著放大，形成平滑的放大波峰，並把其他圖示往兩側推開；游標離開時全部恢復原尺寸。（做法：mousemove 時計算每個圖示中心與游標的水平距離，scale = 1 + 0.9 × max(0, 1 − 距離/影響範圍)，寫入 CSS 變數控制 width / height，讓排版自然推開；加短 transition 讓變化順滑）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx166">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「Dock 放大選單」.

### JavaScript — `FX[166]` from `site/fx.js`

```js
166(s,x,card){const l=el('div','abs dockw');const d=el('div','dock');const ic=[...Array(7)].map((_,i)=>{const e=el('i','dki');e.style.background=`linear-gradient(140deg,${GC[i%5]},${GC[(i+2)%5]})`;d.append(e);return e});l.append(d);s.append(l);
  vpointer(l,card,(px,py)=>{const r=d.getBoundingClientRect(),lr=l.getBoundingClientRect();const cy=r.top-lr.top+r.height/2,near=Math.abs(py-cy)<r.height*1.6;const R=l.offsetWidth*.18;
    ic.forEach(e=>{const cx=e.offsetLeft+e.offsetWidth/2+(d.offsetLeft);const k=near?Math.max(0,1-Math.abs(px-cx)/R):0;e.style.setProperty('--s',1+k*.9)})},(t,W,H)=>[W*(.5+.42*Math.sin(t*.8)),H*.62])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx166` rules from `site/fx.css`

_No dedicated `.fx166` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #166
