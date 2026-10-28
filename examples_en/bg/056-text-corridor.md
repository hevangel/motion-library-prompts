# 056 · Text Corridor — 文字走廊

Floor and walls are all text, moving forward all the way

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Headline · Hero
- Style / keywords: 3D Spatial Rotation
- Tag: Immersive·MV
- Example text: "Forward" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Corridor (文字走廊)" motion effect: A corridor in 3D perspective, its floor, ceiling, and left and right walls all covered in repeated text, the text continuously flowing toward the viewer, with a dark gradient at the vanishing point in the center. About 6 seconds per cycle, an immersive forward-moving feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx56">`, preview text "Forward". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Corridor".

### JavaScript — `FX[56]` from `site/fx.js`

```js
56(s,x){const u=rep(x+'　',14);const rows=Array(28).fill(`<div style="white-space:nowrap;font-weight:900;font-size:6cqw;line-height:1.3">${u}</div>`).join('');
  const P=(tf,w,h,anim)=>`<div style="position:absolute;left:50%;top:50%;width:${w}cqw;height:${h}cqw;margin:${-h/2}cqw 0 0 ${-w/2}cqw;transform:${tf};overflow:hidden;background:var(--a);color:#111"><div style="animation:${anim}">${rows}${rows}</div></div>`;
  s.insertAdjacentHTML('beforeend',`<div style="position:absolute;inset:0;perspective:30cqw;transform-style:preserve-3d">
  ${P('translateY(13cqw) translateZ(-138cqw) rotateX(90deg)',52,300,'mqv 6s linear infinite reverse')}
  ${P('translateY(-13cqw) translateZ(-138cqw) rotateX(-90deg)',52,300,'mqv 6s linear infinite reverse')}
  ${P('translateX(-26cqw) translateZ(-138cqw) rotateY(90deg)',300,26,'mq 6s linear infinite')}
  ${P('translateX(26cqw) translateZ(-138cqw) rotateY(-90deg)',300,26,'mq 6s linear infinite reverse')}
  </div><div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,#111 0 4%,#1116 12%,transparent 30%)"></div>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx56` rules from `site/fx.css`

```css
.fx51 svg,.fx56 svg{width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #56
