# 250 · 水滴單選 — Liquid Radio

切換單選項時，選中的圓點被拉長成水滴滑到新選項，再彈回圓形

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 單選 radio 選項 水滴 液態 拉伸 Liquid Radio Button Gooey Morph 表單 控制項
- 標籤 Tag: GSAP elastic
- 範例文字 Example text: 「標準寄送 快速到貨 門市自取」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「水滴單選（Liquid Radio）」動態效果：一組直向排列的單選項，被選中的圓點是一顆獨立的實心小圓：切換選項時，小圓先被拉長成上下延伸的水滴形，沿直線滑到新選項的圓圈中心，抵達後以彈性晃動恢復成圓形，像液體一樣流過去；被選中的外圈同時改變樣式。（GSAP timeline：先 scaleY 2.2 / scaleX 0.7，同時 tween y 到新位置 power3.inOut，最後 scaleX/scaleY 回 1 用 elastic.out(1.2,0.5)；原生 radio 隱藏但保留鍵盤操作）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx250">`, preview text 「標準寄送 快速到貨 門市自取」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「水滴單選」.

### JavaScript — `FX[250]` from `site/fx.js`

```js
250(s,x,card){const ws=words(x).slice(0,3);const w=el('div','fm-rd');w.innerHTML='<i class="fm-dot"></i>';const ls=ws.map((t,i)=>{const l=el('label');l.innerHTML='<input type="radio" name="r'+Math.random().toString(36).slice(2)+'"><i></i><span></span>';l.querySelector('span').textContent=t;w.append(l);return l});
  const nm='fm'+Math.random().toString(36).slice(2);ls.forEach(l=>l.querySelector('input').name=nm);s.append(w);const dot=w.querySelector('.fm-dot');let cur=-1,real=0;
  const go=(i,instant)=>{if(i===cur)return;const r=ls[i].querySelector('i'),wr=w.getBoundingClientRect(),rr=r.getBoundingClientRect(),y=rr.top-wr.top+rr.height/2;ls[i].querySelector('input').checked=true;
    if(instant||cur<0)gsap.set(dot,{y,x:rr.left-wr.left+rr.width/2});else gsap.timeline().to(dot,{scaleY:2.2,scaleX:.7,duration:.15,ease:'power1.in'}).to(dot,{y,duration:.35,ease:'power3.inOut'},0).to(dot,{scaleY:1,scaleX:1,duration:.4,ease:'elastic.out(1.2,.5)'},.3);cur=i};
  ls.forEach((l,i)=>l.querySelector('input').addEventListener('change',()=>{real=Date.now();go(i)}));requestAnimationFrame(()=>go(0,true));
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go((cur+1)%ls.length)},1400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx250` rules from `site/fx.css`

_No dedicated `.fx250` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #250
