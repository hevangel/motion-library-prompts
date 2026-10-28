# 221 · 加入購物車飛入 — Add to Cart Fly

點加入購物車，商品縮圖以弧線飛進購物車，數字跳一下

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面、強調重點
- 風格／關鍵字 Style: 購物車 加入 電商 飛入 拋物線 回饋 Add To Cart Fly Ecommerce Shop Feedback 卡片 群組
- 標籤 Tag: GSAP arc
- 範例文字 Example text: 「手工陶杯」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「加入購物車飛入（Add to Cart Fly）」動態效果：商品卡片按下「加入購物車」時，按鈕輕按回饋，商品縮圖複製一份並沿著拋物線弧線飛向右上角的購物車圖示，飛行中逐漸縮小，抵達時購物車彈跳放大一下，角落的數量徽章 +1 並彈出。約 0.75 秒，給使用者明確的「已加入」回饋。（GSAP：飛行元素的 x 用 power1.in、y 用 back.in 分開 tween 形成弧線，同時 scale 1→0.15；完成後移除元素並更新徽章，徽章 scale 用 back.out(3)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx221">`, preview text 「手工陶杯」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「加入購物車飛入」.

### JavaScript — `FX[221]` from `site/fx.js`

```js
221(s,x,card){const w=el('div','kd-shop');w.innerHTML='<div class="kd-cart"><svg viewBox="0 0 24 24"><path d="M3 4h2l2.4 11h10.8L21 7H7"/><circle cx="9.5" cy="19.5" r="1.4"/><circle cx="17" cy="19.5" r="1.4"/></svg><em>0</em></div><div class="kd-prd"><i class="kd-img"></i><b></b><span>NT$ 1,280</span><button>加入購物車</button></div>';w.querySelector('.kd-prd b').textContent=x;s.append(w);
  const cart=w.querySelector('.kd-cart'),badge=cart.querySelector('em'),img=w.querySelector('.kd-img'),bt=w.querySelector('button');let n=0,real=0;
  const add=()=>{const wr=w.getBoundingClientRect(),ir=img.getBoundingClientRect(),cr=cart.getBoundingClientRect();const d=el('i','kd-fly');d.style.background=getComputedStyle(img).background;w.append(d);const sx=ir.left-wr.left+ir.width/2,sy=ir.top-wr.top+ir.height/2,ex=cr.left-wr.left+cr.width/2,ey=cr.top-wr.top+cr.height/2;
    gsap.set(d,{x:sx,y:sy,xPercent:-50,yPercent:-50,scale:1});gsap.to(d,{x:ex,duration:.75,ease:'power1.in'});gsap.to(d,{y:ey,duration:.75,ease:'back.in(2.2)'});gsap.to(d,{scale:.15,duration:.75,ease:'power2.in',onComplete:()=>{d.remove();badge.textContent=++n;gsap.fromTo(cart,{scale:1},{scale:1.25,duration:.15,yoyo:true,repeat:1});gsap.fromTo(badge,{scale:.4},{scale:1,duration:.4,ease:'back.out(3)'})}});
    gsap.fromTo(bt,{scale:1},{scale:.92,duration:.1,yoyo:true,repeat:1})};
  bt.onclick=()=>{real=Date.now();add()};card._timers.push(setInterval(()=>{if(Date.now()-real>4000)add()},2400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx221` rules from `site/fx.css`

_No dedicated `.fx221` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #221
