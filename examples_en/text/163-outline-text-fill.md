# 163 · Outline Text Fill — 空心字填滿

Hovering over hollow large text fills it solid from left to right

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, UI Interaction
- Style / keywords: Hollow Text Outline Fill Big Type outline stroke text fill hover hover Hover Mouse Enter Hover Interaction
- Tag: background-clip
- Example text: "DESIGN MOTION PLAY" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Outline Text Fill (空心字填滿)" motion effect: A few lines of extra-large hollow outline text: when the mouse moves over a line, that line fills in to solid from left to right (like ink pouring in), and when the mouse moves away, it retreats back to hollow from right to left; about 0.6 seconds, ease-in-out, suited to portfolio headings or menus. (CSS: the text uses -webkit-text-stroke for the outline, color:transparent; the background uses a solid-color linear-gradient with background-clip:text, and on hover, background-size 0%→100% with a transition)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx163">`, preview text "DESIGN MOTION PLAY". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Outline Text Fill".

### JavaScript — `FX[163]` from `site/fx.js`

```js
163(s,x,card){const w=el('div','ofw');const its=words(x).slice(0,3).map(v=>{const d=el('div','ofl');d.textContent=v;w.append(d);return d});w.style.fontSize=Math.min(12,64/Math.max(...words(x).slice(0,3).map(v=>chars(v).length)))+'cqw';s.append(w);autoHover(w,its,card,1100)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx163` rules from `site/fx.css`

_No dedicated `.fx163` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #163
