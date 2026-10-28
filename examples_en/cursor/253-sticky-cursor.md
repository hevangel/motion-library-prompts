# 253 · Sticky Cursor — 黏性游標

When the cursor approaches a button it is attracted to it, deforms to wrap the whole button, and the button is also pulled slightly

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: GSAP
- Uses: UI Interaction, Emphasis
- Style / keywords: Sticky Attraction Magnetic Deformation Wrap Navigation Sticky Cursor Magnetic Morph Nav Cursor Mouse
- Tag: GSAP
- Example text: "Work About Contact" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Sticky Cursor (黏性游標)" motion effect: A row of buttons in a navigation bar, with the cursor as a small circle: when the cursor approaches a button, the small circle is “sucked” over, deforms into a rounded rectangle that wraps the whole button, and its position still shifts slightly with the mouse inside the button; the button itself is also pulled slightly toward the mouse direction, and its text and background colors invert; when moving away from the button, the small circle shrinks back and the button bounces back to its original position. (GSAP: mousemove determines whether the cursor is within a button's range (with a little expansion), and if inside, tweens the cursor's x/y/width/height to the button's center and size + offset × 0.12, otherwise tweens back to a small circle; the button's x/y = offset × 0.15, power3.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx253">`, preview text "Work About Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Sticky Cursor".

### JavaScript — `FX[253]` from `site/fx.js`

```js
253(s,x,card){const l=el('div','abs gl cr-st');const row=el('div','cr-sr');const ws=words(x).slice(0,3);const bs=ws.map(t=>{const b=el('button','cr-sb');b.textContent=t;row.append(b);return b});const c=el('i','cr-sc');l.append(row,c);s.append(l);
  const st={x:0,y:0,w:16,h:16,r:8};let tg=st;
  vpointer(l,card,(px,py)=>{const r=l.getBoundingClientRect();let hit=null;bs.forEach(b=>{const q=b.getBoundingClientRect();const on=px>q.left-r.left-6&&px<q.right-r.left+6&&py>q.top-r.top-6&&py<q.bottom-r.top+6;b.classList.toggle('on',on);if(on)hit=q});
    if(hit){const bx=hit.left-r.left+hit.width/2,by=hit.top-r.top+hit.height/2;gsap.to(c,{x:bx+(px-bx)*.12,y:by+(py-by)*.12,width:hit.width+10,height:hit.height+10,borderRadius:99,duration:.35,ease:'power3.out',overwrite:'auto'});
      bs.forEach(b=>{if(b.classList.contains('on'))gsap.to(b,{x:(px-bx)*.15,y:(py-by)*.2,duration:.35,overwrite:'auto'});else gsap.to(b,{x:0,y:0,duration:.5,overwrite:'auto'})})}
    else{gsap.to(c,{x:px,y:py,width:16,height:16,borderRadius:99,duration:.25,ease:'power3.out',overwrite:'auto'});bs.forEach(b=>gsap.to(b,{x:0,y:0,duration:.5,overwrite:'auto'}))}});gsap.set(c,{xPercent:-50,yPercent:-50})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx253` rules from `site/fx.css`

_No dedicated `.fx253` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #253
