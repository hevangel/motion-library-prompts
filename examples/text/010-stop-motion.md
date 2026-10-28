# 010 · 定格晃動 — Stop Motion

定格動畫般喀喀晃動

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 手作・玩具
- 範例文字 Example text: 「コマ撮り」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「定格晃動（Stop Motion）」動態效果：每個字以不連續、一格一格跳動的方式隨機微晃與微旋轉（像定格動畫，無平滑過渡），各字節奏錯開。約 0.9 秒循環，手作玩具感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx10">`, preview text 「コマ撮り」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「定格晃動」.

### JavaScript — `FX[10]` from `site/fx.js`

```js
10(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx10` rules from `site/fx.css`

```css
.fx10 .c{animation:stp .9s calc(var(--i)*-.23s) infinite steps(1)}
@keyframes stp{0%{transform:rotate(-6deg) translate(2%,-4%)}25%{transform:rotate(4deg) translate(-3%,3%)}50%{transform:rotate(-2deg) translate(2%,5%)}75%{transform:rotate(7deg) translate(-2%,-2%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #10
