# 264 · 低飽和喚醒 — Saturate on Hover

圖片平常是低飽和、偏暗，滑過時恢復鮮豔並微微放大

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 灰階 去色 飽和度 喚醒 濾鏡 作品集 團隊照片 Grayscale Saturate Filter Hover Team 圖片 媒體
- 標籤 Tag: CSS filter
- 範例文字 Example text: 「春 夏 秋」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「低飽和喚醒（Saturate on Hover）」動態效果：一排團隊或作品照片，平常呈現低飽和、略暗的樣子，讓整排畫面安靜統一；滑鼠滑過某張時，該張在約 0.6 秒內恢復完整的飽和度與亮度，並在框內微微放大到 1.05 倍，底部的名字標籤浮上來。（CSS：img 預設 filter: grayscale(.9) brightness(.8)，:hover 時 filter:none 並 scale(1.05)，filter 與 transform 一起 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx264">`, preview text 「春 夏 秋」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「低飽和喚醒」.

### JavaScript — `FX[264]` from `site/fx.js`

```js
264(s,x,card){const ws=words(x);const w=el('div','md-sg');const fs=[0,1,3].map((p,i)=>{const f=el('figure','md-st');f.innerHTML=mdImg(p)+'<figcaption></figcaption>';f.querySelector('figcaption').textContent=ws[i%ws.length];w.append(f);return f});s.append(w);autoHover(w,fs,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx264` rules from `site/fx.css`

_No dedicated `.fx264` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #264
