# 058 · Ring Text Tunnel — 圓環隧道

Rings of text rush toward you

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Transitions, Background Decoration
- Style / keywords: 3D Spatial Rotation
- Tag: Opening·Sci-Fi
- Example text: "TUNNEL•" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Ring Text Tunnel (圓環隧道)" motion effect: Multiple rings made of text scale up one by one from tiny at the center, rushing toward the viewer and fading out, each ring itself also rotating, adjacent rings in opposite directions. About 4.2 seconds per ring.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx58">`, preview text "TUNNEL•". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Ring Text Tunnel".

### JavaScript — `FX[58]` from `site/fx.js`

```js
58(s,x){for(let i=0;i<6;i++){const l=el('div','tl');l.append(ringOf(rep(x,Math.max(1,Math.round(16/chars(x).length))),9,2.4,i%2?'cw':'ccw'));l.querySelector('.ring2').style.position='static';l.style.animationDelay=(-i*4.2/6)+'s';s.append(l)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx58` rules from `site/fx.css`

```css
.fx55 .tl,.fx58 .tl{position:absolute;left:50%;top:50%;width:0;height:0;display:grid;place-items:center;animation:tun 3.6s linear infinite}
.fx58 .tl{animation-duration:4.2s}
.fx58 .tl:nth-child(even) .ring2 span{color:var(--a)}
@keyframes tun{0%{transform:scale(.04);opacity:0}25%{opacity:1}100%{transform:scale(9);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #58
