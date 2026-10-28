# 273 · Scroll Rotating Cube — 捲動旋轉立方體

A 3D cube rotates with scrolling, each face written with a different keyword

- Component: Shapes · SVG (`shape`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Headline · Hero
- Style / keywords: Cube 3D Rotation Block cube Scroll Scroll Rotate Cube Faces Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "Design Develop Motion Brand Strategy Test" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Scroll Rotating Cube (捲動旋轉立方體)" motion effect: In the center of the screen is a 3D cube, its six faces each written with a keyword and using a different theme color: as the user scrolls down, the cube tilts slightly down (rotateX −20 degrees) and rotates around the vertical axis, turning 270 degrees according to scroll progress so each face turns in sequence to face front. (GSAP ScrollTrigger scrub: the cube has transform-style: preserve-3d, its six faces are composed with rotateY / rotateX ± 90 degrees plus translateZ(half the side length); scrolling tweens rotationY)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx273">`, preview text "Design Develop Motion Brand Strategy Test". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Rotating Cube".

### JavaScript — `FX[273]` from `site/fx.js`

```js
273(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen','sx-pv');const ws=words(x);const c=el('div','sx-cb');['f','r','b','l','t','d'].forEach((k,i)=>{const f=el('div','sx-cf '+k);f.textContent=ws[i%ws.length];f.style.background=i%2?'var(--a)':GC[i%5];c.append(f)});view.append(c);
  gsap.fromTo(c,{rotationX:-20,rotationY:0},{rotationX:-20,rotationY:-270,ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx273` rules from `site/fx.css`

_No dedicated `.fx273` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #273
