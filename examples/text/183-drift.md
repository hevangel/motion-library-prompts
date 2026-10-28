# 183 · 漂移 — Drift

文字從側邊淡入後持續緩慢漂移，再淡出

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場、退場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、轉場切換
- 風格／關鍵字 Style: 漂移 緩慢 橫移 淡入淡出 簡報 Drift Slow Slide Fade Canva 風格 Canva Drift 漂移 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「慢慢漂移」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「漂移（Drift）」動態效果：文字從右側約 12% 的位置淡入並快速減速，之後沒有停下，而是以非常慢的等速持續往左漂移，最後一邊漂移一邊淡出；整段約 4 秒，給人安靜流動的感覺，適合簡報或社群貼文的標題。（CSS：keyframes 前 20% 用減速曲線淡入，20%–80% 線性小幅位移，最後淡出）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx183">`, preview text 「慢慢漂移」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「漂移」.

### JavaScript — `FX[183]` from `site/fx.js`

```js
183(s,x){s.append(T(x,Math.min(12,60/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx183` rules from `site/fx.css`

```css
.fx183 .t{animation:drift 4.2s linear infinite}
@keyframes drift{0%{transform:translateX(12%);opacity:0;animation-timing-function:cubic-bezier(.2,.6,.3,1)}20%{transform:translateX(3%);opacity:1;animation-timing-function:linear}80%{transform:translateX(-3%);opacity:1}100%{transform:translateX(-6%);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #183
