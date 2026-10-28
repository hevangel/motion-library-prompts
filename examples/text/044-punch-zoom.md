# 044 · 衝擊放大 — Punch Zoom

從深處飛出、後面拖著殘影

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 開場・強調
- 範例文字 Example text: 「突破」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「衝擊放大（Punch Zoom）」動態效果：文字從畫面深處（極小、模糊）高速衝向前方並略微放大過頭再回彈定位，後方拖著 4 層半透明殘影。約 2.2 秒一輪，開場強調感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx44">`, preview text 「突破」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「衝擊放大」.

### JavaScript — `FX[44]` from `site/fx.js`

```js
44(s,x){const w=el('div','w');for(let k=4;k>=1;k--){const g=T(x,18);g.classList.add('g');g.style.setProperty('--op',(.55/k).toFixed(2));g.style.setProperty('--d',(k*.05)+'s');w.append(g)}w.append(T(x,18));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx44` rules from `site/fx.css`

```css
.fx44 .w{position:relative}
.fx44 .t{color:#fff;animation:pz 2.2s var(--d,0s) infinite both cubic-bezier(.2,.9,.3,1.2)}
.fx44 .g{position:absolute;left:0;top:0;color:var(--a);opacity:var(--op)}
@keyframes pz{0%{transform:scale(.05);opacity:0;filter:blur(6px)}28%{transform:scale(1.14);filter:none;opacity:1}36%,84%{transform:scale(1);opacity:1}100%{transform:scale(1);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #44
