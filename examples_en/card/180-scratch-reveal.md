# 180 · Scratch Reveal — 刮刮樂揭示

Use the cursor or a finger to scratch off the surface layer and reveal the content underneath

- Component: Cards · Groups (`card`)
- Timing: Drag Gesture
- Tech: Canvas
- Uses: UI Interaction, Emphasis, App Interface
- Style / keywords: scratch card scratch off reveal prize draw coupon gamification Scratch Card Reveal Lottery Coupon Gamification Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas erase
- Example text: "Free Shipping Coupon" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Scratch Reveal (刮刮樂揭示)" motion effect: The card is covered with a surface layer with a metallic gradient texture and the words 'scratch to see'. Wherever the user holds down the mouse or drags a finger, it is scratched away (a thick brush with a round tip), revealing the prize or offer content underneath; when the scratched area exceeds about half, the remaining surface layer automatically fades out for a full reveal. Suitable for prize draws, coupons and event pages. (Canvas 2D: the surface layer is drawn on a canvas, while dragging use globalCompositeOperation = "destination-out" to draw lines along the path and erase; periodically sample the transparent proportion of getImageData to judge whether to reveal; set touch-action:none on mobile)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx180">`, preview text "Free Shipping Coupon". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scratch Reveal".

### JavaScript — `FX[180]` from `site/fx.js`

```js
180(s,x,card){const pr=el('div','scp');pr.innerHTML='<small>恭喜你</small><b></b>';pr.querySelector('b').textContent=x;s.append(pr);let real=0;
  const cv=cfx(s,card,{init:(c,W,H)=>{cover(c,W,H);return{lx:null,ly:null,cnt:0}},
    frame:(c,W,H,t,dt,m,o)=>{let px,py,on=false;if(m.down){px=m.x;py=m.y;on=true;real=Date.now()}else if(Date.now()-real>4000){const p=(t%7)/7;if(p<.7){const q=p/.7;px=W*(.12+.76*((q*5)%1));py=H*(.2+.6*q);on=true;if((q*5)%1<.04)o.lx=null}
        else if(p<.72){cv.style.opacity=0}else if(p>.95&&cv.style.opacity==='0'){cover(c,W,H);cv.style.opacity=1;o.lx=null}}
      if(on){c.globalCompositeOperation='destination-out';c.lineCap='round';c.lineWidth=W*.08;c.beginPath();c.moveTo(o.lx??px,o.ly??py);c.lineTo(px,py);c.stroke();c.globalCompositeOperation='source-over';o.lx=px;o.ly=py}else{o.lx=null;o.ly=null}
      if(m.down&&++o.cnt%20===0){const d=c.getImageData(0,0,c.canvas.width,c.canvas.height).data;let a=0,n=0;for(let i=3;i<d.length;i+=400){n++;if(d[i]>0)a++}if(a/n<.45){cv.style.opacity=0;setTimeout(()=>{cover(c,W,H);cv.style.opacity=1},2200)}}}});
  cv.classList.add('scr2');
  function cover(c,W,H){c.globalCompositeOperation='source-over';const g=c.createLinearGradient(0,0,W,H);g.addColorStop(0,'#b9bcc6');g.addColorStop(.5,'#e6e8ee');g.addColorStop(1,'#9fa3ad');c.fillStyle=g;c.fillRect(0,0,W,H);
    c.fillStyle='rgba(0,0,0,.35)';c.font=`800 ${W*.045}px "Noto Sans JP",sans-serif`;c.textAlign='center';c.textBaseline='middle';c.fillText('刮開看看 ✦',W/2,H/2)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx180` rules from `site/fx.css`

_No dedicated `.fx180` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #180
