# 218 · 評論輪播 — Testimonial Slider

引言淡出上移換下一則，頭像跟著切換，進度條計時

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換、循環待機
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 評論 推薦 客戶見證 輪播 引言 Testimonial Review Quote Slider Carousel 卡片 群組
- 標籤 Tag: GSAP
- 範例文字 Example text: 「王小姐 陳先生 林設計師」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「評論輪播（Testimonial Slider）」動態效果：客戶評價輪播：中間是一大段引言與署名，下方一排圓形頭像與一條進度條；每隔約 2.6 秒，目前的引言往上淡出、下一則從下方淡入上滑，對應的頭像放大並加上外框、其他頭像縮小變淡，進度條從 0 重新填滿計時；點擊頭像可直接切換到那則。（GSAP：新舊引言各自 tween y 與 opacity；進度條 scaleX 0→1、ease none，duration 與自動切換間隔相同）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx218">`, preview text 「王小姐 陳先生 林設計師」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「評論輪播」.

### JavaScript — `FX[218]` from `site/fx.js`

```js
218(s,x,card){const Q=['用了之後，整個團隊的溝通效率都提升了。','介面直覺又好看，客戶一看就懂。','終於找到一個不用教就會用的工具！'];const ws=words(x);const w=el('div','kd-ts');w.innerHTML='<div class="kd-q"></div><div class="kd-av"></div><div class="kd-pb"><i></i></div>';const q=w.querySelector('.kd-q'),av=w.querySelector('.kd-av'),pb=w.querySelector('.kd-pb i');
  const as=Q.map((_,i)=>{const a=el('button','kd-a');a.style.background=GC[i+1];a.setAttribute('aria-label',ws[i%ws.length]);av.append(a);return a});s.append(w);let cur=-1,real=0;
  const go=i=>{cur=i;const old=q.firstChild;const n=el('div','kd-qi');n.innerHTML='<p></p><b></b>';n.querySelector('p').textContent='「'+Q[i]+'」';n.querySelector('b').textContent='— '+ws[i%ws.length];q.append(n);if(old)gsap.to(old,{y:-14,opacity:0,duration:.35,onComplete:()=>old.remove()});gsap.fromTo(n,{y:14,opacity:0},{y:0,opacity:1,duration:.5,delay:.15,ease:'power3.out'});as.forEach((a,j)=>a.classList.toggle('on',j===i));gsap.fromTo(pb,{scaleX:0},{scaleX:1,duration:2.6,ease:'none',overwrite:true})};
  as.forEach((a,i)=>a.onclick=()=>{real=Date.now();go(i)});go(0);card._timers.push(setInterval(()=>{if(Date.now()-real>4000)go((cur+1)%Q.length)},2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx218` rules from `site/fx.css`

_No dedicated `.fx218` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #218
