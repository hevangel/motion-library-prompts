# 215 · Pricing Toggle — 價格方案切換

When switching between monthly and yearly payment, each plan's price rolls to update, and the recommended plan stands out

- Component: Cards · Groups (`card`)
- Timing: Switch
- Tech: GSAP
- Uses: Numbers & Data, UI Interaction
- Style / keywords: Price Plans Subscription Monthly Yearly Pricing Table Pricing Table Plans Toggle Monthly Yearly SaaS Cards Group
- Tag: GSAP
- Example text: "Basic Professional Enterprise" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Pricing Toggle (價格方案切換)" motion effect: At the top of a pricing page there is a "Monthly / Yearly" toggle capsule; when clicked, the slider slides to the other side; the price numbers on the three plan cards roll and accumulate from the old value to the new value (about 0.6 seconds), the unit changes to "/month" or "/year" in sync, and each card gently floats up and settles back down in sequence; the recommended plan in the middle is enlarged by default and given a border and a "Recommended" label. (GSAP: tween a numeric object value and write it in onUpdate; stagger the cards' y yoyo with a delay based on index; the toggle capsule uses a CSS transform transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx215">`, preview text "Basic Professional Enterprise". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Pricing Toggle".

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
