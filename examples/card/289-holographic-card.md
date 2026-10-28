# 289 · 全息閃卡 — Holographic Card

收藏卡跟著游標立體傾斜，表面的炫彩箔光和反光跟著角度流動

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、介面互動
- 風格／關鍵字 Style: 全息 閃卡 炫彩 箔 卡牌 寶可夢 傾斜 反光 Holographic Foil Card Tilt Glare Shiny Trading Card hover 懸停 滑過
- 標籤 Tag: mix-blend-mode
- 範例文字 Example text: 「HOLO」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「全息閃卡（Holographic Card）」動態效果：一張收藏卡（上方圖片、下方標題與編號），跟著游標在 3D 空間中傾斜（最大約 13 度）；卡片表面有一層炫彩的全息箔光，箔光的位置跟著游標移動，傾斜越多箔光越明顯，另外還有一團柔和反光跟著游標位置；游標離開時卡片回正、箔光淡化。（CSS + JS：mousemove 計算游標在卡片上的相對位置 0~1，設定 rotateX/rotateY 與 CSS 變數 --px、--py；箔光層是 repeating-linear-gradient 的炫彩條紋、mix-blend-mode:color-dodge，background-position 用 --px/--py；反光層是 radial-gradient 疊 overlay；父層 perspective）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx289">`, preview text 「HOLO」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「全息閃卡」.

### JavaScript — `FX[289]` from `site/fx.js`

```js
289(s,x,card){const l=el('div','abs gl ho-hw');const c=el('div','ho-ho');c.innerHTML='<div class="ho-hi">'+mdImg(2)+'</div><b></b><small>No. 289 · HOLO</small><i class="ho-foil"></i><i class="ho-gl"></i>';c.querySelector('b').textContent=x;l.append(c);s.append(l);
  vpointer(l,card,(px,py)=>{const r=c.getBoundingClientRect(),q=l.getBoundingClientRect(),cx=(px-(r.left-q.left))/r.width,cy=(py-(r.top-q.top))/r.height,X=Math.max(0,Math.min(1,cx)),Y=Math.max(0,Math.min(1,cy));
    c.style.transform=`rotateY(${(X-.5)*26}deg) rotateX(${(.5-Y)*26}deg)`;c.style.setProperty('--px',X*100+'%');c.style.setProperty('--py',Y*100+'%');c.style.setProperty('--d',Math.hypot(X-.5,Y-.5)*1.6)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx289` rules from `site/fx.css`

_No dedicated `.fx289` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #289
