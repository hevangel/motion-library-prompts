# 061 · Extrude Text — 立體字

The thickness of 3D letters rotates a full turn

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Logo · Brand, Headline · Hero
- Style / keywords: 3D Spatial Rotation
- Tag: Title
- Example text: "3D" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Extrude Text (立體字)" motion effect: Thick 3D extruded text, its front brighter and its sides built from multiple layers of shading from dark to light to form the thickness; the whole set of letters slowly rotates a full turn around a vertical axis, letting the side thickness be seen. About 5 seconds per revolution.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx61">`, preview text "3D". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Extrude Text".

### JavaScript — `FX[61]` from `site/fx.js`

```js
61(s,x){const e=el('div','ex');for(let i=14;i>=1;i--){const l=T(x,20);l.classList.add('l');l.style.transform=`translateZ(${-i*.45}cqw)`;l.style.color=`hsl(15 60% ${12+i*.6}%)`;e.append(l)}const f=T(x,20);f.style.color='#fff';e.append(f);s.append(e)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx61` rules from `site/fx.css`

```css
.fx61 .ex{position:relative;transform-style:preserve-3d;animation:exr 5s linear infinite}
.fx61 .ex .t{color:var(--a)}
.fx61 .ex .t.l{position:absolute;left:0;top:0}
@keyframes exr{from{transform:rotateX(12deg) rotateY(0)}to{transform:rotateX(12deg) rotateY(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #61
