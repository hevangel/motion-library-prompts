# 020 · 重力反轉 — Gravity Flip

重力反轉往上彈

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 驚奇・SF
- 範例文字 Example text: 「重力反転」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「重力反轉（Gravity Flip）」動態效果：每個字先加速往上「掉」到上方並翻轉成上下顛倒，停留後再掉回原位並翻正，落地時小彈一下，字與字依序錯開。約 3 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx20">`, preview text 「重力反転」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「重力反轉」.

### JavaScript — `FX[20]` from `site/fx.js`

```js
20(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx20` rules from `site/fx.css`

```css
.fx20 .c{animation:grv 3s calc(var(--i)*.09s) infinite}
.fx20 .c:nth-child(even){color:var(--a)}
@keyframes grv{0%,10%{transform:none;animation-timing-function:cubic-bezier(.5,0,1,.5)}33%{transform:translateY(-80%) rotate(180deg);animation-timing-function:ease-out}40%{transform:translateY(-65%) rotate(180deg);animation-timing-function:ease-in}46%,58%{transform:translateY(-80%) rotate(180deg);animation-timing-function:cubic-bezier(.5,0,1,.5)}80%{transform:translateY(0) rotate(360deg);animation-timing-function:ease-out}87%{transform:translateY(-14%) rotate(360deg)}93%,100%{transform:rotate(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #20
