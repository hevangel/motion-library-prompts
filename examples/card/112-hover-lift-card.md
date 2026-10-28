# 112 · 卡片浮起 — Hover Lift Card

hover 時卡片上浮、陰影加深，縮圖在框內放大

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 卡片 hover 浮起 陰影 縮圖 放大 Hover Lift Card Shadow Zoom 作品集 商品
- 標籤 Tag: CSS hover
- 範例文字 Example text: 「品牌 網站 插畫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「卡片浮起（Hover Lift Card）」動態效果：一排作品卡片（上方縮圖、下方標題與一條文字列）。滑鼠移到某張卡片上時，卡片往上浮起一點並出現更深更大的陰影，縮圖在原本的框內慢慢放大約 1.15 倍（框不變、圖被裁切）；滑鼠離開時平滑回到原位。約 0.45–0.6 秒，緩出。（CSS：卡片 transition transform 與 box-shadow，:hover 時 translateY(-8px)；縮圖外框 overflow:hidden，內層圖 transform:scale(1.14)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx112">`, preview text 「品牌 網站 插畫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「卡片浮起」.

### JavaScript — `FX[112]` from `site/fx.js`

```js
112(s,x,card){const w=el('div','lift');const ws=words(x);const cs=[0,1,2].map(i=>{const c=el('div','lc');c.innerHTML='<div class="im"><i></i></div><b></b><span></span>';c.querySelector('b').textContent=ws[i%ws.length];c.querySelector('.im i').style.background=`linear-gradient(135deg,${GC[i]},${GC[(i+1)%5]})`;w.append(c);return c});s.append(w);
  let k=0,real=false;w.addEventListener('pointerenter',()=>{real=true;cs.forEach(c=>c.classList.remove('hv'))});w.addEventListener('pointerleave',()=>real=false);
  card._timers.push(setInterval(()=>{if(real)return;cs.forEach((c,i)=>c.classList.toggle('hv',i===k%3));k++},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx112` rules from `site/fx.css`

_No dedicated `.fx112` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #112
