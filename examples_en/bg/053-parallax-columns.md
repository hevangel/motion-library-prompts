# 053 · Parallax Columns — 直書三層

Three layers of vertical text flowing together

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Night·Eastern
- Example text: "Rainy Night Street Lights" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Parallax Columns (直書三層)" motion effect: Three layers of vertical text flowing vertically: the back layer is small, very faint, and fast; the middle layer is semi-transparent at medium speed; the front layer is large, opaque, and slow, creating a parallax depth of field, in a serif (Mincho) typeface. A nighttime Eastern feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx53">`, preview text "Rainy Night Street Lights". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Parallax Columns".

### JavaScript — `FX[53]` from `site/fx.js`

```js
53(s,x){[[9,'#0001',6,5],[6,'#0004',10,8],[3,'#111',16,13]].forEach(([n,c,d,f])=>{const l=el('div','lay');for(let i=0;i<n;i++){const e=el('div','col');e.innerHTML=chars(rep(x,6)).join('<br>');e.style.cssText+=`;color:${c};font-size:${f}cqw;--dur:${d+i%3}s`;if(i%2)e.style.animationDirection='reverse';l.append(e)}s.append(l)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx53` rules from `site/fx.css`

```css
.fx53 .lay{position:absolute;inset:0;display:flex;justify-content:space-around;overflow:hidden}
.fx53 .col{align-self:flex-start;text-align:center;font-family:"Noto Serif JP",serif;font-weight:900;line-height:1;animation:mqv var(--dur) linear infinite}
@keyframes mqv{to{transform:translateY(-50%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #53
