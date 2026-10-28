# 011 · 文字雨 — Letter Rain

文字如雨般落下

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 奇幻・背景
- 範例文字 Example text: 「あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろ」（預覽底色：cream，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字雨（Letter Rain）」動態效果：整個區塊背景布滿直排的假名文字，像雨一樣由上往下不斷落下，每一行速度不同（約 3–5 秒落完），少數幾行用強調色，其餘用低對比色調，奇幻背景感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx11">`, preview text 「あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろ」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字雨」.

### JavaScript — `FX[11]` from `site/fx.js`

```js
11(s,x){s.classList.add('fx11');const pool=chars(x);for(let i=0;i<13;i++){const c=el('div','col'+(Math.random()<.25?' a':''));let str='';for(let j=0;j<12;j++)str+=pool[Math.floor(Math.random()*pool.length)];c.textContent=str;c.style.left=(i*7.8+1)+'%';const d=rnd(2.8,5.5);c.style.animationDuration=d+'s';c.style.animationDelay=-rnd(0,d)+'s';s.append(c)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx11` rules from `site/fx.css`

```css
.fx11 .col{position:absolute;top:0;writing-mode:vertical-rl;font-weight:700;font-size:5.4cqw;line-height:1.1;letter-spacing:.1em;animation:rain linear infinite;color:#222}
.fx11 .col.a{color:var(--a)}
.fx11{container-type:size}
@keyframes rain{from{transform:translateY(-100%)}to{transform:translateY(110cqh)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #11
