# 186 · 霓虹閃爍 — Neon Flicker

文字像霓虹燈管一樣不規則閃爍後點亮

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機、進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、Logo・品牌、強調重點
- 風格／關鍵字 Style: 霓虹 燈管 閃爍 發光 招牌 夜店 Neon Glow Flicker Sign Canva 風格 Canva Neon 霓虹 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「OPEN」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「霓虹閃爍（Neon Flicker）」動態效果：文字像剛通電的霓虹燈管：先暗著，接著不規則地快速閃兩下，然後穩定點亮並帶有多層外發光（內層較亮、外層擴散）；之後大部分時間穩定發光，偶爾再短暫閃一下，增加真實感。適合招牌、夜晚主題。（CSS：keyframes 在少數百分比切換 opacity 與 text-shadow 做不規則閃爍；發光用 2–3 層不同半徑的 text-shadow；圓體或粗體字效果較好）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx186">`, preview text 「OPEN」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「霓虹閃爍」.

### JavaScript — `FX[186]` from `site/fx.js`

```js
186(s,x){const t=T(x,Math.min(15,60/chars(x).length));t.classList.add('neo');s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx186` rules from `site/fx.css`

_No dedicated `.fx186` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #186
