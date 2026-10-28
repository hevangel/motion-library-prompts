# 021 · 磁鐵吸附 — Magnet Pull

文字像被磁鐵吸過來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌、標題・Hero
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 集中・Logo
- 範例文字 Example text: 「引き寄せる」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「磁鐵吸附（Magnet Pull）」動態效果：文字一開始散得很開、模糊且半透明，接著像被磁鐵吸住一樣加速往中心靠攏、略微過衝後吸附定位，停留後再散開；最後兩個字用強調色當重點。約 2.8 秒一輪。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx21">`, preview text 「引き寄せる」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「磁鐵吸附」.

### JavaScript — `FX[21]` from `site/fx.js`

```js
21(s,x){const t=split(x);const cs=t.querySelectorAll('.c');const mid=(cs.length-1)/2;cs.forEach((c,i)=>c.style.setProperty('--o',(i-mid)));s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx21` rules from `site/fx.css`

```css
.fx21 .c{color:#888;animation:mag 2.8s infinite}
.fx21 .c:nth-last-child(-n+2){color:var(--a)}
@keyframes mag{0%,8%{transform:translateX(calc(var(--o)*16cqw)) scale(.75);filter:blur(3px);opacity:.25;animation-timing-function:cubic-bezier(.7,0,1,.6)}48%{transform:translateX(calc(var(--o)*-.8cqw)) scale(1.05);filter:none;opacity:1}55%,82%{transform:none;filter:none;opacity:1}100%{transform:translateX(calc(var(--o)*16cqw)) scale(.75);filter:blur(3px);opacity:.25}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #21
