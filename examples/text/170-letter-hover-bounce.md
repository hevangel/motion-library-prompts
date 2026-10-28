# 170 · 逐字跳動 — Letter Hover Bounce

滑過文字時，碰到的每個字各自彈跳一下

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 文字 逐字 跳動 彈跳 俏皮 letter bounce hover playful hover 懸停 滑鼠移入 滑過 互動
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「HOVER ME 試試看」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「逐字跳動（Letter Hover Bounce）」動態效果：標題文字拆成一個個字，游標滑過哪個字，那個字就往上彈跳一下並短暫變成強調色（約 0.5 秒、彈性），游標快速橫掃時會形成一串波浪；每個字的動畫各自獨立，結束後回到原位。（做法：每個字包 inline-block 的 span，pointerenter 時移除再加上動畫 class 以重播，animationend 時移除；keyframes 在 30% 時 translateY(-35%) scale(1.12)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx170">`, preview text 「HOVER ME 試試看」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「逐字跳動」.

### JavaScript — `FX[170]` from `site/fx.js`

```js
170(s,x,card){x=x.replace(/ /g,'\u00a0');const t=split(x,Math.min(11,70/chars(x).length));t.classList.add('lw');s.append(t);const cs=[...t.querySelectorAll('.c')];
  const jump=c=>{c.classList.remove('j');void c.offsetWidth;c.classList.add('j')};cs.forEach(c=>{c.addEventListener('pointerenter',()=>jump(c));c.addEventListener('animationend',()=>c.classList.remove('j'))});
  let real=false;t.addEventListener('pointerenter',()=>real=true);t.addEventListener('pointerleave',()=>real=false);card._timers.push(setInterval(()=>{if(!real)cs.forEach((c,i)=>setTimeout(()=>jump(c),i*60))},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx170` rules from `site/fx.css`

_No dedicated `.fx170` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #170
