# 161 · Circle Reveal Transition — 圓形擴張轉場

When scrolling, a circular mask expands from the center, revealing the next chapter

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered, Switch
- Tech: GSAP
- Uses: Transitions, Scroll Effects
- Style / keywords: Transition Circle Mask Expand Reveal Section Circle Reveal Clip Path Transition Section Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: clip-path scrub
- Example text: "Chapter Two" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Circle Reveal Transition (圓形擴張轉場)" motion effect: A transition between two sections: when scrolling, the next section appears from the center of the screen through a circular mask; the circle expands with scroll progress from 0 until it covers the whole screen, while the previous section's heading slowly shrinks and fades and the next section's heading scales back from 1.2x to its original size; scrolling back shrinks the circle back. (GSAP: a timeline bound to ScrollTrigger scrub, with the section pinned or sticky; tween clipPath "circle(0% at 50% 50%)" → "circle(75% at 50% 50%)")
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx161">`, preview text "Chapter Two". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Circle Reveal Transition".

### JavaScript — `FX[161]` from `site/fx.js`

```js
161(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('crv');view.innerHTML='<div class="c1"></div><div class="c2"></div>';const a=T('第一章',12),b=T(x,Math.min(12,56/chars(x).length));view.firstChild.append(a);view.lastChild.append(b);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:true}}).fromTo(view.lastChild,{clipPath:'circle(0% at 50% 50%)'},{clipPath:'circle(75% at 50% 50%)',ease:'none'},0).fromTo(a,{scale:1,opacity:1},{scale:.8,opacity:.3,ease:'none'},0).fromTo(b,{scale:1.2},{scale:1,ease:'none'},0);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx161` rules from `site/fx.css`

_No dedicated `.fx161` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #161
