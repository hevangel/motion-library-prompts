# 175 · 數字雨 — Matrix Rain

一行行字元像下雨一樣往下落，帶殘影拖尾

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: Canvas
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 數字雨 駭客 程式碼 字元 矩陣 科技 Matrix Code Rain Hacker Digital Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas text
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「數字雨（Matrix Rain）」動態效果：整個區塊被一欄欄往下落的字元填滿（片假名、數字、英文），每欄速度一致、起點不同，最前端的字最亮，後面的字逐漸變暗拉出拖尾；落到底部後隨機回到頂端重新開始。科技、駭客感。（Canvas 2D：欄數 = 寬度 ÷ 字級，每欄記錄目前的 y；每約 55ms 用半透明底色覆蓋整個畫面一次，再在每欄目前位置畫一個隨機字元，y 往下一格，超出畫面後隨機重置）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx175">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「數字雨」.

### JavaScript — `FX[175]` from `site/fx.js`

```js
175(s,x,card){const CH='アイウエオカキクケコサシスセソタチツテト0123456789ABCDEF';cfx(s,card,{init:(c,W,H)=>{c.fillStyle=`rgb(${BGD})`;c.fillRect(0,0,W,H);const fs=W/38;return{fs,D:[...Array(Math.ceil(W/fs))].map(()=>rnd(-H/fs,0)),acc:0,c:accRGB(s)}},
  frame:(c,W,H,t,dt,m,o)=>{o.acc+=dt;if(o.acc<.055)return;o.acc=0;c.fillStyle=`rgba(${BGD},.12)`;c.fillRect(0,0,W,H);c.font=`700 ${o.fs}px ui-monospace,monospace`;c.textAlign='center';
    o.D.forEach((y,i)=>{const ch=CH[Math.floor(Math.random()*CH.length)],px=i*o.fs+o.fs/2,py=y*o.fs;c.fillStyle=`rgba(${o.c},.85)`;c.fillText(ch,px,py-o.fs);c.fillStyle='#fff';c.fillText(CH[Math.floor(Math.random()*CH.length)],px,py);
      o.D[i]=py>H&&Math.random()>.96?0:y+1})}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx175` rules from `site/fx.css`

_No dedicated `.fx175` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #175
