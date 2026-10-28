# 156 · Hide Header on Scroll — 往下捲隱藏導覽列

The navigation bar hides when scrolling down and slides out immediately when scrolling back up

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: UI Interaction, Scroll Effects, App Interface
- Style / keywords: Navigation Bar Header Menu header navbar Hide Show Direction Headroom Hide On Scroll Down Show On Scroll Up Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger direction
- Example text: "LOGO" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Hide Header on Scroll (往下捲隱藏導覽列)" motion effect: The header navigation bar is fixed at the top; when the user scrolls down (reading content), the navigation bar slides up out of the screen to make room; as soon as they scroll up (looking for the menu), it immediately slides back in from the top, and it is always shown at the very top; about 0.35 seconds, decelerating. Very common on mobile. (How to: compare the current and previous scrollY to judge direction, or use ScrollTrigger's self.direction; toggle a class so the header uses translateY(-100%), with a transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx156">`, preview text "LOGO". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hide Header on Scroll".

### JavaScript — `FX[156]` from `site/fx.js`

```js
156(s,x){const sc=el('div','scr nopad');const h=el('header','hh');h.innerHTML='<b></b><nav><i></i><i></i><i></i></nav>';h.querySelector('b').textContent=x;const c=el('div','shc');for(let i=0;i<10;i++)c.append(el('i'));sc.append(h,c);s.append(sc);
  ScrollTrigger.create({scroller:sc,start:0,end:'max',onUpdate:t=>h.classList.toggle('hide',t.direction===1&&t.scroll()>30)});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx156` rules from `site/fx.css`

_No dedicated `.fx156` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #156
