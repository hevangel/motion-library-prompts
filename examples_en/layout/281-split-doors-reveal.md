# 281 · Split Doors Reveal — 對開門轉場

The whole screen is cut down the middle into left and right doors that pull open to the sides with scrolling, revealing the next section

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Transitions
- Style / keywords: Double Doors Opening Pull Open Split Transition Reveal Split Doors Curtain Reveal Scroll Transition Scroll Trigger ScrollTrigger
- Tag: ScrollTrigger
- Example text: "Welcome" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Split Doors Reveal (對開門轉場)" motion effect: A transition between two sections of content: the previous section is a full screen of an accent color, with a huge character in the middle; when the user scrolls down, this screen is cut vertically from the exact center into left and right doors (the big character is also cut in half along with it), and the two doors slide open to the left and right sides according to scroll progress, revealing the next section behind, while the next section simultaneously enlarges from 0.8 times and becomes clear. (GSAP ScrollTrigger scrub: two blocks each 50% wide with overflow: hidden on the left and right, inside each placing one copy of the same big character at 200% width (the left aligned left, the right aligned right) so it looks like the same character; the timeline moves the two doors to xPercent −100 / 100)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx281">`, preview text "Welcome". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Split Doors Reveal".

### JavaScript — `FX[281]` from `site/fx.js`

```js
281(s,x){const{sc,wrap,view}=scrollBox(s);const nx=el('div','abs gl sx-cn');nx.append(T(x,Math.min(11,50/chars(x).length)));const L=el('div','sx-ct l'),R=el('div','sx-ct r');L.innerHTML=R.innerHTML='<b>SCROLL</b>';view.append(nx,L,R);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).to(L,{xPercent:-100,ease:'power2.inOut'},.15).to(R,{xPercent:100,ease:'power2.inOut'},.15).fromTo(nx,{scale:.8,opacity:.2},{scale:1,opacity:1,ease:'power2.out'},.15);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx281` rules from `site/fx.css`

_No dedicated `.fx281` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #281
