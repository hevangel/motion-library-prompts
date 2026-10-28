# 032 · 洗牌重排 — Shuffle Letters

文字互換位置後排整齊

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 遊戲・解謎
- 範例文字 Example text: 「ならびかえ」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「洗牌重排（Shuffle Letters）」動態效果：文字的每個字隨機互換位置並帶點彈跳與歪斜，連續洗牌幾次後歸位排整齊，停留後再開始洗。每次換位約 0.6 秒，遊戲解謎感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx32">`, preview text 「ならびかえ」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「洗牌重排」.

### JavaScript — `FX[32]` from `site/fx.js`

```js
32(s,x,card){const cs=chars(x),n=cs.length;const t=T(x);t.classList.add('w');t.style.width=(n*1.05)+'em';const sp=cs.map((c,i)=>{const e=el('span','c');e.textContent=c;t.append(e);return e});s.append(t);
  const place=o=>sp.forEach((e,i)=>{e.style.left=(o[i]*1.05)+'em';e.style.transform=o[i]===i?'none':`translateY(${(Math.random()-.5)*40}%) rotate(${(Math.random()-.5)*30}deg)`});
  const shuf=()=>{const a=[...Array(n).keys()];for(let i=n-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
  let step=0;place(shuf());card._timers.push(setInterval(()=>{step=(step+1)%7;place(step<4?shuf():[...Array(n).keys()])},600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx32` rules from `site/fx.css`

```css
.fx32 .w{position:relative;height:1.2em}
.fx32 .c{position:absolute;top:0;transition:left .45s cubic-bezier(.5,1.6,.5,1),transform .45s}
.fx32 .c:nth-child(odd){color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #32
