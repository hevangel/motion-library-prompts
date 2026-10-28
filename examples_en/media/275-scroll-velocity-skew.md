# 275 · Scroll Velocity Skew — 捲動速度傾斜

An image list skews with speed when scrolling fast, and returns to straight when it stops

- Component: Images · Media (`media`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, UI Interaction
- Style / keywords: Tilt Skew Velocity Inertia skew Scroll Scroll Velocity Skew Images List Scroll Trigger ScrollTrigger
- Tag: getVelocity
- Example text: "Mountain Sea City Forest" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Scroll Velocity Skew (捲動速度傾斜)" motion effect: A scrollable row of image cards, normally arranged neatly; when the user scrolls quickly, all cards skew vertically (skewY) according to scroll speed, the faster the scroll the more the skew, the direction following the scroll direction, up to about 12 degrees; when scrolling slows or stops it smoothly returns to straight, bringing out inertia and a sense of speed. (GSAP: in ScrollTrigger.create's onUpdate, get self.getVelocity(), convert it to an angle and clamp it, and use gsap.quickTo(element, "skewY", {duration: .5, ease: "power3.out"}) to set it smoothly)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx275">`, preview text "Mountain Sea City Forest". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Velocity Skew".

### JavaScript — `FX[275]` from `site/fx.js`

```js
275(s,x){const sc=el('div','scr nopad');const ls=el('div','sx-sk');words(x).concat(words(x)).slice(0,8).forEach((t,i)=>{const r=el('div','sx-sr');r.innerHTML=mdImg(i)+'<b></b>';r.querySelector('b').textContent=t;ls.append(r)});sc.append(ls);s.append(sc);
  const rows=[...ls.children],set=gsap.quickTo(rows,'skewY',{duration:.5,ease:'power3.out'});let last=0,lt=0;
  ScrollTrigger.create({scroller:sc,trigger:ls,start:'top top',end:'bottom bottom',onUpdate:self=>{const v=self.getVelocity();set(gsap.utils.clamp(-12,12,v/-90))}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx275` rules from `site/fx.css`

_No dedicated `.fx275` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #275
