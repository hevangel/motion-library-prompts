# 048 · 巨字滑過 — Huge Text Scroll

超大字一快一慢橫越畫面

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 背景・遠景
- 範例文字 Example text: 「台北夜行」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「巨字滑過（Huge Text Scroll）」動態效果：超大字級的文字（比畫面還大）持續由右往左慢慢橫越，底部另有一條細帶，帶上的小字以較快速度反方向滑動。大字約 9 秒一輪，遠景背景感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx48">`, preview text 「台北夜行」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「巨字滑過」.

### JavaScript — `FX[48]` from `site/fx.js`

```js
48(s,x){s.append(mqRow(rep(x+'・',3),34,9,false,'font-weight:900;line-height:1;color:#fff'));const sm=mqRow(rep(x+'・',10),4,5,true);sm.className+=' small';s.append(sm)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx48` rules from `site/fx.css`

```css
.fx48 .big{font-weight:900;font-size:34cqw;line-height:1;color:#fff}
.fx48 .small{position:absolute;bottom:3cqw;left:0;font-weight:900;font-size:4cqw;background:var(--a);color:#111;padding:.3cqw 0}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #48
