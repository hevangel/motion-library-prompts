# 024 · Text Fan — 文字扇

The same character opens out like a fan

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Logo · Brand, Headline · Hero
- Style / keywords: 3D Spatial Rotation
- Tag: Japanese Style · Entrance
- Example text: "Fan" (stage background: dark, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Fan (文字扇)" motion effect: The same character is copied 7 times and stacked together, opening out into a fan shape pivoting below the character, pausing, then folding closed again. The center copy is opaque and the rest are semi-transparent. About 3 seconds per cycle, with a Japanese-style entrance feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx24">`, preview text "Fan". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Fan".

### JavaScript — `FX[24]` from `site/fx.js`

```js
24(s,x){const w=el('div','w');const ch=chars(x)[0];for(let i=0;i<7;i++){const sp=el('span');sp.textContent=ch;sp.style.setProperty('--a2',(i-3)*24+'deg');sp.style.opacity=i===3?1:.45+Math.abs(3-i)*-.08+.25;if(i!==3)sp.style.color='var(--a)';sp.style.zIndex=i===3?2:1;w.append(sp)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx24` rules from `site/fx.css`

```css
.fx24 .w{position:relative;width:1px;height:1px}
.fx24 .w span{position:absolute;left:0;top:0;font-weight:900;font-size:17cqw;line-height:1;transform-origin:50% 140%;translate:-50% -60%;animation:fan 3s ease-in-out infinite;color:#fff}
@keyframes fan{0%,12%{transform:rotate(0)}45%,80%{transform:rotate(var(--a2))}100%{transform:rotate(0)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #24
