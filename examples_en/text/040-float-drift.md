# 040 · Float Drift — 漂浮

Floats light and airy

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Logo · Brand
- Style / keywords: Letter-by-Letter Motion
- Tag: Healing · Dreamy
- Example text: "Fluffy" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Float Drift (漂浮)" motion effect: Each character floats slowly up, down, left and right at a different speed and rotates slightly, with a soft glow, like a feather drifting lightly. About 3–4.5 seconds per cycle for each character, with a soothing, dreamy feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx40">`, preview text "Fluffy". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Float Drift".

### JavaScript — `FX[40]` from `site/fx.js`

```js
40(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>c.style.setProperty('--dur',rnd(2.8,4.4).toFixed(2)+'s'));s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx40` rules from `site/fx.css`

```css
.fx40 .c{animation:flo var(--dur) calc(var(--i)*-.7s) ease-in-out infinite;text-shadow:0 0 12px #fff6}
.fx40 .c:nth-child(even){color:var(--a)}
@keyframes flo{0%,100%{transform:translate(0,0) rotate(-4deg)}33%{transform:translate(4%,-14%) rotate(4deg)}66%{transform:translate(-3%,-5%) rotate(-1deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #40
