# 137 · Flowing Connectors — 流程連線流動

Dashed connectors between nodes keep flowing, with small dots traveling along the lines

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Numbers & Data, Background Decoration
- Style / keywords: Flowchart Architecture Diagram Node Connector Dashed Line Flow Data Flow Flow Diagram Connector Dashed Line Data Flow
- Tag: stroke-dashoffset
- Example text: "User Frontend Backend Database" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Flowing Connectors (流程連線流動)" motion effect: In a flowchart or system architecture diagram, the nodes (circles + labels underneath) are connected with smooth curves; the connectors are dashed lines whose dashes keep moving in the direction of the data flow, and small dots also travel back and forth along each connector, expressing that data is flowing; the speed is steady and loops without stopping. (CSS: set stroke-dasharray on the paths and use keyframes to continuously change stroke-dashoffset; the small dots use SVG animateMotion or CSS offset-path to move along the same path, each with an offset start time)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx137">`, preview text "User Frontend Backend Database". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flowing Connectors".

### JavaScript — `FX[137]` from `site/fx.js`

```js
137(s,x){const ws=words(x);const N=[[25,45],[80,20],[80,70],[135,45]];const P=['M34,45 C52,45 56,20 71,20','M34,45 C52,45 56,70 71,70','M89,20 C104,20 108,45 126,45','M89,70 C104,70 108,45 126,45'];
  s.insertAdjacentHTML('beforeend',`<svg class="flow" viewBox="0 0 160 90">${P.map((d,i)=>`<path d="${d}"/><circle class="mv" r="1.8"><animateMotion dur="2.2s" begin="${-i*.55}s" repeatCount="indefinite" path="${d}"/></circle>`).join('')}${N.map(([cx,cy])=>`<circle class="nd" cx="${cx}" cy="${cy}" r="9"/>`).join('')}${N.map(([cx,cy],i)=>`<text x="${cx}" y="${cy+17}"></text>`).join('')}</svg>`);
  s.querySelectorAll('.flow text').forEach((t,i)=>t.textContent=ws[i%ws.length])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx137` rules from `site/fx.css`

_No dedicated `.fx137` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #137
