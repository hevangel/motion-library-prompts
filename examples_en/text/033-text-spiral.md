# 033 · Text Spiral — 文字漩渦

Text rotates along a spiral

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Transitions
- Style / keywords: 3D Spatial Rotation
- Tag: Fantasy · Drawn In
- Example text: "Spiral" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Spiral (文字漩渦)" motion effect: Text is arranged along a spiral line, gradually growing larger from small characters at the center outward; the whole vortex keeps rotating, and the characters' opacity alternates between bright and dark in turn. About 9 seconds per revolution, with a fantastical drawn-in feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx33">`, preview text "Spiral". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Spiral".

### JavaScript — `FX[33]` from `site/fx.js`

```js
33(s,x){const sp=el('div','sp');const cs=chars(x);for(let i=0;i<46;i++){const e=el('span');e.textContent=cs[i%cs.length];const a=i*.48,r=2.5+i*.85;e.style.fontSize=(1.6+i*.09)+'cqw';e.style.transform=`rotate(${a}rad) translate(${r}cqw,0) rotate(90deg)`;e.style.color=i%3?'#fff':'var(--a)';e.style.animationDelay=(-i*.15)+'s';sp.append(e)}s.append(sp)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx33` rules from `site/fx.css`

```css
.fx33 .sp{position:absolute;left:50%;top:50%;width:0;height:0;animation:spin 9s linear infinite}
.fx33 .sp span{position:absolute;left:0;top:0;font-weight:900;transform-origin:0 0;line-height:1;animation:sin 9s linear infinite}
@keyframes sin{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes spin{to{transform:rotate(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #33
