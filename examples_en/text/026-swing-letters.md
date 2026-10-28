# 026 · Swing Letters — 鐘擺搖晃

Swings like a pendulum from a point above

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Logo · Brand
- Style / keywords: Letter-by-Letter Motion
- Tag: Cute · Lazy
- Example text: "Swaying" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Swing Letters (鐘擺搖晃)" motion effect: Each character has a small dot at its top, and the character swings left and right like a pendulum from that pivot point by about ±14 degrees, with each character's swinging offset from the others. About 1.7 seconds per swing, lazy and cute.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx26">`, preview text "Swaying". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Swing Letters".

### JavaScript — `FX[26]` from `site/fx.js`

```js
26(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx26` rules from `site/fx.css`

```css
.fx26 .c{transform-origin:50% -18%;animation:sw 1.7s calc(var(--i)*-.27s) ease-in-out infinite;position:relative}
.fx26 .c::before{content:"";position:absolute;left:50%;top:-22%;width:1cqw;height:1cqw;margin-left:-.5cqw;border-radius:50%;background:#111}
.fx26 .c:nth-child(even){color:#fff}
@keyframes sw{0%,100%{transform:rotate(14deg)}50%{transform:rotate(-14deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #26
