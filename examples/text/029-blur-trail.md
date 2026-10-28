# 029 · 殘影疾走 — Blur Trail

拖著殘影疾馳而過

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 速度・疾走
- 範例文字 Example text: 「疾走」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「殘影疾走（Blur Trail）」動態效果：文字從畫面左外側高速衝進中央並帶斜體傾斜，短暫停住後再衝出右側，後方拖著 4 層半透明模糊的殘影，背景閃過橫向速度線。約 2.6 秒一輪，疾走感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx29">`, preview text 「疾走」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「殘影疾走」.

### JavaScript — `FX[29]` from `site/fx.js`

```js
29(s,x){s.append(el('div','lines'));const w=el('div','w');for(let k=4;k>=1;k--){const g=T(x,20);g.classList.add('g');g.style.setProperty('--op',(.5/k).toFixed(2));g.style.animation=`dash 2.6s ${-0.035*k}s infinite cubic-bezier(.7,0,.3,1)`;w.append(g)}w.append(T(x,20));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx29` rules from `site/fx.css`

```css
.fx29 .w{position:relative}
.fx29 .t{animation:dash 2.6s infinite cubic-bezier(.7,0,.3,1);color:#fff}
.fx29 .g{position:absolute;left:0;top:0;color:var(--a);filter:blur(3px);opacity:var(--op)}
.fx29 .lines{position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 9%,#ffffff10 9% 10%);animation:fl2 2.6s infinite}
@keyframes dash{0%{transform:translateX(-130cqw) skewX(-20deg)}45%{transform:translateX(0) skewX(-12deg)}55%{transform:translateX(0) skewX(0)}62%{transform:translateX(-2cqw)}100%{transform:translateX(140cqw) skewX(-20deg)}}
@keyframes fl2{0%,30%,60%,100%{opacity:0}40%,90%{opacity:1}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #29
