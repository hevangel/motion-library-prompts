# 057 · 圓柱 — Text Cylinder

文字圓柱反向旋轉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 立體・Logo
- 範例文字 Example text: 「轉圈圈」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「圓柱（Text Cylinder）」動態效果：三根以文字組成的 3D 圓柱（同一字環繞一圈），沿水平軸旋轉，相鄰圓柱方向相反，中間那根用強調色。約 4 秒轉一圈，立體 Logo 感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx57">`, preview text 「轉圈圈」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓柱」.

### JavaScript — `FX[57]` from `site/fx.js`

```js
57(s,x){const w=el('div','w');chars(x).slice(0,3).forEach((c,k)=>{const cy=el('div','cy'+(k%2?' rev':''));for(let i=0;i<10;i++){const e=el('span');e.textContent=c;e.style.setProperty('--a2',i*36+'deg');cy.append(e)}w.append(cy)});s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx57` rules from `site/fx.css`

```css
.fx57 .w{display:flex;gap:9cqw;transform-style:preserve-3d}
.fx57 .cy{position:relative;width:9cqw;height:9cqw;transform-style:preserve-3d;animation:cyl 4s linear infinite}
.fx57 .cy.rev{animation-direction:reverse}
.fx57 .cy span{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:8cqw;color:#111;backface-visibility:hidden;transform:rotateX(var(--a2)) translateZ(13cqw)}
.fx57 .cy:nth-child(2) span{color:var(--a)}
@keyframes cyl{to{transform:rotateX(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #57
