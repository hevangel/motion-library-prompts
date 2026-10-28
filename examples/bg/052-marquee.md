# 052 · 跑馬燈 — Marquee

字體、速度都不同的帶子疊在一起

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、數字資訊
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 公告・街頭
- 範例文字 Example text: 「限時開賣 新品上市 預購中 最後一天」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「跑馬燈（Marquee）」動態效果：四條橫向跑馬燈疊在一起，每條字體、字級、速度、方向都不同，帶子之間有細分隔線。速度 5–11 秒一輪不等，像街頭公告看板。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx52">`, preview text 「限時開賣 新品上市 預購中 最後一天」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「跑馬燈」.

### JavaScript — `FX[52]` from `site/fx.js`

```js
52(s,x){const r=el('div','rows');const ws=words(x);const F=['"Noto Sans JP"','"Zen Maru Gothic"','"Noto Serif JP"','"Reggae One"'];const sz=[6,9,5,8],du=[7,11,5,9];for(let i=0;i<4;i++){const w=ws[i%ws.length];r.append(mqRow(rep(w+'・',10),sz[i],du[i],i%2,`font-family:${F[i]}`))}s.append(r)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx52` rules from `site/fx.css`

```css
.fx52 .rows{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center}
.fx52 .mq{border-bottom:.3cqw solid #111;color:#111;font-weight:900;line-height:1.25}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #52
