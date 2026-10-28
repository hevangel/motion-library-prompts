# 027 · 像素溶解 — Pixel Dissolve

化成方塊溶解消失再復原

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: 數位
- 範例文字 Example text: 「ピクセル化」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「像素溶解（Pixel Dissolve）」動態效果：文字上方覆蓋小方格，方格隨機一格格出現把文字遮掉，再一格格消失讓文字回來，夾雜少數強調色方塊，像像素溶解。約 3 秒一輪，數位感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx27">`, preview text 「ピクセル化」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「像素溶解」.

### JavaScript — `FX[27]` from `site/fx.js`

```js
27(s,x){s.append(T(x));const px=el('div','px');for(let i=0;i<24*14;i++){const c=el('i',Math.random()<.12?'k':(Math.random()<.06?'h':''));c.style.setProperty('--d',(Math.random()*.9).toFixed(2)+'s');px.append(c)}s.append(px)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx27` rules from `site/fx.css`

```css
.fx27 .px{position:absolute;inset:0;display:grid;grid-template-columns:repeat(24,1fr);grid-template-rows:repeat(14,1fr)}
.fx27 .px i{background:var(--cream);opacity:0;animation:pix 3s var(--d) infinite steps(1)}
.fx27 .px i.k{background:#111}
.fx27 .px i.h{background:var(--a)}
@keyframes pix{0%,25%{opacity:0}40%,60%{opacity:1}75%,100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #27
