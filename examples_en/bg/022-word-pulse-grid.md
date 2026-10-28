# 022 · Word Pulse Grid — 脈動格子

A grid of text expands with a wave

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Background · Rhythm
- Example text: "Pulse" (stage background: acc, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Word Pulse Grid (脈動格子)" motion effect: The same character is arranged in an 8×4 grid, expanding in sequence in rings from the center outward, brightening, then shrinking and dimming again, forming a pulsing ripple. About 1.8 seconds per wave, with a rhythmic background feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx22">`, preview text "Pulse". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Word Pulse Grid".

### JavaScript — `FX[22]` from `site/fx.js`

```js
22(s,x){const g=el('div','g');for(let r=0;r<4;r++)for(let c=0;c<8;c++){const sp=el('span');sp.textContent=chars(x)[0];sp.style.setProperty('--d',Math.hypot(c-3.5,(r-1.5)*1.6).toFixed(2));g.append(sp)}s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx22` rules from `site/fx.css`

```css
.fx22 .g{display:grid;grid-template-columns:repeat(8,1fr);gap:1.4cqw 3cqw}
.fx22 .g span{font-weight:900;font-size:6.5cqw;color:#1b1340;animation:pg 1.8s calc(var(--d)*.13s) ease-in-out infinite}
@keyframes pg{0%,100%{transform:scale(.55);opacity:.35}45%{transform:scale(1.2);opacity:1;color:#fff}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #22
