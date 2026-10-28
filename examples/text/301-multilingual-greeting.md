# 301 · 多語問候切換 — Multilingual Greeting

不同語言的「你好」輪流出現，模糊淡入淡出，外框寬度平滑跟著變

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換、循環待機
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 多語 問候 你好 Hello 切換 國際 Multilingual Greeting Hello Languages Rotate 文字 標題 動態文字
- 標籤 Tag: GSAP
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「多語問候切換（Multilingual Greeting）」動態效果：Hero 標題位置輪流顯示不同語言的「你好」（Hello、你好、こんにちは、Bonjour、Hola、안녕하세요、Ciao），每隔約 1.6 秒切換：舊的詞往上模糊淡出，新的詞從下方模糊淡入變清楚；因為每個詞長度不同，包住文字的容器寬度會平滑地縮放到新詞的寬度，讓後面跟著的小圓點也平滑移動，而不是瞬間跳動。（GSAP：先量出新詞的寬度（隱藏的量測元素），容器 width tween 到新寬度 power3.inOut；文字 opacity、filter:blur、y 做淡出淡入）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx301">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「多語問候切換」.

### JavaScript — `FX[301]` from `site/fx.js`

```js
301(s,x){const G=['Hello','你好','こんにちは','Bonjour','Hola','안녕하세요','Ciao'];const w=el('div','tx-ml');w.innerHTML='<span class="tx-mw"><b></b></span><i class="tx-dot"></i>';const box=w.querySelector('.tx-mw'),b=box.querySelector('b');s.append(w);let k=0;
  const ms=el('span','tx-me');w.append(ms);const meas=t=>{ms.textContent=t;return ms.offsetWidth};
  const go=()=>{const t=G[k++%G.length];const wd=meas(t);gsap.timeline().to(b,{opacity:0,filter:'blur(8px)',y:'-.3em',duration:.3,ease:'power2.in'}).add(()=>{b.textContent=t}).to(box,{width:wd,duration:.45,ease:'power3.inOut'},'<').fromTo(b,{opacity:0,filter:'blur(8px)',y:'.3em'},{opacity:1,filter:'blur(0px)',y:0,duration:.4,ease:'power2.out'})};
  b.textContent=G[0];requestAnimationFrame(()=>{box.style.width=meas(G[0])+'px';k=1});gsap.timeline({repeat:-1}).add(go,1.4).add(()=>{},1.6)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx301` rules from `site/fx.css`

_No dedicated `.fx301` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #301
