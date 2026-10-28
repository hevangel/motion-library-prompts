# 241 · 紙飛機送出 — Send Plane Button

按下送出，紙飛機從按鈕飛走，文字換成「已送出」再恢復

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 送出 紙飛機 寄出 訊息 表單 成功 Send Paper Plane Submit Button Success 按鈕
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「送出訊息」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「紙飛機送出（Send Plane Button）」動態效果：送出按鈕左側有一個紙飛機圖示：按下時按鈕先輕壓回彈，文字往右淡出，紙飛機先往後蓄力再往右上方加速飛出按鈕並消失；接著文字換成「已送出」從左滑入；約 1 秒後文字換回原本內容，紙飛機從左下方飛回原位。（GSAP timeline：按鈕 scale 0.94→1、文字 x 與 opacity、紙飛機 keyframes 往右上 x/y/rotation 以 power2.in 加速，再用 add() 切換文字內容；按鈕 overflow:hidden 讓飛機飛出時被裁切）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx241">`, preview text 「送出訊息」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「紙飛機送出」.

### JavaScript — `FX[241]` from `site/fx.js`

```js
241(s,x,card){const b=bxBtn('bx-sd',x);b.insertAdjacentHTML('afterbegin','<svg class="bx-pl" viewBox="0 0 24 24"><path d="M3 11l18-8-7 18-3-7z M11 14l10-11"/></svg>');s.append(b);const lb=b.querySelector('span'),pl=b.querySelector('.bx-pl');let busy=false;
  const go=()=>{if(busy)return;busy=true;const tl=gsap.timeline({onComplete:()=>busy=false});
    tl.to(b,{scale:.94,duration:.1}).to(b,{scale:1,duration:.3,ease:'back.out(3)'}).to(lb,{x:'1.2em',opacity:0,duration:.25},'<')
      .to(pl,{x:'-.3em',rotation:-15,duration:.2},'<').to(pl,{keyframes:[{x:'4em',y:'-1.4em',rotation:20,duration:.35,ease:'power2.in'},{opacity:0,duration:.05}]})
      .add(()=>lb.textContent='已送出').fromTo(lb,{x:'-1em',opacity:0},{x:0,opacity:1,duration:.3,ease:'back.out(2)'}).set(pl,{x:'-3em',y:'1em',rotation:0,opacity:0})
      .add(()=>{},'+=1.1').to(lb,{opacity:0,duration:.2}).add(()=>lb.textContent=x).to(lb,{opacity:1,duration:.2}).to(pl,{x:0,y:0,opacity:1,duration:.4,ease:'power3.out'},'<')};
  b.addEventListener('click',go);bxDemo(b,card,go,3600)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx241` rules from `site/fx.css`

_No dedicated `.fx241` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #241
