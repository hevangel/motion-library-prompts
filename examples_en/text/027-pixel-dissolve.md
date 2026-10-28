# 027 · Pixel Dissolve — 像素溶解

Turns into blocks, dissolves away, then restores

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Transitions
- Style / keywords: Dissipating Exit
- Tag: Digital
- Example text: "Pixelated" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Pixel Dissolve (像素溶解)" motion effect: The text is covered with small squares on top of it; the squares appear randomly, one by one, to hide the text, then disappear one by one to bring the text back, with a few accent-colored squares mixed in, like a pixel dissolve. About 3 seconds per cycle, with a digital feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx27">`, preview text "Pixelated". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Pixel Dissolve".

### JavaScript — `FX[27]` from `site/fx.js`

```js
27(s,x){s.append(T(x));const px=el('div','px');for(let i=0;i<24*14;i++){const c=el('i',Math.random()<.12?'k':(Math.random()<.06?'h':''));c.style.setProperty('--d',(Math.random()*.9).toFixed(2)+'s');px.append(c)}s.append(px)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx27` rules from `site/fx.css`

```css
.fx27 .px{position:absolute;inset:0;display:grid;grid-template-columns:repeat(24,1fr);grid-template-rows:repeat(14,1fr)}
.fx27 .px i{background:var(--cream);opacity:0;animation:pix 3s var(--d) infinite steps(1)}
.fx27 .px i.k{background:#111}
.fx27 .px i.h{background:var(--a)}
@keyframes pix{0%,25%{opacity:0}40%,60%{opacity:1}75%,100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #27
