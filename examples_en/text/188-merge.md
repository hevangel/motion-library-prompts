# 188 · Merge — 合併

The top and bottom halves of the text slide in from the left and right respectively, merging into complete characters

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Transitions
- Style / keywords: merge join top and bottom cut in half left and right slide in Merge Split Halves Join Canva style Canva Merge merge presentation social post animation
- Tag: clip-path
- Example text: "Become One" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Merge (合併)" motion effect: A title is cut horizontally into top and bottom halves: the top half slides in and fades in from the left, the bottom half from the right at the same time, precisely aligning in the middle to form the complete text (about 0.9 seconds, strong ease-out), then fades out after a pause. (CSS: the same text is placed twice, using clip-path:inset(0 0 50% 0) and inset(50% 0 0 0) respectively to show only the top half and the bottom half, each with keyframes translateX(∓35%) to 0)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx188">`, preview text "Become One". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Merge".

### JavaScript — `FX[188]` from `site/fx.js`

```js
188(s,x){const w=el('div','mg');const sz=Math.min(13,60/chars(x).length);const a=T(x,sz),b=T(x,sz);a.classList.add('a');b.classList.add('b');w.append(a,b);s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx188` rules from `site/fx.css`

_No dedicated `.fx188` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #188
