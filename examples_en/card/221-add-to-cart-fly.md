# 221 · Add to Cart Fly — 加入購物車飛入

Click add to cart, and the product thumbnail flies in an arc into the cart while the count jumps

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction, App Interface, Emphasis
- Style / keywords: Cart Add E-commerce Fly In Parabola Feedback Add To Cart Fly Ecommerce Shop Feedback Cards Group
- Tag: GSAP arc
- Example text: "Handmade Ceramic Cup" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Add to Cart Fly (加入購物車飛入)" motion effect: When the "Add to Cart" button on a product card is pressed, the button gives a light press feedback, a copy of the product thumbnail flies along a parabolic arc to the cart icon at the top right, gradually shrinking during flight; on arrival the cart bounces and enlarges once, and the count badge in the corner increments by 1 and pops out. About 0.75 seconds, giving the user clear "added" feedback. (GSAP: tween the flying element's x with power1.in and y with back.in separately to form an arc, while scaling from 1 to 0.15; on completion remove the element and update the badge, with the badge scale using back.out(3))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx221">`, preview text "Handmade Ceramic Cup". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Add to Cart Fly".

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
