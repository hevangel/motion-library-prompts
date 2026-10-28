# 003 · 硬幣翻轉 — Coin Flip

文字像硬幣一樣翻轉彈跳

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 碰運氣・遊戲
- 範例文字 Example text: 「表か裏か」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「硬幣翻轉（Coin Flip）」動態效果：每個字像硬幣一樣以 Y 軸翻轉兩圈並往上跳，落地後再小彈一下，字與字之間依序延遲約 0.14 秒。約 2.4 秒一輪，輕快俏皮。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx3">`, preview text 「表か裏か」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「硬幣翻轉」.

### JavaScript — `FX[3]` from `site/fx.js`

```js
3(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx3` rules from `site/fx.css`

```css
.fx3 .c{animation:coin 2.4s calc(var(--i)*.14s) infinite}
@keyframes coin{0%{transform:translateY(0) rotateY(0)}28%{transform:translateY(-45%) rotateY(360deg)}42%{transform:translateY(0) rotateY(720deg)}48%{transform:translateY(-8%) rotateY(720deg)}54%,100%{transform:translateY(0) rotateY(720deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #3
