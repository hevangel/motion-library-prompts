# 272 · Scroll Flip Card — 捲動翻轉卡片

When scrolling down, a card flips in 3D to its back, while enlarging slightly

- Component: Cards · Groups (`card`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, UI Interaction
- Style / keywords: Flip Flip Over 3D Card Front and Back Scroll Scroll Flip Card 3D RotateY Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "Back Story" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Scroll Flip Card (捲動翻轉卡片)" motion effect: A card is located in the center of the screen, its front an image and its back text (the back uses an accent color): when the user scrolls down, the card flips in 3D along the vertical axis by 180 degrees according to scroll progress, while enlarging from 0.85 times to 1 times; halfway through scrolling it is exactly side-on to the viewer, and when scrolling is complete the back is fully displayed; scrolling back flips it back to the front. (GSAP ScrollTrigger scrub: the container is pinned or sticky, timeline fromTo rotationY 0 → 180; the parent sets perspective, the card transform-style: preserve-3d, both front and back faces backface-visibility: hidden, the back pre-rotated rotateY(180deg))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx272">`, preview text "Back Story". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Flip Card".

### JavaScript — `FX[272]` from `site/fx.js`

```js
272(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen','sx-pv');const c=el('div','sx-fc');c.innerHTML='<div class="f">'+mdImg(0)+'</div><div class="b"><b></b><small>捲動翻到背面</small></div>';c.querySelector('b').textContent=x;view.append(c);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).fromTo(c,{rotationY:0,scale:.85},{rotationY:180,scale:1,ease:'none'});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx272` rules from `site/fx.css`

_No dedicated `.fx272` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #272
