# 158 · Image Parallax in Frame — 圖框內視差

An image moves inside its frame more slowly than the scroll, creating depth

- Component: Images · Media (`media`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Headline · Hero
- Style / keywords: Image Parallax Frame Photo Depth Image Parallax Frame Inner Parallax Gallery Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger scrub
- Example text: "Morning Afternoon Night" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Image Parallax in Frame (圖框內視差)" motion effect: A column of images arranged top to bottom, each image in a fixed frame that crops the overflow, with the image itself somewhat taller than the frame; when scrolling, the image displaces in reverse inside the frame at a slower speed (from about +12% to −12%), looking like scenery outside a window and giving more depth than scrolling as one whole block; there is a short caption below each image. (GSAP: the frame has overflow:hidden, the inner image is about 128% tall; each image gets its own ScrollTrigger, start "top bottom", end "bottom top", scrubbing yPercent -12→12)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx158">`, preview text "Morning Afternoon Night". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Image Parallax in Frame".

### JavaScript — `FX[158]` from `site/fx.js`

```js
158(s,x){const sc=el('div','scr');const ws=words(x);const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0']];
  sc.innerHTML='<div class="pxs"></div>';const box=sc.firstChild;P.forEach((c,i)=>{const fr=el('figure','pxf');fr.innerHTML=`<div class="pxi">${scene(...c)}</div><figcaption></figcaption>`;fr.querySelector('figcaption').textContent=ws[i%ws.length];box.append(fr)});s.append(sc);
  box.querySelectorAll('.pxf').forEach(fr=>gsap.fromTo(fr.querySelector('.pxi'),{yPercent:-12},{yPercent:12,ease:'none',scrollTrigger:{trigger:fr,scroller:sc,start:'top bottom',end:'bottom top',scrub:true}}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx158` rules from `site/fx.css`

_No dedicated `.fx158` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #158
