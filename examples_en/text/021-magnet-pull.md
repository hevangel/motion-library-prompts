# 021 · Magnet Pull — 磁鐵吸附

Text is pulled in as if by a magnet

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Logo · Brand, Headline · Hero
- Style / keywords: Impact Entrance
- Tag: Focus · Logo
- Example text: "Drawn In" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Magnet Pull (磁鐵吸附)" motion effect: The text starts spread far apart, blurred and semi-transparent, then, as if pulled in by a magnet, accelerates toward the center, overshoots slightly, and snaps into place; after a pause it spreads apart again. The last two characters use an accent color as the focal point. About 2.8 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx21">`, preview text "Drawn In". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Magnet Pull".

### JavaScript — `FX[21]` from `site/fx.js`

```js
21(s,x){const t=split(x);const cs=t.querySelectorAll('.c');const mid=(cs.length-1)/2;cs.forEach((c,i)=>c.style.setProperty('--o',(i-mid)));s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx21` rules from `site/fx.css`

```css
.fx21 .c{color:#888;animation:mag 2.8s infinite}
.fx21 .c:nth-last-child(-n+2){color:var(--a)}
@keyframes mag{0%,8%{transform:translateX(calc(var(--o)*16cqw)) scale(.75);filter:blur(3px);opacity:.25;animation-timing-function:cubic-bezier(.7,0,1,.6)}48%{transform:translateX(calc(var(--o)*-.8cqw)) scale(1.05);filter:none;opacity:1}55%,82%{transform:none;filter:none;opacity:1}100%{transform:translateX(calc(var(--o)*16cqw)) scale(.75);filter:blur(3px);opacity:.25}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #21
