# 164 · 卡片 3D 翻面 — Flip Card

滑過卡片時 3D 翻到背面，顯示更多資訊

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 卡片 翻轉 翻面 正反面 3D flip card hover back side hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS 3D
- 範例文字 Example text: 「品牌 網站 插畫」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「卡片 3D 翻面（Flip Card）」動態效果：一排作品卡片，正面是主視覺與標題；滑鼠移入時卡片以垂直軸 3D 翻轉 180 度到背面，背面顯示「查看專案 →」等行動文字，翻轉帶一點過衝回彈；移出時翻回正面。約 0.7 秒。（CSS：外層 perspective，內層 transform-style:preserve-3d + transition transform，hover 時 rotateY(180deg)；正反兩面 backface-visibility:hidden，背面預先 rotateY(180deg)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx164">`, preview text 「品牌 網站 插畫」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「卡片 3D 翻面」.

### JavaScript — `FX[164]` from `site/fx.js`

```js
164(s,x,card){const w=el('div','flp');const ws=words(x);const cs=[0,1,2].map(i=>{const c=el('div','fc2');c.innerHTML='<div class="in"><div class="f"><b></b><small>PROJECT 0'+(i+1)+'</small></div><div class="b">查看專案 →</div></div>';c.querySelector('.f').style.background=`linear-gradient(160deg,${GC[i]},${GC[(i+2)%5]})`;c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});s.append(w);autoHover(w,cs,card,1400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx164` rules from `site/fx.css`

_No dedicated `.fx164` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #164
