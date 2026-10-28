# 190 · 滑行 — Skate

文字像溜冰一樣斜著滑進來，煞車後擺正

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場、退場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、轉場切換
- 風格／關鍵字 Style: 滑行 溜冰 傾斜 煞車 速度感 Skate Skew Slide Brake Canva 風格 Canva Skate 滑行 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「滑行進場」（預覽底色：acc）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「滑行（Skate）」動態效果：文字從左側高速滑入時整體往前傾斜（skewX 約 -28 度），抵達時稍微滑過頭並往反方向傾斜（像煞車時身體往後仰），接著擺正停住；離場時再加速往右滑出並重新前傾。有速度感與重量感。（CSS：keyframes 依序 translateX(-70%) skewX(-28deg) → translateX(4%) skewX(14deg) → skewX(-4deg) → none，離場段用加速曲線）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx190">`, preview text 「滑行進場」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滑行」.

### JavaScript — `FX[190]` from `site/fx.js`

```js
190(s,x){const t=T(x,Math.min(12,60/chars(x).length));t.classList.add('skt');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx190` rules from `site/fx.css`

_No dedicated `.fx190` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #190
