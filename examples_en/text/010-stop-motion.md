# 010 · Stop Motion — 定格晃動

Shakes frame by frame, like stop-motion animation

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Letter-by-Letter Motion
- Tag: Handmade · Toy
- Example text: "Stop Motion" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Stop Motion (定格晃動)" motion effect: Each character trembles and rotates slightly at random in a discontinuous, frame-by-frame jumping manner (like stop-motion animation, with no smooth transitions), with each character offset in rhythm from the others. About a 0.9-second loop, with a handmade toy feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx10">`, preview text "Stop Motion". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Stop Motion".

### JavaScript — `FX[10]` from `site/fx.js`

```js
10(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx10` rules from `site/fx.css`

```css
.fx10 .c{animation:stp .9s calc(var(--i)*-.23s) infinite steps(1)}
@keyframes stp{0%{transform:rotate(-6deg) translate(2%,-4%)}25%{transform:rotate(4deg) translate(-3%,3%)}50%{transform:rotate(-2deg) translate(2%,5%)}75%{transform:rotate(7deg) translate(-2%,-2%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #10
