# 215 · 價格方案切換 — Pricing Toggle

月付／年付切換時，各方案價格滾動更新，推薦方案突出

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、介面互動
- 風格／關鍵字 Style: 價格 方案 訂閱 月付 年付 定價表 Pricing Table Plans Toggle Monthly Yearly SaaS 卡片 群組
- 標籤 Tag: GSAP
- 範例文字 Example text: 「基本 專業 企業」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「價格方案切換（Pricing Toggle）」動態效果：價格方案頁上方有「月付／年付」切換膠囊，點擊時滑塊滑到另一側；三張方案卡片的價格數字從舊值滾動累加到新值（約 0.6 秒），單位同步改成「/月」或「/年」，每張卡片依序輕輕上浮再落下；中間的推薦方案預設放大並加上框線與「推薦」標籤。（GSAP：數字 tween 物件數值 + onUpdate 寫入；卡片 y 的 yoyo 用 delay 依索引錯開；切換膠囊用 CSS transform transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx215">`, preview text 「基本 專業 企業」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「價格方案切換」.

### JavaScript — `FX[215]` from `site/fx.js`

```js
215(s,x,card){const P=[[290,2900],[590,5900],[990,9900]],N=words(x);const w=el('div','kd-pr');w.innerHTML='<div class="kd-tg"><i></i><span class="on">月付</span><span>年付 <em>省 17%</em></span></div><div class="kd-pl"></div>';const pl=w.querySelector('.kd-pl'),tg=w.querySelector('.kd-tg');
  const cs=P.map((p,i)=>{const c=el('div','kd-pc'+(i===1?' hot':''));c.innerHTML=(i===1?'<small>推薦</small>':'')+'<b></b><div class="kd-pv">NT$<strong>'+p[0]+'</strong><span>/月</span></div><i></i><i class="s"></i>';c.querySelector('b').textContent=N[i%N.length];pl.append(c);return c});s.append(w);let yr=false,real=0;
  const set=y=>{yr=y;tg.classList.toggle('yr',y);tg.querySelectorAll('span').forEach((e,i)=>e.classList.toggle('on',i===(y?1:0)));cs.forEach((c,i)=>{const st=c.querySelector('strong'),o={v:+st.textContent};gsap.to(o,{v:P[i][y?1:0],duration:.6,ease:'power2.out',onUpdate:()=>st.textContent=Math.round(o.v)});c.querySelector('.kd-pv span').textContent=y?'/年':'/月';gsap.fromTo(c,{y:0},{y:-4,duration:.2,yoyo:true,repeat:1,delay:i*.06})})};
  tg.onclick=()=>{real=Date.now();set(!yr)};card._timers.push(setInterval(()=>{if(Date.now()-real>4000)set(!yr)},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx215` rules from `site/fx.css`

_No dedicated `.fx215` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #215
