# 299 · Echo Stack — 殘影堆疊

Several hollow copies are stacked behind the text, unfolding diagonally backward in sequence, then drawing back in

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: Afterimage Stacking Copies Hollow 3D Echo Echo Stack Outline Layers Repeat Text Text Heading Animated Text
- Tag: CSS keyframes
- Example text: "ECHO" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Echo Stack (殘影堆疊)" motion effect: A bold large heading, behind which 5 layers of hollow outlined copies of the same text are stacked, each layer's outline fainter the farther back it goes; during the animation these copy layers unfold in sequence (each layer delayed by about 0.06 seconds) diagonally up and to the right, forming an afterimage like an echo or a 3D staircase, linger for a moment, then draw back in to overlap the original text, looping back and forth. (CSS: multiple spans stacked in the same grid cell, using the CSS variable --i to compute the translate distance, outline opacity and animation-delay; -webkit-text-stroke creates the hollow text)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx299">`, preview text "ECHO". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Echo Stack".

### JavaScript — `FX[299]` from `site/fx.js`

```js
299(s,x){const w=el('div','tx-ec');w.style.fontSize=Math.min(14,60/chars(x).length)+'cqw';for(let i=0;i<6;i++){const d=el('span');d.textContent=x;d.style.setProperty('--i',i);w.append(d)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx299` rules from `site/fx.css`

_No dedicated `.fx299` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #299
