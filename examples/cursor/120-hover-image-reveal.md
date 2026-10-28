# 120 · 清單懸停預覽圖 — Hover Image Reveal

滑過作品清單時，預覽圖跟著游標浮出並隨移動傾斜

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 游標 清單 列表 預覽 圖片 浮出 跟隨 Hover Image Reveal List Preview Follow Cursor Portfolio
- 標籤 Tag: Hover preview
- 範例文字 Example text: 「品牌識別 網站設計 包裝 插畫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「清單懸停預覽圖（Hover Image Reveal）」動態效果：一份大字作品清單（每列左邊作品名、右邊編號，列與列之間有細分隔線），未選中的列文字較淡；游標滑到某一列時，該列文字變清楚並稍微往右推，同時一張該作品的預覽圖從小放大浮現在游標旁邊並跟著游標移動，左右移動越快、圖片往移動方向傾斜越多；換到另一列時預覽圖換成另一張，離開清單時圖片縮小淡出。（做法：預覽圖 position:absolute + pointer-events:none，mousemove 時 translate 到游標位置，rotate 依水平速度計算並設上限；圖片切換用 opacity / scale 過場）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx120">`, preview text 「品牌識別 網站設計 包裝 插畫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「清單懸停預覽圖」.

### JavaScript — `FX[120]` from `site/fx.js`

```js
120(s,x,card){const l=el('div','abs hl');const rows=words(x).slice(0,4).map((w,i)=>{const r=el('div','hr');r.innerHTML=`<b></b><span>0${i+1}</span>`;r.querySelector('b').textContent=w;l.append(r);return r});const im=el('div','himg');l.append(im);s.append(l);let lx=0;
  vpointer(l,card,(px,py)=>{const i=rows.findIndex(r=>py>=r.offsetTop&&py<r.offsetTop+r.offsetHeight);rows.forEach((r,k)=>r.classList.toggle('on',k===i));im.classList.toggle('on',i>=0);if(i>=0)im.style.background=`linear-gradient(135deg,${GC[i%5]},${GC[(i+2)%5]})`;
    const vx=px-lx;lx=px;im.style.transform=`translate(${px}px,${py}px) rotate(${Math.max(-12,Math.min(12,vx*.8))}deg)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx120` rules from `site/fx.css`

_No dedicated `.fx120` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #120
