# 055 · Text Tunnel — 文字隧道

Pass through the middle of the text

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Transitions, Headline · Hero
- Style / keywords: 3D Spatial Rotation
- Tag: Opening·Sci-Fi
- Example text: "Pass Through" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Tunnel (文字隧道)" motion effect: Multiple layered copies of the same word continuously scale up from tiny at the center, growing larger until they rush out of the frame and fade, one layer after another, like passing through a text tunnel, adjacent layers alternating between two color tones. About 3.6 seconds per layer.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx55">`, preview text "Pass Through". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Tunnel".

### JavaScript — `FX[55]` from `site/fx.js`

```js
55(s,x){for(let i=0;i<7;i++){const l=el('div','tl');l.innerHTML=`<span>${x}</span>`;l.style.animationDelay=(-i*3.6/7)+'s';s.append(l)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx55` rules from `site/fx.css`

```css
.fx55 .tl,.fx58 .tl{position:absolute;left:50%;top:50%;width:0;height:0;display:grid;place-items:center;animation:tun 3.6s linear infinite}
.fx55 .tl span{font-weight:900;font-size:11cqw;white-space:nowrap;color:#fff}
.fx55 .tl:nth-child(even) span{color:var(--a)}
@keyframes tun{0%{transform:scale(.04);opacity:0}25%{opacity:1}100%{transform:scale(9);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #55
