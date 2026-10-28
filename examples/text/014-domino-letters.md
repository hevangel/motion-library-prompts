# 014 · 骨牌倒下 — Domino Letters

文字像骨牌一樣倒下

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: 幽默・連鎖
- 範例文字 Example text: 「ドミノ倒し」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「骨牌倒下（Domino Letters）」動態效果：每個字以右下角為支點，依序往右倒下約 72 度，像骨牌一樣連鎖傾倒，停留後一起站回。字下方有一條地板線，約 3.2 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx14">`, preview text 「ドミノ倒し」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「骨牌倒下」.

### JavaScript — `FX[14]` from `site/fx.js`

```js
14(s,x){s.append(split(x),el('div','floor'))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx14` rules from `site/fx.css`

```css
.fx14 .c{transform-origin:100% 100%;animation:dom 3.2s calc(var(--i)*.13s) infinite cubic-bezier(.5,0,.8,.6)}
.fx14 .c:nth-child(3n+2){color:#fff6ea}
.fx14 .floor{position:absolute;left:8%;right:8%;bottom:26%;height:2px;background:#0005}
@keyframes dom{0%,8%{transform:none}24%,74%{transform:rotate(72deg)}86%,100%{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #14
