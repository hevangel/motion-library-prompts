# 031 · Roller Path — ∞ 軌道

Text races along an ∞ track

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Racing · Joyful
- Example text: "Rolling" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Roller Path (∞ 軌道)" motion effect: Each character runs in sequence along a dashed “∞”-shaped track, turning to follow its direction of travel, linked head-to-tail like a little convoy. About 4.5 seconds per lap, with a joyful racing feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx31">`, preview text "Rolling". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Roller Path".

### JavaScript — `FX[31]` from `site/fx.js`

```js
31(s,x){const P='M160,90 C200,30 280,30 280,90 C280,150 200,150 160,90 C120,30 40,30 40,90 C40,150 120,150 160,90 Z';const cs=chars(x);
  s.insertAdjacentHTML('beforeend',`<svg viewBox="0 0 320 180"><path d="${P}" fill="none" stroke="#111" stroke-opacity=".25" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>${cs.map((c,i)=>`<text font-size="30" font-weight="900" text-anchor="middle" dy="10" fill="${i%2?'#111':'var(--a)'}">${c}<animateMotion dur="4.5s" repeatCount="indefinite" rotate="auto" begin="${-(cs.length-i)*0.22}s" path="${P}"/></text>`).join('')}</svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx31` rules from `site/fx.css`

```css
.fx31 svg{width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #31
