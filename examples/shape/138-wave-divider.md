# 138 · 波浪分隔線 — Wave Divider

區塊底部多層波浪以不同速度緩慢流動

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、轉場切換
- 風格／關鍵字 Style: 波浪 分隔線 區塊分隔 水波 海浪 Wave Divider Section Separator Liquid
- 標籤 Tag: SVG wave
- 範例文字 Example text: 「波浪分隔」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「波浪分隔線（Wave Divider）」動態效果：兩個區塊之間用波浪形狀分隔，波浪由 3 層組成，後層較淡較高、前層較實較低，三層以不同速度（約 6、9、13 秒一輪）左右緩慢流動、方向不完全相同，形成有深度的水波感，無縫循環。（CSS：每層是一個寬度 200%、內含兩個完整波長的 SVG path，用 translateX(0 → -50%) 的 linear 無限動畫做到無縫；不同層設定不同 animation-duration 與方向）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx138">`, preview text 「波浪分隔」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「波浪分隔線」.

### JavaScript — `FX[138]` from `site/fx.js`

```js
138(s,x){const W='M0,20 C25,8 25,8 50,20 C75,32 75,32 100,20 C125,8 125,8 150,20 C175,32 175,32 200,20 L200,40 L0,40 Z';s.append(T(x,Math.min(10,50/chars(x).length)));
  s.insertAdjacentHTML('beforeend',`<div class="wv">${[0,1,2].map(i=>`<svg viewBox="0 0 200 40" preserveAspectRatio="none" class="w${i}"><path d="${W}"/></svg>`).join('')}</div>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx138` rules from `site/fx.css`

```css
.fx138 .t{color:#fff;margin-bottom:16cqw}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #138
