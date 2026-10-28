# 113 · Spotlight Card — 光暈邊框卡片

As the cursor passes, the card's border and interior are lit by a pool of light

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Card Glow Border Spotlight Cursor Glow Spotlight Card Glow Border Linear Vercel
- Tag: radial-gradient
- Example text: "Design Development Marketing" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Spotlight Card (光暈邊框卡片)" motion effect: A row of understated cards: when the cursor moves near a card, the stretch of the card's border closest to the cursor is lit by a pool of light (in the accent color), and inside the card there is also a very faint glow following the cursor; the light only illuminates the area near the cursor and gets darker the farther away it is, so the edges of neighboring cards can also be seen faintly lit at the same time. (How it works: on mousemove, calculate the cursor's coordinates relative to each card and write them into --x and --y; ::before uses radial-gradient(circle at var(--x) var(--y)) with mask-composite to show only the border ring, and ::after creates the soft interior glow)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx113">`, preview text "Design Development Marketing". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Spotlight Card".

### JavaScript — `FX[113]` from `site/fx.js`

```js
113(s,x,card){const l=el('div','abs gl');const w=el('div','spw');const ws=words(x);const cs=[0,1,2].map(i=>{const c=el('div','spc');c.innerHTML='<i></i><b></b><span></span><span class="s"></span>';c.querySelector('b').textContent=ws[i%ws.length];w.append(c);return c});l.append(w);s.append(l);
  vpointer(l,card,(px,py)=>cs.forEach(c=>{c.style.setProperty('--x',px-c.offsetLeft+'px');c.style.setProperty('--y',py-c.offsetTop+'px')}))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx113` rules from `site/fx.css`

_No dedicated `.fx113` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #113
