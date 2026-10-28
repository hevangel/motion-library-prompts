# 060 · 方塊 — Text Cube

四面寫字的方塊直向翻轉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 轉場切換、數字資訊
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 切換・立體
- 範例文字 Example text: 「春夏秋冬」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「方塊（Text Cube）」動態效果：一個 3D 立方體，四個面各寫一個字，以水平軸每次翻轉 90 度換到下一面，翻轉後停留一下，略帶傾斜視角，方塊有粗邊框。約 1.5 秒換一面。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx60">`, preview text 「春夏秋冬」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「方塊」.

### JavaScript — `FX[60]` from `site/fx.js`

```js
60(s,x){const c=el('div','cube');const cs=chars(x);for(let i=0;i<4;i++){const e=el('span');e.textContent=cs[i%cs.length];e.style.setProperty('--a2',-i*90+'deg');c.append(e)}s.append(c)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx60` rules from `site/fx.css`

```css
.fx60 .cube{position:relative;width:24cqw;height:24cqw;transform-style:preserve-3d;animation:cube 6s infinite}
.fx60 .cube span{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:16cqw;background:var(--a);color:#111;border:.4cqw solid #111;transform:rotateX(var(--a2)) translateZ(12cqw)}
@keyframes cube{0%,18%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(0)}25%,43%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(90deg)}50%,68%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(180deg)}75%,93%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(270deg)}100%{transform:rotateX(-18deg) rotateY(-24deg) rotateX(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #60
