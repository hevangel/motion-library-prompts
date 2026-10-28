# 305 · Border Spotlight Grid — 邊框聚光網格

As the cursor moves among a group of cards, the borders and interiors of the cards near it are lit up by a pool of light

- Component: Cards · Groups (`card`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Headline · Hero
- Style / keywords: Border Spotlight Glow Grid Feature Introduction SaaS Linear Border Spotlight Glow Grid Feature Cards Cards Group
- Tag: radial-gradient
- Example text: "Speed Security Collaboration Integration Analytics Support" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Border Spotlight Grid (邊框聚光網格)" motion effect: A set of cards in a feature-introduction section arranged in a grid, each card's border a fine ring: as the cursor moves within the whole section, each card draws a soft pool of light at "the cursor's position relative to itself", so the borders of cards close to the cursor are lit up in the accent color and their interiors also carry a faint glow, while cards farther away barely light up at all; as the cursor moves between cards, the light naturally crosses the borders of neighboring cards. (CSS: the card's outer layer uses 1px of padding as the border, with background radial-gradient(circle at var(--x) var(--y), accent color, transparent); the inner layer uses another, fainter radial-gradient; on mousemove over the container, JS computes the relative coordinates for each card and writes them into --x and --y)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx305">`, preview text "Speed Security Collaboration Integration Analytics Support". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Border Spotlight Grid".

### JavaScript — `FX[305]` from `site/fx.js`

```js
305(s,x,card){const ws=words(x);const g=el('div','abs gl cg-bs');const gr=el('div','cg-bg');const cs=[0,1,2,3,4,5].map(i=>{const c=el('div','cg-bc');c.innerHTML='<div class="cg-bi"><i></i><b></b><small>滑過看看邊框光</small></div>';c.querySelector('b').textContent=ws[i%ws.length];gr.append(c);return c});g.append(gr);s.append(g);
  vpointer(g,card,(px,py)=>{const q=g.getBoundingClientRect();cs.forEach(c=>{const r=c.getBoundingClientRect();c.style.setProperty('--x',(px-(r.left-q.left))+'px');c.style.setProperty('--y',(py-(r.top-q.top))+'px')})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx305` rules from `site/fx.css`

_No dedicated `.fx305` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #305
