# 052 · Marquee — 跑馬燈

Bands with different fonts and speeds layered together

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Numbers & Data
- Style / keywords: Flowing Background
- Tag: Announcement·Street
- Example text: "Limited Sale New Arrivals Pre-order Last Day" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Marquee (跑馬燈)" motion effect: Four horizontal marquee bands layered together, each with a different font, font size, speed, and direction, with thin divider lines between the bands. Speeds vary from 5–11 seconds per cycle, like a street bulletin board.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx52">`, preview text "Limited Sale New Arrivals Pre-order Last Day". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Marquee".

### JavaScript — `FX[52]` from `site/fx.js`

```js
52(s,x){const r=el('div','rows');const ws=words(x);const F=['"Noto Sans JP"','"Zen Maru Gothic"','"Noto Serif JP"','"Reggae One"'];const sz=[6,9,5,8],du=[7,11,5,9];for(let i=0;i<4;i++){const w=ws[i%ws.length];r.append(mqRow(rep(w+'・',10),sz[i],du[i],i%2,`font-family:${F[i]}`))}s.append(r)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx52` rules from `site/fx.css`

```css
.fx52 .rows{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center}
.fx52 .mq{border-bottom:.3cqw solid #111;color:#111;font-weight:900;line-height:1.25}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #52
