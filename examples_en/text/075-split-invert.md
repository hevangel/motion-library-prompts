# 075 · Split Invert — 斜線反轉

A diagonal line sweeps across and the two areas swap

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Transitions
- Style / keywords: Text Switching Canva Style Canva Block Block
- Tag: Switching·Title
- Example text: "Invert" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Split Invert (斜線反轉)" motion effect: The frame is divided into two areas by a diagonal line, the two areas' background and text colors in contrast with each other; the diagonal line sweeps across the frame from left to right, swapping the text's two color schemes. One sweep about every 3.4 seconds, with a title-switching feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx75">`, preview text "Invert". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Split Invert".

### JavaScript — `FX[75]` from `site/fx.js`

```js
75(s,x){const a=el('div','lay');a.append(T(x,24));const b=el('div','lay b');b.append(T(x,24));s.append(a,b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx75` rules from `site/fx.css`

```css
.fx75 .lay{position:absolute;inset:0;display:grid;place-items:center;background:#fff;color:#111}
.fx75 .lay.b{background:#2b2b2b;color:var(--a);animation:si 3.4s infinite cubic-bezier(.7,0,.3,1)}
@keyframes si{0%{clip-path:polygon(0 0,0% 0,-25% 100%,0 100%)}40%,60%{clip-path:polygon(0 0,62% 0,38% 100%,0 100%)}100%{clip-path:polygon(0 0,130% 0,105% 100%,0 100%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #75
