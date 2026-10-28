# 013 · 亂碼解讀 — Scramble Decode

從亂碼解讀成正確文字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、數字資訊
- 風格／關鍵字 Style: 文字切換
- 標籤 Tag: 駭客・SF
- 範例文字 Example text: 「解読完了」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「亂碼解讀（Scramble Decode）」動態效果：文字一開始是不斷跳動的亂碼（片假名、符號、數字），再由左到右逐字解碼成正確文字並改用強調色，停留後重新開始。像素點陣字體，駭客科幻感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx13">`, preview text 「解読完了」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「亂碼解讀」.

### JavaScript — `FX[13]` from `site/fx.js`

```js
13(s,x,card){const t=T(x);s.append(t);const tgt=chars(x),pool='アイウエオカキクケコ#$%&@01XZ暗号解読完了ﾊﾞｸ';let f=0;
  card._timers.push(setInterval(()=>{f++;const cyc=f%(tgt.length*7+40);t.innerHTML=tgt.map((c,i)=>cyc>8+i*7?`<span class="r">${c}</span>`:pool[Math.floor(Math.random()*pool.length)]).join('')},55))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx13` rules from `site/fx.css`

```css
.fx13 .t{font-family:"DotGothic16",monospace;font-weight:400;color:#fff}
.fx13 .t .r{color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #13
