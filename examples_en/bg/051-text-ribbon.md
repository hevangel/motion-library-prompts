# 051 · Text Ribbon — 緞帶

Text flows along a wavy line

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Decoration·Soundtrack Feel
- Example text: "Move to the Beat" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Ribbon (緞帶)" motion effect: A wide, semi-transparent wavy ribbon crosses the frame, and text continuously flows forward along the wavy curve. It flows through a segment in about 2.4 seconds, with a decorative, musical rhythm.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx51">`, preview text "Move to the Beat". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Ribbon".

### JavaScript — `FX[51]` from `site/fx.js`

```js
51(s,x){const id='rb'+Math.random().toString(36).slice(2);const unit=x+'・';const L=chars(unit).length*18;const P='M-30,130 C40,40 110,40 160,95 S270,150 350,55';
  s.insertAdjacentHTML('beforeend',`<svg viewBox="0 0 320 180"><path id="${id}" d="${P}" fill="none" stroke="#ffffff12" stroke-width="34"/><text font-size="18" font-weight="900" fill="#fff" dy="6"><textPath href="#${id}" startOffset="0">${rep(unit,9)}<animate attributeName="startOffset" from="${-L}" to="0" dur="2.4s" repeatCount="indefinite"/></textPath></text></svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx51` rules from `site/fx.css`

```css
.fx51 svg,.fx56 svg{width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #51
