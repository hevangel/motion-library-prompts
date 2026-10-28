# 210 · Split Screen Scroll — 左右分割捲動

The text on the right scrolls down, while the fixed image on the left switches to match the corresponding section

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Headline · Hero
- Style / keywords: Split Screen Left Right Two Columns Fixed Image Switch Storytelling Split Screen Sticky Image Scrollytelling Layout Page Web Structure
- Tag: Sticky · ScrollTrigger
- Example text: "Morning Afternoon Night" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Split Screen Scroll (左右分割捲動)" motion effect: The screen is split into left and right columns: the left column is a fixed (sticky) large-image area, and the right column is text chapters that can be scrolled section by section; whenever a chapter on the right scrolls to the middle of the screen, the image on the left cross-fades into the image for the corresponding chapter and shrinks back from a slightly enlarged state to its original size, creating a synchronized image-and-text storytelling experience. (CSS position:sticky + GSAP ScrollTrigger: each chapter has start "top 55%" and end "bottom 55%", and onToggle switches the active class of the corresponding image on the left; images use transitions on opacity and scale)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx210">`, preview text "Morning Afternoon Night". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Split Screen Scroll".

### JavaScript — `FX[210]` from `site/fx.js`

```js
210(s,x){const ws=words(x).slice(0,3);const sc=el('div','scr nopad ly-sp');const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0']];
  sc.innerHTML='<div class="ly-sl"><div class="ly-si"></div></div><div class="ly-sr"></div>';const si=sc.querySelector('.ly-si'),sr=sc.querySelector('.ly-sr');const ims=P.map((p,i)=>{const d=el('div','ly-im'+(i?'':' on'));d.innerHTML=scene(...p);si.append(d);return d});
  ws.forEach((v,i)=>{const sec=el('section');sec.innerHTML=`<small>0${i+1}</small><b></b><i class="ly-bl"></i><i class="ly-bl s"></i>`;sec.querySelector('b').textContent=v;sr.append(sec);ScrollTrigger.create({trigger:sec,scroller:sc,start:'top 55%',end:'bottom 55%',onToggle:t=>{if(t.isActive)ims.forEach((m,j)=>m.classList.toggle('on',j===i))}})});s.append(sc);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx210` rules from `site/fx.css`

_No dedicated `.fx210` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #210
