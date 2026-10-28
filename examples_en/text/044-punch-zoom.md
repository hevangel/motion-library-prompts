# 044 · Punch Zoom — 衝擊放大

Flies out from deep inside, trailing afterimages behind it

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Impact Entrance
- Tag: Opening·Emphasis
- Example text: "Breakthrough" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Punch Zoom (衝擊放大)" motion effect: The text rushes forward at high speed from deep in the frame (tiny and blurred), overshooting slightly as it enlarges before rebounding into place, trailing 4 layers of semi-transparent afterimages behind it. About 2.2 seconds per cycle, with a strong opening emphasis.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx44">`, preview text "Breakthrough". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Punch Zoom".

### JavaScript — `FX[44]` from `site/fx.js`

```js
44(s,x){const w=el('div','w');for(let k=4;k>=1;k--){const g=T(x,18);g.classList.add('g');g.style.setProperty('--op',(.55/k).toFixed(2));g.style.setProperty('--d',(k*.05)+'s');w.append(g)}w.append(T(x,18));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx44` rules from `site/fx.css`

```css
.fx44 .w{position:relative}
.fx44 .t{color:#fff;animation:pz 2.2s var(--d,0s) infinite both cubic-bezier(.2,.9,.3,1.2)}
.fx44 .g{position:absolute;left:0;top:0;color:var(--a);opacity:var(--op)}
@keyframes pz{0%{transform:scale(.05);opacity:0;filter:blur(6px)}28%{transform:scale(1.14);filter:none;opacity:1}36%,84%{transform:scale(1);opacity:1}100%{transform:scale(1);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #44
