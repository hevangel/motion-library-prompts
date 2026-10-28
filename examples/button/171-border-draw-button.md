# 171 · 邊框描繪按鈕 — Border Draw Button

滑過按鈕時，四條邊框依序畫出圍住按鈕

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 按鈕 邊框 描邊 線條 畫出 border draw outline button hover hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS transition
- 範例文字 Example text: 「了解更多」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「邊框描繪按鈕（Border Draw Button）」動態效果：平時只有很淡細框的按鈕，滑鼠移入時，強調色的邊框從左上角開始依序畫出：上邊往右 → 右邊往下 → 下邊往左 → 左邊往上，每段約 0.18 秒，接起來把按鈕圍住，畫完後文字也換成強調色；滑鼠移出時以相反順序收回。（CSS：四個絕對定位的線條元素，各自用 scaleX / scaleY 搭配不同 transform-origin；用 transition-delay 安排順序，hover 與非 hover 狀態的 delay 相反）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx171">`, preview text 「了解更多」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「邊框描繪按鈕」.

### JavaScript — `FX[171]` from `site/fx.js`

```js
171(s,x,card){const b=el('button','bdr');b.innerHTML='<i class="t"></i><i class="r"></i><i class="b"></i><i class="l"></i><span></span>';b.querySelector('span').textContent=x;s.append(b);autoHover(b,[b],card,1600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx171` rules from `site/fx.css`

_No dedicated `.fx171` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #171
